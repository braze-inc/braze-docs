---
nav_title: Regal
article_title: Regal
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Regal, einer Telefon- und SMS-Verkaufslösung, mit der Sie Daten aus beiden Quellen nutzen können, um personalisierte Erlebnisse für Ihre Kunden zu schaffen."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io][6] ist die Lösung für den Telefon- und SMS-Vertrieb, mit der Sie mehr Gespräche führen und so Ihre Wachstumsziele schneller erreichen können.

Durch die Integration von Regal und Braze können Sie ein konsistentes und personalisiertes Erlebnis über alle Ihre Kundenkontaktpunkte hinweg schaffen.
- Senden Sie die richtige nächstbeste E-Mail oder Push-Benachrichtigung von Braze auf der Grundlage dessen, was in einem Telefongespräch auf Regal gesagt wurde.
- Lösen Sie einen Anruf in Regal aus, wenn ein hochwertiger Kunde auf eine Marketing-E-Mail von Braze klickt, aber nicht konvertiert.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Regal-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Regal-Konto. |
| Regal API-Schlüssel | Ein Regal-API-Schlüssel ermöglicht das Senden von Ereignissen von Braze an Regal.<br><br>Senden Sie eine E-Mail an [support@regal.io](mailto:support@regal.io), um diesen Schlüssel zu erhalten. |
| Braze Data Transformation | Die Datenumwandlung befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Customer Success Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind. Dies ist notwendig, um Daten von Regal zu empfangen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration: Senden von Daten von Braze zu Regal

Im folgenden Abschnitt wird beschrieben, wie Sie Braze als Quelle für das Senden Ihrer Kundenprofil- und Ereignisdaten an Regal mithilfe von Braze Canvas oder Kampagnen-Webhooks verwenden.

### Schritt 1: Neue Kontakte in Regal erstellen

Erstellen Sie ein Canvas oder eine Kampagne, die jedes Mal, wenn ein neuer Kontakt in Braze erstellt wird, der für Anrufe und SMS in Regal verfügbar sein soll, einen Webhook zu Regal herstellt. 

1. Erstellen Sie ein Canvas oder eine Kampagne mit dem Titel "Neuen Kontakt für Regal erstellen" und wählen Sie als Eintragstyp " **Aktionsbasiert"**.

2. Legen Sie die Auslöserlogik als **Benutzerdefiniertes Ereignis** fest und wählen Sie das Ereignis, das ausgelöst wird, wenn ein Kontakt mit einer Telefonnummer erstellt wird. Regal empfiehlt außerdem, einen zusätzlichen Filter für das Telefonfeld hinzuzufügen, der sicherstellt, dass es eingestellt ist.

3. Füllen Sie in Ihrer neuen Webhook-Vorlage die folgenden Felder aus:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

Regal.io erfordert auch einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits in der Vorlage als Schlüssel-Wert-Paar auf der Registerkarte **Einstellungen** enthalten:
{% raw %}
- **HTTP-Methode**: POST
- **Kopfzeilen anfordern**:
    - **Autorisierung**: `{{<REGAL_API_KEY>}}`
    - **Inhalt-Typ**: application/json
{% endraw %}

#### Anfragetext

Das einzige erforderliche Feld darunter ist die Eigenschaft `traits.phone`. Der Rest ist optional. Wenn Sie jedoch `optIn` einschließen, müssen Sie `optIn.channel` und `optIn.subscribed` einschließen.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

Das obige Beispiel für die Nutzdaten setzt voraus, dass alle Ihre Kontakte das Opt-in für Sprache und SMS akzeptiert haben. Wenn das nicht der Fall ist, können Sie die Eigenschaft `optIn` aus der obigen Liste entfernen und ein separates Canvas oder eine Kampagne einrichten, um einen Kontakt in Regal zu aktualisieren, wenn `optIn` erfasst wird.

### Schritt 2: Opt-in-Informationen aktualisieren 

Wenn Opt-In und Opt-Out an verschiedenen Stellen in Ihrer App stattfinden können, ist es wichtig, Regal zu aktualisieren, wenn Benutzer sich ein- oder austragen. Im Folgenden finden Sie eine empfohlene Anleitung, wie Sie aktuelle Opt-in-Informationen an Regal senden können. Es wird davon ausgegangen, dass Sie dies als Braze-Profilfeld speichern, aber wenn nicht, kann der Auslöser genauso gut ein Ereignis in Ihrem Braze-Konto sein, das eine An- oder Abmeldung eines Benutzers darstellt. (Das folgende Beispiel bezieht sich auf die telefonische Anmeldung, aber Sie können ein ähnliches Canvas oder eine Kampagne für die SMS-Anmeldung einrichten, wenn Sie diese separat sammeln).

1. Erstellen Sie ein neues Canvas oder eine Kampagne mit dem Titel "Opt-In oder Out an Regal senden".

2. Wählen Sie eine der folgenden Auslöseroptionen und wählen Sie das Feld, das den Opt-in-Status des Benutzers darstellt. Wenn Sie ein Ereignis an Braze senden, um ein Opt-in oder ein Opt-out darzustellen, verwenden Sie stattdessen dieses Ereignis als Auslöser.
    - Benutzerprofilfeld aktualisiert
    - Status der Abonnementgruppe aktualisieren
    - Status des Abonnements

3. Füllen Sie in Ihrer neuen Webhook-Vorlage die folgenden Felder aus:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

Regal.io erfordert auch einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, allerdings auf der Registerkarte **Einstellungen**:
{% raw %}
- **HTTP-Methode**: POST
- **Kopfzeilen anfordern**:
    - **Autorisierung**: `{{<REGAL_API_KEY>}}`
    - **Inhalt-Typ**: application/json
{% endraw %}

#### Anfragetext

Sie können auch gerne zusätzliche Benutzerprofilattribute in diese Nutzlast aufnehmen, wenn Sie sicherstellen möchten, dass mehr Attribute gleichzeitig auf dem neuesten Stand sind.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### Schritt 3: Benutzerdefinierte Ereignisse senden

Schließlich richten Sie ein Canvas oder eine Kampagne für jedes Schlüsselereignis ein, das Sie an Regal senden möchten. Regal empfiehlt, alle Ereignisse zu senden, die für die Auslösung von SMS und Anrufen in Regal wichtig sind (z. B. ein Ereignis bei jedem Schritt des Anmelde- oder Kaufprozesses) oder die als Ausstiegskriterien für Kontakte verwendet werden, die aus Regal-Kampagnen herausfallen sollen.

Unten sehen Sie zum Beispiel einen Workflow, der Regal ein Ereignis sendet, wenn ein Benutzer den ersten Schritt einer Anwendung abschließt.

1. Erstellen Sie ein neues Canvas oder eine neue Kampagne mit dem Titel "Send Application Step 1 Completed Event to Regal".

2. Legen Sie die Logik des Auslöseknotens als **Benutzerdefiniertes Ereignis** fest und wählen Sie den Namen des Ereignisses, das Sie an Regal senden möchten, z. B. "Anwendungsschritt 1 abgeschlossen".

3. Füllen Sie in Ihrer neuen Webhook-Vorlage die folgenden Felder aus:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

Regal.io erfordert auch einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, allerdings auf der Registerkarte **Einstellungen**:
{% raw %}
- **HTTP-Methode**: POST
- **Kopfzeilen anfordern**:
    - **Autorisierung**: `{{<REGAL_API_KEY>}}`
    - **Inhalt-Typ**: application/json
{% endraw %}

#### Anfragetext

Sie können gerne zusätzliche Benutzerprofilattribute in diese Nutzlast aufnehmen, wenn Sie sicherstellen möchten, dass mehr Attribute gleichzeitig auf dem neuesten Stand sind.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

#### Aktuelle Kontaktattribute

Auch wenn es nicht notwendig ist, empfiehlt Regal, alle wichtigen Datenfelder des Benutzerprofils an die Ereignis-Payloads Ihrer Ereignis-Workflows zu senden, um sicherzustellen, dass Regal Zugriff auf die aktuellsten Kontaktattribute hat, wenn wichtige Ereignisse verfügbar werden.

{% alert note %}
Wenn Sie Fragen dazu haben, welche Ereignisse wichtig sind, um sie an Regal zu senden, oder wie Sie diese Canvases und Kampagnen am besten einrichten, kontaktieren Sie support@regal.io.
{% endalert %}

## Integration: Senden von Daten von Regal an Braze

In diesem Abschnitt wird beschrieben, wie Sie Regal-Berichtsereignisse wie `SMS.sent` und `call.completed` in Braze übertragen, damit sie in Ihren Braze-Profilen erscheinen und im Braze-Segmentierungstool, in Canvas und in Kampagnen verfügbar sind. Diese Integration verwendet Regal Reporting Webhooks und Braze Data Transformation, um den Datenfluss zu automatisieren.

### Schritt 1: Erstellen Sie eine Datenumwandlung in Braze

{% alert important %}
Die Datenumwandlung befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Customer Success Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind.
{% endalert %}

Braze empfiehlt, eine Transformation für den Regal-Webhook zu erstellen, den Sie an Braze senden möchten. 

Um eine Datenumwandlung zu erstellen:
1. Navigieren Sie zur Seite **Transformationen** in Ihrem Braze Dashboard.
2. Geben Sie Ihrer Transformation einen Namen und klicken Sie auf **Transformation erstellen**.
3. Klicken Sie in der Liste der Transformationen auf <i class="fa-solid fa-ellipsis-vertical" title="Aktionen anzeigen"></i> und wählen Sie **Webhook-URL kopieren**.

![][4]

### Schritt 2: Aktivieren Sie Webhooks für die Berichterstattung in Regal

So richten Sie Webhooks für Berichte ein:
1. Gehen Sie zur Regal-App und öffnen Sie die **Einstellungsseite**.

2. Klicken Sie im Bereich **Reporting Webhooks** auf **Webhooks erstellen**.

3. Fügen Sie in der Eingabe für den Webhook-Endpunkt die Webhook-URL der Braze Datenumwandlung für die zugehörige Datenumwandlung hinzu.

![][5]{: style="max-width:60%;"}

#### Aktualisieren eines Endpunkts
Wenn Sie einen Endpunkt bearbeiten, kann es bis zu 5 Minuten dauern, bis der Cache aktualisiert ist und stattdessen Ereignisse an Ihren neuen Endpunkt gesendet werden.
#### Wiederholungen
Derzeit gibt es bei diesen Ereignissen keine Wiederholungsversuche. Wenn innerhalb von 5 Sekunden keine Antwort eingeht, wird das Ereignis verworfen und nicht erneut versucht. Regal wird in einer zukünftigen Version Wiederholungsversuche hinzufügen.
#### Events
Der [Reporting Webhooks Leitfaden von Regal][7] enthält die vollständige Liste der Reporting-Ereignisse, die sie veröffentlichen. Dort können Sie auch Definitionen von Eigenschaften und Beispiel-Nutzdaten sehen.

### Schritt 3: Verwandeln Sie Regal-Events in Braze-Events

Mit der [Datenumwandlungsfunktion]({{site.baseurl}}/data_transformation) von Braze können Sie eingehende Regal-Ereignisse in das Format umwandeln, das erforderlich ist, um sie als Attribute, Ereignisse oder Käufe in Braze hinzuzufügen.

1. Benennen Sie Ihre Datenumwandlung. Es wird empfohlen, eine Datenumwandlung pro Ereignis-Webhook einzurichten.

2. Um die Verbindung zu testen, führen Sie einen ausgehenden Anruf vom Regal Agent Desktop zu Ihrem Mobiltelefon und übermitteln Sie das Formular Gesprächszusammenfassung, um ein call.completed Ereignis zu erstellen.

3. Legen Sie fest, welche Identifikatoren Sie für die Zuordnung Ihrer Regal-Kontakte zu Ihren Braze-Profilen verwenden möchten. Zu den verfügbaren Identifikatoren in Regal-Ereignissen gehören:
   - `userId` - nur bei Ereignissen gesetzt, wenn Sie diese Kennung zuvor für einen Kontakt gesendet haben
   - `traits.phone`
   - `traits.email` - nur bei Ereignissen gesetzt, wenn Sie diese Kennung zuvor für einen Kontakt gesendet haben

#### Braze-unterstützte Identifikatoren
- Braze unterstützt keine Telefonnummern als Identifikator. Um diese als Kennung zu verwenden, kann die Telefonnummer als [Benutzer-Alias][8] in Braze eingestellt werden.
- Bei der Verwendung von Braze Data Transformation kann die E-Mail-Adresse als Identifikator verwendet werden. Wenn die E-Mail-Adresse als Profil in Braze existiert, wird das bestehende Profil aktualisiert. Wenn die E-Mail-Adresse noch nicht in Braze vorhanden ist, wird ein reines E-Mail-Profil erstellt.

## Anwendungsfälle

{% tabs %}
{% tab Eine E-Mail auslösen %}

**Auslösen einer E-Mail von Braze basierend auf einer Anrufdisposition in Regal**

Nachfolgend sehen Sie ein Beispiel für ein `call.completed` Ereignis in Regal. 

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

Nachfolgend finden Sie ein Beispiel für eine Datenumwandlung, um dies einem benutzerdefinierten Ereignis in Braze zuzuordnen.

```
// Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Profilattribute aktualisieren %}

**Aktualisieren Sie Profilattribute in Braze basierend auf `contact.attribute.edited` Ereignissen von Regal**

Nachfolgend sehen Sie ein Beispiel für ein `contact.attribute.edited` Ereignis in Regal. Dieses Ereignis wird jedes Mal ausgelöst, wenn einer Ihrer Agenten in einem Gespräch etwas Neues erfährt und ein Attribut im Profil des Kontakts aktualisiert.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

Nachfolgend finden Sie ein Beispiel für eine Datenumwandlung, um die neuen benutzerdefinierten Eigenschaftswerte den entsprechenden Attributen in Ihren Braze-Profilen zuzuordnen:

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Halten Sie Ihre Experimente auf dem Laufenden %}

**Halten Sie Ihre Experimente in Braze und Regal mit Hilfe von `contact.experiment.assigned` Ereignissen synchronisiert.**

Nachfolgend sehen Sie ein Beispiel für ein `contact.experiment.assigned` Ereignis in Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

Nachfolgend finden Sie ein Beispiel für eine Datenumwandlung, um dies einem benutzerdefinierten Ereignis in Braze zuzuordnen.

```
// Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Einen Kontakt abbestellen %}

**Abbestellen eines Kontakts in Braze auf der Grundlage einer `contact.unsubscribed` von Regal**

Nachfolgend sehen Sie ein Beispiel für ein `contact.unsubscribed` Ereignis in Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

Nachfolgend finden Sie ein Beispiel für eine Datenumwandlung, um den Kontakt in Braze abzumelden.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% endtabs %}

[2]: {% image_buster /assets/img/regal/webhook_rawtext.png %}
[3]: {% image_buster /assets/img/regal/request_header.png %}
[4]: {% image_buster /assets/img/regal/copy_webhook_url.png %}
[5]: {% image_buster /assets/img/regal/edit_webhook.png %}
[6]: https://regal.io
[7]: https://developer.regal.io/docs/reporting-webhooks#events
[8]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases