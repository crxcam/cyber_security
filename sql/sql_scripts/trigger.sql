delimiter |
create trigger set_ville_marseille before insert on cours_lid.personne
for each row
begin
if new.ville is null then 
set new.ville = 'Marseille';
end if;
end
|
delimiter ;


delimiter |
create trigger check_augment_salaire before update on cours_lid.personne
for each row
begin

if new.salaire  - old.salaire >= 200 then 
set new.salaire = old.salaire;
end if;
end
|
delimiter ;



insert into cours_lid.personne (num,nom,prenom,salaire) values (10,'ragnar','lothbrok',1500)