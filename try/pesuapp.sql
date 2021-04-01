-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 01, 2021 at 09:12 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pesuapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

create DATABASE pesuapp;
use pesuapp;

CREATE TABLE `admin` (
  `id` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `password`, `name`) VALUES
('1235', 'sahith02.cods@gmail.com', 'password4', 'sahith02 cods'),
('1234', 'sahith02@gmail.com', 'password1', 'sahith02'),
('12310', 'sahith02@yahoo.com', 'password3', 'sahith02 yahoo'),
('1232', 'sahithk02@gmail.com', 'password2', 'sahithk02');

-- --------------------------------------------------------

--
-- Table structure for table `announcement`
--

CREATE TABLE `announcement` (
  `id` varchar(10) NOT NULL,
  `title` varchar(50) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `description` varchar(300) DEFAULT NULL,
  `picture_link` varchar(100) DEFAULT NULL,
  `hyperlink` varchar(100) DEFAULT NULL,
  `posting_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `announcement`
--

INSERT INTO `announcement` (`id`, `title`, `location`, `description`, `picture_link`, `hyperlink`, `posting_time`) VALUES
('1', 'Kindly note a student registering for Special ESA ', 'MRD', 'Kindly note a student registering for Special ESA / Backlog Course can take a maximum of 20 credits in May 2021 ESA. This limit includes both Special ESA + Backlog Course. For Example: If a student has registered for 8 credits in backlog he/she can take a maximum of 12 credits in Special ESA.', 'https://leverageedu.com/blog/wp-content/uploads/2019/08/Course-after-MBA.png', 'https://www3.nd.edu/~pkamat/pdf/researchpaper.pdf', '2021-03-31 21:41:07'),
('2', 'ESA March-April 2021 Time Table for BBAHEM 6th sem', '', 'ESA March-April 2021 Time Table for BBAHEM 6th sem', 'https://cdn1.vectorstock.com/i/1000x1000/53/10/school-timetable-icon-vector-13465310.jpg', 'https://www3.nd.edu/~pkamat/pdf/researchpaper.pdf', '2021-03-31 21:41:07'),
('3', 'From the VC\'s desk - Bulletin #19, March 12, 2021', '', 'From the VC\'s desk', 'http://tiny.cc/97gvtz', '', '2021-03-31 21:41:07');

-- --------------------------------------------------------

--
-- Table structure for table `coufac`
--

CREATE TABLE `coufac` (
  `facultyid` varchar(10) NOT NULL,
  `courseid` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `coufac`
--

INSERT INTO `coufac` (`facultyid`, `courseid`) VALUES
('1234567891', '2345678911'),
('1234567891', '2345678912'),
('1234567891', '2345678914'),
('1234567892', '2345678914'),
('1234567893', '2345678913'),
('1234567894', '2345678911');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `courseid` varchar(10) NOT NULL,
  `coursetitle` varchar(50) NOT NULL,
  `department` varchar(5) NOT NULL,
  `coursedetails` varchar(800) NOT NULL,
  `avl` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`courseid`, `coursetitle`, `department`, `coursedetails`, `avl`) VALUES
('2345678911', 'DBMS', 'CSE', 'Database Management Course Basics', 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-830-database-systems-fall-2010/'),
('2345678912', 'DAA', 'CSE', 'Design and Analysis of Algorithms', 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/'),
('2345678913', 'Thermodynamics', 'Mech', 'Thermal Systems', 'https://ocw.mit.edu/courses/mechanical-engineering/'),
('2345678914', 'OOAD', 'CSE', 'Software Engineering', 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-1-software-engineering/');

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `FacultyID` varchar(10) NOT NULL,
  `Name` varchar(10) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `ContactNumber` varchar(10) DEFAULT NULL,
  `Address` varchar(50) NOT NULL,
  `DateOfJoining` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`FacultyID`, `Name`, `Email`, `ContactNumber`, `Address`, `DateOfJoining`) VALUES
('1234567891', 'ahith02', 'ahith02@gmail.com', '0123456789', 'addr1', '2021-03-31 21:58:18'),
('1234567892', 'ahithk02', 'ahithk02@gmail.com', '0123456789', 'addr2', '2021-03-31 21:58:18'),
('1234567893', 'ahith02 ya', 'ahith02@yahoo.com', '0123456789', 'addr3', '2021-03-31 21:58:19'),
('1234567894', 'ahith02 co', 'ahith02.cods@gmail.com', '0123456789', 'addr4', '2021-03-31 21:58:19');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `CourseID` varchar(10) NOT NULL,
  `StudentID` varchar(10) NOT NULL,
  `Review` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`CourseID`, `StudentID`, `Review`) VALUES
('2345678911', '3456789121', 'review1'),
('2345678912', '3456789122', 'review2'),
('2345678913', '3456789123', 'review3'),
('2345678914', '3456789124', 'review4');

-- --------------------------------------------------------

--
-- Table structure for table `stucou`
--

CREATE TABLE `stucou` (
  `courseid` varchar(10) NOT NULL,
  `studentid` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stucou`
--

INSERT INTO `stucou` (`courseid`, `studentid`) VALUES
('2345678911', '3456789121'),
('2345678911', '3456789122'),
('2345678911', '3456789124'),
('2345678912', '3456789121'),
('2345678913', '3456789123'),
('2345678914', '3456789122'),
('2345678914', '3456789124');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `emailid` varchar(50) NOT NULL,
  `studname` varchar(50) NOT NULL,
  `srn` varchar(10) NOT NULL,
  `pgm` varchar(7) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phonenumber` varchar(10) DEFAULT NULL,
  `branch` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`emailid`, `studname`, `srn`, `pgm`, `address`, `phonenumber`, `branch`) VALUES
('abcd@gmail.com', 'abcd', '3456789121', 'BTECH', 'delhi-6', '1234567890', 'CSE'),
('abcde@gmail.com', 'abcde', '3456789122', 'BTECH', 'bangalore-4', '1234567890', 'CSE'),
('abcdef@gmail.com', 'abcdef', '3456789123', 'BTECH', 'kolkata-42', '1234567890', 'Mech'),
('abcdefg@gmail.com', 'abcdefg', '3456789124', 'BTECH', 'hyderabad-7', '1234567890', 'CSE');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `account_type` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`, `account_type`) VALUES
('abcd@gmail.com', '$5$rounds=535000$WvBiO5VEAtVXe/zf$9eCrSEV1WU3cIJdYF8hu6xeCoTYsbafrCeso/60.N6C', 'student'),
('abcde@gmail.com', '$5$rounds=535000$Cpavc78gsOImhyjy$ASx00peaIhHiwrpmz33qwy0AOQr7Os0ZT.5d6suGF9.', 'student'),
('abcdef@gmail.com', '$5$rounds=535000$t0TR8gLWbKRsaOoM$f0ROZOha/4TuFgSmbgnYXh7XkYdXQI5/4o.8ei1tAO2', 'student'),
('abcdefg@gmail.com', '$5$rounds=535000$anS6Yb8DXUnz58za$39ifX.zU6u1CyagOo2Wh813o2xYhafq06cYm7Xz7l32', 'student'),
('ahith02.cods@gmail.com', '$5$rounds=535000$dcMD8X5luDL6595X$ZljgpNgc9t9aFpW0ujCXgMA0IB9R//hoDrhgybWb6Z4', 'faculty'),
('ahith02@gmail.com', '$5$rounds=535000$ThsxoXxmsN.soL99$7sc5IR5lcMArrR.74TqZHcd/FEkC0UN48SfGz52Ln62', 'faculty'),
('ahith02@yahoo.com', '$5$rounds=535000$EeFr7Ukxeum8Cq98$bm4mIvJWpYDrplCvElGqPdhU/Xh7KVFK.XE5JRPHplC', 'faculty'),
('ahithk02@gmail.com', '$5$rounds=535000$B0eoXOpARWJQUP/7$DHx0gRAreIMNy.Wm1hX3fDHi2n77MaHDDdO6oHoIGID', 'faculty'),
('sahith02.cods@gmail.com', '$5$rounds=535000$tsNuJNwmt68L3pYa$kghyV48OPSXnkYB3SgIiCJkzvDXOXRotqYVQPL3HzW8', 'admin'),
('sahith02@gmail.com', '$5$rounds=535000$.SEYq/T5mWYBflVR$Lx.OMNSCA7j4F1ADk.LjLEwYAvfdFsSOolINpRcoHXD', 'admin'),
('sahith02@yahoo.com', '$5$rounds=535000$W2oBb5SV0JEr/uft$GkkV.G2vuKmeQz7H.fgqd/L4pfoZzhuBOQ0YgoJ7GZ9', 'admin'),
('sahithk02@gmail.com', '$5$rounds=535000$E6fm4aLIqeCkV9Om$rCU2k19s6nKv6UZjyxUZMwOq84TgHIZuQZC3GycCfe4', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `announcement`
--
ALTER TABLE `announcement`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `coufac`
--
ALTER TABLE `coufac`
  ADD PRIMARY KEY (`facultyid`,`courseid`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`courseid`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`FacultyID`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `Address` (`Address`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`CourseID`,`StudentID`);

--
-- Indexes for table `stucou`
--
ALTER TABLE `stucou`
  ADD PRIMARY KEY (`courseid`,`studentid`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`emailid`,`srn`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
