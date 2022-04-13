# Database Design Implementation


### Computing Platform

We will use Amazon Relational Database Service (RDS).


### Connecting to the class database

<!--  
* Navigate to your VM instance in the Cloud Platform Console, start it again, and click the SSH button that appears next to it. A terminal window will pop up.
-->


After the installation is completed, connect to our postgres database in one of two ways:

* Use [the convenient notebook on colab](https://colab.research.google.com/github/w4111/project1-s22/blob/main/part2.ipynb)
  * You will want to copy the notebook to your google drive if you want to save your work.
* Use `psql`command in your computer's terminal:

      psql -h w4111.cisxo09blonu.us-east-1.rds.amazonaws.com -U YOUR_UNI proj1part2
  * Note that you should connect to proj1part2 database, not w4111! You can check the current database by: `SELECT current_database();`
  * It will ask for your password, which is included in the e-mail we sent. If you didn't get the message, post a private question on discussion board. You may play with Postgres a little bit before the graded project 1 part 1 is returned to you.


### Creating your schema

Create the SQL tables based on your revised schema.

* Each student gets an individual account and environment (i.e. a PostgreSQL "schema") on the database server, so decide with your teammate which database account you will be using. You will share such account credentials and use it for submission.
* Include all key and type constraints.
* The PostgreSQL documentation for [CREATE TABLE](http://www.postgresql.org/docs/10/static/sql-createtable.html)
and [data types](http://www.postgresql.org/docs/10/static/datatype.html) may help.

Create the CHECK constraints that you need to express the rest of your real-world constraints.

* Note: PostgreSQL's CHECK constraints are limited ([see the documentation](http://www.postgresql.org/docs/10/static/ddl-constraints.html)).
* Note: PostgreSQL doesn't support CREATE ASSERTION statements, but does support triggers.

### Populate the tables

Insert at least 10 realistic/real tuples into each table in your database.

### Run some queries

Create at least 3 interesting SELECT queries.  The three queries, together, should include 

* multi-table joins,
* WHERE clauses, and 
* aggregation (e.g. COUNT, SUM, MIN, etc). 

