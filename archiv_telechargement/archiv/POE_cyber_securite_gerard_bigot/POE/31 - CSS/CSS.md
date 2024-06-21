CSS, ou Cascading Style Sheets (Feuilles de style en cascade), est un langage de feuille de style utilisé pour décrire la présentation d'un document écrit en HTML ou en XML (y compris des langages basés sur XML comme SVG ou XHTML). 

CSS définit comment les éléments de la structure HTML doivent être affichés à l'écran, sur papier, en parole, ou sur d'autres médias.

### Fonctions principales de CSS

1. **Séparation du contenu et de la présentation** : CSS facilite la séparation entre le contenu d'une page (HTML) et sa présentation (style). Cela rend le contenu plus accessible et la page plus facile à maintenir.

2. **Contrôle de la mise en page** : CSS permet de contrôler précisément la mise en page des éléments web sur une grande variété de dispositifs, tailles d'écran et orientations.

3. **Économie de travail** : Les styles sont définis une fois dans des feuilles de style externes et peuvent être appliqués à n'importe quelle page du site. Cela permet de changer le style de plusieurs pages en ajustant un seul fichier.

4. **Améliorations visuelles** : Avec CSS, les développeurs peuvent implémenter des designs complexes incluant des animations, des transitions, des formes, des ombres, et des gradients sans l'utilisation d'images ou d'autres méthodes traditionnelles.

### Syntaxe de base de CSS

CSS utilise des sélecteurs pour définir à quels éléments du document HTML les règles s'appliquent. Une règle CSS se compose d'un sélecteur et d'un bloc de déclaration contenant une ou plusieurs déclarations séparées par des points-virgules. Chaque déclaration inclut un nom de propriété et une valeur, séparés par un deux-points.

```css
/* Exemple de règle CSS */
p {
    color: red;
    text-align: center;
}
```

Dans cet exemple, `p` est le sélecteur, et le bloc de déclarations définit que le texte à l'intérieur des éléments `<p>` doit être centré et coloré en rouge.

### Types de sélecteurs en CSS

1. **Sélecteurs d'élément** (ou sélecteurs de type) : ciblent des balises HTML spécifiques.
2. **Sélecteurs de classe** : commencent par un point et sont suivis par le nom de la classe.
3. **Sélecteurs d'ID** : commencent par un dièse (`#`) suivi par l'ID de l'élément.
4. **Sélecteurs d'attribut** : ciblent des éléments basés sur un attribut et sa valeur.
5. **Sélecteurs pseudo-classes et pseudo-éléments** : ciblent des éléments dans un état spécifique ou certaines parties d'éléments.

### Incorporation de CSS dans HTML

CSS peut être incorporé dans HTML de trois manières :
- **Externe** : via un fichier `.css` lié avec une balise `<link>`.
- **Interne** : dans l'en-tête du document avec une balise `<style>`.
- **Inline** : directement dans les attributs `style` des balises HTML.

### Conclusion

CSS est vital pour la création de sites web modernes, offrant aux développeurs et aux concepteurs le contrôle nécessaire pour créer des présentations visuelles précises et réactives. Grâce à son évolution constante, CSS continue d'introduire de nouvelles fonctionnalités comme les grilles (CSS Grid), les flexbox, les variables CSS, et bien plus, rendant le web plus dynamique et interactif.