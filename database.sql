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
  `isDeleted` INT NOT NULL DEFAULT 0
  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `skill` (`name`, `description`) VALUES
('Communication', 'Learn to communicate well in a team.' ),
('Leadership', 'Learn to lead the team well'),
('Project Management', 'Learn to manage projects well'),
('Critical Thinking', 'Learn to think critically' ),
('Problem Solving', 'Learn methods to solve problems');

-- ROLES
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(50) DEFAULT NULL UNIQUE,
  `description`  varchar(100)  DEFAULT NULL,
  `isDeleted` INT NOT NULL DEFAULT 0
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

--  INDEX `fk_Staff_Position_idx` (`Position_ID` ASC) VISIBLE,
--  CONSTRAINT `fk_Staff_Position`
--    FOREIGN KEY (`Position_ID`)
--    REFERENCES `spmproj`.`Staff_Group` (`Staff_Group_ID`)
--    ON DELETE SET NULL
--    ON UPDATE SET NULL)
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
  `description`  varchar(100)  DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `type`  varchar(50) DEFAULT NULL,
  `category`varchar(50) DEFAULT NULL

  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `courses` (`id`, `name` , `description`, `status`, `type`,   `category`) VALUES
('COR001','Systems Thinking and Design','This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking','Active','Internal','Core'),
('COR002','Lean Six Sigma Green Belt Certification','Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics','Active','Internal','Core'),
('SAL001','Risk Management for Smart Business','Apply risk management concepts to digital business','Retired','Internal','Sales'),
('COR004','Service Excellence','The programme provides the learner with the key foundations of what builds customer confidence','Pending','Internal','Core'),
('COR006','Manage Change','Identify risks associated with change and develop risk mitigation plans','Retired','External','Core'),
('FIN003','Business Continuity Planning','Business continuity planning is essential in any business to minimise loss','Retired','External','Finance'),
('MGT001','People Management','Enable learners to manage team performance and development through effective communication','Active','Internal','Management');
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
INSERT INTO `roles_skills` (`Roles_id`,`Skills_id`) VALUES (3, 3);
INSERT INTO `roles_skills` (`Roles_id`,`Skills_id`) VALUES (1, 2);
INSERT INTO `roles_skills` (`Roles_id`,`Skills_id`) VALUES (1, 3);

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

INSERT INTO `LearningJourney` ( `Completion_Status`,`Roles_id`,`Staff_ID`) VALUES
('In progress', 2, 130001),
('In progress', 2, 140001),
('In progress', 1, 140001),
('In progress', 3, 130002),
('In progress', 3, 130001);


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

INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR001", 1);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR002", 2);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR001", 2);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR001", 3);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR002", 3);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR004", 1);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("COR006", 1);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("FIN003", 3);
INSERT INTO `courses_skills` (`Course_id`,`Skill_id`) VALUES ("MGT001", 3);

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
    ON UPDATE SET NULL)
ENGINE = InnoDB;


INSERT INTO `learning_journey_courses` (`Course_id`,`Skill_id`,`Learning_Journey_Id`) VALUES ("COR001", 1,1);
INSERT INTO `learning_journey_courses` (`Course_id`,`Skill_id`,`Learning_Journey_Id`) VALUES ("COR001", 3,1);