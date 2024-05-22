module.exports = {
    HOST: "185.231.115.248",
    PORT: "1433",
    USER: "sa",
    PASSWORD: "amf@sql2022",
    DB: "amf_db",
    dialect: "mssql",
    pool: {
      max: 5,
      min: 0,
      acquire: 30000,
      idle: 10000
    }
  };
