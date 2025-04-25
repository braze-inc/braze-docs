--- 
nav_title: SessionM
article_title: SessionM
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und SessionM, einer Customer-Engagement- und Loyalitätsplattform."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# SessionM Treueplattform

> [SessionM](https://www.mastercardservices.com/en/capabilities/sessionm) ist eine Plattform für Customer-Engagement und Kundentreue, die Marketern Features für das Kampagnenmanagement und Lösungen für das Loyalitätsmanagement zur Verfügung stellt, um das Engagement und den Gewinn durch gezielte Ansprache zu steigern.

## Voraussetzungen

| Quelle | Anforderung | Beschreibung |
| --- | --- | --- |
| Braze | Ein Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `trigger_send` Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze | Ein Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| Braze und SessionM | Passender Bezeichner | Um die Integration zu nutzen, stellen Sie sicher, dass sowohl SessionM als auch Braze über einen Datensatz mit den von jeder Plattform verwendeten Bezeichnern verfügen. Verweise auf `user_id` entsprechen dem Bezeichner des Nutzers:in, der zum Zeitpunkt der Erstellung des Profils in SessionM generiert wurde. |
| SessionM | Ein SessionM-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein SessionM-Konto. |
| SessionM | Ein SessionM Core REST Endpunkt | Ihr Endpunkt hängt von der SessionM URL Ihrer Instanz ab. Diese kann im Dashboard von SessionM unter **Digitale Eigenschaften** erstellt werden. |
| SessionM | Ein SessionM Core REST API-Schlüssel | Der SessionM API-Schlüssel, der mit Ihrer Instanz und der Braze Integration verbunden ist. Dieser Schlüssel kann für alle Core-basierten Aufrufe einschließlich Tags verwendet werden. Diese kann im Dashboard von SessionM unter **Digitale Eigenschaften** erstellt werden. |
| SessionM | Ein SessionM Core REST API Geheimnis | Das SessionM API-Geheimnis, das mit Ihrer Instanz und der Braze-Integration verbunden ist. Dieser Schlüssel kann für alle Core-basierten Aufrufe einschließlich Tags verwendet werden. Diese kann im Dashboard von SessionM unter **Digitale Eigenschaften** erstellt werden. |
| SessionM | Ein SessionM Connect REST Endpunkt | Ihr Endpunkt hängt von der SessionM URL Ihrer Instanz ab. Bitte wenden Sie sich an Ihren technischen Account Manager oder Ihr Zustellungsteam von SessionM. |
| SessionM | A SessionM Connect REST Autorisierungs-String | Der SessionM Connect Basic Authorization String, der mit Ihrer Instanz verknüpft ist. Dieser String zur Authentifizierung kann für alle connect-basierten Aufrufe verwendet werden, einschließlich get_user_offers. Bitte wenden Sie sich an Ihren technischen Account Manager oder Ihr Zustellungsteam von SessionM. |
| SessionM | A SessionM Connect REST Einzelhändler ID | Eine eindeutige Kennung für den spezifischen Kunden, der mit Ihrer Instanz verbunden ist. Wenden Sie sich an Ihren technischen Account Manager oder Ihr Zustellungsteam von SessionM. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) verwenden, können Sie einen API-Schlüssel unter **Entwickler:in** > **API-Einstellungen** erstellen.
{% endalert %} 

## Anwendungsfälle

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten, wie Sie die Integration von SessionM und Braze nutzen können.

- Erstellen Sie eine Segmentierung, die Daten aus allen Kundenbindungs-, Kundenmanagement- und Messaging-Plattformen einbezieht.
- Nutzen Sie eine solide Segmentierung, um bestimmte Nutzergruppen mit Angeboten und Aktionen anzusprechen.
- Nutzen Sie immer die aktuellsten Benutzer-, Angebots- und Treueinformationen, wenn Sie Nachrichten versenden.
- Informieren Sie Ihre Kunden ausführlich über den Fortschritt und den Abschluss von Werbe- und Treueaktionen.
- Benachrichtigen Sie Ihre Kunden, wenn es ein neues Angebot gibt, und geben Sie die Einzelheiten des Angebots bekannt.

## Integration von SessionM mit Braze

### Schritt 1: Erstellen eines Segments in Braze

Erstellen Sie in Braze ein Segment von Nutzer:innen für das Targeting mit SessionM-Aktionen und Angeboten. 

![Segment Builder mit dem ausgewählten Filter "Angepasste Attribute".]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Schritt 2: Segmente von Braze in SessionM importieren

#### Option 1: Export zum SessionM Tag Endpunkt (empfohlen)

Erstellen Sie zunächst eine Webhook-Kampagne in Braze und setzen Sie die Webhook-URL auf {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Verwenden Sie Liquid, um die `user_id` innerhalb der URL zu definieren. 

Stellen Sie den **Body für die Anfrage** des Webhooks mit Hilfe eines Rohtextes so zusammen, dass er die gewünschten Tags, die dem Nutzerprofil in SessionM hinzugefügt werden sollen, und die gewünschte Zeitspanne enthält. Ein Beispiel ist:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

Auf dem Tab **Einstellungen** fügen Sie die Schlüssel-Wert-Paare für jedes Anfrage-Header-Feld hinzu:
    \- Erstellen Sie einen Schlüssel `Content-Type` mit einem entsprechenden Wert `application/json`
    \- Erstellen Sie einen Schlüssel `Authorization` mit einem entsprechenden Wert `Basic YOUR-ENCODED-STRING-KEY`. Wenden Sie sich an Ihr SessionM Team, um den kodierten String-Schlüssel für Ihren Endpunkt zu erhalten. 

![Webhook-Einstellungen.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Planen Sie Ihre Zustellung, legen Sie Ihre **Zielgruppen** für das Targeting des [zuvor erstellten](#step-1-create-a-segment-in-braze) Segments fest und starten Sie dann Ihre Kampagne.

{% alert important %}
Dieser Vorgang kann auch über einen API Client, wie z.B. Postman, durchgeführt werden, indem Sie eine Anfrage direkt an den [SessionM Tag Endpunkt](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) stellen und dabei den Kunden, den Tag-Namen und eine Zeitspanne für jeden Nutzer: in des Anrufs angeben (ein Nutzer pro Anruf).
<br><br>
Die folgende Beispielanfrage verwendet cURL. 

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### Option 2: CSV-Import

Exportieren Sie Ihre Segmente aus Braze mit dem Braze Segmenter und stellen Sie SessionM eine CSV-Datei zur Verfügung, die die zu taggenden Kund:innen, den Tag-Namen und eine Laufzeit für jeden Nutzer:innen in der Datei enthält.

## Abrufen von Realtime-Angeboten mit Braze

Die Integration von SessionM mit Braze erlaubt den Abruf von Nutzerdaten in Echtzeit zum Zeitpunkt des Versendens von Nachrichten mit Hilfe von Connected-Content, um das Risiko auszuschalten, dass veraltete, abgelaufene oder bereits eingelöste Treueangebote an die Nutzer:innen übermittelt werden. 

Das folgende Beispiel zeigt, wie Connected-Content als Template verwendet wird, um Daten aus der Brieftasche in eine Nachricht zu integrieren. Connected-Content kann jedoch mit jedem der Connect-Endpunkte von SessionM verwendet werden. 

### Schritt 1: Angebot in SessionM ausgeben

SessionM bietet Kund:in verschiedene interne Hebel an, die angepasst werden können. Nach der Ausgabe werden die Angebote in einen Zustand versetzt, den SessionM als "Angebotsmappe" bezeichnet.

Ein Kund:in muss die gewünschte Aktion durchführen oder das Targeting erfüllen und erhält das Angebot innerhalb von SessionM.

SessionM fügt das Angebot dann der Brieftasche des Kund:in im ausgegebenen Zustand hinzu.

### Schritt 2: SessionM Offer Wallet API aufrufen

In Kampagnen oder Canvas-Schritten mit den SessionM-Angeboten verwenden Sie [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/), um einen API-Aufruf an den [SessionM `get_user_offers` Endpunkt](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/) zu tätigen.

Geben Sie in der Connected-Content-Anfrage die SessionM `user_id` des Nutzers und Ihre `retailer_id` an, um die vollständige Liste der aktiven Angebote abzurufen, die der Kund:innen in seiner Brieftasche hat. Jede Anfrage an diesen Endpunkt kann einen einzelnen Nutzer:innen enthalten. Wenden Sie sich an das Team von SessionM, um den kodierten String-Schlüssel für den grundlegenden Autorisierungs-Header in Ihrem Connected-Content-Aufruf zu erhalten.

Im Körper der Anfrage ist `culture` standardmäßig auf `en-US` eingestellt, aber Sie können Liquid verwenden, um ein Template für die Sprache eines Nutzers:innen für mehrsprachige SessionM-Angebote zu erstellen (z.B. mit {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post     
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### Schritt 3: Angebotspalette für Braze Messaging auffüllen

Nachdem eine Anfrage an den Endpunkt gestellt wurde, gibt SessionM die vollständige Liste der Angebote im Ausgabestatus zurück, zusammen mit den vollständigen Details zu jedem Angebot. Dies ist ein Beispiel für eine zurückgegebene Antwort:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Mit der Liquid-Dot-Notation kann dies in die Nachricht eingefügt werden. Um die Nachricht mit dem Ergebnis `offer_id` zu personalisieren, könnten Sie beispielsweise die Rückgabe-Nutzlast nutzen, indem Sie {% raw %}`{{wallet.payload.available_points}`{% endraw %} verwenden, die `100` zurückgibt.

{% alert note %}
Dies ist eine individuelle API. Wenn Sie beabsichtigen, einen Stapel von mehr als 500 Nutzer:innen zu versenden, setzen Sie sich mit Ihrem SessionM Team in Verbindung, um zu erfahren, wie Sie Massendaten in die Integration einbeziehen können.
{% endalert %}

## Einrichten von getriggerten Nachrichten

Die Integration von SessionM und Braze erlaubt es, Daten aus Nutzerprofilen, Angebotsdetails und Punktesalden dynamisch in Messaging einzubringen und in Echtzeit an den Kunden zu senden, wenn dieser aktiv wird.

### Schritt 1: SessionM Zustellung Team konfiguriert Templates

Arbeiten Sie mit Ihrem SessionM Zustellungsteam zusammen, um Templates für die Verwendung in Ihren getriggerten Nachrichten zu entwickeln. SessionM fügt Nutzerprofildaten, Angebotsdetails und Punktesalden in das Messaging ein und triggert sie in Braze für Nachrichten in Realtime.

Zu den Standardfeldern in allen Templates von SessionM gehören:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
Wenn Sie die `broadcast flag` auf `true` einstellen, wird die Nachricht an das gesamte Segment gesendet, auf das die Kampagne oder das Canvas in Braze abzielt.
{% endalert %}

Zusätzliche Felder können je nach Bedarf konfiguriert werden:

- **Daten anbieten:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Daten des Punktpreises:** `point award amount`, `point account name`
- **Daten zum Auslösen von Ereignissen:** Alle Daten im Trigger-Ereignis, die das Ergebnis des Triggers/Sende-Webhooks nutzen
- **Kampagnenspezifische Daten:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Zusätzliche Felder werden an Braze als `trigger_properties` gesendet, um die Nachricht zu personalisieren. 

### Schritt 2: Erstellen Sie eine Braze-Kampagne oder ein Braze-Canvas

Erstellen Sie eine API-getriggerte Kampagne oder ein Canvas in Braze, das von SessionM getriggert werden kann. Wenn zusätzliche Felder konfiguriert wurden, wie `offer_id` oder `offer title`, verwenden Sie Liquid (z.B. {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}), um die personalisierten Felder in Ihre Nachrichten einzufügen.

![API triggernde Eigenschaften.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

Auf dem Tab **Zeitplan Zustellung** notieren Sie sich die ID der Kampagne oder des Canvas, da diese zu den **erweiterten Einstellungen der** SessionM-Kampagne hinzugefügt wird.

![API-getriggerte Kampagne.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Schließen Sie die Details Ihrer Kampagne oder Ihres Canvas ab, und wählen Sie **Starten**. 

### Schritt 3: Erstellen Sie eine SessionM Werbe- oder Messaging-Kampagne

Als nächstes erstellen Sie Ihre Kampagne in SessionM.

![SessionM Kampagne erstellen.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Aktualisieren Sie die erweiterten Einstellungen in der SessionM Kampagne, um den folgenden JSON-Payload einzuschließen, der die `braze_campaign_id` oder `braze_canvas_id` enthält.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![Erweiterte Einstellungen von SessionM.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Erstellen Sie einen Trigger für Nachrichten nach dem gewünschten Zeitplan oder Verhalten. Wählen Sie dann im Menü **Externe Nachrichten** als **Messaging-Variante** **Braze** aus, um das Template zu verwenden.

![SessionM externe Nachricht.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

Dieses Template zieht die relevanten statischen und dynamischen Attribute und ruft den Braze Endpunkt auf.

![SessionM Braze Template.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}
