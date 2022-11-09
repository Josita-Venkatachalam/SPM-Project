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


DROP DATABASE IF EXISTS `spmProj`;

CREATE DATABASE IF NOT EXISTS `spmProj` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spmProj`;

-- STAFF_GROUP

DROP TABLE IF EXISTS `staff_group`;
CREATE TABLE `staff_group` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(50) DEFAULT NULL UNIQUE
  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `staff_group` (`name`) VALUES
('Admin'),
('User'),
('Manager'),
('Trainer');

-- SKILLS

DROP TABLE IF EXISTS `skill`;
CREATE TABLE `skill` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(50) DEFAULT NULL UNIQUE,
  `description`  varchar(100)  DEFAULT NULL,
  `isDeleted` INT DEFAULT 0
  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ROLES
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(50) DEFAULT NULL UNIQUE,
  `description`  varchar(100)  DEFAULT NULL,
  `isDeleted` INT DEFAULT 0
  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'role'
--


-- STAFF

DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
  `Staff_ID` INT NOT NULL,
  `Staff_FName` VARCHAR(50) NOT NULL,
  `Staff_LName` VARCHAR(50) NOT NULL,
  `Dept` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(50) NOT NULL,
  `Staff_group_id` INT, 
--  `Username` VARCHAR(45) NOT NULL,
--  `Password` VARCHAR(45) NOT NULL,
--  `Position_ID` INT,
  PRIMARY KEY (`Staff_ID`),
  UNIQUE INDEX `id_UNIQUE` (`Staff_ID` ASC),
  CONSTRAINT `fk_Staff_StaffGroup_1`
    FOREIGN KEY (`Staff_group_id`)
    REFERENCES `spmproj`.`staff_group` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)

ENGINE = InnoDB;

INSERT INTO `staff` (`Staff_ID`,`Staff_FName`,`Staff_LName`,`Dept`,`Email`,`Staff_group_id`) VALUES
(130001	,'John','Sim','Chariman','jack.sim@allinone.com.sg',1),
(130002,'Jack','Sim','CEO','jack.sim@allinone.com.sg',1),
(140001,'Derek','Tan','Sales','Derek.Tan@allinone.com.sg',3),
(140002, 'Susan', 'Goh', 'Sales', 'Susan.Goh@allinone.com.sg', 2);


-- COURSES
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `id` varchar(50) NOT NULL PRIMARY KEY,
  `name` varchar(50) DEFAULT NULL UNIQUE,
  `description`  varchar(300)  DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `type`  varchar(50) DEFAULT NULL,
  `category`varchar(50) DEFAULT NULL

  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ROLE-SKILLS

DROP TABLE IF EXISTS `roles_skills`;
CREATE TABLE IF NOT EXISTS `roles_skills` (
  `Roles_id` INT ,
  `Skills_id` INT,
  `ID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`),
  INDEX `fk_Roles_has_Skills_Skills1_idx` (`Skills_id` ASC),
  INDEX `fk_Roles_has_Skills_Roles1_idx` (`Roles_id` ASC),
  CONSTRAINT `fk_Roles_has_Skills_Roles1`
    FOREIGN KEY (`Roles_id`)
    REFERENCES `spmproj`.`role` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Roles_has_Skills_Skills1`
    FOREIGN KEY (`Skills_id`)
    REFERENCES `spmproj`.`skill` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;

-- LEARNING JOURNEY

DROP TABLE IF EXISTS `LearningJourney`;

CREATE TABLE IF NOT EXISTS `LearningJourney` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Completion_Status` VARCHAR(45) NULL,
  `Roles_id` INT,
  `Staff_ID` INT,
  PRIMARY KEY (`id`),
  INDEX `fk_Learning Journey_Roles1_idx` (`Roles_id` ASC),
  INDEX `fk_Learning Journey_Staff1_idx` (`Staff_ID` ASC),
  CONSTRAINT `fk_Learning Journey_Roles1`
    FOREIGN KEY (`Roles_id`)
    REFERENCES `spmproj`.`role` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Learning Journey_Staff1`
    FOREIGN KEY (`Staff_ID`)
    REFERENCES `spmproj`.`Staff` (`Staff_ID`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


-- COURSE-SKILL
DROP TABLE IF EXISTS `courses_skills`;

CREATE TABLE IF NOT EXISTS `courses_skills` (
  `Course_id` varchar(50) ,
  `Skill_id` INT,
  `ID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`),
  INDEX `fk_Courses_has_Skills_Skills1_idx` (`Skill_id` ASC),
  INDEX `fk_Courses_has_Skills_Courses1_idx` (`Course_id` ASC),
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

-- LEARNING JOURNEY - COURSE

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
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Skills_is_in_LJ1`
    FOREIGN KEY (`Skill_id`)
    REFERENCES `spmproj`.`skill` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
CREATE TABLE IF NOT EXISTS `registration`(
  `Reg_ID` int(3) DEFAULT NULL,
  `Course_ID` varchar(6) DEFAULT NULL,
  `Staff_ID` int(6) DEFAULT NULL,
  `Reg_Status` varchar(10) DEFAULT NULL,
  `Completion_Status` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


