-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Εξυπηρετητής: 127.0.0.1
-- Χρόνος δημιουργίας: 01 Ιουν 2024 στις 23:30:06
-- Έκδοση διακομιστή: 10.4.32-MariaDB
-- Έκδοση PHP: 8.2.12

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
  `cover` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Άδειασμα δεδομένων του πίνακα `books`
--

INSERT INTO `books` (`ISBN`, `title`, `author`, `publisher`, `genre`, `price`, `cover`) VALUES
('01', 'Kafka on the Shore', 'Murakami Haruki', 'Vintage Books', 'Literature', 12.99, 0x6b61666b615f6f6e5f7468655f73686f72652e6a7067),
('02', '1Q84 Books 1 and 2', 'Murakami Haruki', 'Vintage Books', 'Literature', 13.99, 0x317138345f312e6a7067),
('03', '1Q84 Book 3', 'Murakami Haruki', 'Vintage Books', 'Literature', 13.99, 0x317138345f332e6a7067),
('04', 'Kokoro', 'Natsume Soseki', 'Vintage Books', 'Literature', 11.99, 0x6b6f6b6f726f2e6a7067),
('05', 'Nakahara Chuuya Poems', 'Nakahara Chuuya', 'Gracewing', 'Poems', 16.99, 0x6368757579615f706f656d732e6a7067),
('06', '100 poems, 100 authors', '-', 'Penguin Classics', 'Poems', 12.99, 0x706f656d732e6a7067),
('07', 'Goodnight Punpun Volume 1', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 0x70756e5f312e6a7067),
('08', 'Goodnight Punpun Volume 2', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 0x70756e5f322e6a7067),
('09', 'Goodnight Punpun Volume 3', 'Asano Inio', 'VIZ Media LLC', 'Manga', 16.99, 0x70756e5f332e6a7067),
('10', 'JOJO Stone Ocean Volume 1', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 0x73746f6e655f6f6365616e5f312e6a6770),
('11', 'JOJO Stone Ocean Volume 2', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 0x73746f6e655f6f6365616e5f322e6a6770),
('12', 'JOJO Stone Ocean Volume 3', 'Araki Hirohiko', 'VIZ Media LLC', 'Manga', 12.99, 0x73746f6e655f6f6365616e5f332e6a6770),
('13', 'Snow Country', 'Kawabata Yasunari', 'Knopf Doubleday Publishing Gro', 'Literature', 9.99, 0x736e6f775f636f756e7472792e6a7067);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `buys`
--

CREATE TABLE `buys` (
  `Transaction_ID` int(100) NOT NULL,
  `store_id` int(10) NOT NULL,
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

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `inventory`
--

CREATE TABLE `inventory` (
  `Inventory_ID` int(255) NOT NULL,
  `book_ISBN` varchar(12) NOT NULL,
  `store_ID` int(10) NOT NULL,
  `quantity` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `sells`
--

CREATE TABLE `sells` (
  `Transaction_ID` int(100) NOT NULL,
  `store_id` int(10) NOT NULL,
  `customer_id` int(10) NOT NULL,
  `book_ISBN` varchar(12) NOT NULL,
  `quantity` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `store`
--

CREATE TABLE `store` (
  `id` int(10) NOT NULL,
  `address` varchar(150) NOT NULL
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
  ADD KEY `store_id` (`store_id`),
  ADD KEY `supplier_id` (`supplier_id`);

--
-- Ευρετήρια για πίνακα `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Ευρετήρια για πίνακα `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`Inventory_ID`),
  ADD KEY `book_ISBN` (`book_ISBN`),
  ADD KEY `store_ID` (`store_ID`);

--
-- Ευρετήρια για πίνακα `sells`
--
ALTER TABLE `sells`
  ADD PRIMARY KEY (`Transaction_ID`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `book_ISBN` (`book_ISBN`) USING BTREE,
  ADD KEY `store_id` (`store_id`);

--
-- Ευρετήρια για πίνακα `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT για πίνακα `inventory`
--
ALTER TABLE `inventory`
  MODIFY `Inventory_ID` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT για πίνακα `sells`
--
ALTER TABLE `sells`
  MODIFY `Transaction_ID` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT για πίνακα `store`
--
ALTER TABLE `store`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

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
  ADD CONSTRAINT `buys_ibfk_2` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `buys_ibfk_3` FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Περιορισμοί για πίνακα `inventory`
--
ALTER TABLE `inventory`
  ADD CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`book_ISBN`) REFERENCES `books` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`store_ID`) REFERENCES `store` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Περιορισμοί για πίνακα `sells`
--
ALTER TABLE `sells`
  ADD CONSTRAINT `sells_ibfk_2` FOREIGN KEY (`book_ISBN`) REFERENCES `books` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sells_ibfk_3` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sells_ibfk_4` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
