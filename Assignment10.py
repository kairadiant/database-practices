# Queens College
# Database System (CSCI 331)
# Winter 2024
# Assignment 10: Database Design and Normalization
# Kayla Washington

import  OutputUtil as ou
import Assignment5 as as5
import Assignment3 as as3


def main():
    assn = "Assignment10"
    db = "udb"
    comments, queries = as5.readQueries(assn +".sql")
    as5.processQueries(comments, queries, db, assn)
    comments, queries = as5.readQueries("Analytics.sql")
    as5.processQueries(comments, queries, db, assn + "a")



if __name__ == "__main__":
    main()