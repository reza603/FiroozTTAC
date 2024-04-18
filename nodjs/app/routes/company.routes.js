const { checkTheUserToken } = require("../controllers/functions.controller.js");
module.exports = (app) => {
  const companies = require("../controllers/company.controller.js");

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
    // Create a new Company
    router.post("/", companies.create);
  
    // Retrieve all Companies
    router.get("/", companies.findAll);//Active on Handheld App
  
    // Retrieve all published Companies
    router.get("/published", companies.findAllPublished);
  
    // Retrieve a single Company with id
    router.get("/:id", companies.findOne);
  
    // Update a Company with id
    router.put("/:id", companies.update);
  
    // Delete a Company with id
    router.delete("/:id", companies.delete);
  
    // Delete all Companies
    router.delete("/", companies.deleteAll);
  
    app.use('/api/Companies', router);
  };