# Queens College
# Database System (CSCI 331)
# Winter 2024
# Assignment 7: Stored Procedures and Functions
# Kayla Washington

import Assignment5 as AS5
import OutputUtil as OU


def main():
    comments, queries = AS5.readQueries("Assignment7.sql")
    outputfile = "Assignment7.html"
    AS5.processQueries(outputfile, comments, queries, "udb", "Assignment 7",  True)

    comments, queries = AS5.readQueries("Analytics.sql")
    outputfile = "Analytics.html"  # Specify the output file name here
    AS5.processQueries(outputfile, comments, queries, "udb", "Assignment 7", True)


if __name__ == '__main__':
    main()
