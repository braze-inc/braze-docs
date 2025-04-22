---
nav_title: November
page_order: 1
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für November 2021."
---
# November 2021

## Metriken für die Click-to-Open Rate
Braze hat eine neue E-Mail Metriken, Click-to-Open Rate, im [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) zur Verfügung gestellt. Diese Metrik gibt den Prozentsatz der geöffneten E-Mails an, die angeklickt wurden.

## Maschine Offene Berichtsmetrik

Auf den Canvas- und Kampagnen Analytics-Seiten für E-Mails steht eine neue Metrik für E-Mails zur Verfügung: [Maschinelle Öffnungen]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens). Diese Metrik identifiziert die Öffnungen von E-Mails, die nicht von Menschen stammen (z.B. von Apples Servern geöffnet werden), und wird als Teilmenge der gesamten Öffnungen angezeigt.

## random_bucket_number Liquid-Variable
Die Liste der [unterstützten Liquid-Variablen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) für die Personalisierung von Nachrichten wurde um die Variable `random_bucket_number` erweitert. 

## Richtlinien für Rich-Push-Benachrichtigungen in iOS 15
Die Rich-Docs für iOS wurden um neue [Richtlinien für Push-Benachrichtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) erweitert, darunter Informationen über Benachrichtigungszustände und eine Aufschlüsselung der Variablen für die Textkürzung.

## IPs, die in der EU für Webhooks und Connected-Content auf die Whitelist gesetzt werden sollen
Weitere IPs, die in der EU für Webhooks und Connected-Content auf die Whitelist gesetzt werden können, wurden zu unserem Artikel über [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) und [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) hinzugefügt. Zu diesen neuen IPs gehören `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188` und `3.70.107.88`.

## Endpunkt Käufe exportieren
Ein neuer [`/purchases/product_list` Endpunkt]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) wurde zu Braze hinzugefügt. Dieser Endpunkt gibt paginierte Listen von Produkt IDs zurück.

## Neue Braze Partnerschaften

### Adobe - Customer Data Platform (CDP)
Die Integration von Braze und [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) erlaubt es Marken, ihre Adobe-Daten (angepasste Attribute und Segmente) mit Braze zu verbinden und in Realtime abzubilden. Marken können dann auf Basis dieser Daten handeln und diesen Nutzer:innen personalisierte, zielgerichtete Erlebnisse bieten. 

### BlueConic - Customer Data Platform (CDP) - Kundendaten
Mit [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic) können Braze-Benutzer Daten in persistenten, individuellen Profilen vereinheitlichen und dann über Kundenkontaktpunkte und Systeme hinweg synchronisieren, um eine breite Palette von wachstumsorientierten Initiativen zu unterstützen, einschließlich Orchestrierung des Kundenlebenszyklus, Modellierung und Analytics, digitale Produkte und Erlebnisse, zielgruppenbasierte Monetarisierung und mehr.

### Worthy - Dynamische Inhalte
Die Integration von Braze und [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) ermöglicht es Ihnen, mit dem Drag-and-Drop-Editor für dynamischen Content von Worthy personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen.

### Judo - Dynamische Inhalte
Die Integration von [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) und Braze erlaubt es Ihnen, Komponenten Ihrer Kampagne zu überschreiben und durch Judo-Erlebnisse zu ersetzen. Daten von Braze können verwendet werden, um personalisierte Inhalte in einem Judo-Erlebnis zu unterstützen. Nutzer:innen-Ereignisse und Daten aus dem Erlebnis können für Attribution und Targeting in Braze zurückgeführt werden.

### Leitung - Messaging
Die Integration von [Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) und Braze erlaubt es Ihnen, Braze-Webhooks, fortschrittliche Segmentierungs-, Personalisierungs- und Triggering-Funktionen zu nutzen, um Ihren Benutzern in Line über die [Line Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/) Nachrichten zu senden.

### RevenueCat - Zahlungen
Die Integration von [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) und Braze ermöglicht es Ihnen, die Kauf-Events und Abo-Lebenszyklen Ihrer Kund:innen automatisch plattformübergreifend zu synchronisieren. So können Sie Kampagnen erstellen, die auf die Phase des Kundenlebenszyklus Ihrer Kunden reagieren, z. B. die Ansprache von Kunden, die sich während der kostenlosen Testphase abgemeldet haben, oder das Versenden von Erinnerungen an Kunden mit Rechnungsproblemen.

### Punchh - Loyalität
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) hat sich mit Braze zusammengetan, um Daten zwischen den beiden Plattformen für Geschenk- und Treuezwecke zu synchronisieren. In Braze veröffentlichte Daten stehen für die Segmentierung zur Verfügung und können über in Braze eingerichtete Webhook-Templates mit Nutzerdaten in Punchh synchronisiert werden.  