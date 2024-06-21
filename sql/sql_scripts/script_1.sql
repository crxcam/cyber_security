/* DB

create database formation;
-- show databases
show databases;
-- use 'database_name'
select database()  //  determine db currant
-- if not exists
-- show create database formation;

show full tables;
*/

/* TABLES
---- create
CREATE TABLE `formation`.`person` (
id int primary key NOT NULL AUTO_INCREMENT,
nom  varchar(50),
prenom  varchar(50),
sex  varchar(1) constraint check_genre check (genre ='H' or genre = 'F' ),

);
CREATE TABLE `formation`.`vehicule` (
id int primary key NOT NULL AUTO_INCREMENT,
marque  varchar(30),
couleur  varchar(30),
id_proprietaire  int,
constraint fk_person foreign key references person(id)
);
-- rename
rename TABLE `formation`.`person` TO  `persone`;
ALTER TABLE `formation`.`persone` rename   `person`;

-- show 
show full tables;	
-- show description
describe person;  
explain person;
show full columns from person;
show create table person;


*/

/* COLUMN
alter table person
add column gendre varchar(10);
-----
alter table person
add column profession varchar(10) after prenom;
-----
alter table person
add column profession varchar(10) first;
-----
alter table person
drop column profession;
-----
alter table person
rename column gendre to sex;
-----
alter table person
modify column sex varchar(20);
*/

/* CONTRAINTS
alter table person
alter column sex  set default 'Doe';

alter table person
alter column sex  drop default ;

---- unique
alter table person
add constraint unique_nom unique (nom) ;

alter table person
drop constraint unique_nom  ;

alter table vehicule
add constraint fk_vehicule_person foreign key (id_proprietaire)
references person  ;

alter table vehicule
drop constraint fk_vehicule_person ;

alter table vehicule
add constraint fk_vehicule_person foreign key (id_proprietaire)
references person(id)  ;
-----
alter table vehicule
drop key fk_vehicule_person ;
-----
-- supprimer primary key avec AUTO_INCREMENT
alter table vehicule
drop primary key,
modify id int;

-- ajouter AUTO_INCREMENT
alter table vehicule
modify id int AUTO_INCREMENT ;

-- ajouter CHECK
alter table vehicule
add column anne int check (anne > 1990);

-- ajouter check 
alter table person
add constraint check_genre check (genre ='H' or genre = 'F' );

-- supprimer check
alter table person
drop check check_genre;

*/






















