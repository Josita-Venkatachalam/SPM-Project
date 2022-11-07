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
-- Table structure for table 'Learning_Journey_Course'
--


DROP TABLE IF EXISTS `learning_journey_courses`;

CREATE TABLE IF NOT EXISTS `learning_journey_courses` (
  `Course_id` varchar(50) ,
  `Skill_id` INT,
  `Learning_Journey_Id` INT,
  `ID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`),
  INDEX `fk_LJ_has_Courses_Courses1_idx` (`Learning_Journey_Id` ASC),
  INDEX `fk_Courses_is_in_LJ1_idx` (`Course_id` ASC),
  CONSTRAINT `fk_LJ_has_Courses_Courses1`
    FOREIGN KEY (`Learning_Journey_Id`)
    REFERENCES `spmproj`.`LearningJourney` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Courses_is_in_LJ1`
    FOREIGN KEY (`Course_id`)
    REFERENCES `spmproj`.`courses` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;

INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR001", 1);

DROP TABLE IF EXISTS `learning_journey_courses`;

CREATE TABLE IF NOT EXISTS `learning_journey_courses` (
  `Course_id` varchar(50) ,
  `Skill_id` INT,
  `Learning_Journey_Id` INT,
  `ID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;

INSERT INTO `learning_journey_courses` (`Course_id`,`Skill_id`,`Learning_Journey_Id`) VALUES ("COR001", 1,1);
INSERT INTO `learning_journey_courses` (`Course_id`,`Skill_id`,`Learning_Journey_Id`) VALUES ("COR001", 3,1);
