---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Personalize.AI, einer KI-basierten SaaS-Geschäftsplattform, die das Umsatzwachstum durch personalisierte Empfehlungen fördert."
alias: /partners/personalize/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) arbeitet mit Braze zusammen, um zusätzliche Umsätze durch personalisierte Nachrichten und Angebote zu generieren, die über Braze verschickt werden. 

Die Integration von Braze und Personalize.AI ermöglicht es Ihnen, Daten von Personalize.AI in die Braze-Plattform zu exportieren, um Nachrichten zu personalisieren und gezielt zu versenden.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Personalize.AI Instanz | Um die Vorteile dieser Partnerschaft zu nutzen, ist eine Personalize.AI Instanz erforderlich. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][1] ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

* Führen Sie Tests durch, einschließlich flexibler Stratifizierung, um Ergebnisse aus Kundenfeedback zu erzielen.
* Geben Sie personalisierte Empfehlungen für Artikel und Angebote, einschließlich Behandlung, Zeitpunkt und Inhalt.
* Identifizieren Sie priorisierte Ziele und sprechen Sie Ihr optimales Publikum mit Braze an.
* Identifizieren Sie Gelegenheiten, um ausgeschiedene Benutzer wieder einzubinden
* Nutzen Sie Geodaten, um die richtige Zielgruppe für neu eröffnete Standorte zu finden.
* Nutzen Sie die Lookalike-Modellierung, um auf den begrenzten verfügbaren Daten für neuere Nutzer aufzubauen und sie mit den relevantesten Empfehlungen abzugleichen.
* Identifizieren Sie die richtigen Wege, um Kunden während ihres gesamten Lebenszyklus einzubinden. 
* Bewerten Sie proaktiv die Abwanderungswahrscheinlichkeit von Kunden und weisen Sie ihnen eine Risikobewertung zu, um Frühindikatoren für die Abwanderung zu finden.
* Richten Sie sich mit personalisierten Interventionen an Kunden, um zu verhindern, dass sie inaktiv werden.

## Integration

### Konfigurieren Sie eine Verbindung mit Braze in Personalize.AI

1. Navigieren Sie unter Personalize.AI in Ihrer Instanz Personalize.AI zur Registerkarte **Integrationen**, die sich unter **Operationalisierung** befindet.
2. Klicken Sie auf **Hartlöten**. 
3. Konfigurieren Sie Ihre Integration mit Braze.
    * **Name der Verbindung:** Nennen Sie Ihre Verbindung. Auf diese Weise wird Ihre Integration in Personalize.AI bezeichnet.
    * **Synchronisationsfrequenz:** Die Synchronisierungsfrequenz steuert, wie oft Personalize.AI Daten nach Braze exportiert. Wählen Sie **Täglich**, **Wöchentlich** oder **Monatlich**. 
    * **API-Schlüssel:** Fügen Sie Ihren Braze API-Schlüssel hinzu.
    * **API-URL:** Fügen Sie die URL Ihres Braze REST-Endpunkts hinzu.
4. Klicken Sie auf **EXPORT**, um Daten nach Braze zu exportieren.

Sobald Ihre Daten exportiert wurden, überträgt Personalize.AI die Daten weiterhin in den Intervallen an Braze, die durch die von Ihnen bei der Integration festgelegte Synchronisierungsfrequenz bestimmt werden.

## Mit dieser Integration

Personalize.AI exportiert Identifikatoren, die für personalisiertes Targeting verwendet werden, in Braze. Diese benutzerdefinierten Attribute geben den Zeitpunkt, den Inhalt, die Behandlung und die Angebote für jeden Kunden an. Je nach Integration können Felder als Ereignis übergeben oder in die [Connected Content APIs][2] gezogen werden, anstatt im Kundenprofil gespeichert zu werden. Personalize.AI unterstützt die Verwendung von `external_id` als Bezeichner.

Die in Braze importierten Datenattribute sind für die Verwendung in Canvases intuitiv benannt und folgen einer einheitlichen Terminologie. Zum Beispiel würde das Attribut `C402_Target_Variant` in Personalize.AI als `"P.AI_Model_Treatment"` nach Braze exportiert werden. Die von Personalize.AI exportierten Attribute sind so konzipiert, dass sie nicht mit bereits vorhandenen Attributen oder der von Ihnen verwendeten Nachverfolgung interferieren. Diese Attribute werden laufend überprüft, damit Sie sich darauf verlassen können. 

Hier ist zum Beispiel eine Reihe von Kundenattributen, die sich auf ein Beispiel für ein auf Abwanderung ausgerichtetes Canvas beziehen.

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
