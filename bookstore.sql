-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 12, 2024 at 02:54 PM
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
  `date` date DEFAULT NULL,
  `cover` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`ISBN`, `title`, `author`, `publisher`, `genre`, `price`, `stock`, `date`, `cover`) VALUES
('01', 'Kafka on the Shore', 'Murakami Haruki', 'Vintage Books', 'Literature', 12.99, 10, '2002-09-12', 'kafka_on_the_shore.jpg'),
('02', '1Q84 Books 1 and 2', 'Murakami Haruki', 'Vintage Books', 'Literature', 13.99, 9, '2009-05-29', '1q84_1.jpg'),
('03', '1Q84 Book 3', 'Murakami Haruki', 'Vintage Books', 'Literature', 13.99, 2, '2010-04-10', '1q84_3.jpg'),
('04', 'Kokoro', 'Natsume Soseki', 'Vintage Books', 'Literature', 11.99, 6, '1914-08-11', 'kokoro.jpg'),
('05', 'Nakahara Chuuya Poems', 'Nakahara Chuuya', 'Gracewing', 'Poems', 16.99, 1, '2004-02-01', 'chuuya_poems.jpg'),
('06', '100 poems, 100 authors', '-', 'Penguin Classics', 'Poems', 12.99, 20, '2007-07-20', 'poems.jpg'),
('07', 'Goodnight Punpun Volume 1', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 6, '2007-08-03', 'pun_1.jpg'),
('08', 'Goodnight Punpun Volume 2', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 6, '2007-12-28', 'pun_2.jpg'),
('09', 'Goodnight Punpun Volume 3', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 8, '2008-06-05', 'pun_3.jpg'),
('10', 'JOJO Stone Ocean Volume 1', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 22, '2008-04-18', 'stone_ocean_1.jgp'),
('11', 'JOJO Stone Ocean Volume 2', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 3, '2008-05-16', 'stone_ocean_2.jgp'),
('12', 'JOJO Stone Ocean Volume 3', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 24, '2008-06-18', 'stone_ocean_3.jgp'),
('13', 'Snow Country', 'Kawabata Yasunari', 'Knopf Doubleday Publishing Gro', 'Literature', 9.99, -1, '1948-11-05', 'snow_country.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `buys`
--

CREATE TABLE `buys` (
  `Transaction_ID` int(100) NOT NULL,
  `book_ISBN` varchar(12) NOT NULL,
  `quantity` int(30) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
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

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `username`, `password`, `country`, `city`, `street`, `street_num`, `postal_code`, `phone`, `email`) VALUES
(1, 'phn', 'user', '123456789', 'greece', 'athens', 'phn', '51', '11242', '6985414123', 'phn@gmail.com'),
(2, 'Sofiaa', 'sofiaaa', '12345', 'greece', 'athens', 'miaou', '2', '35100', '6940884497', 'dndif@jfi.com'),
(3, 'sofia', 'sofini', '12345', 'greece', 'ath', 'ath', '2', '12345', '1234567890', 'sof@gmail.com'),
(4, 'test', 'test', '12345', 'sdvc', 'dsvgsdft', 'detf', '3', '12345', '1234565890', 'sdvg@gmail.com'),
(5, 'Jolyne', 'jolyne', '12345', 'Japan', '', 'Jojolandstreet', '12', '1234', '14534423', 'wheresmydad@gmail.com'),
(6, 'Jotaro', 'jotaro', '12345', 'Japan', 'Tokyo', '3232GSHJKS', '2', '232', '343434323', 'jotaro@gmail.com'),
(7, 'diavolo', 'diavolo', '12345', 'Japan', 'DLSKJSKD', 'ABSJAHDLKASJ', '1', '123', '2325345345', 'diavolo@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `sells`
--

CREATE TABLE `sells` (
  `Transaction_ID` int(100) NOT NULL,
  `customer_id` int(10) NOT NULL,
  `book_ISBN` varchar(12) NOT NULL,
  `quantity` int(30) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sells`
--

INSERT INTO `sells` (`Transaction_ID`, `customer_id`, `book_ISBN`, `quantity`, `date`) VALUES
(17, 6, '11', 1, '2024-06-12'),
(18, 6, '10', 1, '2024-06-12'),
(19, 6, '12', 1, '2024-06-12'),
(20, 5, '11', 1, '2024-06-12'),
(21, 5, '10', 1, '2024-06-12'),
(22, 5, '10', 1, '2024-06-12'),
(23, 5, '12', 1, '2024-06-12'),
(24, 7, '11', 1, '2024-06-12'),
(25, 7, '12', 1, '2024-06-12'),
(26, 4, '07', 1, '2024-06-12'),
(27, 4, '08', 1, '2024-06-12'),
(28, 1, '07', 1, '2024-06-12'),
(29, 1, '08', 1, '2024-06-12'),
(30, 1, '09', 1, '2024-06-12'),
(31, 3, '07', 1, '2024-06-12'),
(32, 3, '08', 1, '2024-06-12'),
(33, 3, '09', 1, '2024-06-12');

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
  ADD KEY `book_ISBN` (`book_ISBN`);

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
  MODIFY `Transaction_ID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `sells`
--
ALTER TABLE `sells`
  MODIFY `Transaction_ID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buys`
--
ALTER TABLE `buys`
  ADD CONSTRAINT `buys_ibfk_1` FOREIGN KEY (`book_ISBN`) REFERENCES `books` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE;

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
