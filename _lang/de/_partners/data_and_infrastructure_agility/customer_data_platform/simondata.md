---
nav_title: Simon Data
article_title: Simon Data
description: "Verwenden Sie die Braze- und Simon Data-Integration, um anspruchsvolle Zielgruppen zu erstellen und mit Braze zu synchronisieren, um sie in Echtzeit und ohne Code zu orchestrieren."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon Data

> [Simon Data][1] ist eine Kundendatenplattform (CDP), die von Marketingfachleuten geschätzt wird und der Datenteams vertrauen. Indem er Ihr Data Warehouse in ein Marketing-Kraftwerk verwandelt, sorgt Simon für bessere Geschäftsergebnisse und ein besseres Kundenerlebnis.

Verwenden Sie die Braze- und Simon Data-Integration, um anspruchsvolle Zielgruppen zu erstellen und mit Braze zu synchronisieren, um sie in Echtzeit und ohne Code zu orchestrieren. Mit dieser Integration können Sie die besten Funktionen von Simons Kampagnenpriorisierung und Identitätsabgleich, die Unterstützung komplexer Aggregate und vieles mehr nutzen, um Ihre Braze-Kampagnen weiterzuentwickeln.

## Voraussetzungen

Um loszulegen, müssen Sie Ihr Braze-Konto innerhalb Ihres Simon Data-Kontos authentifizieren.

| Anforderung         | Beschreibung                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon Data          | Sie müssen ein bestehendes Simon Data-Konto haben, um die Braze-Integration von Simon Data aus zu nutzen.                                                                    |
| Braze REST API Schlüssel  | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `campaigns.trigger.schedule.create`, und `campaigns.trigger.send`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Dashboard URL | [Ihre REST-Endpunkt-URL][3]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

- Auslösen eines Braze Canvas oder einer E-Mail  
- Segmenteigenschaften übergeben und pflegen
- Sync-Eigenschaften und Kontakteigenschaften

{% alert note %}  
Wenn Sie die Integration von Simon und Braze verwenden, sendet Simon bei jeder Synchronisierung nur Deltas an Braze, um Kosten für irrelevante Daten zu vermeiden. Weitere Informationen finden Sie unter [Sync-Eigenschaften und Kontakteigenschaften](#sync-traits-and-contact-properties).
{% endalert %}

## Integration

### Authentifizieren Sie Ihr Braze-Konto in Simon

Um die Braze-Integration zu nutzen, authentifizieren Sie zunächst Ihr Braze-Konto in Simon:

1. Klicken Sie in der linken Navigation auf **Integrationen** und scrollen Sie dann zu Braze.
2. Geben Sie Ihren Braze [REST API-Schlüssel][2] und die [URL][3] Ihres [Dashboards][3] ein.
3. Klicken Sie auf **Änderungen speichern**.

Bei einer erfolgreichen Verbindung wird im Fenster **Verbunden** angezeigt.

![Bildschirm Integration in Simon Data][8]{: style="max-width:70%"}

### Hinzufügen von Braze-Aktionen zu Flows oder Journeys in Simon

Nachdem Sie Ihr Braze-Konto in Simon authentifiziert haben, können Sie Braze-Aktionen zu [Flows][4] und [Journeys][5] hinzufügen.

Es sind drei Aktionen verfügbar:

- **Sync Simon Segment Attribut**: Synchronisieren Sie Ihre Segmentdetails mit einem neuen oder bestehenden benutzerdefinierten Attribut in Braze.
- **Lösen Sie eine Hartlöt-Leinwand aus**: Lösen Sie ein Braze Canvas aus, das Ihre Simon-Segmentdaten nutzt.
- **Senden Sie eine Braze-Kampagne**: Starten Sie eine komplette Braze-Kampagne von Simon aus.

![Dropdown-Menü mit einer Liste der verfügbaren Braze-Aktionen in Simon Data.][9]{: style="max-width:60%"}

Einige Aktionen sind nur für bestimmte Flussarten oder Reisen verfügbar. Erfahren Sie mehr unter [docs.simondata.com][6].

### Eigenschaften und Kontakteigenschaften synchronisieren

Um den Datenverbrauch zu minimieren, können Sie bestimmte Merkmale auswählen, die standardmäßig synchronisiert werden sollen, anstatt jedes Feld für alle Kunden in einem Segment zu aktualisieren.

{% alert note %}
Um mit der Synchronisierung von Traits zu beginnen, senden Sie eine Anfrage an das [Simon Support Center](https://docs.simondata.com/docs/support-center). Ihr Kundenbetreuer wird Ihnen mitteilen, wann Sie mit den folgenden Schritten fortfahren können.
{% endalert %}

Nachdem Contact Traits von Ihrem Kundenbetreuer aktiviert wurde:

1. Erweitern Sie in Simon das **Admin Center** in der linken Navigation und wählen Sie **Kontaktmerkmale synchronisieren**.
2. Wählen Sie **Braze**. Hier werden die Kontakteigenschaften angezeigt, verschachtelt nach Datensatz.
3. Wählen Sie die Felder aus, die Sie bei der Verwendung der Simon und Braze Integration synchronisieren möchten:
   1. **Die Anzahl der Merkmale** gibt an, wie viele Merkmale in diesem Datensatz zur Auswahl stehen. Sie können alle auswählen oder die Zeile erweitern, um einzelne Felder auszuwählen.
   2. Bearbeiten Sie den **Downstream-Namen**, wenn Sie möchten, dass die Feldnamen anders aussehen, wenn sie in Braze ankommen.
   3. Wenn Sie Braze zum ersten Mal von Simon aus integrieren, klicken Sie auf **Alle Kontakte wieder auffüllen**. Beim Backfilling werden alle Datenpunkte an Braze gesendet, wenn Sie eine Aktion in einem Fluss oder einer Reise zum ersten Mal verwenden, um sicherzustellen, dass alle Daten vollständig synchronisiert sind. Bei nachfolgenden Synchronisierungen werden dann nur die Eigenschaften, die Sie in diesem Bildschirm auswählen, an Braze gesendet. So stellen Sie sicher, dass Ihnen nur die Daten in Rechnung gestellt werden, die Sie benötigen.

![Auswählen von Synchronisationsmerkmalen in Simon Data.][10]




[1]: https://www.simondata.com
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center

[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}  
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}  
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}
