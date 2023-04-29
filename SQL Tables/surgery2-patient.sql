USE Surgery;

CREATE TABLE patient(
	pat_id smallint not null primary key auto_increment,
    cus_id smallint not null,
    pat_name varchar(50) not null,
    species varchar(50) not null,
    breed varchar(50),
    sex char(1),
    date_of_birth date,
    weight int,
    chip_num varchar(50),
    neutered_status tinyint,
    has_insurance tinyint,
    foreign key (cus_id) references customer(cus_id) on delete cascade
);


