# Queens College
# Database System (CSCI 331)
# Winter 2024
# Assignment 6 DDL and DML Practice
# Kayla Washington

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
            sql = sql.strip()
            comments.append(comment)
            sqls.append(sql)
        return comments, sqls


def processQueries(comments, queries, db, assignment, outputfile, add_stats=False):
    tables = []
    for i in range(len(queries)):
        query = queries[i]
        comment = comments[i]
        try:
            headers, data = AS3.run_query(query, comment, db, assignment)
            if len(headers) == 0:
                continue
            numeric = [all([is_number(data[i][j]) for i in range(len(data))]) for j in range(len(data[0]))]
            types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
            alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
            if add_stats:
                stat_cols = [j for j in range(len(numeric)) if numeric[j]]
                if len(stat_cols) > 0:
                    OU.add_stats(data, stat_cols, 0, 3, True)
            table = [comment, headers, types, alignments, data]
            tables.append(table)
        except Exception as e:
            print(f"Error processing query: {query}\n Error: {e}\n\n")
    title = f"ALL queries for '{assignment}'"
    OU.write_html_file_new(outputfile, title, tables, open_file=True, do_toc=True)


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
    comments, queries = readQueries("Assignment6.sql")
    outputfile = "Assignment6.html"
    processQueries(comments, queries, "udb", "Assignment 6", "Assignment6.html" , True)
    #
    # assignments = [f"Assignment {i}" for i in range(3,6)]
    # retrieve_query_log(assignments, "udb")

    comments, queries = readQueries("Analytics.sql")
    outputfile = "Analytics.html"  # Specify the output file name here
    processQueries(comments, queries, "udb", "Assignment 6", outputfile, True)


if __name__ == '__main__':
    main()
