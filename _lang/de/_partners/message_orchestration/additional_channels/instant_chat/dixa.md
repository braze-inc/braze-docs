---
nav_title: Dixa
article_title: Dixa
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) ist eine Plattform für den Kundenservice, die durch die Zusammenführung von Kommunikationskanälen wie Chat, E-Mail, Telefon und soziale Medien in einer einzigen Schnittstelle die Support-Erfahrung verbessert. Es hilft Unternehmen, die Kundenzufriedenheit und Effizienz durch intelligentes Routing, Automatisierung und Echtzeit-Einblicke in die Leistung zu verbessern.

Die Integration von Braze und Dixa bietet einen besseren Überblick über alle Ihre Benutzer, indem sie den Kundendienstmitarbeitern Braze-Daten in Echtzeit zur Verfügung stellt.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Dixa-Konto        | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Dixa-Administratorkonto.                                                                                           |
| Ein Braze REST API Schlüssel  | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.export.ids` und `email.status`.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Ein Braze REST Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

## Anwendungsfälle

Zeigen Sie Braze-Daten in der Ansicht des Kundendienstmitarbeiters an, während Sie mit Ihren Benutzern über verschiedene Kommunikationskanäle, wie E-Mail, Messenger oder Chat, kommunizieren.

## Integration

Sie müssen ein Dixa-Administrator sein, um Integrationen innerhalb von Dixa zu konfigurieren. Für die Integration von Braze gehen Sie in Dixa zu **Einstellungen** > **Integrationen** > **Braze**.

![][1]{: style="width:450px;"}

### Schritt 1: Erstellen Sie die Integration in Dixa

Auf der Seite **Braze-Widget erstellen** füllen Sie die folgenden erforderlichen Felder aus, um die Integration zu erstellen:

- **Name des Widgets:** Dies ist der Name der Integration, der später in der Konversations-Seitenleiste als Titel verwendet wird.
- **API-URL:** Dies ist die URL des REST-API-Endpunkts von Braze für Ihre Instanz.
- **API-Schlüssel:** Dies ist der Braze-API-Schlüssel, den Sie in den Voraussetzungen erstellt haben.

### Schritt 2: Konfigurieren Sie die Integration

Als nächstes konfigurieren Sie die Integration von Braze und Dixa. Wählen Sie eine der folgenden Optionen, um die Ansicht des Braze-Widgets in der Konversations-Seitenleiste anzupassen.

#### Das Widget in der Konversations-Seitenleiste anzeigen

Mit dieser Einstellung können Sie die gesamte Integration in der Konversations-Seitenleiste in Dixa ein- oder ausblenden. 

Wenn Sie die Integration aktiv konfigurieren, empfehlen wir, diese Funktion zu deaktivieren, während Sie die erforderlichen Felder ausfüllen. Wenn Sie mit der Konfiguration fertig sind, können Sie sie wieder einschalten und die Dixa-Agenten können die Integration nutzen.

#### Kundendetails anzeigen

Wählen Sie, ob Sie die Details des Benutzers anzeigen oder verbergen möchten. Die Details enthalten Daten zu Standort, E-Mail, Telefonnummer, Status des E-Mail-Abonnements, Status des Push-Benachrichtigungs-Abonnements und die Dauer der Mitgliedschaft in Braze. 

#### Zeigen Sie die Schaltfläche zum Ändern des E-Mail-Abonnementstatus an

Die Schaltflächen basieren auf einem der drei Abonnementstatus von Braze: `subscribed`, `opted-in` und `unsubscribed`. Wenn ein Benutzer `subscribed` ist, kann der Agent `opt-in` oder `unsubscribe` wählen. Wenn ein Benutzer `opted-in` oder `unsubscribed` ist, ist es nur möglich, zwischen diesen beiden zu wechseln.

#### Eine Liste der benutzerdefinierten Attribute anzeigen

Wählen Sie, ob Sie die benutzerdefinierten Braze-Attribute des Benutzers anzeigen oder ausblenden möchten.

#### Eine Liste der benutzerdefinierten Ereignisse anzeigen

Wählen Sie, ob Sie die benutzerdefinierten Braze-Ereignisse des Benutzers anzeigen oder ausblenden möchten.

#### Eine Liste der Einkäufe anzeigen

Wählen Sie, ob Sie eine Liste der vom Benutzer gekauften Produkte anzeigen oder ausblenden möchten. Hier können Sie sehen, wie oft es gekauft wurde. Um das Datum des ersten und letzten Kaufs anzuzeigen, bewegen Sie den Mauszeiger über den Artikel. 

### Beispiel Integration

Im Folgenden sehen Sie ein Beispiel für die Integration:

![Die Braze- und Dixa-Integration in Dixa, die den Status des E-Mail-Abonnements eines Benutzers, benutzerdefinierte Attribute, benutzerdefinierte Ereignisse und Einkäufe anzeigt.][2]{: style="width:350px;"}

[1]: {% image_buster /assets/img/dixa/dixa-create-integration.png %}
[2]: {% image_buster /assets/img/dixa/dixa-braze-integration.png %}