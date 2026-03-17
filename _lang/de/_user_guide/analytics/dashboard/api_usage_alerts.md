---
nav_title: API-Nutzungswarnungen
article_title: API-Nutzungsmeldungen
description: "Dieser Artikel bietet eine Übersicht über die API-Nutzungswarnungen, mit denen Sie unerwarteten Datenverkehr proaktiv erkennen können."
page_order: 3.6
---

# API-Nutzungswarnungen

> API-Nutzungswarnungen bieten wichtige Einblicke in Ihre API-Nutzung und ermöglichen es Ihnen, unerwarteten Datenverkehr proaktiv zu erkennen. Durch die Einrichtung dieser Benachrichtigungen zum Tracking wichtiger API-Anfragevolumina können Sie Realtime-Benachrichtigungen erhalten und Probleme beheben, bevor sie sich auf Ihre Marketing-Kampagnen auswirken.

## Informationen zu Benachrichtigungen über die Nutzung der API

Sie können API-Nutzungswarnungen verwenden, um das Volumen der Anfragen für die folgenden Kategorien zu überwachen:

| API-Kategorie | Details |
|--------------|---------|
| REST API-Endpunkte | Verfolgt die Nutzung aller REST API-Aufrufe, die an das Backend von Braze gesendet werden, wie beispielsweise das Versenden von Nachrichten, das Erstellen von Kampagnen oder das Exportieren von Nutzer:innen. |
| SDK-API-Anfragen | Verfolgt API-Anfragen, die von Braze-SDKs in Client-Apps gestellt werden, wie beispielsweise das Triggern von In-App-Nachrichten oder die Synchronisierung von Nutzerdaten.<br><br>_\*Nur für Kund:innen verfügbar, die „Monatlich aktive:r Nutzer:in – CY 24-25“ erworben haben._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Erstellen einer Benachrichtigung zur API-Nutzung

Um eine Benachrichtigung zur API-Nutzung zu erstellen:

1. Bitte gehen Sie zu **„Einstellungen“** > **„APIs und Bezeichner“** > **„API-Nutzungswarnungen“** und erstellen Sie eine neue Warnung.
2. Geben Sie einen Namen für Ihre Benachrichtigung ein und wählen Sie die REST API Endpunkte und API-Schlüssel aus, für die Sie benachrichtigt werden möchten.
3. Definieren Sie Ihre Alarmkriterien, indem Sie einen oder mehrere Codes auswählen und die [Alarmschwellenwerte](#api-usage-alert-thresholds) festlegen.
4. Wenn Sie fertig sind, schalten Sie **bitte die Option „Warnung aktiviert“** um.
    ![Ein Beispiel für eine API-Nutzungswarnung, die Benachrichtigungen sendet, wenn der Endpunkt „Nutzer:innen verfolgen“ innerhalb einer Stunde um 100 Prozent zunimmt.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Alarmschwellen {#api-usage-alert-thresholds}

Bei der Definition Ihrer Alarmkriterien können Sie die folgenden Schwellenwerte anpassen:

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
        Definiert die Bedingungen, die zu dem Schwellenwert führen, bei dessen Erreichen Sie benachrichtigt werden möchten. Die folgenden Funktionen werden unterstützt:<br><br>
        <ul>
          <li><strong>Erhöht um</strong> oder <strong>verringert um</strong>: Vergleicht Anfragen mit dem vorherigen Zeitfenster.</li>
          <li><strong>Prozentualer Anstieg</strong> oder <strong>prozentualer Rückgang</strong>: Vergleicht die prozentuale Veränderung der Anfragen mit dem vorherigen Zeitfenster.</li>
          <li><strong>Größer als oder gleich</strong>, oder <strong>kleiner als oder gleich</strong>: Zählt die Anfragen innerhalb eines Zeitfensters.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Grenzwert-Volumen</td>
      <td>Wird in Verbindung mit einer Schwellenbedingung verwendet.</td>
    </tr>
    <tr>
      <td>Innerhalb</td>
      <td>Das Zeitfenster für die Bewertung von Warnmeldungen.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Einrichten von Benachrichtigungen

Sie können eine E-Mail-Benachrichtigung, eine Webhook-Benachrichtigung oder beides einrichten. Webhook-Benachrichtigungen können für Anwendungsfälle wie das Senden einer Benachrichtigung an externe Plattformen, beispielsweise einen Slack-Kanal, äußerst nützlich sein. Ein Beispiel finden Sie in unserer [Dokumentation](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) zur Integration von Benachrichtigungen mit Slack für unsere Benachrichtigungseinstellungen.

![Eine E-Mail wird an die ausgewählte E-Mail-Adresse gesendet, sobald die Kriterien für die Benachrichtigung erfüllt sind.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Beispiel-Nutzlast {#payload}

Im Folgenden finden Sie ein Beispiel für die Nutzlast des Hauptteils eines API-Nutzungsalarm-Webhooks.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Beispielwarnungen

Im Folgenden finden Sie einige Möglichkeiten, wie Sie Ihre API-Nutzungsbenachrichtigungen so konfigurieren können, dass Sie in den folgenden Szenarien benachrichtigt werden.

{% tabs local %}
{% tab api health %}
Sie können Benachrichtigungen einrichten, um den allgemeinen Zustand Ihrer APIs zu überwachen. Beispielsweise können Sie diese Warnmeldungen einrichten, wenn API-Fehler drastisch zunehmen, beispielsweise um 20 % gegenüber der vorherigen Stunde.

| Endpunkt | API-Schlüssel | Antwortcode | Grenzwert-Bedingung | Grenzwert-Volumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| Alle Endpunkte | Alle API-Schlüssel | `4XX` und `5XX` | Um 10 % erhöht | (10 %) | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Bitte beachten Sie, dass Sie benachrichtigt werden, wenn Ihre Workspace die Rate-Limits für`/users/track`Endpunkte erreicht. Sie können diese Konfiguration auch auf andere Braze-Endpunkte anwenden.

| Endpunkt | API-Schlüssel | Antwortcode | Grenzwert-Bedingung | Grenzwert-Volumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Alle API-Schlüssel | `429` | Größer als oder gleich | (100 %) | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
Diese Alarmkonfiguration benachrichtigt Sie, wenn Fehler bei API-triggerten Kampagnen und Canvases auftreten, von denen einige möglicherweise eine hohe Priorität haben.

| Endpunkt | API-Schlüssel | Antwortcode | Grenzwert-Bedingung | Grenzwert-Volumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Alle API-Schlüssel | `4XX` und `5XX` | Größer als oder gleich | (1 %) | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Verwenden Sie die folgende Alarmkonfiguration, um benachrichtigt zu werden, wenn eine Partnerintegration keine Daten mehr an Braze sendet.

| Endpunkt | API-Schlüssel | Antwortcode | Grenzwert-Bedingung | Grenzwert-Volumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| Alle Endpunkte | Der API-Schlüssel, der für Ihre Partnerintegration verwendet wird | Alle Antwortcodes | Kleiner oder gleich | 0 | 1 Tag |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Überlegungen

- Jede aktive Warnmeldung sendet nur einmal alle 8 Stunden eine E-Mail- oder Webhook-Benachrichtigung. Dies dient dazu, eine übermäßige Anzahl von Benachrichtigungen aufgrund einer einzelnen Warnmeldung zu vermeiden. Sollte Ihre Benachrichtigung vorzeitig erfolgen, empfehlen wir Ihnen, die Benachrichtigungskriterien anzupassen, um sie besser auf Ihren Anwendungsfall abzustimmen.
- Sie können bis zu 10 Benachrichtigungen pro Workspace einrichten.
