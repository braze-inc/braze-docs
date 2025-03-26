---
nav_title: Shopify Übersicht
article_title: "Shopify Übersicht"
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Shopify, einem globalen Handelsunternehmen, das es Ihnen ermöglicht, Ihren Shopify-Shop nahtlos mit Braze zu verbinden, um ausgewählte Shopify-Webhooks an Braze zu übergeben. Nutzen Sie die kanalübergreifenden Strategien und Canvas von Braze, um Kunden dazu zu bewegen, ihre Einkäufe abzuschließen, oder um Benutzer auf der Grundlage ihrer früheren Einkäufe erneut anzusprechen."
page_type: partner
search_tag: Partner
alias: "/shopify_overview/"
page_order: 0
---

# Shopify Übersicht

> [Shopify](https://www.shopify.com/) ist ein weltweit führendes Handelsunternehmen, das zuverlässige Tools für die Gründung, das Wachstum, die Vermarktung und die Verwaltung von Einzelhandelsgeschäften jeder Größe anbietet. Shopify macht den Handel für alle besser, mit einer Plattform und Dienstleistungen, die auf Zuverlässigkeit ausgelegt sind und gleichzeitig ein besseres Einkaufserlebnis für Verbraucher überall bieten.

Die Shopify- und Braze-Integration ermöglicht es Ihnen, Ihren Shopify-Shop zu verbinden, um Ihre Shopify-Daten nahtlos an Braze zu übergeben. Sie können kanalübergreifende Strategien und Canvas in Braze nutzen, um neue Leads anzusprechen, neue Kunden anzusprechen oder Ihre Benutzer mit Nachrichten über abgebrochene Kassiervorgänge erneut anzusprechen, um sie dazu zu bewegen, ihre Einkäufe abzuschließen.

## Unterstützte Funktionen

- Verfolgen Sie das Verhalten vor Ort und anonyme Benutzer über das Braze Web SDK
- Unterstützung bei der Synchronisierung und dem Abgleich von Shopify-Kunden in Braze über das Braze Web SDK
- Shopify-Kundendaten synchronisieren
- Erfassen Sie die Opt-In-Status von Shopify-E-Mail- und SMS-Abonnenten
- Historische Shopify-Einkaufsdaten wieder auffüllen 
- Shopify Katalog synchronisieren 
- Verwenden Sie In-App-Nachrichten als Kanal 

## Unterstützte Anwendungsfälle 

- Path-to-purchase-Kampagnen und Canvas User Journeys, einschließlich: 
  - Browse abandonment 
  - Verlassener Wagen 
  - Abgebrochene Kasse 
- Post-Purchase-Kampagnen und Canvas-Benutzerreisen, einschließlich:
  - Auftragsbestätigungen 
  - Updates zum Thema Fulfillment 
  - Stornierungen von Bestellungen 
  - Erstattungen bestellen
- Produkt-Empfehlungen
- Cross-Selling und Upselling
- [Vorrätig]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## Anforderungen

| Anforderung | Beschreibung |
| --- | --- |
| Shopify-Shop | Sie haben einen aktiven [Shopify-Shop](https://www.shopify.com/).<br><br>Sie können einen Shopify-Shop pro Arbeitsbereich verbinden. Wenn Sie daran interessiert sind, mehrere Geschäfte mit einem Arbeitsbereich zu verbinden, wenden Sie sich an Ihren Customer Success Manager, um an der Shopify Multiple Stores Beta teilzunehmen. |
| Shopify-Benutzerberechtigungen | Sie haben eine der folgenden Berechtigungen für Ihren Shopify-Shop:{::nomarkdown}<ul><li>Ladenbesitzer</li><li>Personal</li><li>Mitglied mit allen allgemeinen und Online-Shop-Einstellungen sowie diesen zusätzlichen Admin-Berechtigungen:<ul><li>Bestellungen</li><li>Ansicht (zu finden unter <b>Produkte</b>)</li><li>Kunden</li><li>Einstellungen verwalten</li><li>Sehen Sie sich die von Mitarbeitern und Kollegen entwickelten Apps an</li><li>Verwalten und Installieren von Apps und Kanälen</li></ul></li></ul>{:/} |
| Braze Web SDK Implementierung | Um das Onsite-Verhalten und anonyme Benutzer zu verfolgen, müssen Sie das Braze Web SDK entweder über unsere standardmäßige Shopify-Integration oder manuell implementieren. <br><br>Weitere Informationen zu Ihren Implementierungsoptionen finden Sie unter [Implementierung des Web SDK auf Ihrer Shopify-Website]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk). |
| Segmentierung von Ereigniseigenschaften aktiviert | Um zu bestätigen, dass Sie Ihre Shopify-Ereignisseigenschaften segmentieren können, wenden Sie sich an Ihren Customer Success Manager oder den [Braze-Support]({{site.baseurl}}/braze_support/), um sicherzustellen, dass die Segmentierung der Ereigniseigenschaften für Ihr Braze-Dashboard aktiviert ist. |
{: .reset-td-br-1 .reset-td-br-2 }

## Allgemeine Datenschutzverordnung (GDPR)

In Bezug auf personenbezogene Daten, die Braze von seinen Kunden oder im Namen seiner Kunden zur Verfügung gestellt werden, ist Braze der Datenverarbeiter und unsere Kunden sind die Datenverantwortlichen. Dementsprechend verarbeitet Braze solche personenbezogenen Daten ausschließlich auf Anweisung unserer Kunden und benachrichtigt unsere Kunden gegebenenfalls über Anfragen von Betroffenen. Als für die Datenverarbeitung Verantwortliche reagieren unsere Kunden direkt auf die Anfragen der Betroffenen. Im Rahmen der Shopify-Integration der Braze-Plattform empfängt Braze automatisch [die GDPR-Webhooks von Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). Braze-Kunden sind jedoch letztendlich dafür verantwortlich, auf Anfragen von Shopify-Kunden zu reagieren, die durch die Verwendung von [Braze-SDKs]({{site.baseurl}}/developer_guide/home/) oder [REST-APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) in Übereinstimmung mit unseren Richtlinien zur [Einhaltung der GDPR]({{site.baseurl}}/help/dp-technical-assistance/) gestellt werden.
