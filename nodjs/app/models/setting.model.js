module.exports = (sequelize, Sequelize) => {
    const Setting = sequelize.define("tblSetting", {
        id: {
            type: Sequelize.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        subsystem: {
            type: Sequelize.STRING
        },
        attribute: {
            type: Sequelize.STRING
        },
        value: {
            type: Sequelize.STRING
        }
    });

    return Setting;
};