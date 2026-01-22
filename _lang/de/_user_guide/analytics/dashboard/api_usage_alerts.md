---
nav_title: Warnungen zur API-Nutzung
article_title: API-Nutzungsmeldungen
description: "Dieser Artikel bietet eine Übersicht über die API-Nutzungswarnungen, mit denen Sie proaktiv unerwarteten Datenverkehr erkennen können."
page_order: 3.6
---

# Warnungen zur API-Nutzung

> API-Nutzungswarnungen bieten einen wichtigen Einblick in Ihre API-Nutzung und ermöglichen es Ihnen, unerwarteten Datenverkehr proaktiv zu erkennen. Indem Sie diese Warnmeldungen einrichten, um das Volumen wichtiger API-Anfragen zu verfolgen, können Sie Realtime-Benachrichtigungen erhalten und Probleme angehen, bevor sie sich auf Ihre Kampagnen auswirken.

## Über API-Nutzungswarnungen

Sie können API-Nutzungswarnungen verwenden, um das Anfragevolumen für die folgenden Kategorien zu überwachen:

| API-Kategorie | Details |
|--------------|---------|
| REST API Endpunkte | Tracking der Nutzung aller REST API-Aufrufe, die an das Backend von Braze gerichtet sind, wie z.B. das Senden von Nachrichten, das Erstellen von Kampagnen oder das Exportieren von Nutzer:innen. |
| SDK API-Anfragen | Tracking von API-Anfragen, die von Braze SDKs in Client Apps gestellt werden, z.B. das Triggern von In-App-Nachrichten oder die Synchronisierung von Nutzerdaten.<br><br>_\*Nur verfügbar für Kund:innen, die monatlich aktive:r Nutzer:in - CY 24-25 erworben haben._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Erstellen einer API-Nutzungsmeldung

So erstellen Sie einen API-Nutzungsalarm:

1. Gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **API-Nutzungswarnungen** und erstellen Sie dann eine neue Warnung.
2. Geben Sie einen Namen für Ihre Benachrichtigung ein und wählen Sie die REST API Endpunkte und API-Schlüssel, für die Sie eine Benachrichtigung erhalten möchten.
3. Definieren Sie Ihre Alarmkriterien, indem Sie einen oder mehrere Response Codes auswählen und die [Alarmschwellenwerte](#api-usage-alert-thresholds) festlegen.
4. Wenn Sie fertig sind, schalten Sie **Alert** um.
    ![Ein Beispiel für einen API-Nutzungsalarm, der Benachrichtigungen sendet, wenn der Endpunkt Tracking Nutzer:innen innerhalb einer Stunde um 100 Prozent steigt.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Schwellenwerte für Alarme {#api-usage-alert-thresholds}

Wenn Sie Ihre Alarmkriterien definieren, können Sie die folgenden Schwellenwerte anpassen:

<table>
  <thead>
    <tr>
      <th>Feld</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Grenzwert-Bedingung</td>
      <td>
        Legt die Bedingungen fest, die zu dem Schwellenwert führen, bei dem Sie alarmiert werden möchten. Folgendes wird unterstützt:<br><br>
        <ul>
          <li><strong>Erhöht um</strong> oder <strong>Verringert um</strong>: Vergleicht Anfragen mit dem vorherigen Zeitfenster.</li>
          <li><strong>Erhöht um Prozent</strong> oder <strong>Verringert um Prozent</strong>: Vergleicht die prozentuale Veränderung der Anfragen gegenüber dem vorherigen Zeitfenster.</li>
          <li><strong>Größer als oder gleich</strong> oder <strong>kleiner als oder gleich</strong>: Zählt Anfragen in einem Zeitfenster.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Grenzwert-Volumen</td>
      <td>Wird in Verbindung mit der Schwellenwertbedingung verwendet.</td>
    </tr>
    <tr>
      <td>Innerhalb</td>
      <td>Das Zeitfenster für die Auswertung des Alarms.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Einrichten von Alarmbenachrichtigungen

Sie können eine E-Mail-Benachrichtigung, eine Webhook-Benachrichtigung oder beides einrichten. Webhook-Benachrichtigungen können für Anwendungsfälle wie das Senden einer Benachrichtigung an externe Plattformen, z. B. an einen Slack-Kanal, sehr nützlich sein. Ein Beispiel finden Sie in unserer [Dokumentation](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) über die Integration von Benachrichtigungen mit Slack für unsere Benachrichtigungseinstellungen.

![Es wird eine E-Mail an die ausgewählte E-Mail gesendet, wenn das Kriterium für den Alarm erreicht ist.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Probe-Nutzlast {#payload}

Nachfolgend finden Sie ein Beispiel für die Nutzdaten eines Webhooks für einen API-Nutzungsalarm.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": [
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition: "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    	],
    "timeframe_start": 2025-03-20T15:35:00Z,
    "timeframe_end": 2025-03-20T16:35:00Z,
    "volume": 1500,
    "previous_timeframe_start": 2025-03-20T14:35:00Z,
    "previous_timeframe_end": 2025-03-20T15:35:00Z,
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Beispiel-Warnungen

Hier finden Sie einige Möglichkeiten, wie Sie Ihre Konfigurationen für API-Nutzungswarnungen so einrichten können, dass Sie in den folgenden Szenarien benachrichtigt werden.

{% tabs local %}
{% tab api health %}
Sie können Warnmeldungen einrichten, um den allgemeinen Zustand Ihres APIs zu überwachen. Sie können diese Warnungen zum Beispiel einrichten, wenn API-Fehler drastisch zunehmen, z.B. um 20% gegenüber der vorherigen Stunde.

| Endpunkt | API-Schlüssel | Antwortcode | Grenzwert-Bedingung | Grenzwert-Volumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| Alle Endpunkte | Alle API-Schlüssel | `4XX` und `5XX` | Erhöht um 10% | (10 %) | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Sie werden benachrichtigt, wenn Ihr Workspace sein Rate-Limits für den Endpunkt `/users/track` erreicht. Sie können diese Konfiguration auch auf andere Endpunkte von Braze anwenden.

| Endpunkt | API-Schlüssel | Antwortcode | Grenzwert-Bedingung | Grenzwert-Volumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Alle API-Schlüssel | `429` | Größer als oder gleich | (100 %) | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
Diese Warnkonfiguration benachrichtigt Sie, wenn Fehler bei API-getriggerten Kampagnen und Canvase auftreten, von denen einige eine hohe Priorität haben können.

| Endpunkt | API-Schlüssel | Antwortcode | Grenzwert-Bedingung | Grenzwert-Volumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/kampagnen/triggern/senden</code></li><li><code>/canvas/triggern/senden</code></li><li><code>/nachrichten/senden</code></li></ul>{:/} | Alle API-Schlüssel | `4XX` und `5XX` | Größer als oder gleich | (1 %) | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Verwenden Sie die folgende Warnkonfiguration, um benachrichtigt zu werden, wenn eine Partnerintegration keine Daten mehr an Braze sendet.

| Endpunkt | API-Schlüssel | Antwortcode | Grenzwert-Bedingung | Grenzwert-Volumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| Alle Endpunkte | Der API-Schlüssel, der für Ihre Partnerintegration verwendet wird | Alle Antwortcodes | Weniger als oder gleich | 0 | 1 Tag |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Überlegungen

- Jeder aktive Alarm sendet nur einmal alle 8 Stunden eine E-Mail oder Webhook-Benachrichtigung. Dies soll verhindern, dass zu viele Benachrichtigungen von einem einzigen Alarm ausgehen. Wenn Ihr Alarm Sie zu früh benachrichtigt, sollten Sie die Kriterien für den Alarm so ändern, dass sie besser zu Ihrem Anwendungsfall passen.
- Sie können bis zu 10 Alarme pro Workspace haben.
