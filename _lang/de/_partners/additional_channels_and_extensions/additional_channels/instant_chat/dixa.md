---
nav_title: Dixa
article_title: Dixa
description: "Dieser Artikel stellt die Partnerschaft zwischen Braze und Dixa vor."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) ist eine Kundenservice-Plattform, mit der Sie Ihre Support-Erlebnisse verbessern können, indem Sie Kommunikationskanäle wie Chat, E-Mail, Telefon und Social Media in einer einzigen Schnittstelle zusammenführen. Sie hilft Unternehmen, die Kundenzufriedenheit und Effizienz durch intelligentes Routing, Automatisierung und Realtime-Performance-Insights zu verbessern.

Die Integration von Braze und Dixa bietet einen besseren Überblick über alle Ihre Nutzer:innen, indem sie den Kundenservice-Agenten Braze-Daten in Realtime zur Verfügung stellt.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Dixa-Konto        | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Dixa-Administratorkonto.                                                                                           |
| Ein Braze REST-API-Schlüssel  | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.export.ids` und `email.status`.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Ein Braze REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Zeigen Sie Braze-Daten in der Ansicht des Kundenservice-Agenten an, während Sie mit Ihren Nutzer:innen über verschiedene Kommunikationskanäle wie E-Mail, Messenger oder Chat kommunizieren. Nutzen Sie außerdem die Braze Datentransformation, um Daten von Dixa an Braze zu senden und Marketing-Aktivitäten zu pausieren, während das Problem einer Nutzerin oder eines Nutzers gelöst wird.

## Integration

Sie müssen Dixa-Administrator:in sein, um Integrationen innerhalb von Dixa zu konfigurieren. Für die Braze-Integration gehen Sie in Dixa zu **Einstellungen** > **Integrationen** > **Braze**.

![Die Seite „Braze-Widget erstellen" in Dixa, auf der Sie den Widget-Namen, die API-URL und den API-Schlüssel eingeben.]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### 1. Schritt: Erstellen Sie die Integration in Dixa

Auf der Seite **Braze-Widget erstellen** füllen Sie die folgenden erforderlichen Felder aus, um die Integration zu erstellen:

- **Name des Widgets:** Dies ist der Name der Integration, der später in der Konversations-Seitenleiste als Titel verwendet wird.
- **API URL:** Dies ist die URL des REST-API-Endpunkts von Braze für Ihre Instanz.
- **API-Schlüssel:** Dies ist der Braze-API-Schlüssel, den Sie unter den Voraussetzungen erstellt haben.

### 2. Schritt: Konfigurieren Sie die Integration

Als Nächstes konfigurieren Sie die Integration von Braze und Dixa. Wählen Sie eine der folgenden Optionen, um die Ansicht des Braze-Widgets in der Konversations-Seitenleiste anzupassen.

#### Widget in der Konversations-Seitenleiste anzeigen

Diese Einstellung blendet die gesamte Integration in der Konversations-Seitenleiste in Dixa ein oder aus. 

Wenn Sie die Integration gerade konfigurieren, empfehlen wir Ihnen, diese Option zu deaktivieren, während Sie die erforderlichen Felder ausfüllen. Wenn Sie mit der Konfiguration fertig sind, können Sie sie wieder einschalten und die Dixa-Agenten können die Integration nutzen.

#### Details zu Kund:innen anzeigen

Wählen Sie, ob Sie die Details der Nutzer:innen anzeigen oder ausblenden möchten. Die Details enthalten Daten über Standort, E-Mail, Telefonnummer, Status des E-Mail-Abos, Status des Push-Benachrichtigungs-Abos und die Dauer der Mitgliedschaft in Braze. 

#### Button zum Ändern des E-Mail-Abo-Status anzeigen

Die Buttons basieren auf einem der drei Abo-Status von Braze: `subscribed`, `opted-in` und `unsubscribed`. Wenn ein:e Nutzer:in `subscribed` ist, kann der Agent zwischen `opt-in` und `unsubscribe` wählen. Wenn ein:e Nutzer:in `opted-in` oder `unsubscribed` ist, kann der Agent nur zwischen diesen beiden wechseln.

#### Liste der angepassten Attribute anzeigen

Wählen Sie, ob Sie die angepassten Braze-Attribute der Nutzer:innen anzeigen oder ausblenden möchten.

#### Liste angepasster Events anzeigen

Wählen Sie, ob Sie die angepassten Braze-Events der Nutzer:innen anzeigen oder ausblenden möchten.

#### Liste der Käufe anzeigen

Wählen Sie, ob Sie eine Liste der Produkte, die die Nutzer:innen gekauft haben, anzeigen oder ausblenden möchten. Hier können Sie sehen, wie oft die Nutzer:innen das Produkt gekauft haben. Um das Datum des ersten und letzten Kaufs anzuzeigen, bewegen Sie den Mauszeiger über den Artikel. 

### Beispiel-Integration

Im Folgenden sehen Sie ein Beispiel für die Integration:

![Die Integration von Braze und Dixa in Dixa, die den Status des E-Mail-Abos, angepasste Attribute, angepasste Events und Käufe einer Nutzerin oder eines Nutzers anzeigt.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

## Datentransformations-Tool

Dixa verwendet Webhooks, um Daten an Braze zu senden. Sie müssen Dixa-Administrator:in sein, um Webhooks zu konfigurieren.

Der erste Schritt besteht darin, eine Datentransformation in Braze zu erstellen. 

1. Gehen Sie zu **Dateneinstellungen** > **Datentransformationen** > **Transformation erstellen**.
2. Wählen Sie **Von Grund auf neu starten**, wählen Sie als Ziel **POST: Track Users** und wählen Sie **Transformation erstellen**.
3. Kopieren Sie im Transformations-Editor den Beispielcode aus dem Abschnitt **Beispiel für das Transformations-Tool** weiter unten und fügen Sie ihn in das Feld **Transformationscode** ein. Wählen Sie **Speichern**, kopieren Sie die **Webhook-URL** und öffnen Sie Dixa.
4. Gehen Sie in Dixa zu **Einstellungen** > **Integrationen** > **Webhooks** > **+ Ausgehender Webhook**.
5. Fügen Sie auf der Seite mit den Webhook-Einstellungen die URL von Braze ein und aktivieren Sie die Events, die Sie tracken möchten. **Konversation erstellt** ist ein guter Ausgangspunkt, um die Konversationen Ihrer Kund:innen zu verfolgen. 
6. Wählen Sie **Speichern**, um die Dixa-Einrichtung abzuschließen.

### Beispiel für das Transformations-Tool

```js
// Transforming the provided payload to match Braze /users/track endpoint specifications.

// Extracting necessary details from the payload
const requester = payload.data.conversation.requester;
const event = payload.data.conversation;

// Defining user attributes based on the provided payload, prioritizing email if available.
const userAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  _update_existing_only: false, // Set to false to create or update user profiles when identified by email
  organization: payload.organization.name, // Including an additional attribute for demonstration
};

// Defining event attributes based on the provided payload.
const eventAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  name: payload.event_fqn, // The name of the event
  time: event.created_at, // ISO 8601 datetime format
  properties: { // Including additional event properties
    event_version: payload.event_version,
    conversation_status: event.status,
    conversation_channel: event.channel
  },
  _update_existing_only: false // Set to false to create or update user profiles when identified by email
};

// Constructing the final object to match Braze /users/track endpoint schema
const brazecall = {
  attributes: [userAttributes], // Wrapping userAttributes in an array as per specifications
  events: [eventAttributes] // Wrapping eventAttributes in an array as per specifications
};

// Returning the transformed data
return brazecall;
```
