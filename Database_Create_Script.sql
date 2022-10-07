-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------

-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Roles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `description` VARCHAR(200) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Skills`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Skills` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `description` VARCHAR(200) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Staff_Group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Staff_Group` (
  `Staff_Group_ID` INT NOT NULL,
  `Staff_Group_Name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`Staff_Group_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Staff` (
  `Staff_ID` INT NOT NULL,
  `Staff_FName` VARCHAR(50) NOT NULL,
  `Staff_LName` VARCHAR(50) NOT NULL,
  `Dept` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(50) NOT NULL,
  `Username` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  `Position_ID` INT NOT NULL,
  PRIMARY KEY (`Staff_ID`),
  UNIQUE INDEX `id_UNIQUE` (`Staff_ID` ASC) VISIBLE,
  INDEX `fk_Staff_Position_idx` (`Position_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Staff_Position`
    FOREIGN KEY (`Position_ID`)
    REFERENCES `mydb`.`Staff_Group` (`Staff_Group_ID`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Courses` (
  `Course_ID` VARCHAR(20) NOT NULL,
  `Course_Name` VARCHAR(50) NOT NULL,
  `Course_Description` VARCHAR(255) NULL,
  `Course_Status` VARCHAR(15) NULL,
  `Course_Type` VARCHAR(10) NULL,
  `Course_Category` VARCHAR(50) NULL,
  PRIMARY KEY (`Course_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Learning Journey`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Learning Journey` (
  `id` INT UNSIGNED NOT NULL,
  `Completion_Status` VARCHAR(45) NULL,
  `Roles_id` INT NOT NULL,
  `Staff_ID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Learning Journey_Roles1_idx` (`Roles_id` ASC) VISIBLE,
  INDEX `fk_Learning Journey_Staff1_idx` (`Staff_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Learning Journey_Roles1`
    FOREIGN KEY (`Roles_id`)
    REFERENCES `mydb`.`Roles` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Learning Journey_Staff1`
    FOREIGN KEY (`Staff_ID`)
    REFERENCES `mydb`.`Staff` (`Staff_ID`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Registration`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Registration` (
  `Reg_ID` INT NOT NULL,
  `Reg_Status` VARCHAR(20) NULL,
  `Completion_Status` VARCHAR(20) NULL,
  `Staff_ID` INT NOT NULL,
  `Course_ID` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`Reg_ID`, `Staff_ID`, `Course_ID`),
  INDEX `fk_Courses_has_Staff_Staff1_idx` (`Staff_ID` ASC) VISIBLE,
  INDEX `fk_Courses_has_Staff_Courses1_idx` (`Course_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Courses_has_Staff_Courses1`
    FOREIGN KEY (`Course_ID`)
    REFERENCES `mydb`.`Courses` (`Course_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Courses_has_Staff_Staff1`
    FOREIGN KEY (`Staff_ID`)
    REFERENCES `mydb`.`Staff` (`Staff_ID`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Roles_Skills`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Roles_Skills` (
  `Roles_id` INT NOT NULL,
  `Skills_id` INT NOT NULL,
  PRIMARY KEY (`Roles_id`, `Skills_id`),
  INDEX `fk_Roles_has_Skills_Skills1_idx` (`Skills_id` ASC) VISIBLE,
  INDEX `fk_Roles_has_Skills_Roles1_idx` (`Roles_id` ASC) VISIBLE,
  CONSTRAINT `fk_Roles_has_Skills_Roles1`
    FOREIGN KEY (`Roles_id`)
    REFERENCES `mydb`.`Roles` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Roles_has_Skills_Skills1`
    FOREIGN KEY (`Skills_id`)
    REFERENCES `mydb`.`Skills` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Courses_Skills`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Courses_Skills` (
  `Courses_Course_ID` VARCHAR(20) NOT NULL,
  `Skills_id` INT NOT NULL,
  PRIMARY KEY (`Courses_Course_ID`, `Skills_id`),
  INDEX `fk_Courses_has_Skills_Skills1_idx` (`Skills_id` ASC) VISIBLE,
  INDEX `fk_Courses_has_Skills_Courses1_idx` (`Courses_Course_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Courses_has_Skills_Courses1`
    FOREIGN KEY (`Courses_Course_ID`)
    REFERENCES `mydb`.`Courses` (`Course_ID`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_Courses_has_Skills_Skills1`
    FOREIGN KEY (`Skills_id`)
    REFERENCES `mydb`.`Skills` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
