---
nav_title: Création d’un catalogue
article_title: Création d’un catalogue
alias: "/catalogs/"
page_order: 1
description: "Le présent article de référence explique comment créer et utiliser des catalogues pour référencer des données non-utilisateurs dans vos campagnes de Braze via Liquid."
---

# Création d’un catalogue

> Avec les catalogues, vous pouvez référencer des données non-utilisateurs dans vos campagnes de Braze via [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). 

{% alert note %}
Vous pouvez créer jusqu’à cinq catalogues dans votre entreprise.
{% endalert %}

La création d’un catalogue implique l’importation d’un fichier CSV de données non-utilisateurs dans Braze. Cela vous permet d’accéder ensuite à ces informations pour enrichir vos messages. Vous pouvez ajouter n’importe quel type de données à un catalogue. Ces données sont généralement des métadonnées de votre entreprise, telles que des informations sur les produits pour une entreprise Ecommerce, ou des informations sur le cours pour un fournisseur de formation. 

Une fois ces informations importées, vous pouvez commencer à y accéder dans les messages de la même manière que pour accéder aux attributs personnalisés ou aux propriétés d’événements personnalisés via Liquid.

## Préparer votre fichier CSV

Avant de créer un catalogue, assurez-vous que votre fichier CSV est prêt si votre méthode de création de catalogue préférée est de le charger. 

Notez ces directives lors de la création de votre fichier CSV. La première colonne du fichier CSV doit être un en-tête de `id`et chaque article `id` doit être unique. Tous les autres noms de colonnes doivent être uniques. En outre, les limitations suivantes s’appliquent aux fichiers CSV du catalogue :

- Maximum de 5 000 articles (lignes)
- Maximum de 30 champs (colonnes)
- Nom maximum de champ (colonne) de 250 caractères
- Taille maximale du fichier CSV de 100 Mo
- Valeur maximale de champ (cellule) de 5 000 caractères
- Valeur maximale de champ (cellule) de 0,5 Ko
- Seuls les lettres, chiffres, traits d’union et traits de soulignement pour `id` et des valeurs d’en-tête

Assurez-vous que vous encodez votre fichier CSV en utilisant le format UTF-8 afin de télécharger avec succès votre fichier CSV à l’étape suivante. Nous vous recommandons également de formater tout le texte dans vos fichiers CSV en minuscules.

{% alert note %}
Vous avez besoin de plus d’espace pour accueillir vos fichiers CSV ? Contactez votre gestionnaire de compte Braze pour plus d’informations.
{% endalert %}

## Sélectionner votre méthode

Pour commencer, cliquez sur **Create New Catalog (Créer un nouveau catalogue)**, puis choisissez de **Upload CSV (Charger un CSV)** ou **Create in browser (Créer dans le navigateur)**. 

### Méthode 1  : Charger un CSV

1. Faites glisser votre fichier dans la zone de téléchargement ou cliquez sur **Télécharger CSV** et choisissez votre fichier. <br>![][1]{: style="max-width:80%;"} <br><br>
2. Sélectionnez l’un des types de données suivants pour chaque colonne : booléen, nombre, chaîne de caractères ou temps.
<br> ![][9]{: style="max-width:80%;"} <br><br>
3. Nommez votre catalogue. Gardez à l’esprit les exigences suivantes pour le nom du catalogue :
- Doit être unique
- Maximum de 250 caractères
- Peut uniquement inclure des chiffres, des lettres, des traits d’union et des traits de soulignement<br><br>
4. (facultatif) Ajoutez une description pour le catalogue.<br><br>
5. Cliquez sur **Process Catalog (Traiter le catalogue)** pour créer le catalogue.

{% alert note %}
Ce type de données ne peut pas être modifié après la configuration de votre catalogue.
{% endalert %}

Notez que vous ne pouvez pas utiliser de modèles dans un nom de catalogue. Par exemple, vous ne pouvez pas avoir les éléments suivants comme nom du catalogue, sinon vous ne pourrez pas le télécharger.
{% raw %}
```liquid
{% catalog_items custom_attribute.${catalog} item1, item2 %}
```
{% endraw %}

{% alert important %}
Votre fichier CSV peut être rejeté si vous dépassez les [limites de l’entreprise](#limits). 
{% endalert %}

Vous avez également la possibilité de mettre à jour le fichier CSV après avoir choisi de créer un catalogue dans le navigateur. Cliquez sur **Update Catalog > Upload CSV (Mettre à jour le catalogue > Charger un CSV)**, puis sélectionnez si vous souhaitez mettre à jour, ajouter ou supprimer des éléments dans votre catalogue.

### Méthode 2 : Créer dans le navigateur

{% alert important %}
La création d’un catalogue dans le navigateur est actuellement en accès anticipé. Contactez votre gestionnaire du succès des clients Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

1. Saisissez un nom pour votre catalogue. Gardez à l’esprit les exigences suivantes pour le nom de votre catalogue :
- Doit être unique
- Maximum de 250 caractères
- Peut uniquement inclure des chiffres, des lettres, des traits d’union et des traits de soulignement <br> ![][14]{: style="max-width:80%;"} <br><br>
2. (facultatif) Saisissez une description pour votre catalogue.<br><br>
3. Sélectionnez le catalogue que vous venez de créer sur la page **Catalogs (Catalogues)** de la liste pour mettre à jour votre catalogue.<br><br>
4. Cliquez sur **Update Catalog > Add fields (Mettre à jour le catalogue > Ajouter des champs)** pour ajouter vos champs. Saisissez ensuite le **Field name ( Nom du champ)** et utilisez la liste déroulante pour sélectionner le type de données. Répétez l’opération en fonction de vos besoins.<br> ![][12]{: style="max-width:50%;"} <br><br>
5. Ensuite, cliquez sur **Update Catalog > Add items (Mettre à jour le catalogue > Ajouter des produits)** pour ajouter un produit à votre catalogue en saisissant les informations en fonction des champs que vous avez précédemment ajoutés. Ensuite, cliquez sur **Save Item (Enregistrer l’élément)** ou **Save and Add Another (Enregistrer et ajouter un autre)** pour continuer à ajouter vos produits. <br> ![][13]{: style="max-width:50%;"}

Vous avez également la possibilité de charger un fichier CSV après avoir choisi de créer un catalogue dans le navigateur. 

#### Exemple de catalogue

Pour ce didacticiel, nous utilisons un catalogue qui répertorie deux jeux, leur coût et un lien d’image.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">titre</th>
    <th class="tg-0pky">prix</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7,49 USD</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Régénération</td>
    <td class="tg-0pky">22,49 USD</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Dans cet exemple, nous allons créer le catalogue en chargeant un fichier CSV. Les types de données pour `id`, `title`, `price` et `image_link` sont respectivement une chaîne de caractères, une chaîne de caractères, un nombre et une chaîne de caractères. 

{% alert note %}
Ce type de données ne peut pas être modifié après la configuration de votre catalogue.
{% endalert %}

![][9]{: style="max-width:85%;"}

Ensuite, nous appellerons ce catalogue « games_catalog » et cliquerons sur le bouton **Process Catalog (Traiter le catalogue)**. Braze vérifiera ensuite votre catalogue pour détecter d’éventuelles erreurs avant sa création.

![][11]{: style="max-width:85%;"}

Veuillez remarquer que vous ne pourrez pas modifier ce nom une fois le catalogue créé. Vous pouvez supprimer un catalogue et retélécharger une version mise à jour en utilisant le même nom de catalogue. 

## Utilisation de catalogues dans un message

Vous pouvez utiliser des catalogues dans tous vos canaux de messagerie, y compris n’importe où dans l’Éditeur Drag & Drop où Liquid est pris en charge.

### Étape 1 : Ajouter un type de personnalisation {#step-one-personalization}

Dans le message de votre choix, cliquez sur l’ocône<i class="fas fa-plus-circle"></i> plus pour ouvrir **Ajouter une personnalisation** modal et sélectionner **Articles des catalogues** pour le **Type de personnalisation**. Sélectionnez ensuite votre **Nom de catalogue**. En utilisant notre exemple précédent, nous allons sélectionner le catalogue des Jeux.

![][2]

Nous pouvons immédiatement voir l’aperçu Liquid suivant :

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Étape 2 : Sélectionner les articles du catalogue

Ensuite, il est temps d’ajouter vos articles de catalogue. À l’aide de la liste déroulante, sélectionnez les éléments du catalogue et les informations à afficher. Ces informations correspondent aux colonnes de votre fichier CSV téléchargé utilisées pour générer votre catalogue.

Par exemple, pour référencer le titre et le prix du de notre jeu Tales, nous pouvons sélectionner `id`, pour Tales (1234) comme article du catalogue et demander `title` et `price` pour les informations affichées.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Ceci donne le résultat suivant :

> Obtenez Tales 7,49 USD seulement !

## Catalogue par API

Vous pouvez tirer parti des [endpoints de catalogue]({{site.baseurl}}/api/endpoints/catalogs/) pour gérer les données et les informations en constante augmentation.

### Gérer les catalogues

Vous pouvez créer un catalogue en utilisant l’endpoint [créer des catalogues]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/).

Au fur et à mesure que vous créez d’autres catalogues, vous pouvez également utiliser l’endpoint [afficher les catalogues]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) pour renvoyer une liste des catalogues dans le groupe d’apps.

### Gérer les articles du catalogue

En plus de gérer vos catalogues, vous pouvez également utiliser des endpoints synchrones et asynchrones pour gérer les articles du catalogue. Ils comprennent la possibilité d’éditer et de supprimer des articles du catalogue ainsi que d’afficher les détails d’un d’eux. 

Par exemple, si vous désirez éditer un produit du catalogue individuel, vous pouvez utiliser l’endpoint [`/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Scénarios d’utilisation supplémentaires

### Plusieurs articles

Vous n’êtes pas limité à un seul article par message. Insérez simplement les éléments de catalogue supplémentaires et les informations à afficher à l’aide du modal **Ajouter une personnalisation**. Veuillez remarquer que vous pouvez ajouter jusqu’à trois articles de catalogue uniquement. 

Consultez cet exemple dans lequel nous ajoutons le `id` de trois jeux, Tales, Teslagrad et Acaratus, comme **articles du catalogue** et sélectionnons `title` comme **information à afficher**.

![][6]{: style="max-width:70%" }

Nous pouvons personnaliser encore notre message en ajoutant du texte autour de notre Liquid :

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Ceci donne le résultat suivant :

> Découvrez le trio ultime Tales, Teslagrad et Acaratus dès aujourd’hui !

{% alert tip %}
Consultez les [sélections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) pour créer des groupes de données pour des envois de messages plus personnalisés !
{% endalert %}

### Utiliser des images {#using-images}

Vous pouvez également consulter les images du catalogue à utiliser dans votre messagerie. Pour ce faire, utilisez la balise`catalogs` et l’objet `item` dans le champ Liquid pour les images.

Par exemple, pour ajouter `image_link` de notre catalogue des Jeux à notre message promotionnel pour Tales, sélectionnez `id` pour **Articles du catalogue** et `image_link` pour le champ **Informations à afficher**. Ceci ajoute les Balise Liquids suivantes à notre champ d’image :

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Compositeur de carte de contenu avec Balise Liquid de catalogue utilisé dans le champ d’image.][3]

Voici à quoi cela ressemble avec Liquid  ;

![Exemple de carte de contenu avec les Balise Liquids de catalogue.][4]{: style="max-width:50%" }

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

À l’aide du modèle Liquid, vous pouvez extraire dynamiquement les ID de la liste d’envies, puis les utiliser dans votre message. Pour ce faire, [attribuer une variable][10] à votre attribut personnalisé, puis utilisez le modal **Ajouter une personnalisation** pour extraire un élément spécifique de le tableau.

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
> Obtenez Tales tout de suite, pour 7,49 USD seulement !

Avec le modèle, vous pouvez transmettre un article du catalogue différent pour chaque utilisateur en fonction de ses attributs personnalisés individuels, des propriétés d’événement ou de tout autre champ de plateau.

### Charger un CSV

Vous pouvez charger un CSV comprenant de nouveaux articles à ajouter ou des articles du catalogue à mettre à jour. Pour supprimer une liste d’articles, vous pouvez charger un CSV d’ID d’articles pour les supprimer.

### Utilisation de Liquid

Vous pouvez également assembler manuellement les catalogues logiques Liquides. Cependant, veuillez remarquer que si vous saisissez un ID qui n’existe pas, Braze restitue toujours un groupe d’articles sans objet. Nous vous recommandons d’inclure la gestion des erreurs, comme la vérification de la taille de la baie et d’utiliser `if` pour tenir compte d’une situation de baie vide.

## Gérer les catalogues

Au fur et à mesure de la création de catalogues, vous pouvez tirer parti des [endpoints de catalogue]({{site.baseurl}}/api/endpoints/catalogs/) pour gérer les données et les informations en constante augmentation. Ils comprennent la possibilité de créer, d’éditer et de supprimer des articles du catalogue ainsi que d’afficher les détails d’un d’eux.

## Limitations {#limits}

Consultez le tableau suivant pour connaître les limites qui s’appliquent au niveau de l’entreprise :

| Zone de limitation | Version gratuite | Catalogues Pro |
|---|---|---|
| Nombre de catalogues | Jusqu’à 5 catalogues | Jusqu’à 10 catalogues |
| Nombre de tous les articles de catalogues | Jusqu’à 5 000 articles | Jusqu’à 100 000 articles |
| Stockage du catalogue | Jusqu’à 100 Mo de données de catalogue | Jusqu’à 2 Go de données de catalogue |
| Sélections | Jusqu’à 1 sélection par catalogue | Jusqu’à 10 sélections par catalogue |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Le tableau suivant décrit les limitations qui s’appliquent au niveau du catalogue :

| Zone de limitation | Version gratuite | Catalogues Pro |
|---|---|---|
| Taille du fichier CSV | Jusqu’à 100 Mo pour un fichier CSV unique | Jusqu’à 2 Go pour un fichier CSV unique |
| Nombre d’articles | Jusqu’à 5 000 articles dans un seul catalogue | Jusqu’à 100 000 articles dans un seul catalogue |
| Nombre de champs | Jusqu’à 30 champs (colonnes) | Jusqu’à 30 champs (colonnes) |
| Limite de caractères pour la valeur de l’article | Jusqu’à 5 000 caractères en une seule valeur. Par exemple, si vous aviez un champ `description`, le nombre maximum de caractères dans le champ est de 5 000. | Jusqu’à 5 000 caractères en une seule valeur. Par exemple, si vous aviez un champ `description`, le nombre maximum de caractères dans le champ est de 5 000. |
| Limite de caractères pour le nom de la colonne d’article | Jusqu’à 250 caractères | Jusqu’à 250 caractères |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Vous souhaitez mettre à niveau ces limites par défaut ? Contactez votre gestionnaire de compte pour commencer.

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[2]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[3]: {% image_buster /assets/img_archive/catalog_image_link1.png %}
[4]: {% image_buster /assets/img_archive/catalog_image_link2.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[6]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
[7]: {% image_buster /assets/img_archive/create_catalog_option.png %}
[9]: {% image_buster /assets/img_archive/catalog_data_type.png %}
[11]: {% image_buster /assets/img_archive/catalog_new_name.png %}
[12]: {% image_buster /assets/img_archive/add_catalog_fields.png %}
[13]: {% image_buster /assets/img_archive/add_catalog_items.png %}
[14]: {% image_buster /assets/img_archive/in_browser_catalog.png %}
[10]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables
