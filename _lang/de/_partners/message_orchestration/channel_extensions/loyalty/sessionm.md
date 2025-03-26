--- 
nav_title: SessionM
article_title: SessionM
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und SessionM, einer Plattform für Kundenbindung und -loyalität."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# SessionM Treueplattform

> [SessionM](https://www.mastercardservices.com/en/capabilities/sessionm) ist eine Plattform für Kundenbindung und -loyalität, die Funktionen für das Kampagnenmanagement und Lösungen für das Loyalitätsmanagement bietet, um Marketingfachleuten dabei zu helfen, gezielte Kontakte zu knüpfen, um das Engagement und die Rentabilität zu steigern.

## Voraussetzungen

| Quelle | Anforderung | Beschreibung |
| --- | --- | --- |
| Löten | Ein Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `trigger_send` Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Löten | Ein Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für Ihre [Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| Braze und SessionM | Übereinstimmender Bezeichner | Um die Integration zu nutzen, stellen Sie sicher, dass sowohl SessionM als auch Braze einen Datensatz mit den von jeder Plattform verwendeten Kennungen haben. Verweise auf `user_id` entsprechen der Benutzerkennung von SessionM, die zum Zeitpunkt der Profilerstellung in SessionM erstellt wurde. |
| SessionM | Ein SessionM-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein SessionM-Konto. |
| SessionM | Ein SessionM Core REST Endpunkt | Ihr Endpunkt hängt von der SessionM URL Ihrer Instanz ab. Diese können Sie im SessionM Dashboard unter **Digitale Eigenschaften** erstellen. |
| SessionM | Ein SessionM Core REST API-Schlüssel | Der SessionM API-Schlüssel, der mit Ihrer Instanz und der Braze-Integration verbunden ist. Dieser Schlüssel kann für alle Core-basierten Anrufe einschließlich Tags verwendet werden. Diese können Sie im SessionM Dashboard unter **Digitale Eigenschaften** erstellen. |
| SessionM | Ein SessionM Core REST API Geheimnis | Das SessionM API-Geheimnis, das mit Ihrer Instanz und der Braze-Integration verbunden ist. Dieser Schlüssel kann für alle Core-basierten Anrufe einschließlich Tags verwendet werden. Diese können Sie im SessionM Dashboard unter **Digitale Eigenschaften** erstellen. |
| SessionM | Ein SessionM Connect REST-Endpunkt | Ihr Endpunkt hängt von der SessionM URL Ihrer Instanz ab. Bitte wenden Sie sich an Ihren technischen Kundenbetreuer bei SessionM oder an das Delivery-Team. |
| SessionM | Eine SessionM Connect REST-Autorisierungszeichenfolge | Die SessionM Connect Basic Authorization Zeichenfolge, die mit Ihrer Instanz verknüpft ist. Diese Authentifizierungszeichenfolge kann für alle verbindungsbasierten Aufrufe einschließlich get_user_offers verwendet werden. Bitte wenden Sie sich an Ihren technischen Kundenbetreuer bei SessionM oder an das Delivery-Team. |
| SessionM | A SessionM Connect REST Händler-ID | Eine eindeutige Kennung für den Kunden, der mit Ihrer Instanz verbunden ist. Wenden Sie sich an Ihren technischen SessionM-Kundenbetreuer oder Ihr Delivery-Team. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %} 

## Anwendungsfälle

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten auf, wie Sie die Integration von SessionM und Braze nutzen können.

- Erstellen Sie eine Segmentierung, die Daten aus allen Kundenbindungs-, Kundenmanagement- und Messaging-Plattformen einbezieht.
- Nutzen Sie eine robuste Segmentierung, um bestimmte Benutzergruppen mit Angeboten und Aktionen anzusprechen.
- Nutzen Sie die aktuellsten Benutzer-, Angebots- und Treueinformationen, wenn Sie Nachrichten versenden.
- Informieren Sie Ihre Kunden ausführlich über den Fortschritt und den Abschluss von Werbe- und Treueaktionen.
- Benachrichtigen Sie Kunden, wenn es ein neues Angebot gibt, und geben Sie die Details des Angebots bekannt.

## Integration von SessionM mit Braze

### Schritt 1: Ein Segment in Braze erstellen

Erstellen Sie in Braze ein Nutzersegment, das Sie mit SessionM-Promotions und Angeboten ansprechen können. 

![Segment Builder mit dem ausgewählten Filter "Benutzerdefinierte Attribute".]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Schritt 2: Importieren Sie Braze-Segmente in SessionM

#### Option 1: Export zum SessionM Tag Endpunkt (empfohlen)

Erstellen Sie zunächst eine Webhook-Kampagne in Braze und setzen Sie die Webhook-URL auf {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Verwenden Sie Liquid, um die `user_id` innerhalb der URL zu definieren. 

Verwenden Sie einen **Rohtext-Anfragetext**, um die gewünschten Tags, die dem Benutzerprofil in SessionM hinzugefügt werden sollen, und die gewünschte Zeitspanne, die noch verbleibt, in den Webhook-Text einzubauen. Ein Beispiel ist:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

Auf der Registerkarte **Einstellungen** fügen Sie die Schlüssel-Wert-Paare für jedes Anfrage-Header-Feld hinzu:
    \- Erstellen Sie einen Schlüssel `Content-Type` mit einem entsprechenden Wert `application/json`
    \- Erstellen Sie einen Schlüssel `Authorization` mit einem entsprechenden Wert `Basic YOUR-ENCODED-STRING-KEY`. Wenden Sie sich an Ihr SessionM-Team, um den kodierten String-Schlüssel für Ihren Endpunkt zu erhalten. 

![Webhook-Einstellungen.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Planen Sie Ihre Zustellung, stellen Sie Ihre **Zielgruppen** so ein, dass sie auf das [zuvor erstellte](#step-1-create-a-segment-in-braze) Segment abzielen, und starten Sie dann Ihre Kampagne.

{% alert important %}
Dieser Vorgang kann auch über einen API-Client wie Postman durchgeführt werden, indem Sie eine Anfrage direkt an den [SessionM Tag-Endpunkt](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) stellen und dabei den Kunden, den Tag-Namen und eine Zeitspanne für jeden Benutzer im Anruf angeben (ein Benutzer pro Anruf).
<br><br>
Die folgende Beispielabfrage verwendet cURL. 

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

Exportieren Sie Ihr Braze-Segment mit Hilfe des Braze-Segmentierers und stellen Sie SessionM eine CSV-Datei zur Verfügung, die die zu taggenden Kunden, den Tag-Namen und eine Zeitspanne für jeden Benutzer in der Datei enthält.

## Abrufen von Echtzeit-Angebotsbriefen mit Braze

Die Integration von SessionM mit Braze ermöglicht das Abrufen von SessionM-Benutzerdaten in Echtzeit zum Zeitpunkt des Nachrichtenversands unter Verwendung von Connected Content, um das Risiko auszuschalten, dass veraltete, abgelaufene oder bereits eingelöste Treueangebote an Kunden kommuniziert werden. 

Das folgende Beispiel zeigt, wie Connected Content verwendet wird, um Daten aus der Brieftasche in eine Nachricht einzufügen. Connected Content kann jedoch mit jedem der Connect-Endpunkte von SessionM verwendet werden. 

### Schritt 1: Angebot in SessionM ausgeben

SessionM erstellt Angebote für Kunden aus verschiedenen internen Hebeln, die konfiguriert werden können. Nach der Ausgabe werden die Angebote in einen Zustand versetzt, den SessionM als "Angebotsmappe" bezeichnet.

Ein Kunde muss die erforderliche Aktion durchführen oder die Zielvorgabe erfüllen und erhält das Angebot innerhalb von SessionM.

SessionM fügt das Angebot dann der Brieftasche des Kunden im Status "Ausgestellt" hinzu.

### Schritt 2: SessionM Offer Wallet API aufrufen

In der Kampagne oder im Canvas-Schritt mit den SessionM-Angeboten verwenden Sie [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/), um einen API-Aufruf an den [SessionM `get_user_offers` Endpunkt](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/) zu tätigen.

In der Anfrage für Connected Content geben Sie die SessionM `user_id` des Benutzers und Ihre `retailer_id` an, um die vollständige Liste der aktiven Angebote abzurufen, die der Kunde in seiner Brieftasche hat. Jede Anfrage an diesen Endpunkt kann einen einzelnen Benutzer enthalten. Wenden Sie sich an das SessionM-Team, um den kodierten String-Schlüssel für den grundlegenden Autorisierungs-Header in Ihrem Connected Content-Aufruf zu erhalten.

Im Anfragekörper ist `culture` standardmäßig auf `en-US` voreingestellt, aber Sie können Liquid verwenden, um die Sprache eines Benutzers für mehrsprachige SessionM-Angebote vorzugeben (z. B. durch Verwendung von {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

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

### Schritt 3: Angebotsportemonnaie für Braze-Nachrichten befüllen

Nachdem eine Anfrage an den Endpunkt gestellt wurde, gibt SessionM die vollständige Liste der Angebote im Ausgabestatus zurück, zusammen mit den vollständigen Details für jedes Angebot. Dies ist ein Beispiel für eine zurückgegebene Antwort:

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

Unter Verwendung der Liquid-Dot-Notation kann dies in die Nachricht eingefügt werden. Um die Nachricht mit dem Ergebnis `offer_id` zu personalisieren, könnten Sie zum Beispiel die Rückgabe-Nutzlast nutzen, indem Sie {% raw %}`{{wallet.payload.available_points}`{% endraw %} verwenden, die `100` zurückgibt.

{% alert note %}
Dies ist eine individuelle API. Wenn Sie beabsichtigen, einen Stapel von mehr als 500 Nutzern zu versenden, wenden Sie sich an Ihr SessionM-Kundenteam, um sich zu erkundigen, wie Sie Massendaten in die Integration einbeziehen können.
{% endalert %}

## Ausgelöste Benachrichtigungen einrichten

Durch die Integration von SessionM und Braze können Benutzerprofildaten, Angebotsdetails und Punktesalden dynamisch in die Nachrichten eingefügt und in Echtzeit an den Kunden am Ort der Aktion gesendet werden.

### Schritt 1: SessionM Delivery Team konfiguriert Vorlagen

Arbeiten Sie mit Ihrem SessionM Delivery Team zusammen, um Vorlagen für Ihre ausgelösten Nachrichten zu entwickeln. SessionM fügt Benutzerprofildaten, Angebotsdetails und Punktesalden in die Nachrichten ein und löst sie in Braze für Echtzeit-Kundenmitteilungen aus.

Zu den Standardfeldern, die in allen Vorlagen von SessionM enthalten sind, gehören:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
Wenn Sie `broadcast flag` auf `true` setzen, wird die Nachricht an das gesamte Segment gesendet, auf das die Kampagne oder das Canvas in Braze abzielt.
{% endalert %}

Zusätzliche Felder können je nach Bedarf konfiguriert werden:

- **Daten anbieten:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Daten zur Punktevergabe:** `point award amount`, `point account name`
- **Daten zum Ereignisauslöser:** Alle Daten im Trigger-Ereignis, die das Ergebnis des Trigger/Send-Webhook nutzen
- **Kampagnenspezifische Daten:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Zusätzliche Felder werden als `trigger_properties` an Braze gesendet, um die Nachricht zu personalisieren. 

### Schritt 2: Erstellen Sie eine Braze-Kampagne oder ein Canvas

Erstellen Sie in Braze eine API-ausgelöste Kampagne oder ein Canvas, das von SessionM ausgelöst wird. Wenn zusätzliche Felder konfiguriert wurden, wie z. B. `offer_id` oder `offer title`, verwenden Sie Liquid (z. B. {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}), um die personalisierten Felder in Ihre Nachrichten aufzunehmen.

![API-Auslösereigenschaften.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

Notieren Sie sich auf der Registerkarte **Zustellungszeitplan** die Kampagnen- oder Canvas-ID, da diese den **erweiterten Einstellungen der** SessionM-Kampagne hinzugefügt wird.

![API-gesteuerte Kampagne.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Schließen Sie die Details Ihrer Kampagne oder Ihres Canvas ab, und wählen Sie **Starten**. 

### Schritt 3: Erstellen Sie eine SessionM Werbe- oder Messaging-Kampagne

Als nächstes erstellen Sie Ihre Kampagne in SessionM.

![Erstellung einer SessionM-Kampagne.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Aktualisieren Sie die erweiterten Einstellungen in der SessionM-Kampagne, um die folgende JSON-Nutzlast einzuschließen, die die `braze_campaign_id` oder `braze_canvas_id` enthält.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![Erweiterte Einstellungen von SessionM.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Erstellen Sie einen Nachrichtenauslöser für den gewünschten Zeitplan oder das gewünschte Verhalten. Wählen Sie dann im Menü **Externe Nachricht** als **Nachrichtenvariante** **Braze Messaging Variante**, um die Vorlage zu verwenden.

![SessionM externe Nachricht.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

Diese Vorlage zieht die relevanten statischen und dynamischen Attribute und ruft den Braze-Endpunkt auf.

![SessionM Braze Vorlage.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}
