drop table if exists diseases;
create table diseases (
    id_disease int unsigned not null auto_increment,
    primary key (id_disease),
    name varchar(255)
);

drop table if exists symptoms;
create table symptoms (
    id_symptom int unsigned not null auto_increment,
    primary key (id_symptom),
    name varchar(255)
);

drop table if exists rules;
create table rules (
    id_rule int unsigned not null auto_increment,
    primary key (id_rule),
    id_disease int unsigned not null,
    foreign key (id_disease) references diseases(id_disease),
    id_symptom int unsigned not null,
    foreign key (id_symptom) references symptoms(id_symptom),
    cf int unsigned not null
);
