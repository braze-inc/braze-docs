---
nav_title: Front
article_title: Front
description: "Lernen Sie, wie Sie Front in Braze integrieren können"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> Mit der Integration von Front können Sie die Braze Data Transformation und Webhooks von jeder Plattform nutzen, um eine SMS-Pipeline für Konversationen in beide Richtungen einzurichten.

Der eingehende Webhook von Front enthält eine Nutzlast, die die vom Live-Agenten gesendete Nachricht enthält. Die Anfrage muss neu formatiert werden, bevor sie von Braze Endpunkten akzeptiert werden kann. Das Template für die Datentransformation an der Vorderseite formatiert die Nutzdaten neu und schreibt ein angepasstes Event mit dem Titel **Ausgehende SMS gesendet** in das Nutzerprofil, wobei der Nachrichtentext als Event-Eigenschaft übergeben wird.

Bevor Sie eine neue Transformation in Braze einrichten, empfehlen wir Ihnen, sich die Support-Matrix für jede Ebene in unserer Dokumentation zur [Datentransformation]({{site.baseurl}}/user_guide/data/data_transformation/overview/) anzusehen. Unsere Free- und Pro-Tiers bieten eine unterschiedliche Anzahl von aktiven Transformationen und eingehenden Anfragen pro Monat. Vergewissern Sie sich, dass Ihr aktueller Plan Ihren Anwendungsfall unterstützen kann.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung             | Beschreibung                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Front-Konto            | Um diese Partnerschaft zu nutzen, benötigen Sie ein Front-Konto.|
| Braze-Daten-Transformation Webhook URL | Die [Braze Datentransformation]({{site.baseurl}}/user_guide/data/data_transformation/overview/) wird verwendet, um den von Front eingehenden Webhook so umzuformatieren, dass er vom Braze /users/track Endpunkt akzeptiert werden kann.|
| Ein Front REST API-Schlüssel         | Ein Front REST API-Schlüssel wird verwendet, um eine ausgehende Webhook-Anfrage von Braze an Front zu stellen. |

## Anwendungsfälle

- Optimieren Sie Ihren Lead-Generierungsprozess mit automatisiertem SMS Messaging von Braze, um die Präferenzen der Nutzer:innen zu erkennen und den Live-Vertriebsmitarbeitern die Möglichkeit zu geben, den Verkauf nachzuverfolgen und abzuschließen.
- Binden Sie Kunden, die ihren Warenkorb-Abbruch verursacht haben, wieder ein, indem Sie die Konversion durch automatisierte SMS-Antworten und Live-Chat-Support fördern.

## Integration der Front

### Schritt 1: Erstellen Sie eine Datentransformation

Zunächst erstellen Sie eine neue Datentransformation in Braze. Die folgenden Schritte sind vereinfacht. Eine vollständige Anleitung finden Sie unter [Erstellen einer Transformation]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/).

1. Gehen Sie in Braze zu **Dateneinstellungen** > **Datentransformationen** und wählen Sie dann **Transformation erstellen**.
2. Wählen Sie unter **Bearbeitungserfahrung** die Option **Von Grund auf neu beginnen**.
3. Wählen Sie unter **Ziel auswählen** **POST: Nutzer:innen tracken**.
4. Kopieren Sie das folgende Template für die Transformation und fügen Sie es ein, speichern und aktivieren Sie den Endpunkt.
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

    Ihre Transformation sollte in etwa so aussehen wie die folgende:

    ![Ein Beispiel für eine Datentransformation.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
Sie können dieses Template an Ihre speziellen Bedürfnisse anpassen. Sie können zum Beispiel den voreingestellten Namen des angepassten Events anpassen. Weitere Informationen finden Sie unter [Übersicht über Datentransformationen]({{site.baseurl}}/user_guide/data/data_transformation/overview/).
{% endalert %}

### Schritt 2: Erstellen Sie eine ausgehende SMS-Kampagne

Als Nächstes erstellen Sie eine SMS-Kampagne, die auf Webhooks von Front wartet und eine angepasste SMS-Antwort an Ihre Kund:innen sendet.

#### Schritt 2.1: Verfassen Sie Ihre Nachricht

Fügen Sie in das Textfeld **Nachricht** den folgenden Liquid Code ein, zusammen mit einer Opt-out-Sprache oder anderen statischen Inhalten.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Ihre Nachricht sollte in etwa so aussehen wie die folgende:

![Eine Beispielnachricht mit Liquid Code.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Zeitplan für die Zustellung

Wählen Sie für die Art der Zustellung **aktionsbasierte Zustellung** und dann für den angepassten Event-Auslöser **Ausgehende SMS** ausgewählt.

![Die Seite "Zeitplan für die Zustellung".]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Bei diesem angepassten Event handelt es sich um die Datentransformation, die in das Profil des Nutzers geschrieben wird. Nachrichten von Agenten werden als Event-Eigenschaften zu diesem Ereignis gespeichert.
{% endalert %}

Schließlich aktivieren Sie unter **Zustellungskontrollen** die Wiederzulassung.

![Die Wiederzulassung wurde unter "Zustellungskontrollen" aktiviert.]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Schritt 3: Einen angepassten Kanal erstellen

Gehen Sie im Front-Dashboard zu **Einstellungen** > **Kanäle** > **Kanäle hinzufügen**, wählen Sie dann **Benutzerdefinierter Kanal** und geben Sie einen Namen für Ihren neuen Braze-Kanal ein.

![Ein angepasster Kanal für Braze im Front-Dashboard.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Schritt 4: Konfigurieren Sie die Einstellungen

Geben Sie in das Feld für den ausgehenden API Endpunkt die Webhook-URL für die Datentransformation ein [, die Sie zuvor erstellt haben](#step-1-set-up-a-data-transformation-in-braze). Alle ausgehenden Nachrichten von Live-Agenten auf Ihrem neuen Braze-Kanal werden hierher gesendet. Dieser Kanal stellt auch eine Endpunkt-URL zur Verfügung, an die Braze SMS-Nachrichten im Feld **Eingehende URL** weiterleiten kann.

Notieren Sie sich diese URL - Sie werden sie später brauchen.

![Die Kanaleinstellungen für den neu erstellten Braze-Kanal in Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Schritt 5: Eingehende SMS-Weiterleitung einrichten

Als nächstes erstellen Sie zwei neue Webhook-Kampagnen in Braze, damit Sie eingehende SMS von Kund:in an den Posteingang von Front weiterleiten können.

|Zahl|Zweck|
|---|---|
|Webhook Kampagne 1|Signalisiert Front, dass ein Live-Chat-Gespräch angefragt wird.|
|Webhook Kampagne 2|Leitet alle vom Kunden eingehenden SMS-Antworten an den Posteingang von Front weiter.|
{: .reset-td-br-1 .reset-td-br-2 }

#### Schritt 5.1: Erstellen Sie eine SMS-Schlüsselwortkategorie

Gehen Sie im Braze-Dashboard auf **Zielgruppe**, wählen Sie Ihre **SMS-Abo-Gruppe** und wählen Sie dann **Benutzerdefiniertes Schlüsselwort hinzufügen**. Um eine exklusive SMS-Schlüsselwortkategorie für Front zu erstellen, füllen Sie die folgenden Felder aus.

|Feld|Beschreibung|
|---|---|
|Keyword-Kategorie|Der Name Ihrer Schlüsselwortkategorie, z. B. `FrontSMS1`.|
|Keyword|Ihre angepassten Schlüsselwörter, wie z.B. `TIMETOMOW`. Vermeiden Sie gebräuchliche Wörter, um versehentliche Trigger zu vermeiden. Denken Sie daran, dass bei Schlüsselwörtern die Groß- und Kleinschreibung keine Rolle spielt. `lawn` würde also auf `LAWN` passen.|
|Antwortnachricht|Die Nachricht, die gesendet wird, wenn ein Schlüsselwort erkannt wird, z. B. "Ein Landschaftsgärtner wird sich in Kürze bei Ihnen melden."|
{: .reset-td-br-1 .reset-td-br-2 }

![Ein Beispiel für eine SMS-Schlüsselwortkategorie in Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Schritt 5.2: Erstellen Sie Ihre erste Webhook-Kampagne

Erstellen Sie im Braze-Dashboard Ihre erste Webhook-Kampagne mit der URL, [die Sie zuvor erstellt haben](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Ein Beispiel für die erste Webhook-Kampagne, die in Braze erstellt werden sollte.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Fügen Sie Ihrem Anfrage-Text Folgendes hinzu:

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

Auf dem Tab Einstellungen konfigurieren Sie die Anfrage-Header `Authorization`, `content-type` und `accept`.

![Eine Beispielanfrage mit den drei erforderlichen Kopfzeilen.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Schritt 5.3: Zeitplan für die erste Zustellung

Wählen Sie für die **Zeitplan-Zustellung** die **aktionsbasierte Zustellung** aus und wählen Sie dann für Ihren Auslösertyp **Eingehende SMS-Nachrichten senden**. Fügen Sie auch die SMS Abo-Gruppe und die Stichwortkategorie hinzu, die Sie [zuvor eingerichtet haben](#step-51-create-an-sms-keyword-category).

![Die Seite "Zeitplan für die Zustellung" für die erste Webhook-Kampagne.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Aktivieren Sie unter **Zustellungskontrollen** die Wiederzulassung.

![Wiederzulassung ausgewählt unter "Zustellungskontrollen" für die erste Webhook Kampagne.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Schritt 5.4: Erstellen Sie Ihre zweite Webhook-Kampagne

Da Ihre zweite Webhook-Kampagne mit der ersten übereinstimmen wird, können Sie [die erste duplizieren und umbenennen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns). Sie können dies jetzt tun.

#### Schritt 5.5: Zeitplan für die zweite Zustellung

Legen Sie für die **Zeitplan-Zustellung** den **aktionsbasierten Auslöser** und die **SMS-Abo-Gruppe** auf die gleiche Weise fest wie bei [der ersten Zustellung](#step-53-schedule-the-first-delivery). Für die **Kategorie Schlüsselwort** wählen Sie jedoch **Andere**.

![Die Seite "Geplante Zustellung" für die zweite Webhook-Kampagne, wobei als Stichwortkategorie "Andere" gewählt wurde.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Schritt 5.6: Einen Zielgruppen-Filter hinzufügen

Ihre Webhook-Kampagne kann jetzt eingehende SMS-Antworten Ihrer Kund:in weiterleiten. Um SMS-Antworten zu filtern, so dass nur Nachrichten für Live-Chats weitergeleitet werden, fügen Sie den Segmentierungsfilter **Zuletzt empfangene Nachricht von bestimmter Kampagne** zum **Schritt Zielgruppen** hinzu.

![Ein Zielgruppen-Filter mit der Auswahl "Zuletzt erhaltene Nachricht aus bestimmter Kampagne".]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Konfigurieren Sie dann Ihren Filter:

1. Wählen Sie unter **Kampagne** die SMS-Kampagne aus, [die Sie zuvor erstellt haben](#step-2-create-an-outbound-sms-campaign).
2. Für **Operator** wählen Sie **Kleiner als**.
3. Wählen Sie für **Zeitfenster** die Zeitspanne, die ein Chat geöffnet bleiben soll, ohne dass eine Kund:in antwortet.

![Die Konfigurationseinstellungen für den ausgewählten Zielgruppen-Filter.]({% image_buster /assets/img/front/front_target_audience.png %})

## Überlegungen

### Abrechenbare Segmente

- SMS-Nachrichten werden bei Braze pro Nachrichtensegment berechnet. Wenn Sie verstehen, was ein Segment definiert und wie diese Nachrichten aufgeteilt werden, können Sie sich ein Bild davon machen, wie Sie für Nachrichten abgerechnet werden. Weitere Informationen finden Sie in unserer [Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- Lange Agentenantworten werden mehr abrechenbare Segmente verbrauchen.

### Datenpunkt Verbrauch

Derzeit erfordert diese Integration, dass ein angepasstes Event in ein Nutzerprofil geschrieben wird, und zwar jedes Mal, wenn ein Live-Agent eine SMS von Front sendet. Dies mag für einen schnellen Austausch von nur ein paar Nachrichten geeignet sein - aber je länger die Konversationen werden, desto mehr Datenpunkte sind erforderlich. Für jedes angepasste Event, das in Braze protokolliert wird, wird ein Datenpunkt verbraucht.

### Einfügen von Links in SMS Nachrichten

Das Senden eines Links aus dem Front-Live-Chat wird mit zusätzlichen HTML-Tags dargestellt.

### Bilddatei von der Vorderseite anhängen

Bilddateien in Front werden in SMS Nachrichten, die von Braze gesendet werden, nicht dargestellt.

### Opt-outs 

Bei Nachrichten im Gespräch besteht ein höheres Risiko, dass sie das Wort "Stopp" oder ähnliche Formulierungen enthalten, die als unscharfe Opt-outs erkannt werden können.
