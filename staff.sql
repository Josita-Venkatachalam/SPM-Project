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
-- STAFF

DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
  `Staff_ID` INT NOT NULL,
  `Staff_FName` VARCHAR(50) NOT NULL,
  `Staff_LName` VARCHAR(50) NOT NULL,
  `Dept` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(50) NOT NULL,
  
--  `Username` VARCHAR(45) NOT NULL,
--  `Password` VARCHAR(45) NOT NULL,
--  `Position_ID` INT,
  PRIMARY KEY (`Staff_ID`))
--  INDEX `fk_Staff_Position_idx` (`Position_ID` ASC) VISIBLE,
--  CONSTRAINT `fk_Staff_Position`
--    FOREIGN KEY (`Position_ID`)
--    REFERENCES `spmproj`.`Staff_Group` (`Staff_Group_ID`)
--    ON DELETE SET NULL
--    ON UPDATE SET NULL)
ENGINE = InnoDB;

INSERT INTO `staff` (`Staff_ID`,`Staff_FName`,`Staff_LName`,`Dept`,`Email`) VALUES
(130001	,'John','Sim','Chariman','jack.sim@allinone.com.sg'),
(130002,'Jack','Sim','CEO','jack.sim@allinone.com.sg'),
(140001,'Derek','Tan','Sales','Derek.Tan@allinone.com.sg'),
(140002, 'Susan', 'Goh', 'Sales', 'Susan.Goh@allinone.com.sg');
