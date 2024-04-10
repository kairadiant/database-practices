# Queens College
# Database System (CSCI 331)
# Winter 2024
# Assignment 5 Tables, Views, and Meta-Data
# Kayla Washington
from imp import reload

import Assignment3 as AS3
import OutputUtil as OU



def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_number(x):
    return isinstance(x, int) or isinstance(x, float) or (isinstance(x, str) and is_float(x))


def readQueries(filename):
    with open(filename, "r", encoding='utf-8') as file:
        text = file.read()
        queries = text.strip().split(";")
        comments = []
        sqls = []
        for query in queries:
            if len(query.strip()) == 0:
                continue
            if "*/" in query:
                comment, sql = query.split("*/", 1)
                comment = comment.replace("/*", "").strip()
            else:
                comment = f"Query from: '{filename}'"
                sql = query
            sql = sql.strip()
            comments.append(comment)
            sqls.append(sql)
        return comments, sqls


# def processQueries(comments, queries, db, assignment, add_stats=False):
#     tables = []
#     for i in range(len(queries)):
#         query = queries[i]
#         comment = comments[i]
#         try:
#             headers, data = AS3.run_query(query, comment, db, assignment)
#             if len(headers) == 0:
#                 continue
#             numeric = [all([is_number(data[i][j]) for i in range(len(data))]) for j in range(len(data[0]))]
#             types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
#             alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
#             if add_stats:
#                 stat_cols = [j for j in range(len(numeric)) if numeric[j]]
#                 if len(stat_cols) > 0:
#                     OU.add_stats(data, stat_cols, 0, 3, True)
#             table = [comment, headers, types, alignments, data]
#             tables.append(table)
#         except Exception as e:
#             print(f"Error processing query: {query}\n Error: {e}\n\n")
#     outputfile = assignment.replace(" ", "") + ".html"
#     title = f"ALL queries for '{assignment}'"
#     OU.write_html_file_new(outputfile, title, tables, open_file=True, do_toc=True)


#[1] Define a function get_ruler(length) that will create a "ruler" (i.e. numeric column headings) used to measure the positions and total space, something like:
def get_ruler_for_html(length):
    ruler1 = "".join([str(10*i).rjust(10, ' ') for i in range(1, 2+int(length/10))])
    ruler1 = ruler1.replace(' ', '&nbsp;')
    ruler2 = "0123456789" * (1+ int(length/10))
    return ruler1 + "<br>" + ruler2


def processQueries(comments, queries, db, assignment, format=""):
    tables = []
    for i in range(len(queries)):
        query = queries[i]
        comment = comments[i]
        try:
            if format in ["F", "V"]:
                headers, data, cursor_desc = AS3.run_query(query, comment, db, assignment, None, True)
                headers.append(("Fixed" if format == "F" else "Variable") + "-Length Format")
                col_widths = [desc[3] for desc in cursor_desc]
                for row in data:
                    print(format)
                    if format == "F":
                        record = "".join([str(row[i]).ljust(col_widths[i], " ") for i in range(len(col_widths))])
                        record = record.replace(" ", "&nbsp;")
                    else:
                        record = "|".join([str(row[i]) for i in range(len(col_widths))])
                    ruler = "<tt>" + get_ruler_for_html(sum(col_widths)) + "<br>" + record + "</tt>"
                    row.append(ruler)
            else:
                headers, data = AS3.run_query(query, comment, db, assignment)
            if len(headers) == 0:
                continue
            numeric = [all([is_number(data[i][j]) for i in range(len(data))]) for j in range(len(data[0]))]
            types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
            alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
            table = [comment, headers, types, alignments, data]
            tables.append(table)
        except:
            print("Error processing query", query)
    output_file = assignment.replace(" ", "") + ".html"
    title = f"All queries for '{assignment}'"
    OU.write_html_file_new(output_file, title, tables, True, None, True)


def retrieve_query_log(assignments, db):
    tables = []
    for assignment in assignments:
        sql = f"select * from query where query_assn = '{assignment}'"
        desc = f"retrieve all queries executed for {assignment}"
        headers, data = AS3.run_query(sql, desc, db, assignments[-1])
        alignments = ["l"] * len(headers)
        types = ["S"] * len(headers)
        table = [desc, headers, types, alignments, data]
        tables.append(table)
        outputfile = assignment.replace(" ", "") + "query-history.html"
        title = "ALL queries for to date"
        OU.write_html_file_new(outputfile, title, tables, open_file=True, do_toc=True)


def main():
    # comments, queries = readQueries("Assignment4.sql")
    # processQueries(comments, queries, "udb",  "Assignment 4", True)
    #
    # comments, queries = readQueries("Assignment5.sql")
    # processQueries(comments, queries, "udb", "Assignment 5", True)
    #
    # assignments = [f"Assignment {i}" for i in range(3,6)]
    # retrieve_query_log(assignments, "udb")

    comments, queries = readQueries("Analytics.sql")
    processQueries(comments, queries, "udb", "Assignment 5", True)


if __name__ == '__main__':
    main()
