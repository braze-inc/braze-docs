---
nav_title: Konstrukteur
article_title: Konstrukteur
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Constructor. Diese Partnerschaft erlaubt es Ihnen, Constructors Offsite Product Discovery zu nutzen, um dynamisch personalisierte Produktempfehlungen in Nachrichten von Braze zu erstellen und zuzustellen."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Konstrukteur

> [Constructor](https://constructor.com/) ist eine Such- und Produktentdeckungsplattform, die KI und maschinelles Lernen einsetzt, um personalisierte Suchen, Empfehlungen und Browsing-Erlebnisse für E-Commerce- und Einzelhandels-Websites bereitzustellen.

Mit der Integration von Braze und Constructor können Sie die Offsite Product Discovery von Constructor nutzen, um dynamisch personalisierte Produktempfehlungen in Nachrichten von Braze zu erstellen und zuzustellen.

## Anwendungsfälle

- **Nachverfolgung von Warenkorb-Abbrüchen und Nachbestellungen**: Erzeugen Sie dynamische Produktempfehlungen auf der Grundlage des Nutzer:innen-Verhaltens und des Inhalts Ihres Warenkorbs, um personalisierte Erinnerungen an abgebrochene Einkäufe oder Vorschläge für Nachbestellungen zu versenden.
- **Ähnliche Produktempfehlungen für Artikel, die im Warenkorb-Abbruch liegen**: Schlagen Sie ähnliche Produkte zu Artikeln im Warenkorb eines Nutzers:innen vor, um das Engagement des Nutzers zu erhalten und Alternativen anzubieten.
- **Erinnerungen an kürzlich angesehene Artikel**: Benachrichtigen Sie Nutzer:innen über Artikel, die sie kürzlich angesehen, aber noch nicht gekauft haben, und ermutigen Sie sie so, ihren Kauf abzuschließen.
- **Kampagnen**: Versenden Sie personalisierte Nachrichten mit kuratierten Produktempfehlungen, die auf die Präferenzen der Nutzer:innen zugeschnitten sind, für saisonale Verkäufe oder Sonderangebote.
- **Visuell ähnliche Produktvorschläge**: Empfehlen Sie visuell ähnliche Artikel wie die, die ein Nutzer:innen kürzlich angesehen hat, und helfen Sie ihm, verwandte Optionen zu entdecken, die er bevorzugen könnte.

## Voraussetzungen

| Anforderung | Beschreibung |
|-------------|-------------|
| Konstrukteur-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Constructor-Konto, in dem der Dienst Offsite Discovery aktiviert ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Arbeiten Sie mit Ihrem Constructor Onboarding Team zusammen, um den Integrationsprozess abzuschließen. Stellen Sie sicher, dass Verhaltensdaten von Ihrer Website oder anderen relevanten Datenquellen verfügbar sind, um personalisierte Produktempfehlungen zu ermöglichen. Ihr Onboarding Team von Constructor hilft Ihnen auch bei der Konfiguration der notwendigen HTML Snippets für die Verwendung in Messaging Nachrichten.

## Offsite Discovery API URL des Konstrukteurs

Sie können die Offsite Discovery API URL von Constructor verwenden, um Produktbilder zu rendern und Nutzer:innen auf die entsprechende Produktdetailseite zu leiten. Im Folgenden finden Sie eine Aufschlüsselung der Struktur des Endpunkts und ein Beispiel für seine Verwendung:

### Beispiel

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img 
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200" 
    border="0" 
    alt="Shop Now" 
  />
</a>
```

### Parameter

| Parameter | Beschreibung |
|-------------|-------------|
| `position` | Verweist auf die Rangfolge des spezifischen empfohlenen Artikels innerhalb der Vorschlagsliste (z.B. `position = 2`). <br>![Rangfolge der Artikel.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Stellt den Bezeichner des Nutzers:in dar, der für die Personalisierung der Empfehlungsergebnisse entscheidend ist. Legen Sie den Parameter `ui` als `external_id` der Kund:in in Braze fest. Wenn Sie diese Option auslassen, gibt Constructor allgemeine Empfehlungen anstelle von Nutzer:innen zurück. |
| `pod_id` | Bezeichner für den Pod, der die Strategie und die Suchregeln für Empfehlungen enthält (z.B. erzeugt ein Pod mit einer Bestseller-Strategie personalisierte Bestseller). |
| `key` | Der Constructor-Indexschlüssel für diese Kund:in. |
| `style_id` | Legt fest, welche Bilder für die Produktkarte angezeigt werden. Zum Beispiel zeigen verschiedene `style_ids` eindeutige Produktkartenbilder an. |
| `campaign_id` | Eindeutige ID für die E-Mail Kampagne. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Optionale Eingänge

| Eingabe | Beschreibung |
|-------------|-------------|
| `item_id` | Stellt den Artikel des Saatguts dar. Notwendig für Artikel-basierte Strategien, wie z.B. alternative, ergänzende, Bündel. Zum Beispiel ist der erste Artikel in einer E-Mail der Startartikel, die nachfolgenden Artikel sind Alternativen. |
| `num_results` | Anzahl der Produkte, die der E-Mail hinzugefügt werden sollen. Der Standardwert ist 10, bis zu 100. Zum Beispiel bedeutet `num_results = 3`, dass drei Empfehlungen hinzugefügt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

