---
nav_title: "Nutzer:innen importieren"
article_title: "Nutzer:innen importieren"
page_order: 4.1
description: "Lernen Sie die verschiedenen Nutzer:innen-Optionen von Braze kennen, wie CSV-Nutzerimport, REST API, Datenaufnahme in der Cloud und mehr."

---
# Nutzer:innen importieren

> Lernen Sie die verschiedenen Nutzer:innen-Optionen von Braze kennen, wie CSV-Nutzerimport, REST API, Datenaufnahme in der Cloud und mehr.

## Über HTML-Validierung

Beachten Sie, dass Braze HTML-Daten während des Imports nicht bereinigt, validiert oder neu formatiert. Das bedeutet, dass Script Tags aus allen Importdaten, die Sie für die Personalisierung des Internets verwenden, entfernt werden müssen.

Wenn Sie Daten in Braze importieren, die ausdrücklich für die Personalisierung in einem Webbrowser bestimmt sind, entfernen Sie alle HTML-, JavaScript- und sonstigen Tags, da diese bei der Darstellung im Webbrowser für böse Absichten genutzt werden könnten.

Alternativ können Sie für HTML auch die Braze Liquid Filter (`strip_html`) verwenden, um gerenderten Text in HTML umzuwandeln. Zum Beispiel:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Optionen importieren

### Braze CSV-Import

Mit dem CSV-Nutzerimport können Sie die folgenden Nutzer:innen-Attribute und angepassten Events erfassen und aktualisieren. Um loszulegen, siehe [CSV-Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

|Typ|Definition|Beispiel|Maximale Dateigröße|
|---|---|---|---|
|Standardattribute|Reservierte Nutzer:innen-Attribute, die von Braze erkannt werden.|`first_name`, `email`|500 MB|
|Angepasste Attribute|Eindeutige Attribute der Nutzer:innen für Ihr Unternehmen.|`last_destination_searched`|500 MB|
|Benutzerdefinierte Ereignisse|Eindeutige Ereignisse in Ihrem Unternehmen, die Nutzer:in darstellen.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Lambda Nutzer:innen-CSV-Nutzerimport

Sie können unser serverloses S3 Lambda CSV-Import-Skript verwenden, um Nutzer:innen-Attribute in Braze hochzuladen. Diese Lösung funktioniert wie ein CSV-Uploader, bei dem Sie Ihre CSV-Dateien in einem S3-Bucket ablegen und die Skripte sie über unsere API hochladen.

Die geschätzte Ausführungszeit für eine Datei mit 1.000.000 Zeilen sollte etwa fünf Minuten betragen. Weitere Informationen finden Sie unter [Nutzer:innen-Attribute CSV-Nutzerimport](https://www.braze.com/docs/user_guide/data/cloud_ingestion/).

### REST API

Verwenden Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), um angepasste Events, Nutzer-Attribute und Käufe für Nutzer:innen aufzuzeichnen.

### Ingestion von Cloud-Daten

Verwenden Sie Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/), um Nutzer:innen-Attribute zu importieren und zu pflegen.

## Gesetzlich vorgeschriebene Transaktions-E-Mails

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}
