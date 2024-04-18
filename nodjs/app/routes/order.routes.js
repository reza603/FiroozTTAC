const { checkTheUserToken } = require("../controllers/functions.controller.js");
module.exports = (app) => {
  const orders = require("../controllers/order.controller.js");

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
  // Create a new Order
  router.post("/", orders.create);

  // Insert a new Order with the given parameters
  router.post("/insert", orders.Insert);//Active on Handheld App
  // Retrieve all Orders
  router.get("/", orders.findAll);
  // Retrieve all Orders related to one device id
  router.get("/:deviceid", orders.findAllByDeviceId);

  // Retrieve all published Orders
  router.get("/published", orders.findAllPublished);

  // Retrieve a single Order with id
  router.get("/:id", orders.findOne);

  // Retrieve a single Order's distributer name with id
  router.get("/:id/distributer", orders.findOneDistributerName);

  // Retrieve a single Order count with id
  router.post("/count", orders.findOneCount);
  // Update an Order with id
  router.put("/:orderid", orders.update);

  // Delete an Order with id
  router.delete("/:orderId", orders.delete);

  router.post("/updateStats", orders.updateStats);//Active on Handheld App

  // Delete all Orders
  router.delete("/", orders.deleteAll);

  app.use("/api/Orders", router);

  var bodyParser = require("body-parser");

  app.use(bodyParser.json());
  
};
