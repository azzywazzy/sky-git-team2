use surgery;

CREATE TABLE credential(
cred_id smallint not null primary key auto_increment,
email varchar(50) not null,
user_type tinyint not null, 
hash_password varchar(50) not null
)



