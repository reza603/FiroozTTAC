const db = require("../models");
const Order_product = db.order;
const Op = db.Sequelize.Op;
const config = require("../config/db.config");
const { QueryTypes } = require("sequelize");
const { order_product } = require("../models");

// Create and Save a new Order_product
exports.create = (req, res) => {
  // Validate request
  if (!req.body.Orderid) {
    res.status(400).send({
      message: "Content can not be empty!",
    });
    return;
  }

  // Create a Order_product
  const Order_Product = {
    orderid: req.body.orderid,
    gtin: req.body.gtin,
  };

  // Save Order_product in the database
  Order_Product.create(order_product)
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating the OrderProduct.",
      });
    });
};

// Retrieve all OrderProducts from the database.
// exports.findAll = (req, res) => {
//   const orderid = req.query.orderid;
//   console.log('Orderid is: '+orderid);
//   var condition = orderid ? { orderid: { [Op.like]: `%${orderid}%` } } : null;

//   Order_product.findAll({ where: condition })
//     .then((data) => {
//       res.send(data);
//     })
//     .catch((err) => {
//       res.status(500).send({
//         message: err.message || "Some error occurred while retrieving orderProductss.",
//       });
//     });
// };

// Find a single OrderProduct with an id

exports.findAll = (req, res) => {
  const orderid = req.query["orderid"];
  var condition = orderid ? { orderid: { [Op.like]: `%${orderid}%` } } : null;

  order_product
    .findAll({ where: condition })
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message: err.message || "Some error occurred while retrieving orders.",
      });
    });
};

exports.findAllWithJoinProducts = async (req, res) => {
  const _orderid = req.query["orderid"];
  var _sql = (_orderid != null)
    ? "SELECT w.id,w.orderid,w.gtin,p.productfrname FROM WarehouseOrderProducts w LEFT JOIN Products p ON w.gtin = p.gtin  WHERE orderid  =:orderid "
    : " SELECT w.id,w.orderid,w.gtin,p.productfrname FROM WarehouseOrderProducts w LEFT JOIN Products p ON w.gtin = p.gtin -- WHERE orderid  =:orderid";

  const Sequelize = require("sequelize");

  const sequelize = new Sequelize(config.DB, config.USER, config.PASSWORD, {
    host: config.HOST,
    dialect: config.dialect,

    pool: {
      max: 5,
      min: 0,
      acquire: 30000,
      idle: 10000,
    },
    operatorsAliases: false,
  });

  await sequelize
    .query(
      _sql,
      {
        replacements: { orderid: _orderid },
        type: QueryTypes.SELECT,
      }
    )
    .then((data) => {
      res.send(data);
    })
    .catch((err) =>
      res.status(500).send({
        message: err.message,
      })
    );

};

exports.findOne = (req, res) => {
  const id = req.params.id;

  Order_product.findByPk(id)
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message: "Error retrieving OrderProduct with id=" + id,
      });
    });
};

// Find a single OrderProduct with an id
exports.findOneCount = async (req, res) => {
  const _orderid = req.body.orderid;

  const Sequelize = require("sequelize");

  const sequelize = new Sequelize(config.DB, config.USER, config.PASSWORD, {
    host: config.HOST,
    dialect: config.dialect,

    pool: {
      max: 5,
      min: 0,
      acquire: 30000,
      idle: 10000,
    },
    operatorsAliases: false,
  });

  await sequelize
    .query(
      "SELECT COUNT(0) as qty FROM WarehouseOrderProducts WHERE orderid = :orderid",
      {
        replacements: { orderid: _orderid },
        type: QueryTypes.SELECT,
      }
    )
    .then((data) => {
      res.send(data);
    })
    .catch((err) =>
      res.status(500).send({
        message:
          "Error retrieving OrderProduct count with id=" +
          id +
          ": " +
          err.message,
      })
    );
};

// Update an existing Order_product by the id in the request
exports.update = (req, res) => {
  const id = req.params.id;

  Order_Product.update(req.body, {
    where: { id: id },
  })
    .then((num) => {
      if (num == 1) {
        res.send({
          message: "Order_product was updated successfully.",
        });
      } else {
        res.send({
          message: `Cannot update OrderProduct with id=${id}. Maybe Order_product was not found or req.body is empty!`,
        });
      }
    })
    .catch((err) => {
      res.status(500).send({
        message: "Error updating OrderProduct with id=" + id,
      });
    });
};

// Delete an Order_product with the specified id in the request
exports.delete = (req, res) => {
  const id = req.params.id;

  Order_Product.destroy({
    where: { id: id },
  })
    .then((num) => {
      if (num == 1) {
        res.send({
          message: "Order_product was deleted successfully!",
        });
      } else {
        res.send({
          message: `Cannot delete Order_product with id=${id}. Maybe Order_product was not found!`,
        });
      }
    })
    .catch((err) => {
      res.status(500).send({
        message: "Could not delete Order_product with id=" + id,
      });
    });
};

// Delete all Orders from the database.
exports.deleteAll = (req, res) => {
  Order_product.destroy({
    where: {},
    truncate: false,
  })
    .then((nums) => {
      res.send({
        message: `${nums} OrderProductss were deleted successfully!`,
      });
    })
    .catch((err) => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while removing all orders.",
      });
    });
};
