const { checkTheUserToken } = require("../controllers/functions.controller.js");
module.exports = (app) => {
  const order_products = require("../controllers/order_product.controller");
  
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

    // Create a new Order_Product
    router.post("/", order_products.create);
  
    // Retrieve all Orders
    router.get("/", order_products.findAll);

    router.get("/withjoin", order_products.findAllWithJoinProducts);
  
    // Retrieve a single Order_Product with id
    router.get("/:id", order_products.findOne);
  
    // Retrieve a single Order_Product count with id
    router.post("/count", order_products.findOneCount);
    // Update an Order_Product with id
    router.put("/:id", order_products.update);
  
    // Delete an Order_Product with id
    router.delete("/:id", order_products.delete);
  
    // Delete all Orders
    router.delete("/", order_products.deleteAll);
  
    app.use("/api/OrderProducts", router);
  };
  