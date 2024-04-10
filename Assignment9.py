# Queens College
# Database System (CSCI 331)
# Winter 2024
# Assignment 9: Pivot Tables in and Outside MYSQL
# Kayla Washington
import Assignment5 as AS5
import Assignment3 as AS3
import OutputUtil as OU


def pivot_table(table, column_x, column_y, column_val):
    query = f"SELECT DISTINCT {column_x} FROM {table}"
    comment = f"GET ALL DISTINCT VALUES OF {column_x} from {table} FOR pivot table"
    headers, data = AS3.run_query(query, comment, db, assn)
    query2 = f"SELECT {column_y}, " + ",\n".join([f"SUM(CASE WHEN {column_x} = '{row[0]}' THEN {column_val} ELSE 0 END) AS '{row[0]}'" for row in data]) + f"FROM {table} GROUP BY {column_y}"
    comment2 = f"Build a pivot table for {column_x} vs {column_y} for {table}"
    result = AS5.processQueries([comment2], [query2], db, assn)
    if result is not None:
        headers2, data2 = result
    else:
        headers2, data2 = [], []
    print(headers2)
    numeric = [all([AS5.is_number(data[i][j]) for i in range(len(data))]) for j in range(len(data[0]))]
    types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
    alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
    table = [comment2, headers2, types, alignments, data2]
    return table


assn = "Assignment 9"
db = "udb"


def main():
    comments, queries = AS5.readQueries("Assignment9.sql")
    AS5.processQueries(comments, queries, db, assn+"sql")
    examples = [["product_sales", "store_location", "product_name", "num_sales"]]
    html_tables = []
    for example in examples:
        html_tables += [pivot_table(example[0], example[1], example[2], example[3])]
    output_file = assn.replace(" ", "") + "-pivot-tables.html"
    title = "Pivot Tables for select examples"
    OU.write_html_file_new(output_file, title, html_tables, True, None, True)

    comments, queries = AS5.readQueries("Analytics.sql")
    outputfile = "Analytics.html"  # Specify the output file name here
    AS5.processQueries(comments, queries, "udb", "Assignment 9", True)


if __name__ == '__main__':
    main()