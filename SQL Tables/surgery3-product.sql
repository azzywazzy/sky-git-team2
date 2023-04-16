USE Surgery;

CREATE TABLE product(
	product_id smallint not null primary key auto_increment,
    prod_cost smallint not null,
    prod_category varchar(50) not null,
    prod_name varchar(150) not null,
    prod_description text,
    prod_image varchar(255),
    prod_species varchar(50) not null,
    quantity_available smallint not null
)
