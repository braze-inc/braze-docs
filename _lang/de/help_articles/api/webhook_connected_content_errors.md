---
nav_title: Fehlerbehebung bei Webhook- und Connected-Content-Anfragen
article_title: Fehlerbehebung bei Webhook- und Connected-Content-Anfragen
page_order: 3
channel:
  - webhooks
description: "In diesem Artikel erfahren Sie, wie Sie Fehlercodes von Webhooks und Connected-Content beheben können. Sie erfahren, um welche Fehler es sich handelt und wie Sie sie beheben können."
---

# Fehlerbehebung bei Webhook- und Connected-Content-Anfragen

> In diesem Artikel erfahren Sie, wie Sie häufige Fehlercodes für Webhooks und Connected-Content beheben können, und erhalten weitere Erklärungen, wie diese Fehler in Ihren Anfragen auftreten können.

## 4XX Fehler

`4XX` Fehler zeigen an, dass es ein Problem mit der an den Endpunkt gesendeten Anfrage gibt. Diese Fehler werden in der Regel durch fehlerhafte Anfragen verursacht, z.B. durch missgebildete Parameter, fehlende Authentifizierungs-Header oder falsche URLs.

In der folgenden Tabelle finden Sie Details zu den Fehlercodes und Schritte zur Behebung:

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Fehlercode</th>
      <th>Was es bedeutet</th>
      <th>Schritte zur Klärung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Schlechte Anfrage</b></td>
      <td>Die Syntax der Anfrage ist ungültig.</td>
      <td>
        <ul>
          <li>Prüfen Sie die Nutzdaten der Anfrage auf Syntaxfehler.</li>
          <li>Vergewissern Sie sich, dass alle erforderlichen Felder enthalten und korrekt formatiert sind.</li>
          <li>Wenn Sie eine JSON-Nutzlast senden, validieren Sie die JSON-Struktur.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Nicht autorisiert</b></td>
      <td>Die Anfrage erfordert eine Nutzer:in-Authentifizierung.</td>
      <td>
        <ul>
          <li>Überprüfen Sie, ob die richtigen Zugangsdaten (wie API-Schlüssel oder Token) in den Anfrage-Headern enthalten sind.</li>
          <li>Vergewissern Sie sich, dass Sie die Nutzer:innen-Berechtigung für den Zugriff auf den Endpunkt haben.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Verboten</b></td>
      <td>Der Endpunkt versteht die Anfrage, weigert sich aber, sie zu autorisieren.</td>
      <td>
        <ul>
          <li>Prüfen Sie, ob der API-Schlüssel oder das Token über die erforderlichen Berechtigungen verfügt.</li>
          <li>Vergewissern Sie sich, dass Sie die Nutzer:innen-Berechtigung für den Zugriff auf den Endpunkt haben.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Nicht gefunden</b></td>
      <td>Der Endpunkt kann die angefragte Ressource nicht finden.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die URL des Endpunkts auf Tippfehler oder falsche Pfade.</li>
          <li>Bestätigen Sie, dass die Ressource, auf die Sie zugreifen möchten, existiert.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Methode Nicht zulässig</b></td>
      <td>Die Methode der Anfrage ist dem Endpunkt bekannt, wird aber von der Zielressource nicht unterstützt.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Vergewissern Sie sich, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Zeitüberschreitung der Anfrage</b></td>
      <td>Der Endpunkt hat die Bearbeitung der Anfrage verzögert.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Vergewissern Sie sich, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Konflikt</b></td>
      <td>Die Anfrage ist unvollständig, weil es einen Konflikt mit dem aktuellen Status der Ressource gibt.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Vergewissern Sie sich, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Zu viele Anfragen</b></td>
      <td>Es wurden zu viele Anfragen in einer bestimmten Zeit gesendet.</td>
      <td>
        <ul>
          <li>Senken Sie das Rate-Limits für Ihre Kampagne oder Ihren Canvas-Schritt.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 5XX Fehler

`5XX` Fehler zeigen an, dass es ein Problem mit dem Endpunkt gibt. Diese Fehler werden in der Regel durch serverseitige Probleme verursacht.

| Fehlercode                    | Was es bedeutet                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Interner Server-Fehler** | Der Endpunkt ist auf eine unerwartete Bedingung gestoßen, die ihn daran gehindert hat, die Anfrage zu beenden.                                                       |
| **502 Schlechtes Gateway**           | Der Endpunkt hat eine ungültige Antwort vom Upstream Server erhalten.                                                                                   |
| **503 Dienst nicht verfügbar**   | Der Endpunkt kann die Anfrage wegen einer vorübergehenden Überlastung oder wegen Wartungsarbeiten derzeit nicht bearbeiten.                                                    |
| **504 Gateway-Zeitüberschreitung**       | Der Endpunkt hat keine rechtzeitige Antwort vom Upstream Server erhalten.                                                                               |
| **529 Host überlastet**       | Der Endpunkt-Host ist überlastet und konnte nicht antworten. |
| **598 Wirt ungesund**        | Braze hat die Antwort simuliert, weil der Endpunkt-Host vorübergehend als ungesund markiert ist. Weitere Informationen finden Sie unter [Erkennung ungesunder Hosts](#unhealthy-host-detection). |
| **599 Verbindungsfehler**      | Braze hat beim Versuch, eine Verbindung zum Endpunkt herzustellen, einen Timeout-Fehler bei der Netzwerkverbindung festgestellt. Das bedeutet, dass der Endpunkt möglicherweise instabil oder ausgefallen ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Behebung von 5XX-Fehlern

Hier finden Sie Tipps für die Fehlerbehebung bei häufigen `5XX` Fehlern:

- Überprüfen Sie die Fehlermeldung auf spezifische Details, die im **Nachrichten-Aktivitätsprotokoll** verfügbar sind. Für Webhooks gehen Sie auf der Braze-Homepage zum Abschnitt **Performance im Zeitverlauf** und wählen Sie die Statistiken für Webhooks aus. Hier können Sie den Zeitstempel finden, der angibt, wann die Fehler aufgetreten sind.
- Stellen Sie sicher, dass Sie nicht zu viele Anfragen senden, die den Endpunkt überlasten. Sie können in Stapeln senden oder das Rate-Limits anpassen, um zu prüfen, ob dadurch Fehler reduziert werden.

## Erkennung fehlerhafter Hosts

Braze-Webhooks und Connected-Content verwenden einen Mechanismus zur Erkennung von ungesunden Hosts, um zu erkennen, wenn der Zielhost eine hohe Rate an signifikanter Verlangsamung oder Überlastung aufweist, die zu Timeouts, zu vielen Anfragen oder anderen Ergebnissen führt, die Braze daran hindern, erfolgreich mit dem Ziel-Endpunkt zu kommunizieren. Diese Funktion dient als Schutzmaßnahme, um unnötige Belastungen zu reduzieren, die dem Zielhost Probleme bereiten könnten. Es dient auch der Stabilisierung der Braze-Infrastruktur und der Aufrechterhaltung schneller Nachrichtenübertragungsgeschwindigkeiten.

Die Schwellenwerte für die Erkennung unterscheiden sich zwischen Webhooks und Connected-Content:
- **Für Webhooks**: Wenn die Anzahl der **Fehlschläge 3.000 in einem beliebigen einminütigen Zeitfenster überschreitet** (pro eindeutiger Kombination von Hostname und App-Gruppe - **nicht** pro Endpunktpfad), hält Braze Anfragen an den Zielhost vorübergehend für eine Minute an.
- **Für Connected-Content**: Wenn die Anzahl der **Fehlschläge 3.000 übersteigt UND die Fehlerrate 90% in einem beliebigen einminütigen gleitenden Zeitfenster übersteigt** (pro eindeutiger Kombination von Hostname und App-Gruppe - **nicht** pro Endpunktpfad), hält Braze Anfragen an den Zielhost vorübergehend für eine Minute an.

Wenn Anfragen gestoppt werden, simuliert Braze Antworten mit einem `598` Fehlercode, um den schlechten Zustand anzuzeigen. Nach einer Minute nimmt Braze die Anfragen mit voller Geschwindigkeit wieder auf, wenn sich der Host als gesund erweist. Wenn der Host immer noch ungesund ist, wartet Braze eine weitere Minute, bevor es erneut versucht wird.

Die folgenden Fehlercodes tragen zur Anzahl der Ausfälle des Unhealthy Host Detectors bei: `408`, `429`, `502`, `503`, `504`, `529`.

Bei Webhooks wird Braze HTTP-Anfragen, die durch den Detektor für ungesunde Hosts angehalten wurden, automatisch wiederholen. Dieser automatische Wiederholungsversuch verwendet exponentielles Backoff und wird nur wenige Male wiederholt, bevor er fehlschlägt. Weitere Informationen zu Webhook-Fehlern finden Sie unter [Fehler, Wiederholungslogik und Timeouts]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#errors-retry-logic-and-timeouts).

Wenn bei Connected-Content Anfragen an den Zielhost durch den Detektor für ungesunde Hosts gestoppt werden, rendert Braze weiterhin Nachrichten und folgt Ihrer Liquid-Logik, als ob es einen Fehlerantwortcode erhalten hätte. Wenn Sie sicherstellen möchten, dass diese Connected-Content-Anfragen erneut versucht werden, wenn sie vom Unhealthy-Host-Detektor angehalten werden, verwenden Sie die Option `:retry`. Weitere Informationen über die Option `:retry` finden Sie unter [Wiederholungsversuche für angeschlossene Inhalte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Wenn Sie glauben, dass die Erkennung eines ungesunden Hosts Probleme verursacht, wenden Sie sich an den [Braze Support]({{site.baseurl}}/support_contact/).

## Automatisierte E-Mails und Einträge im Nachrichten-Aktivitätsprotokoll

### Einrichten von automatisierten E-Mails

Wenn in einem Workspace innerhalb von 24 Stunden mehr als 100.000 Webhook- oder Connected-Content-Endpunkt-Fehler (einschließlich Wiederholungen) auftreten, erhalten Sie eine E-Mail mit den folgenden Informationen zur Behebung der Fehler. 

- Name des Workspace
- Ein Link zum Canvas oder zur Kampagne
- Endpunkt-URL
- Fehlercode
- Zeitpunkt, zu dem der Fehler zuletzt beobachtet wurde
- Links zum Nachrichten-Aktivitätsprotokoll und zur zugehörigen Dokumentation

{% alert note %}
Sie können die Fehlerschwelle pro Workspace konfigurieren. Um diesen Schwellenwert anzupassen, wenden Sie sich an den [Braze Support]({{site.baseurl}}/support_contact/).
{% endalert %}

Die Fehler am Endpunkt sind:

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

Diese E-Mails werden nur einmal pro Tag auf der Ebene des Workspace gesendet. Wenn sich keine Nutzer:innen für diese E-Mails registrieren, werden alle Administratoren des Unternehmens benachrichtigt.

Um sich für den Erhalt dieser E-Mails zu registrieren, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Benachrichtigungspräferenzen**.
2. Wählen Sie **Connected-Content-Fehler** und **Webhook-Fehler** im Bereich **Canvas & Kampagnen** aus.

### Einträge im Nachrichten-Aktivitätsprotokoll

Es gibt mindestens einen Eintrag im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab), der sich auf den Fehler bezieht, der die automatisierte E-Mail ausgelöst hat.

### Zusätzliche Insights zum Versagen in Braze Currents

Um die Transparenz bei Webhook-Problemen zu erhöhen, streamt Braze detaillierte Webhook-Ausfallereignisse an Currents und Snowflake Data Sharing. Zu diesen Ereignissen gehören auch fehlgeschlagene Webhook-Anfragen (z.B. HTTP `4xx` oder `5xx` Antworten), so dass Sie besser beobachten können, wie sich Webhook-Probleme auf die Zustellung von Nachrichten auswirken können. Beachten Sie, dass Fehlerereignisse sowohl Terminalfehler als auch Fehler, die erneut versucht werden, umfassen.

{% alert note %}
Connected-Content-Anfragen sind in diesen Webhook-Fehlerereignissen nicht enthalten.
{% endalert %}

Weitere Informationen finden Sie im [Glossar der Ereignisse des Messaging-Engagements]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).
