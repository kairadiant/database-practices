# Queens College
# Database System (CSCI 331)
# Winter 2024
# Assignment 11: Database Record Storage
# Kayla Washington

import OutputUtil as ou
import Assignment5 as AS5



def main ():
    assn = "Assignment11"
    db = "udb"
    comments, queries = AS5.readQueries(f"{assn}.sql")
    AS5.processQueries(comments, queries, db, assn + "F", "F")
    AS5.processQueries(comments, queries, db, assn + "V", "V")
    comments, queries = AS5.readQueries("Analytics.sql")
    AS5.processQueries(comments, queries, db, f"{assn}a")

if __name__ == "__main__":
    main()