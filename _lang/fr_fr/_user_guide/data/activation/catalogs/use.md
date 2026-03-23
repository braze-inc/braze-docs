---
nav_title: Utilisation des catalogues
article_title: Utiliser les catalogues
page_order: 1.5
description: "Cet article de référence explique comment utiliser les catalogues pour référencer les données non-utilisateurs dans vos campagnes Braze via Liquid."
---

# Utilisation des catalogues

> Après avoir créé un catalogue, vous pouvez référencer des données non-utilisateurs dans vos campagnes Braze via [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Vous pouvez utiliser les catalogues dans tous vos canaux de communication, y compris partout dans l'éditeur par glisser-déposer où Liquid est pris en charge.

## Utilisation de catalogues dans un message

### Étape 1 : Ajouter un type de personnalisation {#step-one-personalization}

Dans l'éditeur de message de votre choix, sélectionnez l'icône <i class="fas fa-plus-circle"></i> « + » pour ouvrir la fenêtre modale **Ajouter une personnalisation**, puis sélectionnez **Éléments du catalogue** comme **type de personnalisation**. Sélectionnez ensuite le nom de votre catalogue. En reprenant l'exemple précédent, nous allons sélectionner le catalogue « Games ».

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Nous pouvons immédiatement voir l'aperçu Liquid suivant :

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Étape 2 : Sélectionner les éléments du catalogue

Ensuite, il est temps d'ajouter vos éléments de catalogue ! À l'aide de la liste déroulante, sélectionnez les éléments du catalogue et les informations à afficher. Ces informations correspondent aux colonnes du fichier CSV importé utilisé pour générer votre catalogue.

Par exemple, pour référencer le titre et le prix de notre jeu Tales, nous pouvons sélectionner l'`id` de Tales (1234) comme élément du catalogue et demander `title` et `price` pour les informations affichées.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Ceci donne le résultat suivant :

> Get Tales for just 7.49!

## Exporter des catalogues

Vous pouvez exporter des catalogues à partir du tableau de bord de deux manières :

- Survolez la ligne du catalogue dans la section **Catalogues**. Sélectionnez ensuite le bouton **Exporter le catalogue**.
- Sélectionnez votre catalogue. Ensuite, sélectionnez le bouton **Exporter le catalogue** dans l'onglet **Prévisualiser** du catalogue.

Vous recevrez un e-mail vous permettant de télécharger le fichier CSV après avoir lancé l'exportation. Vous disposerez de quatre heures pour récupérer ce fichier.

## Cas d'utilisation supplémentaires

### Plusieurs éléments

Vous n'êtes pas limité à un seul élément par message. Utilisez la fenêtre modale **Ajouter une personnalisation** pour ajouter jusqu'à trois éléments du catalogue à la fois. Pour en ajouter davantage, sélectionnez à nouveau **Ajouter une personnalisation** dans l'éditeur, puis choisissez les éléments supplémentaires du catalogue et les informations à afficher.

Dans cet exemple, nous ajoutons l'`id` de trois jeux — Tales, Teslagrad et Acaratus — pour les **éléments du catalogue** et nous sélectionnons `title` pour les **informations à afficher**.

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Nous pouvons personnaliser davantage notre message en ajoutant du texte autour de notre Liquid :

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Ceci donne le résultat suivant :

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

Dans cet exemple, la balise `catalog_items` récupère l'élément `1234` du catalogue `Games`, puis l'instruction `if` vérifie le champ `on_sale` pour afficher différents messages.

#### Avec des sélections de catalogue

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer. 
{% else %} 
{% abort_message('no venue_name') %} 
{% endif %}
```
{% endraw %}

Dans cet exemple, différents messages s'affichent selon que le champ `venue_name` contient plus ou moins de 10 caractères. Si `venue_name` est vide, le message est interrompu.

{% alert tip %}
Pour éviter les erreurs de syntaxe Liquid, sélectionnez le bouton **+** dans l'éditeur de message pour insérer automatiquement les étiquettes Liquid de catalogue.
{% endalert %}

### Utiliser des images {#using-images}

Vous pouvez également référencer les images du catalogue pour les utiliser dans vos messages. Pour ce faire, utilisez la balise `catalogs` et l'objet `item` dans le champ Liquid pour les images.

Par exemple, pour ajouter le `image_link` de notre catalogue Games à notre message promotionnel pour Tales, sélectionnez l'`id` pour le champ **Éléments du catalogue** et `image_link` pour le champ **Informations à afficher**. Ceci ajoute les étiquettes Liquid suivantes à notre champ d'image :

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Éditeur de carte de contenu avec une étiquette Liquid de catalogue utilisée dans le champ d'image.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Voici à quoi cela ressemble une fois le Liquid rendu :

![Exemple de carte de contenu avec rendu des étiquettes Liquid du catalogue.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### Modèles d'éléments de catalogue

Vous pouvez également utiliser les modèles pour extraire dynamiquement des éléments du catalogue en fonction des attributs personnalisés. Par exemple, imaginons qu'un utilisateur possède l'attribut personnalisé `wishlist`, qui contient un tableau d'ID de jeux de votre catalogue.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
Les objets JSON dans les catalogues ne sont ingérés que par l'API. Vous ne pouvez pas importer un objet JSON à l'aide d'un fichier CSV.
{% endalert %}

Grâce au modèle Liquid, vous pouvez extraire dynamiquement les ID de la liste de souhaits, puis les utiliser dans votre message. Pour ce faire, [affectez une variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) à votre attribut personnalisé, puis utilisez la fenêtre modale **Ajouter une personnalisation** pour extraire un élément spécifique du tableau. Les variables référencées comme ID d'élément du catalogue doivent être placées entre accolades pour être correctement référencées, comme `{{result}}`.

{% alert tip %}
N'oubliez pas que les tableaux commencent à `0` et non à `1`.
{% endalert %}

Par exemple, pour informer un utilisateur que Tales (un élément de notre catalogue qu'il a ajouté à ses souhaits) est en promotion, nous pouvons ajouter ce qui suit à notre éditeur de message :

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

Ce qui s'affichera comme suit :
> Get Tales now for just 7.49!

Avec les modèles, vous pouvez afficher un élément du catalogue différent pour chaque utilisateur en fonction de ses attributs personnalisés, de ses propriétés d'événement ou de tout autre champ modélisable.

### Charger un CSV

Vous pouvez importer un fichier CSV de nouveaux éléments de catalogue à ajouter ou d'éléments de catalogue à mettre à jour. Pour supprimer une liste d'éléments, vous pouvez charger un CSV d'ID d'éléments pour les supprimer.

### Utilisation de Liquid

Vous pouvez également composer manuellement des catalogues avec la logique Liquid. Cependant, notez que si vous saisissez un ID qui n'existe pas, Braze renverra tout de même un tableau d'éléments sans objet. Nous vous recommandons d'inclure la gestion des erreurs, comme la vérification de la taille du tableau et l'utilisation d'une instruction `if` pour gérer le cas d'un tableau vide.

#### Modélisation d'éléments de catalogue incluant du Liquid

Tout comme pour le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), vous devez utiliser le drapeau `:rerender` dans une étiquette Liquid pour afficher le contenu Liquid d'un élément du catalogue. Notez que le drapeau `:rerender` ne s'applique qu'à un seul niveau de profondeur, ce qui signifie qu'il ne s'appliquera pas aux appels d'étiquettes Liquid imbriqués.

Si un élément du catalogue contient des champs de profil utilisateur (dans une étiquette de personnalisation Liquid), ces valeurs doivent être définies dans Liquid plus tôt dans le message et avant la modélisation afin de garantir le bon rendu du Liquid. Si le drapeau `:rerender` n'est pas fourni, le contenu Liquid brut sera restitué.

Par exemple, si un catalogue nommé « Messages » possède un élément avec ce Liquid :

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Pour rendre le contenu Liquid suivant :

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

L'affichage sera le suivant :

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Les étiquettes Liquid des catalogues ne peuvent pas être utilisées de manière récursive à l'intérieur des catalogues.
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}