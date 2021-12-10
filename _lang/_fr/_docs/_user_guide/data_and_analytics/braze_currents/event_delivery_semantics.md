---
nav_title: Sémantiques de livraison d'événement
article_title: Sémantiques de livraison d'événement
page_order: 3
page_type: Référence
description: "Cet article de référence décrit la façon dont les Monnaies gèrent les données d’événements à plat que nous envoyons à Data Warehouse partenaires."
tool: Courants
---

# Sémantique de livraison d'événements

> Cet article décrit comment Monnaies gère les données d’événements à plat que nous envoyons à Data Warehouse partenaires.

Les courants de stockage de données sont des flux continus de données de notre plate-forme vers un seau de stockage sur l'une de nos [connexions partenaires d'entrepôt de données]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).

Les courants écrivent des fichiers Avro dans votre seau de stockage à des seuils réguliers, vous permettant de traiter et d’analyser les données de l’événement à l’aide de votre propre outil Business Intelligence.

{% alert important %}
Veuillez noter que ce contenu **s'applique uniquement aux données d'événement de fichier à plat que nous envoyons aux partenaires de Data Warehouse (Google Cloud Storage, Amazon S3, et Microsoft Azure Blob Storage)**. Pour le contenu qui s'applique aux autres partenaires, veuillez consulter [leurs pages respectives]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).
{% endalert %}


## Livraison au moins une fois

En tant que système à haut débit, les courants garantissent la livraison d’événements au moins une fois, ce qui signifie que les événements en double peuvent parfois être écrits dans votre compartiment de stockage. Cela peut se produire lorsque des événements sont retraités de notre file d'attente pour n'importe quelle raison.

Si vos cas d'utilisation requièrent une livraison exacte, vous pouvez utiliser le champ d'identification unique qui est envoyé avec chaque événement (`id`) pour dédupliquer les événements. Puisque le fichier laisse notre contrôle une fois qu'il est écrit dans votre compartiment de stockage, nous n'avons aucun moyen de garantir la déduplication de notre bout.

## Horodatage

Tous les horodatages exportés par les courants sont envoyés dans le fuseau horaire utc. Pour certains événements où il est disponible, un champ de fuseau horaire est également inclus, qui délivre le format iana du fuseau horaire local de l'utilisateur au moment de l'événement.

## Avro

Les intégrations de stockage de données Braze Monnaie affichent des données au format `.avro`. nous avons choisi [avro](https://avro.apache.org/) parce que c'est un format de données flexible qui supporte nativement l'évolution du schéma et est supporté par une grande variété de produits de données:

-   Avro est soutenu par presque tous les grands entrepôts de données.
-   Dans le cas où vous souhaitez laisser vos données en S3, Avro comprime mieux que CSV et JSON, de sorte que vous payez moins pour le stockage et peut potentiellement utiliser moins de CPU pour analyser les données.
-   Avro nécessite des schémas lorsque les données sont écrites ou lues. Les schémas peuvent être évolués au fil du temps pour gérer l'ajout de champs sans se casser.

Les courants vont créer un fichier pour chaque type d'événement en utilisant le format ci-dessous:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.intégration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration<integration-id>+<partition>+<offset>.avro
```

_Impossible de voir le code à cause de la barre de défilement ? Voyez comment résoudre ce problème [ici]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)._

| Segment de nom de fichier            | Définition                                                                                                                                                                              |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<your-bucket-prefix>`         | Le préfixe pour cette intégration de courants.                                                                                                                                          |
| `<cluster-identifier>`         | Pour une utilisation interne par Braze. Sera une chaîne de caractères telle que "prod-01", "prod-02", "prod-03", ou "prod-04". Tous les fichiers auront le même identifiant de cluster. |
| `<connection-type-identifier>` | L'identifiant du type de connexion. Les options sont "S3", "AzureBlob", ou "GCS".                                                                                                       |
| `<integration-id>`             | L'ID unique pour cette intégration de Courants.                                                                                                                                         |
| `<event-type>`                 | Le type d'événement dans le fichier (voir la liste des événements ci-dessous).                                                                                                          |
| `<date>`                       | L'heure où les événements sont mis en file d'attente dans notre système pour être traités. Formaté AAAA-MM-DD-HH.                                                                       |
| `<schema-id>`                  | Utilisé pour la version `.avro` schémas pour la rétrocompatibilité et l'évolution du schéma. Nombre entier.                                                                             |
| `<zone>`                       | Pour une utilisation interne par Braze. Une seule lettre.                                                                                                                               |
| `<partition>`                  | Pour une utilisation interne par Braze. Nombre entier.                                                                                                                                  |
| `<offset>`                     | Pour une utilisation interne par Braze. Nombre entier.                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Les conventions de nommage des fichiers peuvent changer à l'avenir, Braze recommande de rechercher toutes les clés de votre compartiment qui ont un préfixe de &lt;your-bucket-prefix&gt;.
{% endalert %}

### Seuil d'écriture Avro

Les fichiers de données seront écrits dans votre compartiment de stockage une fois que vous aurez cliqué sur _l'un des seuils fixés_, que ce soit le premier qui se produira :

| Partenaire                   | Seuil d'écriture                                             |
| ---------------------------- | ------------------------------------------------------------ |
| Amazon AWS S3                | Toutes les 5 minutes. <br> Tous les 15 000 événements. |
| Microsoft Azure Blob Storage | Toutes les 5 minutes. <br> Tous les 15 000 événements. |
| Stockage Google Cloud        | Toutes les 5 minutes. <br> Tous les 15 000 événements. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Les courants n'écriront jamais de fichiers vides.
{% endalert %}

### Changements de schéma Avro

De temps à autre, Braze peut apporter des modifications au schéma Avro lorsque des champs sont ajoutés, modifiés ou supprimés. Pour nos buts ici, il y a deux types de changements: la rupture et la non-rupture. Dans tous les cas, le `<schema-id>` sera avancé pour indiquer que le schéma a été mis à jour.

#### Changements sans rupture

Lorsqu'un champ est ajouté au schéma Avro, nous considérons qu'il s'agit d'un changement sans rupture. Les champs ajoutés seront toujours "optionnels" les champs Avro (i.e. avec une valeur par défaut de `null`), donc ils "correspondent" les schémas plus anciens selon la spécification [de résolution du schéma Avro](http://avro.apache.org/docs/current/spec.html#schema+resolution). Ces ajouts ne devraient pas affecter les processus de ETL existants, car le champ sera simplement ignoré jusqu'à ce qu'il soit ajouté à votre processus ETL.

{% alert important %}
Nous recommandons que votre configuration ETL soit explicite sur les champs qu'elle traite pour éviter de casser le flux lorsque de nouveaux champs sont ajoutés.
{% endalert %}

Bien que nous nous efforcions de vous avertir à l'avance en cas de modification, nous pouvons inclure des modifications du schéma à tout moment.

#### Changements en cours

Lorsqu'un champ est retiré ou modifié dans le schéma Avro, nous considérons qu'il s'agit d'un changement de rupture. La rupture des changements peut nécessiter des modifications aux processus de ETL existants, car les champs utilisés ne peuvent plus être enregistrés comme prévu.

Toutes les modifications du schéma seront communiquées avant le changement.
