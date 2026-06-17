-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 17, 2026 at 05:20 AM
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
-- Database: `sql12830722`
--

-- --------------------------------------------------------

--
-- Table structure for table `menu_items`
--

CREATE TABLE `menu_items` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `category` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `status` enum('active','inactive') DEFAULT 'active',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `menu_items`
--

INSERT INTO `menu_items` (`id`, `name`, `category`, `description`, `price`, `image`, `status`, `created_at`) VALUES
(1, 'Espresso', 'Coffee', 'Strong espresso shot', 120.00, NULL, 'active', '2026-06-16 08:44:17'),
(2, 'Latte', 'Coffee', 'Milk coffee', 180.00, NULL, 'active', '2026-06-16 08:44:17'),
(3, 'Cappuccino', 'Coffee', 'Italian style coffee', 190.00, NULL, 'active', '2026-06-16 08:44:17'),
(4, 'Americano', 'Coffee', 'Black coffee', 150.00, NULL, 'active', '2026-06-16 08:44:17'),
(5, 'Veg Sandwich', 'Food', 'Fresh vegetable sandwich', 220.00, NULL, 'active', '2026-06-16 08:44:17'),
(6, 'Paneer Sandwich', 'Food', 'Grilled paneer sandwich', 250.00, NULL, 'active', '2026-06-16 08:44:17'),
(7, 'French Fries', 'Snacks', 'Crispy fries', 180.00, NULL, 'active', '2026-06-16 08:44:17'),
(8, 'Chocolate Cake', 'Dessert', 'Chocolate pastry', 200.00, NULL, 'active', '2026-06-16 08:44:17'),
(9, 'Brownie', 'Dessert', 'Hot brownie', 220.00, NULL, 'active', '2026-06-16 08:44:17'),
(10, 'Cold Coffee', 'Beverages', 'Chilled coffee', 210.00, NULL, 'active', '2026-06-16 08:44:17');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `order_no` varchar(50) NOT NULL,
  `table_id` int(11) NOT NULL,
  `status` enum('pending','preparing','ready','paid','cancelled') DEFAULT 'pending',
  `total_amount` decimal(10,2) DEFAULT 0.00,
  `remarks` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

-- INSERT INTO `orders` (`id`, `order_no`, `table_id`, `status`, `total_amount`, `remarks`, `created_at`, `updated_at`) VALUES
-- (1, 'ORD-20260616151029', 5, 'paid', 1470.00, NULL, '2026-06-16 09:40:29', '2026-06-16 11:09:38'),
-- (2, 'ORD-20260616163857', 6, 'paid', 550.00, NULL, '2026-06-16 11:08:57', '2026-06-16 11:14:06'),
-- (3, 'ORD-20260616182525', 6, 'paid', 360.00, NULL, '2026-06-16 12:55:25', '2026-06-16 12:55:47'),
-- (4, 'ORD-20260616182657', 9, 'preparing', 1410.00, NULL, '2026-06-16 12:56:57', '2026-06-16 13:14:40');

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `menu_item_id` int(11) NOT NULL,
  `item_name` varchar(255) DEFAULT NULL,
  `quantity` int(11) DEFAULT 1,
  `unit_price` decimal(10,2) DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_items`
--

-- INSERT INTO `order_items` (`id`, `order_id`, `menu_item_id`, `item_name`, `quantity`, `unit_price`, `total_price`, `created_at`) VALUES
-- (1, 1, 1, 'Espresso', 2, 120.00, 240.00, '2026-06-16 09:40:29'),
-- (2, 1, 2, 'Latte', 1, 180.00, 180.00, '2026-06-16 09:40:29'),
-- (3, 1, 10, 'Cold Coffee', 1, 210.00, 210.00, '2026-06-16 11:04:33'),
-- (4, 1, 3, 'Cappuccino', 1, 190.00, 190.00, '2026-06-16 11:04:33'),
-- (5, 1, 6, 'Paneer Sandwich', 1, 250.00, 250.00, '2026-06-16 11:04:34'),
-- (6, 1, 5, 'Veg Sandwich', 1, 220.00, 220.00, '2026-06-16 11:04:34'),
-- (7, 1, 7, 'French Fries', 1, 180.00, 180.00, '2026-06-16 11:04:34'),
-- (8, 2, 10, 'Cold Coffee', 1, 210.00, 210.00, '2026-06-16 11:08:57'),
-- (9, 2, 4, 'Americano', 1, 150.00, 150.00, '2026-06-16 11:08:57'),
-- (10, 2, 3, 'Cappuccino', 1, 190.00, 190.00, '2026-06-16 11:08:57'),
-- (11, 3, 10, 'Cold Coffee', 1, 210.00, 210.00, '2026-06-16 12:55:25'),
-- (12, 3, 4, 'Americano', 1, 150.00, 150.00, '2026-06-16 12:55:25'),
-- (14, 4, 4, 'Americano', 1, 150.00, 150.00, '2026-06-16 12:56:57'),
-- (15, 4, 7, 'French Fries', 1, 180.00, 180.00, '2026-06-16 12:58:46'),
-- (16, 4, 5, 'Veg Sandwich', 1, 220.00, 220.00, '2026-06-16 12:58:46'),
-- (17, 4, 9, 'Brownie', 1, 220.00, 220.00, '2026-06-16 13:11:03'),
-- (18, 4, 9, 'Brownie', 1, 220.00, 220.00, '2026-06-16 13:11:11'),
-- (19, 4, 10, 'Cold Coffee', 2, 210.00, 420.00, '2026-06-16 13:14:14');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_method` enum('cash','upi','card') DEFAULT NULL,
  `payment_status` enum('pending','paid') DEFAULT 'pending',
  `transaction_ref` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payments`
--

-- INSERT INTO `payments` (`id`, `order_id`, `amount`, `payment_method`, `payment_status`, `transaction_ref`, `created_at`) VALUES
-- (1, 1, 420.00, 'cash', 'paid', NULL, '2026-06-16 10:33:44'),
-- (2, 1, 1470.00, 'cash', 'paid', NULL, '2026-06-16 11:09:38'),
-- (3, 2, 550.00, 'cash', 'paid', NULL, '2026-06-16 11:14:06'),
-- (4, 3, 360.00, 'cash', 'paid', NULL, '2026-06-16 12:55:47');

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_tables`
--

CREATE TABLE `restaurant_tables` (
  `id` int(11) NOT NULL,
  `table_no` int(11) NOT NULL,
  `verification_code` varchar(10) NOT NULL,
  `status` enum('open','reserved') DEFAULT 'open',
  `active_order_id` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `restaurant_tables`
--

INSERT INTO `restaurant_tables` (`id`, `table_no`, `verification_code`, `status`, `active_order_id`, `created_at`) VALUES
(1, 1, 'T1A2', 'open', NULL, '2026-06-16 08:44:17'),
(2, 2, 'T2B7', 'open', NULL, '2026-06-16 08:44:17'),
(3, 3, 'T3C8', 'open', NULL, '2026-06-16 08:44:17'),
(4, 4, 'T4D9', 'open', NULL, '2026-06-16 08:44:17'),
(5, 5, 'T5E3', 'open', NULL, '2026-06-16 08:44:17'),
(6, 6, 'T6F4', 'open', NULL, '2026-06-16 08:44:17'),
(7, 7, 'T7G5', 'open', NULL, '2026-06-16 08:44:17'),
(8, 8, 'T8H6', 'open', NULL, '2026-06-16 08:44:17'),
(9, 9, 'T9J7', 'open', NULL, '2026-06-16 08:44:17'),
(10, 10, 'T10K8', 'open', NULL, '2026-06-16 08:44:17');

-- --------------------------------------------------------

--
-- Table structure for table `table_sessions`
--

CREATE TABLE `table_sessions` (
  `id` int(11) NOT NULL,
  `table_id` int(11) NOT NULL,
  `session_token` varchar(100) DEFAULT NULL,
  `verified` tinyint(1) DEFAULT 0,
  `started_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `expires_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `menu_items`
--
ALTER TABLE `menu_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `order_no` (`order_no`),
  ADD KEY `table_id` (`table_id`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `menu_item_id` (`menu_item_id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`);

--
-- Indexes for table `restaurant_tables`
--
ALTER TABLE `restaurant_tables`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `table_no` (`table_no`);

--
-- Indexes for table `table_sessions`
--
ALTER TABLE `table_sessions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `table_id` (`table_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `menu_items`
--
ALTER TABLE `menu_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `orders`
--
-- ALTER TABLE `orders`
--   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `order_items`
--
-- ALTER TABLE `order_items`
--   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `payments`
--
-- ALTER TABLE `payments`
--   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `restaurant_tables`
--
ALTER TABLE `restaurant_tables`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `table_sessions`
--
ALTER TABLE `table_sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`table_id`) REFERENCES `restaurant_tables` (`id`);

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  ADD CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`menu_item_id`) REFERENCES `menu_items` (`id`);

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

--
-- Constraints for table `table_sessions`
--
ALTER TABLE `table_sessions`
  ADD CONSTRAINT `table_sessions_ibfk_1` FOREIGN KEY (`table_id`) REFERENCES `restaurant_tables` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
