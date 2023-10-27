-- MySQL dump 10.13  Distrib 5.7.8-rc, for Linux (x86_64)
--
-- Host: localhost    Database: hbnb_dev_db
-- ------------------------------------------------------
-- Server version	5.7.8-rc

USE tp_test_db;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `employees`;

CREATE TABLE `employees` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `first_name` varchar(128) NOT NULL,
  `last_name` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone` varchar(128) NOT NULL,
  `dept` varchar(128) NOT NULL,
  `position` varchar(128) NOT NULL,
  `DOB` varchar(128) NOT NULL,
  `company` varchar(128) NOT NULL,
  `address` varchar(128) NOT NULL,
  `city` varchar(128) NOT NULL,
  `country` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Dumping data for table `cities`
--

LOCK TABLES `employees` WRITE;

INSERT INTO `employees` VALUES ('521a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Akron','poom','a@gmail.com','','5464785','finance','team-lead','12/may/1990','abc', 'ghihhdoiohod','Lagos','Nigeria'),('521a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','Douglas','yum','b@gmail.com','','546472266','finance','supervisor','2/may/1991','abc','khdhhuuou','Lagos','Nigeria'),('521a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','San Francisco','oop','yy@gmail.com','','546626286798','hr','worker','12/june/1993','xyz','ahxxhadhskdhhk','Nariobi','Kenya'),('521a55f4-7d82-47d9-b54c-a76916479548','2017-03-25 19:42:41','2017-03-25 19:42:41','Denver','wassy','qqy@gmail.com','','676689795464785','finance','team-lead','12/march/1980','xyz','hsjljklkjsj','Nariobi','Kenya');

UNLOCK TABLES;

-- Dump completed on 2017-03-25 19:42:51
