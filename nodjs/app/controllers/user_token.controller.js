const db = require("../models");
const User_token = db.user_tokens;
exports.User_token = User_token;
const WhUser = db.users;
exports.WhUser = WhUser;
const jwt = require('jsonwebtoken');
const { InsertOrUpdateUserToken } = require("./functions.controller");

// const Op = _Sequelize.Op;
// import { DB, USER, PASSWORD, HOST, dialect as _dialect } from "../config/db.config";
// import { QueryTypes } from 'sequelize';


exports.create = (req, res) => {
  // Validate request
  console.log(req.body);
  if (!req.body.userid) {
    res.status(400).send({
      message: "User id can not be empty!"
    });
    return;
  }
  const userId = req.body.userid;
  InsertOrUpdateUserToken(userId, res);
};

exports.validate = (req, res) => {
  let tokenHeaderKey = process.env.TOKEN_HEADER_KEY;
  let jwtSecretKey = process.env.JWT_SECRET_KEY;

  try {
    const token = req.header(tokenHeaderKey);

    const verified = jwt.verify(token, jwtSecretKey);
    if (verified) {
      return res.status(200).send("Successfully Verified");
    } else {
      // Access Denied 
      return res.status(401).send(error);
    }
  } catch (error) {
    // Access Denied 
    return res.status(401).send(error);
  }
}


