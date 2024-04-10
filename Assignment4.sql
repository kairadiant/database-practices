/* Chapter 3, Slide 49: Find the average instructors’ salaries of those departments where the average salary is greater than $42,000.”*/
select dept_name, avg_salary
from ( select dept_name, avg (salary)
           from instructor
           group by dept_name)
            as dept_avg (dept_name, avg_salary)
where avg_salary > 42000;

/* Chapter 3, Slide 50: Find all departments with the maximum budget */
with max_budget as(
	select MAX(budget) as VALUE
      from department
)
select department.dept_name
from udb.department, max_budget
where department.budget = max_budget.value;

/* Chapter 3, Slide 51: Find all departments where the total salary is greater than the average of the total salary at all departments*/
with dept_total (dept_name, value) as
        (select dept_name, sum(salary)
         from instructor
         group by dept_name),
dept_total_avg(value) as
       (select avg(value)
       from dept_total)
select dept_name
from dept_total, dept_total_avg
where dept_total.value > dept_total_avg.value;

/* Chapter 3, Slide 52: List all departments along with the number
   of
 */
select dept_name,
       (select count(*)
        from instructor
        where department.dept_name = instructor.dept_name)
as run_instructors
from department;

/* Make each student in the Music department who has earned more than 144 credit hours an instructor in the Music department with a salary of  $18,000.*/
insert into instructor
select ID, name, dept_name, 18000
from   student
where   dept_name = 'Music' and total_cred > 144;

/* Chapter 3, Slide 56: Add a new tuple to student  with tot_creds set to null*/
select distinct T.name
from instructor as T, instructor as S
where (T.salary > S.salary) and S.dept_name = 'Biology';

/* Chapter 3, Slide 58: Give  a 5% salary raise to instructors whose salary is less than average*/
update instructor
set salary = salary * 1.05
where salary <  (select avg (salary)
                 from instructor);

/* Chapter 3, Slide 59: Increase salaries of instructors whose salary is over $100,000 by 3% */
update instructor
set salary = salary * 1.03
where salary > 100000;

/* Chapter 3, Slide 59: All others by a 5% */
update instructor
set salary = salary * 1.05
where salary <= 100000;

/* Chapter 3, Slide 61: Recompute and update tot_creds value for all students*/
update student S
set tot_cred = (select sum(credits)
                from takes, course
                where takes.course_id = course.course_id  and
                      S.ID= takes.ID and
                      takes.grade <> 'F' and
                      takes.grade is not null);


/* Sample query for testing */
select * from instructor;

/* Homework Query #1: Retrieve all courses that have the letters a, e, i in THAT order in their name*/
select * from course
where lower(title) like 'a%e%i%';

/* Homework Query #2: Retrieve all courses that have the letters a, e, i in ANY order in their names:*/
SELECT *
FROM course
WHERE title LIKE '%a%' AND title LIKE '%e%' AND title LIKE '%i%';

/*Retrieve the names of all students who failed a course (grade of F) along with the name of the course that they failed:*/
SELECT student.name, course.course_id
FROM student
JOIN takes ON student.id = takes.id
JOIN course ON takes.course_id = course.course_id
WHERE takes.grade = 'F';

/*Retrieve the percentage of solid A grades compared to all courses, and rename that column "Percent_A":*/
SELECT COUNT(CASE WHEN takes.grade = 'A' THEN 1 END) / COUNT(*) * 100 AS Percent_A
FROM takes;

/*Retrieve the names and numbers of all courses that do not have prerequisites:*/
SELECT title, course_id
FROM course
WHERE course_id NOT IN (SELECT DISTINCT prereq_id FROM prereq);

/*Retrieves the names of all students and their advisors if they have one:*/
SELECT student.name AS student_name, instructor.name AS advisor_name
FROM student, instructor
JOIN advisor WHERE (student.id = advisor.s_ID) AND (instructor.id = advisor.i_ID);


