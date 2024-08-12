---
nav_title: Ingestion de données Cloud
article_title: Ingestion de Données Cloud dans Braze
alias: /cloud_ingestion/
description: "Cet article de référence décrit l’ingestion de données cloud dans Braze en utilisant Snowflake et Redshift et les recommandations de paramétrages de données."
layout: dev_guide
page_order: 4.1
page_type: landing

guide_top_header: "Ingestion de Données Cloud dans Braze"
guide_top_text: "<h2>Qu’est-ce que l’Ingestion de données Cloud dans Braze ?</h2>L’ingestion de données cloud dans Braze vous permet de configurer une connexion directe entre votre instance Snowflake ou Redshift et Braze pour synchroniser les attributs, les événements et les achats pertinents de l’utilisateur. Une fois synchronisées avec Braze, ces données peuvent être exploitées dans des cas d’utilisation tels que la personnalisation ou la segmentation.<br><br>**Capacités de l’ingestion de données cloud de Braze :**<br> - Créer une intégration simple directement depuis votre entrepôt de données vers Braze en quelques minutes<br>- Synchroniser les données utilisateur en toute sécurité, y compris les attributs, événements et achats depuis votre entrepôt de données vers Braze<br>- Fermer la boucle de données avec Braze en combinant l’ingestion de données cloud avec Currents ou le partage de données de Snowflake"

guide_featured_title: "Section Articles"
guide_featured_list:
  - name: Aperçu et bonnes pratiques
    link: /docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
    image: /assets/img/braze_icons/cloud-blank-01.svg
  - name: Intégration Snowflake
    link: /docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/snowflake/
    image: /assets/img/braze_icons/snowflake-01.svg
  - name: Intégration Redshift
    link: /docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/redshift/
    image: /assets/img/braze_icons/settings-01.svg

---

{% alert important %}
L’ingestion de données cloud Braze est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}
<!--

  - name: Redshift 
    link: /docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/redshift/
    image: /assets/img/braze_icons/settings-01.svg

## What is Braze Cloud Data Ingestion?

Braze Cloud Data Ingestion allows you to set up a direct connection from your Snowflake instance to Braze to sync relevant user attributes, events, and purchases. Once synced to Braze, this data can be leveraged for use cases such as personalization or segmentation.
-->
<br><br>

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}