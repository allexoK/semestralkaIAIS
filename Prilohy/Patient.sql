-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 14, 2020 at 05:19 PM
-- Server version: 5.7.31-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Patient`
--

-- --------------------------------------------------------

--
-- Table structure for table `Diagnostics`
--

CREATE TABLE `Diagnostics` (
  `id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_czech_ci NOT NULL,
  `icd-10` varchar(16) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Diagnostics`
--

INSERT INTO `Diagnostics` (`id`, `name`, `icd-10`) VALUES
(1, 'Respiratory tuberculosis', 'A15'),
(3, 'Viral warts', 'B07'),
(4, 'Taeniasis', 'B68');

-- --------------------------------------------------------

--
-- Table structure for table `Diagnostics choise`
--

CREATE TABLE `Diagnostics choise` (
  `id` int(11) NOT NULL,
  `diagnosticsId` int(11) NOT NULL,
  `visitId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Diagnostics choise`
--

INSERT INTO `Diagnostics choise` (`id`, `diagnosticsId`, `visitId`) VALUES
(23, 3, 40),
(24, 3, 4),
(25, 4, 4),
(26, 4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `Doctor`
--

CREATE TABLE `Doctor` (
  `id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_czech_ci NOT NULL,
  `login` varchar(64) COLLATE utf8_czech_ci NOT NULL,
  `password` varchar(64) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Doctor`
--

INSERT INTO `Doctor` (`id`, `name`, `login`, `password`) VALUES
(1111, 'Jan Novak', 'janvak', 'jan123');

-- --------------------------------------------------------

--
-- Table structure for table `Intervention`
--

CREATE TABLE `Intervention` (
  `id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_czech_ci NOT NULL,
  `snomed` varchar(16) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Intervention`
--

INSERT INTO `Intervention` (`id`, `name`, `snomed`) VALUES
(121356, 'General treatment', '7922000'),
(121357, 'Provider-specific procedure', '127777001'),
(121358, 'Obstetric procedure', '386637004');

-- --------------------------------------------------------

--
-- Table structure for table `Intervention choise`
--

CREATE TABLE `Intervention choise` (
  `id` int(11) NOT NULL,
  `interventionId` int(11) NOT NULL,
  `visitId` int(11) NOT NULL,
  `date` date NOT NULL,
  `result` varchar(64) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Intervention choise`
--

INSERT INTO `Intervention choise` (`id`, `interventionId`, `visitId`, `date`, `result`) VALUES
(37, 121357, 40, '2020-11-12', 'pos');

-- --------------------------------------------------------

--
-- Table structure for table `Medicine`
--

CREATE TABLE `Medicine` (
  `id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_czech_ci NOT NULL,
  `snomed` varchar(8) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Medicine`
--

INSERT INTO `Medicine` (`id`, `name`, `snomed`) VALUES
(3, 'Urethan', '873008'),
(4, 'Vascormone', '2346005'),
(5, 'Fusarin', '28999000'),
(6, 'Satratoxins', '41492002');

-- --------------------------------------------------------

--
-- Table structure for table `Medicine choise`
--

CREATE TABLE `Medicine choise` (
  `medicineId` int(11) NOT NULL,
  `visitId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Medicine choise`
--

INSERT INTO `Medicine choise` (`medicineId`, `visitId`) VALUES
(4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `Patient`
--

CREATE TABLE `Patient` (
  `id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_czech_ci NOT NULL,
  `surname` varchar(32) COLLATE utf8_czech_ci NOT NULL,
  `doctorId` int(11) DEFAULT NULL,
  `gender` varchar(8) COLLATE utf8_czech_ci NOT NULL,
  `status` varchar(32) COLLATE utf8_czech_ci NOT NULL,
  `birthPlace` varchar(64) COLLATE utf8_czech_ci NOT NULL,
  `birthState` varchar(32) COLLATE utf8_czech_ci NOT NULL,
  `birthCity` varchar(32) COLLATE utf8_czech_ci NOT NULL,
  `birthPostal` int(11) NOT NULL,
  `birthDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Patient`
--

INSERT INTO `Patient` (`id`, `name`, `surname`, `doctorId`, `gender`, `status`, `birthPlace`, `birthState`, `birthCity`, `birthPostal`, `birthDate`) VALUES
(12332, 'Lenka', 'Lorencova', 1111, 'Female', 'Single', 'CR', '', 'Kladno', 27201, '1995-06-10'),
(42341, 'Jim', 'Moris', 1111, 'Male', 'Single', 'USA', 'Texas', 'Texas city', 1221, '1977-06-18'),
(42342, 'Lu', 'Kang', 1111, 'Male', 'Married', 'China', '', 'Pekin', 21201, '1973-06-09');

-- --------------------------------------------------------

--
-- Table structure for table `Visit`
--

CREATE TABLE `Visit` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `patientId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Visit`
--

INSERT INTO `Visit` (`id`, `date`, `patientId`) VALUES
(4, '2020-03-10', 42341),
(5, '2020-02-10', 42341),
(20, '2020-11-11', 42342),
(21, '2020-11-11', 42342),
(22, '2020-11-11', 42342),
(23, '2020-11-11', 42342),
(24, '2020-11-11', 42342),
(25, '2020-11-11', 42342),
(26, '2020-11-11', 42342),
(27, '2020-11-11', 42342),
(28, '2020-11-01', 42342),
(30, '2020-09-02', 42341),
(40, '2010-12-11', 12332),
(42, '2020-11-12', 12332);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Diagnostics`
--
ALTER TABLE `Diagnostics`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Diagnostics choise`
--
ALTER TABLE `Diagnostics choise`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diagnosticsId` (`diagnosticsId`),
  ADD KEY `Diagnostics choise_ibfk_2` (`visitId`);

--
-- Indexes for table `Doctor`
--
ALTER TABLE `Doctor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`);

--
-- Indexes for table `Intervention`
--
ALTER TABLE `Intervention`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Intervention choise`
--
ALTER TABLE `Intervention choise`
  ADD PRIMARY KEY (`id`),
  ADD KEY `interventionId` (`interventionId`),
  ADD KEY `Intervention choise_ibfk_2` (`visitId`);

--
-- Indexes for table `Medicine`
--
ALTER TABLE `Medicine`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Medicine choise`
--
ALTER TABLE `Medicine choise`
  ADD PRIMARY KEY (`medicineId`,`visitId`),
  ADD KEY `Medicine choise_ibfk_2` (`visitId`);

--
-- Indexes for table `Patient`
--
ALTER TABLE `Patient`
  ADD PRIMARY KEY (`id`),
  ADD KEY `doctorId` (`doctorId`);

--
-- Indexes for table `Visit`
--
ALTER TABLE `Visit`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patientId` (`patientId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Diagnostics`
--
ALTER TABLE `Diagnostics`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `Diagnostics choise`
--
ALTER TABLE `Diagnostics choise`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT for table `Intervention`
--
ALTER TABLE `Intervention`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121359;
--
-- AUTO_INCREMENT for table `Intervention choise`
--
ALTER TABLE `Intervention choise`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
--
-- AUTO_INCREMENT for table `Medicine`
--
ALTER TABLE `Medicine`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `Visit`
--
ALTER TABLE `Visit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Diagnostics choise`
--
ALTER TABLE `Diagnostics choise`
  ADD CONSTRAINT `Diagnostics choise_ibfk_1` FOREIGN KEY (`diagnosticsId`) REFERENCES `Diagnostics` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Diagnostics choise_ibfk_2` FOREIGN KEY (`visitId`) REFERENCES `Visit` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Intervention choise`
--
ALTER TABLE `Intervention choise`
  ADD CONSTRAINT `Intervention choise_ibfk_1` FOREIGN KEY (`interventionId`) REFERENCES `Intervention` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Intervention choise_ibfk_2` FOREIGN KEY (`visitId`) REFERENCES `Visit` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Medicine choise`
--
ALTER TABLE `Medicine choise`
  ADD CONSTRAINT `Medicine choise_ibfk_1` FOREIGN KEY (`medicineId`) REFERENCES `Medicine` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Medicine choise_ibfk_2` FOREIGN KEY (`visitId`) REFERENCES `Visit` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Patient`
--
ALTER TABLE `Patient`
  ADD CONSTRAINT `Patient_ibfk_1` FOREIGN KEY (`doctorId`) REFERENCES `Doctor` (`id`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Constraints for table `Visit`
--
ALTER TABLE `Visit`
  ADD CONSTRAINT `Visit_ibfk_1` FOREIGN KEY (`patientId`) REFERENCES `Patient` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
