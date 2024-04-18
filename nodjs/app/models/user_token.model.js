module.exports = (sequelize, Sequelize) => {
    const User = sequelize.define("WhUserToken", {
      id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true
      },
      key: {
        type: Sequelize.STRING
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
    });
  
    return User;
  };