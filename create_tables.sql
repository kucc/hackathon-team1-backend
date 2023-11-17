CREATE TABLE K_TestTable (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  age INT(3)
);

CREATE TABLE `K_MainEvent` (
	`main_event_id`	INT	AUTO_INCREMENT PRIMARY KEY,
	`event_date`	DATE	NOT NULL,
	`event_name`	VARCHAR(255)	NOT NULL,
	`priority`	INT	NOT NULL	DEFAULT 15
);

CREATE TABLE `K_Event` (
	`event_id`	INT AUTO_INCREMENT PRIMARY KEY,
	`event_date`	DATE	NULL,
	`event_name`	VARCHAR(255)	NULL,
	`priority`	INT	NOT NULL	DEFAULT 0,
	`event_type`	VARCHAR(255)	NOT NULL,
	`category`	VARCHAR(255)	NOT NULL
	`finished`	BOOLEAN	NOT NULL	DEFAULT FALSE,
);