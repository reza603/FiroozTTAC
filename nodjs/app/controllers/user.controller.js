const db = require("../models");
const User = db.users;
const Op = db.Sequelize.Op;
const config = require("../config/db.config");
const { QueryTypes } = require('sequelize');
const { InsertOrUpdateUserToken } = require("./functions.controller");

// Create and Save a new User
exports.create = (req, res) => {
  // Validate request
  if (!req.body.username) {
    res.status(400).send({
      message: "UserName can not be empty!"
    });
    return;
  }

  // Create a User
  const user = {
    // id: req.body.id,
    fname: req.body.fname,
    lname: req.body.lname,
    phone: req.body.phone,
    username: req.body.username,
    password: req.body.password,
  };

  // Save User in the database
  User.create(user)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating the User."
      });
    });
};

exports.insert = async (req, res) => {
  const user = {
    // id: req.body.id,
    fname: req.body.fname,
    lname: req.body.lname,
    phone: req.body.phone,
    username: req.body.username,
    password: req.body.password,
  };
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
  tableName = "WhUsers";

  sql = "DECLARE @fname VARCHAR(100) =:fname \n"
    + "DECLARE @lname VARCHAR(100) =:lname \n"
    + "DECLARE @username VARCHAR(100) =:username \n"
    + "DECLARE @password VARCHAR(100) =:password \n"
    + "DECLARE @phone VARCHAR(20) =:phone \n"
    + "IF EXISTS( \n"
    + "       SELECT 1 \n"
    + "       FROM   WhUsers AS wu \n"
    + "       WHERE  username          = @username \n"
    + "              AND [PASSWORD]     = @password \n"
    + "   ) \n"
    + "BEGIN \n"
    + "	SELECT 'duplicate' AS ServerUserId  \n"
    + "	RETURN	 \n"
    + "END \n"
    + "INSERT INTO [dbo].[WhUsers]  \n"
    + "       ( \n"
    + "           [fname], \n"
    + "           [lname], \n"
    + "           [username], \n"
    + "           [password], \n"
    + "           [phone], \n"
    + "           [createdAt], \n"
    + "           [updatedAt] \n"

    + "       ) \n"
    + "SELECT @fname, \n"
    + "       @lname, \n"
    + "       @username, \n"
    + "       @password, \n"
    + "       @phone, \n"
    + "       GETDATE(), \n"
    + "       GETDATE()  \n"
    + "SELECT SCOPE_IDENTITY() AS ServerUserId";

  await sequelize
    .query(sql, {
      replacements: { fname: user.fname, lname: user.lname, username: user.username, password: user.password, phone: user.phone },
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

exports.inquiry = async (req, res) => {
  const user = {
    username: req.body.username,
    password: req.body.password,
  };
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
  sql = "DECLARE @username VARCHAR(100) =:username \n"
    + "DECLARE @password VARCHAR(100) =:password \n"
    + "IF NOT EXISTS( \n"
    + "       SELECT 1 \n"
    + "       FROM   WhUsers AS wu \n"
    + "       WHERE  username          = @username \n"
    + "              AND [PASSWORD]     = @password \n"
    + "   ) \n"
    + "BEGIN \n"
    + "	SELECT 'notfound' AS result  \n"
    + "	RETURN	 \n"
    + "END \n"
    + "	SELECT top(1) *,'ok' as result FROM   WhUsers AS wu WHERE  username          = @username \n"
    + "              AND [PASSWORD]     = @password \n"

  await sequelize
    .query(sql, {
      replacements: { username: user.username, password: user.password },
      type: QueryTypes.SELECT,
    })
    .then(async (rows) => {
      console.log(rows);
      let userToken= '';
      if (rows.length > 0) {
        // User is found , get the id field
        console.log('Getting user token from database ...');
        const userid = rows[0].id;
        userToken = await InsertOrUpdateUserToken(userid);
        console.log("User token: " + userToken);
      }
      rows[rows.length] = {"token": userToken};
      res.send(rows);
    })
    .catch((err) => {
      res.send(err);
      console.log(err);
    });
};
// Retrieve all Users from the database.
exports.findAll = (req, res) => {
  const userid = req.query.id;
  var condition = userid ? { userid: { [Op.like]: `%${userid}%` } } : null;

  User.findAll({ where: condition })
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving users."
      });
    });
};

// Find a single User with an id
exports.findOne = (req, res) => {
  const id = req.params.id;

  User.findByPk(id)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message: "Error retrieving User with id=" + id
      });
    });
};

// Update an existing User by the id in the request
exports.update = (req, res) => {
  const id = req.params.id;

  User.update(req.body, {
    where: { id: id }
  })
    .then(num => {
      if (num == 1) {
        res.send({
          message: "User was updated successfully."
        });
      } else {
        res.send({
          message: `Cannot update User with id=${id}. Maybe User was not found or req.body is empty!`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error updating User with id=" + id
      });
    });
};

// Delete an User with the specified id in the request
exports.delete = (req, res) => {
  const id = req.params.id;

  User.destroy({
    where: { id: id }
  })
    .then(num => {
      if (num == 1) {
        res.send({
          message: "User was deleted successfully!"
        });
      } else {
        res.send({
          message: `Cannot delete User with id=${id}. Maybe User was not found!`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Could not delete User with id=" + id
      });
    });
};

// Delete all Users from the database.
exports.deleteAll = (req, res) => {
  User.destroy({
    where: {},
    truncate: false
  })
    .then(nums => {
      res.send({ message: `${nums} Users were deleted successfully!` });
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while removing all users."
      });
    });
};

// find all published User
exports.findAllPublished = (req, res) => {
  User.findAll({ where: { published: true } })
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving users."
      });
    });
};
