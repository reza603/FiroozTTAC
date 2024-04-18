// Import the ScanLog model
const db = require("../models");
const ScanLog = db.scanlog;
const Op = db.Sequelize.Op;
const sequelize = require("sequelize");
const config = require("../config/db.config");
const { QueryTypes } = require("sequelize");


// Create and save a new ScanLog
exports.create = (req, res) => {
    // Validate request
    if (!req.body.uuid) {
        res.status(400).send({
            message: "UUID can not be empty!"
        });
        return;
    }

    // Create a ScanLog
    const scanLog = {
        whOrderId: req.body.whOrderId,
        whUserId: req.body.whUserId,
        uuid: req.body.uuid
    };

    // Save ScanLog in the database
    ScanLog.create(scanLog)
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while creating the ScanLog."
            });
        });
};

// Retrieve all ScanLogs from the database.
exports.findAll = (req, res) => {
    const uuid = req.query.uuid;
    var condition = uuid ? { uuid: { [Op.like]: `%${uuid}%` } } : null;

    ScanLog.findAll({ where: condition })
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while retrieving ScanLogs."
            });
        });
};

// Find a single ScanLog with an id
exports.findOne = (req, res) => {
    const id = req.params.id;

    ScanLog.findByPk(id)
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message: "Error retrieving ScanLog with id=" + id
            });
        });
};

// Update a ScanLog by the id in the request
exports.update = (req, res) => {
    const id = req.params.id;

    ScanLog.update(req.body, {
        where: { id: id }
    })
        .then(num => {
            if (num == 1) {
                res.send({
                    message: "ScanLog was updated successfully."
                });
            } else {
                res.send({
                    message: `Cannot update ScanLog with id=${id}. Maybe ScanLog was not found or req.body is empty!`
                });
            }
        })
        .catch(err => {
            res.status(500).send({
                message: "Error updating ScanLog with id=" + id
            });
        });
};

// Delete a ScanLog with the specified id in the request
exports.delete = (req, res) => {
    const id = req.params.id;

    ScanLog.destroy({
        where: { id: id }
    })
        .then(num => {
            if (num == 1) {
                res.send({
                    message: "ScanLog was deleted successfully!"
                });
            } else {
                res.send({
                    message: `Cannot delete ScanLog with id=${id}. Maybe ScanLog was not found!`
                });
            }
        })
        .catch(err => {
            res.status(500).send({
                message: "Could not delete ScanLog with id=" + id
            });
        });
};

// Delete all ScanLogs from the database.
exports.deleteAll = (req, res) => {
    ScanLog.destroy({
        where: {},
        truncate: false
    })
        .then(nums => {
            res.send({ message: `${nums} ScanLogs were deleted successfully!` });
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while removing all ScanLogs."
            });
        });
};
// Find all ScanLogs with a uuid and sort by date
exports.findByUUId = (req, res) => {
    const uuid = req.params.uuid;

    ScanLog.findAll({ where: { uuid: uuid }, order: [['createdAt', 'DESC']] })
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message: "Error retrieving ScanLogs with uuid=" + uuid
            });
        });
};

exports.findOrderTypeByUUId = async (req, res) => {
    const _uuid = req.params.uuid;

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
      .query("SELECT ordertype AS ordertype \n"
        + "FROM   WarehouseOrders \n"
        + "WHERE  orderid             = ( \n"
        + "           SELECT TOP(1) sl.whOrderId \n"
        + "           FROM   ScanLogs AS sl \n"
        + "           WHERE  uuid     = :uuid \n"
        + "           ORDER BY \n"
        + "                  sl.createdAt DESC \n"
        + "       )",
        {
          replacements: { uuid: _uuid },
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

// exports.countOrder = (req, res) => {
//     const _whorderid = req.body.whorderid;
//     console.log(`inside countOrder   ${_whorderid}`);
//     ScanLog.count({ where: { whorderid: _whorderid } })
//         .then((data) => {
//             res.send(data + "");
//         })
//         .catch((err) => {
//             res.status(500).send({
//                 message: "Error retrieving ScanLog count",
//             });
//         });
// };
exports.countOrder = (req, res) => {
    const _whorderid = req.body.whorderid;
    console.log(`inside countOrder   ${_whorderid}`);
    // Use sequelize.where to wrap the function call in the where clause
    ScanLog.count({ where: { whorderid: _whorderid, $and: sequelize.where(sequelize.fn('substring', sequelize.col('uuid'), 6, 1), '0') } })
        .then((data) => {
            res.send(data + "");
        })
        .catch((err) => {
            res.status(500).send({
                message: "Error retrieving ScanLog count",
            });
        });
};
