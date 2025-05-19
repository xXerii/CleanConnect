-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2025 at 11:23 AM
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
-- Database: `clean_connect`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories_services`
--

CREATE TABLE `categories_services` (
  `catsv_id` int(50) NOT NULL,
  `cat/sv_name` varchar(1000) DEFAULT NULL,
  `parentCat_id` int(50) DEFAULT NULL,
  `cat_desc` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories_services`
--

INSERT INTO `categories_services` (`catsv_id`, `cat/sv_name`, `parentCat_id`, `cat_desc`) VALUES
(1, 'Sofa Cleaning\r\n', NULL, 'Clean Sofa'),
(2, 'Mattress Cleaning\r\n', NULL, 'Test 12'),
(3, 'Aircon Servicing\r\n', NULL, 'TestDesc'),
(4, 'Deep Cleaning\r\n', NULL, 'TestUpdate'),
(5, 'Steam Cleaning\r\n', 1, NULL),
(6, 'Extraction\r\n', 1, NULL),
(7, 'Leather Cleaning\r\n', 1, NULL),
(8, 'Kitchen Deep Clean\r\n', 4, NULL),
(9, 'Bathroom Scrub Down\r\n', 4, NULL),
(10, 'Bedroom Deep Clean\r\n', 4, NULL),
(11, 'UV-C Cleaning\r\n', 2, NULL),
(12, 'Steam Cleaning', 2, NULL),
(13, 'Extraction\r\n', 2, NULL),
(14, 'Category_9218', NULL, 'This is a category about 49'),
(15, 'Category_7202', NULL, 'This is a category about 10'),
(16, 'Category_3875', NULL, 'This is a category about 60'),
(17, 'Category_8820', NULL, 'This is a category about 58'),
(18, 'Category_2703', NULL, 'This is a category about 60'),
(19, 'Category_1974', NULL, 'This is a category about 18'),
(20, 'Category_3189', NULL, 'This is a category about 4'),
(21, 'Category_2838', NULL, 'This is a category about 27'),
(22, 'Category_5216', NULL, 'This is a category about 78'),
(23, 'Category_3575', NULL, 'This is a category about 43'),
(29, 'Service_4888', 22, NULL),
(30, 'Service_9058', 2, NULL),
(31, 'Service_7625', 4, NULL),
(32, 'Service_6163', 22, NULL),
(33, 'Service_3977', 18, NULL),
(34, 'Service_8122', 2, NULL),
(35, 'Service_1515', 17, NULL),
(36, 'Service_4823', 23, NULL),
(37, 'Service_8583', 14, NULL),
(38, 'Service_0779', 14, NULL),
(39, 'Service_1442', 14, NULL),
(40, 'Service_8774', 4, NULL),
(41, 'Service_9461', 18, NULL),
(42, 'Service_2311', 3, NULL),
(43, 'Service_3364', 18, NULL),
(44, 'Service_4516', 18, NULL),
(45, 'Service_2335', 18, NULL),
(46, 'Service_2467', 15, NULL),
(47, 'Service_8542', 1, NULL),
(48, 'Service_2125', 20, NULL),
(49, 'Service_8644', 23, NULL),
(50, 'Service_0873', 23, NULL),
(51, 'Service_1202', 16, NULL),
(52, 'Service_2665', 22, NULL),
(53, 'Service_5668', 14, NULL),
(54, 'Service_7892', 21, NULL),
(55, 'Service_4403', 17, NULL),
(56, 'Service_4419', 21, NULL),
(57, 'Service_3498', 22, NULL),
(58, 'Service_1617', 16, NULL),
(59, 'Service_7793', 14, NULL),
(60, 'Service_5627', 14, NULL),
(61, 'Service_5709', 20, NULL),
(62, 'Service_2058', 4, NULL),
(63, 'Service_6459', 22, NULL),
(64, 'Service_1622', 19, NULL),
(65, 'Service_8636', 22, NULL),
(66, 'Service_4789', 15, NULL),
(67, 'Service_5599', 4, NULL),
(68, 'Service_4573', 2, NULL),
(69, 'Service_3606', 2, NULL),
(70, 'Service_6542', 4, NULL),
(71, 'Service_2519', 17, NULL),
(72, 'Service_7539', 19, NULL),
(73, 'Service_3410', 17, NULL),
(74, 'Service_9125', 17, NULL),
(75, 'Service_3821', 3, NULL),
(76, 'Service_1196', 20, NULL),
(77, 'Service_1085', 21, NULL),
(78, 'Service_6366', 14, NULL),
(79, 'Service_1815', 22, NULL),
(80, 'Service_9880', 18, NULL),
(81, 'Service_8886', 16, NULL),
(82, 'Service_4587', 19, NULL),
(83, 'Service_5801', 15, NULL),
(84, 'Service_3948', 20, NULL),
(85, 'Service_5051', 17, NULL),
(86, 'Service_6654', 3, NULL),
(87, 'Service_4679', 1, NULL),
(88, 'Service_0446', 14, NULL),
(89, 'Service_0778', 14, NULL),
(90, 'Service_0441', 2, NULL),
(91, 'Service_8574', 19, NULL),
(92, 'Service_4136', 23, NULL),
(93, 'Service_6240', 1, NULL),
(94, 'Service_0391', 22, NULL),
(95, 'Service_8644', 15, NULL),
(96, 'Service_8029', 19, NULL),
(97, 'Service_6303', 17, NULL),
(98, 'Service_2180', 4, NULL),
(156, 'Service_6762', 19, NULL),
(157, 'Service_6826', 21, NULL),
(158, 'Service_3885', 16, NULL),
(159, 'ServiceAlpha', 23, NULL),
(160, 'ServiceOmega', 17, NULL),
(161, 'ServiceTheta', 15, NULL),
(162, 'SCP CONTAINMENT', 16, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cleaner_service`
--

CREATE TABLE `cleaner_service` (
  `clean_svc_id` int(50) NOT NULL,
  `cleaner_id` int(50) DEFAULT NULL,
  `category_id` int(50) DEFAULT NULL,
  `service_id` int(50) DEFAULT NULL,
  `price` varchar(500) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cleaner_service`
--

INSERT INTO `cleaner_service` (`clean_svc_id`, `cleaner_id`, `category_id`, `service_id`, `price`, `description`) VALUES
(1, 6, 4, 10, '9999.0', 'Includes windows as well!'),
(3, 34, 16, 158, '65.14', 'Auto-gen service for Service_3885'),
(7, 6, 18, 44, '13.02', 'Auto-gen service for Service_4516'),
(10, 81, 22, 63, '73.9', 'Auto-gen service for Service_6459'),
(11, 31, 22, 32, '15.33', 'Auto-gen service for Service_6163'),
(15, 34, 4, 62, '22.24', 'Auto-gen service for Service_2058'),
(17, 10, 4, 10, '120.0', 'Auto-gen service for Bedroom Deep Clean'),
(19, 36, 14, 60, '15.27', 'Auto-gen service for Service_5627'),
(32, 79, 4, 98, '77.99', 'Auto-gen service for Service_2180'),
(34, 84, 19, 72, '97.75', 'Auto-gen service for Service_7539'),
(36, 6, 17, 73, '6.22', 'Auto-gen service for Service_3410'),
(43, 11, 18, 45, '1.45', 'Auto-gen service for Service_2335'),
(44, 34, 2, 30, '12.52', 'Auto-gen service for Service_9058'),
(46, 82, 3, 42, '45.77', 'Auto-gen service for Service_2311'),
(49, 63, 2, 34, '46.09', 'Auto-gen service for Service_8122'),
(50, 46, 1, 5, '53.59', 'Auto-gen service for Steam Cleaning\r\n'),
(54, 81, 4, 31, '10.67', 'Auto-gen service for Service_7625'),
(57, 11, 15, 95, '54.33', 'Auto-gen service for Service_8644'),
(58, 67, 22, 79, '32.06', 'Auto-gen service for Service_1815'),
(60, 82, 21, 56, '99.19', 'Auto-gen service for Service_4419'),
(62, 79, 14, 89, '74.92', 'Auto-gen service for Service_0778'),
(64, 79, 15, 46, '64.42', 'Auto-gen service for Service_2467'),
(65, 82, 2, 11, '76.96', 'Auto-gen service for UV-C Cleaning\r\n'),
(66, 81, 19, 91, '66.19', 'Auto-gen service for Service_8574'),
(73, 79, 18, 33, '38.25', 'Auto-gen service for Service_3977'),
(74, 35, 1, 47, '14.82', 'Auto-gen service for Service_8542'),
(129, 10, 18, 33, '44.08', 'Auto-gen service for Service_3977'),
(131, 82, 3, 86, '93.49', 'Auto-gen service for Service_6654'),
(136, 92, 1, 7, '12.69', 'Auto-gen service for Leather Cleaning\r\n'),
(137, 42, 19, 64, '58.85', 'Auto-gen service for Service_1622'),
(140, 31, 22, 32, '98.79', 'Auto-gen service for Service_6163'),
(148, 6, 22, 63, '46.35', 'Auto-gen service for Service_6459'),
(153, 19, 1, 5, '93.83', 'Auto-gen service for Steam Cleaning\r\n'),
(156, 35, 4, 70, '70.95', 'Auto-gen service for Service_6542'),
(158, 84, 4, 67, '5.76', 'Auto-gen service for Service_5599'),
(161, 79, 16, 162, '70.67', 'Auto-gen service for SCP CONTAINMENT'),
(162, 81, 23, 50, '78.86', 'Auto-gen service for Service_0873'),
(163, 6, 16, 81, '1.62', 'Auto-gen service for Service_8886'),
(168, 17, 19, 96, '44.71', 'Auto-gen service for Service_8029'),
(169, 31, 14, 39, '5.15', 'Auto-gen service for Service_1442'),
(171, 42, 17, 71, '55.32', 'Auto-gen service for Service_2519'),
(173, 31, 21, 77, '97.3', 'Auto-gen service for Service_1085'),
(179, 79, 14, 64, '343.66', 'Service includes option 9 and guarantee.'),
(180, 67, 21, 45, '287.65', 'Service includes option 2 and guarantee.'),
(181, 105, 4, 58, '450.83', 'Service includes option 8 and guarantee.'),
(182, 10, 1, 157, '433.08', 'Service includes option 7 and guarantee.'),
(183, 101, 18, 97, '355.09', 'Service includes option 9 and guarantee.'),
(184, 52, 20, 5, '173.81', 'Service includes option 2 and guarantee.'),
(185, 64, 20, 74, '78.5', 'Service includes option 6 and guarantee.'),
(186, 35, 23, 80, '313.04', 'Service includes option 4 and guarantee.'),
(187, 92, 22, 63, '113.35', 'Service includes option 7 and guarantee.'),
(188, 46, 2, 35, '369.36', 'Service includes option 8 and guarantee.'),
(189, 10, 17, 37, '237.86', 'Service includes option 1 and guarantee.'),
(190, 97, 18, 45, '182.85', 'Service includes option 3 and guarantee.'),
(191, 63, 21, 90, '346.28', 'Service includes option 7 and guarantee.'),
(192, 11, 17, 63, '210.96', 'Service includes option 6 and guarantee.'),
(193, 36, 20, 59, '58.29', 'Service includes option 3 and guarantee.'),
(194, 82, 16, 9, '211.26', 'Service includes option 5 and guarantee.'),
(195, 90, 18, 62, '285.03', 'Service includes option 10 and guarantee.'),
(196, 22, 18, 13, '129.24', 'Service includes option 1 and guarantee.'),
(197, 32, 22, 32, '241.5', 'Service includes option 3 and guarantee.'),
(198, 92, 23, 62, '266.45', 'Service includes option 9 and guarantee.'),
(199, 31, 18, 48, '489.89', 'Service includes option 1 and guarantee.'),
(200, 63, 14, 86, '179.81', 'Service includes option 8 and guarantee.'),
(201, 81, 23, 72, '376.32', 'Service includes option 7 and guarantee.'),
(202, 19, 4, 85, '89.28', 'Service includes option 3 and guarantee.'),
(203, 31, 21, 86, '64.99', 'Service includes option 10 and guarantee.'),
(204, 46, 15, 13, '76.49', 'Service includes option 7 and guarantee.'),
(205, 101, 20, 53, '103.15', 'Service includes option 5 and guarantee.'),
(206, 64, 1, 41, '348.52', 'Service includes option 4 and guarantee.'),
(207, 92, 15, 90, '190.92', 'Service includes option 8 and guarantee.'),
(208, 92, 17, 60, '354.04', 'Service includes option 8 and guarantee.'),
(209, 10, 19, 40, '425.71', 'Service includes option 1 and guarantee.'),
(210, 101, 3, 58, '323.84', 'Service includes option 3 and guarantee.'),
(211, 19, 15, 52, '52.54', 'Service includes option 5 and guarantee.'),
(212, 81, 20, 56, '96.58', 'Service includes option 7 and guarantee.'),
(213, 92, 23, 162, '302.74', 'Service includes option 4 and guarantee.'),
(214, 84, 17, 50, '262.52', 'Service includes option 7 and guarantee.'),
(215, 81, 23, 80, '297.24', 'Service includes option 4 and guarantee.'),
(216, 99, 1, 79, '399.4', 'Service includes option 6 and guarantee.'),
(217, 36, 1, 57, '102.59', 'Service includes option 8 and guarantee.'),
(218, 99, 16, 62, '416.22', 'Service includes option 10 and guarantee.'),
(219, 79, 20, 60, '475.66', 'Service includes option 8 and guarantee.'),
(220, 92, 16, 64, '265.27', 'Service includes option 6 and guarantee.'),
(221, 11, 19, 68, '261.9', 'Service includes option 5 and guarantee.'),
(222, 10, 23, 50, '171.56', 'Service includes option 10 and guarantee.'),
(223, 97, 23, 53, '375.93', 'Service includes option 4 and guarantee.'),
(224, 82, 2, 6, '286.98', 'Service includes option 2 and guarantee.'),
(225, 32, 18, 74, '156.22', 'Service includes option 9 and guarantee.'),
(226, 90, 18, 8, '414.78', 'Service includes option 1 and guarantee.'),
(227, 46, 17, 70, '114.55', 'Service includes option 7 and guarantee.'),
(228, 79, 1, 34, '406.1', 'Service includes option 1 and guarantee.'),
(229, 82, 4, 92, '285.9', 'Service includes option 1 and guarantee.'),
(230, 63, 2, 78, '406.56', 'Service includes option 5 and guarantee.'),
(231, 90, 15, 66, '165.42', 'Service includes option 6 and guarantee.'),
(232, 42, 16, 55, '169.88', 'Service includes option 4 and guarantee.'),
(233, 31, 20, 31, '408.63', 'Service includes option 7 and guarantee.'),
(234, 84, 21, 156, '352.89', 'Service includes option 8 and guarantee.'),
(235, 36, 16, 162, '216.57', 'Service includes option 9 and guarantee.'),
(236, 52, 4, 93, '249.78', 'Service includes option 8 and guarantee.'),
(237, 46, 23, 46, '128.4', 'Service includes option 10 and guarantee.'),
(238, 64, 17, 41, '80.47', 'Service includes option 9 and guarantee.'),
(239, 99, 20, 46, '294.84', 'Service includes option 1 and guarantee.'),
(240, 35, 15, 64, '220.43', 'Service includes option 1 and guarantee.'),
(241, 36, 16, 59, '426.49', 'Service includes option 6 and guarantee.'),
(242, 64, 22, 5, '491.99', 'Service includes option 8 and guarantee.'),
(243, 90, 1, 79, '395.78', 'Service includes option 7 and guarantee.'),
(244, 32, 15, 9, '342.76', 'Service includes option 7 and guarantee.'),
(245, 31, 1, 98, '131.3', 'Service includes option 7 and guarantee.'),
(246, 79, 3, 76, '193.8', 'Service includes option 10 and guarantee.'),
(247, 90, 17, 159, '329.49', 'Service includes option 1 and guarantee.'),
(248, 22, 15, 162, '152.06', 'Service includes option 1 and guarantee.');

-- --------------------------------------------------------

--
-- Table structure for table `job_history`
--

CREATE TABLE `job_history` (
  `cleaner_id` int(8) NOT NULL,
  `booked_by` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `total_charged` varchar(500) NOT NULL,
  `booked_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `job_history`
--

INSERT INTO `job_history` (`cleaner_id`, `booked_by`, `category_id`, `service_id`, `total_charged`, `booked_at`) VALUES
(11, 24, 18, 45, '1.45', '2025-01-17'),
(63, 41, 2, 34, '46.09', '2025-02-14'),
(81, 103, 22, 63, '73.9', '2025-04-04'),
(79, 107, 18, 33, '38.25', '2025-04-13'),
(67, 86, 22, 79, '32.06', '2025-03-04'),
(6, 33, 4, 10, '9999.0', '2025-05-08'),
(46, 18, 1, 5, '53.59', '2025-03-16'),
(79, 86, 14, 89, '74.92', '2025-02-17'),
(10, 71, 4, 10, '120.0', '2025-02-28'),
(82, 27, 2, 11, '76.96', '2025-01-14'),
(82, 107, 3, 42, '45.77', '2025-03-16'),
(81, 86, 19, 91, '66.19', '2025-05-17'),
(6, 58, 18, 44, '13.02', '2025-01-16'),
(81, 37, 4, 31, '10.67', '2025-04-06'),
(11, 49, 15, 95, '54.33', '2025-04-26'),
(31, 55, 22, 32, '15.33', '2025-03-18'),
(34, 27, 4, 62, '22.24', '2025-01-19'),
(35, 28, 1, 47, '14.82', '2025-05-15'),
(79, 27, 4, 98, '77.99', '2025-05-07'),
(34, 3, 16, 158, '65.14', '2025-01-21'),
(6, 80, 17, 73, '6.22', '2025-02-05'),
(36, 18, 14, 60, '15.27', '2025-03-01'),
(79, 47, 15, 46, '64.42', '2025-02-08'),
(84, 18, 19, 72, '97.75', '2025-03-28'),
(82, 47, 21, 56, '99.19', '2025-04-16'),
(34, 27, 2, 30, '12.52', '2025-05-06'),
(6, 7, 17, 73, '6.22', '2025-04-03'),
(81, 61, 19, 91, '66.19', '2025-01-21'),
(82, 49, 3, 42, '45.77', '2025-03-28'),
(81, 78, 4, 31, '10.67', '2025-02-11'),
(6, 71, 18, 44, '13.02', '2025-03-16'),
(82, 18, 21, 56, '99.19', '2025-05-05'),
(34, 27, 2, 30, '12.52', '2025-01-11'),
(34, 68, 16, 158, '65.14', '2025-04-09'),
(31, 80, 22, 32, '15.33', '2025-03-07'),
(34, 80, 4, 62, '22.24', '2025-03-01'),
(46, 7, 1, 5, '53.59', '2025-05-03'),
(79, 55, 15, 46, '64.42', '2025-03-08'),
(11, 94, 15, 95, '54.33', '2025-04-21'),
(11, 94, 18, 45, '1.45', '2025-03-27'),
(81, 80, 22, 63, '73.9', '2025-03-21'),
(67, 38, 22, 79, '32.06', '2025-02-10'),
(36, 33, 14, 60, '15.27', '2025-02-15'),
(82, 69, 2, 6, '286.98', '2025-04-27'),
(79, 37, 20, 60, '475.66', '2025-05-16'),
(101, 94, 20, 53, '103.15', '2025-05-08'),
(10, 58, 23, 50, '171.56', '2025-05-02'),
(99, 53, 20, 46, '294.84', '2025-05-16'),
(10, 28, 17, 37, '237.86', '2025-05-03'),
(97, 61, 23, 53, '375.93', '2025-04-28'),
(10, 23, 4, 10, '120.0', '2025-04-30'),
(31, 72, 1, 98, '131.3', '2025-05-14'),
(10, 86, 18, 33, '44.08', '2025-04-25'),
(19, 37, 4, 85, '89.28', '2025-04-26'),
(90, 7, 17, 159, '329.49', '2025-04-25'),
(46, 3, 23, 46, '128.4', '2025-05-13'),
(64, 2, 17, 41, '80.47', '2025-05-16'),
(79, 107, 18, 33, '38.25', '2025-05-15'),
(36, 93, 20, 59, '58.29', '2025-05-10'),
(31, 94, 22, 32, '15.33', '2025-05-03'),
(19, 94, 15, 52, '52.54', '2025-05-18'),
(22, 53, 15, 162, '152.06', '2025-05-02'),
(35, 24, 23, 80, '313.04', '2025-04-25'),
(79, 47, 1, 34, '406.1', '2025-04-28'),
(31, 28, 14, 39, '5.15', '2025-04-30'),
(81, 93, 20, 56, '96.58', '2025-05-16'),
(92, 93, 17, 60, '354.04', '2025-05-13'),
(11, 69, 17, 63, '210.96', '2025-04-28'),
(11, 68, 18, 45, '1.45', '2025-04-22'),
(31, 45, 20, 31, '408.63', '2025-05-13'),
(52, 68, 4, 93, '249.78', '2025-05-12'),
(17, 27, 19, 96, '44.71', '2025-04-23'),
(36, 103, 16, 59, '426.49', '2025-05-05'),
(63, 33, 2, 34, '46.09', '2025-05-05'),
(22, 23, 18, 13, '129.24', '2025-04-29'),
(67, 49, 22, 79, '32.06', '2025-05-06'),
(42, 24, 19, 64, '58.85', '2025-04-29'),
(42, 23, 17, 71, '55.32', '2025-04-24'),
(79, 72, 14, 64, '343.66', '2025-05-07'),
(90, 72, 1, 79, '395.78', '2025-05-05'),
(105, 47, 4, 58, '450.83', '2025-04-20'),
(36, 107, 16, 162, '216.57', '2025-05-05'),
(64, 13, 1, 41, '348.52', '2025-05-17'),
(99, 49, 16, 62, '416.22', '2025-05-16'),
(34, 38, 16, 158, '65.14', '2025-05-14'),
(97, 78, 18, 45, '182.85', '2025-05-04'),
(42, 2, 16, 55, '169.88', '2025-05-05'),
(31, 33, 22, 32, '98.79', '2025-05-01'),
(46, 38, 1, 5, '53.59', '2025-04-26'),
(64, 3, 22, 5, '491.99', '2025-05-04'),
(52, 80, 20, 5, '173.81', '2025-05-15'),
(63, 3, 14, 86, '179.81', '2025-04-26'),
(92, 41, 16, 64, '265.27', '2025-05-03'),
(82, 18, 16, 9, '211.26', '2025-04-20'),
(32, 107, 18, 74, '156.22', '2025-04-26'),
(6, 93, 4, 10, '9999.0', '2025-05-05'),
(63, 33, 2, 78, '406.56', '2025-04-20'),
(82, 107, 3, 86, '93.49', '2025-05-18'),
(10, 93, 19, 40, '425.71', '2025-05-07'),
(6, 93, 16, 81, '1.62', '2025-05-07'),
(79, 37, 3, 76, '193.8', '2025-04-28'),
(82, 55, 2, 11, '76.96', '2025-05-07'),
(92, 72, 23, 162, '302.74', '2025-05-04'),
(35, 58, 15, 64, '220.43', '2025-05-12'),
(11, 27, 19, 68, '261.9', '2025-05-12'),
(64, 107, 20, 74, '78.5', '2025-05-08'),
(67, 69, 21, 45, '287.65', '2025-05-15'),
(82, 107, 3, 42, '45.77', '2025-05-06'),
(46, 49, 17, 70, '114.55', '2025-05-07'),
(81, 80, 23, 72, '376.32', '2025-04-27'),
(11, 69, 15, 95, '54.33', '2025-04-30'),
(6, 45, 17, 73, '6.22', '2025-04-22'),
(90, 103, 18, 62, '285.03', '2025-05-10'),
(92, 13, 15, 90, '190.92', '2025-05-17'),
(101, 80, 18, 97, '355.09', '2025-04-22'),
(84, 37, 17, 50, '262.52', '2025-05-10'),
(90, 13, 18, 8, '414.78', '2025-04-26'),
(63, 23, 21, 90, '346.28', '2025-05-15'),
(32, 23, 15, 9, '342.76', '2025-04-23'),
(6, 7, 22, 63, '46.35', '2025-04-22'),
(79, 68, 4, 98, '77.99', '2025-04-22'),
(35, 45, 4, 70, '70.95', '2025-05-16'),
(10, 33, 1, 157, '433.08', '2025-05-12');

-- --------------------------------------------------------

--
-- Table structure for table `profile_view`
--

CREATE TABLE `profile_view` (
  `view_id` int(11) NOT NULL,
  `cleaner_id` int(11) NOT NULL,
  `viewer_id` int(11) NOT NULL,
  `viewed_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `profile_view`
--

INSERT INTO `profile_view` (`view_id`, `cleaner_id`, `viewer_id`, `viewed_at`) VALUES
(1, 6, 7, '2025-04-29 20:31:33'),
(2, 10, 7, '2025-04-29 20:31:39'),
(3, 6, 7, '2025-05-02 17:08:04'),
(4, 10, 7, '2025-05-02 17:56:42'),
(5, 10, 7, '2025-05-02 17:57:37'),
(6, 10, 7, '2025-05-02 17:57:51'),
(7, 10, 7, '2025-05-02 17:57:52'),
(8, 6, 7, '2025-05-02 17:57:54'),
(9, 10, 7, '2025-05-02 17:58:01'),
(10, 10, 7, '2025-05-02 17:58:13'),
(11, 10, 7, '2025-05-02 18:03:42'),
(12, 6, 7, '2025-05-04 15:49:32'),
(13, 10, 7, '2025-05-04 15:49:35'),
(14, 6, 7, '2025-05-04 15:49:40'),
(15, 10, 7, '2025-05-14 13:50:17'),
(16, 6, 7, '2025-05-14 13:50:19'),
(17, 10, 7, '2025-05-14 13:50:21'),
(18, 10, 7, '2025-05-14 13:50:25'),
(19, 6, 7, '2025-05-14 13:50:26'),
(20, 10, 7, '2025-05-14 13:50:28'),
(21, 6, 7, '2025-05-16 19:13:38'),
(22, 6, 7, '2025-05-16 19:13:40'),
(23, 6, 7, '2025-05-16 19:13:42'),
(24, 6, 7, '2025-05-16 20:33:36'),
(25, 6, 7, '2025-05-17 14:48:23'),
(26, 6, 45, '2025-04-18 17:45:40'),
(27, 101, 27, '2025-05-07 17:45:40'),
(28, 64, 69, '2025-04-27 17:45:40'),
(29, 34, 61, '2025-05-13 17:45:40'),
(30, 106, 7, '2025-04-20 17:45:40'),
(31, 67, 78, '2025-04-21 17:45:40'),
(32, 84, 68, '2025-05-13 17:45:40'),
(33, 6, 49, '2025-04-27 17:45:40'),
(34, 67, 28, '2025-04-26 17:45:40'),
(35, 84, 53, '2025-05-01 17:45:40'),
(36, 11, 49, '2025-05-04 17:45:40'),
(37, 34, 28, '2025-05-05 17:45:40'),
(38, 64, 71, '2025-05-16 17:45:40'),
(39, 102, 49, '2025-04-23 17:45:40'),
(40, 106, 72, '2025-05-04 17:45:40'),
(41, 100, 47, '2025-04-24 17:45:40'),
(42, 25, 55, '2025-05-03 17:45:40'),
(43, 63, 13, '2025-04-21 17:45:40'),
(44, 35, 27, '2025-04-22 17:45:40'),
(45, 99, 107, '2025-04-19 17:45:40'),
(46, 82, 103, '2025-04-25 17:45:40'),
(47, 34, 72, '2025-04-23 17:45:40'),
(48, 79, 27, '2025-05-08 17:45:40'),
(49, 106, 3, '2025-04-21 17:45:40'),
(50, 105, 28, '2025-05-13 17:45:40'),
(51, 90, 72, '2025-04-23 17:45:40'),
(52, 11, 2, '2025-04-18 17:45:40'),
(53, 84, 107, '2025-05-11 17:45:40'),
(54, 46, 78, '2025-04-21 17:45:40'),
(55, 106, 27, '2025-05-06 17:45:40'),
(56, 84, 53, '2025-05-12 17:45:40'),
(57, 82, 33, '2025-04-23 17:45:40'),
(58, 22, 7, '2025-04-30 17:45:40'),
(59, 46, 24, '2025-04-21 17:45:40'),
(60, 99, 93, '2025-05-10 17:45:40'),
(61, 97, 80, '2025-05-13 17:45:40'),
(62, 6, 37, '2025-04-24 17:45:40'),
(63, 11, 49, '2025-05-05 17:45:40'),
(64, 84, 23, '2025-05-10 17:45:40'),
(65, 52, 28, '2025-04-20 17:45:40'),
(66, 81, 7, '2025-05-08 17:45:40'),
(67, 64, 69, '2025-05-11 17:45:40'),
(68, 11, 86, '2025-05-12 17:45:40'),
(69, 84, 55, '2025-04-26 17:45:40'),
(70, 11, 58, '2025-04-28 17:45:40'),
(71, 79, 13, '2025-04-19 17:45:40'),
(72, 42, 55, '2025-05-06 17:45:40'),
(73, 67, 41, '2025-05-05 17:45:40'),
(74, 36, 69, '2025-04-30 17:45:40'),
(75, 63, 93, '2025-05-05 17:45:40'),
(76, 90, 61, '2025-05-01 17:45:40'),
(77, 25, 37, '2025-05-09 17:45:40'),
(78, 79, 69, '2025-04-19 17:45:40'),
(79, 19, 37, '2025-04-29 17:45:40'),
(80, 97, 58, '2025-04-20 17:45:40'),
(81, 63, 45, '2025-05-14 17:45:40'),
(82, 105, 93, '2025-04-19 17:45:40'),
(83, 101, 93, '2025-05-05 17:45:40'),
(84, 26, 7, '2025-05-10 17:45:40'),
(85, 11, 107, '2025-05-12 17:45:40'),
(86, 82, 69, '2025-05-05 17:45:40'),
(87, 84, 24, '2025-05-13 17:45:40'),
(88, 92, 49, '2025-04-30 17:45:40'),
(89, 92, 3, '2025-05-08 17:45:40'),
(90, 19, 53, '2025-05-09 17:45:40'),
(91, 26, 23, '2025-04-22 17:45:40'),
(92, 25, 47, '2025-05-17 17:45:40'),
(93, 25, 93, '2025-05-15 17:45:40'),
(94, 99, 33, '2025-05-04 17:45:40'),
(95, 46, 41, '2025-04-29 17:45:40'),
(96, 102, 107, '2025-05-10 17:45:40'),
(97, 92, 80, '2025-05-17 17:45:40'),
(98, 32, 68, '2025-04-28 17:45:40'),
(99, 34, 41, '2025-04-30 17:45:40'),
(100, 11, 3, '2025-04-30 17:45:40'),
(101, 98, 2, '2025-05-19 16:48:49'),
(102, 87, 2, '2025-05-19 16:49:06'),
(103, 68, 2, '2025-05-19 16:49:37'),
(104, 10, 7, '2025-05-19 16:53:18'),
(105, 82, 7, '2025-05-19 16:53:35'),
(106, 82, 7, '2025-05-19 16:53:38'),
(107, 98, 7, '2025-05-19 16:53:43'),
(108, 82, 7, '2025-05-19 16:56:49'),
(109, 82, 7, '2025-05-19 16:57:06'),
(110, 98, 7, '2025-05-19 17:00:54'),
(111, 79, 2, '2025-05-19 17:22:23'),
(112, 82, 2, '2025-05-19 17:22:32'),
(113, 84, 111, '2025-05-19 17:22:49'),
(114, 81, 111, '2025-05-19 17:22:52');

-- --------------------------------------------------------

--
-- Table structure for table `shortlist`
--

CREATE TABLE `shortlist` (
  `short_id` int(11) NOT NULL,
  `cleaner_id` int(11) NOT NULL,
  `homeowner_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `clean_svc_id` int(11) NOT NULL,
  `shortlisted_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shortlist`
--

INSERT INTO `shortlist` (`short_id`, `cleaner_id`, `homeowner_id`, `category_id`, `service_id`, `clean_svc_id`, `shortlisted_at`) VALUES
(1, 6, 47, 4, 10, 1, '2025-05-17 17:41:22'),
(5, 6, 72, 18, 44, 7, '2025-05-28 00:00:00'),
(9, 81, 47, 19, 91, 66, '2025-01-23 00:00:00'),
(13, 34, 49, 16, 158, 3, '2025-01-07 00:00:00'),
(14, 82, 69, 2, 11, 65, '2025-03-24 00:00:00'),
(17, 46, 93, 1, 5, 50, '2025-02-24 00:00:00'),
(20, 10, 103, 4, 10, 17, '2025-03-06 00:00:00'),
(27, 36, 13, 14, 60, 19, '2025-03-29 00:00:00'),
(38, 34, 13, 16, 158, 3, '2025-04-12 00:00:00'),
(42, 46, 103, 1, 5, 50, '2025-05-14 00:00:00'),
(45, 46, 86, 1, 5, 50, '2025-04-18 00:00:00'),
(47, 11, 47, 15, 95, 57, '2025-05-05 00:00:00'),
(49, 63, 41, 2, 34, 49, '2025-02-14 00:00:00'),
(60, 67, 78, 22, 79, 58, '2025-03-11 00:00:00'),
(63, 84, 38, 19, 72, 34, '2025-04-20 00:00:00'),
(70, 82, 28, 2, 11, 65, '2025-01-18 00:00:00'),
(75, 11, 78, 15, 95, 57, '2025-03-05 00:00:00'),
(79, 81, 28, 22, 63, 10, '2025-01-09 00:00:00'),
(80, 84, 53, 19, 72, 34, '2025-04-09 00:00:00'),
(81, 34, 103, 16, 158, 3, '2025-02-08 00:00:00'),
(82, 46, 71, 1, 5, 50, '2025-05-08 00:00:00'),
(85, 82, 61, 3, 42, 46, '2025-05-17 00:00:00'),
(86, 79, 78, 15, 46, 64, '2025-02-25 00:00:00'),
(87, 36, 3, 14, 60, 19, '2025-05-04 00:00:00'),
(90, 36, 23, 14, 60, 19, '2025-03-17 00:00:00'),
(94, 11, 94, 15, 95, 57, '2025-01-21 00:00:00'),
(98, 82, 71, 21, 56, 60, '2025-02-21 00:00:00'),
(103, 82, 7, 3, 42, 46, '2025-05-19 16:57:02'),
(119, 81, 69, 19, 91, 66, '2025-05-11 17:21:27'),
(120, 46, 37, 2, 35, 188, '2025-05-11 17:21:27'),
(121, 82, 68, 16, 9, 194, '2025-05-07 17:21:27'),
(122, 79, 33, 14, 89, 62, '2025-05-09 17:21:27'),
(123, 84, 33, 21, 156, 234, '2025-05-17 17:21:27'),
(124, 11, 58, 15, 95, 57, '2025-05-10 17:21:27'),
(125, 22, 18, 15, 162, 248, '2025-05-08 17:21:27'),
(126, 90, 18, 17, 159, 247, '2025-05-18 17:21:27'),
(127, 19, 24, 15, 52, 211, '2025-05-15 17:21:27'),
(128, 79, 53, 1, 34, 228, '2025-05-08 17:21:27'),
(129, 84, 72, 17, 50, 214, '2025-05-13 17:21:27'),
(130, 52, 68, 4, 93, 236, '2025-05-08 17:21:27'),
(131, 32, 3, 15, 9, 244, '2025-05-17 17:21:27'),
(132, 82, 68, 3, 42, 46, '2025-05-14 17:21:27'),
(133, 82, 49, 4, 92, 229, '2025-05-12 17:21:27'),
(134, 6, 38, 4, 10, 1, '2025-05-09 17:21:27'),
(135, 63, 47, 2, 78, 230, '2025-05-11 17:21:27'),
(136, 10, 13, 1, 157, 182, '2025-05-15 17:21:27'),
(137, 97, 86, 18, 45, 190, '2025-05-17 17:21:27'),
(138, 46, 69, 17, 70, 227, '2025-05-17 17:21:27'),
(139, 36, 23, 1, 57, 217, '2025-05-06 17:21:27'),
(140, 79, 61, 4, 98, 32, '2025-05-09 17:21:27'),
(141, 11, 45, 17, 63, 192, '2025-05-16 17:21:27'),
(142, 10, 53, 4, 10, 17, '2025-05-12 17:21:27'),
(143, 82, 58, 2, 6, 224, '2025-05-06 17:21:27'),
(144, 36, 24, 20, 59, 193, '2025-05-14 17:21:27'),
(145, 92, 61, 16, 64, 220, '2025-05-19 17:21:27'),
(146, 67, 72, 22, 79, 58, '2025-05-18 17:21:27'),
(147, 90, 80, 18, 8, 226, '2025-05-09 17:21:27'),
(148, 79, 41, 14, 64, 179, '2025-05-13 17:21:27'),
(149, 35, 23, 15, 64, 240, '2025-05-13 17:21:27'),
(150, 79, 107, 18, 33, 73, '2025-05-12 17:21:27'),
(151, 101, 94, 3, 58, 210, '2025-05-19 17:21:27'),
(152, 99, 33, 20, 46, 239, '2025-05-10 17:21:27'),
(153, 79, 72, 3, 76, 246, '2025-05-09 17:21:27'),
(154, 10, 107, 17, 37, 189, '2025-05-08 17:21:27'),
(155, 36, 23, 16, 162, 235, '2025-05-08 17:21:27'),
(156, 31, 49, 21, 86, 203, '2025-05-14 17:21:27'),
(157, 32, 61, 22, 32, 197, '2025-05-17 17:21:27'),
(158, 81, 78, 22, 63, 10, '2025-05-14 17:21:27'),
(159, 19, 18, 1, 5, 153, '2025-05-18 17:21:27'),
(160, 82, 107, 3, 86, 131, '2025-05-12 17:21:27'),
(161, 92, 107, 23, 62, 198, '2025-05-13 17:21:27'),
(162, 81, 55, 23, 72, 201, '2025-05-19 17:21:27'),
(163, 32, 27, 18, 74, 225, '2025-05-14 17:21:27'),
(164, 52, 38, 20, 5, 184, '2025-05-11 17:21:27'),
(165, 92, 103, 23, 162, 213, '2025-05-13 17:21:27'),
(166, 31, 53, 14, 39, 169, '2025-05-12 17:21:27'),
(167, 63, 7, 2, 34, 49, '2025-05-08 17:21:27'),
(168, 19, 37, 4, 85, 202, '2025-05-16 17:21:27'),
(182, 79, 2, 4, 98, 32, '2025-05-12 17:22:06'),
(183, 31, 86, 1, 98, 245, '2025-05-10 17:22:06'),
(184, 36, 71, 1, 57, 217, '2025-05-11 17:22:06'),
(185, 32, 58, 15, 9, 244, '2025-05-19 17:22:06'),
(186, 10, 3, 23, 50, 222, '2025-05-07 17:22:06'),
(187, 32, 94, 18, 74, 225, '2025-05-13 17:22:06'),
(188, 63, 93, 21, 90, 191, '2025-05-09 17:22:06'),
(189, 17, 13, 19, 96, 168, '2025-05-15 17:22:06'),
(190, 90, 38, 15, 66, 231, '2025-05-19 17:22:06'),
(191, 36, 80, 16, 162, 235, '2025-05-19 17:22:06'),
(192, 79, 49, 14, 89, 62, '2025-05-12 17:22:06'),
(193, 19, 69, 15, 52, 211, '2025-05-14 17:22:06'),
(194, 82, 27, 2, 6, 224, '2025-05-19 17:22:06'),
(195, 105, 68, 4, 58, 181, '2025-05-10 17:22:06'),
(196, 31, 103, 21, 86, 203, '2025-05-19 17:22:06'),
(197, 6, 37, 18, 44, 7, '2025-05-08 17:22:06'),
(198, 31, 13, 18, 48, 199, '2025-05-18 17:22:06'),
(199, 52, 78, 4, 93, 236, '2025-05-08 17:22:06'),
(200, 36, 86, 20, 59, 193, '2025-05-14 17:22:06'),
(201, 64, 103, 1, 41, 206, '2025-05-07 17:22:06'),
(202, 82, 33, 21, 56, 60, '2025-05-17 17:22:06'),
(203, 97, 41, 18, 45, 190, '2025-05-15 17:22:06'),
(204, 64, 69, 22, 5, 242, '2025-05-08 17:22:06'),
(205, 46, 55, 17, 70, 227, '2025-05-10 17:22:06'),
(206, 19, 72, 1, 5, 153, '2025-05-18 17:22:06'),
(207, 31, 72, 22, 32, 140, '2025-05-11 17:22:06'),
(208, 79, 37, 1, 34, 228, '2025-05-19 17:22:06'),
(209, 22, 103, 18, 13, 196, '2025-05-08 17:22:06'),
(210, 90, 58, 17, 159, 247, '2025-05-17 17:22:06'),
(211, 63, 13, 2, 34, 49, '2025-05-12 17:22:06');

-- --------------------------------------------------------

--
-- Table structure for table `useraccounts`
--

CREATE TABLE `useraccounts` (
  `user_id` int(11) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role_id` int(50) DEFAULT NULL,
  `suspended` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `useraccounts`
--

INSERT INTO `useraccounts` (`user_id`, `name`, `username`, `email`, `password`, `role_id`, `suspended`) VALUES
(1, 'Ryz', 'admin1', 'test@email.com', '12345', 1, 0),
(2, 'janjan', 'janjan', 'jan@test.com', '12345', 3, 0),
(3, 'alex', 'alex123', 'alex@test.com', 'abcde', 3, 0),
(4, 'maria', 'maria456', 'maria@test.com', 'pass456', 1, 0),
(6, 'Hojlund', 'cleaner1', 'quicksell@rubbish.com', '12345', 2, 0),
(7, 'viviann', 'homeowner1', 'viv@gmail.com', '12345', 3, 0),
(8, 'Superman', 'platform1', 'totallynotclark@dailyplanet.com', '12345', 4, 0),
(9, 'Afiq', 'admin2', 'test@email.com', '123456', 1, 0),
(10, 'Ryzlan', 'xxerii', 'xxerii@email.com', '54321', 2, 0),
(11, 'name9178', 'user48372', 'user66511@example.com', '87437', 2, 0),
(12, 'name1683', 'user06292', 'user80958@example.com', '85915', 4, 1),
(13, 'name1874', 'user66432', 'user75911@example.com', '80262', 3, 0),
(14, 'name1475', 'user92497', 'user18212@example.com', '13569', 1, 0),
(15, 'name8707', 'user59345', 'user35506@example.com', '99498', 4, 1),
(16, 'name0891', 'user75464', 'user50586@example.com', '26537', 4, 0),
(17, 'name8234', 'user36641', 'user36176@example.com', '70957', 2, 0),
(18, 'name5330', 'user11277', 'user96473@example.com', '48534', 3, 0),
(19, 'name4355', 'user55786', 'user48268@example.com', '73981', 2, 0),
(20, 'name4252', 'user01921', 'user82034@example.com', '04409', 4, 1),
(21, 'name0457', 'user23442', 'user3483@example.com', '47088', 1, 1),
(22, 'name4352', 'user66524', 'user2044@example.com', '10649', 2, 0),
(23, 'name7673', 'user72836', 'user33975@example.com', '51365', 3, 0),
(24, 'name3736', 'user25590', 'user15851@example.com', '02484', 3, 0),
(25, 'name8986', 'user98661', 'user23699@example.com', '22512', 2, 0),
(26, 'name7452', 'user53287', 'user42853@example.com', '54404', 2, 1),
(27, 'name4007', 'user38087', 'user70220@example.com', '36842', 3, 1),
(28, 'name6548', 'user55720', 'user82164@example.com', '43657', 3, 0),
(29, 'name2464', 'user39218', 'user22146@example.com', '93078', 4, 0),
(30, 'name8076', 'user57250', 'user43960@example.com', '48048', 1, 1),
(31, 'name6324', 'user23232', 'user26421@example.com', '62412', 2, 1),
(32, 'name8537', 'user96614', 'user26944@example.com', '44880', 2, 1),
(33, 'name8526', 'user76750', 'user27953@example.com', '09516', 3, 1),
(34, 'name5916', 'user25617', 'user50598@example.com', '76138', 2, 0),
(35, 'name9369', 'user20258', 'user20194@example.com', '40198', 2, 1),
(36, 'name8596', 'user85507', 'user69647@example.com', '91716', 2, 1),
(37, 'name1630', 'user62399', 'user63075@example.com', '28181', 3, 1),
(38, 'name1421', 'user49543', 'user5059@example.com', '76668', 3, 0),
(39, 'name4957', 'user15429', 'user28426@example.com', '95842', 4, 1),
(40, 'name2892', 'user98170', 'user4087@example.com', '25926', 1, 0),
(41, 'name9326', 'user39097', 'user15692@example.com', '61171', 3, 0),
(42, 'name7556', 'user46692', 'user6762@example.com', '93733', 2, 1),
(43, 'name5838', 'user09828', 'user73971@example.com', '40373', 4, 1),
(44, 'name5332', 'user30712', 'user93591@example.com', '75819', 4, 1),
(45, 'name2579', 'user36501', 'user5133@example.com', '16162', 3, 1),
(46, 'name9664', 'user47502', 'user47573@example.com', '95359', 2, 1),
(47, 'name1929', 'user43557', 'user59902@example.com', '68842', 3, 0),
(48, 'name8642', 'user84186', 'user61642@example.com', '55651', 4, 1),
(49, 'name1854', 'user93606', 'user12391@example.com', '81136', 3, 1),
(50, 'name9016', 'user53423', 'user96611@example.com', '22786', 1, 1),
(51, 'name8838', 'user85503', 'user62368@example.com', '55335', 4, 1),
(52, 'name4052', 'user57094', 'user63887@example.com', '48155', 2, 0),
(53, 'name5815', 'user87474', 'user62909@example.com', '52126', 3, 0),
(54, 'name9995', 'user90382', 'user52043@example.com', '89069', 4, 1),
(55, 'name2675', 'user97138', 'user5421@example.com', '35693', 3, 0),
(56, 'name3304', 'user53449', 'user68101@example.com', '80158', 4, 0),
(57, 'name2039', 'user76044', 'user19045@example.com', '67093', 4, 1),
(58, 'name1689', 'user13361', 'user16108@example.com', '40455', 3, 0),
(59, 'name8016', 'user55598', 'user37502@example.com', '20718', 4, 1),
(60, 'name9306', 'user85531', 'user48465@example.com', '85734', 4, 1),
(61, 'name4603', 'user52677', 'user25268@example.com', '68309', 3, 0),
(62, 'name2172', 'user37257', 'user21107@example.com', '93763', 1, 0),
(63, 'name1445', 'user33713', 'user25198@example.com', '24852', 2, 1),
(64, 'name9792', 'user83278', 'user22610@example.com', '63216', 2, 1),
(65, 'name1322', 'user11347', 'user17058@example.com', '51249', 1, 1),
(66, 'name4286', 'user99468', 'user68749@example.com', '45345', 1, 1),
(67, 'name7029', 'user52443', 'user51329@example.com', '99319', 2, 0),
(68, 'name4758', 'user92662', 'user20568@example.com', '24856', 3, 0),
(69, 'name0383', 'user04248', 'user9730@example.com', '35904', 3, 0),
(70, 'name6873', 'user11824', 'user52927@example.com', '29160', 4, 0),
(71, 'name7710', 'user42628', 'user81819@example.com', '81213', 3, 1),
(72, 'name1516', 'user97624', 'user42632@example.com', '20290', 3, 0),
(73, 'name1379', 'user48320', 'user206@example.com', '56068', 4, 0),
(74, 'name1293', 'user73405', 'user28223@example.com', '20901', 1, 0),
(75, 'name2292', 'user05173', 'user57081@example.com', '69889', 4, 1),
(76, 'name7208', 'user16398', 'user65747@example.com', '79542', 1, 1),
(77, 'name1722', 'user94951', 'user23075@example.com', '30523', 4, 0),
(78, 'name7675', 'user07638', 'user7912@example.com', '16648', 3, 0),
(79, 'name5939', 'user54214', 'user92897@example.com', '01844', 2, 0),
(80, 'name4401', 'user78706', 'user61487@example.com', '71320', 3, 0),
(81, 'name1728', 'user46202', 'user79154@example.com', '57166', 2, 1),
(82, 'name0659', 'user21947', 'user89957@example.com', '83944', 2, 1),
(83, 'name3752', 'user95400', 'user64415@example.com', '35875', 4, 0),
(84, 'name5674', 'user14630', 'user2926@example.com', '70740', 2, 0),
(85, 'name2723', 'user98964', 'user13122@example.com', '68718', 1, 0),
(86, 'name6218', 'user65996', 'user43436@example.com', '19190', 3, 1),
(87, 'name5630', 'user69569', 'user78942@example.com', '86002', 4, 0),
(88, 'name6004', 'user76443', 'user2098@example.com', '81162', 4, 1),
(89, 'name7188', 'user97177', 'user70226@example.com', '59601', 4, 1),
(90, 'name2715', 'user62303', 'user30045@example.com', '63318', 2, 0),
(91, 'name3220', 'user34084', 'user73807@example.com', '66784', 1, 1),
(92, 'name7323', 'user79715', 'user78883@example.com', '55271', 2, 0),
(93, 'name4445', 'user24149', 'user87372@example.com', '64412', 3, 0),
(94, 'name5261', 'user43589', 'user60113@example.com', '69796', 3, 0),
(95, 'name6321', 'user14603', 'user83358@example.com', '72985', 1, 1),
(96, 'name3194', 'user93805', 'user73204@example.com', '84608', 1, 1),
(97, 'name0630', 'user41563', 'user88907@example.com', '19846', 2, 0),
(98, 'name1753', 'user78646', 'user40620@example.com', '67163', 1, 1),
(99, 'name9952', 'user92803', 'user65436@example.com', '48770', 2, 1),
(100, 'name1439', 'user97768', 'user45653@example.com', '34962', 2, 1),
(101, 'name0826', 'user88252', 'user16457@example.com', '17527', 2, 0),
(102, 'name7894', 'user78463', 'user55493@example.com', '42078', 2, 1),
(103, 'name3486', 'user94362', 'user67219@example.com', '53011', 3, 1),
(104, 'name9956', 'user23962', 'user21123@example.com', '33728', 1, 0),
(105, 'name1008', 'user74876', 'user44133@example.com', '96034', 2, 1),
(106, 'name1051', 'user00274', 'user69824@example.com', '48298', 2, 0),
(107, 'name7994', 'user54119', 'user30763@example.com', '91460', 3, 1),
(108, 'name5834', 'user39714', 'user23527@example.com', '98493', 1, 0),
(109, 'name0402', 'user78325', 'user79551@example.com', '62778', 4, 1),
(110, 'name1357', 'user04281', 'user80694@example.com', '90628', 1, 1),
(111, 'TestBat', 'bruce', 'bruce@wayneent.com', 'wayne', 3, 0);

-- --------------------------------------------------------

--
-- Table structure for table `userprofile`
--

CREATE TABLE `userprofile` (
  `role_id` int(50) NOT NULL,
  `role` varchar(50) DEFAULT NULL,
  `suspended` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userprofile`
--

INSERT INTO `userprofile` (`role_id`, `role`, `suspended`) VALUES
(1, 'Admin', 0),
(2, 'Cleaner', 0),
(3, 'HomeOwner', 0),
(4, 'PlatfMngr', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories_services`
--
ALTER TABLE `categories_services`
  ADD PRIMARY KEY (`catsv_id`),
  ADD KEY `parentCat_id` (`parentCat_id`);

--
-- Indexes for table `cleaner_service`
--
ALTER TABLE `cleaner_service`
  ADD PRIMARY KEY (`clean_svc_id`),
  ADD UNIQUE KEY `price` (`price`),
  ADD KEY `cleaner_id` (`cleaner_id`,`service_id`),
  ADD KEY `service_id(fk)` (`service_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `job_history`
--
ALTER TABLE `job_history`
  ADD KEY `cleaner_id` (`cleaner_id`),
  ADD KEY `booked_by` (`booked_by`),
  ADD KEY `service_id` (`service_id`),
  ADD KEY `total_charged` (`total_charged`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `profile_view`
--
ALTER TABLE `profile_view`
  ADD PRIMARY KEY (`view_id`),
  ADD KEY `cleaner_id` (`cleaner_id`),
  ADD KEY `viewer_id` (`viewer_id`);

--
-- Indexes for table `shortlist`
--
ALTER TABLE `shortlist`
  ADD PRIMARY KEY (`short_id`),
  ADD UNIQUE KEY `cleaner_id_2` (`cleaner_id`,`homeowner_id`,`category_id`,`service_id`),
  ADD KEY `homeowner_id` (`homeowner_id`),
  ADD KEY `category_id` (`category_id`,`service_id`),
  ADD KEY `service_id` (`service_id`),
  ADD KEY `cleaner_id` (`cleaner_id`),
  ADD KEY `clean_svc_id` (`clean_svc_id`);

--
-- Indexes for table `useraccounts`
--
ALTER TABLE `useraccounts`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `role_id(fk)` (`role_id`);

--
-- Indexes for table `userprofile`
--
ALTER TABLE `userprofile`
  ADD PRIMARY KEY (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories_services`
--
ALTER TABLE `categories_services`
  MODIFY `catsv_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=172;

--
-- AUTO_INCREMENT for table `cleaner_service`
--
ALTER TABLE `cleaner_service`
  MODIFY `clean_svc_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=306;

--
-- AUTO_INCREMENT for table `profile_view`
--
ALTER TABLE `profile_view`
  MODIFY `view_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=115;

--
-- AUTO_INCREMENT for table `shortlist`
--
ALTER TABLE `shortlist`
  MODIFY `short_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=213;

--
-- AUTO_INCREMENT for table `useraccounts`
--
ALTER TABLE `useraccounts`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=112;

--
-- AUTO_INCREMENT for table `userprofile`
--
ALTER TABLE `userprofile`
  MODIFY `role_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `categories_services`
--
ALTER TABLE `categories_services`
  ADD CONSTRAINT `parent_cat(fk)` FOREIGN KEY (`parentCat_id`) REFERENCES `categories_services` (`catsv_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `cleaner_service`
--
ALTER TABLE `cleaner_service`
  ADD CONSTRAINT `cleaner_id(fk)` FOREIGN KEY (`cleaner_id`) REFERENCES `useraccounts` (`user_id`),
  ADD CONSTRAINT `cleaner_service_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories_services` (`parentCat_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `service_id(fk)` FOREIGN KEY (`service_id`) REFERENCES `categories_services` (`catsv_id`) ON UPDATE CASCADE;

--
-- Constraints for table `job_history`
--
ALTER TABLE `job_history`
  ADD CONSTRAINT `job_history_ibfk_1` FOREIGN KEY (`cleaner_id`) REFERENCES `useraccounts` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `job_history_ibfk_3` FOREIGN KEY (`service_id`) REFERENCES `categories_services` (`catsv_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `job_history_ibfk_4` FOREIGN KEY (`total_charged`) REFERENCES `cleaner_service` (`price`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `job_history_ibfk_5` FOREIGN KEY (`booked_by`) REFERENCES `useraccounts` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `job_history_ibfk_6` FOREIGN KEY (`category_id`) REFERENCES `categories_services` (`parentCat_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `profile_view`
--
ALTER TABLE `profile_view`
  ADD CONSTRAINT `profile_view_ibfk_1` FOREIGN KEY (`cleaner_id`) REFERENCES `useraccounts` (`user_id`),
  ADD CONSTRAINT `profile_view_ibfk_2` FOREIGN KEY (`viewer_id`) REFERENCES `useraccounts` (`user_id`);

--
-- Constraints for table `shortlist`
--
ALTER TABLE `shortlist`
  ADD CONSTRAINT `shortlist_ibfk_1` FOREIGN KEY (`cleaner_id`) REFERENCES `useraccounts` (`user_id`),
  ADD CONSTRAINT `shortlist_ibfk_2` FOREIGN KEY (`homeowner_id`) REFERENCES `useraccounts` (`user_id`),
  ADD CONSTRAINT `shortlist_ibfk_3` FOREIGN KEY (`service_id`) REFERENCES `categories_services` (`catsv_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `shortlist_ibfk_5` FOREIGN KEY (`clean_svc_id`) REFERENCES `cleaner_service` (`clean_svc_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `shortlist_ibfk_6` FOREIGN KEY (`category_id`) REFERENCES `categories_services` (`parentCat_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `useraccounts`
--
ALTER TABLE `useraccounts`
  ADD CONSTRAINT `role_id(fk)` FOREIGN KEY (`role_id`) REFERENCES `userprofile` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
