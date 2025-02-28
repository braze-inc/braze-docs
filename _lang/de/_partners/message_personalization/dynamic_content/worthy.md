---
nav_title: Worthy
article_title: Worthy
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Worthy, einer Plattform zur Personalisierung von Nachrichten, die es Ihnen ermöglicht, personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zu liefern."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> Die Integration von [Worthy](https://worthy.ai/) und Braze ermöglicht es Ihnen, mit dem Drag-and-Drop-Editor von Worthy auf einfache Weise personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze bereitzustellen. Außerdem wird Worthy automatisch Folgendes tun:

- Erstellen Sie einen Connected Content Server und eine gesicherte API für Ihre Nachrichtenübermittlung.
- Erstellen Sie Ihre In-App-Nachrichten mit Analysen und Klick-Tracking, die direkt in Braze angezeigt werden.
- Exportieren Sie automatisch HTML über den Drag-and-Drop-Editor von Worthy zur Verwendung in **Custom Code** In-App-Nachrichtenkampagnen in Braze, komplett mit den erforderlichen API-Verbindungen und dynamischen Inhalten, die Sie konfigurieren.

## Anwendungsfälle

- Individuelle Begrüßungserlebnisse auf der Grundlage der vom Benutzer beim Onboarding getroffenen Auswahl
- In-App-Erlebnisse für besondere Ereignisse und Werbeaktionen
- Sammeln von Kundenfeedback und Bewertungen basierend auf dem App-Verhalten
- Schnelles Testen potenzieller App-Produktideen
- Reichhaltige Mitteilungen, Nachrichten und Community-Updates

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| [Würdiges](https://worthy.ai/) Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Worthy-Konto. |
| Braze SDK | Sie müssen das Braze SDK in Ihrer mobilen Anwendung konfigurieren, um Rich-In-App-Nachrichten zu versenden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie personalisierte Nachrichten in Worthy

Navigieren Sie zu Ihrer App im Worthy Dashboard, wählen Sie den **Message Creator** und erstellen Sie eine personalisierte Nachricht, mit der Sie Ihre Nutzer ansprechen möchten.

### Schritt 2: Erstellen Sie eine Braze-Kampagne

Erstellen Sie eine [In-App-Nachrichtenkampagne]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) in Braze und setzen Sie den **Nachrichtentyp** auf **Custom Code**.

### Schritt 3: Kopieren Sie Ihre personalisierte Nachricht in Braze

Klicken Sie im Worthy message creator auf **Exportieren** und wählen Sie **Braze**, um Ihre personalisierte Nachricht zur Verwendung in Braze-Kampagnen zu exportieren. Kopieren Sie den exportierten Inhalt in das HTML-Textfeld unter **HTML + Asset Zip** im Braze-Kampagneneditor.

Das war's! Sie können Ihre personalisierte Nachricht sofort testen, indem Sie die Registerkarte **Test** im Braze-Kampagneneditor verwenden. 
