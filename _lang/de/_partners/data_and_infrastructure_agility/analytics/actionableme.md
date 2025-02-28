---
nav_title: actionable.me
article_title: actionable.me
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und actionable.me, einer proprietären Software und Prozessen, die es Ihnen ermöglichen, das Beste aus Ihrer Braze-Investition herauszuholen - und zwar sofort."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me][2]die vom Team von Massive Rocket, einer Daten- und CRM-Agentur, entwickelt wurde, ist ein standardisierter und automatisierter Ansatz für die Durchführung von CRM-Programmen, der Tools und Prozesse bereitstellt, mit denen Braze-Kunden schnell, konsistent und vorhersehbar einen Mehrwert erhalten. 

Die Integration von Braze und actionable.me ermöglicht Ihnen die Bereitstellung eines Dienstes zur Überwachung Ihrer Fortschritte bei der Nutzung von Braze. Durch eine Kombination von Tools und Prozessen werden sie Ihre CRM-Leistung schnell bewerten, neue Möglichkeiten identifizieren und Empfehlungen für eine bessere Leistung geben.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| actionable.me Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein actionable.me Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den im nächsten Abschnitt aufgeführten Berechtigungen.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Um Braze und actionable.me zu integrieren, muss die Plattform actionable.me konfiguriert werden, und ein Braze-API-Schlüssel muss in Braze erstellt und im Dashboard actionable.me konfiguriert werden.

### Schritt 1: Erstellen Sie Ihren Braze API-Schlüssel

Navigieren Sie in Braze zu **Einstellungen** > **API-Schlüssel**. Wählen Sie **Neuen API-Schlüssel erstellen** und stellen Sie sicher, dass die folgenden Berechtigungen hinzugefügt werden:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

### Schritt 2: Stellen Sie dem Team von actionable.me Informationen zur Verfügung.

Um die Integration abzuschließen, müssen Sie Ihren REST-API-Schlüssel und die [REST-Endpunkt-URL][1] an Ihr actionable.me Betriebsteam übermitteln. actionable.me wird dann die Verbindung herstellen und sich nach Abschluss der Einrichtung mit Ihnen in Verbindung setzen, um mit dem Austausch von Erkenntnissen zu beginnen.

![Die Seite actionable.me "Plattform hinzufügen", die das Betriebsteam von actionable.me konfigurieren wird.][5]

## Fehlersuche

Kontaktieren Sie das Team von actionable.me oder Massive Rocket für weitere Unterstützung: [info@massiverocket.com][3]

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://actionable.me
[3]: mailto:info@massiverocket.com
[4]: {% image_buster /assets/img/actionableme/image1.png %}
[5]: {% image_buster /assets/img/actionableme/image2.png %}
