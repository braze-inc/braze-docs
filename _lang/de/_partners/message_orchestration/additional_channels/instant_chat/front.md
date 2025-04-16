---
nav_title: Front
article_title: Front
description: "Erfahren Sie, wie Sie Front mit Braze integrieren können"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> Die Integration von Front ermöglicht es Ihnen, die Datenumwandlung von Braze und Webhooks von jeder Plattform zu nutzen, um eine SMS-Pipeline für Konversationen in beide Richtungen einzurichten.

Der eingehende Webhook von Front enthält eine Nutzlast, die die vom Live-Agenten gesendete Nachricht enthält.  Die Vorlage Front Data Transformation formatiert die Nutzdaten neu und schreibt ein benutzerdefiniertes Ereignis mit dem Titel **Outbound SMS Sent** in das Benutzerprofil **,** wobei der Nachrichtentext als Ereigniseigenschaft übergeben wird.

 Unsere Free- und Pro-Tiers bieten eine unterschiedliche Anzahl von aktiven Transformationen und eingehenden Anfragen pro Monat. Vergewissern Sie sich, dass Ihr aktueller Tarif Ihren Anwendungsfall unterstützt.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung             | Beschreibung                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Front-Konto            | Um diese Partnerschaft zu nutzen, benötigen Sie ein Front-Konto.|
| Braze Data Transformation Webhook URL | |
| Ein Front REST API-Schlüssel         | Ein Front REST API-Schlüssel wird verwendet, um eine ausgehende Webhook-Anfrage von Braze an Front zu stellen. |

## Anwendungsfälle

- 
- Binden Sie Kunden, die ihren Einkaufswagen verlassen haben, wieder ein, indem Sie die Verkaufszahlen durch automatische SMS-Antworten und Live-Chat-Support steigern.

## Integration der Front

### Schritt 1: Erstellen Sie eine Datenumwandlung

Zunächst erstellen Sie eine neue Datentransformation in Braze. 

1. Gehen Sie in Braze zu **Dateneinstellungen** > **Datentransformationen** und wählen Sie dann **Transformation erstellen**.
2. Wählen Sie unter **Bearbeitungserfahrung** die Option **Von Grund auf neu beginnen**.
3. Wählen Sie unter **Ziel wählen** **POST: Benutzer verfolgen**.
4. Kopieren Sie die folgende Transformationsvorlage und fügen Sie sie ein, speichern und aktivieren Sie dann den Endpunkt.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Ihre Umwandlung sollte in etwa so aussehen wie die folgende:

    ![Ein Beispiel für eine Datenumwandlung.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
Sie können diese Vorlage an Ihre speziellen Bedürfnisse anpassen. Sie können zum Beispiel den voreingestellten Namen des Ereignisses anpassen. 
{% endalert %}

### Schritt 2: Erstellen Sie eine ausgehende SMS-Kampagne

Als Nächstes erstellen Sie eine SMS-Kampagne, die auf Webhooks von Front wartet und eine individuelle SMS-Antwort an Ihre Kunden sendet.

#### Schritt 2.1: Verfassen Sie Ihre Nachricht

Fügen Sie in das Textfeld **Nachricht** den folgenden Liquid-Code ein, zusammen mit einer eventuellen Abmeldesprache oder anderen statischen Inhalten.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Ihre Nachricht sollte in etwa wie folgt lauten:

![Eine Beispielnachricht mit Liquid-Code.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Planen Sie die Lieferung

Wählen Sie für die Zustellungsart **Aktionsbasierte Zustellung** und für den benutzerdefinierten Ereignisauslöser die Option **Ausgehende SMS gesendet**.

![Die Seite "Lieferung planen".]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Dieses benutzerdefinierte Ereignis ist die Datenumwandlung, die in das Profil des Benutzers geschrieben wird. Agentennachrichten werden als Ereigniseigenschaft zu diesem Ereignis gespeichert.
{% endalert %}

Aktivieren Sie schließlich unter **Lieferkontrollen** die Wiederzulassung.

![Wiederzulassung aktiviert unter "Lieferkontrollen".]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Schritt 3: Einen benutzerdefinierten Kanal erstellen

Gehen Sie im Front-Dashboard zu **Einstellungen** > **Kanäle** > **Kanäle hinzufügen**, wählen Sie dann **Benutzerdefinierter Kanal** und geben Sie einen Namen für Ihren neuen Braze-Kanal ein.

![Ein benutzerdefinierter Kanal für Braze im vorderen Armaturenbrett.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Schritt 4: Konfigurieren Sie die Einstellungen

Geben Sie in das Feld ausgehender API-Endpunkt die Datenumwandlungs-Webhook-URL ein [, die Sie zuvor erstellt haben](#step-1-set-up-a-data-transformation-in-braze). Alle ausgehenden Nachrichten von Live-Agenten auf Ihrem neuen Braze-Kanal werden hierher gesendet. Dieser Kanal enthält auch eine Endpunkt-URL, an die Braze die SMS-Nachrichten weiterleiten soll, im Feld **Eingehende URL**.

Notieren Sie sich diese URL - Sie werden sie später brauchen.

![Die Kanaleinstellungen für den neu erstellten Braze-Kanal in Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Schritt 5: Eingehende SMS-Weiterleitung einrichten

Als nächstes erstellen Sie zwei neue Webhook-Kampagnen in Braze, damit Sie eingehende SMS von Kunden an den Posteingang von Front weiterleiten können.

|Zahl|Zweck|
|---|---|
|Webhook-Kampagne 1|Signalisiert Front, dass ein Live-Chat-Gespräch gewünscht wird.|
|Webhook-Kampagne 2|Leitet alle vom Kunden gesendeten SMS-Antworten an den Posteingang der Front weiter.|
{: .reset-td-br-1 .reset-td-br-2 }

#### Schritt 5.1: Erstellen Sie eine SMS-Schlüsselwortkategorie

Gehen Sie im Braze Dashboard zu **Zielgruppe**, wählen Sie Ihre **SMS-Abonnementgruppe** und wählen Sie dann **Benutzerdefiniertes Schlüsselwort hinzufügen**. Um eine exklusive SMS-Schlüsselwortkategorie für Front zu erstellen, füllen Sie die folgenden Felder aus.

|Feld|Beschreibung|
|---|---|
|Keyword-Kategorie|Der Name Ihrer Schlüsselwortkategorie, z. B. `FrontSMS1`.|
|Keyword|Ihre benutzerdefinierten Schlüsselwörter, wie `TIMETOMOW`. Vermeiden Sie gebräuchliche Wörter, um versehentliche Auslöser zu vermeiden. Denken Sie daran, dass bei Schlüsselwörtern die Groß- und Kleinschreibung keine Rolle spielt. `lawn` würde also auf `LAWN` passen.|
|Antwortnachricht|Die Nachricht, die gesendet wird, wenn ein Schlüsselwort erkannt wird, z. B. "Ein Landschaftsgärtner wird sich in Kürze bei Ihnen melden."|
{: .reset-td-br-1 .reset-td-br-2 }

![Ein Beispiel für eine SMS-Schlüsselwortkategorie in Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Schritt 5.2: Erstellen Sie Ihre erste Webhook-Kampagne

Erstellen Sie im Braze-Dashboard Ihre erste Webhook-Kampagne unter Verwendung der URL, [die Sie zuvor erstellt haben](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Ein Beispiel für die erste Webhook-Kampagne, die in Braze erstellt werden sollte.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Fügen Sie Folgendes in den Text Ihrer Anfrage ein:

{% raw %}
```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

Auf der Registerkarte Einstellungen konfigurieren Sie Ihre `Authorization`, `content-type` und `accept` Anfrage-Header.

![Eine Beispielanfrage mit den drei erforderlichen Kopfzeilen.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Schritt 5.3: Planen Sie die erste Lieferung

Wählen Sie für **Zeitgesteuerte Zustellung** die Option **Aktionsbasierte Zustellung** und wählen Sie dann als Auslösertyp **Ankommende SMS senden**. Fügen Sie auch die SMS-Abonnementgruppe und die Stichwortkategorie hinzu, die Sie [zuvor eingerichtet haben](#step-51-create-an-sms-keyword-category).

![Die Seite "Lieferung planen" für die erste Webhook-Kampagne.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Aktivieren Sie unter **Lieferungskontrollen** die Wiederzulassung.

![Die Wiederzulassung wurde unter "Zustellungskontrollen" für die erste Webhook-Kampagne ausgewählt.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Schritt 5.4: Erstellen Sie Ihre zweite Webhook-Kampagne

Da Ihre zweite Webhook-Kampagne mit der ersten übereinstimmen wird, können Sie [die erste duplizieren und sie umbenennen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns). Sie können dies jetzt tun.

#### Schritt 5.5: Planen Sie die zweite Lieferung

Stellen Sie für die **geplante Zustellung** den **aktionsbasierten Auslöser** und die **SMS-Abonnementgruppe** auf denselben Wert wie bei [der ersten Zustellung](#step-53-schedule-the-first-delivery). Für die **Kategorie Schlüsselwort** wählen Sie jedoch **Andere**.

![Die Seite "Geplante Zustellung" für die zweite Webhook-Kampagne, wobei als Stichwortkategorie "Andere" gewählt wurde.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Schritt 5.6: Einen Publikumsfilter hinzufügen

Ihre Webhook-Kampagne kann jetzt eingehende SMS-Antworten von Ihren Kunden weiterleiten. Um SMS-Antworten so zu filtern, dass nur Nachrichten für Live-Chats weitergeleitet werden, fügen Sie den Segmentierungsfilter **Letzte erhaltene Nachricht von bestimmter Kampagne** zum **Schritt Zielgruppen** hinzu.

![Ein Publikumsfilter mit der Auswahl "Letzte erhaltene Nachricht von bestimmter Kampagne".]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Konfigurieren Sie dann Ihren Filter:

1. Wählen Sie unter **Kampagne** die SMS-Kampagne aus, [die Sie zuvor erstellt haben](#step-2-create-an-outbound-sms-campaign).
2. Für **Operator** wählen Sie **Kleiner als**.
3. Wählen Sie unter **Zeitfenster** die Zeitspanne, die ein Chat offen bleiben soll, ohne dass der Kunde antwortet.

![Die Konfigurationseinstellungen für den ausgewählten Publikumsfilter.]({% image_buster /assets/img/front/front_target_audience.png %})

## Überlegungen

### Abrechenbare Segmente

- SMS-Nachrichten werden bei Braze pro Nachrichtensegment berechnet. Wenn Sie wissen, was ein Segment ausmacht und wie diese Nachrichten aufgeteilt werden, ist es wichtig zu verstehen, wie Sie für die Nachrichten abgerechnet werden. Weitere Informationen finden Sie in unserer [Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments).
- Lange Antworten von Agenten werden mehr abrechenbare Segmente verbrauchen.

### Datenpunkt Verbrauch

Derzeit erfordert diese Integration, dass jedes Mal, wenn ein Live-Agent eine SMS von Front sendet, ein benutzerdefiniertes Ereignis in ein Benutzerprofil geschrieben wird. Dies mag für einen schnellen Austausch von nur ein paar Nachrichten geeignet sein - aber je länger die Konversationen werden, desto mehr Datenpunkte sind erforderlich. Für jedes benutzerdefinierte Ereignis, das in Braze protokolliert wird, wird ein Datenpunkt verbraucht.

### Einfügen von Links in SMS-Nachrichten

Das Senden eines Links aus dem Front-Live-Chat wird mit zusätzlichen HTML-Tags dargestellt.

### Bilddatei von der Vorderseite anhängen

Bilddateien in Front werden in SMS-Nachrichten, die von Braze gesendet werden, nicht dargestellt.

### Abmeldungen 

Bei Sprachnachrichten besteht ein höheres Risiko, dass sie das Wort "Stopp" oder eine ähnliche Formulierung enthalten, die als unscharfe Opt-outs erkannt werden können.
