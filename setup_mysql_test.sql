-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS tp_test_db;
CREATE USER IF NOT EXISTS 'tp_test'@'localhost' IDENTIFIED BY 'TP_test_pwd_001';
GRANT ALL PRIVILEGES ON `tp_test_db`.* TO 'tp_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tp_test'@'localhost';
FLUSH PRIVILEGES;
