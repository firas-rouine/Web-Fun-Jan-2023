SELECT * FROM users.users;
insert into users(first_name,last_name,email) values("ahmed","sassi","dsdd@gmail.com");
insert into users(first_name,last_name,email)
        values (%(first_name)s,%(last_name)s,%(email)s);