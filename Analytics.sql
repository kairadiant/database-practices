/* List of databases, tables, columns, and data types */


SELECT *
FROM v_udb_columns
ORDER BY table_name, COLUMN_NUM;


/* Summary of queries */

SELECT query_assn, COUNT(*), MIN(query_dur) AS Min_Dur, AVG(query_dur) AS Avg_Dur, MAX(query_dur) AS Max_Dur, SUM(query_dur) AS Total_Dur
FROM query
GROUP BY query_assn
ORDER BY query_assn;

/* Retrieve queries for Assignment 3 */

SELECT * FROM query where query_assn = 'Assignment 3' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 4 */

SELECT * FROM query where query_assn = 'Assignment 4' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 5 */

SELECT * FROM query where query_assn = 'Assignment 5' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 6 */

SELECT * FROM query where query_assn = 'Assignment 6' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 7 */

SELECT * FROM query where query_assn = 'Assignment 7' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 8 */

SELECT * FROM query where query_assn = 'Assignment 8' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 9 */

SELECT * FROM query where query_assn = 'Assignment 9' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 10 */

SELECT * FROM query where query_assn = 'Assignment10a' ORDER BY query_ended LIMIT 100;


/* Retrieve queries for Assignment 11 */

SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT11', 'ASSIGNMENT11') ORDER BY query_ended LIMIT 100;


/* Retrieve queries for Assignment 12 */

SELECT * FROM query where query_assn = 'Assignment12a' ORDER BY query_ended LIMIT 100;


/* Retrieve from view v_table_backups that has a list of backups */
SELECT * FROM v_table_backups;
