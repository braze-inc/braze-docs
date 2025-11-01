---
nav_title: "Création d'un catalogue"
article_title: "Création d'un catalogue"
alias: "/catalogs/"
page_order: 1
description: "Cet article de référence explique comment créer des catalogues qui référencent des données non-utilisateurs dans vos campagnes Braze via Liquid."
---

# Création d'un catalogue

> La création d'un catalogue implique l'importation d'un fichier CSV de données non-utilisateurs dans Braze. Cela vous permet ensuite d'accéder à ces informations pour enrichir vos messages. Vous pouvez introduire n'importe quel type de données dans un catalogue. Ces données sont généralement des métadonnées de votre entreprise, telles que des informations sur les produits pour une entreprise de commerce électronique ou des informations sur les cours pour un prestataire de services éducatifs.

## Cas d'utilisation

Les cas d'utilisation des catalogues sont les suivants

- Produits
- Services
- Alimentation
- Événements à venir
- Musique
- Emballages

Une fois ces informations importées, vous pouvez commencer à y accéder dans les messages d'une manière similaire à l'accès aux attributs personnalisés ou aux propriétés d'événement personnalisé via Liquid.

## Création d'un catalogue

Pour créer un catalogue, accédez à **Paramètres des données** > **Catalogues**, puis sélectionnez **Créer un nouveau catalogue** et choisissez l'une des options suivantes :

{% tabs local %}
{% tab Upload CSV %}
### Étape 1 : Examinez votre fichier CSV

Avant de télécharger votre fichier CSV, assurez-vous qu'il remplit les conditions suivantes :

| Exigence CSV | Détails |
|-----------------|---------|
| En-têtes | La première colonne du fichier CSV doit être nommée `id`, et chaque ligne doit avoir une valeur unique `id`. |
| Colonnes | Un fichier CSV peut comporter un maximum de 1 000 champs (colonnes), et chaque nom de colonne peut comporter jusqu'à 250 caractères. |
| Taille du fichier | Pour les plans gratuits, la taille totale de tous les fichiers CSV d'une entreprise est limitée à 100 Mo. Pour les plans Pro, la taille maximale d'un fichier CSV est de 2 Go. |
| Valeurs des champs | Chaque cellule (valeur du champ) peut contenir jusqu'à 5 000 caractères. |
| Caractères valables | La colonne `id` et toutes les valeurs d'en-tête ne peuvent contenir que des lettres, des chiffres, des traits d'union et des traits de soulignement. |
| Types de données | Les types de données pris en charge pour le téléchargement d'un fichier CSV sont les suivants : chaîne de caractères, entier, float, booléen ou date. |
| Formatage | Formulez tout le texte en minuscules pour maintenir la cohérence. |
| Encodage | Enregistrez et téléchargez le fichier CSV en utilisant le codage UTF-8. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Vous avez besoin de plus d'espace pour vos fichiers CSV ? Contactez votre gestionnaire de compte Braze pour plus d'informations sur la mise à jour de vos catalogues.
{% endalert %}

### Étape 2 : Télécharger le CSV

Glissez-déposez votre fichier dans la zone de téléchargement ou sélectionnez **Télécharger CSV** et choisissez votre fichier.

\![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Sélectionnez un type de données pour chaque colonne.

{% alert note %}
Ce type de données ne peut pas être modifié une fois que vous avez configuré votre catalogue. En outre, la valeur `NULL` n'est pas prise en charge dans le téléchargement CSV et sera traitée comme une chaîne de caractères.
{% endalert %}

\![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Saisissez un nom et une description facultative pour votre catalogue. Gardez à l'esprit les exigences suivantes lorsque vous donnez un nom à votre catalogue :

  - Doit être unique
  - Maximum de 250 caractères
  - Ne peut comprendre que des chiffres, des lettres, des traits d'union et des traits de soulignement.

{% alert tip %}
Vous pouvez également [utiliser des modèles dans le nom d'un catalogue](#template-catalog-names), ce qui vous permet de générer dynamiquement des noms de catalogue en fonction de variables telles que la langue ou la campagne.
{% endalert %}

\![Un catalogue nommé "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Sélectionnez **Process Catalog** pour créer le catalogue.

{% alert important %}
Votre fichier CSV peut être rejeté si vous dépassez votre [seuil.](#tiers)
{% endalert %}

### Tutoriel : Création d'un catalogue à partir d'un fichier CSV

Pour ce tutoriel, nous utilisons un catalogue qui répertorie deux jeux, leur coût et un lien vers une image.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">titre</th>
    <th class="tg-0pky">prix</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Contes</td>
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

Nous allons créer le catalogue en téléchargeant un fichier CSV. Les types de données pour `id`, `title`, `price` et `image_link` sont respectivement chaîne, chaîne de caractères, nombre et chaîne. 

{% alert note %}
Ce type de données ne peut pas être modifié une fois que vous avez configuré votre catalogue.
{% endalert %}

\![Quatre noms de colonnes du catalogue : "id", "title", "price", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Ensuite, nous nommerons ce catalogue "games_catalog" et nous sélectionnerons le bouton **Traiter le catalogue.**  Ensuite, Braze vérifie que le catalogue ne contient pas d'erreurs avant de le créer.

\![Un catalogue nommé "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Notez que vous ne pourrez pas modifier ce nom après la création du catalogue. Vous pouvez supprimer un catalogue et télécharger à nouveau une version mise à jour en utilisant le même nom de catalogue.

Après avoir créé le catalogue, vous pouvez commencer à y faire référence [dans une campagne.]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/)
{% endtab %}

{% tab Create in browser %}
### Conditions préalables

Avant de pouvoir modifier ou créer des catalogues dans le navigateur, vous devez disposer de l'autorisation **Gérer le tableau de bord des catalogues**.

### Étape 1 : Entrez les détails du catalogue

Saisissez un nom et une description facultative pour votre catalogue. Gardez à l'esprit les exigences suivantes lorsque vous donnez un nom à votre catalogue :

- Doit être unique
- Maximum de 250 caractères
- Ne peut comprendre que des chiffres, des lettres, des traits d'union et des traits de soulignement.

{% alert tip %}
Vous pouvez également [utiliser des modèles dans le nom d'un catalogue](#template-catalog-names), ce qui vous permet de générer dynamiquement des noms de catalogue en fonction de variables telles que la langue ou la campagne.
{% endalert %}

\![Un catalogue nommé "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Étape 2 : Créez votre catalogue

Sélectionnez votre catalogue dans la liste, puis sélectionnez **Mettre à jour le catalogue** > **Ajouter des champs.** Saisissez le **nom du champ** et utilisez le menu déroulant pour sélectionner le type de données. Répétez l'opération autant de fois que nécessaire.

Deux exemples de champs "rating" et "name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Sélectionnez **Mettre à jour le catalogue** > **Ajouter des éléments** pour ajouter un élément à votre catalogue en saisissant les informations basées sur les champs que vous avez précédemment ajoutés. Ensuite, sélectionnez **Enregistrer l'élément** ou **Enregistrer et ajouter un autre** élément pour continuer à ajouter vos éléments.

\![Ajouter un article au catalogue.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze traite les valeurs temporelles sur la base de l'horodatage du tableau de bord. Par exemple, si une colonne a pour valeur "13/03/2024" et que votre fuseau horaire est celui du Pacifique, cette heure sera importée dans Braze sous la forme "12 mars 2024, 17:00 PM".
{% endalert %}
{% endtab %}
{% endtabs %}

## Utilisation de modèles dans les noms de catalogues {#template-catalog-names}

Lorsque vous nommez votre catalogue, vous pouvez également utiliser des modèles dans le nom du catalogue. Cela vous permet de générer dynamiquement des noms de catalogues en fonction de variables telles que la langue ou la campagne. Par exemple, vous pouvez utiliser les éléments suivants :

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Gestion des catalogues

### Dans le tableau de bord

Pour mettre à jour votre catalogue après avoir téléchargé un fichier CSV ou créé un catalogue dans le navigateur, sélectionnez **Mettre à jour le catalogue > Charger CSV**, puis choisissez de mettre à jour, d'ajouter ou de supprimer des éléments dans votre catalogue.

### Utilisation de l'API REST

Au fur et à mesure que vous créez des catalogues, vous pouvez également utiliser l'[endpoint List catalogs]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) pour obtenir la liste des catalogues d'un espace de travail.

Les types de données pris en charge pour l'utilisation de l'API sont les suivants : chaîne de caractères, entier, float, booléen ou date. Vous pouvez également télécharger des tableaux et des objets lorsque vous gérez vos catalogues avec l'API.

## Gérer les éléments du catalogue

Outre la gestion de vos catalogues, vous pouvez également utiliser des endpoints asynchrones et synchrones pour gérer les éléments du catalogue. Il permet notamment de modifier et de supprimer des éléments du catalogue et d'en répertorier les détails. 

Par exemple, si vous souhaitez modifier un article de catalogue individuel, vous pouvez utiliser l'[endpoint`/catalogs/catalog_name/items/item_id` ]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Stockage dans le catalogue {#tiers}

La version gratuite de Catalogues prend en charge des tailles de fichiers CSV allant jusqu'à 100 Mo pour tous les fichiers CSV combinés de votre entreprise, tandis que la version Pro de Catalogues prend en charge des tailles de fichiers CSV allant jusqu'à 2 Go pour un seul fichier CSV.

{% alert important %}
Le droit au forfait indiqué dans le tableau de bord de Braze est arrondi à l'unité la plus proche à des fins visuelles ; toutefois, vous avez toujours droit à l'intégralité du droit acheté. Pour demander une mise à niveau pour le stockage des catalogues, contactez votre gestionnaire de compte Braze.
{% endalert %}

#### Version gratuite

La taille de stockage pour la version gratuite des catalogues est de 100 Mo maximum. Vous pouvez avoir un nombre illimité d'articles tant qu'ils ne dépassent pas 100 Mo. 

#### Catalogues Pro

Au niveau de l'entreprise, le stockage maximum pour Catalogues Pro est basé sur la taille des données du catalogue. Les options de taille de stockage sont les suivantes : 5 Go, 10 Go ou 15 Go. Notez que l'espace de stockage de la version gratuite (100 Mo) est inclus dans chacun de ces plans.
