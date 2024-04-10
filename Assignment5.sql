/* Assignment 5 In-Class View of all tables and columns in UDB database */
CREATE OR REPLACE VIEW v_udb_table_columns AS
SELECT table_name, ORDINAL_POSITION as COLUMN_NUM, COLUMN_NAME, DATA_TYPE, coalesce(CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION) as LENGTH, IS_NULLABLE as NULLABLE
FROM information_schema.columns
WHERE TABLE_SCHEMA = 'udb'
ORDER BY table_name, ORDINAL_POSITION;

/* Select everything from the new view: v_udb_table_columns */
SELECT *
FROM v_udb_table_columns
ORDER BY table_name, COLUMN_NUM;

/* Aggregation technique: Retrieve number of columns per table */
SELECT table_name, count(column_name) as COLUMNS
FROM v_udb_table_columns
GROUP BY table_name;
