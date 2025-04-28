---
nav_title: Link-Kürzung
article_title: Link-Kürzung
page_order: 5
description: "In diesem Referenzartikel erfahren Sie, wie Sie die Linkverkürzung in Ihren SMS-Nachrichten aktivieren können und welche Fragen häufig gestellt werden."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# Link-Verkürzung

> Auf dieser Seite erfahren Sie, wie Sie die Linkverkürzung in Ihren SMS-Nachrichten aktivieren, verkürzte Links testen, Ihre benutzerdefinierte Domain in verkürzten Links verwenden und vieles mehr.

Linkverkürzung und Klickverfolgung ermöglichen es Ihnen, in SMS-Nachrichten enthaltene URLs automatisch zu verkürzen und die Klickrate zu analysieren. So erhalten Sie zusätzliche Kennzahlen, die Ihnen helfen zu verstehen, wie Ihre Nutzer mit Ihren SMS-Kampagnen umgehen.

Linkverkürzung und Klickverfolgung können auf der [Ebene der Nachrichtenvariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) sowohl in Kampagnen als auch in Canvases aktiviert werden. 

Die Länge der URL hängt von der aktivierten Trackingmethode ab:
- **Basic Tracking** ermöglicht die Verfolgung von Klicks auf Kampagnenebene. Statische URLs sind 20 Zeichen lang, dynamische 25.
- **Erweitertes Tracking** ermöglicht Klick-Tracking auf Kampagnen- und Nutzerebene. Klicks erzeugen auch ein [SMS-Klickereignis]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), das über Currents gesendet wird. Statische URLs mit erweitertem Tracking haben eine Länge von 27-28 Zeichen, so dass Sie Segmente von Benutzern erstellen können, die auf URLs geklickt haben. Dynamische URLs haben eine Länge von 32-33 Zeichen.

Die Links werden über unsere Shared Short Domain (`brz.ai`) gekürzt. Eine Beispiel-URL könnte etwa so aussehen: `https://brz.ai/8jshX` (einfach, statisch) oder `https://brz.ai/8jshX/2dj8d` (erweitert, dynamisch). Weitere Informationen finden Sie unter [Testen](#testing).

Alle statischen URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Statische verkürzte URLs sind für ein Jahr ab dem Datum ihrer Erstellung gültig. Verkürzte URLs, die Liquid Personalization enthalten, sind zwei Monate lang gültig.

{% alert note %}
Wenn Sie den [intelligenten Kanalfilter]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) von BrazeAI<sup>TM</sup> und den SMS-Kanal auswählbar machen möchten, schalten Sie die SMS-Linkverkürzung mit erweitertem Tracking und [Klick-Tracking]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking) ein.
{% endalert %}

## Linkverkürzung verwenden

Um die Linkverkürzung zu verwenden, stellen Sie sicher, dass der Umschalter zur Linkverkürzung im Nachrichten-Editor aktiviert ist. Wählen Sie dann entweder einfaches oder erweitertes Tracking.

![Nachrichten-Editor mit Umschalter zur Linkverkürzung.][1]

Braze erkennt nur URLs, die mit `http://` oder `https://` beginnen. Wenn eine URL erkannt wird, wird der Bereich **Vorschau** mit einer Platzhalter-URL aktualisiert. Braze schätzt die Länge der URL nach dem Kürzen, aber eine Warnung fordert Sie auf, einen Testbenutzer auszuwählen und die Nachricht als Entwurf zu speichern, um eine genauere Schätzung zu erhalten.

![Nachrichten-Editor mit langer URL im Feld "Nachricht" und einem verkürzten Link in der Vorschau.][3]

### Hinzufügen von UTM-Parametern

{% multi_lang_include click_tracking.md section='UTM-Parameter' %}

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

Wir kürzen URLs, die von Liquid erstellt werden – auch solche in API-Triggereigenschaften. Wenn {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} zum Beispiel eine gültige URL darstellt, wird diese vor dem Versand der SMS gekürzt und dann getrackt. 

### URLs im Endpunkt /messages/send kürzen

Die Linkverkürzung ist über den [`/messages/send`Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) auch bei reinen API-Nachrichten aktiviert. Um auch grundlegendes oder erweitertes Tracking zu aktivieren, verwenden Sie den Anfrageparameter `link_shortening_enabled` oder `user_click_tracking_enabled`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Optional | Boolesch | Setzen Sie `link_shortening_enabled` auf `true`, um die Linkverkürzung und die Klickverfolgung auf Kampagnenebene zu aktivieren. Tracking erfordert eine `campaign_id` und eine `message_variation_id`.|
|`user_click_tracking_enabled`| Optional | Boolesch | Stellen Sie `user_click_tracking_enabled` auf `true` ein, um die Linkverkürzung sowie die Klickverfolgung auf Kampagnen- und Benutzerebene zu aktivieren. Sie können die Trackingdaten verwenden, um Nutzersegmente zu erstellen, die URLs angeklickt haben.<br><br> Um diesen Parameter zu verwenden, muss `link_shortening_enabled` `true` sein, und `campaign_id` und `message_variation_id` müssen vorhanden sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Eine vollständige Liste der Anfrageparameter finden Sie unter [Anfrageparameter]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testen

Bevor Sie Ihre Kampagne oder Ihr Canvas starten, ist es am besten, wenn Sie Ihre Nachricht zunächst in der Vorschau anzeigen und testen. Gehen Sie dazu auf die Registerkarte **Test**, um eine Vorschau anzuzeigen und eine SMS an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) oder einen einzelnen Benutzer zu senden. 

Diese Vorschau wird mit der entsprechenden Personalisierung und der verkürzten URL aktualisiert. Die Anzahl der Zeichen und [kostenpflichtigen Segmente]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) wird ebenfalls um die Personalisierung und die verkürzte URL angepasst. 

Stellen Sie sicher, dass Sie die Kampagne oder das Canvas speichern, bevor Sie eine Testnachricht senden, um eine Darstellung der verkürzten URL zu erhalten, die in Ihrer Nachricht versendet wird. Wenn die Kampagne oder das Canvas vor einem Probeversand nicht gespeichert wird, enthält dieser eine Platzhalter-URL.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine verkürzte URL generiert. Dies geschieht erst dann, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

![Tab "Nachrichtentest" mit Feldern zur Empfängerauswahl.][2]

{% alert note %}
Die Flüssigpersonalisierung und die verkürzten URLs werden auf der Registerkarte **Test** nach der Auswahl eines Benutzers als Vorlage verwendet. Überprüfen Sie die Nutzerauswahl, um eine genaue Zeichenzahl zu erhalten.
{% endalert %}

## Klick-Tracking

Wenn die Linkverkürzung aktiviert ist, enthält die SMS- und MMS-Leistungstabelle eine Spalte mit dem Titel **Gesamtklicks**, die die Anzahl der Klickereignisse pro Variante und die zugehörige Klickrate anzeigt. Weitere Einzelheiten zu den SMS-Metriken finden Sie unter [Leistung von SMS-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance).

![Tabelle der SMS- und MMS-Leistungskennzahlen.][4]

Die Diagramme **Historische Leistung** und **SMS/MMS-Leistung** enthalten auch eine Option für **Gesamtklicks** und zeigen eine tägliche Zeitreihe von Klickereignissen. Klicks werden bei einer Weiterleitung erhöht (z.B. wenn ein Benutzer einen Link besucht) und können mehr als einmal pro Benutzer erhöht werden.

## Nutzer-Retargeting

Eine Anleitung zum Retargeting finden Sie unter [SMS-Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include click_tracking.md section='Angepasste Domains' %}

{% multi_lang_include click_tracking.md section='Häufig gestellte Fragen' %}

### Kann ich wissen, welche einzelnen Benutzer auf eine URL klicken?

Ja Wenn das **erweiterte Tracking** aktiviert ist, können Sie Nutzer, die auf URLs geklickt haben, erneut ansprechen, indem Sie die [SMS-Retargeting-Filter]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) oder die von Currents gesendeten SMS-Klick-Ereignisse (`users.messages.sms.ShortLinkClick`) nutzen.

### Funktioniert die Linkverkürzung mit Deep Links oder universellen Links?

Deeplinks können nicht gekürzt werden. Sie können universelle Links von Anbietern wie Branch oder Appsflyer kürzen, aber Braze ist nicht in der Lage, Probleme zu beheben, die dabei auftreten können (z. B. die Unterbrechung der Attribution oder eine Umleitung).

[1]: {% image_buster /assets/img/link_shortening/shortening1.png %}
[2]: {% image_buster /assets/img/link_shortening/shortening2.png %}
[3]: {% image_buster /assets/img/link_shortening/shortening3.png %}
[4]: {% image_buster /assets/img/link_shortening/shortening4.png %}
[5]: {% image_buster /assets/img/sms/retargeting5.png %}
[6]: {% image_buster /assets/img/sms/retargeting4.png %}
[7]: {% image_buster /assets/img/custom_domain.png %}
[8]: {% image_buster /assets/img/custom_domain2.png %}
[11]: {% image_buster /assets/img/sms/link_shortening10.png %}
[13]: {% image_buster /assets/img/link_shortening/shortening3.png %}   

