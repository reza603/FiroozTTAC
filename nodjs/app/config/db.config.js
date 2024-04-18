module.exports = {
    HOST: "127.0.0.1",
    PORT: "1433",
    USER: "sa",
    PASSWORD: "amf@sql2022",
    DB: "AMF_DB",
    dialect: "mssql",
    pool: {
      max: 5,
      min: 0,
      acquire: 30000,
      idle: 10000
    }
  };
