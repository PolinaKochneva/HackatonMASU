BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Moderators" (
	"ID Модератора"	INTEGER NOT NULL,
	"Фамилия модератора"	TEXT NOT NULL,
	"Имя модератора"	TEXT NOT NULL,
	"Отчество модератора"	TEXT DEFAULT NULL,
	"Электронная почта"	TEXT NOT NULL UNIQUE,
	"Логин"	TEXT NOT NULL UNIQUE,
	"Пароль"	TEXT NOT NULL,
	"Номер телефона"	TEXT DEFAULT NULL UNIQUE,
	PRIMARY KEY("ID Модератора" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Invited_organizations" (
	"Номер письма"	INTEGER NOT NULL,
	"Название организации"	TEXT NOT NULL UNIQUE,
	"Фамилия руководителя"	TEXT NOT NULL,
	"Имя руководителя"	TEXT NOT NULL,
	"Отчество руководителя"	TEXT DEFAULT NULL,
	"Электронная почта организации"	TEXT DEFAULT NULL UNIQUE,
	"Тема письма"	TEXT NOT NULL,
	"Дата отправки письма"	NUMERIC NOT NULL,
	"Участник (Да/Нет)"	INTEGER DEFAULT NULL,
	PRIMARY KEY("Номер письма" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Participating_organizations" (
	"Номер организации_участника"	INTEGER NOT NULL,
	"Название организации"	TEXT NOT NULL UNIQUE,
	"Фамилия руководителя"	TEXT NOT NULL,
	"Имя руководителя"	TEXT NOT NULL,
	"Отчество руководителя"	TEXT DEFAULT NULL,
	"Электронная почта организации"	TEXT DEFAULT NULL UNIQUE,
	"Ссылка на сайт организации"	TEXT DEFAULT NULL UNIQUE,
	"Номер письма"	INTEGER NOT NULL UNIQUE,
	"Что может предоставить"	TEXT DEFAULT NULL,
	FOREIGN KEY("Номер письма") REFERENCES "Invited_organizations"("Номер письма") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("Номер организации_участника" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Participants" (
	"ID Участника"	INTEGER NOT NULL,
	"Фамилия участника"	TEXT DEFAULT NULL,
	"Имя участника"	TEXT DEFAULT NULL,
	"Отчество участника"	TEXT DEFAULT NULL,
	"Дата рождения"	NUMERIC DEFAULT NULL,
	"Место обучения"	TEXT DEFAULT NULL,
	"Место работы"	TEXT DEFAULT NULL,
	"Электронная почта"	TEXT NOT NULL UNIQUE,
	"Логин"	TEXT NOT NULL UNIQUE,
	"Пароль"	TEXT NOT NULL,
	"Номер команды"	INTEGER DEFAULT NULL,
	FOREIGN KEY("Номер команды") REFERENCES "Teams"("Номер команды") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("ID Участника" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Problem_solution" (
	"Порядок оценивания"	INTEGER NOT NULL,
	"Этап"	INTEGER NOT NULL,
	"Номер команды"	INTEGER NOT NULL,
	"Номер задачи"	INTEGER NOT NULL,
	"Время начала"	NUMERIC NOT NULL,
	"Результат этапа"	TEXT NOT NULL,
	"Экспертная оценка"	INTEGER NOT NULL,
	"Результирующая оценка"	INTEGER NOT NULL,
	"Хранилище решения (ссылка)"	TEXT NOT NULL,
	FOREIGN KEY("Номер задачи") REFERENCES "Tasks"("Номер задачи") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("Номер команды") REFERENCES "Teams"("Номер команды") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("Порядок оценивания" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Representatives_organizations" (
	"ID Представителя организации"	INTEGER NOT NULL,
	"Фамилия представителя организации"	TEXT NOT NULL,
	"Имя представителя организации"	TEXT NOT NULL,
	"Отчество представителя организации"	TEXT DEFAULT NULL,
	"Электронная почта представителя организации"	TEXT NOT NULL UNIQUE,
	"Номер организации"	INTEGER NOT NULL,
	"Должность"	TEXT DEFAULT NULL,
	"Статус на мероприятии"	TEXT DEFAULT NULL,
	FOREIGN KEY("Номер организации") REFERENCES "Participating_organizations"("Номер организации_участника") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("ID Представителя организации" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Tasks" (
	"Номер задачи"	INTEGER NOT NULL,
	"Категория"	TEXT NOT NULL,
	"Номер организации_участника"	INTEGER NOT NULL,
	"Ссылка на текст задания"	TEXT DEFAULT NULL,
	FOREIGN KEY("Номер организации_участника") REFERENCES "Participating_organizations"("Номер организации_участника") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("Номер задачи" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Teams" (
	"Номер команды"	INTEGER NOT NULL,
	"Название команды"	TEXT NOT NULL,
	"Номер задачи"	INTEGER DEFAULT NULL UNIQUE,
	"Номер модератора"	INTEGER DEFAULT NULL UNIQUE,
	FOREIGN KEY("Номер модератора") REFERENCES "Moderators"("ID Модератора") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("Номер задачи") REFERENCES "Tasks"("Номер задачи") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("Номер команды" AUTOINCREMENT)
);
COMMIT;
