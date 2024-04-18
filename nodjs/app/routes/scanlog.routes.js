const { checkTheUserToken } = require("../controllers/functions.controller.js");
module.exports = (app) => {
  const scanLogs = require("../controllers/scanlog.controller.js");
  
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
// Import the controller
// Create a new ScanLog
router.post("/", scanLogs.create);

// Retrieve all ScanLogs
router.get("/", scanLogs.findAll);

// Retrieve a single ScanLog with id
router.get("/:id", scanLogs.findOne);

// Update a ScanLog with id
router.put("/:id", scanLogs.update);

// Delete a ScanLog with id
router.delete("/:id", scanLogs.delete);

// Delete all ScanLogs
// router.delete("/", scanLogs.deleteAll);

// Find all ScanLogs with a uuid and sort by date
router.get("/uuid/:uuid", scanLogs.findByUUId);
router.get("/ordertype/:uuid", scanLogs.findOrderTypeByUUId);


router.post("/countOrder", scanLogs.countOrder);


app.use('/api/scanLogs', router);
}
