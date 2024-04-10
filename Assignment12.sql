/* Drop Index on query table*/
ALTER TABLE query
DROP INDEX idx_query_assignment;


/* Select all queries using IN clause without Index*/
Select count(*) as count From query where query_assn in
('Assignment3','Assignment4','Assignment5','Assignment6','Assignment7',
 'Assignment8', 'Assignment9', 'Assignment10', 'Assignment11');


/* Select all queries using OR clause without Index */
Select count(*) as count From query where
query_assn = 'Assignment3' or
query_assn = 'Assignment4' or
query_assn = 'Assignment5' or
query_assn = 'Assignment6' or
query_assn = 'Assignment7' or
query_assn = 'Assignment8' or
query_assn = 'Assignment9' or
query_assn = 'Assignment10' or
query_assn = 'Assignment11';


/* Select all queries using LIKE Clause without Index */
Select count(*) as count From query where query_assn like 'Assignment %';


/* Select all queries using UNION Clause without Index */
Select sum(c) as count From
(Select count(*) as c From query where query_assn = 'Assignment3'
union
Select count(*) as c From query where query_assn = 'Assignment4'
union
Select count(*) as c From query where query_assn = 'Assignment5'
union
Select count(*) as c From query where query_assn = 'Assignment6'
union
Select count(*) as c From query where query_assn = 'Assignment7'
union
Select count(*) as c From query where query_assn = 'Assignment8'
union
Select count(*) as c From query where query_assn = 'Assignment9'
union
Select count(*) as c From query where query_assn = 'Assignment10'
union
Select count(*) as c From query where query_assn = 'Assignment11')
as counts;


/* Create Index on query table */
CREATE INDEX idx_query_assignment ON query (query_assn);


/* Select all queries using IN clause with Index */
Select count(*) as count From query where query_assn in
('Assignment3','Assignment4','Assignment5','Assignment6','Assignment7',
 'Assignment8', 'Assignment9', 'Assignment10', 'Assignment11');



/* Select all queries using OR clause with Index */
Select count(*) as count From query where
query_assn = 'Assignment3' or
query_assn = 'Assignment4' or
query_assn = 'Assignment5' or
query_assn = 'Assignment6' or
query_assn = 'Assignment7' or
query_assn = 'Assignment8' or
query_assn = 'Assignment9' or
query_assn = 'Assignment10' or
query_assn = 'Assignment11';


/* Select all queries using LIKE Clause with Index */
Select count(*) as count From query where query_assn like 'Assignment %';


/* Select all queries using UNION Clause with Index */
Select sum(c) as count From
(Select count(*) as c From query where query_assn = 'Assignment3'
union
Select count(*) as c From query where query_assn = 'Assignment4'
union
Select count(*) as c From query where query_assn = 'Assignment5'
union
Select count(*) as c From query where query_assn = 'Assignment6'
union
Select count(*) as c From query where query_assn = 'Assignment7'
union
Select count(*) as c From query where query_assn = 'Assignment8'
union
Select count(*) as c From query where query_assn = 'Assignment9'
union
Select count(*) as c From query where query_assn = 'Assignment10'
union
Select count(*) as c From query where query_assn = 'Assignment11')
as counts;


/* Find queries associated with this assignment */
Select * From query where query_assn = 'Assignment12' Order by query_ended desc limit 10;