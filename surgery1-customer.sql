CREATE Database Surgery;
USE Surgery;

CREATE TABLE customer(
	cus_id smallint not null primary key auto_increment,
    cus_first_name varchar(50) not null,
    cus_last_name varchar(50) not null,
    cus_email varchar(50) not null,
    address varchar(255) not null,
    phone char(11) not null,
    cus_status tinyint
)
