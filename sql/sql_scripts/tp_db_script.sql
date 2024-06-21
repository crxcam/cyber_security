create database tp_location;

use tp_location;

create table habitation(
    code_habitation int primary key,
    type_habitation char(10) check(
        type_habitation in (
            'TYPE1',
            'TYPE2',
            'TYPE3',
            'TYPE4',
            'TYPE5',
            'VILLA'
        )
    ),
    adresse char(32),
    ville char(32),
    loyer_mensuel real
);

create table client(
    id_client int primary key,
    nom char(32),
    profession char(32)
);

create table location(
    code_habitation int,
    id_client int,
    nombre_mois int,
    primary key (code_habitation, id_client)
);

alter table
    location
add
    constraint fk_location_client foreign key (id_client) references client(id_client);

alter table
    location
add
    constraint fk_location_habitation foreign key (code_habitation) references habitation(code_habitation);

insert into
    habitation
values
    (
        120,
        'TYPE3',
        'Bd. Charles de Gaulle 1',
        'Avignon',
        750
    );

insert into
    habitation
values
    (
        123,
        'TYPE1',
        'Bd. Charles de Gaulle 89',
        'Lyon',
        650
    );

insert into
    habitation
values
    (
        112,
        'TYPE1',
        'Av. de la Foret 26',
        'Grenoble',
        400.00
    );

insert into
    habitation
values
    (
        513,
        'TYPE2',
        'R. d Espagne 24',
        'Marseille',
        600
    );

insert into
    habitation
values
    (
        618,
        'TYPE2',
        'R. Flaubert 24',
        'Toulouse',
        400
    );

insert into
    habitation
values
    (
        184,
        'TYPE2',
        'Rue de Paris 118',
        'Toulouse',
        600
    );

insert into
    habitation
values
    (
        113,
        'TYPE3',
        'Av. de la Foret 26',
        'Grenoble',
        800
    );

insert into
    habitation
values
    (456, 'TYPE3', 'RUE MARTIGUES', 'Lyon', 1200);

insert into
    habitation
values
    (
        678,
        'TYPE3',
        'R. de la Republique 45',
        'Nice',
        1000.00
    );

insert into
    habitation
values
    (
        694,
        'TYPE3',
        'R. Cassis 67',
        'Marseille',
        900
    );

insert into
    habitation
values
    (
        812,
        'TYPE3',
        'Bd. Des Platans 134',
        'Paris',
        1000.00
    );

insert into
    habitation
values
    (
        331,
        'TYPE3',
        'R. d Italie 11',
        'Nancy',
        500.00
    );

insert into
    habitation
values
    (
        392,
        'TYPE3',
        'Bd. de la Bastille 63',
        'Nantes',
        700.00
    );

insert into
    habitation
values
    (
        675,
        'TYPE4',
        'Av de la Poste 43',
        'Avignon',
        800.00
    );

insert into
    habitation
values
    (
        517,
        'TYPE4',
        'R. d Espagne 24',
        'Marseille',
        900.00
    );

insert into
    habitation
values
    (
        752,
        'TYPE4',
        'Bd. Des Platans 78',
        'Paris',
        1200.00
    );

insert into
    habitation
values
    (
        667,
        'TYPE4',
        'Av de la Poste 89',
        'Avignon',
        700.00
    );

insert into
    habitation
values
    (
        332,
        'TYPE5',
        'R. d Italie 11',
        'Nancy',
        1000.00
    );

insert into
    habitation
values
    (
        679,
        'TYPE5',
        'Bd de la Poste 43',
        'Lyon',
        1100.00
    );

insert into
    habitation
values
    (
        789,
        'TYPE5',
        'R. Cassis 130',
        'Marseille',
        1400.00
    );

insert into
    habitation
values
    (
        561,
        'TYPE5',
        'Rue Mandeville 34',
        'Nantes',
        1100.00
    );

insert into
    habitation
values
    (
        912,
        'VILLA',
        'R. de la Republique 13',
        'Nice',
        1700.00
    );

insert into
    habitation
values
    (
        169,
        'VILLA',
        'Rue de Paris 118',
        'Toulouse',
        1300.00
    );

insert into
    habitation
values
    (
        699,
        'VILLA',
        'R. Cassis 71',
        'Marseille',
        1500.00
    );

insert into
    habitation
values
    (
        276,
        'VILLA',
        'Av. de la Republique 54',
        'Paris',
        1400.00
    );

insert into
    habitation
values
    (
        964,
        'VILLA',
        'Rue Verlain 40',
        'Chambery',
        2000.00
    );

insert into
    habitation
values
    (
        900,
        'TYPE4',
        'St Marguerite 9',
        'Marseille',
        1200.00
    );

insert into
    client
values
    (1, 'Bonnard',  'Cadre'),
    (2, 'Canat',  'SecrÃ©taire'),
    (3, 'Damien',  'Enseignant'),
    (4, 'Dupont',  'CommerÃ§ant'),
    (5, 'Durand',  'CommerÃ§ant'),
    (6, 'Flaubert',  'Enseignant'),
    (7, 'Florant',  'Cadre'),
    (8, 'Florentin',  'CommerÃ§ant'),
    (9, 'Leonard',  'Entrepreneur'),
    (10, 'Martini',  'SecrÃ©taire'),
    (11, 'Siegel',  'Cadre'),
    (12, 'Torres',  'IngÃ©nieur'),
    (13, 'Valdes',  'IngÃ©nieur'),
    (14, 'Smith',  'Enseignant'),
    (15, 'Laurent',  'Cadre');

insert into
    location
values
    (113, 5, 8),
    (561, 7, 12),
    (123, 6, 7),
    (123, 11, 5),
    (123, 13, 7),
    (517, 4, 4),
    (678, 9, 9),
    (618, 9, 15),
    (184, 1, 10),
    (184, 7, 11),
    (392, 2, 16),
    (392, 6, 20),
    (699, 12, 19),
    (112, 8, 7),
    (112, 10, 4),
    (332, 2, 5),
    (812, 10, 7),
    (276, 11, 5),
    (169, 13, 3),
    (169, 14, 5);