insert into diseases values(1, 'Viroză respiratorie');
insert into diseases values(2, 'Amigdalită');
insert into diseases values(3, 'Pneumonie');

insert into simptoms values(1, 'Tuse');
insert into simptoms values(2, 'Durere în gât');
insert into simptoms values(3, 'Amigdale inflamate');
insert into simptoms values(4, 'Durere în piept');
insert into simptoms values(5, 'Febră');
insert into simptoms values(6, 'Congestie nazală');
insert into simptoms values(7, 'Dificultate la înghițire');
insert into simptoms values(8, 'Durere de cap');
insert into simptoms values(9, 'Strănut');
insert into simptoms values(10, 'Frisoane');


insert into rules values(null, 1, 1, cf);
insert into rules values(null, 1, 5, cf);
insert into rules values(null, 1, 6, cf);
insert into rules values(null, 1, 8, cf);
insert into rules values(null, 1, 9, cf);
insert into rules values(null, 1, 10, cf);

insert into rules values(null, 2, 2, cf);
insert into rules values(null, 2, 3, cf);
insert into rules values(null, 2, 5, cf);
insert into rules values(null, 2, 7, cf);
insert into rules values(null, 2, 9, cf);
insert into rules values(null, 2, 10, cf);

insert into rules values(null, 3, 1, cf);
insert into rules values(null, 3, 4, cf);
insert into rules values(null, 3, 5, cf);
insert into rules values(null, 3, 6, cf);
insert into rules values(null, 3, 9, cf);
insert into rules values(null, 3, 10, cf);
