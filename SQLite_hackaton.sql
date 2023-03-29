BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Invited_organizations" (
	"Letter number"	INTEGER NOT NULL,
	"Organization name"	varchar(100) NOT NULL UNIQUE,
	"Manager surname"	varchar(100) NOT NULL,
	"Manager name"	varchar(100) NOT NULL,
	"Manager patronymic"	varchar(100),
	"Organization email"	varchar(100) UNIQUE,
	"Letter subject"	varchar(100) NOT NULL,
	"Mailing day"	date NOT NULL,
	"Participant (Yes/No)"	tinyint(3),
	PRIMARY KEY("Letter number" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Moderators" (
	"Moderator ID"	INTEGER NOT NULL,
	"Moderator surname"	varchar(100) NOT NULL,
	"Moderator name"	varchar(100) NOT NULL,
	"Moderator patronymic"	varchar(100),
	"Moderator email"	varchar(100) NOT NULL UNIQUE,
	"Login"	varchar(100) NOT NULL UNIQUE,
	"Password"	varchar(100) NOT NULL,
	"Phone number"	char(15) UNIQUE,
	PRIMARY KEY("Moderator ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Participants" (
	"Participant ID"	INTEGER NOT NULL,
	"Participant surname"	varchar(100),
	"Participant name"	varchar(100),
	"Participant patronymic"	varchar(100),
	"Birth date"	date,
	"Place of study"	varchar(100),
	"Place of work"	varchar(100),
	"Participant email"	varchar(100) NOT NULL UNIQUE,
	"Login"	varchar(100) NOT NULL UNIQUE,
	"Password"	varchar(100) NOT NULL,
	"Team number"	INTEGER,
	FOREIGN KEY("Team number") REFERENCES "Teams"("Team number") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("Participant ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Participating_organizations" (
	"Participating organization number"	INTEGER NOT NULL,
	"Organization name"	varchar(100) NOT NULL UNIQUE,
	"Manager surname"	varchar(100) NOT NULL,
	"Manager name"	varchar(100) NOT NULL,
	"Manager patronymic"	varchar(100),
	"Organization email"	varchar(100) UNIQUE,
	"Link to organization website"	varchar(100) UNIQUE,
	"Letter number"	INTEGER NOT NULL UNIQUE,
	"What can provide"	varchar(100),
	FOREIGN KEY("Letter number") REFERENCES "Invited_organizations"("Letter number") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("Participating organization number" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Problem_solution" (
	"Evaluation procedure"	INTEGER NOT NULL,
	"Stage"	varchar(100) NOT NULL,
	"Team number"	INTEGER NOT NULL,
	"Task number"	INTEGER NOT NULL,
	"Start time"	datetime NOT NULL,
	"Stage result"	varchar(100) NOT NULL,
	"Expert review"	INTEGER NOT NULL,
	"Resulting score"	INTEGER NOT NULL,
	"Solution repository (link)"	varchar(100) NOT NULL,
	FOREIGN KEY("Task number") REFERENCES "Tasks"("Task number") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("Team number") REFERENCES "Teams"("Team number") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("Evaluation procedure" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Representatives_organizations" (
	"Organization Representative ID"	INTEGER NOT NULL,
	"Organization representative surname"	varchar(100) NOT NULL,
	"Organization representative name"	varchar(100) NOT NULL,
	"Organization representative patronymic"	varchar(100),
	"Organization representative email"	varchar(100) NOT NULL UNIQUE,
	"Organization number"	INTEGER NOT NULL,
	"Post"	varchar(100),
	"Status at the event"	varchar(100),
	FOREIGN KEY("Organization number") REFERENCES "Participating_organizations"("Participating organization number") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("Organization Representative ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Tasks" (
	"Task number"	INTEGER NOT NULL,
	"Category"	varchar(100) NOT NULL,
	"Participating organization number"	INTEGER NOT NULL,
	"Link to the task text"	varchar(100),
	FOREIGN KEY("Participating organization number") REFERENCES "Participating_organizations"("Participating organization number") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("Task number" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Teams" (
	"Team number"	INTEGER NOT NULL,
	"Team name"	varchar(100) NOT NULL UNIQUE,
	"Task number"	INTEGER,
	"Moderator number"	INTEGER,
	FOREIGN KEY("Task number") REFERENCES "Tasks"("Task number") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("Moderator number") REFERENCES "Moderators"("Moderator ID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("Team number" AUTOINCREMENT)
);
COMMIT;
