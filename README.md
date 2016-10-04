# stock_search toy system
This is a small stock search system. People can search the price of the stock that is in the database or add a new record of a stock.
When you click into the search page and type the stock name that you want to find information of, then the website will show the result of that stock. 
Also, we can add a new record of the stock(name, price) into the database.

The database we used is MYSQL running on the localhost.

Schema of the database called "stock":

CREATE TABLE new_table
(
    Name varchar(45) NOT NULL,
    Price int(11),
    Primary Key(Name)
)


