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

UPDATE `pesuapp`.`announcement` SET `title` = 'PESU Pre-Placement Training Test', `description` = 'Dear Student,<br/>This is to inform you about the pre placement test coming up soon.<br/>Hope to see all of you participate!<br/>have a nice day!', `picture_link` = 'https://ielts.com.au/wp-content/uploads/2020/03/IELTS-Writing-Assist-Portal.jpg', `hyperlink` = 'http://ppt.pes.edu/' WHERE (`id` = '4');
UPDATE `pesuapp`.`announcement` SET `title` = 'From the VC\'s desk - Bulletin #19, March 12, 2021', `description` = 'From the VC\'s desk', `picture_link` = 'http://tiny.cc/97gvtz', `hyperlink` = '' WHERE (`id` = '3');
UPDATE `pesuapp`.`announcement` SET `title` = 'ESA March-April 2021 Time Table for BBAHEM 6th sem', `description` = 'ESA March-April 2021 Time Table for BBAHEM 6th sem', `picture_link` = 'https://cdn1.vectorstock.com/i/1000x1000/53/10/school-timetable-icon-vector-13465310.jpg', `hyperlink` = 'https://www3.nd.edu/~pkamat/pdf/researchpaper.pdf' WHERE (`id` = '2');
UPDATE `pesuapp`.`announcement` SET `title` = 'Kindly note a student registering for Special ESA ', `description` = 'Kindly note a student registering for Special ESA / Backlog Course can take a maximum of 20 credits in May 2021 ESA. This limit includes both Special ESA + Backlog Course. For Example: If a student has registered for 8 credits in backlog he/she can take a maximum of 12 credits in Special ESA.', `picture_link` = 'https://leverageedu.com/blog/wp-content/uploads/2019/08/Course-after-MBA.png', `hyperlink` = '' WHERE (`id` = '1');
