---
nav_title: FAQ
article_title: FAQ sur les courants
page_order: 9
page_type: reference
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de la mise en place de Braze Currents."
tool: Currents
---

# Foire aux questions

> Cette page fournit des réponses à certaines questions fréquemment posées au sujet de Currents.

### Comment obtenir des données historiques ?

Currents est un flux de données en continu et en temps réel, ce qui signifie que les événements ne peuvent pas être rejoués. Toutefois, vous pouvez stocker les données Currents dans un entrepôt de données tel qu'[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) ou [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), afin de pouvoir agir sur les événements passés comme bon vous semble. Les données sont conservées pendant 30 jours, mais pour obtenir des données plus historiques, vous pouvez interroger [Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/).

### Pourquoi Currents fournit-il des données au format Avro et non JSON ?

Avro, contrairement à JSON sans schéma, supporte nativement l'évolution des schémas. Vous bénéficierez également de la possibilité d'envoyer des fichiers Avro en utilisant moins de bande passante et en économisant de l'espace de stockage, car Avro est hautement compressible.

### Comment Braze gère-t-il la surcharge des fichiers ?

Nous créons un processus d'extraction, de transformation et de chargement (ETL), qui vous permet d'extraire de grandes quantités de données d'une base de données pour les placer et les stocker dans une autre.

### Où dois-je stocker ces données pour pouvoir les interroger ?

Braze est partenaire de plusieurs entrepôts de données dans lesquels vous pouvez stocker vos données pour les interroger. Nous vous recommandons d'utiliser :
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google cloud storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).