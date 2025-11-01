---
nav_title: "Sémantique de réception/distribution d'événements"
article_title: "Sémantique de réception/distribution d'événements"
page_order: 3
page_type: reference
description: "Cet article de référence décrit et définit la manière dont Currents gère les données d'événements en fichier plat que nous envoyons aux partenaires de stockage de l'entrepôt de données."
tool: Currents

---

# Sémantique de réception/distribution d'événements

> Cette page décrit et définit la manière dont Currents gère les données d'événements sous forme de fichiers plats que nous envoyons aux partenaires de stockage de l'entrepôt de données.

Currents for Data Storage est un flux continu de données transmis de notre plateforme à un compartiment de stockage sur l'une des [connexions de]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) nos [partenaires d']({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)entrepôt de données. Currents écrit des fichiers Avro dans votre compartiment de stockage à des seuils réguliers, ce qui vous permet de traiter et d'analyser les données d'événements avec votre propre ensemble d'outils de veille stratégique (BI).

{% alert important %}
Ce contenu **ne s'applique qu'aux données d'événements sous forme de fichiers plats que nous envoyons aux partenaires de Data Warehouse Storage (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage).** <br><br>Pour le contenu qui s'applique à d'autres partenaires, reportez-vous à notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et consultez leurs pages respectives.
{% endalert %}

## Réception/distribution au moins une fois

En tant que système à haut débit, Currents assure une réception/distribution des événements "au moins une fois", ce qui signifie que des événements en double peuvent occasionnellement être écrits dans votre compartiment de stockage. Cela peut se produire lorsque des événements sont retirés de notre file d'attente pour une raison quelconque.

Si vos cas d'utilisation nécessitent une réception/distribution "exactement une fois", vous pouvez utiliser le champ d'identification unique qui est envoyé avec chaque événement (`id`) pour dédupliquer les événements. Étant donné que le fichier échappe à notre contrôle lorsqu'il est écrit dans votre compartiment de stockage, nous n'avons aucun moyen de garantir la déduplication de notre côté.

## Horodatage

Tous les horodatages exportés par Currents sont envoyés dans le fuseau horaire UTC. Pour certains événements où il est disponible, un champ "fuseau horaire" est également inclus, qui fournit le format IANA (Internet Assigned Numbers Authority) du fuseau horaire local de l'utilisateur au moment de l'événement.

### Temps de latence

Les événements envoyés à Braze par l'intermédiaire du SDK ou de l'API peuvent inclure un horodatage du passé. L'exemple le plus notable est celui des données du SDK qui sont mises en file d'attente, par exemple lorsqu'il n'y a pas de connectivité mobile. Dans ce cas, l'horodatage de l'événement reflétera le moment où l'événement a été généré. Cela signifie qu'un pourcentage d'événements apparaîtra comme ayant une latence élevée.

## Format Apache Avro

Les intégrations currents de Braze produisent des données au format `.avro`. Nous avons choisi [Apache Avro](https://avro.apache.org/) parce qu'il s'agit d'un format de données flexible qui supporte nativement l'évolution des schémas et qui est pris en charge par une grande variété de produits de données : 

- Avro est pris en charge par presque tous les grands entrepôts de données.
- Dans le cas où vous souhaiteriez laisser vos données dans S3, Avro compresse mieux que CSV et JSON, vous payez donc moins pour le stockage et pouvez potentiellement utiliser moins de CPU pour analyser les données.
- Avro exige des schémas lorsque des données sont écrites ou lues. Les schémas peuvent être modifiés au fil du temps pour gérer l'ajout de champs sans rupture.

Currents créera un fichier pour chaque type d'événement en utilisant le format suivant :

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Vous ne pouvez pas voir le code à cause de la barre de défilement ? Apprenez à résoudre ce problème [ici.]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)
{% endalert %}

|Segmentation du nom de fichier |Définition|
|---|---|
| `<your-bucket-prefix>` | Le jeu de préfixes pour cette intégration currents. |
| `<cluster-identifier>` | Réservé à l'usage interne de Braze. Il s'agit d'une chaîne de caractères telle que "prod-01", "prod-02", "prod-03" ou "prod-04". Tous les fichiers auront le même identifiant de cluster.|
| `<connection-type-identifier>` | L'identifiant du type de connexion. Les options sont "S3", "AzureBlob" ou "GCS". |
| `<integration-id>` | L'ID unique de cette intégration currents. |
| `<event-type>` | Le type d'événement dans le fichier. |
| `<date>` | L'heure à laquelle les événements sont mis en file d'attente dans notre système pour être traités dans le fuseau horaire UTC. Formaté YYYY-MM-DD-HH. |
| `<schema-id>` | Utilisé pour la version des schémas `.avro` pour la compatibilité ascendante et l'évolution des schémas. Entier. |
| `<zone>` | Réservé à l'usage interne de Braze. |
| `<partition>` | Réservé à l'usage interne de Braze. Entier. |
| `<offset>`| Réservé à l'usage interne de Braze. Entier. Notez que différents fichiers envoyés au cours de la même heure auront un paramètre `<offset>` différent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Les conventions de dénomination des fichiers peuvent changer à l'avenir. Braze recommande de rechercher toutes les clés de votre compartiment dont le préfixe est <your-bucket-prefix>.
{% endalert %}

### Seuil d'écriture Avro

Dans des circonstances normales, Braze écrit des fichiers de données dans votre compartiment de stockage toutes les 5 minutes ou tous les 15 000 événements, au premier des deux termes échus. En cas de forte charge, nous pouvons écrire des fichiers de données plus importants pouvant contenir jusqu'à 100 000 événements par fichier.

{% alert important %}
Les courants n'écrivent jamais de fichiers vides.
{% endalert %}

### Modifications du schéma Avro

De temps à autre, Braze peut apporter des modifications au schéma Avro lorsque des champs sont ajoutés, modifiés ou supprimés. Pour ce qui nous intéresse ici, il y a deux types de changements : les changements qui rompent et ceux qui ne rompent pas. Dans tous les cas, le site `<schema-id>` sera avancé pour indiquer que le schéma a été mis à jour. Les événements courants écrits sur Azure Blob Storage, Google Cloud Storage et Amazon S3 écriront l'adresse `<schema-id>` dans le chemin d'accès. Par exemple `<your-bucket-name0>/<currents-integration-id>/<event-type>/<date-of-event>/<schema-id>/<environment>/<avro-file>`.

#### Changements irréversibles

Lorsqu'un champ est ajouté au schéma Avro, nous considérons qu'il s'agit d'une modification sans rupture. Les champs ajoutés seront toujours des champs Avro "facultatifs" (par exemple avec une valeur par défaut de `null`), de sorte qu'ils "correspondront" aux anciens schémas conformément à la [spécification de résolution des schémas Avro](http://avro.apache.org/docs/current/spec.html#schema+resolution). Ces ajouts ne devraient pas affecter les processus d'extraction, de transformation et de chargement (ETL) existants, car le champ sera simplement ignoré jusqu'à ce qu'il soit ajouté à votre processus ETL. 

{% alert important %}
Nous recommandons que votre configuration extraire, transformer, soit explicite sur les champs qu'elle traite pour éviter d'interrompre le flux lorsque de nouveaux champs sont ajoutés.
{% endalert %}

Bien que nous nous efforcions de vous avertir à l'avance pour toutes les modifications, nous pouvons à tout moment apporter des changements non irréversibles au schéma.

#### Changements en cours

Lorsqu'un champ est supprimé ou modifié dans le schéma Avro, nous considérons qu'il s'agit d'un changement radical. Les ruptures peuvent nécessiter des modifications des processus d'extraire, transformer, car les champs qui étaient utilisés peuvent ne plus être enregistrés comme prévu.

Toutes les modifications importantes apportées au schéma seront communiquées à l'avance.
