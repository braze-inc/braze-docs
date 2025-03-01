---
nav_title: Wiederherstellen
article_title: Wiederherstellen
alias: /partners/remerge/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Remerge, einer speziell entwickelten App für Retargeting in großem Maßstab, die Sie mit Tools zur effizienten Segmentierung von App-Zielgruppen und zum Retargeting von Benutzern ausstattet."
page_type: partner
search_tag: Partner

---

# Wiederherstellen

> [Remerge](https://www.remerge.io/) wurde speziell für das Retargeting von Apps in großem Umfang entwickelt und gibt Ihnen Tools an die Hand, mit denen Sie App-Zielgruppen effizient segmentieren und Nutzer erneut ansprechen können.

Die Integration von Braze und Remerge hilft Ihnen bei der Entwicklung robuster, kanalübergreifender Lifecycle-Marketing-Kampagnen, indem sie Benutzerdaten über Webhook-Ereignisse an Remerge sendet, um das Retargeting von Benutzern über deren mobile Demand-Side-Plattform zu unterstützen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Konto wiederherstellen | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Remerge-Konto. |
| Webhook-Schlüssel wiederherstellen | Dieser Schlüssel wird von Remerge zur Verfügung gestellt. |
| Android-App-ID | Ihre eindeutige Braze-Anwendungskennung für Android (z. B. "com.example"). |
| iOS App ID | Ihre eindeutige Braze-Anwendungskennung für iOS (z. B. "012345678"). |
| Aktivieren Sie die IDFA-Sammlung im Braze SDK | Die IDFA-Sammlung ist im Braze SDK optional und standardmäßig deaktiviert. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie Ihre Braze Webhook-Vorlage

Um eine Remerge-Webhook-Vorlage für zukünftige Kampagnen oder Canvases zu erstellen, navigieren Sie zu **Vorlagen** > **Webhook-Vorlagen** in der Braze-Plattform. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Wenn Sie eine einmalige Remerge-Webhook-Kampagne erstellen oder eine vorhandene Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen.

Füllen Sie in Ihrer neuen Webhook-Vorlage die folgenden Felder aus:
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
- Legen Sie den Namen des Ereignisses fest. Dieser Name erscheint dann in Ihrem [remerge.io][65] Dashboard.
- Übergeben Sie den eindeutigen Anwendungsbezeichner Ihrer App für Android (z. B. "com.example") und iOS (z. B. "012345678") an remerge.
- Definieren Sie einen Schlüssel; Remerge stellt diesen zur Verfügung.

![Die Webhook-URL und die Nachrichtenvorschau werden im Braze Webhook-Builder angezeigt.][67]

{% alert important %}
Braze erfasst die IDFA/AAID des Geräts nicht automatisch, so dass Sie diese Werte selbst speichern müssen. Beachten Sie, dass Sie für die Erfassung dieser Daten möglicherweise die Zustimmung des Benutzers benötigen.
{% endalert %}

#### Kopfzeilen der Anfrage und Methode

Der Remerge-Webhook erfordert eine HTTP-Methode und einen Anfrage-Header.

- **HTTP-Methode**: GET
- **Kopfzeilen anfordern**:
  - **Inhalt-Typ**: application/json

![Die Anfrage-Header, die HTTP-Methode und die Nachrichtenvorschau, die im Braze Webhook-Builder angezeigt werden.][68]

#### Anfragetext

Sie müssen für diesen Webhook keinen Anfragetext definieren.

## Schritt 2: Vorschau Ihrer Anfrage

Zeigen Sie die Nachricht in der Vorschau an, um sicherzustellen, dass die Anfrage für verschiedene Benutzer korrekt wiedergegeben wird. Wir empfehlen eine Vorschau und das Versenden von Testanfragen sowohl für Android- als auch für iOS-Nutzer. Wenn die Anfrage erfolgreich ist, antwortet die API mit `HTTP 204`.

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %}
[68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}
