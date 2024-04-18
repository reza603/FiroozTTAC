const { checkTheUserToken } = require("../controllers/functions.controller.js");
module.exports = (app) => {
  const ongoingbarcodes = require("../controllers/ongoingbarcode.controller.js");

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
  
    // Create a new Ongoingbarcode
    router.post("/", ongoingbarcodes.create);
  
    // Retrieve all Ongoingbarcodes
    router.get("/", ongoingbarcodes.findAll);

    // Retrieve children list
    router.get("/children",ongoingbarcodes.findChildren);//Active on Handheld App
    // Retrieve all published Ongoingbarcodes
    router.get("/published", ongoingbarcodes.findAllPublished);
  
    // Retrieve a single Ongoingbarcode with id
    router.get("/:uuid", ongoingbarcodes.findOne);
  
    // Update a Ongoingbarcode with id
    // router.put("/:id", ongoingbarcodes.update);
  
    // Update a Ongoingbarcode with uuid
    router.post("/updatefavoritecode", ongoingbarcodes.updatefavcode);//Active on Handheld App
    
    router.post("/productcount", ongoingbarcodes.warehouseOrderProductCount);//Active on Handheld App

    router.post("/getbarcodefromuid", ongoingbarcodes.getBarcodeFromUid);//Active on Handheld App

    
    router.post("/countOrder", ongoingbarcodes.countOrder);//Active on Handheld App
    
    router.post("/countOrderLevels", ongoingbarcodes.countOrderLevels);//Active on Handheld App

    
    router.post("/track", ongoingbarcodes.trackBarcode);
    // Delete a Ongoingbarcode with id
    router.delete("/:id", ongoingbarcodes.delete);
    
    app.use('/api/Ongoingbarcodes', router);
  };