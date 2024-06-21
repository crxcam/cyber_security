from src.models.trois_points import TroisPoints
from src.models.point import Point


# creation object adreee 
# tester acces 
# ajout attribut addresse a la classe Personne 
# creation de prsonne avec adresse 
# test acess

point1 =  Point(1.23,5.32)
point2 =  Point(1.05,5.21)
print("###### object point1 : ",point1)
print("###### object point2 : ",point2)
print("###### point.calc_distance : ",point1.calc_distance(point2))
print("###### point.calc_milieu : ",point1.calc_milieu(point2))

trois_points =  TroisPoints(Point(0.23,1.32),Point(0.23,2.32),Point(0.23,8.32))

print("###### trois_points._une : ",trois_points._une)
print("###### sont_alignes : ",trois_points.sont_alignes())


