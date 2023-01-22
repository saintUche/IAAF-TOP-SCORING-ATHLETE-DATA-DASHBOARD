CREATE DATABASE eventRankings;
USE eventRankings; 


CREATE TABLE Rankings(	
	AthleteID INT AUTO_INCREMENT PRIMARY KEY,
    Competitor VARCHAR(255),
    DOB DATE,
    Nat VARCHAR(10),
	Score int,
    Discipline VARCHAR(100),
	Sex CHAR,
    Jr BOOL
    );
    
-- Change a database
ALTER DATABASE eventRankings
CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci; 

-- Change a table
ALTER TABLE Rankings 
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 

-- SELECT * FROM Rankings;

CREATE TABLE Males AS
SELECT * FROM Rankings WHERE SEX='M';

-- SELECT * FROM Males;

CREATE TABLE Females AS
SELECT * FROM Rankings WHERE Sex='F';

-- SELECT * FROM Females

CREATE TABLE Juniors AS 
SELECT * FROM Rankings WHERE Jr=1;

-- SELECT * FROM Juniors;

CREATE TABLE malesJr AS
SELECT * FROM Juniors WHERE sex='M';

-- SELECT * FROM malesJr;

CREATE TABLE femalesJr AS
SELECT * FROM Juniors WHERE sex='F';

-- SELECT * FROM femalesJr;


CREATE TABLE CountryData(
	Nat VARCHAR(10),
    AthleteCount INT,
    Males INT,
    Females INT,
    ScoreMale INT,
    ScoreFemale INT,
    ScoreTotal INT,
    EventCount INT
);
