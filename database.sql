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
  `isDeleted` INT DEFAULT 0
  --  FOREIGN KEY (id) REFERENCES Roles(skillId)
  --  FOREIGN KEY (id) REFERENCES Courses(skillId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'role'
--

INSERT INTO `role` (`name`, `description`) VALUES
('Project Manager', 'A Project Manager manages a team of people.' ),
('Data Analyst', 'A Data Analyst reviews data to identify key insights.'),
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
  `description`  varchar(300)  DEFAULT NULL,
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
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Skills_is_in_LJ1`
    FOREIGN KEY (`Skill_id`)
    REFERENCES `spmproj`.`skill` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


INSERT INTO `learning_journey_courses` (`Course_id`,`Skill_id`,`Learning_Journey_Id`) VALUES ("COR001", 1,1);
INSERT INTO `learning_journey_courses` (`Course_id`,`Skill_id`,`Learning_Journey_Id`) VALUES ("COR001", 3,1);

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

--
-- Dumping data for table `table 9`
--

INSERT INTO `registration` (`Reg_ID`, `Course_ID`, `Staff_ID`, `Reg_Status`, `Completion_Status`) VALUES
(1, 'COR002', 130001, 'Registered', 'Completed'),
(245, 'COR001', 130001, 'Registered', 'Completed'),
(2, 'COR002', 130002, 'Registered', 'Completed'),
(3, 'COR002', 140001, 'Registered', 'Completed'),
(111, 'SAL004', 140001, 'Registered', 'Completed'),
(200, 'MGT001', 140001, 'Registered', 'Completed'),
(246, 'COR006', 140001, 'Waitlist', ''),
(4, 'COR002', 140002, 'Registered', 'Completed'),
(112, 'SAL004', 140002, 'Registered', 'Completed'),
(247, 'FIN001', 140002, 'Waitlist', ''),
(5, 'COR002', 140003, 'Rejected', ''),
(113, 'SAL003', 140003, 'Registered', 'Completed'),
(248, 'FIN002', 140003, 'Registered', 'Completed'),
(114, 'SAL003', 140004, 'Registered', 'OnGoing'),
(203, 'COR002', 140004, 'Registered', 'Completed'),
(249, 'FIN003', 140004, 'Registered', 'OnGoing'),
(6, 'COR002', 140008, 'Registered', 'OnGoing'),
(115, 'SAL004', 140008, 'Rejected', ''),
(250, 'HRD001', 140008, 'Registered', 'OnGoing'),
(204, 'COR002', 140015, 'Waitlist', ''),
(251, 'MGT001', 140015, 'Registered', ''),
(7, 'COR002', 140025, 'Registered', 'OnGoing'),
(116, 'SAL003', 140025, 'Registered', 'OnGoing'),
(252, 'MGT002', 140025, 'Rejected', ''),
(8, 'COR002', 140036, 'Waitlist', ''),
(253, 'MGT004', 140036, 'Registered', ''),
(9, 'COR002', 140078, 'Waitlist', ''),
(117, 'SAL004', 140078, 'Registered', ''),
(254, 'MGT007', 140078, 'Registered', 'Completed'),
(10, 'COR002', 140102, 'Registered', ''),
(118, 'SAL004', 140102, 'Waitlist', ''),
(255, 'SAL001', 140102, 'Waitlist', ''),
(11, 'COR002', 140103, 'Registered', ''),
(119, 'SAL003', 140103, 'Waitlist', ''),
(12, 'COR002', 140108, 'Registered', ''),
(120, 'SAL003', 140108, 'Registered', 'Completed'),
(256, 'SAL004', 140108, 'Registered', 'Completed'),
(13, 'COR002', 140115, 'Registered', 'Completed'),
(121, 'SAL004', 140115, 'Registered', 'Completed'),
(257, 'tch001', 140115, 'Registered', 'Completed'),
(14, 'COR002', 140525, 'Rejected', ''),
(122, 'SAL004', 140525, 'Registered', 'Completed'),
(258, 'tch002', 140525, 'Registered', 'Completed'),
(123, 'SAL003', 140736, 'Registered', 'OnGoing'),
(205, 'COR002', 140736, 'Waitlist', ''),
(259, 'tch003', 140736, 'Registered', 'OnGoing'),
(15, 'COR002', 140878, 'Registered', 'Completed'),
(124, 'SAL003', 140878, 'Rejected', ''),
(260, 'tch005', 140878, 'Rejected', ''),
(201, 'MGT001', 150008, 'Registered', 'Completed'),
(206, 'COR002', 150008, 'Registered', 'Completed'),
(261, 'tch008', 150008, 'Registered', 'OnGoing'),
(17, 'COR002', 150065, 'Waitlist', ''),
(126, 'tch003', 150065, 'Waitlist', ''),
(263, 'tch013', 150065, 'Waitlist', ''),
(16, 'COR002', 150075, 'Registered', 'Completed'),
(125, 'tch002', 150075, 'Registered', ''),
(262, 'tch012', 150075, 'Registered', ''),
(18, 'COR002', 150076, 'Waitlist', ''),
(264, 'tch014', 150076, 'Waitlist', ''),
(26, 'COR002', 150085, 'Waitlist', ''),
(132, 'tch002', 150085, 'Waitlist', ''),
(273, 'HRD001', 150085, 'Registered', 'OnGoing'),
(25, 'COR002', 150095, 'Registered', ''),
(131, 'tch001', 150095, 'Waitlist', ''),
(272, 'FIN003', 150095, 'Waitlist', ''),
(27, 'COR002', 150096, 'Waitlist', ''),
(133, 'tch003', 150096, 'Registered', 'Completed'),
(274, 'MGT001', 150096, 'Registered', 'OnGoing'),
(35, 'COR002', 150115, 'Waitlist', ''),
(137, 'tch001', 150115, 'Registered', 'Completed'),
(284, 'tch005', 150115, 'Registered', 'Completed'),
(19, 'COR002', 150118, 'Registered', 'Completed'),
(127, 'tch005', 150118, 'Registered', 'Completed'),
(265, 'tch015', 150118, 'Registered', ''),
(34, 'COR002', 150125, 'Registered', 'OnGoing'),
(283, 'tch003', 150125, 'Registered', 'Completed'),
(36, 'COR002', 150126, 'Waitlist', ''),
(138, 'tch002', 150126, 'Registered', 'Completed'),
(285, 'tch008', 150126, 'Registered', 'OnGoing'),
(28, 'COR002', 150138, 'Registered', 'Completed'),
(275, 'MGT002', 150138, 'Registered', ''),
(20, 'COR002', 150142, 'Registered', 'OnGoing'),
(266, 'tch018', 150142, 'Registered', ''),
(21, 'COR002', 150143, 'Registered', 'OnGoing'),
(128, 'tch001', 150143, 'Registered', 'Completed'),
(267, 'tch019', 150143, 'Registered', 'Completed'),
(22, 'COR002', 150148, 'Registered', ''),
(129, 'tch002', 150148, 'Registered', 'OnGoing'),
(268, 'COR001', 150148, 'Registered', 'Completed'),
(23, 'COR002', 150155, 'Rejected', ''),
(130, 'tch003', 150155, 'Rejected', ''),
(29, 'COR002', 150162, 'Registered', 'Completed'),
(134, 'tch005', 150162, 'Registered', 'Completed'),
(276, 'MGT004', 150162, 'Registered', ''),
(30, 'COR002', 150163, 'Registered', 'Completed'),
(277, 'MGT007', 150163, 'Rejected', ''),
(212, 'COR002', 150165, 'Registered', 'OnGoing'),
(43, 'COR002', 150166, 'Registered', 'Completed'),
(143, 'tch005', 150166, 'Registered', 'Completed'),
(189, 'FIN001', 150166, 'Waitlist', ''),
(202, 'MGT001', 150166, 'Registered', 'Completed'),
(237, 'tch003', 150166, 'Rejected', ''),
(293, 'COR006', 150166, 'Registered', 'OnGoing'),
(31, 'COR002', 150168, 'Registered', 'Completed'),
(135, 'tch001', 150168, 'Rejected', ''),
(278, 'SAL001', 150168, 'Registered', ''),
(32, 'COR002', 150175, 'Rejected', ''),
(279, 'SAL003', 150175, 'Registered', 'Completed'),
(37, 'COR002', 150192, 'Registered', ''),
(139, 'tch003', 150192, 'Registered', 'Completed'),
(286, 'tch012', 150192, 'Rejected', ''),
(38, 'COR002', 150193, 'Registered', ''),
(287, 'tch013', 150193, 'Registered', 'OnGoing'),
(39, 'COR002', 150198, 'Registered', ''),
(140, 'tch005', 150198, 'Rejected', ''),
(288, 'tch014', 150198, 'Registered', ''),
(40, 'COR002', 150205, 'Registered', 'Completed'),
(289, 'tch015', 150205, 'Waitlist', ''),
(44, 'COR002', 150208, 'Waitlist', ''),
(190, 'FIN002', 150208, 'Registered', 'Completed'),
(238, 'tch005', 150208, 'Waitlist', ''),
(294, 'FIN001', 150208, 'Rejected', ''),
(371, 'MGT002', 150208, 'Registered', 'Completed'),
(51, 'COR002', 150215, 'Registered', ''),
(148, 'tch002', 150215, 'Waitlist', ''),
(198, 'FIN002', 150215, 'Registered', 'Completed'),
(243, 'tch001', 150215, 'Registered', 'Completed'),
(302, 'SAL001', 150215, 'Registered', 'OnGoing'),
(379, 'tch003', 150215, 'Waitlist', ''),
(110, 'COR002', 150216, 'Waitlist', ''),
(149, 'tch003', 150216, 'Registered', 'Completed'),
(199, 'FIN001', 150216, 'Registered', 'OnGoing'),
(244, 'tch005', 150216, 'Registered', 'OnGoing'),
(303, 'SAL003', 150216, 'Rejected', ''),
(45, 'COR002', 150232, 'Waitlist', ''),
(144, 'tch001', 150232, 'Registered', 'Completed'),
(191, 'FIN001', 150232, 'Registered', 'Completed'),
(295, 'FIN002', 150232, 'Registered', 'OnGoing'),
(372, 'MGT004', 150232, 'Registered', 'Completed'),
(46, 'COR002', 150233, 'Registered', 'Completed'),
(145, 'tch002', 150233, 'Registered', 'OnGoing'),
(192, 'FIN002', 150233, 'Registered', 'Completed'),
(296, 'FIN003', 150233, 'Registered', ''),
(373, 'MGT007', 150233, 'Registered', 'Completed'),
(47, 'COR002', 150238, 'Registered', 'OnGoing'),
(146, 'tch003', 150238, 'Rejected', ''),
(193, 'FIN001', 150238, 'Registered', 'OnGoing'),
(297, 'HRD001', 150238, 'Waitlist', ''),
(374, 'SAL001', 150238, 'Registered', 'OnGoing'),
(48, 'COR002', 150245, 'Registered', 'OnGoing'),
(194, 'FIN002', 150245, 'Rejected', ''),
(239, 'tch001', 150245, 'Rejected', ''),
(298, 'MGT001', 150245, 'Waitlist', ''),
(375, 'SAL003', 150245, 'Rejected', ''),
(52, 'COR002', 150258, 'Registered', ''),
(304, 'SAL004', 150258, 'Registered', ''),
(60, 'COR002', 150265, 'Registered', 'OnGoing'),
(153, 'tch001', 150265, 'Registered', 'Completed'),
(313, 'tch015', 150265, 'Registered', 'Completed'),
(213, 'COR002', 150275, 'Waitlist', ''),
(312, 'tch014', 150275, 'Registered', 'Completed'),
(154, 'tch002', 150276, 'Registered', 'Completed'),
(214, 'COR002', 150276, 'Registered', 'Completed'),
(314, 'tch018', 150276, 'Rejected', ''),
(53, 'COR002', 150282, 'Waitlist', ''),
(150, 'tch005', 150282, 'Registered', 'Completed'),
(305, 'tch001', 150282, 'Waitlist', ''),
(54, 'COR002', 150283, 'Waitlist', ''),
(306, 'tch002', 150283, 'Registered', 'Completed'),
(55, 'COR002', 150288, 'Registered', 'Completed'),
(151, 'tch001', 150288, 'Rejected', ''),
(307, 'tch003', 150288, 'Registered', 'Completed'),
(56, 'COR002', 150295, 'Registered', 'Completed'),
(308, 'tch005', 150295, 'Registered', 'OnGoing'),
(61, 'COR002', 150318, 'Registered', 'OnGoing'),
(155, 'tch003', 150318, 'Registered', 'Completed'),
(315, 'tch019', 150318, 'Waitlist', ''),
(62, 'COR002', 150342, 'Waitlist', ''),
(316, 'COR001', 150342, 'Registered', 'Completed'),
(63, 'COR002', 150343, 'Waitlist', ''),
(156, 'tch005', 150343, 'Rejected', ''),
(159, 'tch005', 150345, 'Registered', 'Completed'),
(215, 'COR002', 150345, 'Registered', ''),
(322, 'MGT001', 150345, 'Registered', 'Completed'),
(64, 'COR002', 150348, 'Registered', ''),
(317, 'COR006', 150348, 'Registered', 'Completed'),
(65, 'COR002', 150355, 'Registered', ''),
(318, 'FIN001', 150355, 'Rejected', ''),
(69, 'COR002', 150356, 'Registered', 'Completed'),
(323, 'MGT002', 150356, 'Registered', 'OnGoing'),
(160, 'tch001', 150398, 'Registered', 'Completed'),
(216, 'COR002', 150398, 'Registered', 'Completed'),
(324, 'MGT004', 150398, 'Registered', 'Completed'),
(70, 'COR002', 150422, 'Registered', 'Completed'),
(161, 'tch002', 150422, 'Registered', 'OnGoing'),
(325, 'MGT007', 150422, 'Registered', 'Completed'),
(71, 'COR002', 150423, 'Waitlist', ''),
(162, 'tch003', 150423, 'Rejected', ''),
(326, 'SAL001', 150423, 'Waitlist', ''),
(72, 'COR002', 150428, 'Waitlist', ''),
(327, 'SAL003', 150428, 'Waitlist', ''),
(73, 'COR002', 150435, 'Registered', 'Completed'),
(328, 'SAL004', 150435, 'Registered', 'Completed'),
(77, 'COR002', 150445, 'Rejected', ''),
(165, 'tch003', 150445, 'Registered', 'Completed'),
(332, 'tch005', 150445, 'Rejected', ''),
(217, 'COR002', 150446, 'Registered', ''),
(333, 'tch008', 150446, 'Registered', ''),
(78, 'COR002', 150488, 'Registered', ''),
(166, 'tch005', 150488, 'Registered', 'Completed'),
(334, 'tch012', 150488, 'Registered', 'Completed'),
(218, 'COR002', 150512, 'Registered', ''),
(335, 'tch013', 150512, 'Waitlist', ''),
(79, 'COR002', 150513, 'Registered', 'Completed'),
(167, 'tch001', 150513, 'Rejected', ''),
(336, 'tch014', 150513, 'Waitlist', ''),
(80, 'COR002', 150518, 'Waitlist', ''),
(337, 'tch015', 150518, 'Registered', 'Completed'),
(81, 'COR002', 150525, 'Waitlist', ''),
(338, 'tch018', 150525, 'Registered', 'Completed'),
(85, 'COR002', 150555, 'Registered', 'OnGoing'),
(169, 'tch001', 150555, 'Registered', 'Completed'),
(341, 'COR006', 150555, 'Registered', 'OnGoing'),
(207, 'COR002', 150565, 'Registered', ''),
(269, 'COR006', 150565, 'Registered', 'Completed'),
(86, 'COR002', 150566, 'Rejected', ''),
(170, 'tch002', 150566, 'Registered', 'Completed'),
(342, 'FIN001', 150566, 'Registered', ''),
(209, 'COR002', 150585, 'Registered', 'OnGoing'),
(280, 'SAL004', 150585, 'Waitlist', ''),
(171, 'tch003', 150608, 'Registered', 'Completed'),
(219, 'COR002', 150608, 'Registered', 'OnGoing'),
(343, 'FIN002', 150608, 'Waitlist', ''),
(41, 'COR002', 150615, 'Rejected', ''),
(290, 'tch018', 150615, 'Waitlist', ''),
(87, 'COR002', 150632, 'Registered', 'OnGoing'),
(344, 'FIN003', 150632, 'Waitlist', ''),
(172, 'tch005', 150633, 'Rejected', ''),
(220, 'COR002', 150633, 'Waitlist', ''),
(345, 'HRD001', 150633, 'Registered', ''),
(88, 'COR002', 150638, 'Registered', ''),
(346, 'MGT001', 150638, 'Registered', ''),
(89, 'COR002', 150645, 'Waitlist', ''),
(347, 'MGT002', 150645, 'Registered', 'Completed'),
(49, 'COR002', 150655, 'Registered', ''),
(195, 'FIN001', 150655, 'Waitlist', ''),
(240, 'tch002', 150655, 'Registered', ''),
(299, 'MGT002', 150655, 'Registered', 'Completed'),
(376, 'SAL004', 150655, 'Registered', 'OnGoing'),
(93, 'COR002', 150695, 'Registered', 'Completed'),
(175, 'tch005', 150695, 'Registered', 'Completed'),
(351, 'SAL003', 150695, 'Registered', 'Completed'),
(57, 'COR002', 150705, 'Registered', 'Completed'),
(309, 'tch008', 150705, 'Rejected', ''),
(66, 'COR002', 150765, 'Registered', ''),
(157, 'tch002', 150765, 'Registered', ''),
(319, 'FIN002', 150765, 'Registered', ''),
(24, 'COR002', 150776, 'Registered', ''),
(270, 'FIN001', 150776, 'Registered', 'Completed'),
(33, 'COR002', 150796, 'Registered', 'OnGoing'),
(281, 'tch001', 150796, 'Waitlist', ''),
(141, 'tch002', 150826, 'Registered', ''),
(211, 'COR002', 150826, 'Rejected', ''),
(291, 'tch019', 150826, 'Registered', 'Completed'),
(74, 'COR002', 150845, 'Registered', 'OnGoing'),
(329, 'tch001', 150845, 'Registered', 'OnGoing'),
(50, 'COR002', 150866, 'Rejected', ''),
(196, 'FIN002', 150866, 'Registered', 'Completed'),
(241, 'tch003', 150866, 'Waitlist', ''),
(300, 'MGT004', 150866, 'Registered', 'Completed'),
(377, 'tch001', 150866, 'Registered', ''),
(58, 'COR002', 150916, 'Registered', 'Completed'),
(310, 'tch012', 150916, 'Waitlist', ''),
(208, 'COR002', 150918, 'Registered', ''),
(271, 'FIN002', 150918, 'Waitlist', ''),
(82, 'COR002', 150935, 'Registered', 'Completed'),
(339, 'tch019', 150935, 'Registered', 'Completed'),
(136, 'tch005', 150938, 'Waitlist', ''),
(210, 'COR002', 150938, 'Rejected', ''),
(282, 'tch002', 150938, 'Registered', 'Completed'),
(42, 'COR002', 150968, 'Registered', 'Completed'),
(142, 'tch003', 150968, 'Waitlist', ''),
(292, 'COR001', 150968, 'Registered', 'Completed'),
(67, 'COR002', 150976, 'Registered', 'Completed'),
(158, 'tch003', 150976, 'Waitlist', ''),
(320, 'FIN003', 150976, 'Waitlist', ''),
(109, 'COR002', 151008, 'Registered', ''),
(147, 'tch001', 151008, 'Waitlist', ''),
(197, 'FIN001', 151008, 'Registered', 'Completed'),
(242, 'tch005', 151008, 'Registered', 'Completed'),
(301, 'MGT007', 151008, 'Registered', 'Completed'),
(378, 'tch002', 151008, 'Waitlist', ''),
(90, 'COR002', 151055, 'Waitlist', ''),
(173, 'tch002', 151055, 'Registered', ''),
(348, 'MGT004', 151055, 'Registered', 'Completed'),
(75, 'COR002', 151056, 'Registered', 'OnGoing'),
(163, 'tch001', 151056, 'Waitlist', ''),
(330, 'tch002', 151056, 'Registered', 'OnGoing'),
(59, 'COR002', 151058, 'Rejected', ''),
(152, 'tch005', 151058, 'Waitlist', ''),
(311, 'tch013', 151058, 'Waitlist', ''),
(68, 'COR002', 151118, 'Rejected', ''),
(321, 'HRD001', 151118, 'Registered', 'Completed'),
(83, 'COR002', 151146, 'Registered', 'Completed'),
(168, 'tch005', 151146, 'Waitlist', ''),
(340, 'COR001', 151146, 'Registered', 'OnGoing'),
(76, 'COR002', 151198, 'Registered', ''),
(164, 'tch002', 151198, 'Waitlist', ''),
(331, 'tch003', 151198, 'Registered', ''),
(91, 'COR002', 151266, 'Registered', ''),
(174, 'tch003', 151266, 'Waitlist', ''),
(349, 'MGT007', 151266, 'Rejected', ''),
(84, 'COR002', 151288, 'Registered', 'Completed'),
(92, 'COR002', 151408, 'Registered', ''),
(350, 'SAL001', 151408, 'Registered', 'Completed'),
(94, 'COR002', 160008, 'Registered', 'Completed'),
(176, 'HRD001', 160008, 'Registered', 'Completed'),
(352, 'SAL004', 160008, 'Waitlist', ''),
(178, 'MGT002', 160065, 'Registered', 'Completed'),
(221, 'COR002', 160065, 'Waitlist', ''),
(354, 'tch002', 160065, 'Registered', 'OnGoing'),
(95, 'COR002', 160075, 'Rejected', ''),
(177, 'MGT001', 160075, 'Registered', 'Completed'),
(353, 'tch001', 160075, 'Waitlist', ''),
(96, 'COR002', 160076, 'Registered', 'Completed'),
(355, 'tch003', 160076, 'Registered', 'OnGoing'),
(179, 'MGT004', 160118, 'Rejected', ''),
(222, 'SAL004', 160118, 'Registered', 'Completed'),
(356, 'tch005', 160118, 'Registered', ''),
(102, 'COR002', 160135, 'Registered', ''),
(182, 'MGT004', 160135, 'Registered', 'Completed'),
(228, 'SAL004', 160135, 'Waitlist', ''),
(362, 'tch018', 160135, 'Waitlist', ''),
(97, 'COR002', 160142, 'Registered', 'Completed'),
(223, 'SAL004', 160142, 'Registered', 'Completed'),
(357, 'tch008', 160142, 'Registered', ''),
(98, 'COR002', 160143, 'Waitlist', ''),
(224, 'SAL003', 160143, 'Registered', 'Completed'),
(358, 'tch012', 160143, 'Rejected', ''),
(101, 'COR002', 160145, 'Registered', 'OnGoing'),
(227, 'SAL003', 160145, 'Registered', ''),
(361, 'tch015', 160145, 'Waitlist', ''),
(103, 'COR002', 160146, 'Registered', ''),
(183, 'MGT007', 160146, 'Registered', 'Completed'),
(229, 'SAL004', 160146, 'Registered', 'Completed'),
(363, 'tch019', 160146, 'Registered', 'Completed'),
(99, 'COR002', 160148, 'Waitlist', ''),
(180, 'MGT001', 160148, 'Registered', ''),
(225, 'SAL003', 160148, 'Registered', 'OnGoing'),
(359, 'tch013', 160148, 'Registered', ''),
(100, 'COR002', 160155, 'Registered', 'OnGoing'),
(181, 'MGT002', 160155, 'Waitlist', ''),
(226, 'SAL004', 160155, 'Rejected', ''),
(360, 'tch014', 160155, 'Registered', 'Completed'),
(104, 'COR002', 160188, 'Rejected', ''),
(184, 'HRD001', 160188, 'Registered', 'Completed'),
(230, 'SAL003', 160188, 'Registered', 'Completed'),
(364, 'COR001', 160188, 'Registered', 'Completed'),
(185, 'MGT001', 160212, 'Registered', 'OnGoing'),
(231, 'SAL003', 160212, 'Registered', 'OnGoing'),
(365, 'COR002', 160212, 'Registered', 'Completed'),
(105, 'COR002', 160213, 'Registered', ''),
(186, 'MGT002', 160213, 'Rejected', ''),
(232, 'SAL004', 160213, 'Rejected', ''),
(366, 'COR006', 160213, 'Registered', 'OnGoing'),
(233, 'SAL004', 160218, 'Waitlist', ''),
(367, 'FIN001', 160218, 'Rejected', ''),
(106, 'COR002', 160225, 'Registered', 'Completed'),
(234, 'SAL003', 160225, 'Waitlist', ''),
(368, 'FIN002', 160225, 'Registered', 'OnGoing'),
(107, 'COR002', 160258, 'Waitlist', ''),
(187, 'MGT007', 160258, 'Registered', ''),
(235, 'SAL003', 160258, 'Registered', 'Completed'),
(369, 'FIN003', 160258, 'Registered', ''),
(108, 'COR002', 160282, 'Waitlist', ''),
(188, 'MGT001', 160282, 'Waitlist', ''),
(236, 'tch002', 160282, 'Registered', 'Completed'),
(370, 'HRD001', 160282, 'Waitlist', '');

