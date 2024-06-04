-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2024 at 01:50 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `ID` int(10) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`ID`, `username`, `password`) VALUES
(1, 'Chris', '123456'),
(2, 'Antonis', 'qwerty'),
(3, 'Sofia', '000000'),
(4, 'Panos', '123123');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `ISBN` varchar(12) NOT NULL,
  `title` varchar(30) NOT NULL,
  `author` varchar(30) NOT NULL,
  `publisher` varchar(30) NOT NULL,
  `genre` varchar(30) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(100) NOT NULL,
  `cover` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`ISBN`, `title`, `author`, `publisher`, `genre`, `price`, `stock`, `cover`) VALUES
('01', 'Kafka on the Shore', 'Murakami Haruki', 'Vintage Books', 'Literature', 12.99, 0, 0x6b61666b615f6f6e5f7468655f73686f72652e6a7067),
('02', '1Q84 Books 1 and 2', 'Murakami Haruki', 'Vintage Books', 'Literature', 13.99, 0, 0x317138345f312e6a7067),
('03', '1Q84 Book 3', 'Murakami Haruki', 'Vintage Books', 'Literature', 13.99, 0, 0x317138345f332e6a7067),
('04', 'Kokoro', 'Natsume Soseki', 'Vintage Books', 'Literature', 11.99, 0, 0x6b6f6b6f726f2e6a7067),
('05', 'Nakahara Chuuya Poems', 'Nakahara Chuuya', 'Gracewing', 'Poems', 16.99, 0, 0x6368757579615f706f656d732e6a7067),
('06', '100 poems, 100 authors', '-', 'Penguin Classics', 'Poems', 12.99, 0, 0x706f656d732e6a7067),
('07', 'Goodnight Punpun Volume 1', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 0, 0x70756e5f312e6a7067),
('08', 'Goodnight Punpun Volume 2', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 0, 0x70756e5f322e6a7067),
('09', 'Goodnight Punpun Volume 3', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 0, 0x70756e5f332e6a7067),
('10', 'JOJO Stone Ocean Volume 1', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 0, 0x73746f6e655f6f6365616e5f312e6a6770),
('11', 'JOJO Stone Ocean Volume 2', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 0, 0x73746f6e655f6f6365616e5f322e6a6770),
('12', 'JOJO Stone Ocean Volume 3', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 0, 0x73746f6e655f6f6365616e5f332e6a6770),
('13', 'Snow Country', 'Kawabata Yasunari', 'Knopf Doubleday Publishing Gro', 'Literature', 9.99, 0, 0x736e6f775f636f756e7472792e6a7067);

-- --------------------------------------------------------

--
-- Table structure for table `buys`
--

CREATE TABLE `buys` (
  `Transaction_ID` int(100) NOT NULL,
  `supplier_id` int(10) NOT NULL,
  `book_ISBN` varchar(12) NOT NULL,
  `quantity` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(12) NOT NULL,
  `name` varchar(30) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `country` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `street` varchar(30) NOT NULL,
  `street_num` varchar(3) NOT NULL,
  `postal_code` varchar(10) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sells`
--

CREATE TABLE `sells` (
  `Transaction_ID` int(100) NOT NULL,
  `customer_id` int(10) NOT NULL,
  `book_ISBN` varchar(12) NOT NULL,
  `quantity` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `id` int(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `country` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `street` varchar(30) NOT NULL,
  `street_number` varchar(10) NOT NULL,
  `postal_code` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`ISBN`);

--
-- Indexes for table `buys`
--
ALTER TABLE `buys`
  ADD PRIMARY KEY (`Transaction_ID`),
  ADD KEY `book_ISBN` (`book_ISBN`),
  ADD KEY `supplier_id` (`supplier_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sells`
--
ALTER TABLE `sells`
  ADD PRIMARY KEY (`Transaction_ID`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `book_ISBN` (`book_ISBN`) USING BTREE;

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `buys`
--
ALTER TABLE `buys`
  MODIFY `Transaction_ID` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sells`
--
ALTER TABLE `sells`
  MODIFY `Transaction_ID` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `supplier`
--
ALTER TABLE `supplier`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buys`
--
ALTER TABLE `buys`
  ADD CONSTRAINT `buys_ibfk_1` FOREIGN KEY (`book_ISBN`) REFERENCES `books` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `buys_ibfk_3` FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sells`
--
ALTER TABLE `sells`
  ADD CONSTRAINT `sells_ibfk_2` FOREIGN KEY (`book_ISBN`) REFERENCES `books` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sells_ibfk_3` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
