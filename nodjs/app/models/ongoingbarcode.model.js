module.exports = (sequelize, Sequelize) => {
  const Ongoingbarcode = sequelize.define("Ongoingbarcode", {
    id: {
      type: Sequelize.INTEGER,
      primaryKey: true,
    },
    orderid: {
      type: Sequelize.STRING,
    },
    levelid: {
      type: Sequelize.INTEGER,
    },
    parent: {
      type: Sequelize.STRING,
    },
    uuid: { type: Sequelize.STRING },
    rndesalat: { type: Sequelize.STRING },
    orderserial: { type: Sequelize.INTEGER },
    favoritecode: { type: Sequelize.INTEGER },
    whorderid: { type: Sequelize.INTEGER},
  });

  return Ongoingbarcode;
};
