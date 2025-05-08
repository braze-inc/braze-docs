---
nav_title: Sémantique des événements de livraison
article_title: Sémantique des événements de livraison
page_order: 3
page_type: reference
description: "Cet article de référence décrit et définit la manière dont Currents gère les données d'événements en fichier plat que nous envoyons aux partenaires de stockage de l'entrepôt de données."
tool: Currents

---

# Sémantique des événements de livraison

> Cette page décrit et définit la manière dont Currents gère les données d'événements sous forme de fichiers plats que nous envoyons aux partenaires de stockage de l'entrepôt de données.

Currents for Data Storage permet un flux continu de données de notre plateforme vers un compartiment de stockage de l’un de nos [partenaires d’entrepôt de données]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/). Currents écrit les fichiers Avro dans votre compartiment de stockage à des seuils réguliers, ce qui vous permet de traiter et d’analyser les données d’événements en utilisant vos propres outils d’aide à la décision.

{% alert important %}
Ce contenu **s’applique uniquement aux données d’événements de fichiers plats que nous envoyons aux partenaires d’entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage)**. <br><br>Pour le contenu qui s'applique aux autres partenaires, reportez-vous à notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) et consultez leurs pages respectives.
{% endalert %}

## Livraison au moins une fois

En tant que système à haut débit, Currents fournit une livraison des événements « au moins une fois » , ce qui signifie que des doublons d’événements peuvent parfois être écrits dans votre compartiment de stockage. Cela peut se produire lorsque des événements sont retraités à partir de notre file d’attente pour une raison ou une autre.

Si vos cas d’utilisation nécessitent une livraison « une seule fois exactement », vous pouvez utiliser le champ Identifiant unique envoyé avec chaque événement (`id`) pour dédupliquer les événements. Étant donné que le fichier échappe à notre contrôle lorsqu'il est écrit dans votre compartiment de stockage, nous n'avons aucun moyen de garantir la déduplication de notre côté.

## Horodatages

Tous les horodatages exportés par Currents sont envoyés au fuseau horaire UTC. Pour certains événements où il est disponible, un champ "fuseau horaire" est également inclus, qui fournit le format IANA (Internet Assigned Numbers Authority) du fuseau horaire local de l'utilisateur au moment de l'événement.

### Temps de latence

Les événements envoyés à Braze par l'intermédiaire du SDK ou de l'API peuvent inclure un horodatage du passé. L'exemple le plus notable est celui des données du SDK qui sont mises en file d'attente, par exemple lorsqu'il n'y a pas de connectivité mobile. Dans ce cas, l'horodatage de l'événement reflétera le moment où l'événement a été généré. Cela signifie qu'un pourcentage d'événements apparaîtra comme ayant une latence élevée.

## Format Apache Avro

Les données de sortie des intégrations de stockage de données Braze Currents au format `.avro`. Nous avons choisi [Apache Avro](https://avro.apache.org/) parce qu'il s'agit d'un format de données flexible qui supporte nativement l'évolution des schémas et qui est pris en charge par une grande variété de produits de données : 

- Avro est pris en charge par la grande majorité des principaux entrepôts de données.
- Dans le cas où vous souhaiteriez laisser vos données dans S3, Avro compresse mieux que CSV et JSON, vous payez donc moins pour le stockage et vous économisez potentiellement du CPU en analysant les données.
- Avro nécessite des schémas lorsque les données sont écrites ou lues. Les schémas peuvent évoluer au fil du temps pour permettre l’ajout de champs sans casser.

Currents créera un fichier pour chaque type d’événement en utilisant le format suivant :

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Vous ne voyez pas le code à cause de la barre de défilement ? Apprenez à résoudre ce problème [ici]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/).
{% endalert %}

|Segment Nom de fichier |Définition|
|---|---|
| `<your-bucket-prefix>` | Le préfixe défini pour cette Intégration Currents. |
| `<cluster-identifier>` | Pour usage interne par Braze. Sera une chaîne de caractères telle que « prod-01 », « prod-02 », « prod-03 » ou « prod-04 ». Tous les fichiers auront le même identifiant de cluster.|
| `<connection-type-identifier>` | L’identifiant du type de connexion. Les options sont « S3 » « AzureBlob » ou « GCS ». |
| `<integration-id>` | L’ID unique pour cette intégration Currents. |
| `<event-type>` | Le type de l’événement dans le fichier. |
| `<date>` | L’heure pendant laquelle les événements sont mis en file d’attente dans notre système pour le traitement dans le fuseau horaire UTC. Au format YYYY-MM-DD-HH. |
| `<schema-id>` | Utilisé pour versionner les `.avro` schémas pour la rétrocompatibilité et les évolutions de schéma. Entier. |
| `<zone>` | Pour usage interne par Braze. |
| `<partition>` | Pour usage interne par Braze. Entier. |
| `<offset>`| Pour usage interne par Braze. Entier. Prenez en compte le fait que les différents fichiers envoyés à la même heure auront un paramètre `<offset>` différent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Les conventions de dénomination des fichiers peuvent changer à l'avenir. Braze recommande d'effectuer une recherche sur toutes les clés de votre compartiment dont le préfixe est <votre-casier-préfixe>.
{% endalert %}

### Seuil d’écriture Avro

Dans des circonstances normales, Braze écrit des fichiers de données dans votre compartiment de stockage toutes les 5 minutes ou tous les 15 000 événements, au premier des deux termes échus. En cas de forte charge, nous pouvons écrire des fichiers de données plus importants pouvant contenir jusqu'à 100 000 événements par fichier.

{% alert important %}
Currents ne génére jamais de fichiers vides.
{% endalert %}

### Modifications du schéma Avro

De temps à autre, Braze peut apporter des modifications au schéma Avro lorsque des champs sont ajoutés, modifiés ou supprimés. Pour ce qui nous concerne ici, il existe deux types de modifications :celles qui « cassent » le schéma et celles qui ne le cassent pas. Dans tous les cas, le `<schema-id>` sera avancé pour indiquer que le schéma a été mis à jour. Les événements Currents écrits sur Azure Blob Storage, Google Cloud Storage et Amazon S3 écriront l'`<schema-id>` dans le chemin d'accès. Par exemple `<your-bucket-name0>/<currents-integration-id>/<event-type>/<date-of-event>/<schema-id>/<environment>/<avro-file>`.

#### Changements non cassants

Lorsqu’un champ est ajouté au schéma Avro, nous considérons qu’il s’agit d’un changement « qui ne casse pas le schéma ». Les champs ajoutés seront toujours des champs Avro "facultatifs" (par exemple avec une valeur par défaut de `null`), de sorte qu'ils "correspondront" aux anciens schémas conformément à la [spécification de résolution des schémas Avro.](http://avro.apache.org/docs/current/spec.html#schema+resolution) Ces ajouts ne devraient pas affecter les processus d'extraction, de transformation et de chargement (ETL) existants, car le champ sera simplement ignoré jusqu'à ce qu'il soit ajouté à votre processus ETL. 

{% alert important %}
Nous recommandons que votre configuration ETL soit explicite sur les champs traités pour éviter de rompre le flux si des nouveaux champs sont ajoutés.
{% endalert %}

Même si nous faisons tout notre possible pour vous informer à l’avance de tous les changements, nous pouvons à tout moment introduire des modifications qui ne cassent pas le schéma.

#### Changements cassants

Lorsqu’un champ est retiré ou modifié dans le schéma Avro, nous considérons qu’il s’agit d’un changement qui « casse le schéma ». Ce type de changement peuvent nécessiter de modifier les processus ETL existants, car les champs utilisés ne peuvent plus être enregistrés comme prévu.

Toutes les modifications de l’enchaînement du schéma seront communiquées avant la modification.
