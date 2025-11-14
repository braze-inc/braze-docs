---
nav_title: FAQ
article_title: Currents FAQ
page_order: 9
page_type: reference
description: "Dieser Artikel behandelt einige der am häufigsten gestellten Fragen, die bei der Einrichtung von Braze-Currents auftreten."
tool: Currents
---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zu Currents.

### Wie komme ich an historische Daten?

Currents ist ein Realtime-Live-Daten-Stream, d.h. Ereignisse können nicht nachgespielt werden. Sie können jedoch Currents Daten in einem Data Warehouse wie [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) oder [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) speichern, so dass Sie nach Belieben auf vergangene Ereignisse reagieren können. Die Daten werden 30 Tage lang aufbewahrt, aber für mehr historische Daten können Sie [Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/) abfragen.

### Warum gibt Currents die Daten im Avro-Format und nicht in JSON aus?

Im Gegensatz zu JSON ohne Schema unterstützt Avro von Haus aus die Schemaentwicklung. Außerdem profitieren Sie von der Möglichkeit, Avro-Dateien mit weniger Bandbreite zu versenden und Speicherplatz zu sparen, da Avro stark komprimierbar ist.

### Wie geht Braze mit dem Datei-Overhead um?

Wir entwickeln einen Extract, Transform, Load (ETL)-Prozess, mit dem Sie große Datenmengen aus einer Datenbank ziehen und in einer anderen speichern können.

### Wo sollte ich diese Daten für Abfragen speichern?

Braze ist Partner von mehreren Data Warehouses, in denen Sie Ihre Daten für Abfragen speichern können. Wir empfehlen die Verwendung:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob-Speicher]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).