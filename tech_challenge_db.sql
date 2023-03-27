CREATE DATABASE  IF NOT EXISTS `tech_challenge_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tech_challenge_db`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: tech_challenge_db
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car_consumption`
--

DROP TABLE IF EXISTS `car_consumption`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_consumption` (
  `distance` double DEFAULT NULL,
  `consume` double DEFAULT NULL,
  `speed` int DEFAULT NULL,
  `temp_inside` double DEFAULT NULL,
  `temp_outside` int DEFAULT NULL,
  `AC` int DEFAULT NULL,
  `rain` int DEFAULT NULL,
  `sun` int DEFAULT NULL,
  `SP98` int DEFAULT NULL,
  `cost` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_consumption`
--

LOCK TABLES `car_consumption` WRITE;
/*!40000 ALTER TABLE `car_consumption` DISABLE KEYS */;
INSERT INTO `car_consumption` VALUES (28,5,26,21.5,12,0,0,0,0,2.31),(12,4.2,30,21.5,13,0,0,0,0,0.8316),(11.2,5.5,38,21.5,15,0,0,0,0,1.0163999999999997),(12.9,3.9,36,21.5,14,0,0,0,0,0.8301149999999999),(18.5,4.5,46,21.5,15,0,0,0,0,1.3736249999999999),(8.3,6.4,50,21.5,10,0,0,0,0,0.8764799999999999),(7.8,4.4,43,21.5,11,0,0,0,0,0.56628),(12.3,5,40,21.5,6,0,0,0,0,1.01475),(4.9,6.4,26,21.5,4,0,0,0,0,0.51744),(11.9,5.3,30,21.5,9,0,0,0,0,1.040655),(12.4,5.6,42,21.5,4,0,0,0,0,1.14576),(11.8,4.6,38,21.5,0,0,0,0,0,0.8956199999999999),(12.3,5.9,59,21.5,10,0,0,0,0,1.197405),(24.7,5.1,58,21.5,12,0,0,0,0,2.0785049999999994),(12.4,4.7,46,21.5,11,0,0,0,0,0.9616199999999999),(17.3,5.1,24,21.5,5,0,0,0,0,1.455795),(33.4,5.6,36,21.5,3,0,0,0,0,3.086159999999999),(11.8,5.1,32,21.5,3,0,0,0,0,0.9929699999999999),(25.9,4.9,39,21.5,8,0,0,0,0,2.094015),(11.8,4.7,40,21.5,4,0,0,0,0,0.9150900000000001),(25.3,5.5,32,21.5,3,0,0,0,0,2.295975),(14.2,5.9,38,21.5,1,0,0,0,0,1.3823699999999999),(17.9,5.7,37,21.5,1,0,0,0,0,1.683495),(11.8,4.7,36,21.5,1,0,0,0,0,0.9150900000000001),(12.3,5.9,62,21.5,6,0,0,0,0,1.197405),(12.4,4.1,57,21.5,9,0,0,0,0,0.8388599999999999),(18.4,5.7,21,22.5,2,0,0,0,0,1.7305199999999998),(18.4,5.8,28,21.5,3,0,0,0,0,1.7608799999999998),(18.3,5.5,29,21.5,1,0,0,0,0,1.6607249999999998),(18.4,5.7,35,21.5,4,0,0,0,0,1.7305199999999998),(12.3,5.3,51,21.5,11,0,0,0,0,1.075635),(11.8,5,29,21.5,10,0,0,0,0,0.9735),(12.3,5.6,58,21.5,8,0,0,0,0,1.13652),(32.6,4.8,40,21.5,7,0,0,0,0,2.5819199999999998),(19,4.3,36,21.5,7,0,0,0,0,1.3480499999999997),(12.1,5.7,36,21.5,8,0,0,0,0,1.138005),(20,5.2,37,21.5,4,0,0,0,0,1.716),(4.9,7.4,26,21.5,6,0,0,0,0,0.59829),(11.8,4.8,23,21.5,9,0,0,0,0,0.93456),(12.3,6.5,58,21.5,7,0,0,0,0,1.319175),(12.4,4,55,21.5,7,1,1,0,0,0.8183999999999999),(4.5,5,29,21.5,7,1,0,0,0,0.37124999999999997),(11.7,4.6,37,21.5,6,0,0,0,0,0.8880299999999998),(10.2,4.3,44,21.5,7,0,0,0,0,0.7236899999999998),(5.4,3.3,32,21.5,7,0,0,0,1,0.3170178),(2,9.9,21,21.5,4,0,0,0,1,0.352242),(14.2,5.1,32,21.5,7,0,0,0,1,1.2883517999999996),(16,4.9,25,21.5,8,0,0,0,1,1.394736),(11.8,4.9,25,21.5,11,0,0,0,1,1.0286178000000001),(27.3,4.7,36,21.5,10,0,0,0,1,2.2826349),(11.8,5.1,29,21.5,5,0,1,0,1,1.0706022),(10.6,4.9,63,21.5,6,0,0,0,1,0.9240126),(11.6,4.2,61,21.5,7,0,0,0,1,0.8667287999999999),(13.1,6.1,46,21.5,6,0,1,0,1,1.4215989),(6.1,6.4,28,21.5,8,0,0,0,1,0.6945216),(153.5,4.9,82,21.5,3,0,1,0,1,13.380748500000001),(11.8,4.9,24,21.5,7,0,0,0,1,1.0286178000000001),(12.3,6.2,61,21.5,8,0,0,0,1,1.3566654),(12.4,4.2,57,21.5,8,0,0,0,1,0.9265032000000001),(12.3,5.7,52,21.5,8,0,1,0,1,1.2472569),(2.9,7.9,18,21.5,9,1,1,0,1,0.40756889999999996),(2.1,12.2,23,21.5,9,1,1,0,1,0.45577979999999996),(9.8,5.8,24,21.5,6,0,0,0,1,1.0111836),(6.8,5.3,26,21.5,6,0,0,0,1,0.6411515999999999),(12.4,5.4,24,21.5,7,0,0,0,1,1.1912184000000001),(12.4,4.7,57,21.5,8,0,0,0,1,1.0368012),(11.8,4.6,41,21.5,6,0,0,0,1,0.9656411999999999),(12.3,5.4,55,21.5,8,0,0,0,1,1.1816118000000002),(14,4.3,40,21.5,8,0,0,0,1,1.0709579999999999),(11.8,4.5,37,21.5,4,1,0,0,1,0.944649),(12.3,5.2,55,21.5,12,0,0,0,1,1.1378484),(2,6.2,20,21.5,10,0,0,0,1,0.22059600000000001),(13.9,5.1,29,21.5,6,0,0,0,1,1.2611331),(9.7,3.9,42,21.5,8,0,0,0,1,0.6729956999999999),(11.6,5,25,21.5,6,0,0,0,1,1.03182),(14.2,5.4,38,21.5,7,0,0,0,1,1.3641372),(11.8,4.5,39,21.5,6,0,0,0,1,0.944649),(24.8,5.1,50,21.5,9,0,0,0,1,2.2500791999999996),(12.4,4.7,56,21.5,7,0,0,0,1,1.0368012),(34.8,4,28,20,4,0,0,0,1,2.476368),(14.2,5.4,36,20,6,0,0,0,1,1.3641372),(5.2,4.5,39,20,10,0,0,0,1,0.416286),(10.5,3.6,42,20,10,0,0,0,1,0.672462),(12.3,5.2,57,20,10,0,0,0,1,1.1378484),(11.8,4.9,25,20,11,0,0,0,1,1.0286178000000001),(12.3,6.2,58,20,11,0,1,0,1,1.3566654),(13.2,4.3,51,20,11,0,1,0,1,1.0097604),(13,5,45,20,11,0,1,0,1,1.15635),(12.9,5.1,32,20,11,0,0,0,1,1.1704040999999998),(13.9,5.6,22,20,8,0,0,0,1,1.3847736),(11.8,4.3,37,20,6,0,0,0,1,0.9026645999999999),(12.2,5.8,60,20,11,0,0,0,1,1.2588204),(12.5,4,51,20,13,0,0,0,1,0.8895),(11.8,5.9,21,20,9,1,1,0,1,1.2385398),(12.5,4.2,57,20,11,0,0,0,1,0.933975),(26.2,5.8,71,21,8,1,1,0,1,2.7033684),(4.9,6.9,25,21,12,0,1,0,1,0.6014799),(12.4,5.4,18,21,11,1,1,0,1,1.1912184000000001),(22.9,5.3,45,20.5,7,0,0,0,1,2.1591722999999994),(162.7,5.5,75,23,1,0,0,0,1,15.919381499999998),(4.9,6.5,26,21,1,0,0,0,1,0.5666114999999999),(11.8,4.7,36,21,4,0,0,0,1,0.9866334000000001),(16.6,5.1,56,21,7,0,0,0,1,1.5061014),(12.4,5.7,37,21,7,0,0,0,1,1.2573972),(15.9,5.4,25,21,7,0,0,0,1,1.5274494),(5.1,8.7,21,23.5,5,0,0,0,1,0.7893422999999998),(22.4,4.9,66,20.5,7,0,0,0,1,1.9526303999999997),(31.1,4.7,42,20.5,7,0,0,0,1,2.6003643),(4.9,6.3,27,20.5,3,0,0,0,1,0.5491773),(11.8,5.1,26,23,4,0,1,0,1,1.0706022),(22.9,6,42,23,4,0,1,0,1,2.4443459999999995),(12.4,4.6,38,23,1,0,1,0,1,1.0147415999999998),(12.9,5.8,40,23,4,0,0,0,1,1.3310478),(11.8,5.1,43,23,0,0,0,0,1,1.0706022),(12.2,5.8,58,23,2,0,0,0,1,1.2588204),(24.8,4.6,55,23,3,0,0,0,1,2.0294831999999996),(14.2,5.6,24,23,8,0,0,0,1,1.4146607999999998),(11.8,4.6,38,23,0,0,1,0,1,0.9656411999999999),(12.2,6.3,57,23,0,0,1,0,1,1.3673393999999999),(24.7,5.5,56,25,1,0,0,0,1,2.4167715),(6.8,4.3,46,24,2,0,0,0,1,0.5201796),(17.3,5.6,37,21.5,1,0,0,0,1,1.7234952),(11.8,4.3,44,21.5,-3,0,0,0,1,0.9026645999999999),(15.9,5.7,46,21.5,5,0,0,0,1,1.6123077),(5.1,6.4,39,21.5,4,0,0,0,1,0.5806656),(16.1,4.5,33,21.5,6,0,0,0,1,1.2888855),(11.8,4.5,43,21.5,3,0,0,0,1,0.944649),(4.2,6,26,21.5,5,0,0,0,1,0.448308),(17.4,5.1,30,21.5,5,0,0,0,1,1.5786845999999997),(23.5,6,25,21.5,5,0,1,0,1,2.50839),(11.8,4.5,38,21.5,5,0,1,0,1,0.944649),(12.3,6.1,61,21.5,10,0,1,0,1,1.3347837),(16.1,5.4,24,21.5,7,0,1,0,0,1.43451),(11.8,4.3,40,21.5,10,0,1,0,0,0.8372099999999999),(12.3,5.4,58,21.5,13,0,0,0,0,1.09593),(12.4,4.3,49,21.5,17,0,0,0,0,0.87978),(7,5.2,25,21.5,17,0,0,0,0,0.6006),(11.8,4.1,37,21.5,10,0,0,0,0,0.7982699999999999),(20.1,4.4,41,21.5,18,0,0,0,0,1.45926),(20.8,4.5,45,21.5,10,0,0,0,0,1.5444),(1.7,10.8,14,21.5,10,0,1,0,0,0.30294),(35.9,4.7,45,21.5,12,0,0,0,0,2.784045),(36.9,4.8,52,21.5,5,0,0,0,0,2.9224799999999997),(16.8,4,46,21.5,8,0,0,0,0,1.1088),(9.9,5,28,21.5,9,0,0,0,0,0.81675),(22.9,4.6,61,21.5,7,0,1,0,0,1.7381099999999998),(17.3,5,61,21.5,6,1,1,0,0,1.4272500000000001),(11.8,4.3,37,21.5,7,0,0,0,0,0.8372099999999999),(36.6,5.2,80,21.5,7,0,1,0,0,3.1402799999999997),(44.9,4.7,62,21.5,8,0,0,0,0,3.481995),(11.8,4.2,34,21.5,9,0,1,0,0,0.81774),(21.6,5.3,44,21.5,9,0,1,0,0,1.88892),(39.4,5.3,60,21.5,9,0,1,0,0,3.4455299999999993),(5.1,8.1,39,21.5,4,0,0,0,0,0.6816149999999999),(26.6,4.8,38,21.5,7,0,0,0,0,2.1067199999999997),(53.2,5.1,71,21.5,2,0,0,0,0,4.47678),(18.9,4.4,53,21.5,2,0,0,0,0,1.37214),(43.5,5,80,21.5,3,0,0,0,0,3.5887499999999997),(6.1,6.3,26,21.5,5,0,0,0,0,0.634095),(16.4,4.8,49,21.5,5,0,0,0,0,1.2988799999999998),(12.3,6.1,40,21.5,6,0,0,0,0,1.237995),(21.1,4.6,36,21.5,8,0,0,0,0,1.6014899999999999),(21.1,4.8,43,21.5,7,0,0,0,0,1.6711200000000002),(22.7,4.7,55,21.5,6,0,0,0,0,1.7603849999999999),(44.4,4.8,38,21.5,8,0,0,0,0,3.5164799999999996),(35.8,4.4,51,21.5,6,0,0,0,0,2.5990800000000003),(11.8,4.9,44,21.5,0,0,0,0,0,0.95403),(26.2,4.9,42,21.5,6,0,0,0,0,2.11827),(40.6,4.4,44,21,3,0,0,0,0,2.94756),(12.4,5.3,38,21,-5,0,0,0,0,1.08438),(14.1,5.3,47,21,-3,0,0,0,0,1.2330449999999997),(58.7,4.8,75,21,0,0,0,0,0,4.64904),(16.2,5.2,29,21,0,0,0,0,0,1.38996),(12.3,4.9,50,22.5,0,0,0,0,0,0.9944550000000002),(12.3,7.1,52,22.5,0,1,1,0,0,1.4409450000000001),(12.4,5.2,51,22.5,1,0,0,0,0,1.06392),(31.8,4.7,59,22.5,3,0,0,0,0,2.4660900000000003),(12.3,5.1,55,22.5,8,0,0,0,0,1.035045),(51.6,5,73,22.5,12,0,0,0,0,4.257),(38.6,4.6,44,22.5,10,0,0,0,0,2.92974),(12.3,4.8,41,22.5,7,0,0,0,0,0.97416),(81.2,4.4,69,22,13,0,0,0,0,5.89512),(130.3,4.6,85,22,12,0,0,0,0,9.88977),(67.2,4.3,67,22,18,0,0,0,0,4.76784),(43.7,4.7,44,22,9,0,1,0,1,3.6538881000000005),(12.1,4.2,43,22,4,0,0,0,1,0.9040877999999999),(56.1,4.8,82,22,13,0,0,0,1,4.7904912),(39,4.1,61,22,16,0,0,0,1,2.8446209999999996),(11.8,4.5,41,21.5,13,0,0,0,1,0.944649),(38.5,4.8,63,21.5,14,0,0,0,1,3.2875919999999996),(28.2,4.6,54,21.5,14,0,0,0,1,2.3077187999999995),(2.9,7.4,24,21.5,14,0,0,0,1,0.38177339999999993),(6.1,5.6,24,21.5,13,0,0,0,1,0.6077063999999999),(19.6,4.9,43,21.5,13,0,0,0,1,1.7085516000000003),(13.6,4.5,44,19,18,0,0,0,1,1.088748),(8.7,5.3,28,22.5,12,1,1,0,1,0.8202968999999999),(7.9,4.7,31,22.5,12,1,0,0,1,0.6605427),(2.4,9,26,20,10,0,0,0,1,0.384264),(4.9,6.3,26,20,10,0,0,0,1,0.5491773),(18.1,3.6,36,20,19,0,0,0,1,1.1591964000000001),(25.9,3.7,39,20,21,0,0,0,1,1.7048157),(1.3,11.5,21,20,10,0,0,0,1,0.26596050000000004),(14.1,5,22,20,12,0,0,0,1,1.254195),(13.4,5.5,31,20,9,0,0,0,1,1.311123),(6.4,4.7,33,20,8,0,0,0,1,0.5351232),(12.9,4.5,42,20,13,0,0,0,1,1.0327095),(12.1,4.4,33,22.5,5,0,0,0,1,0.9471396),(15.7,4.1,32,22.5,13,0,0,0,1,1.1451422999999998),(16.2,4.4,26,22.5,11,0,0,0,1,1.2680712),(12.8,4.6,22,22.5,12,0,0,0,1,1.0474751999999998),(19,4.4,58,22.5,17,0,0,1,1,1.487244),(29,4,27,22.5,12,0,0,0,1,2.06364),(12.1,5,32,22.5,9,0,0,0,1,1.076295),(12.3,5.2,55,22.5,10,0,0,0,1,1.1378484),(24.8,4,56,22.5,11,0,0,0,1,1.764768),(12.9,5.1,34,22.5,8,0,1,0,1,1.1704040999999998),(11.8,4.5,39,22.5,3,0,0,0,1,0.944649),(31.4,4.6,62,22.5,11,0,0,0,1,2.5695875999999997),(19,5.1,53,22.5,4,0,1,0,1,1.7238509999999998),(13,5.7,38,22.5,3,1,1,0,1,1.3182390000000002),(11.8,4.8,42,22.5,2,0,0,0,1,1.0076256),(13,6.2,32,22.5,4,0,0,0,1,1.433874),(11.8,5,43,22.5,1,0,0,0,1,1.0496100000000002),(27.1,5,69,22.5,8,0,0,0,1,2.410545),(5.2,4.6,38,22.5,8,0,0,0,1,0.4255368),(19,4.5,29,22.5,10,0,0,0,0,1.41075),(12.4,4.8,38,22.5,1,0,0,0,0,0.9820799999999998),(25.2,5,55,22.5,9,0,0,0,0,2.0789999999999997),(14.3,4.8,36,22.5,10,0,0,0,0,1.13256),(11.8,4.6,40,22.5,2,0,0,0,0,0.8956199999999999),(16.9,4.5,48,22.5,9,0,0,1,0,1.2548249999999999),(12.4,4.6,55,22.5,11,0,0,1,0,0.9411599999999998),(17.4,4.4,36,22.5,12,0,0,1,0,1.26324),(9.2,5.7,33,22.5,8,0,1,0,0,0.8652599999999999),(12.3,5.8,54,22.5,10,0,1,0,0,1.17711),(13,5.9,32,22.5,10,0,0,0,0,1.2655500000000002),(11.8,6.1,16,22.5,6,0,1,0,0,1.18767),(13,5.7,37,22.5,11,0,1,0,0,1.22265),(12.3,5,42,22.5,10,0,0,0,0,1.01475),(12.3,5.2,57,22.5,15,0,0,1,0,1.05534),(12.5,4.3,57,22.5,16,0,0,1,0,0.886875),(31.5,4.1,30,22.5,16,0,0,1,0,2.130975),(11.8,4.4,42,22.5,8,0,0,0,0,0.8566800000000001),(24.9,4.5,53,22.5,14,0,0,0,0,1.848825),(17,3.9,46,22.5,14,0,0,1,0,1.09395),(2,8.1,20,22.5,14,0,0,0,0,0.2673),(11.8,4.4,33,22.5,8,0,0,0,0,0.8566800000000001),(7.4,5,31,22.5,12,0,0,0,0,0.6105),(12.4,4.7,55,22.5,14,0,0,1,0,0.9616199999999999),(2,6,22,22.5,14,0,0,0,0,0.19799999999999998),(14,5,41,22.5,8,0,0,0,0,1.155),(25.7,5,45,22.5,7,0,0,0,0,2.12025),(11.8,4.5,28,22.5,12,0,0,0,0,0.87615),(4.1,5.4,24,22.5,13,0,0,0,0,0.36530999999999997),(4.2,5.6,29,22,17,0,0,0,0,0.38808),(4.2,3.9,29,22,18,0,0,1,0,0.27027),(16,4,40,22,10,0,0,0,0,1.056),(15.4,4.5,50,22,14,0,0,0,0,1.1434499999999999),(16,3.8,41,22,12,0,0,0,0,1.0031999999999999),(4.2,5.6,32,22,18,0,0,0,0,0.38808),(101.9,5.2,75,22,18,0,0,0,0,8.743020000000001),(93.9,4.8,88,23,18,1,0,1,0,7.4368799999999995),(25.7,4.9,50,22,10,0,1,0,1,2.2402947),(16,4.1,40,22,10,0,0,0,1,1.1670239999999998),(16.1,4.5,32,22,19,0,0,0,1,1.2888855),(16,4.4,40,22,7,1,1,0,1,1.252416),(16,4.5,41,22,11,0,0,0,1,1.2808799999999998),(24.7,4.5,26,22,10,0,0,0,1,1.9773584999999998),(16,3.9,42,22,8,0,0,0,1,1.110096),(15.4,4.6,43,22,16,0,0,0,1,1.2602435999999997),(16,3.8,40,22,8,0,0,0,1,1.081632),(32.1,4.5,50,22,16,0,0,0,1,2.5697655),(25.9,4.4,40,22,14,0,0,0,1,2.0273484),(48.6,4.3,44,22,12,0,0,0,1,3.7177541999999995),(37.2,4,45,22,20,0,0,1,1,2.647152),(28.8,3.9,35,22,15,0,0,1,1,1.9981728000000003),(6.7,5,30,22,17,0,0,0,1,0.595965),(7.4,4.1,25,22,18,0,0,1,1,0.5397486),(17.3,4.1,22,22,25,0,0,1,1,1.2618447),(6.6,5.6,43,22,16,0,0,0,1,0.6575184),(14.3,4.1,26,22,20,0,0,0,1,1.0430277000000001),(13.3,4.6,33,22,18,0,0,0,1,1.0883922),(8.3,4.9,26,22,23,0,0,0,1,0.7235193000000001),(12.7,4.5,39,22,27,0,0,1,1,1.0166985),(16.5,4.1,47,22,14,0,0,0,1,1.2034935),(20.6,4.1,38,22,21,0,0,0,1,1.5025434),(16.3,4.5,58,22,16,0,0,0,1,1.3048965),(18.7,4.2,65,25,18,1,0,1,1,1.3972266),(36.5,3.9,54,23,18,0,0,1,1,2.5324065),(19,5,35,22,15,1,0,1,1,1.6900499999999998),(16.6,4.4,46,22,5,1,0,0,1,1.2993816),(29.9,4.5,32,22,18,1,0,0,1,2.3936444999999997),(16,3.8,42,22,11,0,0,0,1,1.081632),(21.1,5.1,33,22,10,0,1,0,1,1.9143819),(16,3.9,40,22,10,0,0,0,1,1.110096),(11.9,5.3,34,22,13,0,0,0,1,1.1220153),(10.1,4.2,35,22,16,0,0,0,1,0.7546517999999999),(31.9,4.3,33,22,16,0,0,0,1,2.4402543),(18.7,4,60,22,13,0,0,0,1,1.330692),(10.8,4.7,48,22,17,0,0,1,1,0.9030204000000001),(19.8,4,56,22,17,0,0,1,1,1.408968),(11.3,4.3,38,22,17,0,0,0,1,0.8644160999999999),(11.5,5.3,53,22,15,0,0,0,1,1.0843005000000001),(21.4,5.2,51,22,13,0,0,0,1,1.9796711999999999),(32,4.9,53,22,15,0,0,0,1,2.789472),(41.9,4.7,53,22,14,0,0,0,1,3.5033847),(211,4.6,80,22,20,0,0,0,1,17.266973999999998),(216.1,5.3,90,22,21,0,0,1,1,20.3754207),(25.5,3.6,27,22,27,0,0,1,1,1.633122),(16.6,4.2,52,22,15,0,1,0,1,1.2403188),(25.9,4.1,43,22,24,0,0,0,1,1.8891200999999995),(16.5,4,48,22,15,0,0,0,1,1.17414),(22.1,3.9,29,22,26,0,0,0,1,1.5333200999999999),(16.6,3.7,49,22,17,0,0,0,0,1.01343),(15.4,4.5,43,22,24,0,0,0,0,1.1434499999999999),(16.5,3.9,43,22,17,0,0,0,0,1.061775),(15.4,5.1,21,22,24,0,0,0,0,1.29591),(18.4,4.2,59,22,24,0,0,0,0,1.27512),(39.5,4.2,58,22,25,0,0,0,0,2.73735),(21.5,4.8,47,25,27,1,0,1,0,1.7027999999999999),(4.8,4.7,26,25,18,0,0,0,0,0.37224),(100.9,4.7,87,23.5,22,0,0,0,0,7.824795000000002),(129.7,4.6,58,24,21,0,0,0,0,9.844229999999998),(16.6,3.8,43,21.5,16,0,0,0,0,1.04082),(15.4,4.2,50,21.5,21,0,0,0,0,1.06722),(16,3.7,45,22,17,0,0,0,0,0.9768000000000001),(16,4.2,41,22,15,0,0,0,0,1.1088),(15.4,4.1,45,22,24,0,0,0,0,1.04181),(16,4,43,22,16,0,0,0,0,1.056),(21,3.8,37,22,21,0,0,0,0,1.3166999999999998),(15.4,3.8,47,22,24,0,0,0,0,0.9655799999999999),(16,3.8,42,22,17,0,0,0,0,1.0031999999999999),(16.1,5.1,30,25,16,1,1,0,0,1.3548149999999999),(16,4,42,22,15,0,0,0,0,1.056),(15.4,4.8,40,22,18,0,0,0,0,1.2196799999999999),(17.2,3.9,35,22,16,0,0,0,0,1.10682),(16.6,4.6,50,22,25,0,0,0,0,1.2599399999999998),(18.3,4.3,46,22,16,0,0,0,1,1.3998950999999997),(16.1,4.8,36,22,18,0,1,0,1,1.3748112),(16,4.1,46,22,17,0,0,0,1,1.1670239999999998),(16.3,4,35,22,23,0,0,0,1,1.159908),(16,3.7,44,22,16,0,0,0,1,1.053168),(18.3,4.3,46,22,23,0,0,0,1,1.3998950999999997),(4.5,5.2,23,22,23,0,0,1,1,0.41628599999999993),(17,4.2,48,22,16,0,0,0,1,1.2702060000000002),(6.1,5,35,24.5,18,0,0,0,1,0.5425949999999999),(6.1,5,33,22,24,0,0,1,1,0.5425949999999999),(17.3,4.2,36,22,22,0,0,0,1,1.2926214000000003),(6,4.8,27,22,17,0,0,0,1,0.5123519999999999),(16,4.1,45,22,15,0,0,0,1,1.1670239999999998),(15.4,4.9,55,22,18,0,0,0,1,1.3424334),(15.4,4.3,39,22,23,0,0,0,1,1.1780538),(16,3.9,35,22,18,0,0,0,1,1.110096),(15.4,4.5,52,22,26,0,0,0,1,1.2328469999999998),(16.6,4.1,48,25.5,30,1,0,1,1,1.2107873999999998),(15.4,5,48,25.5,31,1,0,0,1,1.3698299999999999),(16,4,43,22,21,1,0,0,1,1.13856),(15.4,4.5,42,22,30,0,0,0,1,1.2328469999999998),(16,3.6,43,22,19,0,0,0,1,1.024704),(20.9,4.1,33,22,21,0,0,0,1,1.5244250999999998),(32.1,3.9,47,22,26,0,0,0,1,2.2271301),(15.3,6.6,16,24,27,1,0,0,1,1.7964342),(28.5,4,44,25,23,1,0,0,1,2.0280599999999995),(11.9,3.7,33,25,19,0,0,0,1,0.7832937000000001),(14.5,4.3,36,25,22,0,0,0,1,1.1092064999999998),(16.6,4.1,49,22,26,0,0,1,1,1.2107873999999998),(16.2,4.4,39,24.5,17,1,0,0,1,1.2680712),(16.7,3.8,44,24.5,23,0,0,1,1,1.1289533999999999),(8.3,5,52,24.5,27,0,0,0,1,0.7382850000000001),(5.5,3.7,33,24.5,28,0,0,1,1,0.36202650000000003),(13.6,3.7,33,24.5,28,0,0,1,1,0.8951928000000001),(16,3.7,39,24.5,18,0,0,0,1,1.053168),(16.1,4.3,38,25,31,1,0,0,1,1.2316017),(16,3.8,45,25,19,0,0,0,1,1.081632),(15.4,4.6,42,25,31,1,0,0,1,1.2602435999999997),(14.7,5,25,25,30,1,0,0,1,1.3075649999999999),(12.4,4.7,43,21.72988693801386,10,0,0,0,1,1.0368012),(11.8,5.3,52,21.731760478708143,11,0,0,0,1,1.1125866),(15.7,5.3,33,21.643106174106524,9,0,0,0,1,1.4803058999999998),(12.9,5.7,35,21.612532721679933,9,0,0,0,1,1.3080987),(6.4,4.4,37,21.73731764488953,10,0,0,0,1,0.5009664),(5.3,4.1,34,21.71796659179536,9,0,0,0,1,0.38657669999999994),(18.8,5,62,21.644610478274032,9,0,1,0,1,1.6722599999999999),(22.2,3.8,42,21.98939035553239,15,0,0,0,1,1.5007644),(12.6,4.1,33,22.01809411506524,17,0,0,0,1,0.9190313999999998),(24.5,3.9,50,22.548040566726428,15,0,0,1,0,1.5765749999999998),(22.9,4,29,22.30455713612761,21,0,0,0,0,1.5113999999999999),(16,3.8,42,21.850344244155337,8,0,0,0,0,1.0031999999999999);
/*!40000 ALTER TABLE `car_consumption` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-27 12:51:25
