# # Queens College
# # Database Systems (CSCI 331)
# # Winter 2024
# # Assignment 3 - SQL & Programing Language
# # Kayla Washington
import os
import webbrowser

import pymysql
import time
import texttable


def print_table_to_html(title, headers, data, alignments=None):
    if alignments is None:
        alignments = ["l"] * len(headers)

    table_html = f"<h2>{title}</h2><table border='1' style='border-collapse: collapse;'>"
    table_html += "<tr>"
    table_html += "".join(
        [f"<th style='padding: 8px; text-align: {align}'>{col}</th>" for col, align in zip(headers, alignments)])
    table_html += "</tr>"

    for row in data:
        table_html += "<tr>"
        table_html += "".join(
            [f"<td style='padding: 8px; text-align: {align}'>{col}</td>" for col, align in zip(row, alignments)])
        table_html += "</tr>"

    table_html += "</table><br>"
    return table_html


def save_to_html(html_content):
    with open("Assignment3.html", "w") as html_file:
        html_file.write(html_content)


def print_table(title, headers, data, alignments=None):
    if alignments is None:
        alignments = ["l"] * len(headers)
    tt = texttable.Texttable(0)
    tt.set_cols_align(alignments)
    tt.add_rows([headers] + data, header=True)
    print(title)
    print(tt.draw())


def get_password():
    with open('password.txt', 'r') as file:
        return file.read().strip()


password = get_password()
user = "Kayla"


def list_db_data(cursor, sql, desc):
    cursor.execute(sql)
    results = [row[0] for row in cursor]
    print(desc + ":", results)
    return results


def log_query(query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur, conn=None):
    query_text = query_text.replace("'", "\\'")
    query = f"INSERT into query (query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur) \nvalues ('{query_text}','{query_desc}','{query_db}', {query_rows} ,'{query_user}','{query_assn}',{query_dur})"
    newconn = False
    if conn is None:
        newconn = True
        conn = pymysql.connect(host="localhost", user="root", passwd=password, db="udb")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    if newconn:
        conn.close()


def run_query(query_text, query_desc, query_db, assignment, query_execute_values=None, get_cursor_desc=False):
    query_src = assignment
    conn = pymysql.connect(host="localhost", user="root", passwd=password, db=query_db)
    start = time.time()
    cursor = conn.cursor()
    if query_text.upper().startswith("CALL"):
        proc_query = query_text[4:].strip()
        idx1 = proc_query.index('(')
        idx2 = proc_query.index(')')
        arg = int(proc_query[idx1+1 : idx2])
        proc = proc_query[:idx1]
        print(f"PROC QUERY {proc}")
        cursor.callproc(proc,(arg,))
    else:
        if query_execute_values is None:
            cursor.execute(query_text)
        else:
            cursor.execute(query_text, query_execute_values)

    end = time.time()
    duration = end - start
    rows = cursor.fetchall()
    conn.commit()
    log_query(query_text, query_desc, query_db, len(rows), user, query_src, duration)
    conn.close()
    query_upper = query_text.upper()
    if query_upper.startswith("SELECT") or query_upper.startswith("SHOW") or query_upper.startswith("DESC"):
        headers = [desc[0] for desc in cursor.description]
        if len(rows) == 0:
            data = [[None for _ in headers]]
        else:
            data = [[col for col in row] for row in rows]
        if get_cursor_desc:
            return headers, data, cursor.description
        else:
            return headers, data
    else:
        return [], []


def preliminary():
    conn = pymysql.connect(host="localhost", user="root", passwd=password)
    cursor = conn.cursor()
    databases = list_db_data(cursor, "SHOW DATABASES", "Databases")
    cursor.execute("USE udb")
    tables = list_db_data(cursor, "SHOW TABLES", "Tables in udb")
    for table in tables:
        columns = list_db_data(cursor, "DESC " + table, "Columns in table " + table)
    conn.close()
    return tables


def main():
    assignment = "Assignment 3"
    tables = preliminary()
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="mystyle.css">
    <title>Assignment 3</title>
</head>
<body>
# """
    for table in tables:
        query = "SELECT * FROM " + table
        desc = "Retrieve all rows table " + table
        db = "udb"
        headers, data = run_query(query, desc, db, assignment)
        html_content += (print_table("Table " + table, headers, data))


    # save_to_html(html_content)

if __name__ == "__main__":
    main()
