show databases;

create database PesuApp;
use pesuapp;
CREATE TABLE `pesuapp`.`admin` (
  `id` VARCHAR(10) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NULL,
  PRIMARY KEY (`email`));

INSERT INTO `pesuapp`.`admin` (`id`, `email`, `password`, `name`) VALUES ("1234", "sahith02@gmail.com", "password1", "sahith02");
INSERT INTO `pesuapp`.`admin` (`id`, `email`, `password`, `name`) VALUES ("1232", "sahithk02@gmail.com", "password2", "sahithk02");
INSERT INTO `pesuapp`.`admin` (`id`, `email`, `password`, `name`) VALUES ("12310", "sahith02@yahoo.com", "password3", "sahith02 yahoo");
INSERT INTO `pesuapp`.`admin` (`id`, `email`, `password`, `name`) VALUES ("1235", "sahith02.cods@gmail.com", "password4", "sahith02 cods");

SELECT id, email FROM admin WHERE email = "sahith02@yahoo.com";



CREATE TABLE `pesuapp`.`announcement` (
  `id` VARCHAR(10) NOT NULL,
  `title` VARCHAR(50) NOT NULL,
  `location` VARCHAR(50) NULL,
  `description` VARCHAR(300) NULL,
  `picture_link` VARCHAR(100) NULL,
  `hyperlink` VARCHAR(100) NULL,
  `posting_time` DATETIME NULL,
  PRIMARY KEY (`id`));
  
SELECT * FROM announcement;
SELECT NOW();

INSERT INTO `pesuapp`.`announcement` (`id`, `title`, `location`, `description`, `picture_link`, `hyperlink`, `posting_time`)
VALUES ("1", "title 1", "location 1", "description 1", "picture link 1", "hyperlink 1", NOW());
INSERT INTO `pesuapp`.`announcement` (`id`, `title`, `location`, `description`, `picture_link`, `hyperlink`, `posting_time`)
VALUES ("2", "title 2", "location 2", "description 2", "picture link 2", "hyperlink 2", NOW());
INSERT INTO `pesuapp`.`announcement` (`id`, `title`, `location`, `description`, `picture_link`, `hyperlink`, `posting_time`)
VALUES ("3", "title 3", "location 3", "description 3", "picture link 3", "hyperlink 3", NOW());
