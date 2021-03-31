CREATE TABLE `pesuapp`.`feedback` (
  `CourseID` VARCHAR(10) NOT NULL,
  `StudentID` VARCHAR(10) NOT NULL,
  `Review` VARCHAR(1000) NULL,
  PRIMARY KEY (`CourseID`, `StudentID`));

INSERT INTO `pesuapp`.`feedback` (`CourseID`, `StudentID`, `Review`) VALUES ("2345678911", "3456789121", "review1");
INSERT INTO `pesuapp`.`feedback` (`CourseID`, `StudentID`, `Review`) VALUES ("2345678912", "3456789122", "review2");
INSERT INTO `pesuapp`.`feedback` (`CourseID`, `StudentID`, `Review`) VALUES ("2345678913", "3456789123", "review3");
INSERT INTO `pesuapp`.`feedback` (`CourseID`, `StudentID`, `Review`) VALUES ("2345678914", "3456789124", "review4");

SELECT Review FROM feedback WHERE CourseID = "c1" AND StudentID = "s1";

CREATE TABLE `pesuapp`.`faculty` (
  `FacultyID` VARCHAR(10) NOT NULL,
  `Name` VARCHAR(10) NOT NULL,
  `Email` VARCHAR(50) NOT NULL UNIQUE,
  `ContactNumber` VARCHAR(10) NULL,
  `Address` VARCHAR(50) NOT NULL UNIQUE,
  `DateOfJoining` DATETIME NULL,
  PRIMARY KEY (`FacultyID`));


INSERT INTO `pesuapp`.`faculty` (`FacultyID`, `Name`, `email`, `ContactNumber`, `Address`, `DateOfJoining`) 
VALUES ("f1", "ahith02", "ahith02@gmail.com", "0123456789", "addr1", NOW());
INSERT INTO `pesuapp`.`faculty` (`FacultyID`, `Name`, `email`, `ContactNumber`, `Address`, `DateOfJoining`) 
VALUES ("f2", "ahithk02", "ahithk02@gmail.com", "0123456789", "addr2", NOW());
INSERT INTO `pesuapp`.`faculty` (`FacultyID`, `Name`, `email`, `ContactNumber`, `Address`, `DateOfJoining`) 
VALUES ("f3", "ahith02 yahoo", "ahith02@yahoo.com", "0123456789", "addr3", NOW());
INSERT INTO `pesuapp`.`faculty` (`FacultyID`, `Name`, `email`, `ContactNumber`, `Address`, `DateOfJoining`)
VALUES ("f4", "ahith02 cods", "ahith02.cods@gmail.com", "0123456789", "addr4", NOW());

SELECT FacultyID, Email FROM faculty WHERE email = "ahith02@yahoo.com";

