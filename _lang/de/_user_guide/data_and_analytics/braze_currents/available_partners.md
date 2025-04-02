---
nav_title: Verfügbare Partner
article_title: Verfügbare Currents-Partner
page_order: 2
page_type: reference
description: "In diesem Referenzartikel werden die Datenpartner, die Sie für die Integration in Braze-Currents verwenden können, und ihre Anwendungsfälle beschrieben."
tool: Currents

---

# Verfügbare Partner

> Auf dieser Seite finden Sie eine Liste der Datenpartner, die Sie in Braze-Currents integrieren können, sowie einen Überblick über deren Anwendungsfälle. 

{% alert note %}
Die Namenskonventionen für Events, die für einen Partner aus Braze fließen, passen möglicherweise nicht zu anderen Partnern. Das Event für die Currents-E-Mail-Öffnungen in Segment lautet beispielsweise `Email Opened`, während es in Mixpanel `Email Open` lautet.
{% endalert %}

## Data Warehouse-Speicherung
[![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/introduction-to-data-warehouses){: style="float:right;width:120px;border:0;" class="noimgborder"}
Data Warehouse bietet eine Sammelquelle für alle Daten, die von Currents gestreamt werden. Diese Partner können entweder als Warehouse (für die Speicherung von Flat-Files) fungieren oder dazu verwendet werden, Business-Intelligence-Tools und Algorithmen für maschinelles Lernen zu betreiben, Insights über die Performance des Marketers zu erhalten und vieles mehr.

* [Amazon S3][1]
* [Google-Cloudspeicher][2]
* [Microsoft Azure Blob-Speicher][3]

Wir sind von der Leistungsfähigkeit von Currents und Data Warehouses so überzeugt, dass [wir sie selbst einsetzen]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/)!

## Kundendaten

Diese Customer Data Platform (CDP) sammelt Daten aus verschiedenen Quellen und leitet sie an eine Vielzahl anderer Standorte weiter, damit Sie die Daten von Braze optimal nutzen können.

* [mParticle][6]
* [Segment][7]
* [Tealium][8]
* [Treasure Data][10]
* [RudderStack][9]
* [Adobe][12]

## Verhaltensanalysen (Behavioral Analytics)

Diese Partner sind auf Produkt Analytics und Business-Intelligence spezialisiert und können Ihnen helfen, mit Ihren Nutzer:innen auf der Grundlage ihrer Aktionen zu interagieren.

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