CREATE DATABASE  IF NOT EXISTS `projectbd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `projectbd`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: projectbd
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `komandi`
--

DROP TABLE IF EXISTS `komandi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `komandi` (
  `Номер команды` int NOT NULL,
  `Название команды` varchar(45) NOT NULL,
  `Номер задачи` int NOT NULL,
  `Номер модератора` int NOT NULL,
  PRIMARY KEY (`Номер команды`),
  KEY `index2` (`Номер модератора`,`Номер задачи`),
  KEY `fk_Команды_2_idx` (`Номер задачи`),
  CONSTRAINT `fk_Команды_1` FOREIGN KEY (`Номер модератора`) REFERENCES `moderatori` (`ID Модератора`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Команды_2` FOREIGN KEY (`Номер задачи`) REFERENCES `zadachi` (`Номер задачи`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `komandi`
--

LOCK TABLES `komandi` WRITE;
/*!40000 ALTER TABLE `komandi` DISABLE KEYS */;
/*!40000 ALTER TABLE `komandi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moderatori`
--

DROP TABLE IF EXISTS `moderatori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moderatori` (
  `ID Модератора` int NOT NULL,
  `Фамилия модератора` varchar(45) NOT NULL,
  `Имя модератора` varchar(45) NOT NULL,
  `Отчество модератора` varchar(45) NOT NULL,
  `Электронная почта` varchar(45) NOT NULL,
  `Логин` varchar(45) NOT NULL,
  `Пароль` varchar(45) NOT NULL,
  `Номер телефона` char(10) NOT NULL,
  PRIMARY KEY (`ID Модератора`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moderatori`
--

LOCK TABLES `moderatori` WRITE;
/*!40000 ALTER TABLE `moderatori` DISABLE KEYS */;
/*!40000 ALTER TABLE `moderatori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ocenki_resheniya_zadach`
--

DROP TABLE IF EXISTS `ocenki_resheniya_zadach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ocenki_resheniya_zadach` (
  `Порядок оценивания` int NOT NULL,
  `Этап` varchar(45) NOT NULL,
  `Номер команды` int NOT NULL,
  `Номер задачи` int NOT NULL,
  `Время начала` varchar(45) NOT NULL,
  `Результат этапа` varchar(45) NOT NULL,
  `Экспертная оценка` int NOT NULL,
  `Результирующая оценка` int NOT NULL,
  `Хранилище решения (ссылка)` varchar(45) NOT NULL,
  PRIMARY KEY (`Порядок оценивания`),
  UNIQUE KEY `index2` (`Номер команды`,`Номер задачи`),
  KEY `fk_Оценки_решения_задач_1_idx` (`Номер задачи`),
  CONSTRAINT `fk_Оценки_решения_задач_1` FOREIGN KEY (`Номер задачи`) REFERENCES `zadachi` (`Номер задачи`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Оценки_решения_задач_2` FOREIGN KEY (`Номер команды`) REFERENCES `komandi` (`Номер команды`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ocenki_resheniya_zadach`
--

LOCK TABLES `ocenki_resheniya_zadach` WRITE;
/*!40000 ALTER TABLE `ocenki_resheniya_zadach` DISABLE KEYS */;
/*!40000 ALTER TABLE `ocenki_resheniya_zadach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organizacii-uchastniki`
--

DROP TABLE IF EXISTS `organizacii-uchastniki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organizacii-uchastniki` (
  `Номер организации-участника` int NOT NULL,
  `Название организации` varchar(45) NOT NULL,
  `Фамилия руководителя` varchar(45) NOT NULL,
  `Имя руководителя` varchar(45) NOT NULL,
  `Отчество руководителя` varchar(45) NOT NULL,
  `Электронная почта организации` varchar(45) NOT NULL,
  `Ссылка на сайт организации` varchar(45) DEFAULT NULL,
  `Номер письма` int NOT NULL,
  `Что может предоставить` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Номер организации-участника`),
  UNIQUE KEY `Номер письма_UNIQUE` (`Номер письма`),
  KEY `fk_Организации-участники_1_idx` (`Номер письма`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_Организации-участники_1` FOREIGN KEY (`Номер письма`) REFERENCES `priglashennie_organizacii` (`Номер письма`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizacii-uchastniki`
--

LOCK TABLES `organizacii-uchastniki` WRITE;
/*!40000 ALTER TABLE `organizacii-uchastniki` DISABLE KEYS */;
/*!40000 ALTER TABLE `organizacii-uchastniki` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `predstaviteli_organizacii`
--

DROP TABLE IF EXISTS `predstaviteli_organizacii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `predstaviteli_organizacii` (
  `ID Представителя организации` int NOT NULL,
  `Фамилия представителя организации` varchar(45) NOT NULL,
  `Имя представителя организации` varchar(45) NOT NULL,
  `Отчество представителя организации` varchar(45) NOT NULL,
  `Электронная почта представителя организации` varchar(45) NOT NULL,
  `Номер организации` int NOT NULL,
  `Должность` varchar(45) DEFAULT NULL,
  `Статус на мероприятии` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID Представителя организации`),
  KEY `fk_Представители_организаций_1` (`Номер организации`),
  CONSTRAINT `fk_Представители_организаций_1` FOREIGN KEY (`Номер организации`) REFERENCES `organizacii-uchastniki` (`Номер организации-участника`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `predstaviteli_organizacii`
--

LOCK TABLES `predstaviteli_organizacii` WRITE;
/*!40000 ALTER TABLE `predstaviteli_organizacii` DISABLE KEYS */;
/*!40000 ALTER TABLE `predstaviteli_organizacii` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `priglashennie_organizacii`
--

DROP TABLE IF EXISTS `priglashennie_organizacii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `priglashennie_organizacii` (
  `Номер письма` int NOT NULL,
  `Название организации` varchar(45) NOT NULL,
  `Фамилия руководителя` varchar(45) NOT NULL,
  `Имя руководителя` varchar(45) NOT NULL,
  `Отчество руководителя` varchar(45) NOT NULL,
  `Электронная почта организации` varchar(45) DEFAULT NULL,
  `Тема письма` varchar(45) NOT NULL,
  `Дата отправки письма` date NOT NULL,
  `Участник (Да/Нет)` tinyint DEFAULT NULL,
  PRIMARY KEY (`Номер письма`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `priglashennie_organizacii`
--

LOCK TABLES `priglashennie_organizacii` WRITE;
/*!40000 ALTER TABLE `priglashennie_organizacii` DISABLE KEYS */;
/*!40000 ALTER TABLE `priglashennie_organizacii` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uchastniki`
--

DROP TABLE IF EXISTS `uchastniki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uchastniki` (
  `ID Участника` int NOT NULL,
  `Фамилия участника` varchar(45) NOT NULL,
  `Имя участника` varchar(45) NOT NULL,
  `Отчество участника` varchar(45) NOT NULL,
  `Дата рождения` date NOT NULL,
  `Место обучения` varchar(45) DEFAULT NULL,
  `Место работы` varchar(45) DEFAULT NULL,
  `Электронная почта` varchar(45) NOT NULL,
  `Логин` varchar(45) NOT NULL,
  `Пароль` varchar(45) NOT NULL,
  `Номер команды` int NOT NULL,
  PRIMARY KEY (`ID Участника`),
  KEY `fk_Участники_1` (`Номер команды`),
  CONSTRAINT `fk_Участники_1` FOREIGN KEY (`Номер команды`) REFERENCES `komandi` (`Номер команды`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uchastniki`
--

LOCK TABLES `uchastniki` WRITE;
/*!40000 ALTER TABLE `uchastniki` DISABLE KEYS */;
/*!40000 ALTER TABLE `uchastniki` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zadachi`
--

DROP TABLE IF EXISTS `zadachi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zadachi` (
  `Номер задачи` int NOT NULL,
  `Категория` varchar(45) NOT NULL,
  `Номер организации-участника` int NOT NULL,
  PRIMARY KEY (`Номер задачи`),
  UNIQUE KEY `Index3` (`Номер задачи`),
  KEY `index2` (`Номер организации-участника`),
  CONSTRAINT `fk_Задачи_1` FOREIGN KEY (`Номер организации-участника`) REFERENCES `organizacii-uchastniki` (`Номер организации-участника`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zadachi`
--

LOCK TABLES `zadachi` WRITE;
/*!40000 ALTER TABLE `zadachi` DISABLE KEYS */;
/*!40000 ALTER TABLE `zadachi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-17 21:10:07
