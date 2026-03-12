---
nav_title: Datenquellen verbinden
article_title: Datenquellen verbinden
page_order: 1
description: "Erfahren Sie, wie Sie Kundendatenquellen mit BrazeAI Decisioning Studio Pro verbinden können, um personalisierte KI-Entscheidungen zu treffen."
---

# Datenquellen verbinden

> Die Mitarbeiter von BrazeAI Decisioning Studio™ Pro müssen den Kund:innen-Kontext vollständig verstehen, um effektive Entscheidungen treffen zu können. Dieser Artikel erläutert, wie Sie Kundendatenquellen mit Decisioning Studio Pro verbinden können.

{% alert tip %}
Ihr KI-Decisioning-Service-Team unterstützt Sie bei der Konfiguration von Datenverbindungen für optimale Performance.
{% endalert %}

## Unterstützte Muster für die Integration

Decisioning Studio Pro unterstützt mehrere Integrationsmuster für die Verknüpfung von Kundendaten:

| Integrationsmuster | Am besten für | Komplexität der Einrichtung |
|---------------------|----------|------------------|
| **Braze-Datenplattform** | Kund:innen, die Braze bereits nutzen | Niedrig |
| **Braze Cloud-Datenaufnahme (CDI)** | Anbindung externer Data Warehouses | Medium |
| **Cloud-Speicher (GCS, AWS, Azure)** | Direkter Export von Daten von anderen Plattformen | Medium |
| **CEP-Integrationen** | SFMC, Klaviyo-Daten-Erweiterungen | Medium |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Kundendaten

Die folgenden Kundendaten helfen den Mitarbeitern, die Personalisierung effektiver zu gestalten:

| Datentyp | Beschreibung | Beispiele |
|-----------|-------------|----------|
| **Kundenprofil** | Statische und sich langsam verändernde Attribute | Kund:in in Jahren, geografische Lage, Akquisitionskanal, Zufriedenheitsgrad, geschätzter Lifetime-Value |
| **Kundenverhalten** | Aktivitäts- und Engagementmuster | Anmeldungen für Konten, Gerätetyp, Interaktionen mit dem Kundendienst, Nutzung von Produkten |
| **Verlauf der Transaktionen** | Kauf- und Konversion-Daten | Erworbene Produkte, Transaktionsbeträge, Zahlungsmethoden, Einkaufskanäle |
| **Marketing-Engagement** | Antworten auf Mitteilungen | E-Mail-Öffnungen/Klicks, SMS-Engagement, Internet- und Mobilaktivitäten, Umfrageantworten |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
Je mehr Informationen die Mitarbeiter über Ihre Kund:innen haben, desto besser wird die Performance sein. Bitte erwägen Sie, Daten zu allen Insights aufzunehmen, die für Ihr Unternehmen besonders wichtig sind (möchten Sie beispielsweise wissen, wie KI Ihre Stammkunden anders behandelt? Bitte stellen Sie sicher, dass der Treuestatus in den Kundendaten vermerkt ist.
{% endalert %}

## Daten nach Plattform verbinden

{% tabs %}
{% tab Braze %}

### Kundendaten über Braze senden

BrazeAI Decisioning Studio kann alle Daten nutzen, die Sie bereits an die Braze-Datenplattform senden.

Sollten Sie Kundendaten für Decisioning Studio verwenden wollen, die derzeit nicht im Nutzerprofil oder in benutzerdefinierten Attributen gespeichert sind, empfehlen wir Ihnen, [Braze Cloud Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) zu verwenden, um Daten aus anderen Quellen zu importieren.

CDI unterstützt direkte Integrationen mit:

- Snowflake
- Rotverschiebung
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Die vollständige Liste der unterstützten Datenquellen finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Sobald Sie mit den Daten, die Sie an die Braze-Datenplattform senden, zufrieden sind, wenden Sie sich bitte an Ihr AI Decisioning Services-Team, um zu besprechen, welche Felder des Benutzerprofils oder angepassten Attribute für AI Decisioning verwendet werden sollen.

Um diesen Prozess zu optimieren, erstellen Sie bitte eine Liste mit Braze-Nutzerprofil-Attributen, die Ihrer Meinung nach das Kundenverhalten am besten widerspiegeln und die in Decisioning Studio verwendet werden sollten (siehe [Liste der verfügbaren Felder]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Ihr Team für Serviceleistungen kann Ihnen auch bei der Durchführung von Discovery-Sitzungen behilflich sein, um zu entscheiden, welche Felder für KI-Entscheidungen am besten geeignet sind.

Weitere Optionen zum Senden von Daten umfassen:

- Versenden von angepassten Braze-Events über das SDK
- Senden von Ereignissen über den REST-Endpunkt ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Diese Muster erfordern einen höheren technischen Aufwand, sind jedoch je nach Ihrer aktuellen Braze-Konfiguration unter Umständen vorzuziehen. Bitte wenden Sie sich an das Team für KI-Entscheidungsdienste, um weitere Informationen zu erhalten.

{% endtab %}
{% tab SFMC %}

### Kundendaten über SFMC senden

Für Salesforce Marketing Cloud-Integrationen:

1. Konfigurieren Sie SFMC-Datenerweiterungen für Ihre Kundendaten.
2. Richten Sie das installierte SFMC-Paket für die API-Integration mit den entsprechenden Berechtigungen ein, die von Decisioning Studio benötigt werden.
3. Bitte stellen Sie sicher, dass die Daten-Erweiterungen täglich aktualisiert werden, da Decisioning Studio die neuesten verfügbaren inkrementellen Daten abruft.

Bitte geben Sie die Erweiterungs-ID und den API-Schlüssel an Ihr AI Decisioning Services-Team weiter. Sie werden bei den nächsten Schritten zur Erfassung von Kundendaten behilflich sein.

{% endtab %}
{% tab Klaviyo %}

### Kundendaten über Klaviyo senden

Für Klaviyo-Integrationen:

1. Bitte bestätigen Sie, dass die Daten zum Kundenprofil in den Klaviyo-Profilen verfügbar sind.
2. Erstellen Sie einen privaten API-Schlüssel mit Vollzugriff auf Profile.
3. Bitte übermitteln Sie den API-Schlüssel an Ihr AI Decisioning Services-Team.

Weitere Informationen zur Einrichtung des API-Schlüssels finden Sie in der [Klaviyo-Dokumentation.](https://help.klaviyo.com/hc/en-us/articles/115005237908)

{% endtab %}
{% tab Cloud Storage %}

### Andere Cloud-Lösungen (Google Cloud Storage, Azure, AWS)

Sollten Kundendaten derzeit nicht in Braze, SFMC oder Klaviyo gespeichert sein, empfiehlt es sich, einen automatisierten Export direkt in einen von Braze verwalteten Google Cloud Storage-Bucket zu konfigurieren. Wir unterstützen auch den Export zu AWS oder Azure (obwohl GCS vorzuziehen ist). Für diese Plattformen erfolgt der Export in den internen Cloud-Speicher dieser Cloud-Plattformen, und Braze kann diese Daten anschließend abrufen.

Um festzustellen, ob dies möglich ist, referenzieren Sie bitte die Dokumentation Ihrer MarTech-Plattform. Zum Beispiel:

- mParticle bietet eine [native Integration mit Google Cloud Storage.](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio-Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Falls dies machbar ist, können wir einen GCS-Bucket zur Verfügung stellen, in den Kundendaten exportiert werden können, der von Decisioning Studio isoliert ist.

{% endtab %}
{% endtabs %}

## Bewährte Praktiken

- **Beschreibende Spaltennamen**: Kundendaten sollten eindeutige, beschreibende Spaltennamen aufweisen. Idealerweise sollte ein Wörterbuch für Daten bereitgestellt werden.
- **Inkrementelle Updates**: Inkrementelle Dateien sind gegenüber täglichen Snapshots des gesamten Verlaufs der Kund:innen vorzuziehen.
- **Konsistente Bezeichner**: Jeder Datensatz muss einen eindeutigen Bezeichner für den Kunden enthalten, der über alle Datenbestände hinweg konsistent ist.
- **Zeitstempel einfügen**: Aufzeichnungen sollten mit Zeitstempeln versehen sein, um genaue Attributionen und Schulungen der Mitarbeiter zu ermöglichen.

## Angepasste Integrationen

Weitere Optionen oder vollständig angepasste Datenpipelines sind möglich. Dies kann zusätzliche Serviceleistungen oder technische Arbeiten seitens Ihres Teams erfordern. Um zu ermitteln, was machbar und optimal ist, arbeiten Sie bitte mit Ihrem KI-Entscheidungsdienst-Team zusammen.

{% alert important %}
Dieser Leitfaden erläutert die gängigsten Muster für Integrationen. Die Informationssicherheit muss weiterhin alle Verbindungspunkte überprüfen, und Lösungsberater stehen für die Beratung bei der Implementierung zur Verfügung.
{% endalert %}

## Nächste Schritte

Nachdem Sie Ihre Datenquellen verbunden haben, fahren Sie mit der Einrichtung der Orchestrierung fort:

- [Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

