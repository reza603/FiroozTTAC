const db = require("../models");
const { QueryTypes } = require("sequelize");
const config = require("../config/db.config");
const Ongoingbarcode = db.ongoingbarcodes;
const ScanLog = db.scanlog;
const Op = db.Sequelize.Op;

// Create and Save a new Ongoingbarcode
exports.create = (req, res) => {
  // Validate request
  if (!req.body.uuid) {
    res.status(400).send({
      message: "Content can not be empty!",
    });
    return;
  }

  // Create a Ongoingbarcode
  const Ongoingbarcode = {
    id: req.body.id,
    orderid: req.body.orderid,
    levelid: req.body.levelid,
    parent: req.body.parent,
    uuid: req.body.uuid,
    rndesalat: req.body.rndesalat,
    orderserial: req.body.orderserial,
    favoritecode: req.body.favoritecode,
  };

  // Save Ongoingbarcode in the database
  Ongoingbarcode.create(ongoingbarcode)
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message:
          err.message ||
          "Some error occurred while creating the Ongoingbarcode.",
      });
    });
};

// Retrieve all Ongoingbarcodes from the database.
exports.findAll = (req, res) => {
  var condition;

  const uuid = req.query.uuid;
  condition = uuid ? { uuid: { [Op.like]: `%${uuid}%` } } : null;

  const _whorderid = req.query.favoritecode;
  condition = _whorderid
    ? { whorderid: { [Op.like]: `%${_whorderid}%` } }
    : null;

  Ongoingbarcode.findAll({ where: condition })
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message:
          err.message ||
          "Some error occurred while retrieving ongoingbarcodes.",
      });
    });
};

// Find a single Ongoingbarcode with an id
exports.findOne = (req, res) => {
  const _uuid = req.params.uuid;

  Ongoingbarcode.findOne({ where: { uuid: _uuid } })
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message: "Error retrieving Ongoingbarcode with uuid=" + _uuid,
      });
    });
};

// Update an existing Ongoingbarcode by the id in the request
exports.update = (req, res) => {
  const uuid = req.params.uuid;

  Ongoingbarcode.update(req.body, {
    where: { uuid: uuid },
  })
    .then((num) => {
      if (num == 1) {
        res.send({
          message: "Ongoingbarcode was updated successfully.",
        });
      } else {
        res.send({
          message: `Cannot update Ongoingbarcode with uuid=${uuid}. Maybe Ongoingbarcode was not found or req.body is empty!`,
        });
      }
    })
    .catch((err) => {
      res.status(500).send({
        message: `Error updating Ongoingbarcode with uuid= ${uuid}`,
      });
    });
};

// Update an existing Ongoingbarcode by the uuid in the request when scanning a specific  barcode
exports.updatefavcode = async (req, res) => {
  const _uuid = req.body.uuid;
  const _favoritecode = req.body.favoritecode;
  const _userid = req.body.userid;
  const _state = req.body.state;
  const _orderType = req.body.orderType;
  const _checkTheFollow = req.body.checkTheFollow;
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
  tableName = "OngoingBarcodes";
  fieldName = "WhOrderId";
  let _levelId = _uuid.substr(5, 1);
  console.log(_levelId);
  console.log(`the orderType is ${_orderType}`);
  sql = "DECLARE @uuid VARCHAR(20),  \n"
  + "        @favoritecode VARCHAR(20),  \n"
  + "        @state VARCHAR(10),  \n"
  + "        @orderid VARCHAR(20),  \n"
  + "        @orderType VARCHAR(20),  \n"
  + "        @checkTheFollow VARCHAR(20),  \n"
  + "        @FollowResult VARCHAR(20),  \n"
  + "        @gtin VARCHAR(20) = '',  \n"
  + "        @childrenCount INT = 0,  \n"
  + "        @productCount INT = 0,  \n"
  + "        @level_2_count INT = 0, \n"
  + "        @level_1_count INT = 0, \n"
  + "        @level_0_count INT=  0, \n"
  + "        @userId INT,  \n"
  + "        @Level INT   \n"
  + "     \n"
  + "DECLARE @rec TABLE  \n"
  + "(  \n"
  + "	Barcode VARCHAR(20),  \n"
  + "	LevelNum INT  \n"
  + ")     \n"
  + "           \n"
  + "SET @uuid = :uuid    \n"
  + "SET @favoritecode = :favoritecode    \n"
  + "SET @Orderid = ''   \n"
  + "SET @Level = CONVERT(INT, SUBSTRING(@uuid, 6, 1))  \n"
  + "SET @userId = :userid  \n"
  + "SET @state = :state  \n"
  + "--SET @state =N'DELETE'  \n"
  + "SET @orderType = '" + _orderType + "' \n"
  + "SET @checkTheFollow = '" + _checkTheFollow + "'  \n"
  + "SET @FollowResult = 'OK' -- default value \n"
  + "                         -- if uuid notfound in OngoingBarcodes table then check Barcodes table \n"
  + "                         -- if uuid notfound in OngoingBarcodes table then check Barcodes table     \n"
  + "SELECT @level_2_count = COUNT(0) FROM ScanLogs AS sl WHERE Whorderid = @favoritecode AND SUBSTRING(uuid,6,1) = '2'  \n"
  + "SELECT @level_1_count = COUNT(0) FROM ScanLogs AS sl WHERE Whorderid = @favoritecode AND SUBSTRING(uuid,6,1) = '1'                           \n"
  + "SELECT @level_0_count = COUNT(0) FROM ScanLogs AS sl WHERE Whorderid = @favoritecode AND SUBSTRING(uuid,6,1) = '0'                           \n"
  + "  \n"
  + "IF NOT EXISTS(   \n"
  + "       SELECT 1   \n"
  + "       FROM   OnGoingBarCodes   \n"
  + "       WHERE  uuid = @uuid   \n"
  + "   )   \n"
  + "BEGIN   \n"
  + "    IF NOT EXISTS(   \n"
  + "           SELECT 1   \n"
  + "           FROM   Barcodes AS o   \n"
  + "           WHERE  uuid = SUBSTRING(@uuid,6,15)   \n"
  + "       )   \n"
  + "    BEGIN   \n"
  + "        SELECT 'notFound'      AS result,   \n"
  + "               ''              AS orderid,   \n"
  + "               @gtin           AS gtin,   \n"
  + "               @childrenCount  AS childrencount,   \n"
  + "               @productCount   AS productcount,  \n"
  + "               @level_2_count AS level2count,  \n"
  + "               @level_1_count AS level1count,   \n"
  + "               @level_0_count AS level0count  \n"
  + "               RETURN  \n"
  + "    END   \n"
  + "    ELSE   \n"
  + "    BEGIN   \n"
  + "    	SELECT @orderid = orderid   \n"
  + "        FROM   barcodes   \n"
  + "        WHERE  uuid = SUBSTRING(@uuid,6,15) \n"
  + "         \n"
  + "        SELECT 'notstarted'    AS result,   \n"
  + "               @orderid        AS orderid,   \n"
  + "               @gtin           AS gtin,   \n"
  + "               @childrenCount  AS childrencount,   \n"
  + "               @productCount   AS productcount,  \n"
  + "               @level_2_count AS level2count,  \n"
  + "               @level_1_count AS level1count,   \n"
  + "               @level_0_count AS level0count     \n"
  + "                \n"
  + "               RETURN            \n"
  + "    END   \n"
  + "END------ End of 'if uuid notfound in OngoingBarcodes' condition--------------------------   \n"
  + "ELSE   \n"
  + "    -- if WhOrderId value is not null        \n"
  + "    	DECLARE @blocked BIT \n"
  + "        SELECT @orderid = orderid,@blocked = IsBlocked   \n"
  + "        FROM   barcodes   \n"
  + "        WHERE  uuid = SUBSTRING(@uuid,6,15) \n"
  //+ "        SELECT @blocked AS BLOCKSTAT   \n"
  + "        IF (@blocked = 1)  \n"
  + "        BEGIN \n"
  + "			SELECT 'blocked'    AS result,   \n"
  + "				   @orderid        AS orderid,   \n"
  + "				   @gtin           AS gtin,   \n"
  + "				   @childrenCount  AS childrencount,   \n"
  + "				   @productCount   AS productcount,  \n"
  + "				   @level_2_count AS level2count,  \n"
  + "				   @level_1_count AS level1count,   \n"
  + "				   @level_0_count AS level0count       \n"
  + "			RETURN 		          \n"
  + "        END      \n"
  + "        \n"
  + "SELECT @gtin = productcode   \n"
  + "FROM   orders   \n"
  + "WHERE  OrderCode = @orderid    \n"
  + "     \n"
  + "SELECT @FollowResult = dbo.CheckUidByOrderType(@uuid, @orderType)    \n"
  + "IF (@checkTheFollow = 'TRUE' AND @FollowResult = 'Duplicate' AND @state = 'ADD')   \n"
  + "BEGIN   \n"
  + "    DECLARE @oldWhorderid INT   \n"
  + "    SELECT @oldWhorderid = sl.whOrderId   \n"
  + "    FROM   ScanLogs AS sl   \n"
  + "    WHERE  uuid = @uuid   \n"
  + "       \n"
  + "    IF @oldWhorderid <> @favoritecode   \n"
  + "    BEGIN   \n"
  + "        SELECT 'otherorder' AS result,   \n"
  + "               @orderid        AS orderid,   \n"
  + "               @gtin           AS gtin,   \n"
  + "               @childrenCount  AS childrencount,   \n"
  + "               @productCount   AS productcount,  \n"
  + "               @level_2_count AS level2count,  \n"
  + "               @level_1_count AS level1count,   \n"
  + "               @level_0_count AS level0count  \n"
  + "               RETURN                  \n"
  + "    END   \n"
  + "    ELSE   \n"
  + "    BEGIN  \n"
  + "    IF (@state = 'ADD')	  \n"
  + "    SELECT 'duplicate' AS result,   \n"
  + "            @orderid        AS orderid,   \n"
  + "            @gtin           AS gtin,   \n"
  + "            @childrenCount  AS childrencount,   \n"
  + "            @productCount   AS productcount,  \n"
  + "            @level_2_count AS level2count,  \n"
  + "            @level_1_count AS level1count,   \n"
  + "            @level_0_count AS level0count                  \n"
  + "            RETURN     		   \n"
  + "    END   \n"
  + "END   \n"
  + "ELSE   \n"
  + "BEGIN   \n"
  + "    IF (@state = 'ADD')   \n"
  + "    BEGIN  \n"
  + "        IF (@checkTheFollow = 'TRUE' AND @FollowResult = 'OK')   \n"
  + "           OR (   \n"
  + "                  @checkTheFollow = 'FALSE'   \n"
  + "                  AND @FollowResult NOT IN ('Duplicate')   \n"
  + "              )   \n"
  + "        BEGIN   \n"
  + "            WITH REC(Barcode, LevelNum) AS (   \n"
  + "                SELECT B.uuid,   \n"
  + "                       @Level           AS LevelNum   \n"
  + "                FROM   OngoingBarcodes     B   \n"
  + "                WHERE  B.uuid = @uuid    \n"
  + "                UNION ALL SELECT B.uuid,   \n"
  + "                                 R.LevelNum - 1   \n"
  + "                          FROM   OngoingBarcodes B   \n"
  + "                                 INNER JOIN REC R   \n"
  + "                                      ON  (R.Barcode = B.Parent)   \n"
  + "        WHERE  R.LevelNum > 0   \n"
  + "            )       \n"
  + "            INSERT INTO @rec (Barcode, LevelNum)   \n"
  + "            SELECT Barcode, LevelNum  \n"
  + "            FROM   REC     \n"
  + "            SELECT @level_2_count = COUNT(0) FROM @rec AS r WHERE r.LevelNum = 2  \n"
  + "            SELECT @level_1_count = COUNT(0) FROM @rec AS r WHERE r.LevelNum = 1   \n"
  + "            SELECT @level_0_count = COUNT(0) FROM @rec AS r WHERE r.LevelNum = 0   \n"
  + "               \n"
  + "            IF (@orderType = 'outgoing')   \n"
  + "            BEGIN   \n"
  + "                UPDATE OngoingBarcodes   \n"
  + "                SET    WhOrderId = @favoritecode,   \n"
  + "                       WhUserId = @userId,   \n"
  + "                       WhScanDate = GETDATE()   \n"
  + "                WHERE  uuid IN (SELECT Barcode   \n"
  + "                                FROM   @rec)   \n"
  + "                       AND WhOrderId IS NULL     \n"
  + "                   \n"
  + "                UPDATE OngoingBarcodes   \n"
  + "                SET    WhOrderId      = @favoritecode,   \n"
  + "                       WhUserId       = @userId,   \n"
  + "                       WhScanDate     = GETDATE()   \n"
  + "                WHERE  uuid           = @uuid   \n"
  + "            END     \n"
  + "               \n"
  + "            INSERT INTO [dbo].[ScanLogs]    \n"
  + "                   ([whOrderId], [whUserId], [uuid], [createdAt])   \n"
  + "            SELECT @favoritecode,   \n"
  + "                   @userId,   \n"
  + "                   Barcode,   \n"
  + "                   GETDATE()   \n"
  + "            FROM   @rec     \n"
  + "               \n"
  + "            SELECT @childrenCount = (   \n"
  + "                       SELECT COUNT(0)   \n"
  + "                       FROM   @rec AS r   \n"
  + "                       WHERE  r.LevelNum = @level - 1   \n"
  + "                   )    \n"
  + "               \n"
  + "            IF (@ordertype = 'incoming')   \n"
  + "            BEGIN   \n"
  + "                SELECT @productCount = (   \n"
  + "                           SELECT COUNT(0)   \n"
  + "                           FROM   OnGoingBarCodes AS ogbc   \n"
  + "                           WHERE  ogbc.OrderId = @orderid   \n"
  + "                                  AND levelId = 0   \n"
  + "                                  AND uuid IN (SELECT uuid   \n"
  + "                                               FROM   ScanLogs AS sl   \n"
  + "                                               WHERE  sl.whOrderId = @favoritecode)   \n"
  + "                       )   \n"
  + "            END   \n"
  + "            ELSE     \n"
  + "            IF (@orderType = 'outgoing')   \n"
  + "            BEGIN   \n"
  + "                SELECT @productCount = (   \n"
  + "                           SELECT COUNT(0)   \n"
  + "                           FROM   OnGoingBarCodes AS ogbc   \n"
  + "                           WHERE  ogbc.OrderId = @orderid   \n"
  + "                                  AND levelId = 0   \n"
  + "                                  AND ogbc.WhOrderId = @favoritecode   \n"
  + "                       )   \n"
  + "            END   \n"
  + "            ELSE     \n"
  + "            IF (@orderType = 'returning')   \n"
  + "            BEGIN   \n"
  + "                SELECT @productCount = (   \n"
  + "                           SELECT COUNT(0)   \n"
  + "                           FROM   OnGoingBarCodes AS ogbc   \n"
  + "                           WHERE  ogbc.OrderId = @orderid   \n"
  + "                                  AND levelId = 0   \n"
  + "                                  AND uuid IN (SELECT uuid   \n"
  + "                                               FROM   ScanLogs AS sl   \n"
  + "                                               WHERE  sl.whOrderId = @favoritecode)   \n"
  + "                       )   \n"
  + "            END    \n"
  + "               \n"
  + "            SELECT 'ok'            AS result,   \n"
  + "                   @orderid        AS orderid,   \n"
  + "                   @gtin           AS gtin,   \n"
  + "                   @childrenCount  AS childrencount,   \n"
  + "                   @productCount   AS productcount,  \n"
  + "				   @level_2_count AS level2count,  \n"
  + "				   @level_1_count AS level1count,   \n"
  + "				   @level_0_count AS level0count                  \n"
  + "                   RETURN                  \n"
  + "            END --   IF (@checkTheFollow = 'TRUE' AND @FollowResult = 'OK' ) OR (@checkTheFollow = 'FALSE')      \n"
  + "            ELSE     \n"
  + "            BEGIN   \n"
  + "            	SELECT @childrenCount = (   \n"
  + "            	           SELECT COUNT(0)   \n"
  + "            	           FROM   @rec AS r   \n"
  + "            	           WHERE  r.LevelNum = @level - 1   \n"
  + "            	       )    \n"
  + "            	   \n"
  + "            	IF (@ordertype = 'incoming')   \n"
  + "            	BEGIN   \n"
  + "            	    SELECT @productCount = (   \n"
  + "            	               SELECT COUNT(0)   \n"
  + "            	               FROM   OnGoingBarCodes AS ogbc   \n"
  + "            	               WHERE  ogbc.OrderId = @orderid   \n"
  + "            	                      AND levelId = 0   \n"
  + "            	                      AND uuid IN (SELECT uuid   \n"
  + "            	                                   FROM   ScanLogs AS sl   \n"
  + "            	                                   WHERE  sl.whOrderId = @favoritecode)   \n"
  + "            	           )   \n"
  + "            	END   \n"
  + "            	ELSE     \n"
  + "            	IF (@orderType = 'outGoing')   \n"
  + "            	BEGIN   \n"
  + "            	    SELECT @productCount = (   \n"
  + "            	               SELECT COUNT(0)   \n"
  + "            	               FROM   OnGoingBarCodes AS ogbc   \n"
  + "            	               WHERE  ogbc.OrderId = @orderid   \n"
  + "            	                      AND levelId = 0   \n"
  + "            	                      AND ogbc.WhOrderId = @favoritecode   \n"
  + "            	           )   \n"
  + "            	END   \n"
  + "            	ELSE     \n"
  + "            	IF (@orderType = 'returning')   \n"
  + "            	BEGIN   \n"
  + "            	    SELECT @productCount = (   \n"
  + "            	               SELECT COUNT(0)   \n"
  + "            	               FROM   OnGoingBarCodes AS ogbc   \n"
  + "            	               WHERE  ogbc.OrderId = @orderid   \n"
  + "            	                      AND levelId = 0   \n"
  + "            	                      AND uuid IN (SELECT uuid   \n"
  + "            	                                   FROM   ScanLogs AS sl   \n"
  + "            	                                   WHERE  sl.whOrderId = @favoritecode)   \n"
  + "            	           )   \n"
  + "            	END    \n"
  + "            	   \n"
  + "            	SELECT @FollowResult   AS result,   \n"
  + "            	       @orderid        AS orderid,   \n"
  + "            	       @gtin           AS gtin,   \n"
  + "            	       @childrenCount  AS childrencount,   \n"
  + "            	       @productCount   AS productcount,  \n"
  + "					   @level_2_count AS level2count,  \n"
  + "					   @level_1_count AS level1count,   \n"
  + "					   @level_0_count AS level0count                  \n"
  + "            	       RETURN    \n"
  + "            END   \n"
  + "    END--  IF (@state = 'ADD')   \n"
  + "    ELSE      \n"
  + "    IF (@state = 'DELETE')   \n"
  + "    BEGIN  \n"
  + "        IF @FollowResult = 'Duplicate' -- already exists in db   \n"
  + "        BEGIN   \n"
  + "            WITH REC(Barcode, LevelNum) AS (   \n"
  + "                SELECT B.uuid,   \n"
  + "                       @Level           AS LevelNum   \n"
  + "                FROM   OngoingBarcodes     B   \n"
  + "                WHERE  B.uuid = @uuid    \n"
  + "                UNION ALL SELECT B.uuid,   \n"
  + "                                 R.LevelNum - 1   \n"
  + "                          FROM   OngoingBarcodes B   \n"
  + "                                 INNER JOIN REC R   \n"
  + "                                      ON  (R.Barcode = B.Parent)   \n"
  + "                          WHERE  R.LevelNum > 0   \n"
  + "            )       \n"
  + "            INSERT INTO @rec (Barcode, LevelNum)   \n"
  + "            SELECT Barcode,   \n"
  + "                   LevelNum   \n"
  + "            FROM   REC     \n"
  + "               \n"
  + "            IF (@orderType = 'outgoing')   \n"
  + "            BEGIN   \n"
  + "                UPDATE OngoingBarcodes   \n"
  + "                SET    WhOrderId = NULL   \n"
  + "                WHERE  uuid IN (SELECT Barcode   \n"
  + "                                FROM   @rec)     \n"
  + "                   \n"
  + "                UPDATE OngoingBarcodes   \n"
  + "                SET    WhOrderId     = NULL   \n"
  + "                WHERE  uuid          = @uuid   \n"
  + "            END     \n"
  + "               \n"
  + "            DELETE    \n"
  + "            FROM   [dbo].[ScanLogs]   \n"
  + "            WHERE  WhOrderId = @favoritecode   \n"
  + "                   AND uuid IN (SELECT Barcode   \n"
  + "                                FROM   @rec)     \n"
  + "               \n"
  + "            DELETE    \n"
  + "            FROM   ScanLogs   \n"
  + "            WHERE  whorderid = @favoritecode   \n"
  + "                   AND uuid = @uuid   \n"
  + "               \n"
  + "            SELECT @childrenCount = 0    \n"
  + "            IF (@ordertype = 'incoming')   \n"
  + "            BEGIN   \n"
  + "                SELECT @productCount = (   \n"
  + "                           SELECT COUNT(0)   \n"
  + "                           FROM   OnGoingBarCodes AS ogbc   \n"
  + "                           WHERE  ogbc.OrderId = @orderid   \n"
  + "                                  AND levelId = 0   \n"
  + "                                  AND uuid IN (SELECT uuid   \n"
  + "                                               FROM   ScanLogs AS sl   \n"
  + "                                               WHERE  sl.whOrderId = @favoritecode)   \n"
  + "                       )   \n"
  + "            END   \n"
  + "            ELSE     \n"
  + "            IF (@orderType = 'outGoing')   \n"
  + "            BEGIN   \n"
  + "                SELECT @productCount = (   \n"
  + "                           SELECT COUNT(0)   \n"
  + "                           FROM   OnGoingBarCodes AS ogbc   \n"
  + "                           WHERE  ogbc.OrderId = @orderid   \n"
  + "                                  AND levelId = 0   \n"
  + "                                  AND ogbc.WhOrderId = @favoritecode   \n"
  + "                       )   \n"
  + "            END   \n"
  + "            ELSE     \n"
  + "            IF (@orderType = 'returning')   \n"
  + "            BEGIN   \n"
  + "                SELECT @productCount = (   \n"
  + "                           SELECT COUNT(0)   \n"
  + "                           FROM   OnGoingBarCodes AS ogbc   \n"
  + "                           WHERE  ogbc.OrderId = @orderid   \n"
  + "                                  AND levelId = 0   \n"
  + "                                  AND uuid IN (SELECT uuid   \n"
  + "                                               FROM   ScanLogs AS sl   \n"
  + "                                               WHERE  sl.whOrderId = @favoritecode)   \n"
  + "                       )   \n"
  + "            END    \n"
  + "               \n"
  + "            SELECT 'ok'            AS result,   \n"
  + "                   @orderid        AS orderid,   \n"
  + "                   @gtin           AS gtin,   \n"
  + "                   @childrenCount  AS childrencount,   \n"
  + "                   @productCount   AS productcount,  \n"
  + "				   @level_2_count AS level2count,  \n"
  + "				   @level_1_count AS level1count,   \n"
  + "				   @level_0_count AS level0count                  \n"
  + "                   RETURN     \n"
  + "               \n"
  + "            END-- IF @FollowResult = 'Duplicate'     \n"
  + "            ELSE      \n"
  + "            BEGIN   \n"
  + "            	SELECT 'notfound'      AS result,   \n"
  + "            	       @orderid        AS orderid,   \n"
  + "            	       @gtin           AS gtin,   \n"
  + "            	       @childrenCount  AS childrencount,   \n"
  + "            	       @productCount   AS productcount,  \n"
  + "					   @level_2_count AS level2count,  \n"
  + "					   @level_1_count AS level1count,   \n"
  + "					   @level_0_count AS level0count                  \n"
  + "            	       RETURN    \n"
  + "            END   \n"
  + "    END-- IF (@state = 'DELETE')'   \n"
  + "END";
  await sequelize
    .query(sql, {
      replacements: { favoritecode: _favoritecode, uuid: _uuid, state: _state, userid: _userid },
      type: QueryTypes.UPDATE,
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

exports.countOrder = (req, res) => {
  const _whorderid = req.body.whorderid;
  const _orderType = req.body.orderType;
  console.log(`inside countOrder   ${_whorderid}`);
  switch (_orderType) {
    case "outgoing":
      Ongoingbarcode.count({ where: { whorderid: _whorderid, levelid: 0 } })
        .then((data) => {
          res.send(data + "");
        })
        .catch((err) => {
          res.status(500).send({
            message: "Error retrieving Ongoingbarcode count",
          });
        });
      break;
    default:
      ScanLog.count({ where: { whorderid: _whorderid } })
        .then((data) => {
          res.send(data + "");
        })
        .catch((err) => {
          res.status(500).send({
            message: "Error retrieving ScanLog count",
          });
        });
  }
};



exports.countOrderLevels = (req, res) => {
  const _whorderid = req.body.whorderid;
  const _orderType = req.body.orderType;

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

  console.log(`inside countOrder   ${_whorderid}`);
  switch (_orderType) {
    case "outgoing":
      // The raw SQL query for the Ongoingbarcode.findAll method
      const sql1 = `SELECT COALESCE(levelid, 0) AS levelid, COUNT(levelid) AS count FROM Ongoingbarcode WHERE whorderid = ${_whorderid} OR levelid IS NULL GROUP BY COALESCE(levelid, 0)`;
      sequelize.query(sql1, {
        type: Sequelize.QueryTypes.SELECT, // The type of query to execute
        model: Ongoingbarcode, // The model to map the results to
        mapToModel: true // Pass true here if you have any mapped fields
      })
        .then((data) => {
          // data will be an array of Ongoingbarcode instances
          res.send(data);
        })
        .catch((err) => {
          res.status(500).send({
            message: "Error retrieving Ongoingbarcode count",
          });
        });
      break;
    default:
      // The raw SQL query for the ScanLog.findAll method
      const sql2 = `SELECT COALESCE(substring(uuid, 6, 1), 0) AS levelid, COUNT(uuid) AS count FROM ScanLogs WHERE whorderid = ${_whorderid} OR uuid IS NULL GROUP BY COALESCE(substring(uuid, 6, 1), 0)`;
      sequelize.query(sql2, {
        type: Sequelize.QueryTypes.SELECT, // The type of query to execute
        model: ScanLog, // The model to map the results to
        mapToModel: true // Pass true here if you have any mapped fields
      })
        .then((data) => {
          // data will be an array of ScanLog instances
          res.send(data);
        })
        .catch((err) => {
          res.status(500).send({
            message: "Error retrieving ScanLogs count",
          });
        });
  }
}


async function isRndEsalatFound(key) {
  console.log("isRndEsalatFound", key);
  const _result = await Ongoingbarcode.findOne({ where: { rndesalat: key } });
  if (_result === null) {
    console.log("No rndesalat found for key " + key);
    return false;
  } else {
    console.log("Found rndesalat " + _result.rndesalat);
    return true;
  }

  // Ongoingbarcode.count({ where: { rndesalat: key } }).then((count) => {
  //   return count > 0 ? true : false;
  // });
}
async function isUuidFound(key) {
  console.log("isUuidFound", key);
  const _result = await Ongoingbarcode.findOne({ where: { uuid: key } });
  if (_result === null) {
    console.log("No uuid found for key " + key);
    return false;
  } else {
    console.log("Found uuid " + _result.uuid);
    return true;
  }
}
async function isBarcodeFound(key) {
  console.log("isBarcodeFound", key);
  _key = key.substring(18, 38);
  const _result = await Ongoingbarcode.findOne({ where: { uuid: _key } });
  if (_result === null) {
    console.log("No uuid found for key " + _key);
    return false;
  } else {
    console.log("Found uuid " + _result.uuid);
    return true;
  }

  // Ongoingbarcode.count({ where: { rndesalat: key } }).then((count) => {
  //   return count > 0 ? true : false;
  // });
}

exports.trackBarcode = async (req, res) => {
  const _userId = req.body.userId;
  const _method = req.body.method;
  const _key = req.body.key;
  console.log(_key, _method, _userId);
  if (_method == "rndEsalat") {
    if (await isRndEsalatFound(_key)) {
      res.send("Found");
      console.log("Found");
      return;
    } else {
      res.send("notFound");
    }
  }
  if (_method == "uuid") {
    if (await isUuidFound(_key)) {
      res.send("Found");
      console.log("Found");
      return;
    } else {
      res.send("notFound");
    }
  }
  if (_method == "barcode") {
    if (await isBarcodeFound(_key)) {
      res.send("Found");
      console.log("Found");
      return;
    } else {
      res.send("notFound");
    }
  }
};
// Delete an Ongoingbarcode with the specified id in the request
exports.delete = (req, res) => {
  const nationalid = req.params.nationalid;

  Ongoingbarcode.destroy({
    where: { nationalid: nationalid },
  })
    .then((num) => {
      if (num == 1) {
        res.send({
          message: "Ongoingbarcode was deleted successfully!",
        });
      } else {
        res.send({
          message: `Cannot delete Ongoingbarcode with nationalid=${nationalid}. Maybe Ongoingbarcode was not found!`,
        });
      }
    })
    .catch((err) => {
      res.status(500).send({
        message: "Could not delete Ongoingbarcode with id=" + id,
      });
    });
};

// Delete all Ongoingbarcodes from the database.
exports.deleteAll = (req, res) => {
  Ongoingbarcode.destroy({
    where: {},
    truncate: false,
  })
    .then((nums) => {
      res.send({
        message: `${nums} Ongoingbarcodes were deleted successfully!`,
      });
    })
    .catch((err) => {
      res.status(500).send({
        message:
          err.message ||
          "Some error occurred while removing all ongoingbarcodes.",
      });
    });
};

// find all published Ongoingbarcode
exports.findAllPublished = (req, res) => {
  Ongoingbarcode.findAll({ where: { published: true } })
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message:
          err.message ||
          "Some error occurred while retrieving ongoingbarcodes.",
      });
    });
};
exports.findChildren = (req, res) => {
  const _uuid = req.query.uuid;
  console.log('find children of $_uuid : ', _uuid + req.params);
  Ongoingbarcode.findAll({ where: { parent: _uuid } })
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({
        message:
          err.message ||
          "Some error occurred while retrieving children list.",
      });
    });
};

exports.warehouseOrderProductCount = async (req, res) => {
  const _uuid = req.body.uuid;
  const _favoritecode = req.body.favoritecode;
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

  sql = "DECLARE @uuid VARCHAR(20), \n"
    + "        @favoritecode VARCHAR(20), \n"
    + "        @orderid VARCHAR(20), \n"
    + "        @orderType VARCHAR(20), \n"
    + "        @gtin VARCHAR(20), \n"
    + "        @productCount INT = 0 \n"
    + " \n"
    + "DECLARE @rec TABLE \n"
    + "( \n"
    + "	Barcode VARCHAR(20), \n"
    + "	LevelNum INT \n"
    + ")  \n"
    + "SET @uuid = :uuid    \n"
    + "SET @favoritecode = :favoritecode    \n"
    + "SELECT @Orderid = orderid \n"
    + "FROM   OnGoingBarCodes \n"
    + "WHERE  uuid = @uuid \n"
    + "     \n"
    + "SELECT @gtin = productcode \n"
    + "FROM   orders \n"
    + "WHERE  ordercode = @orderid \n"
    + "     \n"
    + "SELECT @productCount = ( \n"
    + "           SELECT COUNT(0) \n"
    + "           FROM   OnGoingBarCodes AS ogbc \n"
    + "           WHERE  ogbc.WhOrderId = @favoritecode  \n"
    + "                  AND ogbc.OrderId IN (SELECT OrderCode From Orders WHERE productcode = @gtin) \n"
    + "                  AND levelId = 0 \n"
    + "       ) \n"
    + " \n"
    + "SELECT 'ok'           AS result, \n"
    + "       @orderid       AS orderid, \n"
    + "       @productCount  AS productcount  ";
  await sequelize
    .query(sql, {
      replacements: { favoritecode: _favoritecode, uuid: _uuid },
      type: QueryTypes.UPDATE,
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


exports.getBarcodeFromUid = async (req, res) => {
  const _uuid = req.body.uuid;
  console.log(_uuid);
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


  sql = "SELECT dbo.MakeBarcodeFromUid(:uuid) AS barcode";

  await sequelize
    .query(sql, {
      replacements: { uuid: _uuid },
      type: QueryTypes.SELECT,
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