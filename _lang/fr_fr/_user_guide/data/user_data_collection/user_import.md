---
nav_title: Importation d’utilisateurs
article_title: Importation d’utilisateurs
page_order: 4
description: "Découvrez les différentes options d'importation d'utilisateurs de Braze, comme l'importation CSV, l'API REST, l'ingestion de données dans le cloud, et plus encore."

---
# User Import

> Découvrez les différentes options d'importation d'utilisateurs de Braze, comme l'importation CSV, l'API REST, l'ingestion de données dans le cloud, et plus encore.

## A propos de la validation HTML

Gardez à l'esprit que Braze ne nettoie pas, ne valide pas et ne reformate pas les données HTML lors de l'importation, ce qui signifie que les tags de script doivent être supprimés de toutes les données d'importation que vous utilisez pour la personnalisation Web.

Lorsque vous importez dans Braze des données spécifiquement destinées à la personnalisation dans un navigateur web, veillez à ce qu'elles soient dépourvues de HTML, de JavaScript ou de toute autre étiquette de script susceptible d'être utilisée à des fins malveillantes lorsqu'elles sont affichées dans un navigateur web.

Pour le HTML, vous pouvez également utiliser les filtres Liquid de Braze (`strip_html`) afin d'extraire le texte rendu du HTML. Par exemple :

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Options d'importation

### Importation d’un fichier CSV Braze

Vous pouvez utiliser l'importation CSV pour enregistrer et mettre à jour les événements personnalisés et les attributs utilisateurs suivants. Pour commencer, consultez la section [Importation de fichiers CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

|Type|Définition|Exemple|Taille maximale du fichier|
|---|---|---|---|
|Attributs par défaut|Attributs réservés de l'utilisateur reconnus par Braze.|`first_name`, `email`|500 MO|
|Attributs personnalisés|Attributs de l'utilisateur uniques à votre entreprise.|`last_destination_searched`|500 MO|
|Événements personnalisés|Événements uniques à votre entreprise qui représentent des actions de l'utilisateur.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Importation CSV d’un utilisateur Lambda

Vous pouvez utiliser notre script d'importation CSV S3 Lambda sans serveur pour télécharger les attributs des utilisateurs dans Braze. Cette solution fonctionne comme un téléchargeur CSV où vous déposez vos CSV dans un compartiment S3, et les scripts les téléchargent via notre API.

Le temps d'exécution estimé pour un fichier de 1 000 000 de lignes devrait être d'environ cinq minutes. Pour plus d'informations, reportez-vous à la section [Importation d'un attribut utilisateur au format CSV vers Braze.](https://www.braze.com/docs/user_guide/data/cloud_ingestion/) 

### API REST

Utilisez l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour enregistrer des événements personnalisés, des attributs utilisateurs et des achats pour les utilisateurs.

### Ingestion de données cloud

Utilisez l'[ingestion de données de Braze Cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/) pour importer et mettre à jour les attributs des utilisateurs.

## Les e-mails transactionnels légalement requis

{% multi_lang_include email-via-sms-warning.md %}
