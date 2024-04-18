module.exports = (sequelize, Sequelize) => {
    const User = sequelize.define("WhUser", {
      id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
      },
      fname: {
        type: Sequelize.STRING
      },
      lname: {
        type: Sequelize.STRING
      },
      username: {
        type: Sequelize.STRING
      },  
      password: {
        type: Sequelize.STRING
      }, 
      phone: {
        type: Sequelize.STRING
      }
    });
  
    return User;
  };