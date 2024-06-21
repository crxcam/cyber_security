La notation **O** (grande O), aussi appelée notation de Landau ou notation asymptotique, est une notation mathématique utilisée principalement pour décrire la complexité algorithmique dans le domaine de l'informatique. Elle permet d'exprimer la croissance des ressources nécessaires (temps d'exécution ou espace mémoire) par rapport à la taille de l'entrée d'un algorithme, en ne tenant compte que du terme le plus significatif et en ignorant les coefficients constants et les termes de moindre importance. Cette notation est cruciale pour l'analyse des algorithmes et aide à comprendre leur efficacité lorsque la taille des données traitées devient très grande.

### Définition de la Notation O

Formellement, on dit que **f(n) = O(g(n))** si et seulement s'il existe des constantes positives **C** et **n0** telles que pour tout **n ≥ n0**, l'inégalité **|f(n)| ≤ C \* |g(n)|** est satisfaite. Ici, **f(n)** représente la complexité de l'algorithme et **g(n)** une fonction qui décrit une limite supérieure de cette complexité.

### Exemples de Calcul avec la Notation O

1. **Exemple simple** :
   - Considérons la fonction **f(n) = 6n² + 15n + 40**.
   - À mesure que **n** devient grand, le terme **6n²** devient le plus dominant car il croît plus vite que les autres termes.
   - Nous pouvons simplifier cette expression en utilisant la notation O pour indiquer que **f(n) = O(n²)**. Cela signifie que la croissance de **f(n)** est au plus quadratique par rapport à **n**.

2. **Exemple avec des algorithmes** : 
   - **Recherche linéaire dans un tableau**: Le pire cas se produit lorsque l'élément recherché est à la dernière position du tableau ou n'est pas présent. Dans ce cas, l'algorithme examine chaque élément une fois, donc la complexité en temps est **f(n) = n**. Ainsi, on dit que la recherche linéaire a une complexité de **O(n)**.
   - **Tri par fusion (Merge Sort)**: Ce tri divise récursivement le tableau en deux moitiés jusqu'à ce que les sous-tableaux contiennent un seul élément, puis les fusionne. La complexité de ce tri est **f(n) = n \* log(n)**, donc il est de **O(n \* log(n))**.

3. **Utilisation pratique de la notation O** :
   - Lorsqu'on compare deux algorithmes de tri, par exemple, le tri à bulles **O(n²)** et le tri rapide **O(n \* log(n))**, la notation O nous aide à comprendre que le tri rapide sera généralement plus rapide sur de grandes entrées, car **n \* log(n)** croît moins vite que **n²**.

En résumé, la notation O est essentielle pour l'analyse théorique des algorithmes en informatique. Elle permet de quantifier et de comparer l'efficacité des algorithmes de manière standardisée, en se concentrant sur leur comportement pour de grandes valeurs de **n**, ce qui est souvent le cas pratique le plus pertinent.