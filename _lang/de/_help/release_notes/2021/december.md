---
nav_title: Dezember
page_order: 0
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Dezember 2021."
alias: "/help/release_notes/2022/january/"
---
# Dezember 2021

## Update zum Exportieren von Nutzer:innen nach Segmenten Endpunkten

Ab Dezember 2021 treten die folgenden Änderungen für den [Endpunkt Nutzer:innen exportieren nach Segmenten]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) in Kraft:

1. Das Feld `fields_to_export` in dieser API-Anfrage wird benötigt. Die Option, alle Felder standardmäßig zu verwenden, wird entfernt.
2. Die Felder für `custom_events`, `purchases`, `campaigns_received` und `canvases_received` enthalten nur Daten aus den letzten 90 Tagen.

## Neue Eigenschaften für Currents Nachrichten-Engagement-Ereignisse

Es wurden neue Eigenschaften für ausgewählte [Messaging-Ereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) hinzugefügt. Dieses Update gilt für die folgenden Currents Nachrichten Engagement-Ereignisse und alle Partner, die sie verwenden:

- Fügen Sie `LINK_ID`, `LINK_ALIAS` zu:
  - E-Mail Klick (alle Ziele)
- Fügen Sie `USER_AGENT` zu:
  - E-Mail-Öffnung
  - E-Mail-Klick
  - E-Mail als Spam markieren
- Fügen Sie `MACHINE_OPEN` zu:
  - E-Mail-Öffnung

## Neuer Liquid-Tag zur Personalisierung

Wir unterstützen jetzt das Targeting von Nutzern:innen, die auf ihrem Gerät Push für den Vordergrund aktiviert haben, mit den folgenden Liquid-Tags:

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

Weitere Informationen finden Sie unter [Unterstützte Tags für die Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## Über Webhooks

Webhooks sind leistungsstarke, flexible Tools - aber sie können auch ein wenig verwirrend sein. Wenn Sie sich fragen, was Webhooks sind und wie Sie sie in Braze verwenden können, lesen Sie unseren neuen Artikel [über Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

## Amazon Personalize

Amazon Personalize ist so, als hätten Sie Ihr eigenes Empfehlungssystem für maschinelles Lernen, das den ganzen Tag läuft. Basierend auf mehr als 20 Jahren Erfahrung mit Empfehlungen ermöglicht Ihnen Amazon Personalize, das Customer-Engagement zu verbessern, indem es personalisierte Produkt- und Inhaltsempfehlungen in Echtzeit sowie gezielte Marketing-Aktionen ermöglicht. 

Wenn Sie mehr erfahren möchten, lesen Sie unseren neuen Artikel über [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize). Dort erfahren Sie, welche Anwendungsfälle Amazon Personalize bietet, mit welchen Daten es arbeitet, wie Sie den Dienst konfigurieren und wie Sie ihn in Braze integrieren können.

## Neue Braze Partnerschaften

### Yotpo - E-Commerce

Die Integration von [Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/) und Braze erlaubt es Ihnen, Sternebewertungen, Top-Rezensionen und visuelle Nutzer:innen-Inhalte zu Produkten in E-Mails und anderen Kommunikationskanälen innerhalb von Braze dynamisch abzurufen und anzuzeigen. Sie können auch Daten zur Kundentreue in E-Mails und andere Kommunikationsmethoden einbeziehen, um eine personalisierte Interaktion zu schaffen, die den Umsatz und die Loyalität steigert.

### Zeotap - Customer Data Platform (CDP)

Mit der Integration von [Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/) und Braze können Sie den Umfang und die Reichweite Ihrer Kampagnen erweitern, indem Sie Segmente von Zeotap-Kunden abgleichen, um Nutzerdaten von Zeotap auf Nutzer:innen-Kontos abzubilden. Sie können dann auf diese Daten reagieren und Ihren Nutzer:innen personalisierte Targeting-Erlebnisse zustellen.