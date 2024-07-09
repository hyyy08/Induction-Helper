-- Stored Users
CREATE TABLE databaseUser (
    userID INT PRIMARY KEY,
    tutorID INT,
    email VARCHAR(254) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    userDate DATE NOT NULL,
    userLevel VARCHAR(7) NOT NULL,
    CONSTRAINT fk_tutorID FOREIGN KEY (tutorID) REFERENCES databaseUser(userID)
);

-- Courses Table
CREATE TABLE Courses (
    courseCode CHAR(8) PRIMARY KEY,
    courseDescription TEXT,
    school TEXT
);

-- Enrollment Table: 
CREATE TABLE Enrollment (
    userID INT,
    courseCode VARCHAR(8),
    startYear YEAR,
    graduationYear YEAR,
    graduated BOOLEAN,
    CONSTRAINT fk_enrollment_userID FOREIGN KEY (userID) REFERENCES databaseUser(userID),
    CONSTRAINT fk_enrollment_courseCode FOREIGN KEY (courseCode) REFERENCES Courses(courseCode)
);

-- Equipment Table
CREATE TABLE Equipment (
    barcode INT PRIMARY KEY, -- find out barcode number - I believe it outputs it as a txt?
    courseCode VARCHAR(8),
    equipmentName VARCHAR(100),
    equipmentDescription TEXT,
    CONSTRAINT fk_courseCode FOREIGN KEY (courseCode) REFERENCES Courses(courseCode)
);

-- Completed Table: 
CREATE TABLE Completed (
    userID INT,
    barcode INT,
    dateAdded DATE,
    dateCompleted DATE,
    completionStatus BOOLEAN,
    CONSTRAINT fk_completed_userID FOREIGN KEY (userID) REFERENCES databaseUser(userID),
    CONSTRAINT fk_completed_barcode FOREIGN KEY (barcode) REFERENCES Equipment(barcode)
);