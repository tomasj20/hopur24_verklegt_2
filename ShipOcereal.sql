CREATE TABLE Product (
	productID serial PRIMARY KEY,
	productname varchar(255),
	inStock boolean NOT NULL,
	producer varchar(255),
	price smallint,
	category varchar(255)
);

CREATE TABLE User (
	userID serial PRIMARY KEY,
	username varchar(255) UNIQUE,
	firstname varchar(255),
	lastname varchar(255),
	address varchar(255) not NULL,
	password VARCHAR(255) DEFAULT '[REDACTED]',
	email varchar(355) UNIQUE,
	cartID references CART (cartID)
);

CREATE TABLE Admin (
	adminID serial PRIMARY KEY,
	isAdmin boolean NOT NULL,
	userID int References User (userID) /* Is A*/
);

CREATE TABLE Cart (
	cartID serial PRIMARY KEY,
	productCount INT NOT NULL DEFAULT 0,
	productID references Products (productID)
	userID references user (UserID)
);

CREATE TABLE Order (
	orderID serial PRIMARY KEY,
	totalPrice int NOT NULL DEFAULT 0,
	shipmentDetails varchar (255),
	productID references PRODUCT (productID),
	userID references USER(userID)	
);
