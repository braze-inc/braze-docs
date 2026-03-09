---
nav_title: Créer un catalogue
article_title: Créer un catalogue
alias: "/catalogs/"
page_order: 1
description: "Cet article de référence explique comment créer des catalogues qui référencent des données non-utilisateurs dans vos campagnes Braze via Liquid."
---

# Créer un catalogue

> La création d’un catalogue implique l’importation d’un fichier CSV de données non-utilisateurs dans Braze. Cela vous permet ensuite d'accéder à ces informations pour enrichir vos messages. Vous pouvez ajouter n’importe quel type de données à un catalogue. Ces données sont généralement des métadonnées de votre entreprise, telles que des informations sur les produits pour une entreprise Ecommerce, ou des informations sur le cours pour un fournisseur de formation.

## Cas d’utilisation

Les cas d'utilisation des catalogues sont les suivants

- Produits
- Services
- Alimentation
- Événements à venir
- Musique
- Emballages

Une fois ces informations importées, vous pouvez commencer à y accéder dans les messages d'une manière similaire à l'accès aux attributs personnalisés ou aux propriétés d'événement personnalisé via Liquid.

## Types de données pris en charge {#supported-data-types}

Le tableau suivant répertorie les types de données de catalogue pris en charge et explique comment les créer ou les mettre à jour.

| Type de données    | Description                                   | Disponible via téléchargement CSV | Disponible via API et CDI |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| Chaîne de caractères       | Une séquence de caractères.                     | Oui                    | Oui                     |
| Nombre       | Une valeur numérique, entière ou float.     | Oui                    | Oui                     |
| Valeur booléenne      | Une `false`valeur A`true`ou B.                    | Oui                    | Oui                     |
| Date         | Une chaîne de caractères formatée au format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).                        | Oui                    | Oui                     |
| Object JSON  | Objet imbriqué contenant des paires clé-valeur. Peut être affiché sur la plateforme, mais ne peut être créé ou mis à jour que via l'API ou le CDI.         | ⛔ Non                     | Oui                     |
| Tableau de chaînes de caractères | Une liste de chaînes de caractères. Peut être affiché sur la plateforme, mais ne peut être créé ou mis à jour que via l'API ou le CDI. Maximum de 100 éléments. | ⛔ Non                     | Oui                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Création d’un catalogue

Pour créer un catalogue, veuillez vous rendre dans **Paramètres des données** > **Catalogues**, puis sélectionnez **Créer un nouveau catalogue** et choisissez l'une des options suivantes :

{% tabs local %}
{% tab Upload CSV %}
### Étape 1 : Veuillez vérifier votre fichier CSV.

Avant de télécharger votre fichier CSV, veuillez vous assurer qu'il répond aux exigences suivantes :

| Exigences relatives aux fichiers CSV | Détails |
|-----------------|---------|
| En-têtes | La première colonne du fichier CSV doit être nommée `id`, et chaque ligne doit contenir une valeur `id`unique. |
| Colonnes | Un fichier CSV peut contenir jusqu'à 1 000 champs (colonnes), et chaque nom de colonne peut comporter jusqu'à 250 caractères. |
| Taille du fichier | Pour les forfaits gratuits, la taille totale de tous les fichiers CSV d'une entreprise est limitée à 100 Mo. Pour les plans Pro, la taille maximale d'un fichier CSV est de 2 Go. |
| Valeurs des champs | Chaque cellule (valeur de champ) peut contenir jusqu'à 5 000 caractères. |
| Caractères valides | La`id`colonne et toutes les valeurs d'en-tête ne peuvent contenir que des lettres, des chiffres, des tirets et des traits de soulignement. |
| Types de données | Les types de données pris en charge pour les téléchargements CSV comprennent les chaînes de caractères, les nombres, les booléens et les heures. Pour obtenir la liste complète des types de données, y compris ceux disponibles uniquement via l'API et le CDI, veuillez consulter la section [Types de données pris en charge](#supported-data-types). |
| Formatage | Veuillez formater tout le texte en minuscules afin de garantir la cohérence. |
| Encodage | Veuillez enregistrer et télécharger le fichier CSV en utilisant l'encodage UTF-8. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Vous avez besoin de plus d’espace pour accueillir vos fichiers CSV ? Contactez votre gestionnaire de compte Braze pour plus d’informations.
{% endalert %}

### Étape 2 : Charger un fichier CSV

Glissez-déposez votre fichier dans la zone de téléchargement ou sélectionnez **Télécharger CSV** et choisissez votre fichier.

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Veuillez sélectionner un type de données pour chaque colonne.

{% alert note %}
Ce type de données ne peut pas être modifié après la configuration de votre catalogue. En outre, la valeur `NULL` n'est pas prise en charge dans le téléchargement CSV et sera traitée comme une chaîne de caractères.
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Veuillez saisir un nom et une description facultative pour votre catalogue. Veuillez tenir compte des exigences suivantes lorsque vous nommez votre catalogue :

  - Doit être unique
  - Maximum de 250 caractères
  - Peut uniquement inclure des chiffres, des lettres, des traits d’union et des traits de soulignement

{% alert tip %}
Vous pouvez également [utiliser des modèles dans un nom de catalogue](#template-catalog-names), ce qui vous permet de générer dynamiquement des noms de catalogue en fonction de variables telles que la langue ou la campagne.
{% endalert %}

![Un catalogue nommé/assets/img_archive/in_browser_catalog.pngimage_buster"my_catalog".]({%%}){: style="max-width:80%;"}

Sélectionnez **Process Catalog** pour créer le catalogue.

{% alert important %}
Votre fichier CSV peut être rejeté si vous dépassez votre [seuil](#tiers).
{% endalert %}

### Tutoriel : Création d'un catalogue à partir d'un fichier CSV

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
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Régénération</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Nous allons créer le catalogue en téléchargeant un fichier CSV. Les types de données pour `id`, `title`, `price` et `image_link` sont respectivement une chaîne de caractères, une chaîne de caractères, un nombre et une chaîne de caractères. 

{% alert note %}
Ce type de données ne peut pas être modifié après la configuration de votre catalogue.
{% endalert %}

![Quatre noms de colonnes du catalogue : « ID », « title », « price »,/assets/img_archive/catalog_data_type.pngimage_buster"image_link".]({%%}){: style="max-width:85%;"}

Ensuite, nous nommerons ce catalogue"games_catalog"et sélectionnerons le bouton **Traiter le catalogue**. Braze vérifie alors que le catalogue ne contient pas d'erreurs avant de le créer.

![Un catalogue nommé/assets/img_archive/catalog_new_name.pngimage_buster"games_catalog".]({%%}){: style="max-width:85%;"}

Notez que vous ne pourrez pas modifier ce nom après la création du catalogue. Vous pouvez supprimer un catalogue et télécharger à nouveau une version mise à jour en utilisant le même nom de catalogue.

Après avoir créé le catalogue, vous pouvez commencer à y faire référence [dans une campagne]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/).
{% endtab %}

{% tab Create in browser %}
### Conditions préalables

Avant de pouvoir modifier ou créer des catalogues dans le navigateur, vous devez disposer des [autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) suivantes pour votre espace de travail :

- Afficher les catalogues
- Modifier les catalogues
- Exporter des catalogues
- Supprimer les catalogues

{% multi_lang_include deprecations/user_permissions.md %}

### Étape 1 : Veuillez saisir les détails du catalogue

Veuillez saisir un nom et une description facultative pour votre catalogue. Veuillez tenir compte des exigences suivantes lorsque vous nommez votre catalogue :

- Doit être unique
- Maximum de 250 caractères
- Peut uniquement inclure des chiffres, des lettres, des traits d’union et des traits de soulignement

{% alert tip %}
Vous pouvez également [utiliser des modèles dans un nom de catalogue](#template-catalog-names), ce qui vous permet de générer dynamiquement des noms de catalogue en fonction de variables telles que la langue ou la campagne.
{% endalert %}

![Un catalogue nommé/assets/img_archive/in_browser_catalog.pngimage_buster"my_catalog".]({%%}){: style="max-width:80%;"}

### Étape 2 : Veuillez créer votre catalogue

Veuillez sélectionner votre catalogue dans la liste, puis choisissez **Mettre à jour le catalogue** > **Ajouter des champs**. Veuillez saisir le **nom du** **champ** et utiliser le menu déroulant pour sélectionner le type de données. Répétez l’opération en fonction de vos besoins.

![Deux exemples de champs : « note » et « nom ».]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Veuillez sélectionner **Mettre à jour le catalogue** > **Ajouter des éléments** pour ajouter un élément à votre catalogue en saisissant les informations dans les champs que vous avez précédemment ajoutés. Ensuite, veuillez sélectionner **« Enregistrer l'élément** » ou **« Enregistrer et ajouter un autre** » pour continuer à ajouter vos éléments.

![Veuillez ajouter un article au catalogue.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze traite les valeurs temporelles sur la base de l'horodatage du tableau de bord. Par exemple, si une colonne a pour valeur « 13/03/2024 » et que votre fuseau horaire est celui du Pacifique, cette heure sera importée dans Braze sous la forme « 13 mars 2024, 17 h 00 PM ».
{% endalert %}
{% endtab %}
{% endtabs %}

## Types de données du catalogue

Les catalogues prennent en charge divers types de données afin de vous aider à organiser et structurer efficacement vos données. Le tableau suivant décrit chaque type de données pris en charge et son mappage avec les noms de types CSV et API :

| Type de données | Format | Exemple | Description |
|-----------|--------|---------|-------------|
| Chaîne de caractères | Texte | `"Hello World"` | Toute séquence de caractères utilisée pour les données textuelles telles que les noms, les descriptions et les ID. Équivalent au`string`type dans les importations CSV et API. |
| Date | ISO 8601 ou horodatage unix (en secondes) | `"2024-03-15T14:30:00Z"` | Valeurs de date et d'heure au format ISO 8601 ou horodatage unix en secondes. Équivalent au type`time` dans l'API et au`datetime`type dans les importations CSV. |
| Valeur booléenne | `true` ou `false` | `true` | Valeurs logiques représentant des états vrais ou faux. Équivalent au`boolean`type dans les importations CSV et API. |
| Nombre | Nombre entier ou décimal | `42` ou `19.99` | Valeurs numériques, y compris les nombres entiers et les nombres à float pour les prix, les quantités, les évaluations, etc. Équivalent aux types`integer`  `float`et  dans les importations CSV et au`number`type  dans l'API. |
| Objet | Object JSON | `{"key": "value", "price": 10}` | Structures de données imbriquées complexes. La `type`valeur de l'API est `object`. Affiché sous forme d'objet JSON dans le tableau de bord. Uniquement disponible via API ou Cloud Data Ingestion (CDI). |
| Tableau | Tableau de chaînes de caractères | `["red", "blue", "green"]` | Listes de valeurs de chaîne de caractères. La `type`valeur de l'API est `array`. Affiché sous forme de tableau de chaînes de caractères dans le tableau de bord. Uniquement disponible via l'API ou le CDI. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Utilisation de modèles dans les noms de catalogues {#template-catalog-names}

Lorsque vous nommez votre catalogue, vous pouvez également utiliser des modèles dans le nom du catalogue. Cela vous permet de générer de manière dynamique des noms de catalogues en fonction de variables telles que la langue ou la campagne. Par exemple, vous pouvez utiliser les éléments suivants :

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Gérer les catalogues

### Dans le tableau de bord

Pour mettre à jour votre catalogue après avoir téléchargé un fichier CSV ou créé un catalogue dans le navigateur, veuillez sélectionner **Mettre à jour le catalogue > Télécharger un fichier CSV**, puis choisir de mettre à jour, d'ajouter ou de supprimer des éléments dans votre catalogue.

### Utiliser l'API REST

Au fur et à mesure que vous créez des catalogues, vous pouvez également utiliser l'[endpoint Lister des catalogues]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) pour obtenir la liste des catalogues d'un espace de travail.

L'API REST prend en charge tous [les types de données du catalogue](#supported-data-types), y compris les objets JSON et les tableaux de chaînes de caractères. Les objets JSON et les tableaux de chaînes de caractères ne peuvent être créés ou mis à jour que via l'API REST.

### Utilisation de l'ingestion de données dans le cloud

Vous pouvez gérer vos catalogues via [l'ingestion de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) en synchronisant régulièrement les données de vos catalogues directement depuis votre entrepôt de données (tel que Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric ou S3).

## Gérer les articles du catalogue

En plus de gérer vos catalogues, vous pouvez également utiliser des endpoints synchrones et asynchrones pour gérer les articles du catalogue. Ils comprennent la possibilité d’modifier et de supprimer des articles du catalogue ainsi que d’afficher les détails d’un d’eux. 

Par exemple, si vous souhaitez modifier un produit de catalogue spécifique, vous pouvez utiliser l'[endpoint `/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Stockage de catalogues {#tiers}

La version gratuite de Catalogues prend en charge des tailles de fichiers CSV allant jusqu'à 100 Mo pour tous les fichiers CSV combinés de votre entreprise, tandis que la version Pro de Catalogues prend en charge des tailles de fichiers CSV allant jusqu'à 2 Go pour un seul fichier CSV.

{% alert important %}
Les droits d’utilisation des packages indiqués dans le tableau de bord de Braze sont arrondis à l'unité la plus proche à des fins visuelles. Toutefois, vous avez toujours droit à l'intégralité des droits d’utilisation achetés. Pour demander une mise à niveau pour le stockage des catalogues, contactez votre gestionnaire de compte Braze.
{% endalert %}

#### Version gratuite

La taille de stockage pour la version gratuite des catalogues est de 100 Mo maximum. Vous pouvez avoir un nombre illimité d'articles tant qu'ils ne dépassent pas 100 Mo. 

#### Catalogues Pro

Au niveau de l'entreprise, le stockage maximum pour Catalogues Pro est basé sur la taille des données du catalogue. Les options de taille de stockage sont les suivantes : 5 Go, 10 Go ou 15 Go. Notez que l'espace de stockage de la version gratuite (100 Mo) est inclus dans chacun de ces plans.
