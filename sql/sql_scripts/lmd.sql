/* 
CREATE TABLE `formation`.`person` (
id int primary key NOT NULL AUTO_INCREMENT,
nom  varchar(50),
prenom  varchar(50),
genre  varchar(1)
);

alter table person
add constraint check_genre check (genre ='H' or genre = 'F' );

INSERT INTO `person` 
 (`nom`, `prenom`,`genre`) VALUES ('Mcartney', 'paul','h');
 
 update `person` 
 set  `prenom` = 'michel'
 where `id` =1;

replace into  `person`
set
nom = 'Denzel',
prenom='Washington';

 update `person` 
 set  `genre` = 'h'
 where `id` = 2
 */
 /*
 -----
 CREATE database cours_lid;
use cours_lid;
CREATE TABLE personne (
num int(3) PRIMARY KEY,
nom varchar(20),
prenom varchar(20),
salaire int(4),
ville varchar(20)
)ENGINE=InnoDB;
CREATE TABLE vehicule (
immatriculation int(3) PRIMARY KEY,
marque varchar(20),
modele varchar(20),
annee int(4),
nump int(3),
CONSTRAINT fk_vehicule_personne FOREIGN KEY (nump) REFERENCES
personne(num)
)ENGINE=InnoDB;

INSERT INTO personne VALUES
(1, 'Cohen', 'Sophie', 2000, 'Marseille'),
(2, 'Leberre', 'Bernard', 1500, 'Marseille'),
(3, 'Benamar', 'Pierre', 1800, 'Lyon'),
(4, 'Hadad', 'Karim', 2500, 'Paris'),
(5, 'Wick', 'John', 3000, 'Paris');
INSERT INTO vehicule VALUES
(100, 'Peugeot', '5008', 2018, 5),
(200, 'Renault', 'clio', 2000, 4),
(300, 'Ford', 'fiesta', 2010, 1),
(400, 'Peugeot', '106', 2002, 3),
(500, 'Citroen', 'C4', 2015, 4),
(600, 'Ford', 'Kuga', 2019, null),
(700, 'Fiat', 'punto', 2008, 5);
*/
/*
SELECT * FROM cours_lid.personne
where ville = 'marseille'
or ville = 'lyon';

SELECT * FROM cours_lid.personne
WHERE salaire BETWEEN 1800 AND 2800;

SELECT * FROM cours_lid.personne
WHERE ville = 'marseille'
and  salaire not BETWEEN 1800 AND 2800;

SELECT * FROM cours_lid.personne
WHERE ville LIKE '%ma%';

SELECT * FROM cours_lid.vehicule
WHERE nump is not null;

SELECT marque,ifnull(nump, 'non affecté') as proprio FROM cours_lid.vehicule

select nump,count(*)
FROM cours_lid.vehicule
group by nump

select nump,count(*) as nombre
FROM cours_lid.vehicule
group by nump
having nombre > 0

select ville,SUM(salaire) as 'somme de salaire'
from cours_lid.personne
group by ville

select cours_lid.personne.num,cours_lid.vehicule.marque
from cours_lid.personne
INNER JOIN cours_lid.vehicule ON cours_lid.vehicule.nump = cours_lid.personne.num
where cours_lid.vehicule.marque = 'renault' 
and cours_lid.vehicule.marque = 'citroen' 

*/
/*
select 
personne.num as 'numero de la personne' ,
personne.nom ,
personne.prenom ,
personne.salaire ,
personne.ville ,
vehicule.marque , 
vehicule.modele ,
vehicule.immatriculation 
from cours_lid.personne as  personne
LEFT JOIN cours_lid.vehicule as vehicule ON vehicule.nump = personne.num
where vehicule.marque is not null;


----- requette imbriqué
select  nump
from cours_lid.vehicule as vehicule
where vehicule.marque = 'fiat'
and  nump in (select nump from cours_lid.vehicule where cours_lid.vehicule.marque ='peugeot' );

select  nump
from cours_lid.vehicule as vehicule
where vehicule.marque = 'fiat'
and  nump = any (select nump from cours_lid.vehicule where cours_lid.vehicule.marque ='peugeot' );

select  nump
from cours_lid.vehicule as vehicule
where vehicule.marque = 'fiat'
and  exists (
select nump from cours_lid.vehicule
 where cours_lid.vehicule.marque ='peugeot'
and vehicule.nump = null
 );
 
 
 select 
personne.num as 'numero de la personne' ,
personne.nom ,
personne.prenom ,
personne.salaire ,
personne.ville ,
vehicule.marque , 
vehicule.modele ,
vehicule.immatriculation 
from cours_lid.personne as  personne

LEFT JOIN cours_lid.vehicule as vehicule ON vehicule.nump = personne.num
where (select count(*) from cours_lid.vehicule where cours_lid.vehicule.immatriculation is not null) > 1;

 select 
personne.nom ,personne.prenom
from cours_lid.personne as  personne , cours_lid.vehicule as vehicule
group by personne.num
having count(*) > 1;

 select 
vehicule.marque 
from cours_lid.personne as  personne
left JOIN cours_lid.vehicule as vehicule ON vehicule.nump = personne.num
where personne.ville = 'paris'
and personne.ville = 'lyon';

 select 
count(personne.num), personne.nom
from cours_lid.personne as  personne
inner JOIN cours_lid.vehicule as vehicule ON vehicule.nump = personne.num
group by personne.num
having count(*) >= all 
(select count(*)  from cours_lid.vehicule group by vehicule.nump )


*/

select  max(salaire)
into @salaire
from cours_lid.personne;

select @salaire


























