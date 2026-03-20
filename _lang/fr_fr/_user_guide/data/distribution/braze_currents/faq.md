---
nav_title: FAQ
article_title: FAQ sur Currents
page_order: 9
page_type: reference
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de la mise en place de Braze Currents."
tool: Currents
---

# Foire aux questions

> Cette page fournit des réponses à certaines questions fréquemment posées au sujet de Currents.

### Comment obtenir des données historiques ?

Currents est un flux de données en continu et en temps réel, ce qui signifie que les événements ne peuvent pas être rejoués. Toutefois, vous pouvez stocker les données Currents dans un entrepôt de données tel qu'[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) ou [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), afin de pouvoir agir sur les événements passés comme bon vous semble. Les données sont conservées pendant 30 jours, mais pour obtenir des données plus anciennes, vous pouvez interroger [Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/).

### Pourquoi Currents fournit-il des données au format Avro et non JSON ?

Avro, contrairement à JSON qui ne repose pas sur un schéma, supporte nativement l'évolution des schémas. Vous bénéficierez également de la possibilité d'envoyer des fichiers Avro en utilisant moins de bande passante et en économisant de l'espace de stockage, car Avro est hautement compressible.

### Comment Braze gère-t-il la surcharge des fichiers ?

Nous mettons en place un processus ETL (extraire, transformer, charger) qui vous permet d'extraire de grandes quantités de données d'une base de données pour les placer et les stocker dans une autre.

### Où dois-je stocker ces données pour pouvoir les interroger ?

Braze est partenaire de plusieurs entrepôts de données dans lesquels vous pouvez stocker vos données pour les interroger. Nous vous recommandons d'utiliser :
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### Quelle est la fiabilité des données Currents ?

Currents garantit une livraison « au moins une fois » (at-least-once), ce qui signifie que des événements en double peuvent occasionnellement être écrits dans votre compartiment de stockage. Si votre cas d'usage nécessite une livraison exactement une fois, vous pouvez dédupliquer les événements à l'aide du champ d'identifiant unique (`id`) envoyé avec chaque événement. Pour plus de détails, consultez la section [Sémantique de livraison des événements]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### À quelle fréquence les données sont-elles synchronisées avec Currents ?

Les données sont diffusées en continu. Braze envoie un lot d'événements chaque fois qu'un lot complet est prêt, ou toutes les 5 minutes, selon ce qui se produit en premier. Pour les connecteurs à fort volume, les données arrivent quasiment en temps réel. Pour les connecteurs à faible volume, comptez un délai de 5 à 30 minutes. Pour plus de détails, consultez la section [Seuil d'écriture Avro]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/#avro-write-threshold).

{% alert note %}
Si un appareil n'est pas connecté à Internet, la création de l'événement peut être retardée. C'est le cas le plus fréquent pour les événements de messages in-app, car les messages in-app peuvent être déclenchés hors ligne.
{% endalert %}

### Comment savoir quels événements sont disponibles pour Currents ?

Pour obtenir la liste complète des événements enregistrés par Currents, consultez les glossaires des [événements de comportement client]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et des [événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). Vous pouvez filtrer ces glossaires par type d'événement (envois, réceptions ou ouvertures, par exemple).

### Tous les événements d'envoi sont-ils enregistrés dans Currents ?

Tous les événements sont enregistrés dans Currents. Il n'existe aucun scénario dans lequel un événement serait intentionnellement supprimé du flux Currents.

### Les données peuvent-elles être corrompues dans Currents ?

Dans des conditions normales, les données Currents ne sont pas corrompues. Bien qu'un problème rare soit toujours possible, il n'existe aucune condition connue dans laquelle les données seraient systématiquement corrompues.

### Pourquoi est-ce que je vois des données d'événements personnalisés datant d'avant la mise en place de mon intégration Currents ?

Braze ne remplit pas rétroactivement les événements dans Currents. Cependant, les événements personnalisés peuvent être enregistrés avec un horodatage passé (par exemple, si un appareil était hors ligne au moment de l'événement et s'est synchronisé plus tard). Dans ces cas, l'horodatage de l'événement reflète le moment où l'événement s'est réellement produit, ce qui peut être antérieur à la configuration de l'intégration Currents.

### Puis-je inclure des attributs personnalisés dans les événements d'envoi Currents ?

Non. Currents n'inclut pas d'attributs personnalisés dans les événements d'envoi. Currents enregistre les événements personnalisés et les événements d'engagement lié aux messages. Pour obtenir la liste complète des champs disponibles, consultez les [glossaires des événements]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/).

### Currents inclut-il les étiquettes de campagne ou les paires clé-valeur ?

Non. Currents n'inclut pas les étiquettes de campagne ni les paires clé-valeur au niveau du message. En guise de solution de contournement, vous pouvez utiliser un canal webhook dans la campagne pour envoyer ces informations vers votre propre endpoint, en utilisant [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) pour modéliser les données d'étiquettes et de paires clé-valeur.

### Comment Braze informe-t-il ses clients des modifications apportées à Currents ?

Lorsque des modifications sont apportées à Currents (nouveaux champs ou types d'événements, par exemple), Braze envoie un e-mail à tous les clients disposant d'intégrations Currents actives et ayant utilisé le tableau de bord au cours des 30 derniers jours. Vous pouvez également consulter le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) pour connaître les dernières modifications.

### De combien d'espace de stockage ai-je besoin pour les données Currents ?

Les besoins en stockage dépendent de votre volume d'événements et des types d'événements que vous exportez. Braze fournit des [exemples d'événements au format Avro](https://github.com/braze-inc/currents-examples/tree/master/sample-data) que vous pouvez utiliser pour estimer la taille des fichiers correspondant à votre cas d'usage.

### Pourquoi le nom de la campagne ou le nom de l'étape du canvas est-il `NULL` dans mes données Currents ?

Lorsque vous créez une nouvelle campagne ou un nouveau canvas, le nom peut mettre un certain temps à se propager dans tous les systèmes Braze. Les événements envoyés via Currents pendant cette période peuvent contenir `NULL` dans les champs de nom (tels que `campaign_name` ou `canvas_step_name`). C'est également le comportement attendu si le nom a été modifié peu avant l'enregistrement des événements. Pour éviter cela, attendez un moment après la création ou le renommage d'une campagne ou d'une étape du canvas avant de procéder à l'envoi.

### Que se passe-t-il si mon compartiment de stockage est indisponible lorsque Currents tente d'écrire des données ?

Si votre compartiment de stockage est indisponible au moment du transfert de données, ces données sont perdues. Braze n'est pas en mesure de renvoyer rétroactivement les événements qui n'ont pas été livrés avec succès. Pour éviter toute perte de données, assurez-vous que votre compartiment de stockage est disponible et correctement configuré en permanence.

### À quelle fréquence l'ID de schéma est-il mis à jour ?

Les ID de schéma sont globaux pour tous les types d'événements et s'incrémentent de manière séquentielle. Les mises à jour peuvent survenir à tout moment, et Braze informera les clients par e-mail des modifications à venir. Chaque fois qu'une mise à jour de schéma a lieu pour un type d'événement, le prochain ID global disponible est attribué. Nous vous recommandons de lire les fichiers de manière récursive à partir du chemin racine pour gérer les changements d'ID de schéma. Pour plus de détails, consultez la section [Modifications du schéma Avro]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/#avro-schema-changes).