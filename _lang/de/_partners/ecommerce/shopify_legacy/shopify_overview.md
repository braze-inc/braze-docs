---
nav_title: Shopify Übersicht (Legacy)
article_title: "Shopify Übersicht (Legacy)"
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Shopify, einem globalen Handelsunternehmen, die es Ihnen erlaubt, ihren Shopify-Shop nahtlos mit Braze zu verbinden, um ausgewählte Shopify-Webhooks an Braze weiterzugeben. Nutzen Sie die kanalübergreifenden Strategien von Braze und Canvas, um Kund:innen zum Abschluss ihrer Einkäufe zu bewegen oder Nutzer:innen auf der Grundlage ihrer früheren Einkäufe erneut zu retargeten."
page_type: partner
search_tag: Partner
alias: /shopify_overview_legacy/
page_order: 0
---

# Shopify Übersicht (Legacy)

> [Shopify](https://www.shopify.com/) ist ein weltweit führendes Handelsunternehmen, das zuverlässige Tools für die Gründung, das Wachstum, das Marketing und die Verwaltung von Einzelhandelsgeschäften jeder Größe bereitstellt. Shopify macht den Handel für alle besser, mit einer Plattform und Diensten, die auf Zuverlässigkeit ausgelegt sind und Verbrauchern:in aller Welt ein besseres Einkaufserlebnis zustellen.

Die Integration von Shopify und Braze erlaubt es Ihnen, Ihren Shopify-Shop zu verbinden, um Ihre Shopify-Daten nahtlos an Braze weiterzugeben. Sie können kanalübergreifende Strategien und Canvas in Braze nutzen, um neue Leads zu engagieren, neue Kunden zu benachrichtigen oder Ihre Benutzer mit Nachrichten über abgebrochene Kassiervorgänge zu retargeten, um sie zum Abschluss ihrer Einkäufe zu bewegen.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Unterstützte Funktionen

- Tracking von Onsite-Verhalten und anonymen Nutzer:innen über das Braze Web SDK
- Unterstützung bei der Synchronisierung und dem Abgleich von Shopify-Kunden in Braze über das Braze Internet SDK
- Synchronisieren Sie Shopify Kundendaten
- Sammeln Sie die Opt-in-Status von Shopify E-Mail- und SMS-Abonnenten Abo
- Backfill historischer Shopify Einkaufsdaten 
- Shopify Katalog synchronisieren 
- Verwenden Sie In-App-Nachrichten als Kanal 

## Unterstützte Anwendungsfälle 

- Path-to-purchase Kampagnen und Canvas Nutzer:innen, einschließlich: 
  - Browse abandonment 
  - Warenkorb-Abbruch 
  - Abgebrochene Kasse 
- Kampagnen nach dem Kauf und Canvas Nutzer:innen, einschließlich:
  - Auftragsbestätigungen 
  - Updates für die Auslieferung 
  - Stornierungen von Bestellungen 
  - Erstattungen bestellen
- Produkt-Empfehlungen
- Cross-Selling und Upselling
- [Vorrätig]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## Anforderungen

| Anforderung | Beschreibung |
| --- | --- |
| Shopify-Shop | Sie haben einen aktiven [Shopify](https://www.shopify.com/) Shop.<br><br>Sie können einen Shopify Shop pro Workspace verbinden. Wenn Sie daran interessiert sind, mehrere Shops mit einem Workspace zu verbinden, wenden Sie sich an Ihren Customer-Success-Manager, um an der Shopify Multiple Stores Beta teilzunehmen. |
| Shopify Nutzer:innen-Berechtigungen | Sie haben eine der folgenden Berechtigungen für Ihren Shopify Shop:{::nomarkdown}<ul><li>Ladenbesitzer</li><li>Personal</li><li>Mitglied mit allen allgemeinen und Online-Shop-Einstellungen sowie diesen zusätzlichen Admin-Berechtigungen:<ul><li>Bestellungen</li><li>Ansicht (befindet sich unter <b>Produkte</b>)</li><li>Kund:in</li><li>Einstellungen verwalten</li><li>Von Mitarbeitern und Kollegen entwickelte Apps ansehen</li><li>Verwalten und installieren Sie Apps und Kanäle</li></ul></li></ul>{:/} |
| Braze Web SDK Implementierung | Um das Tracking von Onsite-Verhalten und anonymen Nutzer:innen zu ermöglichen, müssen Sie das Braze Web SDK entweder über unsere Standard Shopify-Integration oder manuell implementieren. <br><br>Weitere Informationen zu Ihren Implementierungsoptionen finden Sie unter [Implementierung des Internet SDK auf Ihrer Shopify-Website]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify). |
| Segmentierung der Eigenschaften von Ereignissen aktiviert | Um zu bestätigen, dass Sie die Eigenschaften Ihrer Shopify Events segmentieren können, arbeiten Sie mit Ihrem Customer-Success-Manager oder dem [Braze-Support]({{site.baseurl}}/braze_support/) zusammen, um sicherzustellen, dass die Segmentierung der Event-Eigenschaften für Ihr Braze-Dashboard aktiviert ist. |
{: .reset-td-br-1 .reset-td-br-2 }

## Allgemeine Datenschutzverordnung (DSGVO)

In Bezug auf personenbezogene Daten, die Braze von seinen Diensten oder im Namen seiner Kunden übermittelt werden, ist Braze der Datenverarbeiter und unsere Kunden sind die Datenverantwortlichen. Dementsprechend verarbeitet Braze solche persönlichen Daten ausschließlich auf Anweisung unserer Kund:in und benachrichtigt unsere Kund:in gegebenenfalls über Anfragen der Betroffenen. Als für die Datenverarbeitung Verantwortliche reagieren unsere Kund:innen direkt auf Anfragen von Betroffenen. Im Rahmen der Shopify-Integration der Braze-Plattform empfängt Braze automatisch [die DSGVO-Webhooks von Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). Braze-Kunden sind jedoch letztlich selbst dafür verantwortlich, auf Anfragen ihrer Shopify-Kunden über die Verwendung von [Braze SDKs]({{site.baseurl}}/developer_guide/home/) oder [REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) in Übereinstimmung mit unseren Richtlinien [zur Einhaltung der DSGVO]({{site.baseurl}}/dp-technical-assistance/) zu reagieren.
