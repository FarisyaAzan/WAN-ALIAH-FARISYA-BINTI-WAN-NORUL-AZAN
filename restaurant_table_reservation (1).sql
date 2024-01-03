-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 09:49 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `restaurant_table_reservation`
--

-- --------------------------------------------------------

--
-- Table structure for table `reservation_info`
--

CREATE TABLE `reservation_info` (
  `customer_name` varchar(30) NOT NULL,
  `phone_number` int(10) NOT NULL,
  `party_size` int(11) NOT NULL,
  `deposit_amount_rm` decimal(10,2) NOT NULL,
  `reservation_datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservation_info`
--

INSERT INTO `reservation_info` (`customer_name`, `phone_number`, `party_size`, `deposit_amount_rm`, `reservation_datetime`) VALUES
('wan aliah farisya', 196711838, 6, 30.00, '2024-01-01 16:23:33'),
('WAN ALIAH FARISYA', 196711838, 7, 35.00, '2024-03-03 21:00:00'),
('WAN ALIAH FARISYA', 196711838, 6, 30.00, '2024-03-03 21:00:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
