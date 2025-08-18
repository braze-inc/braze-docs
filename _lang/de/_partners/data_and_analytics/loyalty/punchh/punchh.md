---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Punchh, einer Plattform für Kundenbindung und Engagement, die es Ihnen ermöglicht, Daten zwischen den beiden Plattformen zu synchronisieren. In Braze veröffentlichte Daten stehen für die Segmentierung zur Verfügung und können über in Braze eingerichtete Webhook-Templates mit Nutzerdaten in Punchh synchronisiert werden."
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/) ist eine branchenführende Plattform für Kundenbindung und Engagement, die es Marken ermöglicht, Omnichannel-Kundenbindungs-Programme sowohl im Shop als auch digital anzubieten. 

_Diese Integration wird von Punchh gepflegt._

## Über die Integration

Die Integration von Braze und Punchh erlaubt es Ihnen, Daten für Geschenk- und Treuezwecke über die beiden Plattformen hinweg zu synchronisieren. In Braze veröffentlichte Daten stehen für die Segmentierung zur Verfügung und können Nutzerdaten über Braze-to-Braze-Webhooks zurück in Punchh synchronisieren.

## Was sind die Vorteile?

- Nehmen Sie Loyalitätsdaten von Punchh in Realtime in Braze auf. 
- Nutzen Sie leistungsstarke Daten der Zielgruppe von Braze, um aussagekräftige und dynamische kanalübergreifende Erlebnisse (App, Handy, Web, E-Mail und SMS) zugestellt zu bekommen.
  - Haben die Kund:in ihre E-Mails geöffnet? Haben die Kund:innen die App in der Nähe eines Shops geöffnet?
- Standardisieren Sie das Erscheinungsbild von Transaktions-E-Mails, die über Braze versendet werden.
- Erstellen Sie Journeys, die A/B-Tests und eine Optimierung im laufenden Betrieb zulassen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Kasperlekonto | Sie benötigen ein aktives Punchh-Konto, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Was sollte ich sonst noch wissen?

#### Vor der Integration

- Wenn Sie die Integration von Braze nutzen, sind zwei Kampagnen erforderlich, eine in Punchh und die zweite in Braze. Wenn Sie beispielsweise eine Kampagne mit einem Angebot versenden, wird die Geschenkkampagne in Punchh konfiguriert, und die Benachrichtigung kann von Braze aus gesendet werden.
- Gäste sollten bereits in Punchh und Braze vorhanden sein. Punchh filtert alle Kund:in heraus, die nicht bereits ein treuer Gast sind.

#### Wichtige Dinge zu beachten

- Punchh hat die Möglichkeit hinzugefügt, das Senden von Standard Nutzer:in-Attributen an Braze zu deaktivieren, so dass dem Kunden keine Mehrkosten für Datenpunkte entstehen. Dies wird bei der Einrichtung des Adapters konfiguriert.
- Wenn Sie angepasste Segmente für wiederkehrende Kampagnen verwenden, muss der Name der Kampagne anstelle der ID der Kampagne verwendet werden, da sich die IDs bei jeder Kampagne ändern.
- Zu den Kommunikationskanälen, die innerhalb jeder Kampagne von Punchh gifting zur Verfügung stehen, gehören Nachrichten, Push-Benachrichtigungen, SMS und E-Mail.
- Nachdem Nutzer:innen von Braze an ein angepasstes Segment von Punchh gesendet wurden, können sie nicht mehr entfernt werden. Einem bestehenden angepassten Segment können nur neue Gäste hinzugefügt werden. Wenn Gäste aus einem bestehenden angepassten Segment von Punchh entfernt werden sollen, muss in Braze eine neue Webhook-Kampagne erstellt werden, um Nutzer:innen an ein neues angepasstes Segment von Punchh zu senden.

## Integration

Punchh bietet verschiedene Endpunkte an, die Braze Kund:in zur Verfügung stehen, um der Punchh Plattform externe IDs hinzuzufügen. Verwenden Sie dazu die folgenden Punchh API Endpunkte. Nachdem Sie die externen IDs hinzugefügt haben, erstellen Sie einen Adapter in Punchh, geben Ihre Zugangsdaten für Braze an und wählen die Ereignisse aus, die Sie synchronisieren möchten. Als Nächstes können Sie die Segment ID von Punchh verwenden, um einen Punchh Webhook zu erstellen, der die Synchronisierung von Kunden in einer Canvas Journey triggert.

Beachten Sie, dass die Punchh `user_id` und Braze `external_id` in beiden Plattformen verfügbar sein müssen, damit die Integration korrekt synchronisiert werden kann. 
- Ereignisse, die von Punchh an Braze gesendet werden, enthalten als Bezeichner den Braze `external_id`. Wenn Punchh so konfiguriert ist, dass es die `external_source_id` verwendet, wird dieser Wert als Braze `external_id` eingestellt. Andernfalls wird bei der Integration standardmäßig die Punchh `user_id` als Braze `external_id` eingestellt.
- Um Webhooks von Braze an Punchh zu senden, muss die Punchh `user_id` im Nutzerprofil von Braze:innen verfügbar sein. Wenn Punchh `user_id` nicht als Braze `external_id` verwendet wird, sollte es als angepasstes Attribut "punchh_user_id" festgelegt werden. 

### Schritt 1: Einrichten von externen ID-Ingestion Endpunkten (optional)

Externe IDs von Braze können über die folgenden Endpunkte für neue und bestehende Nutzer:innen von Punchh hinzugefügt werden.

{% alert important %}
Die Werte in den Feldern `external_source` und `external_source_id` müssen eindeutig für Punchh sein und dürfen nicht mit bestehenden Profilen verknüpft sein.
{% endalert %}

1. Neue Nutzer:innen von Punchh<br>
Erstellen Sie neue Nutzer:innen in Punchh mit einem Punchh Endpunkt für die Registrierung unter Verwendung der Felder `external_source` und `external_source_id`. Punchh erlaubt die Übermittlung von externen Bezeichnern mit einem Nutzerprofil über einen der folgenden Endpunkte für die Registrierung:
- [Mobile Signup API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO-Anmelde-API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Bestehende Nutzer:innen von Punchh <br>
Update `external_source_id` für bestehende Nutzer:innen von Punchh. Punchh erlaubt das Hinzufügen von externen Bezeichnern zu einem Profil über einen Nutzer:innen API Update Endpunkt: 
- [Mobile Nutzer:innen Update](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO Nutzer:innen Update](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Dashboard Nutzer:innen Update](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab API-Beispiel für die Registrierung von Nutzer:innen %}
Dieses Beispiel ermöglicht es Ihnen, bei der Registrierung externe Bezeichner mit einem Nutzerprofil zu senden. Dies geschieht, indem Sie `external_source` als "customer_id" und `external_source_id` als "111111111111111111" als String-Datentyp senden.

```json
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab Nutzer:innen Update API Beispiel %}
Dieses Beispiel ermöglicht es Ihnen, externe Bezeichner mit einem Nutzerprofil zu aktualisieren. Dies geschieht, indem Sie `external_source` als "customer_id" und `external_source_id` als "111111111111111111" als String-Datentyp senden.

```json
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**Plattform-Konfiguration:** Um externe Bezeichner in Punchh zu aktivieren, navigieren Sie vom Punchh Dashboard aus zu **Cockpit** > **Dashboard** > **Externe Nutzer:innen Bezeichner**.
{% endalert %}

### Schritt 2: Einrichtung des Lötadapters in Punchh

#### Verfügbare zu synchronisierende Ereignisse {#available-events-to-sync}

1. **Gast:** Ausgelöst bei jeder Anmeldung, jedem Update des Gastprofils, bei Deaktivierung oder Löschung
2. **Loyalitäts-Check-in:** Ausgelöst bei Treuetransaktionen oder durch Scannen des Barcodes auf dem Kassenbon
3. **Geschenk Check-in:** Ausgelöst durch Punkte, die aus einer Kampagne stammen
4. **Erlösung:** Ausgelöst im Falle einer Einlösung von Prämien mit Ausnahme von Punchh-Coupons, da diese separat als Coupon-Ereignisse gesendet werden, einschließlich der Ausgabe und der Einlösung.
5. **Rewards:** Ausgelöst durch geschenkte Rewards aus Kampagnen, Aktivität, Konversion von Punkten in Rewards oder Admin-Geschenke
6. **Benachrichtigungen über Transaktionen:** Ausgelöst bei Transaktionsaktivitäten eines Nutzers:in innerhalb des Punchh-Systems (z.B. Punkteverfall)
7. **Marketing-Benachrichtigungen:** Ausgelöst auf der Grundlage verschiedener Kampagnen-Setups in Punchh für ein zugehöriges Segment von Nutzer:innen

{% alert note %}
Referenzieren Sie die Dokumentation von Punchh, wie Beispiel-Nutzdaten für diese verfügbaren Ereignisse aussehen können.
{% endalert %}

Arbeiten Sie mit Ihrem Punchh Implementation Manager zusammen, um diesen Adapter einzurichten.

Um die Integration von Braze und Punchh einzurichten, gehen Sie wie folgt vor:

1. Navigieren Sie im Punchh Dashboard zu **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** und schalten Sie auf **Enable Webhook Management** um.<br><br>
2. Als nächstes aktivieren Sie die Adapter, indem Sie zu **Einstellungen** > **Webhooks Manager** > **Konfigurationen** > **Tab Adapter anzeigen** navigieren und den **Tab Adapter anzeigen** umschalten.<br><br>
3. Navigieren Sie zu **Webhooks Manager:** in der Registerkarte **Einstellungen**, wählen Sie die Registerkarte **Adapter** und klicken Sie auf **Adapter erstellen**. <br><br>![]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Geben Sie den Namen des Adapters, die Beschreibung und die E-Mail des Administrators ein. Wählen Sie **Braze** als Ihren Adapter aus und geben Sie Ihren REST API-Endpunkt und Ihren REST-API-Schlüssel von Braze an.<br><br>
5. Wählen Sie dann die verfügbaren Ereignisse aus, die Sie aktivieren möchten. Eine Liste dieser Ereignisse finden Sie unter [Zu synchronisierende Ereignisse](#available-events-to-sync).<br><br>![]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Klicken Sie auf **Senden**, um den Webhook zu aktivieren.

## Punchh-Webhook in Braze erstellen

Braze kann Nutzer:innen über Webhooks zu einem Punchh Segment hinzufügen, indem es Punchh Custom Segmente verwendet.

1. Erstellen Sie ein angepasstes Segment in Punchh und beachten Sie die `custom_segment_id` in der URL des Punchh-Segment-Dashboards, wie unten gezeigt. Es können sowohl klassische als auch Beta-Segmente verwendet werden. Es wird jedoch empfohlen, die Beta-Version zu verwenden, da die Classic-Version irgendwann veraltet sein wird.<br><br>Navigieren Sie in der Punchh-Plattform zu **Gast** > **Segmente** > **Angepasste Liste** > **Neue angepasste Liste**.<br><br>![]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Erstellen Sie eine Webhook-Kampagne in Braze, indem Sie den Endpunkt Punchh verwenden, um einen Nutzer:innen einem angepassten Segment als Webhook-URL hinzuzufügen. Hier können Sie die `custom_segment_id` aus der URL und `user_id` als Schlüssel-Wert-Paare angeben.<br><br>![]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Dieser Webhook kann als singuläre Kampagne oder als Schritt innerhalb eines Canvas eingerichtet werden. Wenn der Webhook, der Nutzer:innen zu diesem speziellen Punchh-Segment hinzufügt, in mehreren Kampagnen oder Canvase verwendet werden soll, kann er alternativ als [Template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template) eingerichtet werden.<br><br>
Der Schlüssel `user_id` innerhalb des Webhooks bildet die Nutzer:innen ID von Punchh ab. Dieser Bezeichner muss zu allen in Braze erstellten Webhooks hinzugefügt werden, um Nutzer:innen einem angepassten Segment von Punchh hinzuzufügen. Das angepasste Attribut `punch_user_id` kann mit Hilfe von [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables) dynamisch als Wert für den Schlüssel `user_id` eingefügt werden. Sie können die angepasste Attribut-Variable `punchh_user_id` einfügen, indem Sie das blaue "Plus"-Symbol oben rechts in jedem Textfeld des Templates verwenden.<br><br>![]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Nachdem der Webhook gespeichert wurde, kann er zur Synchronisierung von Nutzer:innen verwendet werden, wie unten gezeigt. Wenn diese Braze-Webhook-Kampagne eingeführt wird, werden zum Beispiel 136 Gäste dem angepassten Segment Punch hinzugefügt.<br><br>![Ein Beispiel für die Synchronisierung von Nutzer:innen mit dem gespeicherten Webhook aufgrund der Integration von Braze und Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Weitere Informationen darüber, wie Webhooks bei Braze verwendet werden, finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 

## Anwendungsfälle Kampagnen

### Kampagne und Canvas-Konfiguration

#### Triggern

Anwendungsfälle für Messaging von Braze, die durch an Braze gesendete Punchh-Ereignisse ausgelöst werden, wie z.B. Rewards-Ereignisse oder Gäste-Ereignisse, können als [aktionsbasierte Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) oder Canvase erstellt werden, die durch das entsprechende Punchh-Ereignis getriggert werden.

Wenn Sie einen Trigger hinzufügen, wird die Liste der in Braze erstellten Ereignisse angezeigt. Wählen Sie das Ereignis, das Ihre Kampagne oder das Canvas triggern soll, das an den Nutzer:in gesendet werden soll, der das Ereignis protokolliert hat.

![]({% image_buster /assets/img/punchh/update5.png %})

Sie können Eigenschaftsfilter hinzufügen, um das auslösende Ereignis weiter zu filtern. Beispielsweise soll die Nachricht nur dann ausgelöst werden, wenn ein Kund:in das Ereignis "checkins_gift" triggert, bei dem die Eigenschaft "approved event" `true` lautet. Dies ist ein optionales Feature, das möglicherweise nicht auf alle Anwendungsfälle anwendbar ist. 

#### Segmentierung

In vielen Fällen können Braze Kampagnen und Canvase, die durch Punchh-Ereignisse ausgelöst werden, auf die Zielgruppe "Alle Benutzer" eingestellt werden, da die Segmentierung der Nutzer:innen, die diese Ereignisse triggern, in Punchh festgelegt wird. Kunden, die jedoch die Zielgruppe der Benutzer, die die durch das Ereignis ausgelösten Nachrichten von Braze erhalten, weiter verfeinern möchten, können dies tun, indem sie zusätzliche Filter und Segmente im Abschnitt **Zielgruppen** des Kampagnen-Composers oder der **Eingangszielgruppe** des Canvas-Composers hinzufügen. 

### Anwendungsfälle

{% tabs local %}
{% tab Anmeldung %}
#### Kampagne zur Registrierung

Wenn Sie die Braze-Konfiguration für eine Registrierungs-Kampagne mit angehängtem Angebot verwenden, müssen Sie in Punchh eine Geschenkkampagne für die Registrierung und in Braze eine Willkommensnachricht konfigurieren. 

Punchh empfiehlt, der Kampagne für die Registrierung eine Ausführungsverzögerung hinzuzufügen, damit Braze die Willkommensnachricht erst auf der Grundlage des Gastereignisses triggern kann. Wenn Sie dem Nutzer:innen eine Nachricht schicken möchten, in der er darüber informiert wird, dass er ein Geschenk erhalten hat, können Sie dies auf der Grundlage des Belohnungsereignisses triggern.

Im Falle einer Kampagne zur Registrierung können alle angemeldeten Personen für das Segment verwendet werden; daher ist ein angepasstes Segment von Braze nicht erforderlich.

Punchh-Konfigurationen erforderlich:
- Kampagne: Registrierung 
- Segmente: Alle haben sich registriert
- Reward: Kund:in wählen
Erforderliche Ereignisse:
- Rewards Ereignis
- Gastveranstaltung
Überlegungen:
- Ausführungsverzögerung. Wir empfehlen, dass der Gast eine 5-10-minütige Verzögerung hinzufügt.

![In Punch wird ein Segment für Nutzer:innen eingerichtet, die sich für ein Kundenbindungs-Programm anmelden. Danach wird das Gast-Ereignis, falls ausgelöst, und die Messaging-Kampagne von Braze ausgelöst. Als nächstes wird nach 10 Minuten die Punchh-Kampagne zur Registrierung ausgelöst, die das Reward-Ereignis und eine optionale Nachricht auslöst.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze willkommen %}
#### Braze Willkommenskampagne

Wenn sich ein neuer Nutzer:innen anmeldet, sendet Punchh an Braze ein Guest Event, das den Nutzer:innen anlegt und ein angepasstes Attribut `signup_channel` sendet, mit dem Sie die Willkommenskampagne von Braze triggern können.

Um die Braze Willkommenskampagne einzurichten, gehen Sie folgendermaßen vor:

1. Erstellen Sie in Braze eine aktionsbasierte Kampagne.
2. Für den Auslöser wählen Sie **Angepassten Attributwert ändern** und setzen das angepasste Attribut `signup_channel` auf **Beliebiger neuer Wert**.
3. Fahren Sie mit der Erstellung Ihrer Kampagne fort und senden Sie sie ab, wenn Sie fertig sind!

{% endtab %}
{% tab Massenangebot %}
#### Kampagne für Massenangebote

Wenn Sie eine Massenangebot-Kampagne für Geschenke verwenden, müssen Sie eine Massenangebot-Kampagne in Punchh und eine Messaging-Kampagne in Braze konfigurieren.

Wenn Sie ein Segment von Braze für Ihre Kampagne verwenden oder vor dem Verschenken von Gästen auf der Punchh-Plattform eine Mitteilung von Braze senden möchten, dann ist ein [angepasstes Punchh-Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) für die Punchh-Geschenkkampagne erforderlich. 

Die Erstellung eines Segments von Nutzer:innen, die dieses Angebot erhalten sollen, ist in Braze nur dann empfehlenswert, wenn Sie Attribute verwenden, die in Punchh nicht verfügbar sind. Andernfalls kann die Segmentierung von Punchh verwendet werden, und die Messaging-Kampagne von Braze wird als aktionsbasierte Kampagne erstellt, die durch die Nutzer:innen ausgelöst wird, die ihre Belohnung erhalten (das von Punchh ausgelöste Belohnungsereignis).

Punchh-Konfigurationen erforderlich:
- Kampagne: Massenangebot
- Segmente: Angepasste Liste oder Wahl der Kund:in
- Reward: Kund:in wählen

**Mit Punchh für Segmentierung und Geschenke und Braze für Messaging:**<br>
Ein Beispiel: Eine $2-Rabattprämie wird an ein innerhalb von Punchh konfigurierbares Segment gesendet, wobei das Messaging über Braze erfolgt.<br>
![In Punchh kann ein Segment von Nutzern:innen konfiguriert werden, die über eine Kampagne mit Massenangeboten von Punchh ein Geschenk erhalten. Als Nächstes wird ein Reward-Ereignis ausgelöst, und dann wird die Messaging-Kampagne von Braze ausgelöst.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Mit Braze Segmentierung und Messaging, und Punchh für Geschenke:**<br>
Zum Beispiel eine $2 Rabatt-Belohnung und Messaging an ein Segment mit Attributen, die in Punchh nicht verfügbar sind.<br>
![In Braze kann ein Nutzer:innen-Segment konfiguriert werden, und dann kann eine Nachricht von einem Braze-zu-Braze-Segment gesendet werden. Anschließend werden die Nutzer:innen über einen Braze-to-Braze-Webhook mit Segment- und Nutzer:innen-ID an das angepasste Segment von Punchh gesendet. Danach erhält der Nutzer:innen ein Geschenk durch eine Punchh Massenangebot Kampagne mit einem angepassten Segment. Danach wird das Reward-Ereignis ausgelöst.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Verwenden Sie Braze Segmentierung und Punchh für Geschenke oder Messaging, oder beides:**<br>
Zum Beispiel wird eine $2 Rabatt-Belohnung an ein Segment gesendet, dessen Attribute in Punchh nicht verfügbar sind, aber es ist kein Messaging erforderlich, oder das Messaging kann über Punchh gesendet werden (beachten Sie, dass alle Gäste in Punchh vorhanden sein müssen).<br>
![Ein Benutzersegment kann in Braze konfiguriert werden, und die Nutzer:innen werden über einen Braze-Webhook mit Segment- und Benutzer-ID an das angepasste Segment von Punchh gesendet. Danach erhält der Nutzer:innen ein Geschenk durch eine Punchh Massenangebot Kampagne mit einem angepassten Segment. Danach wird das Reward-Ereignis ausgelöst.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Wiederkehrendes Massenangebot %}
#### Wiederkehrende Kampagne für Massenangebote

Wenn Sie eine wiederkehrende Massenangebot-Kampagne für Geschenke verwenden, müssen Sie eine Massenangebot-Kampagne in Punchh konfigurieren und eine Messaging-Kampagne in Braze einrichten. Ein angepasstes Segment von Punchh ist erforderlich, wenn der Kund:in die Segmentierung von Braze einsteigen möchte (nur empfohlen, wenn Attribute verwendet werden, die in Punchh nicht verfügbar sind). Andernfalls kann die Segmentierung von Punchh verwendet werden, und die Messaging-Kampagne von Braze wird auf der Grundlage des Belohnungsereignisses getriggert.

Punchh-Konfigurationen erforderlich:
- Kampagne: Wiederkehrendes Massenangebot
- Segmente: Angepasste Liste oder Wahl der Kund:in
- Reward: Kund:in wählen
Überlegungen:
- IDs und Namen von Kampagnen werden als Event-Eigenschaften des Ereignisses an Braze gesendet. Wenn Sie in Braze einen Bezeichner für Punchh-Kampagnen verwenden möchten, um die Zielgruppe, die die Kampagne erhält, weiter zu filtern, muss der Kampagnenname verwendet werden, da sich die IDs der Kampagnen täglich ändern.

{% endtab %}
{% tab Post Check-in Angebot mit Benachrichtigung %}
#### Kampagne für Post-Check-in-Angebote mit Benachrichtigung

Wenn Sie eine Kampagne mit Post-Check-in-Angeboten nutzen, sendet Braze die Benachrichtigung über das Geschenk, und wenn der Gast eincheckt, erhält er ein Geschenk aus der Punchh Post-Check-in-Kampagne. Daher muss eine Angebotskampagne nach dem Einchecken in Punchh und eine Messaging-Kampagne in Braze konfiguriert werden (wenn die Kunden über die Kampagne informiert werden sollen).

Punchh-Konfigurationen erforderlich:
- Kampagne: Angebot nach dem Einchecken
- Segmente: Angepasste Liste
- Reward: Kund:in wählen

Eine E-Mail, in der Gäste darauf hingewiesen werden, dass sie an diesem Wochenende zu Besuch kommen sollen, um doppelte Punkte zu erhalten, gehört beispielsweise zu einem Segment mit Attributen, die in Punchh nicht verfügbar sind. Punchh schenkt diesem Segment Punkte nach einem qualifizierten Check-in und optionalem Messaging von Braze. 

![Ein Nutzer:innen-Segment wird in Braze konfiguriert, und Nachrichten werden von Braze nach einer Check-in-Kampagne gesendet. Als nächstes werden die qualifizierten Nutzer:innen über den Braze-to-Braze-Webhook mit Segment- und Nutzer:innen-ID an die angepasste Segmentierung von Punchh gesendet. Schließlich checkt der qualifizierte Nutzer:innen des angepassten Segments ein und erhält das Geschenk und die optionale Nachricht über die Post Check-in Kampagne]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Post Check-in Angebot ohne Benachrichtigung %}
#### Kampagne für Post-Check-in-Angebote ohne Benachrichtigung

Wenn Sie eine Post-Check-in-Angebotskampagne verwenden, bei der die Kunden nicht zuerst benachrichtigt werden, wird die Kampagne ein Geschenk machen (optionales Messaging) und eine Benachrichtigung innerhalb von Braze triggern. Daher muss eine Kampagne mit Post-Check-in-Angeboten in Punchh konfiguriert werden; eine angepasste Liste ist jedoch nicht erforderlich. Stattdessen können Sie das gewünschte Segment innerhalb von Punchh auswählen. 

Punchh-Konfigurationen erforderlich:
- Kampagne: Angebot nach dem Einchecken
- Segmente: Kund:in wählen
- Reward: Kund:in wählen

Zum Beispiel wird eine Kampagne für eine überraschende und erfreuliche Braze an ein Segment gesendet, das in Punchh verfügbar ist. Die Kampagne bedankt sich bei den Gästen für ihren Besuch und belohnt sie mit $2 Rabatt auf ihren nächsten Besuch.

![Innerhalb von Punchh kann ein Segment für qualifizierte Nutzer:innen konfiguriert werden. Ein qualifizierter Nutzer:innen checkt ein und erhält über eine Punchh-Kampagne nach dem Einchecken ein Geschenk. Danach wird ein Reward-Ereignis ausgelöst und die Rückrufnachricht gesendet, die die Gäste über die von Braze gesendete Belohnung informiert.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Jahrestag %}
#### Kampagne zum Jahrestag 

Wenn Sie eine Jubiläums-Kampagne nutzen, erhalten Nutzer:innen zunächst ein Geschenk zu ihrem Jubiläum aus der Kampagne Punchh. Dieses Geschenk (Rewards-Ereignis) triggert die Messaging-Kampagne innerhalb von Braze, die den Nutzer:innen über das Geschenk informiert. Eine angepasste Liste ist daher nicht erforderlich. Stattdessen können Sie die Segmente und die Jubiläumseinstellungen in Punchh auswählen.

Punchh-Konfigurationen erforderlich:
- Kampagne: Kampagne zum Jahrestag
- Segmente: Kund:in wählen
- Reward: Kund:in wählen
Überlegungen:
- Monat der Registrierung verschenken
- Gültigkeitsdauer (Wie lange ist die Geburtstagsbelohnung gültig?)
- Wiederkehrende Kampagnen, Zeitplan erforderlich 

![Ein optionales Segment kann innerhalb von Punchh erstellt werden, und ein qualifizierter Nutzer:innen erhält eine Belohnung durch eine Punchh-Jubiläumskampagne. Danach wird ein Reward-Ereignis ausgelöst und die Rückrufnachricht gesendet, die die Gäste über die von Braze gesendete Belohnung informiert.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Rückruf %}
#### Kampagne zur Rückrufaktion

Beim Targeting von Nutzer:innen auf der Basis von Inaktivität kann eine Rückrufkampagne verwendet werden. Der Kund:in kann die Segmente und Kampagnen innerhalb von Punchh erstellen, aber für das Messaging Braze verwenden.

Wenn Sie eine in Braze erstellte Segmentierung verwenden möchten, können Sie ein [angepasstes Punchh-Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) auf der Grundlage von Inaktivität an eine Kampagne mit wiederkehrenden Massenangeboten anhängen.

Punchh-Konfigurationen erforderlich:
- Kampagne: Kampagne zur Rückrufaktion
- Segmente: Kund:in wählen
- Reward: Kund:in wählen
Überlegungen:
- Kampagne läuft nach einem Zeitplan

![Ein optionales Segment kann innerhalb von Punchh erstellt werden, und ein qualifizierter Nutzer:innen erhält eine Belohnung durch eine Punchh-Rückrufkampagne. Danach wird ein Reward-Ereignis ausgelöst, und die Rückrufnachricht wird gesendet, um die Gäste über die von Braze gesendete Belohnung zu informieren.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


