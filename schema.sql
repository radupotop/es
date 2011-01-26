drop table if exists simptoms;
create table simptoms (
    id_simptom int unsigned not null auto_increment,
    primary key (id_simptom),
    name varchar(255)
);

drop table if exists diseases;
create table diseases (
    id_disease int unsigned not null auto_increment,
    primary key (id_disease),
    name varchar(255)
);

drop table if exists rules;
create table rules (
    id_rule int unsigned not null auto_increment,
    primary key (id_rule),
    id_simptom int unsigned not null,
    foreign key (id_simptom) references simptoms(id_simptom),
    id_disease int unsigned not null,
    foreign key (id_disease) references diseases(id_disease),
    cf int unsigned not null
);

drop table if exists facts;
create table facts (
    id_fact int unsigned not null auto_increment,
    primary key (id_fact),
    id_rule int unsigned not null,
    foreign key (id_rule) references rules(id_rule)
);
