USE Surgery;

CREATE TABLE order_history(
	order_id smallint not null primary key auto_increment,
    product_id smallint not null,
    cus_id smallint not null,
    quantity_ordered smallint not null,
    order_date date not null,
    collected smallint,
    collection_date date,    
	foreign key (product_id) references product(product_id) on delete cascade,
	foreign key (cus_id) references customer(cus_id) on delete cascade
)