-- create user 'guest' for general public wanting to browse products and staff and sign up as a customer
create user 'guest'@'localhost' identified by 'password';
grant select on surgery.product to 'guest'@'localhost';
grant select on surgery.vet_personnel to 'guest'@'localhost';
grant insert on surgery.customer to 'guest'@'localhost';

-- create user 'customer' for logged in user to view tables, update customer details and add new patient 
create user 'customer'@'localhost' identified by 'password';
grant select on surgery.* to 'customer'@'localhost';
grant update on surgery.customer to 'customer'@'localhost';
grant insert on surgery.patient to 'customer'@'localhost';

-- create user 'admin' to view, update and insert all and to delete existing customer or patient.
create user 'admin'@'localhost' identified by 'password';
grant select on surgery.* to 'admin'@'localhost';
grant insert on surgery.* to 'admin'@'localhost';
grant update on surgery.* to 'admin'@'localhost';
grant delete on surgery.customer to 'admin'@'localhost';
grant delete on surgery.patient to 'admin'@'localhost';