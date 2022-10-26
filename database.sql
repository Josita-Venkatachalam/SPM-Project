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
  `description`  varchar(100)  DEFAULT NULL
  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `skill` (`name`, `description`) VALUES
('Communication', 'Learn to communicate Well in a team.' ),
('Leadership', 'Learn to lead the team well'),
('Project Management', 'Learn to manage projects well');

-- ROLES
DROP TABLE IF EXISTS `role`;
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

-- STAFF

DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
  `Staff_ID` INT NOT NULL,
  `Staff_FName` VARCHAR(50) NOT NULL,
  `Staff_LName` VARCHAR(50) NOT NULL,
  `Dept` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(50) NOT NULL,
  `Roles_id` INT, 
--  `Username` VARCHAR(45) NOT NULL,
--  `Password` VARCHAR(45) NOT NULL,
--  `Position_ID` INT,
  PRIMARY KEY (`Staff_ID`),
  UNIQUE INDEX `id_UNIQUE` (`Staff_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Roles_Saff_1`
    FOREIGN KEY (`Roles_id`)
    REFERENCES `spmproj`.`role` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)

--  INDEX `fk_Staff_Position_idx` (`Position_ID` ASC) VISIBLE,
--  CONSTRAINT `fk_Staff_Position`
--    FOREIGN KEY (`Position_ID`)
--    REFERENCES `spmproj`.`Staff_Group` (`Staff_Group_ID`)
--    ON DELETE SET NULL
--    ON UPDATE SET NULL)
ENGINE = InnoDB;

INSERT INTO `staff` (`Staff_ID`,`Staff_FName`,`Staff_LName`,`Dept`,`Email`,`Roles_id`) VALUES
(130001	,'John','Sim','Chariman','jack.sim@allinone.com.sg',1),
(130002,'Jack','Sim','CEO','jack.sim@allinone.com.sg',1),
(140001,'Derek','Tan','Sales','Derek.Tan@allinone.com.sg',3),
(140002, 'Susan', 'Goh', 'Sales', 'Susan.Goh@allinone.com.sg', 2);

-- COURSES
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




-- ROLE-SKILLS

DROP TABLE IF EXISTS `roles_skills`;
CREATE TABLE IF NOT EXISTS `roles_skills` (
  `Roles_id` INT ,
  `Skills_id` INT,
  `ID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`),
  INDEX `fk_Roles_has_Skills_Skills1_idx` (`Skills_id` ASC) VISIBLE,
  INDEX `fk_Roles_has_Skills_Roles1_idx` (`Roles_id` ASC) VISIBLE,
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

INSERT INTO `roles_skills` (`Roles_id`,`Skills_id`) VALUES (1, 1);
INSERT INTO `roles_skills` (`Roles_id`,`Skills_id`) VALUES (2, 2);

-- LEARNING JOURNEY

DROP TABLE IF EXISTS `LearningJourney`;

CREATE TABLE IF NOT EXISTS `LearningJourney` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Completion_Status` VARCHAR(45) NULL,
  `Roles_id` INT,
  `Staff_ID` INT,
  PRIMARY KEY (`id`),
  INDEX `fk_Learning Journey_Roles1_idx` (`Roles_id` ASC) VISIBLE,
  INDEX `fk_Learning Journey_Staff1_idx` (`Staff_ID` ASC) VISIBLE,
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

INSERT INTO `LearningJourney` ( `Completion_Status`,`Roles_id`,`Staff_ID`) VALUES
('In progress', 1, 130001),
('In progress', 2, 140001),
('In progress', 3, 130002);


-- COURSE-SKILL
DROP TABLE IF EXISTS `courses_skills`;

CREATE TABLE IF NOT EXISTS `courses_skills` (
  `Course_id` varchar(50) ,
  `Skill_id` INT,
  `ID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`),
  INDEX `fk_Courses_has_Skills_Skills1_idx` (`Skill_id` ASC) VISIBLE,
  INDEX `fk_Courses_has_Skills_Courses1_idx` (`Course_id` ASC) VISIBLE,
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
