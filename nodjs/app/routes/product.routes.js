const { checkTheUserToken } = require("../controllers/functions.controller.js");
module.exports = app => {
  const products = require("../controllers/product.controller.js");
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

  // Create a new Product
  router.post("/", products.create);

  // Retrieve all Products
  router.get("/", products.findAll);

  // Retrieve all published Products
  router.get("/published", products.findAllPublished);

  // Retrieve a single Product with id
  router.get("/:gtin", products.findOne);

  // Update a product with id
  router.put("/:gtin", products.update);

  // Delete a product with id
  router.delete("/:gtin", products.delete);

  // Delete all Products
  router.delete("/", products.deleteAll);

  app.use('/api/Products', router);
};
