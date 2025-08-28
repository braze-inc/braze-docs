---
nav_title: Utilisation des catalogues
article_title: Utilisation des catalogues
page_order: 1.5
description: "Cet article de référence explique comment utiliser les catalogues pour référencer les données non-utilisateurs dans vos campagnes Braze via Liquid."
---

# Utilisation de catalogues dans un message

> Après avoir créé un catalogue, vous pouvez référencer des données non-utilisateurs dans vos campagnes Braze via [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Vous pouvez utiliser les catalogues dans tous vos canaux de communication, y compris partout dans l'éditeur par glisser-déposer où Liquid est pris en charge.

## Étape 1 : Ajouter un type de personnalisation {#step-one-personalization}

Dans le composeur de messages de votre choix, sélectionnez l'icône <i class="fas fa-plus-circle"></i> plus pour ouvrir la fenêtre modale/boîte de dialogue de **l'ajout de personnalisation** et sélectionnez **Articles de catalogue** pour le **type de personnalisation**. Sélectionnez ensuite votre **nom de catalogue**. En reprenant l'exemple précédent, nous allons sélectionner le catalogue « Jeux ».

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Nous pouvons immédiatement voir l’aperçu Liquid suivant :

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

## Étape 2 : Sélectionner les articles du catalogue

Ensuite, il est temps d’ajouter vos articles de catalogue. À l’aide de la liste déroulante, sélectionnez les éléments du catalogue et les informations à afficher. Ces informations correspondent aux colonnes de votre fichier CSV téléchargé utilisées pour générer votre catalogue.

Par exemple, pour référencer le titre et le prix du de notre jeu Tales, nous pouvons sélectionner `id`, pour Tales (1234) comme article du catalogue et demander `title` et `price` pour les informations affichées.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Ceci donne le résultat suivant :

> Obtenez Tales pour seulement 7,49 euros !

## Exporter des catalogues

Vous pouvez exporter des catalogues à partir du tableau de bord de deux manières : 

- Survolez la ligne du catalogue dans la section **Catalogues**. Sélectionnez ensuite le bouton **Exporter le catalogue**.
- Sélectionnez votre catalogue. Ensuite, sélectionnez le bouton **Exporter le catalogue** dans l'onglet **Aperçu** du catalogue.

Vous recevrez un e-mail vous permettant de télécharger le fichier CSV après avoir lancé l'exportation. Vous aurez jusqu'à quatre heures pour récupérer ce fichier.

## Scénarios d’utilisation supplémentaires

### Plusieurs articles

Vous n'êtes pas limité à un seul élément dans un seul message. Vous pouvez utiliser la fenêtre modale/boîte de dialogue de **personnalisation** pour ajouter jusqu'à trois éléments de catalogue à la fois. Pour ajouter d'autres éléments à votre message, sélectionnez **Ajouter une personnalisation** dans le compositeur de message et sélectionnez les éléments et informations supplémentaires du catalogue à afficher.

Dans cet exemple, nous ajoutons l’`id` de trois jeux, Tales, Teslagrad et Acaratus, pour les **produits du catalogue** et nous sélectionnons `title` pour les **informations à afficher**.

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Nous pouvons personnaliser encore notre message en ajoutant du texte autour de notre Liquid :

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Ceci donne le résultat suivant :

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Découvrez les [sélections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) permettant de créer des groupes de données pour un envoi de messages plus personnalisé !
{% endalert %}

### Utilisation des instructions Liquid `if`

Vous pouvez utiliser des éléments de catalogue pour créer des instructions conditionnelles. Par exemple, vous pouvez déclencher l'affichage d'un certain message lorsqu'un produit spécifique est sélectionné dans votre campagne.

Pour ce faire, vous utiliserez une déclaration Liquid `if`, comme dans cet exemple :

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size < 10 %}
Message if the venue name's size is less than 10 characters. 
{% else %} 
{% abort_message(no venue_name) %} 
{% endif %}
```
{% endraw %}

Dans cet exemple, des messages différents s'afficheront si l'attribut personnalisé `venue_name` comporte plus de 10 caractères ou moins de 10 caractères. Si `venue_name` est `blank`, rien ne s'affichera. 

Notez que vous devez déclarer la liste du catalogue et, le cas échéant, la sélection avant d'utiliser les instructions `if`. Dans l'exemple, `item-list` est la liste du catalogue et `selections` est le nom de la sélection.

### Utiliser des images {#using-images}

Vous pouvez également consulter les images du catalogue à utiliser dans votre messagerie. Pour ce faire, utilisez la balise`catalogs` et l’objet `item` dans le champ Liquid pour les images.

Par exemple, pour ajouter le `image_link` de notre catalogue de jeux à notre message promotionnel pour Tales, sélectionnez l’`id` pour le champ **Produits du catalogue** et `image_link` pour le champ **Informations à afficher**. Ceci ajoute les Balise Liquids suivantes à notre champ d’image :

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Composant de la carte de contenu avec l'étiquette Liquid du catalogue utilisée dans le champ de l'image.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Voici à quoi cela ressemble avec Liquid  ;

![Exemple de carte de contenu avec rendu des étiquettes Liquid du catalogue.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### Modèles d’articles de catalogue

Vous pouvez également utiliser les modèles pour extraire dynamiquement des éléments du catalogue en fonction des attributs personnalisés. Par exemple, disons qu’un utilisateur a l’attribut personnalisé `wishlist`, qui contient une série d’ID de jeu de votre catalogue.

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
Les objets JSON dans les catalogues ne sont ingérés que par l'API. Vous ne pouvez pas télécharger un objet JSON à l'aide d'un fichier CSV.
{% endalert %}

À l’aide du modèle Liquid, vous pouvez extraire dynamiquement les ID de la liste d’envies, puis les utiliser dans votre message. Pour ce faire, [affectez une variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) à votre attribut personnalisé, puis utilisez la fenêtre modale/boîte de dialogue de **personnalisation** pour extraire un élément spécifique du tableau. Les variables référencées comme l'ID de l'article du catalogue doivent être placées entre crochets pour être référencées correctement, comme `{{result}}`.

{% alert tip %}
Souvenez-vous que les baies commencent à `0` et non pas à `1`.
{% endalert %}

Par exemple, pour informer un utilisateur que Tales (un article de notre catalogue qu’il a souhaité) est en solde, nous pouvons ajouter ce qui suit à notre rédacteur de message :

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

Il s’affichera comme suit :
> Obtenez Tales dès maintenant, pour seulement 7,49 !

Avec le modèle, vous pouvez transmettre un article du catalogue différent pour chaque utilisateur en fonction de ses attributs personnalisés individuels, des propriétés d’événement ou de tout autre champ de plateau.

### Charger un CSV

Vous pouvez télécharger un fichier CSV de nouveaux éléments de catalogue à ajouter ou d'éléments de catalogue à mettre à jour. Pour supprimer une liste d’articles, vous pouvez charger un CSV d’ID d’articles pour les supprimer.

### Utilisation de Liquid

Vous pouvez également composer manuellement des catalogues avec la logique Liquid. Cependant, veuillez remarquer que si vous saisissez un ID qui n’existe pas, Braze restitue toujours un groupe d’articles sans objet. Nous vous recommandons d’inclure la gestion des erreurs, comme la vérification de la taille de la baie et d’utiliser `if` pour tenir compte d’une situation de baie vide.

{% alert note %}
Actuellement, les liquides ne peuvent pas être utilisés dans les catalogues. Si la personnalisation Liquid est listée dans une cellule de votre catalogue, la valeur dynamique ne sera pas affichée et seul le Liquid s'affichera.
{% endalert %}

#### Modélisation de produits de catalogue comprenant des étiquettes Liquid

Comme pour le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), vous devez utiliser l'indicateur `:rerender` dans une étiquette Liquid pour rendre le contenu Liquid d'un article de catalogue. Notez que l'indicateur `:rerender` ne s'applique qu'à un seul niveau, ce qui signifie qu'il ne s'appliquera pas aux appels d'étiquettes Liquid imbriqués.

Si un article de catalogue contient des champs de profil d'utilisateur (dans une étiquette Liquid de personnalisation), ces valeurs doivent être définies dans Liquid plus tôt dans le message et avant la mise en page pour que le rendu de Liquid soit correct. Si l’indicateur `:rerender` n'est pas fourni, le contenu brut Liquid sera restitué.

Par exemple, si un catalogue nommé « Messages » possède un produit avec ce Liquid :

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Pour rendre le contenu Liquid suivant :

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

L'affichage est le suivant :

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
