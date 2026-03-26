---
nav_title: Guide de style pour les images
article_title: Guide de style pour les images
description: "Lignes directrices pour la création et la mise en forme des images dans la documentation Braze."
page_order: 1
noindex: true
---

# Guide de style pour les images

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

## Optimiser le placement et le dimensionnement

Dans la mesure du possible, placez les images à proximité du texte correspondant et veillez à utiliser le Markdown de mise en forme des images pour redimensionner les images plus grandes. Pour certains contenus, il convient d'[ancrer le texte à gauche ou à droite de la page]({{site.baseurl}}/home/styling_test_page/#image-test) en fonction de l'image et de l'espace disponible.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %}" alt="Exemple de placement d'image correctement optimisé."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %}" alt="Exemple de placement d'image mal optimisé."></td></tr>
</tbody>
</table>
{:/}

## Recadrer les images

Recadrez les sections pertinentes au plus près. Sauf si c'est nécessaire, n'incluez pas la barre de navigation latérale et fournissez plutôt les indications de navigation dans l'article. Cela limite le nombre d'images à modifier lors de changements d'interface.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_1.png %}" alt="Exemple d'image correctement recadrée."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_1.png %}" alt="Exemple d'image mal recadrée."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_2.png %}" alt="Exemple d'image correctement recadrée."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_2.png %}" alt="Exemple d'image mal recadrée."></td></tr>
</tbody>
</table>
{:/}

La documentation Braze ajoutant déjà une bordure à chaque image, omettez les bordures dans les captures d'écran de sections. L'objectif est un recadrage net. La bordure peut être conservée si des éléments se trouvent à l'extérieur ou à l'intérieur de celle-ci ; consultez les images suivantes à titre d'exemples.

**À faire :**
![Exemple d'image correctement recadrée.]({% image_buster /assets/img/contributing/style_guide/cropping_do_3.png %})

**À éviter :**  
![Exemple d'image mal recadrée.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_3.png %})
  
**À faire :**  
![Exemple d'image correctement recadrée.]({% image_buster /assets/img/contributing/style_guide/cropping_do_4.png %})

## Flouter les informations sensibles

Floutez toute information personnelle identifiable (PII) telle que les noms, les e-mails et les clés API.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_do.png %}" alt="Exemple de floutage correct."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_dont.png %}" alt="Exemple de floutage incorrect."></td></tr>
</tbody>
</table>
{:/}

## Ne pas intégrer de texte important dans les images

Évitez d'intégrer du texte dans les images, car tous les utilisateurs ne peuvent pas lire le texte en anglais (et les outils de traduction de page ne traduisent pas les images). Ce texte doit être fourni dans l'article. Ajoutez un texte alternatif aux images pour une accessibilité maximale.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_do.png %}" alt="Exemple correct sans texte intégré dans l'image."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %}" alt="Exemple incorrect avec du texte intégré dans l'image."></td></tr>
</tbody>
</table>
{:/}

## Ne pas mettre en évidence les composants inutilement

Ne mettez pas en évidence les composants des images sauf si c'est nécessaire. Utilisez des rectangles bleus (l'option la plus accessible) d'épaisseur fine à moyenne pour mettre en surbrillance les différents composants des images. Assurez-vous que les « sections mises en évidence » ne masquent pas l'interface normale.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_1.png %}" alt="Exemple de mise en évidence correcte des composants dans une image."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_1.png %}" alt="Exemple de mise en évidence incorrecte des composants dans une image."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_2.png %}" alt="Exemple de mise en évidence correcte des composants dans une image."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_2.png %}" alt="Exemple de mise en évidence incorrecte des composants dans une image."></td></tr>
</tbody>
</table>
{:/}