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
-- Table structure for table 'courses_skill'
--

DROP TABLE IF EXISTS `courses_skills`;

CREATE TABLE IF NOT EXISTS `courses_skills` (
  `Course_id` varchar(50) ,
  `Skill_id` INT,
  `ID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`),
  INDEX `fk_Courses_has_Skills_Skills1_idx` (`Skill_id` ASC) ,
  INDEX `fk_Courses_has_Skills_Courses1_idx` (`Course_id` ASC) ,
  CONSTRAINT `fk_Courses_has_Skills_Courses1`
    FOREIGN KEY (`Course_id`)
    REFERENCES `spmproj`.`courses` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Courses_has_Skills_Skills1`
    FOREIGN KEY (`Skill_id`)
    REFERENCES `spmproj`.`skill` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;

INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR001", 1);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR001", 3);
