
delimiter |
create function puissance(x int, y int)
returns int
begin
declare resultat int;
declare compteur int;
set compteur = 1;
set resultat =1;
while compteur <= y do
set resultat = resultat * x;
set compteur = compteur + 1;
end while;
return resultat;
end
|
delimiter ;

select puissance(2,3)

#SET GLOBAL log_bin_trust_function_creators = 1