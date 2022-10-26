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
-- Table structure for table 'courses'
--
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `id` varchar(50) NOT NULL PRIMARY KEY,
  `name` varchar(50) DEFAULT NULL UNIQUE,
  `description`  varchar(100)  DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `type`  varchar(50) DEFAULT NULL,
  `category`varchar(50) DEFAULT NULL

  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'skill'
--

-- INSERT INTO `skill` (`name`, `description`) VALUES
-- ('Communication', 'Learn to communicate Well in a team.' ),
-- ('Leadership', 'Learn to lead the team well'),
-- ('Project Management', 'Learn to manage projects well');

LOAD DATA LOCAL INFILE "/Course/courses_from_LMS.csv" INTO TABLE courses
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(Course_ID, Course_Name, Course_Desc, Course_Status, Course_Type, Course_Category)