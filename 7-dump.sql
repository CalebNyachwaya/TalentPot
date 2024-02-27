-- MySQL dump 10.13  Distrib 5.7.8-rc, for Linux (x86_64)
--
-- Host: localhost    Database: hbnb_dev_db
-- ------------------------------------------------------
-- Server version	5.7.8-rc

USE tp_dev_db;

--
-- Table structure for table `cities`
--

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `employees` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `session_created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `first_name` varchar(128) NULL,
  `last_name` varchar(128) NULL,
  `email` varchar(128) NOT NULL,
  `hashed_password` varchar(128) NOT NULL,
  `phone` varchar(128) NULL,
  `dept` varchar(128) NULL,
  `position` varchar(128) NULL,
  `DOB` varchar(128) NULL,
  `company` varchar(128) NULL,
  `address` varchar(128) NULL,
  `city` varchar(128) NULL,
  `session_id` varchar(250) NULL,
  `reset_token` varchar(250) NULL,
  `country` varchar(128) NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cities`
--

/*LOCK TABLES `employees` WRITE;*/
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;

/*INSERT INTO `employees` VALUES ('521a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Akron','poom','a@gmail.com','','5464785','finance','team-lead','12/may/1990','abc', 'ghihhdoiohod','Lagos','Nigeria'),('521a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','Douglas','yum','b@gmail.com','','546472266','finance','supervisor','2/may/1991','abc','khdhhuuou','Lagos','Nigeria'),('521a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','San Francisco','oop','yy@gmail.com','','546626286798','hr','worker','12/june/1993','xyz','ahxxhadhskdhhk','Nariobi','Kenya'),('521a55f4-7d82-47d9-b54c-a76916479548','2017-03-25 19:42:41','2017-03-25 19:42:41','Denver','wassy','qqy@gmail.com','','676689795464785','finance','team-lead','12/march/1980','xyz','hsjljklkjsj','Nariobi','Kenya');*/
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
/*UNLOCK TABLES;*/

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
-- Dump completed on 2017-03-25 19:42:51
