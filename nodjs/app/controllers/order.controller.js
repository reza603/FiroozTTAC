const db = require("../models");
const Order = db.orders;
const Op = db.Sequelize.Op;
const config = require("../config/db.config");
const { QueryTypes } = require("sequelize");

// Create and Save a new Order
exports.
  create = (req, res) => {
    // Validate request
    if (!req.body.Orderid) {
      res.status(400).send({
        message: "Content can not be empty!",
      });
      return;
    }

    // Create a Order
    const Order = {
      orderid: req.body.orderid,
      gtin: req.body.gtin,
      batchnumber: req.body.batchnumber,
      expdate: req.body.expdate,
      userid: req.body.userid,
      insertdate: req.body.insertdate,
      lastxmldate: req.body.lastxmldate,
      distributercompanynid: req.body.distributercompanynid,
      ordertype: req.body.ordertype,
      details: req.body.details,
    };

    // Save Order in the database
    Order.create(order)
      .then((data) => {
        res.send(data);
      })
      .catch((err) => {
        res.status(500).send({
          message: err.message || "Some error occurred while creating the Order.",
        });
      });
  };

// Retrieve all Orders from the database.
exports.findAll = (req, res) => {
  const orderid = req.query.orderid;
  var condition = orderid ? { orderid: { [Op.like]: `%${orderid}%` } } : null;

  Order.findAll({ where: condition })
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message: err.message || "Some error occurred while retrieving orders.",
      });
    });
};
exports.findAllByDeviceId = (req, res) => {
  const _deviceId = req.params.deviceid;
  console.log(`_deviceId: ${_deviceId}`);
  Order.findAll({ where: { deviceId: _deviceId } })
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving Orders."
      });
    });
};

exports.UpdateOneByDeviceId = (req, res) => {
  const _deviceId = req.params.deviceid;
  Order.findAll({ where: { deviceId: _deviceId } })
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving Orders."
      });
    });
};
// Find a single Order with an id
exports.findOne = (req, res) => {
  const id = req.params.id;

  Order.findByPk(id)
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message: "Error retrieving Order with id=" + id,
      });
    });
};

// Find a single Order with an id
exports.findOneCount = async (req, res) => {
  const _whorderid = req.body.whorderid;

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
      "SELECT COUNT(0) as qty FROM ongoingbarcodes WHERE whorderid = :whorderid AND LevelId = 0",
      {
        replacements: { whorderid: _whorderid },
        type: QueryTypes.SELECT,
      }
    )
    .then((data) => {
      res.send(data);
    })
    .catch((err) =>
      res.status(500).send({
        message:
          "Error retrieving Order count with id=" + id + ": " + err.message,
      })
    );
};

exports.findOneDistributerName = async (req, res) => {
  const id = req.params.id;
  let _companyName = "";
  let _nationalId = "";
  Order.findByPk(id).then(
    async (order) => {
      _nationalId = order.distributercompanynid;
      console.log("received id:" + id + " and nationalId:" + _nationalId);

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
          "SELECT CompanyFaName FROM Companies AS c WHERE c.NationalId = :NationalId",
          {
            replacements: { NationalId: _nationalId },
            type: QueryTypes.SELECT,
          }
        )
        .then((data) => {
          res.send(data);
        })
        .catch((err) =>
          res.status(500).send({
            message:
              "Error retrieving Order's distributer name with id=" +
              id +
              ": " +
              err.message,
          })
        );
    },
    (err) => {
      console.error(err);
    }
  ); //findByPk
};

// Update an existing Order by the id in the request
exports.update = (req, res) => {
  // const id = req.params.id;
  const _orderid = req.params.orderid;

  Order.update({ deviceid: req.body.deviceid }, {
    where: { orderid: _orderid },
  })
    .then((num) => {
      if (num == 1) {
        res.send({
          message: "Order was updated successfully.",
        });
      } else {
        res.send({
          message: `Cannot update Order with orderid=${_orderid}. Maybe Order was not found or req.body is empty!`,
        });
      }
    })
    .catch((err) => {
      res.status(500).send({
        message: "Error updating Order with id=" + _orderid + " \\n  " + err.message,
      });
    });
};

// Delete an Order with the specified id in the request
exports.delete = async (req, res) => {
  const _orderId = req.params.orderId;
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
  });//following function description: result = orderid => ok// result = -1 => edit mode but order does not exist// result = -2 => error  
  sql = "DECLARE @whOrderid VARCHAR(20) \n"
    + "SET @whOrderid = :whOrderid \n"
    + "SELECT @whOrderId = CASE ISNUMERIC(@whOrderid) \n"
    + "                         WHEN 0 THEN 0 \n"
    + "                         ELSE @whOrderid \n"
    + "                    END \n"
    + "IF EXISTS( \n"
    + "       SELECT 1 \n"
    + "       FROM   WareHouseOrders wo \n"
    + "       WHERE  wo.OrderId = @whOrderid \n"
    + "              AND LEN(wo.LastXMLDate) > 6 \n"
    + "   ) \n"
    + "BEGIN \n"
    + "    SELECT 'xmlgenerated' AS result \n"
    + "END \n"
    + "ELSE \n"
    + "BEGIN \n"
    + "    UPDATE OnGoingBarCodes \n"
    + "    SET    WhOrderId = NULL \n"
    + "    WHERE  WhOrderId = @whOrderid \n"
    + "     \n"
    + "    DELETE  \n"
    + "    FROM   WarehouseOrders \n"
    + "    WHERE  OrderId = @whOrderid \n"
    + "    SELECT 'ok' AS result \n"
    + "END \n";
  await sequelize
    .query(sql, {
      replacements: { whOrderid: _orderId },
      type: QueryTypes.INSERT,
    })
    .then((rows) => {
      console.log(rows);
      res.send(rows);
    })
    .catch((err) => {
      res.send(err);
      console.log(err);
    });

};

// Delete all Orders from the database.
exports.deleteAll = (req, res) => {
  Order.destroy({
    where: {},
    truncate: false,
  })
    .then((nums) => {
      res.send({ message: `${nums} Orders were deleted successfully!` });
    })
    .catch((err) => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while removing all orders.",
      });
    });
};

// find all published Order
exports.findAllPublished = (req, res) => {
  Order.findAll({ where: { published: true } })
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message: err.message || "Some error occurred while retrieving orders.",
      });
    });
};

// Update an existing Ongoingbarcode by the uuid in the request when scanning a specific  barcode
exports.Insert = async (req, res) => {
  const _orderid = req.body.orderid;
  const _distributerNid = req.body.distributernid;
  const _qty = req.body.qty;
  const _isNewOrder = req.body.isNewOrder;
  const _deviceId = req.body.deviceId;
  const _orderType = req.body.orderType;
  const _details = req.body.details;
  const _userId = req.body.userid;


  console.log("_deviceId value is " + _deviceId);
  console.log("_distributerNid value is " + _distributerNid);

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
  //following function description:
  //result = orderid => ok
  // result = -1 => edit mode but order does not exist
  // result = -2 => error
  sql = "BEGIN TRY \n"
    + "	DECLARE @qty                   INT, \n"
    + "	        @distributerNid        VARCHAR(11), \n"
    + "	        @deviceId        VARCHAR(20), \n"
    + "	        @orderid               INT, \n"
    + "	        @userid                INT, \n"
    + "	        @isOrderExist          BIT, \n"
    + "	        @isOrderLevelExist     BIT, \n"
    + "	        @isNewOrder            BIT, \n"
    + "         @orderType             VARCHAR(20), \n"
    + "         @details               VARCHAR(100) \n"
    + "	 \n"
    + "	SET @isNewOrder = :isNewOrder \n"
    + "	SET @orderid = :orderid \n"
    + "	SET @qty = :qty \n"
    + "	SET @distributerNid = :distributerNid \n"
    + "	SET @deviceId = :deviceId \n"
    + " SET @orderType = :orderType \n"
    + " SET @details = :details \n"
    + " SET @userid = :userid \n"
    + "	SELECT @isOrderExist = 0, \n"
    + "	       @isOrderLevelExist = 0 \n"
    + "	 \n"
    + "	IF EXISTS( \n"
    + "	       SELECT 1 \n"
    + "	       FROM   WarehouseOrders \n"
    + "	       WHERE  OrderId = @orderid \n"
    + "	   ) \n"
    + "	    SET @isOrderExist = 1 \n"
    + "	 \n"
    + "	IF @isNewOrder = 1 \n"
    + "	BEGIN \n"
    + "	    SELECT @orderid = ISNULL(MAX(OrderId), 0) + 1 \n"
    + "	    FROM   WarehouseOrders \n"
    + "	    SET @isOrderExist = 0 \n"
    + "	    SET @isOrderLevelExist = 0 \n"
    + "	END \n"
    + "	ELSE \n"
    + "	IF @isOrderExist = 0 -- On edit mode must has orderid already in db \n"
    + "	BEGIN \n"
    + "	    SELECT -1 AS result \n"
    + "	    RETURN \n"
    + "	END \n"
    + "--	SELECT @orderid\n"
    + "	IF EXISTS(\n"
    + "	       SELECT 1\n"
    + "	       FROM   WareHouseOrderLevels\n"
    + "	       WHERE  OrderId = @orderid\n"
    + "	   )\n"
    + "	    SET @isOrderLevelExist = 1\n"
    + "	\n"
    + "	IF (@isOrderExist = 0)\n"
    + "	BEGIN\n"
    + "	    INSERT INTO WarehouseOrders\n"
    + "	      (\n"
    + "	        orderid,\n"
    + "	        DistributerCompanyNid,\n"
    + "	        DeviceId,\n"
    + "           OrderType,\n"
    + "           Details,\n"
    + "           userId\n"
    + "	      )\n"
    + "	    VALUES\n"
    + "	      (\n"
    + "	        @orderid,\n"
    + "	        @distributerNid,\n"
    + "	        @deviceId,\n"
    + "           @orderType,\n"
    + "           @details,\n"
    + "           @userid\n"
    + "	      )\n"
    + "	END\n"
    + "	ELSE\n"
    + "	BEGIN\n"
    + "	    UPDATE WarehouseOrders\n"
    + "	    SET    DistributerCompanyNid     = @distributerNid,\n"
    + "	    DeviceId     = @deviceId,\n"
    + "       OrderType     = @orderType,\n"
    + "       Details       = @details,\n"
    + "       userId       = @userid\n"
    + "	    WHERE  OrderId                   = @orderid\n"
    + "	END\n"
    + "	\n"
    + "	IF (@isOrderLevelExist = 0)\n"
    + "	BEGIN\n"
    + "	    INSERT INTO WarehouseOrderLevels\n"
    + "	      (\n"
    + "	        OrderId,\n"
    + "	        LevelId,\n"
    + "	        NumberOfOrder\n"
    + "	      )\n"
    + "	    VALUES\n"
    + "	      (\n"
    + "	        @orderid,\n"
    + "	        0,\n"
    + "	        @qty\n"
    + "	      )\n"
    + "	END\n"
    + "	ELSE\n"
    + "	BEGIN\n"
    + "	    UPDATE WareHouseOrderLevels\n"
    + "	    SET    NumberOfOrder     = @qty\n"
    + "	    WHERE  OrderId           = @orderid\n"
    + "	           AND LevelId       = 0\n"
    + "	END\n"
    + "	EXEC [dbo].[SaveWhOrderProducts] @whOrderId=@orderid\n"
    + "	SELECT @orderid AS result\n"
    + "END TRY\n"
    + "BEGIN CATCH\n"
    + "	SELECT 0 AS result\n"
    + "END CATCH";
  try {
    const rows = await sequelize.query(sql, {
      replacements: {
        orderid: _orderid, qty: _qty, distributerNid: _distributerNid,
        isNewOrder: _isNewOrder, deviceId: _deviceId,
        orderType: _orderType, details: _details, userid: _userId
      },
      type: QueryTypes.INSERT,
    });
    console.log(rows);
    res.send(rows);
  } catch (err) {
    // Handle any errors or exceptions here
    console.error(err);
    res.status(500).send({ message: err.message });
  }
};

exports.updateStats = async (req, res) => {
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
  //  const sql = require('mssql');

  try {
    // Get the array of objects from the request body
    const orderStats = req.body;
    console.log(orderStats);
    // Use Promise.all to wait for all callbacks
    const promises = orderStats.map(async element => {
      const whorderid = element.whorderid;
      const gtin = element.gtin;
      const maxLimit = element.maxlimit;
      console.log(whorderid);
      const query = 'EXEC dbo.[spInsertStatsFromApp] @whorderid = :whorderid, @gtin= :gtin, @max= :max';
      // const replacements = { whorderid: whorderid, gtin: gtin, max: maxLimit }
      //const result = await sequelize.query(query, { replacements });

      const rows = await sequelize.query(query, {
        replacements: {
          whorderid: whorderid, gtin: gtin, max: maxLimit
        },
        type: QueryTypes.INSERT,
      });
      //res.send(rows);
    });
    // Wait for all promises to resolve
    await Promise.all(promises);
    // Send a success response
    res.status(200).json({ message: 'All stats inserted successfully' });
  }
  catch (err) {
    // Send an error response with the error message
    res.status(500).json({ message: 'Something went wrong', error: err.message });
  }
};  