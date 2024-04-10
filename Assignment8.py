# Queens College
# Database Systems (CSCI 331)
# Winter 2024
# Assignment 8: Complex Data Types
# Kayla Washington
import json

import Assignment3 as AS3
import Assignment5 as AS5
import OutputUtil as OU


# [2a]
def to_csv(headers, data):
    s_headers = ','.join(headers)
    s_data = '\n'.join([",".join([str(col) for col in row]) for row in data])
    return s_headers + "\n" + s_data


def to_json(title, headers, data):
    rows = []
    for i in range(len(data)):
        s = '{' + ', '.join(['"' + headers[j] + '":"' + str(data[i][j]) + '"' for j in range(len(headers))]) + '}'
        rows.append(s)
    return '{' + '"' + title + '":[\n' + ",\n".join(rows) + ']}'


def to_xml(title, headers, data):
    nl = "\n"
    headers = [header.replace(" ", "") for header in headers]
    x_header = '<?xml version="1.0" encoding="UTF-8"' + '?>'
    x_title = nl + OU.create_element("title", xml_clean(title))
    content = ""
    for row in data:
        x_items = nl + "".join([OU.create_element(headers[i], xml_clean(row[i])) for i in range(len(row))])
        x_row = OU.create_element("row", x_items)
        content += x_row
    x_body = nl + OU.create_element("root", x_title + content)
    xml = x_header + x_body
    return xml


# [4]
def backup_table(name):
    query = f"SELECT * FROM {name}"
    desc = f"RETRIEVE ROWS FROM {name} FOR backup"
    headers, data = AS3.run_query(query, desc, db, assn)
    csv_data = to_csv(headers, data)
    xml_data = to_xml(name, headers, data)
    json_data = to_json(name, headers, data)
    query2 = (f"INSERT into backup (relation, num_rows, cols, csv_length, xml_length, json_length, csv_data, xml_data, json_data) "
              f"values ('{name}', {len(data)}, {len(headers)}, {len(csv_data)}, {len(xml_data)}, {len(json_data)}, '{csv_data}', '{xml_data}', '{json_data}')")
    desc2 = f"Save a copy of table {name} in different formats"
    headers2, data2 = AS3.run_query(query2, desc2, db, assn)
    print(json_data)


def from_json(json_text, name):
    json_data = json.loads(json_text)
    headers = []
    data = []
    do_headers = True
    for items in json_data[name]:
        row = []
        for item in items:
            row.append(items[item])
            if do_headers:
                headers.append(item)
        do_headers = False
        data.append(row)
    return headers, data


# [3a] Create a Python function from_csv(csv) that converts the csv into headers (1D) and data (2D)
def from_csv(csv):
    lines = csv.split("\n")
    headers = lines[0].split(",")
    data = [lines[1:][i-1].split(",") for i in range(1, len(lines))]
    return headers, data


def restore_data(name):
    query = f"SELECT * FROM backup where lower(relation) = '{name.lower()}' and dtm = (SELECT MAX(dtm) FROM backup where lower(relation) = '{name.lower()}')"
    desc = f"Retrieve the latest backup row for the table {name}"
    headers, data = AS3.run_query(query, desc, db, assn)
    headers_csv, data_csv = from_csv(data[0][7])
    headers_json, data_json = from_json(data[0][9], name)


def xml_clean(item):
    return str(item).replace("&", "&amp;")


assn = "Assignment 8"
db = "udb"


def main():
    comments, queries = AS5.readQueries("Assignment8.sql")
    outputfile = "Assignment8.html"
    AS5.processQueries(outputfile, comments, queries, db, assn)

    udb_tables = ["advisor", "classroom", "course", "department", "instructor", "prereq", "section", "student", "takes",
                  "teaches", "time_slot"]
    for table in udb_tables:
        backup_table(table)

    html_tables = []
    for table in udb_tables:
        html_tables += restore_data(table)
    outputfile = assn.replace(" ", "") + "-restoration.html"
    title = "Restoration of all original University Database Tables"
    OU.write_html_file_new(outputfile, html_tables, True, None, True)



    comments, queries = AS5.readQueries("Analytics.sql")
    outputfile = "Analytics.html"  # Specify the output file name here
    AS5.processQueries(outputfile, comments, queries, "udb", "Assignment 8", True)


if __name__ == '__main__':
    main()
