CREATE DATABASE  IF NOT EXISTS `bd_itermobi` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `bd_itermobi`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bd_itermobi
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.17-MariaDB

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
-- Table structure for table `onibus`
--

DROP TABLE IF EXISTS `onibus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `onibus` (
  `id_onibus` int(50) NOT NULL,
  `empresa` varchar(30) NOT NULL,
  PRIMARY KEY (`id_onibus`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onibus`
--

LOCK TABLES `onibus` WRITE;
/*!40000 ALTER TABLE `onibus` DISABLE KEYS */;
INSERT INTO `onibus` (`id_onibus`, `empresa`) VALUES (372,'São Miguel');
/*!40000 ALTER TABLE `onibus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trajeto_onibus`
--

DROP TABLE IF EXISTS `trajeto_onibus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trajeto_onibus` (
  `id_trajeto_onibus` varchar(5) NOT NULL,
  `trajeto_id` varchar(5) NOT NULL,
  PRIMARY KEY (`id_trajeto_onibus`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trajeto_onibus`
--

LOCK TABLES `trajeto_onibus` WRITE;
/*!40000 ALTER TABLE `trajeto_onibus` DISABLE KEYS */;
INSERT INTO `trajeto_onibus` (`id_trajeto_onibus`, `trajeto_id`) VALUES ('372A','372'),('372B','372'),('372C','372'),('372D','372');
/*!40000 ALTER TABLE `trajeto_onibus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trajetos`
--

DROP TABLE IF EXISTS `trajetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trajetos` (
  `id_trajeto_onibus` varchar(5) NOT NULL,
  `trajeto` varchar(30) NOT NULL,
  `id_onibus` varchar(5) NOT NULL,
  PRIMARY KEY (`id_trajeto_onibus`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trajetos`
--

LOCK TABLES `trajetos` WRITE;
/*!40000 ALTER TABLE `trajetos` DISABLE KEYS */;
INSERT INTO `trajetos` (`id_trajeto_onibus`, `trajeto`, `id_onibus`) VALUES ('372A','Primavera via Itapuca','372'),('372B','Parque Minas Gerais','372'),('372C','Rodoviária / Faz. Barra 3','372'),('372D','Rodoviária / Primavera','372');
/*!40000 ALTER TABLE `trajetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(200) NOT NULL,
  `senha` varchar(200) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id_usuario`, `nome`, `email`, `senha`) VALUES (1,'emanuel','emanulucio@gmail.com','202ef218mn194ab55nm234uv2887288710656');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'bd_itermobi'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-13 22:29:47
