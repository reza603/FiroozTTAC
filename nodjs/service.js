var Service = require('node-windows').Service;
var svc = new Service({
 name:'arsham-warehouse-app-service',
 description: 'Node.js service for Arsham Warehouse APP to save data on sql server.',
 script: 'E:\\Mojtaba\\Programing\\NodeJs\\node-js-crud-sql-server\\HandheldAPI\\server.js'
 
});

svc.on('install',function(){
 svc.start();
});

svc.install();