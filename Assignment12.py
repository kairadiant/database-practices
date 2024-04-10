# Database Systems (CSCI 331)
# Winter 2024
# Assignment 12 - Indexing and Query Optimization
# Kayla Washington

import DBUtil


def main():
    DBUtil.assn = "Assignment12"
    DBUtil.db = "udb"

    comments, queries = DBUtil.read_queries(DBUtil.assn + ".sql")
    DBUtil.process_queries(comments, queries, DBUtil.db, DBUtil.assn)

    comments, queries = DBUtil.read_queries("Analytics.sql")
    DBUtil.process_queries(comments, queries, DBUtil.db, DBUtil.assn + "a")


if __name__ == '__main__':
    main()