-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 27, 2021 at 08:33 AM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: 'is212_example'
--
CREATE DATABASE IF NOT EXISTS `spmProj` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spmProj`;

-- --------------------------------------------------------

--
-- Table structure for table 'skill'
--

CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(50) DEFAULT NULL UNIQUE,
  `description`  varchar(100)  DEFAULT NULL
  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'role'
--

INSERT INTO `role` (`name`, `description`) VALUES
('Project Manager', 'A Project Manager manages a team of people.' ),
('Data analyst', 'A Data Analyst reviews data to identify key insights.'),
('Data Scientist', 'A Data Scientist analyze data for actionable insights.');

