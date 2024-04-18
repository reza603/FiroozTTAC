module.exports = (sequelize, Sequelize) => {
    const Order_Product = sequelize.define("WarehouseOrderProduct", {
      orderid: {
        type: Sequelize.INTEGER
      },
      gtin: {
        type: Sequelize.STRING
      },
                
    });
    return Order_Product;
  };