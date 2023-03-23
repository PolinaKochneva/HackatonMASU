-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Мар 23 2023 г., 08:15
-- Версия сервера: 10.5.18-MariaDB-0+deb11u1
-- Версия PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `hackaton`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Invited_organizations`
--

CREATE TABLE `Invited_organizations` (
  `Номер письма` int(11) NOT NULL,
  `Название организации` varchar(45) NOT NULL,
  `Фамилия руководителя` varchar(45) NOT NULL,
  `Имя руководителя` varchar(45) NOT NULL,
  `Отчество руководителя` varchar(45) NOT NULL,
  `Электронная почта организации` varchar(45) DEFAULT NULL,
  `Тема письма` varchar(45) NOT NULL,
  `Дата отправки письма` date NOT NULL,
  `Участник (Да/Нет)` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Moderators`
--

CREATE TABLE `Moderators` (
  `ID Модератора` int(11) NOT NULL,
  `Фамилия модератора` varchar(45) NOT NULL,
  `Имя модератора` varchar(45) NOT NULL,
  `Отчество модератора` varchar(45) NOT NULL,
  `Электронная почта` varchar(45) NOT NULL,
  `Логин` varchar(45) NOT NULL,
  `Пароль` varchar(45) NOT NULL,
  `Номер телефона` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Participants`
--

CREATE TABLE `Participants` (
  `ID Участника` int(11) NOT NULL,
  `Фамилия участника` varchar(45) NOT NULL,
  `Имя участника` varchar(45) NOT NULL,
  `Отчество участника` varchar(45) NOT NULL,
  `Дата рождения` date NOT NULL,
  `Место обучения` varchar(45) DEFAULT NULL,
  `Место работы` varchar(45) DEFAULT NULL,
  `Электронная почта` varchar(45) NOT NULL,
  `Логин` varchar(45) NOT NULL,
  `Пароль` varchar(45) NOT NULL,
  `Номер команды` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Participating_organizations`
--

CREATE TABLE `Participating_organizations` (
  `Номер организации_участника` int(11) NOT NULL,
  `Название организации` varchar(45) NOT NULL,
  `Фамилия руководителя` varchar(45) NOT NULL,
  `Имя руководителя` varchar(45) NOT NULL,
  `Отчество руководителя` varchar(45) NOT NULL,
  `Электронная почта организации` varchar(45) NOT NULL,
  `Ссылка на сайт организации` varchar(45) DEFAULT NULL,
  `Номер письма` int(11) NOT NULL,
  `Что может предоставить` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Problem_solution`
--

CREATE TABLE `Problem_solution` (
  `Порядок оценивания` int(11) NOT NULL,
  `Этап` varchar(45) NOT NULL,
  `Номер команды` int(11) NOT NULL,
  `Номер задачи` int(11) NOT NULL,
  `Время начала` varchar(45) NOT NULL,
  `Результат этапа` varchar(45) NOT NULL,
  `Экспертная оценка` int(11) NOT NULL,
  `Результирующая оценка` int(11) NOT NULL,
  `Хранилище решения (ссылка)` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Representatives_organizations`
--

CREATE TABLE `Representatives_organizations` (
  `ID Представителя организации` int(11) NOT NULL,
  `Фамилия представителя организации` varchar(45) NOT NULL,
  `Имя представителя организации` varchar(45) NOT NULL,
  `Отчество представителя организации` varchar(45) NOT NULL,
  `Электронная почта представителя организации` varchar(45) NOT NULL,
  `Номер организации` int(11) NOT NULL,
  `Должность` varchar(45) DEFAULT NULL,
  `Статус на мероприятии` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Tasks`
--

CREATE TABLE `Tasks` (
  `Номер задачи` int(11) NOT NULL,
  `Категория` varchar(45) NOT NULL,
  `Номер организации_участника` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Teams`
--

CREATE TABLE `Teams` (
  `Номер команды` int(11) NOT NULL,
  `Название команды` varchar(45) NOT NULL,
  `Номер задачи` int(11) DEFAULT NULL,
  `Номер модератора` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Invited_organizations`
--
ALTER TABLE `Invited_organizations`
  ADD PRIMARY KEY (`Номер письма`);

--
-- Индексы таблицы `Moderators`
--
ALTER TABLE `Moderators`
  ADD PRIMARY KEY (`ID Модератора`);

--
-- Индексы таблицы `Participants`
--
ALTER TABLE `Participants`
  ADD PRIMARY KEY (`ID Участника`),
  ADD KEY `fk_Участники_1` (`Номер команды`);

--
-- Индексы таблицы `Participating_organizations`
--
ALTER TABLE `Participating_organizations`
  ADD PRIMARY KEY (`Номер организации_участника`),
  ADD UNIQUE KEY `Номер письма_UNIQUE` (`Номер письма`),
  ADD KEY `fk_Организации-участники_1_idx` (`Номер письма`);

--
-- Индексы таблицы `Problem_solution`
--
ALTER TABLE `Problem_solution`
  ADD PRIMARY KEY (`Порядок оценивания`),
  ADD UNIQUE KEY `index2` (`Номер команды`,`Номер задачи`),
  ADD KEY `fk_Оценки_решения_задач_1_idx` (`Номер задачи`);

--
-- Индексы таблицы `Representatives_organizations`
--
ALTER TABLE `Representatives_organizations`
  ADD PRIMARY KEY (`ID Представителя организации`),
  ADD KEY `fk_Представители_организаций_1` (`Номер организации`);

--
-- Индексы таблицы `Tasks`
--
ALTER TABLE `Tasks`
  ADD PRIMARY KEY (`Номер задачи`),
  ADD UNIQUE KEY `Index3` (`Номер задачи`),
  ADD KEY `index2` (`Номер организации_участника`);

--
-- Индексы таблицы `Teams`
--
ALTER TABLE `Teams`
  ADD PRIMARY KEY (`Номер команды`),
  ADD KEY `index2` (`Номер модератора`,`Номер задачи`),
  ADD KEY `fk_Команды_2_idx` (`Номер задачи`);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `Participants`
--
ALTER TABLE `Participants`
  ADD CONSTRAINT `fk_Участники_1` FOREIGN KEY (`Номер команды`) REFERENCES `Teams` (`Номер команды`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Participating_organizations`
--
ALTER TABLE `Participating_organizations`
  ADD CONSTRAINT `fk_Организации-участники_1` FOREIGN KEY (`Номер письма`) REFERENCES `Invited_organizations` (`Номер письма`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Problem_solution`
--
ALTER TABLE `Problem_solution`
  ADD CONSTRAINT `fk_Оценки_решения_задач_1` FOREIGN KEY (`Номер задачи`) REFERENCES `Tasks` (`Номер задачи`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Оценки_решения_задач_2` FOREIGN KEY (`Номер команды`) REFERENCES `Teams` (`Номер команды`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Representatives_organizations`
--
ALTER TABLE `Representatives_organizations`
  ADD CONSTRAINT `fk_Представители_организаций_1` FOREIGN KEY (`Номер организации`) REFERENCES `Participating_organizations` (`Номер организации_участника`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Tasks`
--
ALTER TABLE `Tasks`
  ADD CONSTRAINT `fk_Задачи_1` FOREIGN KEY (`Номер организации_участника`) REFERENCES `Participating_organizations` (`Номер организации_участника`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Teams`
--
ALTER TABLE `Teams`
  ADD CONSTRAINT `fk_Команды_1` FOREIGN KEY (`Номер модератора`) REFERENCES `Moderators` (`ID Модератора`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Команды_2` FOREIGN KEY (`Номер задачи`) REFERENCES `Tasks` (`Номер задачи`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
