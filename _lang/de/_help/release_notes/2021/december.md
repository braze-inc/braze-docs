---
nav_title: Dezember
page_order: 0
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Dezember 2021."
alias: "/help/release_notes/2022/january/"
---
# Dezember 2021

## Update zum Exportieren von Benutzern nach Segment-Endpunkt

Ab Dezember 2021 treten die folgenden Änderungen für den [Endpunkt Benutzer nach Segment exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) in Kraft:

1. Das Feld `fields_to_export` in dieser API-Anfrage ist erforderlich. Die Option, alle Felder standardmäßig zu verwenden, wird entfernt.
2. Die Felder für `custom_events`, `purchases`, `campaigns_received` und `canvases_received` enthalten nur Daten aus den letzten 90 Tagen.

## Neue Eigenschaften für Currents Nachrichtenereignisse

Es wurden neue Eigenschaften für ausgewählte [Ereignisse der Nachrichteneinbindung]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) hinzugefügt. Dieses Update gilt für die folgenden Currents-Nachrichten und alle Partner, die sie verwenden:

- Fügen Sie `LINK_ID`, `LINK_ALIAS` zu:
  - E-Mail-Klick (alle Ziele)
- Fügen Sie `USER_AGENT` zu:
  - E-Mail-Öffnung
  - E-Mail-Klick
  - E-Mail als Spam markieren
- Fügen Sie `MACHINE_OPEN` zu:
  - E-Mail-Öffnung

## Neuer Tag zur Personalisierung von Flüssigkeiten

Wir unterstützen jetzt die Ansprache von Benutzern, die auf ihrem Gerät die Push-Funktion für den Vordergrund aktiviert haben, mit den folgenden Liquid-Tags:

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

Weitere Informationen finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## Über Webhooks

Webhooks sind leistungsstarke, flexible Tools - aber sie können auch ein wenig verwirrend sein. Wenn Sie sich fragen, was Webhooks sind und wie Sie sie in Braze verwenden können, lesen Sie unseren neuen Artikel [über Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

## Amazon Personalisieren

Amazon Personalize ist wie Ihr eigenes maschinelles Empfehlungssystem von Amazon, das den ganzen Tag über arbeitet. Amazon Personalize basiert auf mehr als 20 Jahren Erfahrung mit Empfehlungen und ermöglicht es Ihnen, die Kundenbindung zu verbessern, indem es personalisierte Produkt- und Inhaltsempfehlungen in Echtzeit und gezielte Marketingaktionen ermöglicht. 

Wenn Sie mehr erfahren möchten, besuchen Sie unseren neuen Artikel über [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/amazon_personalize/). Dort erfahren Sie, welche Anwendungsfälle Amazon Personalize bietet, mit welchen Daten es arbeitet, wie Sie den Service konfigurieren und wie Sie ihn in Braze integrieren können.

## Neue Lötpartnerschaften

### Yotpo - Elektronischer Handel

Die Integration von [Yotpo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/yotpo/) und Braze ermöglicht es Ihnen, Sternebewertungen, Top-Rezensionen und visuelle nutzergenerierte Inhalte zu Produkten in E-Mails und anderen Kommunikationskanälen in Braze dynamisch abzurufen und anzuzeigen. Sie können auch Daten zur Kundentreue in E-Mails und andere Kommunikationsmethoden einbeziehen, um eine persönlichere Interaktion zu schaffen, die den Umsatz und die Loyalität steigert.

### Zeotap - Plattform für Kundendaten

Mit der Integration von [Zeotap]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/zeotap/) und Braze können Sie den Umfang und die Reichweite Ihrer Kampagnen erweitern, indem Sie Zeotap-Kundensegmente synchronisieren, um Zeotap-Benutzerdaten den Braze-Benutzerkonten zuzuordnen. Sie können dann auf diese Daten reagieren und Ihren Nutzern personalisierte, zielgerichtete Erlebnisse bieten.