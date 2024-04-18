module.exports = (sequelize, Sequelize) => {
    const Product = sequelize.define("Product", {
      gtin: {
        type: Sequelize.STRING
      },
      // id: {
      //   type: Sequelize.INTEGER
      // },
      productfrname: {
        type: Sequelize.STRING
      },
      irc: {
        type: Sequelize.STRING
      },
      producercompanycode: {
        type: Sequelize.INTEGER
      },
    });
  
    return Product;
  };