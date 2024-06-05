-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Εξυπηρετητής: 127.0.0.1
-- Χρόνος δημιουργίας: 05 Ιουν 2024 στις 17:56:25
-- Έκδοση διακομιστή: 10.4.32-MariaDB
-- Έκδοση PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `bookstore`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `admins`
--

CREATE TABLE `admins` (
  `ID` int(10) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Άδειασμα δεδομένων του πίνακα `admins`
--

INSERT INTO `admins` (`ID`, `username`, `password`) VALUES
(1, 'Chris', '123456'),
(2, 'Antonis', 'qwerty'),
(3, 'Sofia', '000000'),
(4, 'Panos', '123123');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `books`
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
-- Άδειασμα δεδομένων του πίνακα `books`
--

INSERT INTO `books` (`ISBN`, `title`, `author`, `publisher`, `genre`, `price`, `stock`, `date`, `cover`) VALUES
('01', 'Kafka on the Shore', 'Murakami Haruki', 'Vintage Books', 'Literature', 12.99, 12, NULL, 'kafka_on_the_shore.jpg'),
('02', '1Q84 Books 1 and 2', 'Murakami Haruki', 'Vintage Books', 'Literature', 13.99, 10, NULL, '1q84_1.jpg'),
('03', '1Q84 Book 3', 'Murakami Haruki', 'Vintage Books', 'Literature', 13.99, 2, '0000-00-00', '1q84_3.jpg'),
('04', 'Kokoro', 'Natsume Soseki', 'Vintage Books', 'Literature', 11.99, 6, '0000-00-00', 'kokoro.jpg'),
('05', 'Nakahara Chuuya Poems', 'Nakahara Chuuya', 'Gracewing', 'Poems', 16.99, 1, '0000-00-00', 'chuuya_poems.jpg'),
('06', '100 poems, 100 authors', '-', 'Penguin Classics', 'Poems', 12.99, 20, '0000-00-00', 'poems.jpg'),
('07', 'Goodnight Punpun Volume 1', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 9, '0000-00-00', 'pun_1.jpg'),
('08', 'Goodnight Punpun Volume 2', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 9, '0000-00-00', 'pun_2.jpg'),
('09', 'Goodnight Punpun Volume 3', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 10, '0000-00-00', 'pun_3.jpg'),
('10', 'JOJO Stone Ocean Volume 1', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 25, '0000-00-00', 'stone_ocean_1.jgp'),
('11', 'JOJO Stone Ocean Volume 2', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 6, '0000-00-00', 'stone_ocean_2.jgp'),
('12', 'JOJO Stone Ocean Volume 3', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 27, '0000-00-00', 'stone_ocean_3.jgp'),
('13', 'Snow Country', 'Kawabata Yasunari', 'Knopf Doubleday Publishing Gro', 'Literature', 9.99, 2, '0000-00-00', 'snow_country.jpg');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `buys`
--

CREATE TABLE `buys` (
  `Transaction_ID` int(100) NOT NULL,
  `supplier_id` int(10) NOT NULL,
  `book_ISBN` varchar(12) NOT NULL,
  `quantity` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `customers`
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
-- Άδειασμα δεδομένων του πίνακα `customers`
--

INSERT INTO `customers` (`id`, `name`, `username`, `password`, `country`, `city`, `street`, `street_num`, `postal_code`, `phone`, `email`) VALUES
(1, 'phn', 'user', '123456789', 'greece', 'athens', 'phn', '51', '11242', '6985414123', 'phn@gmail.com');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `sells`
--

CREATE TABLE `sells` (
  `Transaction_ID` int(100) NOT NULL,
  `customer_id` int(10) NOT NULL,
  `book_ISBN` varchar(12) NOT NULL,
  `quantity` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `supplier`
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
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`ID`);

--
-- Ευρετήρια για πίνακα `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`ISBN`);

--
-- Ευρετήρια για πίνακα `buys`
--
ALTER TABLE `buys`
  ADD PRIMARY KEY (`Transaction_ID`),
  ADD KEY `book_ISBN` (`book_ISBN`),
  ADD KEY `supplier_id` (`supplier_id`);

--
-- Ευρετήρια για πίνακα `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Ευρετήρια για πίνακα `sells`
--
ALTER TABLE `sells`
  ADD PRIMARY KEY (`Transaction_ID`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `book_ISBN` (`book_ISBN`) USING BTREE;

--
-- Ευρετήρια για πίνακα `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT για άχρηστους πίνακες
--

--
-- AUTO_INCREMENT για πίνακα `admins`
--
ALTER TABLE `admins`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT για πίνακα `buys`
--
ALTER TABLE `buys`
  MODIFY `Transaction_ID` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT για πίνακα `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT για πίνακα `sells`
--
ALTER TABLE `sells`
  MODIFY `Transaction_ID` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT για πίνακα `supplier`
--
ALTER TABLE `supplier`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- Περιορισμοί για άχρηστους πίνακες
--

--
-- Περιορισμοί για πίνακα `buys`
--
ALTER TABLE `buys`
  ADD CONSTRAINT `buys_ibfk_1` FOREIGN KEY (`book_ISBN`) REFERENCES `books` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `buys_ibfk_3` FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Περιορισμοί για πίνακα `sells`
--
ALTER TABLE `sells`
  ADD CONSTRAINT `sells_ibfk_2` FOREIGN KEY (`book_ISBN`) REFERENCES `books` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sells_ibfk_3` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
