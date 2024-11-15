-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.1.0 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for url_prediction
CREATE DATABASE IF NOT EXISTS `url_prediction` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `url_prediction`;

-- Dumping structure for table url_prediction.contact_queries
CREATE TABLE IF NOT EXISTS `contact_queries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` text NOT NULL,
  `submitted_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table url_prediction.contact_queries: ~1 rows (approximately)
INSERT INTO `contact_queries` (`id`, `name`, `email`, `message`, `submitted_at`) VALUES
	(1, 'vfvf', 'aparajita@ssipmt.com', 'dfvfbfggbsrgtbrth', '2024-08-08 14:13:53');

-- Dumping structure for table url_prediction.reported_urls
CREATE TABLE IF NOT EXISTS `reported_urls` (
  `id` int NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `prediction_percentage` decimal(5,2) NOT NULL,
  `report_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table url_prediction.reported_urls: ~6 rows (approximately)
INSERT INTO `reported_urls` (`id`, `url`, `prediction_percentage`, `report_date`) VALUES
	(1, 'http://example.com', 98.45, '2024-08-08 13:39:47'),
	(2, 'http://example.com', 98.45, '2024-08-08 13:39:51'),
	(3, 'http://example.com', 98.45, '2024-08-08 13:39:54'),
	(4, 'http://example.com', 98.45, '2024-08-08 13:40:00'),
	(5, 'http://example.com', 98.45, '2024-08-08 13:47:41'),
	(6, 'h', 71.64, '2024-08-08 15:03:39');

-- Dumping structure for table url_prediction.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table url_prediction.users: ~6 rows (approximately)
INSERT INTO `users` (`id`, `username`, `password`, `email`, `phone`) VALUES
	(1, 'sjsj', 'pbkdf2:sha256:600000$syArFMbN8ktYYO1V$ca3b0e4e3f26b3a93d17eea7fd362b090afdda18d964aa72ed689d3bf377e91c', 'aashutosh.vaish2023@ssipmt.com', '7712772989'),
	(2, 'jvbdj', 'pbkdf2:sha256:600000$TNREbgUfzhMhid84$0d05a3018a3976e2e96221ff4bb66efff641c182b47034c2a056fc80a112b2dc', 'aashutosh.vaish2023@ssipmt.com', '7712772989'),
	(3, 'sjcbsdcij', 'pbkdf2:sha256:600000$3tAAiA4CCFNrjiRE$7c1134bbe64c0abc7571435b5a1a872cb44263d68fb79b4b0acef3e17e2ac3d2', 'aashutosh.vaish2023@ssipmt.com', '7712772989'),
	(4, 'jvbcjdv', 'pbkdf2:sha256:600000$MgQth7GlXHlKgVly$6636e6e1d8ca2b7a4c92cf0325f7af74e002ba8ce982a68b7adc557e6be74eb2', 'aparajita@ssipmt.com', '987654324'),
	(5, 'apii', 'pbkdf2:sha256:600000$YPJfwB1p7USZxAJp$b182f816b26957dc9aba1a056e1252bfde8638e53f50337e9baef85f6c9d6467', 'aparajita@ssipmt.com', '9876543213'),
	(6, '160138', 'pbkdf2:sha256:600000$vwh6BpPW1bvOGrw5$225af984d65ba7f396fd1b8dfc0ba499348dcdd95038c04898b0839552e6e06c', 'aparajita@ssipmt.com', 'vv');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
