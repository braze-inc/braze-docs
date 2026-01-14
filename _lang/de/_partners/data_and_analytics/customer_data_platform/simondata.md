---
nav_title: Simon Data
article_title: Simon Data
description: "Nutzen Sie die Integration von Braze und Simon Data, um anspruchsvolle Zielgruppen für die Orchestrierung zu erstellen und mit Braze zu synchronisieren - in Realtime und ohne Code."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon Data

> [Simon Data](https://www.simondata.com) ist eine Customer Data Platform (CDP), die für Marketer freundlich ist und von Datenteams geschätzt wird. Durch die Transformation Ihres Data Warehouse in ein Marketing-Powerhouse sorgt Simon für bessere Geschäftsergebnisse und ein besseres Kundenerlebnis.

Nutzen Sie die Integration von Braze und Simon Data, um anspruchsvolle Zielgruppen für die Orchestrierung zu erstellen und mit Braze zu synchronisieren - in Realtime und ohne Code. Mit dieser Integration können Sie die besten Funktionen von Simon für die Priorisierung von Kampagnen und den Abgleich von Identitäten, die Unterstützung komplexer Aggregate und vieles mehr nutzen, um Ihre Kampagnen in Braze weiterzuentwickeln.

## Voraussetzungen

Um loszulegen, müssen Sie Ihr Braze-Konto innerhalb Ihres Simon Data-Kontos authentifizieren.

| Anforderung         | Beschreibung                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon Data          | Sie müssen über ein bestehendes Simon Data-Konto verfügen, um die Braze-Integration von Simon Data aus nutzen zu können.                                                                    |
| Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `campaigns.trigger.schedule.create`, und `campaigns.trigger.send`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Dashboard URL | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

- Triggern Sie ein Braze-Canvas oder eine E-Mail  
- Segmenteigenschaften weitergeben und pflegen
- Sync-Eigenschaften und Kontakt-Eigenschaften

{% alert note %}  
Wenn Sie die Integration von Simon und Braze verwenden, sendet Simon bei jeder Synchronisierung nur Deltas an Braze und vermeidet so Kosten für irrelevante Daten. Weitere Informationen finden Sie unter [Sync-Eigenschaften und Kontakteigenschaften](#sync-traits-and-contact-properties).
{% endalert %}

## Integration

### Authentifizieren Sie Ihr Braze-Konto in Simon

Um die Braze-Integration zu nutzen, authentifizieren Sie zunächst Ihr Braze-Konto in Simon:

1. Klicken Sie in der linken Navigation auf **Integrationen** und scrollen Sie dann zu Braze.
2. Geben Sie Ihren Braze [REST API-Schlüssel]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys) und Ihre [Dashboard-URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) ein.
3. Klicken Sie auf **Änderungen speichern**.

Bei einer erfolgreichen Verbindung wird im Fenster **Verbunden** angezeigt.

![Integration Bildschirm in Simon Data]({% image_buster /assets/img/simon_data/ConnecttoBraze.png %}){: style="max-width:70%"}

### Hinzufügen von Braze-Aktionen zu Flows oder Journeys in Simon

Nachdem Sie Ihr Braze-Konto in Simon authentifiziert haben, können Sie Braze-Aktionen zu [Flows](https://docs.simondata.com/docs/campaigns-flows) und [Journeys](https://docs.simondata.com/docs/campaigns-journeys-two) hinzufügen.

Es sind drei Aktionen verfügbar:

- **Sync Simon Segment Attribut**: Synchronisieren Sie die Details Ihrer Segmente mit einem neuen oder bereits vorhandenen angepassten Attribut in Braze.
- **Triggern Sie ein Braze-Canvas**: Triggern Sie ein Braze-Canvas, das die Daten Ihrer Simon Segmente nutzt.
- **Senden Sie eine Braze Kampagne**: Starten Sie eine komplette Braze-Kampagne von Simon aus.

![Dropdown-Liste mit den verfügbaren Braze-Aktionen in Simon Data.]({% image_buster /assets/img/simon_data/BrazeActions.png %}){: style="max-width:60%"}

Einige Aktionen sind nur für bestimmte Flussarten oder Reisen verfügbar. Erfahren Sie mehr unter [docs.simondata.com](https://docs.simondata.com).

### Eigenschaften und Kontakteigenschaften synchronisieren

Um den Datenverbrauch zu minimieren, können Sie bestimmte Merkmale auswählen, die standardmäßig synchronisiert werden sollen, anstatt jedes Feld für alle Kunden eines Segments zu aktualisieren.

{% alert note %}
Um mit der Synchronisierung von Traits zu beginnen, senden Sie eine Anfrage an das [Simon Support Center](https://docs.simondata.com/docs/support-center). Ihr Account Manager:in wird Ihnen mitteilen, wann Sie mit den folgenden Schritten fortfahren können.
{% endalert %}

Nachdem Contact Traits von Ihrem Account Manager:in aktiviert wurde:

1. Erweitern Sie in Simon das **Admin Center** in der linken Navigation und wählen Sie **Kontaktmerkmale synchronisieren**.
2. Wählen Sie **Braze**. Hier werden die Eigenschaften der Kontakte angezeigt, verschachtelt nach Datensatz.
3. Wählen Sie die Felder aus, die Sie bei der Integration von Simon und Braze synchronisieren möchten:
   1. **Die Anzahl der Merkmale** gibt an, wie viele Merkmale in diesem Datensatz zur Auswahl stehen. Sie können alle auswählen oder die Zeile erweitern, um einzelne Felder auszuwählen.
   2. Bearbeiten Sie den **Downstream-Namen**, wenn Sie möchten, dass die Feldnamen bei ihrer Ankunft in Braze anders aussehen.
   3. Wenn dies Ihre erste Integration mit Braze von Simon aus ist, klicken Sie auf **Alle Kontakte zurücksetzen**. Backfilling sendet alle Datenpunkte an Braze, wenn Sie eine Aktion in einem Fluss oder einer Reise zum ersten Mal verwenden, um sicherzustellen, dass alle Daten vollständig synchronisiert sind. Bei späteren Synchronisierungen werden dann nur die Eigenschaften, die Sie in diesem Bildschirm auswählen, an Braze gesendet. So stellen Sie sicher, dass Ihnen nur die Daten in Rechnung gestellt werden, die Sie benötigen.

![Auswählen von Synchronisationsmerkmalen in Simon Data.]({% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %})





