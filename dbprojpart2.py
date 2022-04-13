# -*- coding: utf-8 -*-
"""DBprojPart2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qn4Eh_Flky5KZxGNT7rRtJDYoKjf1E_D
"""

!pip3 install sqlalchemy # ORM for databases
!pip3 install ipython-sql # SQL magic function

# Commented out IPython magic to ensure Python compatibility.
# %load_ext sql

"""## Connect With Your Credentials

The current connection string DOES NOT WORK!   
Make sure to change the YOURUSER:YOURPASSWORD part of the connection string to your team's account information!
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql postgresql://tw2724:6246@w4111.cisxo09blonu.us-east-1.rds.amazonaws.com/proj1part2

# change your password
#%%sql ALTER ROLE YOURUNI   
#WITH PASSWORD 'YOURNEWPASSWORD';

# create table
# %%sql CREATE TABLE R (
#     A int,
#     B int
# );
# INSERT INTO R VALUES (1,2);
# INSERT INTO R VALUES (3,4);

# see table R
# %sql SELECT * FROM R;

# see all the tables you have
# %%sql SELECT *
# FROM pg_catalog.pg_tables
# WHERE tableowner='YOURUNI'

# drop table
# %sql DROP TABLE R;

"""MY CODE"""

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT current_database()



# Commented out IPython magic to ensure Python compatibility.
# %sql drop table Users

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE Users
# (
#  user_id int NOT NULL,
#  password text NOT NULL,
#  icon text,
#  gender int CHECK(gender in (0,1)),
#  age int CHECK(age>0),
#  PRIMARY KEY (user_id)
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql INSERT INTO Users VALUES (1,'sdfgsdg','a.png',0,12);
# INSERT INTO Users VALUES (2,'sdgsdg','b.png',1,14);
# INSERT INTO Users VALUES (3,'cvbcf','c.png',1,56);
# INSERT INTO Users VALUES (4,'rfertyr','d.png',1,54);
# INSERT INTO Users VALUES (5,'xcvsdfg','e.png',0,34);
# INSERT INTO Users VALUES (6,'adfsfdsdf','f.png',0,99);
# INSERT INTO Users VALUES (7,'etert','g.png',0,43);
# INSERT INTO Users VALUES (8,'tyrtryut','h.png',1,17);
# INSERT INTO Users VALUES (9,'we4tert','i.png',0,64);
# INSERT INTO Users VALUES (10,'erteert','j.png',1,54);

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM Users

# Commented out IPython magic to ensure Python compatibility.
# %sql drop table Follow

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE Follow
# (
#  user_id_1 int REFERENCES Users(user_id),
#  user_id_2 int REFERENCES Users(user_id),
#  PRIMARY KEY (user_id_1,user_id_2),
#  CHECK (user_id_1 != user_id_2)
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql INSERT INTO Follow VALUES (1,2);
# INSERT INTO Follow VALUES (1,3);
# INSERT INTO Follow VALUES (1,4);
# INSERT INTO Follow VALUES (1,5);
# INSERT INTO Follow VALUES (1,6);
# INSERT INTO Follow VALUES (1,7);
# INSERT INTO Follow VALUES (1,8);
# INSERT INTO Follow VALUES (1,9);
# INSERT INTO Follow VALUES (2,3);
# INSERT INTO Follow VALUES (2,4);

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM Follow

# Commented out IPython magic to ensure Python compatibility.
# %sql drop table Merchants

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE Merchants
# (
#  merchant_id int NOT NULL,
#  category text,
#  address text,
#  star int CHECK(star>0 and star<=5),
#  is_vip boolean,
#  PRIMARY KEY (merchant_id)
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql INSERT INTO Merchants VALUES (1,'food','',1,True);
# INSERT INTO Merchants VALUES (2,'food','',1,True);
# INSERT INTO Merchants VALUES (3,'food','',1,True);
# INSERT INTO Merchants VALUES (4,'food','',1,True);
# INSERT INTO Merchants VALUES (5,'food','',1,True);
# INSERT INTO Merchants VALUES (6,'food','',1,False);
# INSERT INTO Merchants VALUES (7,'Milk Tea','',1,False);
# INSERT INTO Merchants VALUES (8,'Milk Tea','',1,False);
# INSERT INTO Merchants VALUES (9,'Milk Tea','',1,False);
# INSERT INTO Merchants VALUES (10,'Milk Tea','',1,False);

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM Merchants

# Commented out IPython magic to ensure Python compatibility.
# %sql drop table Wishlists_edit

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE Wishlists_edit
# (
#  wishlist_id int UNIQUE NOT NULL,
#  user_id int NOT NULL,
#  number int CHECK(number >0),
#  PRIMARY KEY (wishlist_id, user_id),
#  FOREIGN KEY (user_id) REFERENCES Users
#  ON DELETE CASCADE
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# INSERT INTO Wishlists_edit VALUES (1,2,1);
# INSERT INTO Wishlists_edit VALUES (2,4,1);
# INSERT INTO Wishlists_edit VALUES (3,6,1);
# INSERT INTO Wishlists_edit VALUES (4,7,2);
# INSERT INTO Wishlists_edit VALUES (5,5,1);
# INSERT INTO Wishlists_edit VALUES (6,3,1);
# INSERT INTO Wishlists_edit VALUES (7,8,4);
# INSERT INTO Wishlists_edit VALUES (8,4,1);
# INSERT INTO Wishlists_edit VALUES (9,8,6);
# INSERT INTO Wishlists_edit VALUES (10,1,1);

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM Wishlists_edit

# Commented out IPython magic to ensure Python compatibility.
# %sql drop table link

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE link
# (
#  wishlist_id int REFERENCES Wishlists_edit(wishlist_id),
#  merchant_id int REFERENCES Merchants(merchant_id),
#  PRIMARY KEY (wishlist_id, merchant_id)
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# INSERT INTO link VALUES (1,1);
# INSERT INTO link VALUES (2,2);
# INSERT INTO link VALUES (3,3);
# INSERT INTO link VALUES (4,4);
# INSERT INTO link VALUES (5,5);
# INSERT INTO link VALUES (6,6);
# INSERT INTO link VALUES (7,7);
# INSERT INTO link VALUES (8,8);
# INSERT INTO link VALUES (9,9);
# INSERT INTO link VALUES (10,10);

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM link

# Commented out IPython magic to ensure Python compatibility.
# %sql drop table Comments_edit_write

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE Comments_edit_write
# (
#  comment_id int UNIQUE NOT NULL,
#  user_id int,
#  merchant_id int,
#  rating int CHECK(rating>=0 and rating<=100),
#  content text,
#  picture text,
#  PRIMARY KEY (comment_id, user_id, merchant_id),
#  FOREIGN KEY (user_id) REFERENCES Users
#  ON DELETE CASCADE,
#  FOREIGN KEY (merchant_id) REFERENCES Merchants
#  ON DELETE CASCADE
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# INSERT INTO Comments_edit_write VALUES (1,1,1,43,'stunning food','1.png');
# INSERT INTO Comments_edit_write VALUES (2,2,1,54,'niiiiice','1.png');
# INSERT INTO Comments_edit_write VALUES (3,3,10,43,'went for brunch','1.png');
# INSERT INTO Comments_edit_write VALUES (4,4,1,65,'would give 5 stars','1.png');
# INSERT INTO Comments_edit_write VALUES (5,5,1,43,'My boy friend LOVES it','1.png');
# INSERT INTO Comments_edit_write VALUES (6,6,2,87,'Great value for the tasting menu','1.png');
# INSERT INTO Comments_edit_write VALUES (7,7,1,14,'went for Happy hours','1.png');
# INSERT INTO Comments_edit_write VALUES (8,8,3,45,'Definitely would come again','1.png');
# INSERT INTO Comments_edit_write VALUES (9,9,1,76,'If I could give this place 0 star I would.','1.png');
# INSERT INTO Comments_edit_write VALUES (10,10,1,43,'Pet friendly!','1.png');

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM Comments_edit_write

# Commented out IPython magic to ensure Python compatibility.
# %sql drop table Orders_make_send

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE Orders_make_send
# (
#  order_id int,
#  user_id int,
#  merchant_id int,
#  date date,
#  price float CHECK(price>0),
#  PRIMARY KEY (order_id, user_id, merchant_id),
#  FOREIGN KEY (user_id) REFERENCES Users
#  ON DELETE CASCADE,
#  FOREIGN KEY (merchant_id) REFERENCES Merchants
#  ON DELETE CASCADE
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# INSERT INTO Orders_make_send VALUES (1,10,8,'2021-11-01',20.4);
# INSERT INTO Orders_make_send VALUES (2,9,9,'2022-03-23',50);
# INSERT INTO Orders_make_send VALUES (3,8,5,'2020-12-18',33);
# INSERT INTO Orders_make_send VALUES (4,7,7,'2021-06-06',117);
# INSERT INTO Orders_make_send VALUES (5,6,4,'2022-02-08',23.8);
# INSERT INTO Orders_make_send VALUES (6,5,1,'2022-02-06',62);
# INSERT INTO Orders_make_send VALUES (7,4,10,'2019-08-27',77);
# INSERT INTO Orders_make_send VALUES (8,3,3,'2022-02-14',16);
# INSERT INTO Orders_make_send VALUES (9,2,6,'2019-12-24',17.9);
# INSERT INTO Orders_make_send VALUES (10,1,2,'2020-01-01',21);

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM Orders_make_send

# Commented out IPython magic to ensure Python compatibility.
# %sql drop table Posts_edit

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE Posts_edit
# (
#  post_id int UNIQUE NOT NULL,
#  user_id int,
#  content text,
#  likes int CHECK(likes>=0),
#  PRIMARY KEY (post_id, user_id),
#  FOREIGN KEY (user_id) REFERENCES Users
#  ON DELETE CASCADE
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# INSERT INTO Posts_edit VALUES (1,10,'Amazing',20);
# INSERT INTO Posts_edit VALUES (2,9,'Tastes great',5);
# INSERT INTO Posts_edit VALUES (3,8,'Would come again',33);
# INSERT INTO Posts_edit VALUES (4,7,'Great value',11);
# INSERT INTO Posts_edit VALUES (5,6,'Worth the price',23);
# INSERT INTO Posts_edit VALUES (6,5,'Perfect for dating',2);
# INSERT INTO Posts_edit VALUES (7,4,'Nice decoration',0);
# INSERT INTO Posts_edit VALUES (8,3,'Great value',6);
# INSERT INTO Posts_edit VALUES (9,2,'Places for dinging outdoors',17);
# INSERT INTO Posts_edit VALUES (10,1,'Great menu to explore',21);

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM Posts_edit

# Commented out IPython magic to ensure Python compatibility.
# %sql drop table tag

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# CREATE TABLE Tag
# (
#  post_id int REFERENCES Posts_edit(post_id),
#  merchant_id int REFERENCES Merchants(merchant_id),
#  PRIMARY KEY (post_id,merchant_id)
# );

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# INSERT INTO Tag VALUES (1,1);
# INSERT INTO Tag VALUES (1,2);
# INSERT INTO Tag VALUES (1,3);
# INSERT INTO Tag VALUES (1,4);
# INSERT INTO Tag VALUES (2,5);
# INSERT INTO Tag VALUES (3,1);
# INSERT INTO Tag VALUES (4,1);
# INSERT INTO Tag VALUES (5,1);
# INSERT INTO Tag VALUES (6,1);
# INSERT INTO Tag VALUES (7,1);

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM Tag

"""SELECT PART"""

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# SELECT U.user_id
# FROM Users U, Posts_edit P
# WHERE U.user_id=P.user_id and P.likes>3

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# SELECT O.merchant_id, COUNT(*) AS total_orders
# FROM Orders_make_send O, Merchants M
# WHERE O.merchant_id = M.merchant_id
# GROUP BY O.merchant_id
# HAVING COUNT(*) > 0

# Commented out IPython magic to ensure Python compatibility.
# %%sql 
# SELECT U.user_id
# FROM Users U CROSS JOIN Posts_edit P
# WHERE U.user_id=P.user_id
# GROUP BY U.user_id
# HAVING COUNT(*)>0
#