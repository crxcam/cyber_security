/*
delimiter |
create procedure augmenter_salaire(somme int)
begin
declare id int;
select num  INTO id from cours_lid.personne 
where cours_lid.personne.salaire =(select min(salaire) from cours_lid.personne);
update cours_lid.personne set  salaire = salaire + somme 
where num = id;
end |
delimiter ;

call augmenter_salaire(200)
*/

delimiter |
create procedure augmenter_salaire_min(somme int)
begin
declare id int;
declare smic int default 1400;
declare salaire_min int default 1400;
select min(salaire) into salaire_min from cours_lid.personne;
select num into id from cours_lid.personne where salaire = salaire_min limit 1;

if salaire_min < smic then
update cours_lid.personne set salaire = smic +somme where num = id;
else
update cours_lid.personne set salaire = salaire +somme where num = id;
end if;

end |
delimiter ;

call augmenter_salaire_min(100)
