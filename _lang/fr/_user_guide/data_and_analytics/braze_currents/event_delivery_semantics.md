---
nav_title: Sémantique des événements de livraison
article_title: Sémantique des événements de livraison
page_order: 3
page_type: reference
description: "Cet article de référence décrit la manière dont Currents gère les données d’événements de fichiers plats que nous envoyons aux partenaires d’entrepôts de données."
tool: Currents

---

# Sémantique des événements de livraison

> Cet article décrit la manière dont Currents gère les données d’événements de fichiers plats que nous envoyons aux partenaires d’entrepôts de données.

Currents for Data Storage permet un flux continu de données de notre plateforme vers un compartiment de stockage de l’un de nos partenaires d’entrepôt de données []({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).

Currents écrit les fichiers Avro dans votre compartiment de stockage à des seuils réguliers, ce qui vous permet de traiter et d’analyser les données d’événements en utilisant vos propres outils d’aide à la décision.

{% alert important %}
Notez que ce contenu **s’applique uniquement aux données d’événements de fichiers plats que nous envoyons aux partenaires d’entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage)**. <br><br>Pour tout contenu qui s’applique aux autres partenaires, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) et consultez leurs pages respectives.
{% endalert %}


## Livraison au moins une fois

En tant que système à haut débit, Currents garantit la livraison des événements « au moins une fois » , ce qui signifie que des doublons d’événements peuvent parfois être écrits dans votre compartiment de stockage. Cela peut se produire lorsque des événements sont retraités à partir de notre file d’attente pour une raison ou une autre.

Si vos cas d’utilisation nécessitent une livraison « une seule fois exactement », vous pouvez utiliser le champ Identifiant unique envoyé avec chaque événement (`id`) pour dédupliquer les événements. Puisque le fichier quitte notre contrôle une fois qu’il est écrit dans votre compartiment de stockage, nous n’avons aucun moyen de garantir la déduplication de notre côté.

## Horodatages

Tous les horodatages exportés par Currents sont envoyés au fuseau horaire UTC. Pour certains événements où il est disponible, un champ de fuseau horaire est également inclus et indique le format iana du fuseau horaire local de l’utilisateur au moment de l’événement.

## Avro Apache

Les données de sortie des intégrations de données de l’unité de stockage Currents Braze au format.`.avro` Nous avons choisi [Avro Apache](https://avro.apache.org/) car il s’agit d’un format de données flexible qui prend nativement en charge l’évolution du schéma et qui est pris en charge une grande variété de produits de données : 

- Avro est pris en charge par la grande majorité des principaux entrepôts de données.
- Dans le cas où vous souhaiteriez laisser vos données dans S3, Avro compresse mieux que CSV et JSON, vous payez donc moins pour le stockage et vous économisez potentiellement du CPU en analysant les données.
- Avro nécessite des schémas lorsque les données sont écrites ou lues. Les schémas peuvent évoluer au fil du temps pour permettre l’ajout de champs sans casser.

Currents créera un fichier pour chaque type d’événement en utilisant le format suivant :

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Vous ne voyez pas le code à cause de la barre de défilement ? Découvrez comment y remédier [ici]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/).
{% endalert %}

|Segment Nom de fichier |Définition|
|---|---|
| `<your-bucket-prefix>` | Le préfixe défini pour cette Intégration Currents. |
| `<cluster-identifier>` | Pour usage interne par Braze. Sera une chaîne de caractères telle que « prod-01 », « prod-02 », « prod-03 » ou « prod-04 ». Tous les fichiers auront le même identifiant de cluster.|
| `<connection-type-identifier>` | L’identifiant du type de connexion. Les options sont « S3 » « AzureBlob » ou « GCS ». |
| `<integration-id>` | L’ID unique pour cette intégration Currents. |
| `<event-type>` | Le type de l’événement dans le fichier. |
| `<date>` | L’heure pendant laquelle les événements sont mis en file d’attente dans notre système pour le traitement dans le fuseau horaire UTC. Au format AAAA-MM-JJ-HH |
| `<schema-id>` | Utilisé pour versionner les `.avro` schémas pour la rétrocompatibilité et les évolutions de schéma. Entier. |
| `<zone>` | Pour usage interne par Braze. |
| `<partition>` | Pour usage interne par Braze. Entier. |
| `<offset>`| Pour usage interne par Braze. Entier. Prenez en compte le fait que les différents fichiers envoyés à la même heure auront un paramètre `<offset>` différent. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Les conventions de nommage des fichiers peuvent évoluer, Braze recommande de rechercher toutes les clés de votre compartiment qui ont un préfixe de &lt;votre préfixe de compartiment&gt;.
{% endalert %}

### Seuil d’écriture Avro

Dans des circonstances normales, Braze écrira des fichiers de données dans votre compartiment de stockage toutes les 5 minutes ou tous les 15 000 événements, selon le premier à subvenir. En cas de charge importante, nous pourrions écrire des fichiers de données plus importants comportant jusqu’à 100 000 événements au cours de la même période de 5 minutes.

{% alert important %}
Currents ne génére jamais de fichiers vides.
{% endalert %}

### Modifications du schéma Avro

De temps à autre, Braze peut apporter des modifications au schéma Avro lorsque des champs sont ajoutés, modifiés ou supprimés. Pour ce qui nous concerne ici, il existe deux types de modifications :celles qui « cassent » le schéma et celles qui ne le cassent pas. Dans tous les cas, le `<schema-id>` sera avancé pour indiquer que le schéma a été mis à jour.

#### Changements non cassants

Lorsqu’un champ est ajouté au schéma Avro, nous considérons qu’il s’agit d’un changement « qui ne casse pas le schéma ». Les champs ajoutés seront toujours des champs Avro « facultatifs » (c.-à-d., avec une valeur par défaut de `null`), pour qu’ils « correspondent » aux schémas plus anciens conformément aux [Spécifications de schémas Avro](http://avro.apache.org/docs/current/spec.html#schema+resolution). Ces ajouts ne doivent pas affecter les processus ETL existants car le champ sera ignoré jusqu’à ce qu’il soit ajouté à votre processus ETL. 

{% alert important %}
Nous recommandons que votre configuration ETL soit explicite sur les champs traités pour éviter de rompre le flux si des nouveaux champs sont ajoutés.
{% endalert %}

Même si nous faisons tout notre possible pour vous informer à l’avance de tous les changements, nous pouvons à tout moment introduire des modifications qui ne cassent pas le schéma.

#### Changements cassants

Lorsqu’un champ est retiré ou modifié dans le schéma Avro, nous considérons qu’il s’agit d’un changement qui « casse le schéma ». Ce type de changement peuvent nécessiter de modifier les processus ETL existants, car les champs utilisés ne peuvent plus être enregistrés comme prévu.

Toutes les modifications de l’enchaînement du schéma seront communiquées avant la modification.
