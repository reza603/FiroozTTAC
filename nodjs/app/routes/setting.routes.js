const { checkTheUserToken } = require("../controllers/functions.controller.js");
module.exports = (app) => {
    const settings = require("../controllers/setting.controller.js");

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
    // Create a new Setting
    router.post("/", settings.create);
    // Get a value by attribute
    router.get("/:key", settings.getValue);
    // ... more routes
    app.use("/api/settings", router);
};