const db = require("../models");
const Setting = db.settings;
const Op = db.Sequelize.Op;
const config = require("../config/db.config");
const { QueryTypes } = require("sequelize");

// Create and Save a new Setting
exports.create = (req, res) => {
    // Validate request
    if (!req.body.subsystem || !req.body.attribute || !req.body.value) {
        res.status(400).send({
            message: "Content can not be empty!",
        });
        return;
    }

    // Create a Setting
    const setting = {
        subsystem: req.body.subsystem,
        attribute: req.body.attribute,
        value: req.body.value,
    };

    // Save Setting in the database
    Setting.create(setting)
        .then((data) => {
            res.send(data);
        })
        .catch((err) => {
            res.status(500).send({
                message: err.message || "Some error occurred while creating the Setting.",
            });
        });
};

exports.getValue = (req, res) => {
    const _key = req.params.key;
    console.log(`Setting _key = ${_key}`);
    Setting.findAll({ where: { attribute: _key } })
      .then(data => {
        res.send(data);
      })
      .catch(err => {
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving settings."
        });
      });
};