/* Drop existing 'grade_points' table if it exists */
DROP TABLE IF EXISTS grade_points;

/* Create the 'grade_points' table */
CREATE TABLE grade_points (
    grade CHAR(2) PRIMARY KEY,
    points DECIMAL(3,1) CHECK(points >= 0 AND points <= 4)
);

/* Insert data into the 'grade_points' table */
INSERT INTO grade_points VALUES
    ('A', 4.0), ('A-', 3.7), ('B+', 3.3), ('B', 3.0),
    ('B-', 2.7), ('C+', 2.3), ('C', 2.0), ('C-', 1.7),
    ('D+', 1.3), ('D', 1.0), ('D-', 0.7), ('F', 0.0);

/* Add a foreign key to the 'takes' table referencing the 'grade_points' table */
ALTER TABLE takes
ADD FOREIGN KEY (grade) REFERENCES grade_points(grade);

/* Create the 'v_takes_points' view */
CREATE OR REPLACE VIEW v_takes_points AS
SELECT t.*, gp.points
FROM takes t
JOIN grade_points gp ON t.grade = gp.grade;

/* Compute total grade points for student X */
SELECT COALESCE(SUM(t.grade * gp.points), 0) AS total_grade_points
FROM takes t
LEFT JOIN grade_points gp ON t.grade = gp.grade
WHERE t.id = '00128';

/* Compute GPA for student X */
SELECT COALESCE(SUM(t.grade * gp.points) / SUM(t.grade), 0) AS gpa
FROM takes t
LEFT JOIN grade_points gp ON t.grade = gp.grade
WHERE t.id = '00128';

/* Create the 'v_student_gpa' view */
CREATE OR REPLACE VIEW v_student_gpa AS
SELECT t.id, COALESCE(SUM(t.grade * gp.points) / SUM(t.grade), 0) AS gpa
FROM takes t
LEFT JOIN grade_points gp ON t.grade = gp.grade
GROUP BY t.id;
