---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Personalize.AI, einer KI-basierten SaaS-Geschäftsplattform, die das Umsatzwachstum durch personalisierte Empfehlungen fördert."
alias: /partners/personalize/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) ist Partner von Braze, um durch die Zustellung von personalisierten Nachrichten und Angeboten, die über Braze zugestellt werden, zusätzliche Umsätze zu generieren. 

Die Integration von Braze und Personalize.AI erlaubt es Ihnen, Daten von Personalize.AI in die Braze-Plattform zu exportieren, um Nachrichten zu personalisieren und zu targetieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Personalize.AI Instanz | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie eine Instanz von Personalize.AI. |
| Braze REST API-Schlüssel | Ein REST-API-Schlüssel von Braze mit allen Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][1] ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

* Setzen Sie Tests ein, einschließlich flexibler Stratifizierung, um die Ergebnisse aus dem Feedback von Kund:in zu verbessern.
* Geben Sie personalisierte Empfehlungen für Artikel und Angebote, einschließlich Behandlung, Zeitpunkt und Inhalt.
* Identifizieren Sie priorisierte Ziele und targeting Sie Ihre optimale Zielgruppe durch Braze
* Identifizieren Sie Opportunitäten zur erneuten Interaktion mit ausgefallenen Nutzer:innen
* Nutzen Sie Geolocation-Daten, um die richtige Zielgruppe für neu geöffnete Standorte zu finden
* Nutzen Sie die Lookalike-Modellierung, um auf den begrenzten Daten für neuere Nutzer:innen aufzubauen und sie mit den relevantesten Empfehlungen abzugleichen.
* Identifizieren Sie die richtigen Wege, um Kunden über ihren gesamten Kundenlebenszyklus hinweg zu engagieren. 
* Bewerten Sie proaktiv die Wahrscheinlichkeit, dass Kunden abwandern, und weisen Sie einen Risikoscore zu, um Frühindikatoren für die Abwanderung zu finden.
* Targeting von Kunden mit personalisierten Interventionen, um zu verhindern, dass sie inaktiv werden

## Integration

### Konfigurieren Sie eine Verbindung mit Braze in Personalize.AI

1. Navigieren Sie unter Personalize.AI in Ihrer Instanz Personalize.AI zum Tab **Integrationen**, der sich unter **Operationalisierung** befindet.
2. Klicken Sie auf **Braze**. 
3. Konfigurieren Sie Ihre Integration mit Braze.
    * **Name der Verbindung:** Nennen Sie Ihre Verbindung. Auf diese Weise wird Ihre Integration in Personalize.AI referenziert.
    * **Synchronisationsfrequenz:** Die Synchronisierungsfrequenz steuert, wie oft Personalize.AI Daten nach Braze exportiert. Wählen Sie **Täglich**, **Wöchentlich** oder **Monatlich**. 
    * **API-Schlüssel:** Fügen Sie Ihren Braze API-Schlüssel hinzu.
    * **API URL:** Fügen Sie die URL Ihres Braze REST-Endpunkts hinzu.
4. Klicken Sie auf **EXPORT**, um Daten nach Braze zu exportieren.

Sobald Ihre Daten exportiert wurden, wird Personalize.AI weiterhin Daten in den Intervallen an Braze weitergeben, die durch die von Ihnen während der Integration festgelegte Synchronisierungsfrequenz bestimmt werden.

## Verwendung dieser Integration

Personalize.AI exportiert Bezeichner für das personalisierte Targeting in Braze. Diese angepassten Attribute geben den Zeitpunkt, den Inhalt, die Behandlung und die Angebote für jede Kund:in an. Je nach Integration können Felder als Event übergeben oder in die [Connected-Content-APIs][2] gezogen werden, anstatt im Profil des Kunden gespeichert zu werden. Personalize.AI unterstützt die Verwendung von `external_id` als Bezeichner.

Die in Braze importierten Datenattribute sind für die Verwendung in Canvase intuitiv benannt und folgen einer einheitlichen Terminologie. Zum Beispiel würde das Attribut `C402_Target_Variant` in Personalize.AI als `"P.AI_Model_Treatment"` nach Braze exportiert werden. Die von Personalize.AI exportierten Attribute sind so konzipiert, dass sie nicht mit bestehenden Attributen oder dem von Ihnen verwendeten Tracking kollidieren. Diese Attribute werden ständig überprüft, damit Sie sie sicher referenzieren können. 

Hier sehen Sie zum Beispiel eine Reihe von Attributen von Kund:in, die sich auf ein beispielhaftes, auf Abwanderung ausgerichtetes Canvas beziehen.

| Personalize.AI Attribut | Wert |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Behandlung |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Caesar Salat" |
| `C4_Subject_Line` | "Wir vermissen Sie" |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/
