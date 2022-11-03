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


DROP TABLE IF EXISTS `LearningJourney`;

CREATE TABLE IF NOT EXISTS `LearningJourney` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Completion_Status` VARCHAR(100) NULL,
  `Roles_id` INT,
  `Staff_ID` INT,
  PRIMARY KEY (`id`),
  INDEX `fk_Learning_Journey_Roles1_idx` (`Roles_id` ASC),
  INDEX `fk_Learning_Journey_Staff1_idx` (`Staff_ID` ASC),
  CONSTRAINT `fk_Learning_Journey_Roles1`
    FOREIGN KEY (`Roles_id`)
    REFERENCES `spmproj`.`role` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Learning_Journey_Staff1`
    FOREIGN KEY (`Staff_ID`)
    REFERENCES `spmproj`.`Staff` (`Staff_ID`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;

INSERT INTO `LearningJourney` ( `Completion_Status`,`Roles_id`,`Staff_ID`) VALUES
('In progress', 1, 130001),
('In progress', 2, 140001),
('In progress', 3, 130002),
('In progress', 3, 130001);


