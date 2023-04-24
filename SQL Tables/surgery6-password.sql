use Surgery;

CREATE TABLE credential(
id smallint not null primary key auto_increment,
email varchar(50) not null,
user_type tinyint not null, 
hash_password varchar(100) not null
);

insert into credential values (1, "MRauk@vets.com", "1", "lkjsalkj7;lkj;klj;aljj9");
insert into credential values (2, "PJames@vets.com", "1", "lksdj;lgkajsd908olijdsf");
insert into credential values (3, "MRai@vets.com", "1", "ldskjf;l89sdfskhj");
insert into credential values (4, "fayequinn@email.com", "0", ";lksaf;lakopim;gd;l");


<<<<<<< Updated upstream
drop table credential;

=======
Select * from credential;
Select * from customer
>>>>>>> Stashed changes
