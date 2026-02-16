---
nav_title: Datenquellen verbinden
article_title: Datenquellen verbinden
page_order: 1
description: "Erfahren Sie, wie Sie Datenquellen von Kund:in mit BrazeAI Decisioning Studio Pro verbinden, um personalisierte KI-Entscheidungen zu treffen."
---

# Datenquellen verbinden

> Die Agenten von BrazeAI Decisioning Studio™ Pro müssen den Kontext der Kund:in vollständig verstehen, um effektive Entscheidungen treffen zu können. Dieser Artikel erklärt, wie Sie Kundendatenquellen mit Decisioning Studio Pro verbinden.

{% alert tip %}
Ihr Team von KI Decisioning Serviceleistungen; Dienste; Dienste unterstützt Sie bei der Konfiguration von Datenverbindungen für optimale Performance.
{% endalert %}

## Unterstützte Integrationsmuster

Decisioning Studio Pro unterstützt mehrere Integrationsmuster für die Verbindung von Kundendaten:

| Integration Muster | Am besten für | Komplexität der Einrichtung |
|---------------------|----------|------------------|
| **Braze-Datenplattform** | Kunden, die Braze bereits verwenden | Niedrig |
| **Braze Cloud-Datenaufnahme (CDI)** | Verbindung mit externen Data Warehouses | Medium |
| **Cloud-Speicher (GCS, AWS, Azure)** | Direkte Datenexporte von anderen Plattformen | Medium |
| **CEP-Integrationen** | SFMC, Klaviyo Daten-Erweiterungen | Medium |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Kundendaten-Typen

Die folgenden Kundendaten helfen den Agenten, die Personalisierung effektiver zu gestalten:

| Datentyp | Beschreibung | Beispiele |
|-----------|-------------|----------|
| **Kundenprofil** | Statische und sich langsam verändernde Attribute | Jahre als Kund:in, Geographie, Akquisitionskanal, Zufriedenheitsgrad, Lifetime-Value-Schätzung |
| **Kundenverhalten** | Aktivitäts- und Engagement-Muster | Kontoanmeldungen, Gerätetyp, Interaktionen mit dem Kund:in, Produktnutzung |
| **Verlauf der Transaktionen** | Daten zum Kauf und zur Konversion | Gekaufte Produkte, Transaktionsbeträge, Zahlungsarten, Kanäle für den Kauf |
| **Marketing Engagement** | Antworten auf Mitteilungen | E-Mail-Öffnungen/Klicks, SMS-Engagement, Internet- und Handy-Aktivitäten, Antworten auf Umfragen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
Je mehr Informationen die Agenten über Ihre Kund:innen haben, desto besser wird ihre Performance sein. Erwägen Sie, Daten zu Insights einzubeziehen, die für Ihr Unternehmen besonders wichtig sind (möchten Sie z.B. sehen, wie KI Ihre treuen Kunden anders behandelt? Stellen Sie sicher, dass der Treuestatus in den Kundendaten enthalten ist).
{% endalert %}

## Daten nach Plattform verknüpfen

{% tabs %}
{% tab Braze %}

### Senden Sie Kundendaten über Braze

BrazeAI Decisioning Studio kann alle Daten verwenden, die Sie bereits an die Braze Data Platform senden.

Wenn Sie Kundendaten für Decisioning Studio verwenden möchten, die derzeit nicht im Nutzerprofil oder in angepassten Attributen gespeichert sind, empfiehlt sich die Verwendung von [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) zur Aufnahme von Daten aus anderen Quellen.

CDI unterstützt direkte Integrationen mit:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Die vollständige Liste der unterstützten Datenquellen finden Sie unter [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Wenn Sie mit den Daten, die Sie an die Braze Data Platform senden, zufrieden sind, wenden Sie sich an Ihr Team für Serviceleistungen; Dienste, um zu besprechen, welche Felder des Nutzerprofils oder angepasste Attribute für die KI-Entscheidungsfindung verwendet werden sollen.

Um diesen Prozess zu rationalisieren, erstellen Sie eine Liste der Attribute des Braze Nutzerprofils, die Ihrer Meinung nach das Verhalten Ihrer Kund:innen am besten repräsentieren und in Decisioning Studio verwendet werden sollen (siehe [Liste der verfügbaren Felder]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Ihr Team für Serviceleistungen; Dienste kann Ihnen auch bei der Durchführung von Discovery-Sitzungen helfen, um zu entscheiden, welche Felder sich am besten für KI Decisioning eignen.

Weitere Optionen zum Senden von Daten sind:

- Senden von angepassten Braze Events über das SDK
- Das Senden von Ereignissen über den REST-Endpunkt ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Diese Muster erfordern mehr technischen Aufwand, sind aber je nach Ihrer aktuellen Braze-Konfiguration manchmal vorzuziehen. Wenden Sie sich an das Team von KI Decisioning Serviceleistungen; Dienste; Dienste, um mehr zu erfahren.

{% endtab %}
{% tab SFMC %}

### Senden Sie Kundendaten über SFMC

Für Salesforce Marketing Cloud Integrationen:

1. Konfigurieren Sie SFMC Data Extension(s) für Ihre Kundendaten
2. Richten Sie das installierte SFMC-Paket für die API-Integration mit den entsprechenden Berechtigungen ein, die von Decisioning Studio benötigt werden.
3. Stellen Sie sicher, dass die Datenerweiterungen täglich aktualisiert werden, da Decisioning Studio die neuesten verfügbaren inkrementellen Daten verwendet.

Geben Sie die ID der Erweiterung und den API-Schlüssel an Ihr Team von KI Decisioning Serviceleistungen; Dienste; Dienste weiter. Sie unterstützen Sie bei den nächsten Schritten zur Aufnahme von Kundendaten.

{% endtab %}
{% tab Klaviyo %}

### Senden Sie Kundendaten über Klaviyo

Für Klaviyo-Integrationen:

1. Bestätigen Sie, dass die Daten des Kundenprofils in den Klaviyo-Profilen verfügbar sind.
2. Generieren Sie einen privaten API-Schlüssel mit Vollzugriff auf Profile
3. Stellen Sie Ihrem Team von KI Decisioning Serviceleistungen; Dienste; Dienste den API-Schlüssel zur Verfügung

Weitere Informationen zur Einrichtung von API-Schlüsseln finden Sie in der [Dokumentation von Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908).

{% endtab %}
{% tab Cloud Storage %}

### Andere Cloud-Lösungen (Google Cloud Storage, Azure, AWS)

Wenn Kundendaten derzeit nicht in Braze, SFMC oder Klaviyo gespeichert sind, ist der nächste beste Schritt die Konfiguration eines automatisierten Exports direkt in einen von Braze kontrollierten Google Cloud Storage Bucket. Wir können auch den Export nach AWS oder Azure unterstützen (obwohl GCS vorzuziehen ist). Für diese Plattformen exportieren Sie in den internen Cloud-Speicher dieser Plattformen und Braze kann diese Daten dann abrufen.

Ob dies möglich ist, entnehmen Sie bitte der Dokumentation Ihrer MarTech Plattform. Zum Beispiel:

- mParticle bietet eine [native Integration mit Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segmente](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Wenn dies möglich ist, können wir einen GCS Bucket für den Export von Kundendaten zur Verfügung stellen, der für Decisioning Studio isoliert ist.

{% endtab %}
{% endtabs %}

## Bewährte Praktiken

- **Beschreibende Spaltennamen**: Kundendaten sollten klare, beschreibende Spaltennamen haben. Idealerweise sollte ein Wörterbuch für die Daten zur Verfügung gestellt werden.
- **Inkrementelle Updates**: Inkrementelle Dateien sind besser als tägliche Schnappschüsse des gesamten Kund:in-Verlaufs.
- **Konsistente Bezeichner**: Jeder Datensatz muss einen eindeutigen Bezeichner für den Kunden enthalten, der für alle Daten konsistent ist.
- **Zeitstempel einschließen**: Datensätze sollten mit Zeitstempeln versehen sein, um eine genaue Attribution zu ermöglichen und Agenten zu trainieren.

## Angepasste Integrationen

Andere Optionen oder komplett angepasste Daten-Pipelines sind möglich. Diese können zusätzliche Serviceleistungen; Dienste oder Ingenieursarbeit von Ihrem Team erfordern. Um festzustellen, was machbar und optimal ist, arbeiten Sie mit Ihrem Team von KI Decisioning Serviceleistungen; Dienste; Dienste zusammen.

{% alert important %}
In diesem Leitfaden werden die gängigsten Integrationsmuster erläutert. Die Informationssicherheit muss noch alle Verbindungspunkte überprüfen, und die Solutions Consultants stehen Ihnen bei der Implementierung beratend zur Seite.
{% endalert %}

## Nächste Schritte

Nachdem Sie Ihre Datenquellen verbunden haben, fahren Sie mit dem Einrichten der Orchestrierung fort:

- [Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

