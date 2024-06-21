# ex:1
select 

habitation.type_habitation,
habitation.adresse,
habitation.ville,
habitation.loyer_mensuel

from tp_location.habitation as habitation
where tp_location.habitation.ville ='marseille';

# ex:2

select 
habitation.ville,
count(*) as 'nombre'
from tp_location.habitation as habitation
group by habitation.ville;


# ex:3
select 
clients.nom,
count(*) as 'nombre_location'
from tp_location.location as location
inner JOIN tp_location.habitation as habitation ON habitation.code_habitation = location.code_habitation
inner JOIN tp_location.client as clients ON clients.id_client = location.id_client
group by location.id_client
ORDER BY clients.nom;





# ex:4
/*
 Pour chaque habitation, affichez son code, son type, la ville o`u elle se trouve, les noms des
locataires et leurs professions.
 */
select 
habitation.code_habitation,
habitation.type_habitation,
habitation.ville,
clients.nom,
clients.profession
from tp_location.location as location
inner JOIN tp_location.habitation as habitation ON habitation.code_habitation = location.code_habitation
inner JOIN tp_location.client as clients ON clients.id_client = location.id_client
ORDER BY habitation.code_habitation;

# ex:5
/*. Trouvez les clients qui n’ont jamais lou´e aucune habitation.*/
select 
clients.nom
from tp_location.client as clients
left JOIN tp_location.location as location ON location.id_client = clients.id_client
where location.nombre_mois is null;

# ex:6
/*. Reprenez la question 4 mais affichez aussi les habitations qui n’ont jamais ´et´e lou´ees.*/
select 
habitation.code_habitation,
habitation.type_habitation,
habitation.ville,
clients.nom,
clients.profession
from tp_location.habitation as habitation
left JOIN tp_location.location as location ON location.code_habitation = habitation.code_habitation
left JOIN tp_location.client as clients ON clients.id_client = location.id_client
ORDER BY clients.nom;

# ex:7
/* . D´eterminez les minimum, maximum et moyenne de loyer des habitations pour chaque type et
chaque ville.*/

select 
habitation.ville,
habitation.type_habitation,
min(habitation.loyer_mensuel) as 'min',
max(habitation.loyer_mensuel) as 'max',
avg(habitation.loyer_mensuel) as 'moyen'
from tp_location.habitation as habitation
group by habitation.type_habitation,habitation.ville
ORDER BY habitation.ville;


# ex:8
/*  Pour chaque type d’habitation, d´eterminez le nombre d’habitations de ce type qui ont ´et´e prises
en location*/

select 
habitation.type_habitation,
count(location.nombre_mois) as 'nombre_location'
from tp_location.habitation as habitation
left JOIN tp_location.location as location ON location.code_habitation = habitation.code_habitation
group by habitation.type_habitation
ORDER BY habitation.type_habitation;

# ex:9

select 
habitation.type_habitation,
count(location.nombre_mois) as 'nombre_location' 
from tp_location.habitation as habitation
left JOIN tp_location.location as location ON location.code_habitation = habitation.code_habitation
group by habitation.type_habitation
having count(location.nombre_mois) > 3
ORDER BY habitation.type_habitation;


# ex:10
/*	. D´eterminez le nombre total des mois de location de chaque habitation. Facultatif : pour celles
qui n’ont jamais ´et´e lou´ees, affichez la valeur 0 (utilisez la fonction ifnull).
*/
select 
habitation.type_habitation,
habitation.code_habitation,
sum(IFNULL(location.nombre_mois, 0)) as 'nombre_mois_total'
from tp_location.habitation as habitation
left JOIN tp_location.location as location ON location.code_habitation = habitation.code_habitation
group by habitation.type_habitation,habitation.code_habitation
ORDER BY habitation.type_habitation;

# ex:11
/*	 Pour chaque client, calculez ses frais totaux de loyer*/
select 
clients.nom,
sum(habitation.loyer_mensuel * location.nombre_mois ) as 'total'
from tp_location.habitation as habitation
left JOIN tp_location.location as location ON location.code_habitation = habitation.code_habitation
left JOIN tp_location.client as clients ON clients.id_client = location.id_client
where clients.nom is not null
group by clients.nom
ORDER BY clients.nom;

# ex:12
/*	  
Trouvez les clients qui ont lou´e `a la fois des appartements de type 1 et des appartements de
type 3. (Utilisez exists).

*/
select 
clients.nom
from tp_location.habitation as habitation
left JOIN tp_location.location as location ON location.code_habitation = habitation.code_habitation
left JOIN tp_location.client as clients ON clients.id_client = location.id_client
 where habitation.type_habitation = 'TYPE1'
 and nom in(
 select 
nom
from tp_location.habitation as habitation1
left JOIN tp_location.location as location1 ON location.code_habitation = habitation.code_habitation
left JOIN tp_location.client as clients1 ON clients.id_client = location.id_client
where habitation.code_habitation = habitation1.code_habitation
and clients.id_client = clients1.id_client
and habitation.type_habitation = 'TYPE3'
 )





