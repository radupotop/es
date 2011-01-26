drop table if exists rules;
create table rules (
    id_rule int unsigned not null auto_increment,
    primary key (id_rule),
    title varchar(255)
);

drop table if exists users;
create table users (
    id_user int unsigned not null auto_increment,
    primary key (id_user),
    id_group int unsigned not null,
    foreign key (id_group) references groups(id_group),
    first_name varchar(255),
    fam_name varchar(255),
    email varchar(255),
    unique key (email),
    pass varchar(255),
    about text
);
