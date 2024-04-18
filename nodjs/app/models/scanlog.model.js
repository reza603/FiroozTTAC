module.exports = (sequelize, Sequelize) => {
  const ScanLog = sequelize.define('ScanLog', {
    // Model attributes are defined here
    id: {
      type: Sequelize.INTEGER,
      primaryKey: true,
      autoIncrement: true
    },
    whOrderId: {
      type: Sequelize.INTEGER,
      references: {
        model: 'WarehouseOrders',
        key: 'OrderId'
      },
      onUpdate: 'CASCADE',
      onDelete: 'CASCADE'
    },
    whUserId: {
      type: Sequelize.INTEGER,
      references: {
        model: 'WhUsers',
        key: 'Id'
      },
      onUpdate: 'CASCADE',
      onDelete: 'SET NULL'
    },
    uuid: {
      type: Sequelize.STRING(20)
    },
    createdAt: {
      type: Sequelize.DATE,
      defaultValue: Sequelize.NOW
    },
    updatedAt: {
      type: Sequelize.DATE
    }
  }, {
    // Other model options go here
  });

  return ScanLog;

};