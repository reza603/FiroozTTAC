const { checkTheUserToken } = require("../controllers/functions.controller.js");
module.exports = (app) => {
  const user_tokens = require("../controllers/user_token.controller.js");

  var router = require("express").Router();
  // Middleware for checking the token
  router.use(async (req, res, next) => {
    console.log("Checking the user token");
    const userToken = await checkTheUserToken(req);
    if (!userToken) {
      // Access Denied 
      console.log('Access Denied');
      return res.status(401).send('Access Denied');
    }
    next();
  });

  // Create a new User
  router.post("/", user_tokens.create);

  // Retrieve all Users
  router.post("/verifyToken", user_tokens.validate);

  app.use('/api/userTokens', router);
};