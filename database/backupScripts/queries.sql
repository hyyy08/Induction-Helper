-- Specific user who have completed a specific equipment
SELECT 
    CASE 
        WHEN EXISTS (
            SELECT 1 
            FROM Completed 
            WHERE userID = [User ID] AND barcode = [Barcode]
        )
        THEN 'Completed'
        ELSE 'Not Completed'
    END AS completion_status;

-- List users who have completed a specific equipment
SELECT AppUser.* 
FROM AppUser 
INNER JOIN Completed ON AppUser.userID = Completed.userID 
WHERE Completed.barcode = 'Barcode';

-- Find users enrolled in a specific course
SELECT AppUser.* 
FROM AppUser 
INNER JOIN Enrollment ON AppUser.userID = Enrollment.userID 
WHERE Enrollment.courseCode = 'Course Code';

-- Find equipment for a specific course
SELECT * FROM Equipment WHERE courseCode = 'Course Code';

-- Count the numbers of students enrolled in each course.
SELECT courseCode, COUNT(userID) AS num_enrolled 
FROM Enrollment 
GROUP BY courseCode;
