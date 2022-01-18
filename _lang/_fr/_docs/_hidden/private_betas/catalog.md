---
nav_title: Catalogues
permalink: "/fr/catalogue/"
hidden: vrai
---

# Catalogues

Vous pouvez utiliser des catalogues pour référencer des données non-utilisateur dans vos campagnes Braze via Liquid.

Pour ce faire, importez d'abord votre catalogue (un CSV de données non-utilisateur) dans Braze, puis accédez à ces informations pour enrichir vos messages. Vous pouvez introduire n'importe quel type de données dans un catalogue. Ces données sont généralement une sorte de métadonnées de votre entreprise, telles que des informations sur les produits pour une entreprise de commerce en ligne, ou des informations de cours pour un prestataire d'enseignement.

Une fois ces informations importées, vous pouvez commencer à y accéder dans des messages d'une manière similaire à accéder à des attributs personnalisés ou à des propriétés d'événements personnalisés via Liquid.

{% alert important %}
Les catalogues sont actuellement en version bêta. Veuillez contacter votre responsable de compte Braze si vous êtes intéressé à participer à la bêta.
{% endalert %}

Si vous souhaitez partager vos commentaires sur cette fonctionnalité ou faire une demande, vous pouvez [réserver une session](https://calendly.com/d/yzvf-frpy/catalog-beta-working-session?month=2021-10) avec l'équipe de Braze Data Ingestion sur Calendly !

## Création d'un catalogue

Pour créer un catalogue au Brésil, téléchargez un CSV sur la page **Catalogues**. Chaque fichier CSV que vous téléchargez sera son propre catalogue. Chaque catalogue a un identifiant ; vous l'utiliserez pour référencer les données de ce catalogue dans une étape ultérieure.

### Étape 1 : Créez votre CSV

Tout d'abord, créez votre fichier CSV. Le CSV doit avoir une colonne avec un en-tête `id`, et l'id `de chaque élément` doit être unique. En outre, les limitations suivantes s'appliquent aux fichiers CSV du catalogue :

- Maximum de 1 000 éléments (lignes)
- Maximum de 20 champs (colonnes)
- Taille maximale du champ (cellule) de 0,5kb
- Taille maximale du fichier CSV de 10 Mo

Pour ce tutoriel, nous utilisons un catalogue qui répertorie deux jeux, leur coût et un lien d'image:

!\[The table shows two example games with columns for id, title, price, and image_link\]\[5\]

### Étape 2 : Téléchargez votre CSV

Après avoir créé votre CSV, accédez à la page **Catalogues** et téléchargez le fichier. Glissez et déposez votre fichier dans la zone de téléchargement, ou cliquez sur **Télécharger CSV** et choisissez votre fichier.

!\[Zone de téléchargement CSV du catalogue\]\[1\]

### Étape 3 : Prenez note de votre ID de catalogue

Après avoir téléchargé votre catalogue avec succès, le catalogue s'affiche dans une liste sous la zone de téléchargement. Chaque catalogue a un ID de catalogue associé, un code alphanumérique de 24 chiffres. Gardez cet identifiant à portée de main, vous en aurez besoin à l'étape suivante.

!\[Exemple d'ID du catalogue et des fichiers CSV associés dans une liste sous la zone de téléchargement\]\[2\]

## Mise à jour d'un catalogue

Si vous avez besoin de mettre à jour un catalogue existant, vous pouvez le faire en remplaçant votre catalogue par une nouvelle version. Pour ce faire, cliquez sur <i class="fas fa-sync-alt"> **Remplacer le catalogue**</i> de la page **Catalogues** et téléchargez votre nouveau CSV.

!\[Remplacer le catalogue existant\]\[8\]

Lorsque vous remplacez un catalogue, tous les contenus et en-têtes du catalogue seront remplacés, mais l'ID du catalogue ne changera pas. Cela vous permet de mettre à jour le contenu du catalogue sans avoir besoin d'aller dans vos messages existants et de mettre à jour les identifiants de catalogue référencés.

## Utiliser des catalogues dans un message

Pour utiliser votre catalogue dans un message, vous aurez besoin de l'ID du catalogue. Pour notre exemple de scénario, l'ID du catalogue pour notre catalogue de Jeux est `6171a881759044006998ed9a`.

### Étape 1 : Récupérer un objet {#step-one-retrieve-item}

Dans le message compositeur de votre choix, utilisez la balise `catalogues` Liquid pour récupérer un élément :

{% raw %}
```liquid
{% catalogs /catalogs/<CATALOG_ID>/items/<ITEM_ID>%}
```
{% endraw %}

Remplacez `<CATALOG_ID>` par votre ID de catalogue et `<ITEM_ID>` par un ID d'élément (ligne) du catalogue.

Par exemple, disons que nous voulons référencer l'élément `tales_storefront`:

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}
```
{% endraw %}

### Étape 2 : Attributs de référence pour cet élément

Sous la balise `catalogues` , utilisez l'objet `item` pour référencer des attributs différents pour cet élément.

{% alert note %}
Rappelez-vous que Liquid est sensible à la casse! Assurez-vous que vous correspondez exactement au cas utilisé dans votre catalogue. Dans notre catalogue d'exemple, nous avons utilisé des minuscules pour nos colonnes, donc nous utilisons des minuscules dans les objets `item`.
{% endalert %}

Par exemple, pour référencer le titre et le prix de l'élément `tales_storefront` nous pourrions ajouter les éléments suivants :

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}

Obtenez {{ item.title }} pour seulement {{ item.price }}!
```
{% endraw %}

Cela se traduit par ce qui suit :

> Obtenez des contes pour seulement 7,49 USD!

## Cas d'utilisation supplémentaires

### Éléments multiples

Vous n'êtes pas limité à un seul élément dans un seul message ! Pour référencer plusieurs éléments de votre catalogue dans un seul message, répétez la balise `catalogues` et remplacez le `<ITEM_ID>` par un élément différent de votre catalogue. Reportez-vous à l'exemple suivant :

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}

Obtenez {{ item.title }} pour seulement {{ item.price }}!

{% catalogs /catalogs/6171a881759044006998ed9a/items/reformation_storefront %}

Obtenez {{ item.title }} pour seulement {{ item.price }}!
```
{% endraw %}

Cela se traduit par ce qui suit :

> Obtenez des Tales pour seulement 7,49 USD!<br> Obtenez des Réformes pour seulement 22,49 USD!

### Utiliser des images {#using-images}

Vous pouvez également référencer des images dans le catalogue pour les utiliser dans votre messagerie. Pour ce faire, utilisez la balise `catalogues` et l'objet `item` dans le champ Liquid pour les images.

Par exemple, pour ajouter le `image_link` de notre catalogue de jeux à notre message promotionnel pour les contes nous pouvons ajouter ce qui suit à notre champ d'image :

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}

{{ item.image_link }}
```
{% endraw %}

!\[Message composer with catalogue Liquid tag used in the Push Icon Image field\]\[3\]

Voici à quoi cela ressemble lorsque le Liquide est rendu :

!\[Exemple de notification de push iOS avec les tags Liquid affichés dans le catalogue\]\[4\]{: style="max-width:50%" }

### Templating catalogue items

Vous pouvez également utiliser le modèle pour extraire dynamiquement les éléments du catalogue en fonction des attributs personnalisés. Par exemple, disons qu'un utilisateur a l'attribut personnalisé `liste de souhaits`, qui contient un tableau d'ID de jeu de votre catalogue.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["tales_storefront", "teslagrad_storefront"]
        }
    ]
 } }
```

En utilisant le modèle Liquid, vous pouvez retirer dynamiquement les identifiants de la liste de souhaits puis les utiliser dans votre message. Pour ce faire, [assignez une variable][10] à votre attribut personnalisé, alors utilisez la balise `catalogues` pour extraire un élément spécifique du tableau.

{% alert tip %}
Rappelez-vous que les tableaux commencent à `0`, pas à `1`.
{% endalert %}

Par exemple, pour informer un utilisateur que `tales_storefront` (un élément de notre catalogue pour lequel il a voulu) est en vente, nous pouvons ajouter ce qui suit à notre compositeur de message :

{% raw %}
```liquid
{% assignez wishlist = {{custom_attribute.${wishlist}}}%}
{% catalogs /catalogs/6171a881759044006998ed9a/items/{{ wishlist[0] }} %}

Obtenez {{item.title}} maintenant, pour seulement {{item.sale_price}}!
```
{% endraw %}

Ce qui sera affiché comme suit:
> Obtenez des contes dès maintenant, pour seulement 7,49 USD!

Avec le modèle, vous pouvez afficher un élément de catalogue différent pour chaque utilisateur en fonction de leurs attributs personnalisés, propriétés d'événement, ou tout autre champ templatable.

### Utiliser des ensembles filtrés

Vous pouvez utiliser des ensembles filtrés pour définir un ensemble de critères. et Braze retournera les éléments correspondants de votre catalogue dans un tableau spécial d'objets nommé `items`. Vous pouvez ensuite itérer à travers ces éléments pour les extraire et référencer leurs différentes propriétés. Les ensembles filtrés sont parfaits pour les cas d'utilisation de type « moteur de recommandation léger ».

Par exemple, voici un catalogue de vêtements avec des champs de disponibilité, de catégorie, de marque, de prix, de nom et de couleur :

!\[Le tableau montre 15 exemples d'articles de vêtements avec des colonnes pour l'identifiant, la disponibilité, la catégorie, la marque, le prix, le nom et la couleur\]\[6\]

Dans le compositeur de votre message, [d'abord assigner des variables][10] aux critères que vous voulez filtrer, trier et limiter dans votre catalogue. Cela vous permet d'ajuster plus facilement vos filtres plus tard.

{% raw %}
```liquid
{% assign var_category = 'pants' %}
{% assign var_availability = 'in_stock' %}
{% assign var_sort = 'price' %}
{% assign var_limit = 2 %}
```
{% endraw %}

Ensuite, faites référence à votre catalogue en utilisant la syntaxe suivante:

{% raw %}
```liquid
{% catalogs /catalogs/<CATALOG_ID>/items?<QUERY_PARAMETERS>%}
```
{% endraw %}

- Ajouter `les paramètres` de filtre au format `field=value`, où chaque paramètre est séparé par un esperluette `&`.
- Ajoute un paramètre `tri` au format `tri[field]=direction`.
- Ajouter un paramètre `limite` au format `limit=valeur`.

Par exemple, les filtres suivants pour les articles de la catégorie pantalon qui sont en stock. Les résultats sont triés par prix avec un maximum de deux éléments affichés :

{% tabs local %}
{% tab Variables %}

{% raw %}
```liquid
{% catalogues /catalogs/61a52350d266a7006d5a529c/articles?category={{var_category}}&disponibilité={{var_availability}}&sort[{{var_sort}}]=asc&limit={{var_limit}}%}
```
{% endraw %}

{% endtab %}
{% tab Values %}
{% raw %}
```liquid
{% catalogs /catalogs/61a52350d266a7006d5a529c/articles?category=pantalons&availability=in_stock&sort[price]=asc&limit=2 %} 
```
{% endraw %}
{% endtab %}
{% endtabs %}

Enfin, ajoutez la copie de votre message et les éléments de référence du tableau. Pour ce faire, utilisez le format `éléments de format[0]. d` où `[0]` est la position de l'élément dans le tableau et `id` est le nom de la colonne dans votre catalogue. Ce qui suit est une simple impression du nom, de la couleur et du prix de l'objet de vêtement:

{% raw %}
```liquid
title: {{ items[0].name }}, couleur : {{ items[0].color }}, prix : {{items[0].price}}
titre : {{ items[1].name }}, couleur : {{ items[1].color }}, prix : {{items[1].price}}
```
{% endraw %}

Alternativement, vous pouvez itérer à travers tous les `éléments` en utilisant :

{% raw %}
```liquid
{% for item in items %}
  titre : {{ item.name }}, couleur : {{ item.color }}, prix : {{item.price}}
{% endfor %}
```
{% endraw %}

L'une ou l'autre des affichages ci-dessus est la suivante :

!\[Exemple de notification de push iOS avec les éléments filtrés du catalogue rendu\]\[7\]{: style="max-width:50%" }

{% alert note %}
Si aucun élément ne correspond aux critères de filtrage, `éléments` seront un tableau vide.
{% endalert %}

#### Limitation

Les limitations suivantes s'appliquent à l'utilisation des ensembles filtrés dans les catalogues :

- Le filtre est pour la chaîne égale seulement
- Le filtre est pour les opérations `ET` seulement
- Le tri est ascendant (`asc`) ou descendant (`desc`), par défaut à `asc`
- La limite par défaut (nombre d'articles à retourner) est de 10
- Limite maximale est de 100
[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %} [2]: {% image_buster /assets/img_archive/catalog_id. ng %} [3]: {% image_buster /assets/img_archive/catalog_image_link1.png %} [4]: {% image_buster /assets/img_archive/catalog_image_link2. ng %} [5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %} [6]: {% image_buster /assets/img_archive/catalog_filtered_csv. ng %} [7]: {% image_buster /assets/img_archive/catalog_filtered_example.png %} [8]: {% image_buster /assets/img_archive/catalog_replace.png %}

[10]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables

[10]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables
