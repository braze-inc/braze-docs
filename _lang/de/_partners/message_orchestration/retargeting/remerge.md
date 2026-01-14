---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Remerge, einer speziell entwickelten App für Retargeting in großem Maßstab, die Ihnen Tools zur effizienten Segmentierung von Zielgruppen in Apps und zum Retargeting von Nutzer:innen an die Hand gibt."
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) wurde speziell für das Retargeting von Apps in großem Umfang entwickelt und gibt Ihnen Tools an die Hand, mit denen Sie Zielgruppen von Apps effizient segmentieren und Nutzer:innen erneut ansprechen können.

_Diese Integration wird von Remerge gepflegt._

## Über die Integration

Die Integration von Braze und Remerge hilft Ihnen, robuste, kanalübergreifende Lebenszyklus-Kampagnen zu entwickeln, indem sie Benutzerdaten über Webhook-Ereignisse an Remerge sendet, um das Retargeting von Benutzern über deren mobile Demand-Side-Plattform zu unterstützen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Konto remergen | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Remerge-Konto. |
| Webhook-Schlüssel remergen | Dieser Schlüssel wird von Remerge zur Verfügung gestellt. |
| Android App ID | Ihr eindeutiger Bezeichner der Braze-Anwendung für Android (z. B. "com.example"). |
| iOS App ID | Ihr eindeutiger Bezeichner der Braze-Anwendung für iOS (z. B. "012345678"). |
| Enablement der IDFA-Sammlung im Braze SDK | Die Erfassung von IDFA ist im Braze SDK optional und standardmäßig deaktiviert. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie Ihr Braze-to-Braze-Webhook Template

Um eine Remerge-Webhook-Vorlage für zukünftige Kampagnen oder Canvase zu erstellen, navigieren Sie zu **Templates** > **Webhook Templates** in der Braze-Plattform. 

Wenn Sie eine einmalige Remerge-Webhook-Kampagne erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook Template die folgenden Felder aus:
- **Anfrage Körper**: Rohtext
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %} 
{% assign android_app_id = 'your_android_app_id' %} 
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

In der Webhook-URL müssen Sie:
- Verwenden Sie die `https://remerge.events/event` API, um Ihre Webhook-Ereignisse zu senden.
- Legen Sie den Namen des Ereignisses fest. Dieser Name erscheint dann in Ihrem [remerge.io](https://www.remerge.io/) Dashboard.
- Übergeben Sie den eindeutigen Bezeichner Ihrer App für Android (z. B. "com.example") und iOS (z. B. "012345678") an remerge.
- Definieren Sie einen Schlüssel; Remerge wird diesen bereitstellen.

![Die Webhook-URL und die Vorschau der Nachrichten, die im Braze-Webhook-Builder angezeigt werden.]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
Braze sammelt den Identifier for Advertisers (IDFA/AAID) des Geräts nicht automatisch, so dass Sie diese Werte selbst einspeichern müssen. Beachten Sie, dass Sie möglicherweise die Zustimmung der Nutzer:innen zur Erfassung dieser Daten benötigen.
{% endalert %}

#### Kopfzeilen der Anfrage und Methode

Der Webhook Remerge erfordert eine HTTP-Methode und einen Anfrage-Header.

- **HTTP-Methode**: GET
- **Anfrage-Header**:
  - **Content-Typ**: application/json

![Die Anfrage-Header, die HTTP-Methode und die Vorschau der Nachrichten, die im Braze-Webhook-Builder angezeigt werden.]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### Anfragetext

Sie müssen für diesen Webhook keinen Anfragetext definieren.

## Schritt 2: Vorschau auf Ihre Anfrage

Vorschau der Nachricht, um sicherzustellen, dass die Anfrage für verschiedene Nutzer:innen korrekt wiedergegeben wird. Wir empfehlen die Vorschau und das Versenden von Testanfragen sowohl für Android- als auch für iOS-Nutzer:innen. Wenn die Anfrage erfolgreich ist, antwortet die API mit `HTTP 204`.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}


