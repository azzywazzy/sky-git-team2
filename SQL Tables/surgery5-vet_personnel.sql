USE Surgery;

CREATE TABLE vet_personnel(
	vet_id smallint not null primary key auto_increment,
    vet_first_name varchar(50) not null,
    vet_last_name varchar(50) not null,
    vet_department varchar(50),
    vet_role varchar(50)
)