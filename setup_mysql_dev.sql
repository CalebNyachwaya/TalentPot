-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS tp_dev_db;
CREATE USER IF NOT EXISTS 'tp_dev'@'localhost' IDENTIFIED BY 'TP_dev_pwd_001';
GRANT ALL PRIVILEGES ON `tp_dev_db`.* TO 'tp_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tp_dev'@'localhost';
FLUSH PRIVILEGES;
