---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Jampp, einer Performance-Marketing-Plattform, die für die Akquisition und das Retargeting von mobilen Kund:in verwendet wird."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/) ist eine Performance-Marketing-Plattform für die Akquisition und das Retargeting von Mobile-Kund:in. Jampp kombiniert Verhaltensdaten mit prädiktiver und programmatischer Technologie, um Einnahmen für Werbetreibende zu generieren, indem persönliche, relevante Anzeigen geschaltet werden, die Verbraucher:in zum ersten oder häufigeren Kauf inspirieren.

_Diese Integration wird von Jampp gepflegt._

## Über die Integration

Die Integration von Braze und Jampp erlaubt es Nutzern:innen von Braze, Ereignisse über Braze-to-Braze-Webhook-Ereignisse mit Jampp zu synchronisieren. Dadurch können Kund:in ihre Retargeting-Initiativen innerhalb ihres mobilen Werbe-Ökosystems reichhaltigere Datensätze hinzufügen.

Einige Beispiele, wann Sie Kunden:in mit einer Anzeige retargeten möchten:
- Wenn sich der Status des E-Mail- oder Push-Abos eines Kunden ändert.
- Wie ein Kunde mit einer Messaging-Kampagne von Braze interagiert hat.
- Wenn der Kunde einen bestimmten Geofence getriggert hat.

## Voraussetzungen

Diese Integration unterstützt iOS- und Android-Apps.

| Anforderung | Beschreibung |
|---|---|
| Jampp Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein [Jampp-Konto](https://www.jampp.com/). |
| Android App ID | Ihr eindeutiger Bezeichner der Braze-Anwendung für Android (z. B. "com.example"). |
| iOS App ID | Ihr eindeutiger Bezeichner der Braze-Anwendung für iOS (z. B. "012345678"). |
| Enablement der IDFA-Sammlung im Braze SDK | Die Erfassung von IDFA ist im Braze SDK optional und standardmäßig deaktiviert. | 
| Erfassung der Google Advertising ID über ein angepasstes Attribut | Die Erfassung der Google Werbe-ID ist für Kund:in optional und kann als [angepasstes Attribut]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) erfasst werden.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Webhook-Vorlage in Braze

Um eine Jampp Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvase verwenden können, navigieren Sie auf der Braze-Plattform zu **Templates** > **Webhook Templates**.

Wenn Sie eine einmalige Jampp-Webhook-Kampagne erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook Template die folgenden Felder aus:
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
- Legen Sie den Namen des Ereignisses fest. Dieser Name wird in Ihrem Jampp Dashboard angezeigt.
- Übergeben Sie den eindeutigen Bezeichner Ihrer App für Android (z. B. "com.example") und iOS (z. B. "012345678").
- Fügen Sie [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) für das entsprechende angepasste Attribut ein, das Sie als Google Advertising ID tracken. Beachten Sie, dass die ID der Google-Werbung in diesem Beispiel als `aaid` aufgeführt ist, aber Sie müssen sie durch den Namen des angepassten Attributs ersetzen, den Ihre Entwickler:in festgelegt haben.

![Die Webhook-URL und die Vorschau der Nachrichten, die im Braze-Webhook-Builder angezeigt werden.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
Braze sammelt den Identifier for Advertisers (IDFA/AAID) des Geräts nicht automatisch, so dass Sie diese Werte selbst einspeichern müssen. Beachten Sie, dass Sie möglicherweise die Zustimmung der Nutzer:innen zur Erfassung dieser Daten benötigen.
{% endalert %}

#### Kopfzeilen der Anfrage und Methode

Der Webhook von Jampp erfordert eine HTTP-Methode und einen Anfrage-Header.

- **HTTP-Methode**: GET
- **Anfrage-Header**:
  - **Content-Typ**: application/json

![Die Anfrage-Header, die HTTP-Methode und die Vorschau der Nachrichten, die im Braze-Webhook-Builder angezeigt werden.]({% image_buster /assets/img/jampp_method.png %})

#### Anfragetext

Sie müssen für diesen Webhook keinen Anfragetext definieren.

### Schritt 2: Vorschau auf Ihre Anfrage

Vorschau der Nachricht, um sicherzustellen, dass die Anfrage für verschiedene Nutzer:innen korrekt wiedergegeben wird. Wir empfehlen die Vorschau und das Versenden von Testanfragen sowohl für Android- als auch für iOS-Nutzer:innen. Wenn die Anfrage erfolgreich ist, antwortet die API mit `HTTP 204`.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}


