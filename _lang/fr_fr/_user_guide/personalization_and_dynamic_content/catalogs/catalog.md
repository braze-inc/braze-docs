---
nav_title: Création d’un catalogue
article_title: Création d’un catalogue
alias: "/catalogs/"
page_order: 1
description: "Cet article de référence explique comment créer des catalogues qui référencent des données non-utilisateurs dans vos campagnes Braze via Liquid."
---

# Création d’un catalogue

> La création d’un catalogue implique l’importation d’un fichier CSV de données non-utilisateurs dans Braze. Cela vous permet ensuite d'accéder à ces informations pour enrichir vos messages. Vous pouvez ajouter n’importe quel type de données à un catalogue. Ces données sont généralement des métadonnées de votre entreprise, telles que des informations sur les produits pour une entreprise de commerce électronique ou des informations sur les cours pour un prestataire de services éducatifs.

Voici quelques exemples d'utilisation courante des catalogues :

- Produits
- Services
- Alimentation
- Événements à venir
- Musique
- Emballages

Une fois ces informations importées, vous pouvez commencer à y accéder dans les messages de la même manière que pour accéder aux attributs personnalisés ou aux propriétés d’événements personnalisés via Liquid.

## Préparer votre fichier CSV

Avant de créer un catalogue, veillez à préparer votre fichier CSV si votre méthode de création de catalogue préférée est le téléchargement.

{% alert note %}
Vous avez besoin de plus d’espace pour accueillir vos fichiers CSV ? Contactez votre gestionnaire de compte Braze pour plus d’informations.
{% endalert %}

### Lignes directrices pour les fichiers CSV

Notez ces directives lors de la création de votre fichier CSV. La première colonne du fichier CSV doit être un en-tête de `id`et chaque article `id` doit être unique. Tous les autres noms de colonnes doivent être uniques. En outre, les limitations suivantes s’appliquent aux fichiers CSV du catalogue :

- Maximum de 1 000 champs (colonnes)
- Nom maximum de champ (colonne) de 250 caractères
- Maximum 100 Mo pour tous les fichiers CSV combinés dans votre entreprise (gratuit)
- Taille maximale du fichier CSV : 2 Go (Pro)
- Valeur maximale de champ (cellule) de 5 000 caractères
- Seuls les lettres, chiffres, traits d’union et traits de soulignement pour `id` et des valeurs d’en-tête

Nous vous recommandons également de formater tout le texte de vos fichiers CSV en minuscules. Assurez-vous d'encoder votre fichier CSV au format UTF-8 afin de pouvoir le télécharger avec succès à l'étape suivante.

## Sélectionner votre méthode

Pour créer un catalogue, allez dans **Paramètres des données** > **Catalogues**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **catalogues** sous **Données.**
{% endalert %}

Sélectionnez **Créer un catalogue**, puis choisissez de **charger un fichier CSV** ou de **créer dans le navigateur**.

### Méthode 1 : Charger un fichier CSV

1. Glissez-déposez votre fichier dans la zone de chargement, ou cliquez sur **Charger un fichier CSV** et choisissez votre fichier. <br>![][1]{: style="max-width:80%;"} <br><br>
2. Sélectionnez l’un des types de données suivants pour chaque colonne : booléen, nombre, chaîne de caractères ou temps.
<br> ![][9]{: style="max-width:80%;"} <br><br>
3. Nommez votre catalogue. Gardez à l’esprit les exigences suivantes pour le nom du catalogue :
- Doit être unique
- Maximum de 250 caractères
- Peut uniquement inclure des chiffres, des lettres, des traits d’union et des traits de soulignement<br><br>
4. (facultatif) Ajoutez une description pour le catalogue.
5. Cliquez sur **Traiter le catalogue** pour créer le catalogue.

{% alert note %}
Ce type de données ne peut pas être modifié après la configuration de votre catalogue.
{% endalert %}

Vous pouvez également utiliser des modèles dans le nom d'un catalogue. Par exemple, vous pouvez utiliser les éléments suivants :
{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

{% alert important %}
Votre fichier CSV peut être rejeté si vous dépassez votre [seuil](#tiers).
{% endalert %}

Vous pouvez également mettre à jour le fichier CSV après avoir choisi de créer un catalogue dans le navigateur. Cliquez sur **Mettre à jour le catalogue > Charger un fichier CSV**, puis choisissez de mettre à jour, d'ajouter ou de supprimer des produits dans votre catalogue.

### Méthode 2 : Créer dans le navigateur

1. Saisissez un nom pour votre catalogue. Gardez à l’esprit les exigences suivantes pour le nom de votre catalogue :
- Doit être unique
- Jusqu’à 250 caractères
- Peut uniquement inclure des chiffres, des lettres, des traits d’union et des traits de soulignement <br> ![Un catalogue nommé "mon_catalogue".][14]{: style="max-width:80%;"} <br><br>
2. (facultatif) Saisissez une description de votre catalogue.
3. Sélectionnez le catalogue que vous venez de créer dans la page **Catalogues** de la liste pour mettre à jour votre catalogue.
4. Sélectionnez **Mettre à jour le catalogue** > **Ajouter des champs** pour ajouter vos champs. Saisissez ensuite le **nom du champ** et utilisez le menu déroulant pour sélectionner le type de données. Répétez l’opération en fonction de vos besoins.<br> ![Deux exemples de champs "rating" et "name".][12]{: style="max-width:50%;"}<br><br>
5. Sélectionnez **Mettre à jour le catalogue** > **Ajouter des éléments** pour ajouter un élément à votre catalogue en saisissant les informations basées sur les champs que vous avez précédemment ajoutés. Ensuite, sélectionnez **Enregistrer l'élément** ou **Enregistrer et ajouter un autre** élément pour continuer à ajouter vos éléments. <br> ![Ajouter un article de catalogue.][13]{: style="max-width:50%;"}

Vous pouvez également télécharger un fichier CSV après avoir choisi de créer un catalogue dans le navigateur.

{% alert note %}
Braze traite les valeurs temporelles sur la base de l'horodatage du tableau de bord. Par exemple, si une colonne a pour valeur « 13/03/2024 » et que votre fuseau horaire est celui du Pacifique, cette heure sera importée dans Braze sous la forme « 13 mars 2024, 17 h 00 PM ».
{% endalert %}

#### Tutoriel : Création d'un catalogue à partir d'un fichier CSV

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

![Quatre noms de colonnes de catalogue : "id", "title", "price", "image_link".][9]{: style="max-width:85%;"}

Ensuite, nous appellerons ce catalogue « games_catalog » et cliquerons sur le bouton **Traiter le catalogue**. Braze vérifie alors que le catalogue ne contient pas d'erreurs avant de le créer.

![Un catalogue nommé "games_catalog".][11]{: style="max-width:85%;"}

Notez que vous ne pourrez pas modifier ce nom après la création du catalogue. Vous pouvez supprimer un catalogue et télécharger à nouveau une version mise à jour en utilisant le même nom de catalogue.

Après avoir créé le catalogue, vous pouvez commencer à y faire référence [dans une campagne]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/).

## Gérer les catalogues via l'API

Au fur et à mesure que vous créez des catalogues, vous pouvez également utiliser l'[endpoint Lister des catalogues]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) pour obtenir la liste des catalogues d'un espace de travail.

### Gérer les articles du catalogue

En plus de gérer vos catalogues, vous pouvez également utiliser des endpoints synchrones et asynchrones pour gérer les articles du catalogue. Ils comprennent la possibilité d’modifier et de supprimer des articles du catalogue ainsi que d’afficher les détails d’un d’eux. 

Par exemple, si vous souhaitez modifier un produit de catalogue spécifique, vous pouvez utiliser l'[endpoint `/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Niveaux du catalogue {#tiers}

Le tableau suivant décrit les différences entre la version gratuite et la version pro des catalogues :

| Secteur                                  | Version gratuite                                                                                                                                            | Catalogues Pro                                                                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Taille du fichier CSV                         | Jusqu'à 100 Mo pour tous les fichiers CSV combinés dans votre entreprise                                                                                        | Jusqu'à 2 Go pour un seul fichier CSV                                                                                                                   |
| Limite de caractères pour la valeur de l’article       | Jusqu’à 5 000 caractères en une seule valeur. Par exemple, si vous aviez un champ `description`, le nombre maximum de caractères dans le champ est de 5 000. | Jusqu’à 5 000 caractères en une seule valeur. Par exemple, si vous aviez un champ `description`, le nombre maximum de caractères dans le champ est de 5 000. |
| Limite de caractères pour le nom de la colonne d’article | Jusqu’à 250 caractères                                                                                                                                    | Jusqu’à 250 caractères                                                                                                                                    |
| Sélections                            | Jusqu'à 30 sélections par catalogue                                                                                                                         | Jusqu'à 30 sélections par catalogue                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Stockage du catalogue

{% alert important %}
Les droits d’utilisation des packages indiqués dans le tableau de bord de Braze sont arrondis à l'unité la plus proche à des fins visuelles. Toutefois, vous avez toujours droit à l'intégralité des droits d’utilisation achetés. Pour demander une mise à niveau pour le stockage des catalogues, contactez votre gestionnaire de compte Braze.
{% endalert %}

#### Version gratuite

La taille de stockage pour la version gratuite des catalogues est de 100 Mo maximum. Vous disposez d’un nombre illimité de produits, tant que cela ne dépasse pas 100 Mo. Les sélections contribueront à votre stockage. Plus une sélection est complexe, plus elle occupera de place. Il y aura également un décalage de taille entre les données du catalogue CSV et la représentation de ces données dans notre magasin de données.

#### Catalogues Pro

Au niveau de l'entreprise, le stockage maximum pour Catalogues Pro est basé sur la taille des données du catalogue. Les options de taille de stockage sont les suivantes : 5 Go, 10 Go ou 15 Go. Notez que l'espace de stockage de la version gratuite (100 Mo) est inclus dans chacun de ces plans.

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[7]: {% image_buster /assets/img_archive/create_catalog_option.png %}
[9]: {% image_buster /assets/img_archive/catalog_data_type.png %}
[11]: {% image_buster /assets/img_archive/catalog_new_name.png %}
[12]: {% image_buster /assets/img_archive/add_catalog_fields.png %}
[13]: {% image_buster /assets/img_archive/add_catalog_items.png %}
[14]: {% image_buster /assets/img_archive/in_browser_catalog.png %}
