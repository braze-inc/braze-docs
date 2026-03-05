---
nav_title: Okendo
article_title: "Okendo"
description: "Erfahren Sie, wie Sie Okendo in Braze integrieren können."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) ist eine einheitliche Plattform für das Kundenmarketing, die Tools zur Pflege der Kundenbindung, zum Ausbau der Mundpropaganda und zur Maximierung des Lifetime-Value bietet, um Ihre Kunden für ein schnelleres und effizienteres Wachstum zu mobilisieren.

*Diese Integration wird von Okendo gepflegt.*

## Über die Integration

Die Integration von Braze in Okendo funktioniert über mehrere Produkte der Okendo-Plattform, darunter Bewertungen, Loyalität, Empfehlungen, Umfragen und Quizze. Okendo sendet angepasste Events und Nutzer-Attribute an Braze, die zur Personalisierung und zum Triggern von Nachrichten verwendet werden können.  

## Voraussetzungen

| Anforderung            | Beschreibung                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Okendo Konto         | Um diese Partnerschaft zu nutzen, benötigen Sie ein Okendo-Konto.        |
| Braze REST API-Schlüssel     | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt    | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Braze Konnektor in Okendo einrichten

1. Gehen Sie in Okendo zu **Einstellungen** > **Integrationen** > **E-Mail & SMS** > **Braze**
2. Fügen Sie den API-Endpunkt und API-Schlüssel zu den **Integrationseinstellungen** hinzu.

### Schritt 2: Konfigurieren Sie Ihren Bezeichner

Das Feld `external_id` dient zur Identifizierung des Nutzers:innen, der mit jedem Ereignis verbunden ist. Schalten Sie **Shopify Customer ID für die Identifizierung von Shopify Nutzern**: **innen** ein, um das Feld mit Shopify Kunden:innen zu verknüpfen. Andernfalls schalten Sie es aus, um es mit den E-Mail-Adressen der einzelnen Nutzer:innen zu verknüpfen.

## Synchronisierung von Okendo Ereignissen und Attributen mit Braze

### Angepasste Events

{% alert note %}
Ein Beispiel für Ereignisdaten finden Sie in [der Dokumentation von Okendo.](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c)
{% endalert %}

#### Ereignisse überprüfen

- Okendo Rezension erstellt
- Okendo Review Anfrage

#### Empfehlung von Veranstaltungen

- Gesendete Okendo Empfehlung
- Opt-in für Okendo-Empfehlungen
- Okendo Empfehlung Einladung
- Okendo-Empfehlungsgutschein erhalten
- Eingelöster Okendo Empfehlungsgutschein
- Okendo Empfehlung Abgelehnt

#### Loyalitätsveranstaltungen

- Eingeschrieben bei Okendo Loyalty
- Vergebene Okendo-Treuepunkte
- Eingelöste Okendo-Treuepunkte
- Okendo Loyalty Tier Geändert
- Okendo Treuepunkte Adjusted

#### Umfrage Ereignis

- Eingereichte Okendo Umfrage

#### Quiz-Veranstaltung

- Eingereichtes Okendo Quiz

### Angepasste Attribute

Okendo sendet Nutzerprofil-Daten als angepasste Attribute in Braze, die zur Segmentierung der Zielgruppe verwendet werden können. Beispiele hierfür sind:

- Profilfragen, die in Umfragen und bei der Einreichung einer Bewertung gestellt werden, wie Alter, Geburtstag, Hauttyp und Haarfarbe
- Metriken wie die _durchschnittliche Bewertung der Rezensionen_ und die _durchschnittliche Meinung zu den Rezensionen_
- Metriken zur Loyalität wie _Punktesaldo_ und _VIP-Stufe_
- Metriken für Empfehlungen wie die _Anzahl der erfolgreichen Empfehlungen_ und die _Gesamteinnahmen aus Empfehlungen_  
- NPS-Punkte aus einer Umfrage

## Verwendung von Braze mit Okendo Produkten

Je nach Okendo-Produkt müssen Sie zusätzliche Schritte durchführen, um Braze und Okendo zusammen zu verwenden. Lesen Sie die folgenden Artikel für weitere Einzelheiten:

- [Integration von Bewertungen in Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Integration von Loyalty mit Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Integration von Empfehlungen mit Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Integration von Umfragen mit Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Integration von Quizzes mit Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
Wenn Sie Hilfe bei der Konfiguration der Integration benötigen, wenden Sie sich an das Okendo Support Team.
{% endalert %}
