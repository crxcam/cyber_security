create or replace  view view_person as
select *
from cours_lid.personne  ;


create or replace  view view_vehicule as
select *
from cours_lid.vehicule ;

select 
v_persone.nom,
v_persone.prenom,
count(*) as 'nombre_vehicule'
from formation.view_person as v_persone
inner JOIN formation.view_vehicule as v_vhl ON v_vhl.nump = v_persone.num
group by v_persone.nom,v_persone.prenom;

#with check option

delimiter |
create procedure augmenter_salaire(somme int)
begin
declare id int;
select num  INTO id from cours_lid.personne as persone
where persone.salaire =(select min(salaire) from persone);
update person set  salaire = salaire + somme 
where num = id;
end |
delimiter ;




