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
DROP DATABASE IF EXISTS `spmProj`;

CREATE DATABASE IF NOT EXISTS `spmProj` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spmProj`;

-- --------------------------------------------------------

--
-- Table structure for table 'skill'
--

CREATE TABLE IF NOT EXISTS `skill` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(50) DEFAULT NULL UNIQUE,
  `description`  varchar(100)  DEFAULT NULL
  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'skill'
--

INSERT INTO `skill` (`name`, `description`) VALUES
('Communication', 'Learn to ommunicate Well in a team.' ),
('Leadership', 'Learn to lead the team well'),
('Project Management', 'Learn to manage projects well');


-- 
-- Table structure for table 'role'
--

CREATE TABLE IF NOT EXISTS `roles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `description` VARCHAR(200) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `roles` (`name`,`description`) VALUES
('Project Manager', 'A project manager is accountable for planning and allocating resources, and keeping stakeholders informed throughout the project lifecycle'),
('Engineering', 'Solve hardware issues' )
;

-- 
-- Table structure for table 'Role_Skills'
--

CREATE TABLE IF NOT EXISTS `Roles_Skills` (
  `Roles_id` INT ,
  `Skills_id` INT ,
  PRIMARY KEY (`Roles_id`, `Skills_id`),
  INDEX `fk_Roles_has_Skills_Skills1_idx` (`Skills_id` ASC),
  INDEX `fk_Roles_has_Skills_Roles1_idx` (`Roles_id` ASC),
  CONSTRAINT `fk_Roles_has_Skills_Roles1`
    FOREIGN KEY (`Roles_id`)
    REFERENCES `roles` (`id`)
    ON DELETE cascade
    ON UPDATE cascade,
  CONSTRAINT `fk_Roles_has_Skills_Skills1`
    FOREIGN KEY (`Skills_id`)
    REFERENCES `skill` (`id`)
    ON DELETE cascade
    ON UPDATE cascade)
ENGINE = InnoDB;

INSERT INTO `Roles_Skills` (`Roles_id`,`Skills_id`) VALUES (1, 1);
INSERT INTO `Roles_Skills` (`Roles_id`,`Skills_id`) VALUES (2, 2);
