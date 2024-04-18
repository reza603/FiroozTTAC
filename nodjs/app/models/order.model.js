module.exports = (sequelize, Sequelize) => {
    const WarehouseOrder = sequelize.define("WarehouseOrder", {
      orderid: {
        type: Sequelize.INTEGER
      },
      gtin: {
        type: Sequelize.STRING
      },
      batchnumber: {
        type: Sequelize.STRING
      },
      expdate: {
        type: Sequelize.STRING
      },  
      userId: {
        type: Sequelize.INTEGER
      }, 
      insertdate: {
        type: Sequelize.STRING
      }, 
      lastxmldate: {
        type: Sequelize.STRING
      }, 
      distributercompanynid: {
        type: Sequelize.STRING
      }, 
      deviceid: {
        type: Sequelize.STRING
      }, 
      productionorderid: {
        type: Sequelize.STRING
      },   
      ordertype: {
        type: Sequelize.STRING
      },
      details:{
        type: Sequelize.STRING
      }                               
    });
  
    return WarehouseOrder;
  };