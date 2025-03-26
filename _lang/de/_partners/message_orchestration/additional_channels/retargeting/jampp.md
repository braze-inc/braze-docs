---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Jampp, einer Performance-Marketing-Plattform für die Akquisition und das Retargeting von mobilen Kunden."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/) ist eine Performance-Marketing-Plattform für die Akquise und das Retargeting von mobilen Kunden. Jampp kombiniert Verhaltensdaten mit prädiktiver und programmatischer Technologie, um Einnahmen für Werbetreibende zu generieren, indem persönliche, relevante Anzeigen geschaltet werden, die die Verbraucher zum ersten oder häufigeren Kauf anregen.

Die Integration von Braze und Jampp ermöglicht es Braze-Benutzern, Ereignisse über Braze-Webhook-Ereignisse mit Jampp zu synchronisieren. Dadurch können Kunden ihre Retargeting-Initiativen innerhalb ihres mobilen Werbe-Ökosystems mit umfangreicheren Datensätzen ergänzen.

Einige Beispiele, wann Sie Kunden mit einer Anzeige erneut ansprechen sollten:
- Wenn sich der Status des E-Mail- oder Push-Abonnements eines Kunden ändert.
- Wie ein Kunde mit einer Braze Messaging-Kampagne interagiert hat.
- Wenn der Kunde einen bestimmten Geofence ausgelöst hat.

## Voraussetzungen

Diese Integration unterstützt iOS- und Android-Apps.

| Anforderung | Beschreibung |
|---|---|
| Jampp-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Jampp-Konto](https://www.jampp.com/). |
| Android-App-ID | Ihre eindeutige Braze-Anwendungskennung für Android (z. B. "com.example"). |
| iOS App ID | Ihre eindeutige Braze-Anwendungskennung für iOS (z. B. "012345678"). |
| Aktivieren Sie die IDFA-Sammlung im Braze SDK | Die IDFA-Sammlung ist im Braze SDK optional und standardmäßig deaktiviert. | 
| Erfassung der Google Werbe-ID über ein benutzerdefiniertes Attribut | Die Erfassung der Google-Werbe-ID ist für Kunden optional und kann als [benutzerdefiniertes Attribut][5]] erfasst werden.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Webhook-Vorlage in Braze

Um eine Jampp-Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvases verwenden können, navigieren Sie auf der Braze-Plattform zu **Vorlagen** > **Webhook-Vorlagen**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Wenn Sie eine einmalige Jampp-Webhook-Kampagne erstellen oder eine vorhandene Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen.

Füllen Sie in Ihrer neuen Webhook-Vorlage die folgenden Felder aus:
- **Anfrage Körper**: Rohtext
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

In der Webhook-URL müssen Sie:
- Legen Sie den Namen des Ereignisses fest. Dieser Name wird in Ihrem Jampp-Dashboard angezeigt.
- Übergeben Sie den eindeutigen Anwendungsbezeichner Ihrer App für Android (z. B. "com.example") und iOS (z. B. "012345678").
- Fügen Sie [Liquid][1] für das entsprechende benutzerdefinierte Attribut ein, das Sie als Google-Werbe-ID verfolgen. Beachten Sie, dass die Google-Werbe-ID in diesem Beispiel als `aaid` aufgeführt ist, aber Sie müssen sie durch den Namen des benutzerdefinierten Attributs ersetzen, den Ihre Entwickler festgelegt haben.

![Die Webhook-URL und die Nachrichtenvorschau werden im Braze Webhook-Builder angezeigt.][2]

{% alert important %}
Braze erfasst die IDFA/AAID des Geräts nicht automatisch, so dass Sie diese Werte selbst speichern müssen. Beachten Sie, dass Sie für die Erfassung dieser Daten möglicherweise die Zustimmung des Benutzers benötigen.
{% endalert %}

#### Kopfzeilen der Anfrage und Methode

Der Jampp-Webhook erfordert eine HTTP-Methode und einen Anfrage-Header.

- **HTTP-Methode**: GET
- **Kopfzeilen anfordern**:
  - **Inhalt-Typ**: application/json

![Die Anfrage-Header, die HTTP-Methode und die Nachrichtenvorschau, die im Braze Webhook-Builder angezeigt werden.][3]

#### Anfragetext

Sie müssen für diesen Webhook keinen Anfragetext definieren.

### Schritt 2: Vorschau Ihrer Anfrage

Zeigen Sie die Nachricht in der Vorschau an, um sicherzustellen, dass die Anfrage für verschiedene Benutzer korrekt wiedergegeben wird. Wir empfehlen eine Vorschau und das Versenden von Testanfragen sowohl für Android- als auch für iOS-Nutzer. Wenn die Anfrage erfolgreich ist, antwortet die API mit `HTTP 204`.

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid
[2]: {% image_buster /assets/img/jampp_webhook.png %}
[3]: {% image_buster /assets/img/jampp_method.png %}
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
