---
nav_title: Verfügbare Partner
article_title: Verfügbare Currents-Partner
page_order: 2
page_type: reference
description: "Dieser referenzierte Artikel beschreibt die Datenpartner, die Sie für die Integration mit Braze-Currents verwenden können, und deren Anwendungsfälle."
tool: Currents

---

# Verfügbare Partner

> Auf dieser Seite finden Sie eine Liste der Datenpartner, die Sie in Braze-Currents integrieren können, sowie einen Überblick über deren Anwendungsfälle. 

{% alert note %}
Die Namenskonventionen für Ereignisse, die für einen Partner aus Braze fließen, passen möglicherweise nicht zu anderen Partnern. Zum Beispiel lautet das Ereignis für die Öffnung von Currents E-Mails in Segmente `Email Opened`, während es in Mixpanel `Email Open` heißt.
{% endalert %}

## Data Warehouse Speicherung
Data Warehouse bietet eine Sammelquelle für alle Daten, die von Currents gestreamt werden. Diese Partner können entweder als Warehouse (für die Speicherung von Flat-Files) fungieren oder dazu verwendet werden, Business-Intelligence-Tools und Algorithmen für maschinelles Lernen zu betreiben, Insights über die Performance des Marketers zu erhalten und vieles mehr.

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
* [Google-Cloudspeicher]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
* [Microsoft Azure Blob-Speicher]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

Wir sind von der Leistungsfähigkeit von Currents und Data Warehouses so überzeugt, dass [wir sie selbst einsetzen]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!

## Kundendaten

Diese Customer Data Platform (CDP) sammelt Daten aus verschiedenen Quellen und leitet sie an eine Vielzahl anderer Standorte weiter, damit Sie die Daten von Braze optimal nutzen können.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents/)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents/)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents/)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents/)
* [Amperity]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents)

## Verhaltensanalysen (Behavioral Analytics)

Diese Partner sind auf Produkt Analytics und Business-Intelligence spezialisiert und können Ihnen helfen, mit Ihren Nutzer:innen auf der Grundlage ihrer Aktionen zu interagieren.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/)

* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)

* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/)



