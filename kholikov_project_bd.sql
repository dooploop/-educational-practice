-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema study_proj
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema study_proj
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `study_proj` DEFAULT CHARACTER SET utf8mb3 ;
USE `study_proj` ;

-- -----------------------------------------------------
-- Table `study_proj`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `study_proj`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `usercol` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `study_proj`.`info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `study_proj`.`info` (
  `info_pers` INT NOT NULL,
  `user_iduser` INT NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  INDEX `fk_cus_user_idx` (`user_iduser` ASC) VISIBLE,
  CONSTRAINT `fk_cus_user`
    FOREIGN KEY (`user_iduser`)
    REFERENCES `study_proj`.`user` (`iduser`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `study_proj`.`user`
-- -----------------------------------------------------
START TRANSACTION;
USE `study_proj`;
INSERT INTO `study_proj`.`user` (`iduser`, `usercol`) VALUES (1, 'amir');

COMMIT;


-- -----------------------------------------------------
-- Data for table `study_proj`.`info`
-- -----------------------------------------------------
START TRANSACTION;
USE `study_proj`;
INSERT INTO `study_proj`.`info` (`info_pers`, `user_iduser`, `id`) VALUES (35, 1, 1);
INSERT INTO `study_proj`.`info` (`info_pers`, `user_iduser`, `id`) VALUES (25, 1, 2);

COMMIT;

