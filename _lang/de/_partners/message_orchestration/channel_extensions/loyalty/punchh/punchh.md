---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Punchh, einer Plattform für Kundenbindung und Engagement, die es Ihnen ermöglicht, Daten zwischen den beiden Plattformen zu synchronisieren. In Braze veröffentlichte Daten stehen für die Segmentierung zur Verfügung und können über in Braze eingerichtete Webhook-Vorlagen mit Punchh synchronisiert werden."
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/) ist eine branchenführende Treue- und Engagement-Plattform, die es Marken ermöglicht, Omnichannel-Kundenbindungsprogramme sowohl in Geschäften als auch digital anzubieten. 

Die Integration von Braze und Punchh ermöglicht es Ihnen, Daten für Geschenk- und Treuezwecke zwischen den beiden Plattformen zu synchronisieren. Die in Braze veröffentlichten Daten stehen für die Segmentierung zur Verfügung und können über Braze-Webhooks zurück in Punchh synchronisiert werden.

## Was sind die Vorteile?

- Übertragen Sie Kundenbindungsdaten in Echtzeit von Punchh zu Braze. 
- Nutzen Sie die leistungsstarken Publikumsdaten von Braze, um aussagekräftige und dynamische kanalübergreifende Erlebnisse zu liefern (App, Mobile, Web, E-Mail und SMS).
  - Haben Kunden E-Mails geöffnet? Haben Kunden die App in der Nähe eines Geschäfts geöffnet?
- Standardisieren Sie das Erscheinungsbild von Transaktions-E-Mails, die über Braze versendet werden.
- Erstellen Sie Journeys, die A/B-Tests und eine fortlaufende Optimierung ermöglichen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Kasperlekonto | Sie benötigen ein aktives Punchh-Konto, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][6]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Was sollte ich sonst noch wissen?

#### Vor der Integration

- Wenn Sie die Braze-Integration verwenden, sind zwei Kampagnen erforderlich, eine in Punchh und die zweite in Braze. Wenn Sie beispielsweise eine Kampagne mit einem Angebot versenden, wird die Geschenkaktion in Punchh konfiguriert, und die Benachrichtigung kann von Braze aus gesendet werden.
- Gäste sollten bereits in Punchh und Braze vorhanden sein. Punchh filtert jeden Kunden heraus, der nicht bereits ein treuer Gast ist.

#### Wichtige Dinge zu beachten

- Punchh hat die Möglichkeit hinzugefügt, das Senden von Standard-Benutzerattributen an Braze zu deaktivieren, so dass dem Kunden keine Überschüsse an Datenpunkten entstehen. Dies wird bei der Einrichtung des Adapters konfiguriert.
- Wenn Sie benutzerdefinierte Segmente für wiederkehrende Kampagnen verwenden, müssen Sie den Kampagnennamen anstelle der Kampagnen-ID verwenden, da sich die IDs bei jeder Ausführung der Kampagne ändern.
- Zu den Kommunikationskanälen, die innerhalb jeder Punchh-Geschenkaktion zur Verfügung stehen, gehören Rich Messages, Push-Benachrichtigungen, SMS und E-Mail.
- Nachdem Benutzer von Braze an ein benutzerdefiniertes Segment von Punchh gesendet wurden, können sie nicht mehr entfernt werden. Einem bestehenden benutzerdefinierten Segment können nur neue Gäste hinzugefügt werden. Wenn Gäste aus einem bestehenden benutzerdefinierten Punchh-Segment entfernt werden müssen, muss in Braze eine neue Webhook-Kampagne erstellt werden, um Benutzer an ein neues benutzerdefiniertes Punchh-Segment zu senden.

## Integration

Punchh bietet verschiedene Endpunkte, die Braze-Kunden zur Verfügung stehen, um externe IDs zur Punchh-Plattform hinzuzufügen. Verwenden Sie dazu die folgenden Punchh-API-Endpunkte. Nachdem Sie die externen IDs hinzugefügt haben, erstellen Sie einen Adapter in Punchh, geben Ihre Braze-Anmeldedaten an und wählen die Ereignisse aus, die Sie synchronisieren möchten. Als Nächstes können Sie die Punchh-Segment-ID verwenden, um einen Punchh-Webhook zu erstellen, der die Kundensynchronisierung in einer Canvas-Reise auslöst.

Beachten Sie, dass die Punchh `user_id` dem Braze-Benutzerprofil als benutzerdefiniertes Attribut "punchh_user_id" hinzugefügt werden muss, damit die Integration genutzt werden kann. In ähnlicher Weise muss die `external_id`, die in Braze verwendet wird, als `external_source_id` Feld in das Punchh Benutzerprofil aufgenommen werden. 

### Schritt 1: Externe ID-Ingestion-Endpunkte einrichten

Externe IDs von Braze können über die folgenden Endpunkte für neue und bestehende Punchh-Benutzer hinzugefügt werden.

{% alert important %}
Die Werte der Felder `external_source` und `external_source_id` müssen für Punchh eindeutig sein und dürfen nicht mit bestehenden Profilen verknüpft sein.
{% endalert %}

1. Neue Punchh-Benutzer<br>
Erstellen Sie neue Benutzer in Punchh mit einem Punchh-Anmeldeendpunkt unter Verwendung der Felder `external_source` und `external_source_id`. Punchh ermöglicht die Übermittlung von externen Identifikatoren mit einem Benutzerprofil über einen der folgenden Anmeldeendpunkte:
- [Mobile Anmeldungs-API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO-Anmelde-API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Bestehende Punchh-Benutzer <br>
Aktualisieren Sie `external_source_id` für bestehende Punchh-Benutzer. Punchh ermöglicht das Hinzufügen von externen Identifikatoren zu einem Profil über einen Benutzer-API-Aktualisierungsendpunkt: 
- [Update für mobile Benutzer](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO Benutzer Update](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Dashboard Benutzer Update](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab Beispiel für eine Benutzeranmelde-API %}
Mit diesem Beispiel können Sie bei der Anmeldung externe Identifikatoren mit einem Benutzerprofil senden. Dies geschieht, indem Sie `external_source` als "customer_id" und `external_source_id` als "111111111111111111" als String-Datentyp senden.

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
{% tab Beispiel einer Benutzeraktualisierungs-API %}
Mit diesem Beispiel können Sie externe Identifikatoren mit einem Benutzerprofil aktualisieren. Dies geschieht, indem Sie `external_source` als "customer_id" und `external_source_id` als "111111111111111111" als String-Datentyp senden.

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
**Plattform-Konfiguration:** Um externe Identifikatoren in Punchh zu aktivieren, navigieren Sie im Punchh-Dashboard zu **Cockpit** > **Dashboard** > **Externe Benutzeridentifikatoren**.
{% endalert %}

### Schritt 2: Einrichtung des Lötadapters in Punchh

#### Verfügbare zu synchronisierende Ereignisse {#available-events-to-sync}

1. **Gast:** Ausgelöst bei jeder Anmeldung, Aktualisierung des Gastprofils, Deaktivierung oder Löschung
2. **Loyalitäts-Check-in:** Ausgelöst für Treuetransaktionen oder Sammeln durch Scannen des Barcodes auf dem Kassenbon
3. **Geschenk Check-in:** Ausgelöst für geschenkte Punkte aus einer Kampagne
4. **Erlösung:** Ausgelöst im Falle einer Prämieneinlösung mit Ausnahme von Punchh-Coupons, da diese separat als Coupon-Ereignisse gesendet werden, einschließlich der Ausgabe und der Einlösung
5. **Belohnungen:** Ausgelöst durch Belohnungen, die im Rahmen von Kampagnen, Aktivitäten, der Umwandlung von Punkten in Belohnungen oder der Vergabe durch den Administrator vergeben werden.
6. **Transaktionsbenachrichtigungen:** Ausgelöst bei Transaktionsaktivitäten eines Benutzers innerhalb des Punchh-Systems (z. B. Verfall von Punkten)
7. **Marketing-Benachrichtigungen:** Ausgelöst auf der Grundlage verschiedener Kampagneneinstellungen in Punchh für ein bestimmtes Benutzersegment

{% alert note %}
Lesen Sie in der Punchh-Dokumentation nach, wie Beispiel-Nutzdaten für diese verfügbaren Ereignisse aussehen können.
{% endalert %}

Arbeiten Sie mit Ihrem Punchh Implementation Manager zusammen, um diesen Adapter einzurichten.

Um die Integration von Braze und Punchh einzurichten, gehen Sie wie folgt vor:

1. Navigieren Sie im Punchh Dashboard zu **Cockpit** > **Dashboard** > **Hauptfunktionen** > **Webhook-Verwaltung aktivieren** und schalten Sie die Option **Webhook-Verwaltung aktivieren** ein.<br><br>
2. Als nächstes aktivieren Sie Adapter, indem Sie zu **Einstellungen** > **Webhooks Manager** > **Konfigurationen** > **Registerkarte Adapter anzeigen** navigieren und die **Registerkarte Adapter anzeigen** aktivieren.<br><br>
3. Navigieren Sie zum **Webhooks Manager** auf der Registerkarte **Einstellungen**, wählen Sie die Registerkarte **Adapter** und klicken Sie auf **Adapter erstellen**. <br><br>![][1]<br><br>
4. Geben Sie den Namen des Adapters, die Beschreibung und die E-Mail-Adresse des Administrators ein. Wählen Sie **Braze** als Ihren Adapter und geben Sie Ihren Braze REST API Endpunkt und Ihren Braze API Schlüssel an.<br><br>
5. Wählen Sie dann die verfügbaren Ereignisse aus, die Sie aktivieren möchten. Eine Liste dieser Ereignisse finden Sie unter [Zu synchronisierende Ereignisse](#available-events-to-sync).<br><br>![][3]<br><br>
6. Klicken Sie auf **Senden**, um den Webhook zu aktivieren.

## Punchh Webhook in Braze erstellen

Braze kann Benutzer über Webhooks zu einem Punchh-Segment hinzufügen, das Punchh Custom Segments verwendet.

1. Erstellen Sie ein benutzerdefiniertes Segment in Punchh und beachten Sie die `custom_segment_id` in der URL des Punchh-Segment-Dashboards, wie unten gezeigt. Es können sowohl klassische als auch Beta-Segmentersteller verwendet werden. Es wird jedoch empfohlen, die Beta-Version zu verwenden, da die Classic-Version irgendwann veraltet sein wird.<br><br>Navigieren Sie auf der Punchh-Plattform zu **Gast** > **Segment** > **Benutzerdefinierte Liste** > **Neue benutzerdefinierte Liste**.<br><br>![][8]<br><br>

2. Erstellen Sie eine Webhook-Kampagne in Braze, indem Sie den Punchh-Endpunkt zum Hinzufügen eines Benutzers zu einem benutzerdefinierten Segment als Webhook-URL verwenden. Hier können Sie die `custom_segment_id` aus der URL und `user_id` als Schlüssel-Wert-Paare angeben.<br><br>![][4]<br><br>

3. Dieser Webhook kann als einzelne Kampagne oder als ein Schritt innerhalb eines Canvas eingerichtet werden. Wenn der Webhook, der Benutzer zu diesem speziellen Punchh-Segment hinzufügt, in mehreren Kampagnen oder Canvases verwendet werden soll, kann er alternativ als [Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template) eingerichtet werden.<br><br>
Der Schlüssel `user_id` innerhalb des Webhooks entspricht der Punchh-Benutzer-ID. Diese Kennung muss zu allen Webhooks hinzugefügt werden, die in Braze erstellt werden, um Benutzer zu einem benutzerdefinierten Segment von Punchh hinzuzufügen. Das benutzerdefinierte Attribut `punch_user_id` kann mit Hilfe von [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables) dynamisch als Wert für den Schlüssel `user_id` ausgefüllt werden. Sie können die benutzerdefinierte Attributvariable `punchh_user_id` einfügen, indem Sie das blaue "Plus"-Symbol oben rechts in jedem Textfeld mit Vorlage verwenden.<br><br>![][10]{: style="max-width:65%;"}<br><br>![][11]{: style="max-width:65%;"}<br><br>

4. Nachdem der Webhook gespeichert wurde, können Sie ihn zur Synchronisierung von Benutzern verwenden, wie unten gezeigt. Zum Beispiel würden 136 Gäste zum benutzerdefinierten Segment Punch hinzugefügt werden, wenn diese Braze Webhook-Kampagne gestartet wird.<br><br>![Ein Beispiel für die Synchronisierung von Benutzern mit dem gespeicherten Webhook dank der Integration von Braze und Punchh.][7]

Weitere Informationen darüber, wie Webhooks bei Braze verwendet werden, finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 

## Anwendungsfall Kampagnen

### Konfiguration von Kampagnen und Canvas

#### Auslöser

Anwendungsfälle für Braze-Nachrichten, die durch an Braze gesendete Punchh-Ereignisse ausgelöst werden, wie z. B. Belohnungsereignisse oder Gästeereignisse, können als [aktionsbasierte Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) oder Canvases erstellt werden, die durch das entsprechende Punchh-Ereignis ausgelöst werden.

Wenn Sie einen Auslöser hinzufügen, wird die Liste der in Braze erstellten Ereignisse angezeigt. Wählen Sie das Ereignis, das Ihre Kampagne auslösen soll, oder die Canvas, die an den Benutzer gesendet werden soll, der das Ereignis protokolliert hat.

![][12]

Es können Eigenschaftsfilter hinzugefügt werden, um das auslösende Ereignis weiter zu filtern. Zum Beispiel sollte die Nachricht nur ausgelöst werden, wenn ein Kunde das Ereignis "checkins_gift" auslöst, bei dem die Eigenschaft "approved" `true` lautet. Dies ist eine optionale Funktion, die möglicherweise nicht für alle Anwendungsfälle geeignet ist. 

#### Segmentierung

In vielen Fällen können Braze-Kampagnen und Canvases, die durch Punchh-Ereignisse ausgelöst werden, auf die Zielgruppe "Alle Benutzer" eingestellt werden, da die Segmentierung der Benutzer, die diese Ereignisse auslösen, in Punchh festgelegt wird. Kunden, die die Zielgruppe der Benutzer, die die durch das Ereignis ausgelöste Braze-Benachrichtigung erhalten, weiter verfeinern möchten, können dies tun, indem sie zusätzliche Filter und Segmente im Abschnitt **Zielgruppen** des Kampagnen-Composers oder der **Einstiegszielgruppe** des Canvas-Composers hinzufügen. 

### Anwendungsfälle

{% tabs local %}
{% tab Anmeldung %}
#### Anmeldungskampagne

Wenn Sie die Braze-Konfiguration für eine Anmeldekampagne mit angehängtem Angebot verwenden, müssen Sie in Punchh eine Geschenkkampagne für die Anmeldung und in Braze eine Willkommensnachricht konfigurieren. 

Punchh empfiehlt, der Anmeldekampagne eine Ausführungsverzögerung hinzuzufügen, damit Braze die Willkommensnachricht erst auf der Grundlage des Gastereignisses auslösen kann. Wenn Sie den Benutzer in einer Folgemeldung darüber informieren möchten, dass er ein Geschenk erhalten hat, können Sie dies auf der Grundlage des Belohnungsereignisses auslösen.

Im Falle einer Anmeldekampagne können alle Angemeldeten für das Segment verwendet werden; daher ist ein benutzerdefiniertes Braze-Segment nicht erforderlich.

Punchh-Konfigurationen erforderlich:
- Kampagne: Anmeldung 
- Segment: Alle haben sich angemeldet
- Belohnung: Wahl des Kunden
Erforderliche Ereignisse:
- Ereignis belohnen
- Gastveranstaltung
Überlegungen:
- Ausführungsverzögerung. Wir empfehlen, dass der Gast eine 5-10-minütige Verzögerung hinzufügt.

![Ein Benutzersegment wird in Punch konfiguriert, und die Gäste melden sich für ein Treueprogramm an. Danach wird das Gast-Ereignis, falls ausgelöst, und die Braze Messaging-Kampagne ausgelöst. Anschließend wird nach 10 Minuten die Punchh-Anmelde-Geschenkaktion ausgelöst, die das Belohnungsereignis und eine optionale Folgenachricht auslöst.]({% image_buster /assets/img/punchh/usecase3.png %})

{% endtab %}
{% tab Massenangebot %}
#### Massenangebot-Kampagne

Wenn Sie eine Massenangebotskampagne für Geschenke verwenden, müssen Sie in Punchh eine Massenangebotskampagne und in Braze eine Nachrichtenkampagne konfigurieren.

Wenn Sie ein Braze-Segment für Ihre Kampagne verwenden oder eine Kommunikation von Braze aus versenden möchten, bevor Sie Gäste auf der Punchh-Plattform beschenken, dann ist ein [benutzerdefiniertes Punchh-Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) für die Punchh-Geschenkkampagne erforderlich. 

Die Erstellung eines Segments von Benutzern, die dieses Angebot in Braze erhalten sollen, wird nur empfohlen, wenn Sie Attribute verwenden, die in Punchh nicht verfügbar sind. Andernfalls kann die Punchh-Segmentierung verwendet werden, und die Braze-Messaging-Kampagne wird als aktionsbasierte Kampagne erstellt, die durch den Erhalt der Belohnung ausgelöst wird (das von Punchh ausgelöste Belohnungsereignis).

Punchh-Konfigurationen erforderlich:
- Kampagne: Massenangebot
- Segment: Benutzerdefinierte Liste oder Kundenauswahl
- Belohnung: Wahl des Kunden

**Wir verwenden Punchh für die Segmentierung und die Vergabe von Geschenken und Braze für die Nachrichtenübermittlung:**<br>
Zum Beispiel wird eine $2-Rabattprämie an ein in Punchh konfigurierbares Segment gesendet, wobei die Benachrichtigung über Braze erfolgt.<br>
![Ein Benutzersegment kann in Punchh konfiguriert werden, und die Benutzer erhalten ein Geschenk über eine Punchh-Massenangebotskampagne. Als nächstes wird ein Belohnungsereignis ausgelöst, und dann wird die Braze-Messaging-Kampagne gestartet.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Verwenden Sie Braze zur Segmentierung und Nachrichtenübermittlung und Punchh zum Verschenken:**<br>
Zum Beispiel eine $2 Rabatt-Belohnung und eine Nachricht, die an ein Segment mit Attributen gesendet wird, die in Punchh nicht verfügbar sind.<br>
![Ein Benutzersegment kann in Braze konfiguriert werden, und dann kann eine Nachricht von einem Braze-zu-Braze-Segment gesendet werden. Anschließend werden die Benutzer über einen Braze-Webhook mit Segment und Benutzer-ID an das benutzerdefinierte Segment von Punchh gesendet. Danach erhält der Benutzer ein Geschenk über eine Punchh-Massenangebotskampagne mit einem benutzerdefinierten Segment. Danach wird das Belohnungsereignis ausgelöst.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Verwenden Sie Braze Segmentierung und Punchh für Geschenke oder Nachrichten oder beides:**<br>
Zum Beispiel wird eine $2-Rabattprämie an ein Segment mit Attributen gesendet, die nicht in Punchh verfügbar sind, aber es ist keine Benachrichtigung erforderlich, oder die Benachrichtigung kann über Punchh gesendet werden (beachten Sie, dass alle Gäste in Punchh anwesend sein müssen).<br>
![Ein Benutzersegment kann in Braze konfiguriert werden, und die Benutzer werden über einen Braze-Webhook mit Segment und Benutzer-ID an das benutzerdefinierte Segment von Punchh gesendet. Danach erhält der Benutzer ein Geschenk über eine Punchh-Massenangebotskampagne mit einem benutzerdefinierten Segment. Danach wird das Belohnungsereignis ausgelöst.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Wiederkehrendes Massenangebot %}
#### Wiederkehrende Massenangebotskampagne

Wenn Sie eine wiederkehrende Massenangebotskampagne für Geschenke verwenden, müssen Sie eine Massenangebotskampagne in Punchh konfigurieren und eine Nachrichtenkampagne in Braze einrichten. Ein benutzerdefiniertes Punchh-Segment ist erforderlich, wenn der Kunde die Braze-Segmentierung verwenden möchte (nur empfohlen, wenn Attribute verwendet werden, die in Punchh nicht verfügbar sind). Andernfalls kann die Punchh-Segmentierung verwendet werden, und die Braze-Nachrichtenkampagne wird auf der Grundlage des Belohnungsereignisses ausgelöst.

Punchh-Konfigurationen erforderlich:
- Kampagne: Wiederkehrendes Massenangebot
- Segment: Benutzerdefinierte Liste oder Kundenauswahl
- Belohnung: Wahl des Kunden
Überlegungen:
- Kampagnen-IDs und Kampagnennamen werden als Ereigniseigenschaft des Ereignisses an Braze gesendet. Wenn Sie in Braze eine Punchh-Kampagnenkennung verwenden möchten, um die Zielgruppe, die die Kampagne erhält, weiter zu filtern, muss der Kampagnenname verwendet werden, da sich die Kampagnen-IDs täglich ändern.

{% endtab %}
{% tab Post Check-in Angebot mit Benachrichtigung %}
#### Angebotskampagne mit Benachrichtigung nach dem Einchecken

Wenn Sie eine Post-Check-in-Angebotskampagne verwenden, sendet Braze die Benachrichtigung über das Geschenk, und wenn der Gast eincheckt, erhält er ein Geschenk aus der Punchh Post-Check-in-Kampagne. Daher müssen Sie eine Angebotskampagne nach dem Einchecken in Punchh und eine Nachrichtenkampagne in Braze konfigurieren (wenn Sie die Kunden über die Kampagne benachrichtigen).

Punchh-Konfigurationen erforderlich:
- Kampagne: Angebot nach dem Einchecken
- Segment: Benutzerdefinierte Liste
- Belohnung: Wahl des Kunden

Ein Beispiel: Eine E-Mail, in der Gäste darauf hingewiesen werden, dass sie an diesem Wochenende doppelte Punkte für ein Segment mit Attributen erhalten, die in Punchh nicht verfügbar sind. Punchh vergibt für dieses Segment Punkte nach einem qualifizierten Check-in und einer optionalen Benachrichtigung von Braze. 

![Ein Benutzersegment wird in Braze konfiguriert, und Nachrichten werden von Braze nach der Check-in-Kampagne gesendet. Anschließend werden die qualifizierten Benutzer über einen Braze-Webhook mit Segment- und Benutzer-ID an das benutzerdefinierte Segment von Punchh gesendet. Schließlich checkt der qualifizierte Benutzer im benutzerdefinierten Segment ein und erhält das Geschenk und die optionale Nachricht über die Post-Check-in-Kampagne]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Post Check-in Angebot ohne Benachrichtigung %}
#### Post-Check-in-Angebotskampagne ohne Benachrichtigung

Wenn Sie eine Post-Check-in-Angebotskampagne verwenden, bei der die Kunden nicht zuerst benachrichtigt werden, wird die Kampagne ein Geschenk machen (optionale Nachrichten) und eine Benachrichtigung in Braze auslösen. Daher muss eine Post-Check-in-Angebotskampagne in Punchh konfiguriert werden; eine benutzerdefinierte Liste ist jedoch nicht erforderlich. Stattdessen können Sie das gewünschte Segment innerhalb von Punchh auswählen. 

Punchh-Konfigurationen erforderlich:
- Kampagne: Angebot nach dem Einchecken
- Segment: Wahl des Kunden
- Belohnung: Wahl des Kunden

Zum Beispiel wird eine "Surprise and Delight Braze"-Kampagne an ein Segment gesendet, das in Punchh verfügbar ist. Sie bedankt sich bei den Gästen für ihren Besuch und belohnt sie mit $2 Rabatt auf ihren nächsten Besuch.

![Ein qualifiziertes Benutzersegment kann in Punchh konfiguriert werden, und ein qualifizierter Benutzer checkt ein und erhält ein Geschenk durch eine Punchh-Kampagne nach dem Einchecken. Danach wird ein Belohnungsereignis ausgelöst und die Rückrufnachricht wird gesendet, um die Gäste über die von Braze gesendete Belohnung zu informieren.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Jahrestag %}
#### Kampagne zum Jahrestag 

Wenn Sie eine Jubiläums-Kampagne nutzen, erhält der Nutzer zunächst ein Geschenk für sein Jubiläum aus der Punchh-Kampagne. Dieses Geschenk (Belohnungsereignis) löst die Nachrichtenkampagne in Braze aus, die den Benutzer über das Geschenk benachrichtigt. Daher ist eine benutzerdefinierte Liste nicht erforderlich. Stattdessen können Sie das Segment und die Jahrestag-Einstellung in Punchh auswählen.

Punchh-Konfigurationen erforderlich:
- Kampagne: Kampagne zum Jahrestag
- Segment: Wahl des Kunden
- Belohnung: Wahl des Kunden
Überlegungen:
- Monat der Anmeldung verschenken
- Gültigkeitsdauer (Wie lange ist die Geburtstagsbelohnung gültig?)
- Wiederkehrende Kampagnen, Zeitplan erforderlich 

![Ein optionales Segment kann in Punchh erstellt werden, und ein qualifizierter Benutzer erhält eine Belohnung durch eine Punchh-Jubiläumskampagne. Danach wird ein Belohnungsereignis ausgelöst und die Rückrufnachricht wird gesendet, um die Gäste über die von Braze gesendete Belohnung zu informieren.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Rückruf %}
#### Rückrufaktion

Wenn Sie Nutzer aufgrund von Inaktivität ansprechen, können Sie eine Rückrufkampagne verwenden. Der Kunde kann das Segment und die Kampagne in Punchh erstellen, aber Braze für die Nachrichtenübermittlung nutzen.

Wenn Sie die in Braze erstellte Segmentierung verwenden möchten, können Sie ein [benutzerdefiniertes Punchh-Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze), das auf Inaktivität basiert, an eine wiederkehrende Massenangebotskampagne anhängen.

Punchh-Konfigurationen erforderlich:
- Kampagne: Rückrufaktion
- Segment: Wahl des Kunden
- Belohnung: Wahl des Kunden
Überlegungen:
- Kampagne läuft nach einem Zeitplan

![Ein optionales Segment kann in Punchh erstellt werden, und ein qualifizierter Benutzer erhält eine Belohnung durch eine Punchh-Rückrufaktion. Danach wird ein Belohnungsereignis ausgelöst, und die Rückrufnachricht wird gesendet, um die Gäste über die von Braze gesendete Belohnung zu informieren.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/punchh/punchh1.png %}
[2]: {% image_buster /assets/img/punchh/punchh2.png %}
[3]: {% image_buster /assets/img/punchh/punchh3.png %}
[4]: {% image_buster /assets/img/punchh/punchh4.png %}
[5]: {% image_buster /assets/img/punchh/punchh5.png %}
[7]: {% image_buster /assets/img/punchh/punchh6.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[8]: {% image_buster /assets/img/punchh/update1.png %}
[9]: {% image_buster /assets/img/punchh/update2.png %}
[10]: {% image_buster /assets/img/punchh/update3.png %}
[11]: {% image_buster /assets/img/punchh/update4.png %}
[12]: {% image_buster /assets/img/punchh/update5.png %}
[13]: {% image_buster /assets/img/punchh/update6.png %}
[14]: {% image_buster /assets/img/punchh/update7.png %}
