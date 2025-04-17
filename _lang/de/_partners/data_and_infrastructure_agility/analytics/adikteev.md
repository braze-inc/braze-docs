---
nav_title: Adikteev
article_title: Adikteev Churn Prognose
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Adikteev, einer Engine zur Bindung von Nutzern:innen, die Prognosen zur Abwanderung mit Full Service App Retargeting kombiniert."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Adikteev Churn Prognose

> [Adikteev](https://www.adikteev.com/churn-prediction) ist eine Maschine zur Bindung von Nutzern:innen, die Prognosen zur Abwanderung mit Full Service Retargeting für Apps kombiniert.

_Diese Integration wird von Adikteev gepflegt._

## Über die Integration

Die Integration von Braze und Adikteev erlaubt es Ihnen, die Bindung von Nutzern zu erhöhen, indem Sie die Prognosen von Adikteev innerhalb von Braze CRM Kampagnen nutzen, um vorrangig risikoreiche Segmente von Nutzern:innen anzusprechen.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Adikteev-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Adikteev-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

{% tabs %}
{% tab Filtern der Zielgruppe %}
Verfeinerung der Segmente Ihrer Zielgruppe auf der Grundlage des Abwanderungsrisikos.<br> Die Namen und Werte der angepassten Attribute, die von Adikteev gesendet werden, sind konfigurierbar.

![Ein Screenshot zeigt ein Beispiel für die Verwendung eines angepassten Attributs, das von Adikteev als Segmentierungs-Filter für die Zielgruppe gesendet wurde.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Messaging-Targeting %}
Anpassung Ihrer Messaging-Kampagnen von Braze auf der Grundlage des Abwanderungsrisikos der Empfänger:innen.

![Ein Screenshot zeigt ein Beispiel für die Verwendung eines von Adikteev gesendeten angepassten Attributs als Filter für das Targeting einer Kampagne.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: Teilen Sie den Ereignis-Stream Ihrer App

Um die Prognosen zur Abwanderung Ihrer App Zielgruppe zu starten, müssen Sie bei Adikteev die Event Postbacks Ihrer mobilen Messplattform aktivieren. Folgen Sie den Anweisungen auf der [Website von Adikteev](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation), um dies einzurichten.

### Schritt 2: Erstellen Sie Ihren Braze REST API-Schlüssel

Navigieren Sie in Braze zu **Einstellungen** > **APIs und Bezeichner**. Wählen Sie **Neuen API-Schlüssel auswählen**, geben Sie den Namen des API-Schlüssels Ihrer Wahl ein und stellen Sie sicher, dass die folgende Berechtigung hinzugefügt wird:

- `users.track`

### Schritt 3: Informationen für das Adikteev Team bereitstellen

Um die Integration abzuschließen, müssen Sie Ihrem Account Manager:in von Adikteev Ihren REST API-Schlüssel und die URL des REST-Endpunkts mitteilen. Adikteev wird die Verbindung herstellen und Sie nach Abschluss der Einrichtung kontaktieren, um die Integration zu bestätigen.

## Batching und Rate-Limits

Der Endpunkt `user.track` dient zum Update von Details über Ihre Nutzer:innen. In der [API-Dokumentation]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) finden Sie ausführliche Informationen über die Rate-Limits des Endpunkts, die Stapelverarbeitung von Anfragen und die Details der Anfragen.

{% alert tip %}
Denken Sie daran, dass API-Aufrufe nur zum Update von Daten erfolgen sollten, die sich geändert haben, um die Anzahl der API-Aufrufe insgesamt zu reduzieren. Mit anderen Worten: Aktualisieren Sie nur Nutzer:innen, bei denen sich das Segment der Abwanderung geändert hat.
{% endalert %}

## Bezeichner für Nutzer:innen und Geräte

Nutzerprofile in Braze können mit jeder Art von Benutzer- oder Geräte-Bezeichnern verknüpft werden. Die Liste der verfügbaren Optionen hängt davon ab, wie Sie die Datenerfassung in Braze integriert haben. Für Adikteev müssen Sie einen gemeinsamen Bezeichner zwischen Ihrem MMP und Ihren Nutzerprofilen in Braze finden, um die Segmente für die Abwanderung korrekt zu senden.

## Bindung und Löschung von Daten

Erfolgt kein Update, werden das Attribut und sein Wert auf unbestimmte Zeit in den Nutzerprofilen von Braze aufbewahrt.

Um ein Attribut des Profils zu entfernen, setzen Sie es auf `null`.

## Anfrage Payloads

Die von Adikteev an Braze gesendete Nutzlast ist anpassbar und kann so konfiguriert werden, dass sie den Bedürfnissen der Kund:in entspricht. Dazu gehört die Konfiguration der verwendeten Bezeichner, der Name des angepassten Attributs und ob Adikteev neue Nutzer:innen in Braze anlegen oder nur bestehende Nutzer:innen aktualisieren kann.


## Unterstützung und Fehlerbehebung

Kontaktieren Sie Ihren Adikteev Account Manager:in, wenn Sie Fragen zur Integration haben oder Unterstützung bei Ihren Anwendungsfällen benötigen.

