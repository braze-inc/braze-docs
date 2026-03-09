---
nav_title: Link-Verkürzung
article_title: Link-Kürzung
page_order: 3
description: "In diesem Referenzartikel erfahren Sie, wie Sie die Linkverkürzung in Ihren SMS-Nachrichten aktivieren können und welche Fragen häufig gestellt werden."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Link-Verkürzung

> Auf dieser Seite erfahren Sie, wie Sie die Linkverkürzung in Ihren SMS- und RCS-Nachrichten aktivieren, verkürzte Links testen, Ihre angepasste Domain in verkürzten Links verwenden und vieles mehr.

Link-Verkürzung und Tracking ermöglichen es Ihnen, URLs in SMS- oder RCS-Nachrichten automatisch zu verkürzen und Click-through-Raten zu erfassen. So erhalten Sie zusätzliche Metriken für das Engagement Ihrer Nutzer:innen in Ihren Kampagnen.

Linkverkürzung und Klickverfolgung können auf der [Ebene der Nachrichtenvariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) sowohl in Kampagnen als auch in Canvases aktiviert werden. 

Die Länge der URL hängt von der aktivierten Trackingmethode ab:
- **Basic Tracking** ermöglicht die Verfolgung von Klicks auf Kampagnenebene. Statische URLs haben eine Länge von 20 Zeichen, personalisierte URLs haben eine Länge von 25 Zeichen.
- **Fortgeschrittenes Tracking** bringt das Tracking von Klicks auf Kampagnen- und Nutzer:innen-Ebene voran und ermöglicht die Nutzung von Segmentierungs- und Retargeting-Funktionen, die auf Klicks basieren. Klicks erzeugen auch ein [SMS-Klickereignis]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), das über Currents gesendet wird. Statische URLs mit erweitertem Tracking haben eine Länge von 27 bis 28 Zeichen, wodurch Sie Segmente von Nutzern erstellen können, die auf URLs geklickt haben. Personalisierte URLs haben eine Länge von 32 bis 33 Zeichen.

Links werden mithilfe unserer gemeinsamen Kurzdomain (`brz.ai`) gekürzt. Eine Beispiel-URL könnte etwa so aussehen: `https://brz.ai/8jshX` (einfach, statisch) oder `https://brz.ai/p/8jshX/2dj8d` (fortschrittlich, personalisiert). Weitere Informationen finden Sie unter [Testen](#testing).

Alle statischen URLs, die mit`http://`  oder  beginnen`https://`, werden gekürzt. Statische verkürzte URLs sind ab dem Datum ihrer Erstellung ein Jahr lang gültig. Verkürzte URLs, die Liquid-Personalisierung enthalten, sind zwei Monate lang gültig.

{% alert note %}
Wenn Sie den <sup>BrazeAITM</sup> [Intelligent Channel Filter]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) verwenden möchten und die SMS- und RCS-Kanäle auswählbar sein sollen, schalten Sie die Linkverkürzung mit fortschrittlichem Tracking ein.
{% endalert %}

## Linkverkürzung verwenden

Um die Linkverkürzung zu verwenden, stellen Sie sicher, dass der Umschalter zur Linkverkürzung im Nachrichten-Editor aktiviert ist. Wählen Sie dann entweder einfaches oder erweitertes Tracking.

![Nachrichten-Editor mit Umschalter zur Linkverkürzung.]({% image_buster /assets/img/link_shortening/shortening1.png %})

Braze erkennt ausschließlich URLs, die mit`http://`  oder beginnen`https://`. Wenn eine URL erkannt wird, wird der Bereich **Vorschau** mit einer Platzhalter-URL aktualisiert. Braze schätzt die Länge der URL nach der Verkürzung, jedoch wird eine Warnung angezeigt, die Sie dazu auffordert, einen Testnutzer:in auszuwählen und die Nachricht als Entwurf zu speichern, um eine genauere Schätzung zu erhalten.

![Nachrichten-Editor mit langer URL im Feld "Nachricht" und einem verkürzten Link in der Vorschau.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Hinzufügen von UTM-Parametern

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Flüssige Personalisierung in URLs

Sie können Ihre URL direkt im Braze Composer dynamisch aufbauen, so dass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Benutzern einzigartige Links senden können (z. B. die Weiterleitung zu einem abgebrochenen Warenkorb oder zu einem bestimmten Produkt, das wieder auf Lager ist).

### Erstellen Sie eine URL mit unterstützten Liquid Personalisierungs-Tags

URLs können durch die Verwendung beliebiger [unterstützter Liquid-Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) dynamisch generiert werden.

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Wir unterstützen auch die Verkürzung von benutzerdefinierten Liquid-Variablen. Im Folgenden finden Sie einige Beispiele:

### Erstellen Sie eine URL mit Liquid-Variablen

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Kürzen Sie URLs, die von Liquid-Variablen gerendert werden

Wir kürzen URLs, die von Liquid erstellt werden – auch solche in API-Triggereigenschaften. Wenn beispielsweise  eine{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} gültige URL darstellt, kürzen und führen wir Tracking für diese URL durch, bevor wir die Nachricht versenden. 

### URLs im`/messages/send`Endpunkt verkürzen

Die Linkverkürzung ist über den [`/messages/send`Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) auch bei reinen API-Nachrichten aktiviert. Um auch grundlegendes oder erweitertes Tracking zu aktivieren, verwenden Sie den Anfrageparameter `link_shortening_enabled` oder `user_click_tracking_enabled`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Optional | Boolesch | Setzen Sie `link_shortening_enabled` auf `true`, um die Linkverkürzung und die Klickverfolgung auf Kampagnenebene zu aktivieren. Tracking erfordert eine `campaign_id` und eine `message_variation_id`.|
|`user_click_tracking_enabled`| Optional | Boolesch | Stellen Sie `user_click_tracking_enabled` auf `true` ein, um die Linkverkürzung sowie die Klickverfolgung auf Kampagnen- und Benutzerebene zu aktivieren. Sie können die Trackingdaten verwenden, um Nutzersegmente zu erstellen, die URLs angeklickt haben.<br><br> Um diesen Parameter zu verwenden, muss `link_shortening_enabled` `true` sein, und `campaign_id` und `message_variation_id` müssen vorhanden sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Eine vollständige Liste der Anfrageparameter finden Sie unter [Anfrageparameter]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testen

Bevor Sie Ihre Kampagne oder Ihr Canvas starten, ist es am besten, wenn Sie Ihre Nachricht zunächst in der Vorschau anzeigen und testen. Gehen Sie dazu auf den Tab **Test**, um eine Vorschau anzuzeigen und eine SMS oder RCS-Nachricht an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) oder einen einzelnen Nutzer:innen zu senden. 

Diese Vorschau erhält ein Update mit den entsprechenden Personalisierungen und der verkürzten URL. Die Anzahl der Zeichen und [abrechnungsfähigen Segmente]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) wird ebenfalls aktualisiert, um die Personalisierung und die verkürzte URL widerzuspiegeln.

Bitte stellen Sie sicher, dass Sie die Kampagne oder Canvas speichern, bevor Sie eine Testnachricht versenden, um eine Darstellung der verkürzten URL zu erhalten, die in Ihrer Nachricht versendet wird. Wenn die Kampagne oder Canvas vor dem Testversand nicht gespeichert wird, enthält der Testversand eine Platzhalter-URL.

Damit Canvases im Filter „Angeklickter verkürzter SMS-Link“ angezeigt werden, muss der Canvas-Schritt, der den Kurzlink enthält, auch mit erweitertem Tracking aktiviert sein, das eine Nachverfolgung der Klicks auf Benutzerebene ermöglicht. Wenn der Kurzlink mit grundlegendem Tracking konfiguriert ist, steht die Option zum Filtern von SMS-Kurzlink-Klickereignissen nicht zur Verfügung.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine verkürzte URL generiert. Die eigentliche verkürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

![Tab "Nachrichtentest" mit Feldern zur Empfängerauswahl.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
Die Flüssigpersonalisierung und die verkürzten URLs werden auf der Registerkarte **Test** nach der Auswahl eines Benutzers als Vorlage verwendet. Überprüfen Sie die Nutzerauswahl, um eine genaue Zeichenzahl zu erhalten.
{% endalert %}

## Klick-Tracking

Wenn die Linkverkürzung aktiviert ist, enthält die Tabelle** „SMS/MMS/RCS-Performance“** eine Spalte mit dem** **Titel **„Gesamtklicks“**, in der die Anzahl der Klicks pro Variante und die zugehörige Klickrate angezeigt werden. Weitere Einzelheiten zu den Metriken finden Sie unter [Performance von Nachrichten]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tabelle der SMS- und MMS-Leistungskennzahlen.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Die Tabellen **„Historische Performance“** und **„SMS/MMS/RCS-Performance“** enthalten auch eine Option für **„Gesamtklicks“** und zeigen eine tägliche Zeitreihe von Klickereignissen an. Klicks werden bei einer Weiterleitung erhöht (z.B. wenn ein Benutzer einen Link besucht) und können mehr als einmal pro Benutzer erhöht werden.

## Nutzer-Retargeting

Eine Anleitung zum Retargeting finden Sie unter [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Kann ich wissen, welche einzelnen Benutzer auf eine URL klicken?

Ja Wenn das **erweiterte Tracking** aktiviert ist, können Sie Nutzer, die auf URLs geklickt haben, erneut ansprechen, indem Sie die [SMS-Retargeting-Filter]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) oder die von Currents gesendeten SMS-Klick-Ereignisse (`users.messages.sms.ShortLinkClick`) nutzen.

### Funktioniert die Linkverkürzung mit Deep Links oder universellen Links?

Deeplinks können nicht gekürzt werden. Alternativ können Sie Universal Links von Drittanbietern wie Branch oder Appsflyer verkürzen, jedoch kann es für die Nutzer:innen zu einer kurzen Weiterleitung oder einem „Flackereffekt” kommen. Dies geschieht, weil der verkürzte Link zunächst über das Internet geleitet wird, bevor er zu dem universellen Link weitergeleitet wird, der die Öffnung der App unterstützt. Darüber hinaus ist Braze nicht in der Lage zur Fehlerbehebung, wenn es um die Verkürzung von Universal Links geht, da dies zu Problemen führen kann, wie beispielsweise der Verlust der Attribution oder unerwartete Weiterleitungen.

{% alert note %}
Bitte testen Sie die Benutzererfahrung, bevor Sie die Linkverkürzung mit Universal Links implementieren, um sicherzustellen, dass sie Ihren Erwartungen entspricht.
{% endalert %}

### Ist `send_ids` mit SMS-Klick-Ereignissen verbunden?

Nein. Wenn Sie jedoch fortgeschrittenes Tracking vorgebracht haben, können Sie `send_ids` generell mit Klick-Ereignissen attributieren, indem Sie mit dem [Query Builder]({{site.baseurl}}/query_builder/) Currents Daten mit dieser Abfrage abfragen:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```
