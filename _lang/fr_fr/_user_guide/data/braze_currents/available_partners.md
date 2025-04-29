---
nav_title: Partenaires disponibles
article_title: Partenaires Currents disponibles
page_order: 2
page_type: reference
description: "Cet article de référence décrit les partenaires de données que vous pouvez utiliser pour intégrer à Braze Currents, avec leurs cas d’utilisation."
tool: Currents

---

# Partenaires disponibles

> Cette page répertorie les partenaires de données que vous pouvez intégrer à Braze Currents et présente leurs cas d'utilisation. 

{% alert note %}
Les conventions de nommage de nos différents partenaires pour les événements envoyés par Braze ne correspondent pas forcément. Par exemple, l'événement d'ouverture d'e-mail Currents dans Segment est `Email Opened`, tandis que dans Mixpanel, il s’agit de `Email Open`.
{% endalert %}

## Entrepôt de données
[![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/introduction-to-data-warehouses){: style="float:right;width:120px;border:0;" class="noimgborder"}
L'entrepôt de données offre une source de collecte pour toutes les informations transmises par Currents. Ces partenaires peuvent soit agir comme des entrepôts (pour le stockage de fichiers plats) soit être utilisés pour alimenter des outils d'intelligence économique, des algorithmes d'apprentissage automatique, obtenir des informations sur les performances marketing, et plus encore.

* [Amazon S3][1]
* [Google Cloud Storage][2]
* [Microsoft Azure Blob Storage][3]

Nous avons tellement confiance en la puissance de Currents et des entrepôts de données ensemble que [nous les utilisons nous aussi]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/) !

## Données client

Ces plates-formes de données client collectent et acheminent des informations de sources multiples vers divers autres emplacements pour vous permettre d’utiliser les données Braze de la meilleure façon possible.

* [mParticle][6]
* [Segment][7]
* [Tealium][8]
* [Treasure Data][10]
* [RudderStack][9]
* [Adobe][12]
* [Amperity][13]

## Analyse comportementale

Ces partenaires sont spécialisés dans l’analyse produit et l’aide à la décision (Informatique décisionnelle), et ils peuvent vous aider à interagir avec vos utilisateurs en fonction de leurs actions.

* [Amplitude][4]

* [Mixpanel][5]

* [Heap][11]



[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/google_cloud_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/microsoft_azure_blob_storage_for_currents/
[4]: {{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/
[5]: {{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/
[6]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/
[7]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/
[8]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents
[9]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack_for_currents/
[10]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/treasure_data/treasure_data_for_currents/
[11]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/
[12]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/adobe_for_currents/
[13]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents
