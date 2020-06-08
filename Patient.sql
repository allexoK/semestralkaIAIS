-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 08, 2020 at 08:11 PM
-- Server version: 5.7.30-0ubuntu0.18.04.1
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
  `date` date NOT NULL,
  `result` varchar(256) COLLATE utf8_czech_ci DEFAULT NULL,
  `patientId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Diagnostics`
--

INSERT INTO `Diagnostics` (`id`, `name`, `date`, `result`, `patientId`) VALUES
(1, 'Reaction tests', '2020-03-19', '', 421441),
(2, 'HIV test', '2020-03-25', 'Negative result', 12331);

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
  `date` date NOT NULL,
  `patientId` int(11) NOT NULL,
  `snomed` varchar(8) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Intervention`
--

INSERT INTO `Intervention` (`id`, `name`, `date`, `patientId`, `snomed`) VALUES
(121351, 'Excision of lesion of patella', '2020-11-11', 12331, '104001'),
(121352, 'Behavioral therapy', '2020-11-11', 12331, '166001');

-- --------------------------------------------------------

--
-- Table structure for table `Medicine`
--

CREATE TABLE `Medicine` (
  `id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Medicine`
--

INSERT INTO `Medicine` (`id`, `name`) VALUES
(3, 'Sebidin'),
(4, 'Ibuprophen');

-- --------------------------------------------------------

--
-- Table structure for table `Medicine choise`
--

CREATE TABLE `Medicine choise` (
  `medicineId` int(11) NOT NULL,
  `patientId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Medicine choise`
--

INSERT INTO `Medicine choise` (`medicineId`, `patientId`) VALUES
(3, 12331);

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
(12331, 'Lenka', 'Lorencova', 1111, 'Female', 'Single', 'CR', '', 'Kladno', 27201, '1995-06-10'),
(42342, 'Lu', 'Kang', 1111, 'Male', 'Married', 'China', '', 'Pekin', 21201, '1973-06-09'),
(421441, 'Jim', 'Moris', 1111, 'Male', 'Single', 'USA', 'Texas', 'Texas city', 1221, '1977-06-18');

-- --------------------------------------------------------

--
-- Table structure for table `Visit`
--

CREATE TABLE `Visit` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `goal` varchar(256) COLLATE utf8_czech_ci DEFAULT NULL,
  `patientId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Dumping data for table `Visit`
--

INSERT INTO `Visit` (`id`, `date`, `goal`, `patientId`) VALUES
(3, '2020-03-12', NULL, 12331),
(4, '2020-03-10', '', 421441),
(5, '2020-02-10', NULL, 421441);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Diagnostics`
--
ALTER TABLE `Diagnostics`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Diagnostics_ibfk_1` (`patientId`);

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
  ADD PRIMARY KEY (`id`),
  ADD KEY `Intervention_ibfk_1` (`patientId`);

--
-- Indexes for table `Medicine`
--
ALTER TABLE `Medicine`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Medicine choise`
--
ALTER TABLE `Medicine choise`
  ADD PRIMARY KEY (`medicineId`,`patientId`),
  ADD KEY `Medicine choise_ibfk_2` (`patientId`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `Intervention`
--
ALTER TABLE `Intervention`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121353;
--
-- AUTO_INCREMENT for table `Medicine`
--
ALTER TABLE `Medicine`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `Visit`
--
ALTER TABLE `Visit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Diagnostics`
--
ALTER TABLE `Diagnostics`
  ADD CONSTRAINT `Diagnostics_ibfk_1` FOREIGN KEY (`patientId`) REFERENCES `Patient` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Intervention`
--
ALTER TABLE `Intervention`
  ADD CONSTRAINT `Intervention_ibfk_1` FOREIGN KEY (`patientId`) REFERENCES `Patient` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Medicine choise`
--
ALTER TABLE `Medicine choise`
  ADD CONSTRAINT `Medicine choise_ibfk_1` FOREIGN KEY (`medicineId`) REFERENCES `Medicine` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Medicine choise_ibfk_2` FOREIGN KEY (`patientId`) REFERENCES `Patient` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

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
