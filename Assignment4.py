# Queens College
# Database System (CSCI 331)
# Winter 2024
# Assignment 4 Query Runner, Tracker, Visual
# Kayla Washington
import Assignment3 as AS3
import OutputUtil as OU


def processQueries(filename, db, assignment):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        queries = text.strip().split(";")
        tables = []
        for query in queries:
            if len(query.strip()) == 0:
                continue
            try:
                if "*/" in query:
                    comment, sql = query.split("*/")
                    comment = comment.replace("/*", "").strip()
                    sql = sql.strip()
                    headers, data = AS3.run_query(sql, comment, db, assignment)
                    alignments = ["l"] * len(headers)
                    types = ["r"] * len(headers)
                    table = [comment, headers, types, alignments, data]
                    tables.append(table)
                else:
                    print(f"No data returns for query: {query}\n\n")
            except Exception as e:
                print(f"Error procesing query: {query}\n Error: {e}\n\n")
        outputfile = assignment.replace(" ", "") + ".html"
        title = "ALL queries for " + assignment + " in " + filename
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
    processQueries("Assignment4.sql", "udb", "Assignment4")


if __name__ == '__main__':
    main()
