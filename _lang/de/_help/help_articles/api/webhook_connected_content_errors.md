---
nav_title: Fehlerbehebung bei Webhook- und Connected Content-Anfragen
article_title: Fehlerbehebung bei Webhook- und Connected Content-Anfragen
page_order: 3
channel:
  - webhooks
description: "In diesem Artikel erfahren Sie, wie Sie Fehlercodes für Webhooks und Connected Content beheben können. Sie erfahren, um welche Fehler es sich handelt und wie Sie diese beheben können."
---

# Fehlerbehebung bei Webhook- und Connected Content-Anfragen

> In diesem Artikel erfahren Sie, wie Sie häufige Fehlercodes für Webhooks und Connected Content beheben können, und erhalten weitere Erklärungen dazu, wie diese Fehler bei Ihren Anfragen auftreten können.

## 4XX Fehler

`4XX` Fehler zeigen an, dass es ein Problem mit der an den Endpunkt gesendeten Anfrage gibt. Diese Fehler werden in der Regel durch fehlerhafte Anfragen verursacht, z.B. durch falsch geformte Parameter, fehlende Authentifizierungs-Header oder falsche URLs.

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
      <td>Die Anfrage enthält eine ungültige Syntax.</td>
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
      <td>Die Anfrage erfordert eine Benutzerauthentifizierung.</td>
      <td>
        <ul>
          <li>Vergewissern Sie sich, dass die korrekten Authentifizierungsdaten (z. B. API-Schlüssel oder Token) in den Headern der Anfrage enthalten sind.</li>
          <li>Vergewissern Sie sich, dass Sie über die erforderlichen Benutzerrechte für den Zugriff auf den Endpunkt verfügen.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Verboten</b></td>
      <td>Der Endpunkt versteht die Anfrage, weigert sich aber, sie zu autorisieren.</td>
      <td>
        <ul>
          <li>Prüfen Sie, ob der API-Schlüssel oder das Token über die erforderlichen Berechtigungen verfügt.</li>
          <li>Vergewissern Sie sich, dass Sie über die erforderlichen Benutzerrechte für den Zugriff auf den Endpunkt verfügen.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Nicht gefunden</b></td>
      <td>Der Endpunkt kann die angeforderte Ressource nicht finden.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die Endpunkt-URL auf Tippfehler oder falsche Pfade.</li>
          <li>Bestätigen Sie, dass die Ressource, auf die Sie zugreifen möchten, existiert.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Methode nicht erlaubt</b></td>
      <td>Die Anfragemethode ist dem Endpunkt bekannt, wird aber von der Zielressource nicht unterstützt.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Stellen Sie sicher, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Zeitüberschreitung der Anfrage</b></td>
      <td>Der Endpunkt hat eine Zeitüberschreitung bei der Bearbeitung der Anfrage.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Stellen Sie sicher, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Konflikt</b></td>
      <td>Die Anfrage ist unvollständig, weil es einen Konflikt mit dem aktuellen Status der Ressource gibt.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Stellen Sie sicher, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Zu viele Anfragen</b></td>
      <td>Es werden zu viele Anfragen in einer bestimmten Zeitspanne gesendet.</td>
      <td>
        <ul>
          <li>Senken Sie das Ratenlimit für Ihre Kampagne oder Canvas-Stufe.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 5XX Fehler

`5XX` Fehler zeigen an, dass es ein Problem mit dem Endpunkt gibt. Diese Fehler werden in der Regel durch serverseitige Probleme verursacht.

| Fehlercode                    | Was es bedeutet                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Interner Serverfehler** | Der Endpunkt ist auf eine unerwartete Bedingung gestoßen, die ihn daran hinderte, die Anfrage zu beenden.                                                       |
| **502 Schlechtes Gateway**           | Der Endpunkt hat eine ungültige Antwort vom Upstream-Server erhalten.                                                                                   |
| **503 Dienst nicht verfügbar**   | Der Endpunkt ist derzeit nicht in der Lage, die Anfrage aufgrund einer vorübergehenden Überlastung oder Wartung zu bearbeiten.                                                    |
| **504 Gateway-Zeitüberschreitung**       | Der Endpunkt hat keine rechtzeitige Antwort vom Upstream-Server erhalten.                                                                               |
| **529 Host überlastet**       | Der Endpunkt-Host ist überlastet und konnte nicht antworten. |
| **598 Wirt ungesund**        | Braze hat die Antwort simuliert, weil der Endpunkt-Host vorübergehend als ungesund markiert ist. Weitere Informationen finden Sie unter [Erkennung ungesunder Hosts](#unhealthy-host-detection). |
| **599 Verbindungsfehler**      | Braze hat beim Versuch, eine Verbindung zum Endpunkt herzustellen, eine Zeitüberschreitung bei der Netzwerkverbindung festgestellt. Das bedeutet, dass der Endpunkt möglicherweise instabil oder ausgefallen ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Behebung von 5XX-Fehlern

Hier finden Sie Tipps zur Behebung häufiger `5XX` Fehler:

- Überprüfen Sie die Fehlermeldung auf spezifische Details, die im **Message Activity Log** verfügbar sind. Für Webhooks gehen Sie zum Abschnitt **Leistung im Zeitverlauf** auf der Braze-Startseite und wählen Sie die Statistiken für Webhooks. Hier können Sie den Zeitstempel finden, der angibt, wann die Fehler aufgetreten sind.
- Stellen Sie sicher, dass Sie nicht zu viele Anfragen senden, die den Endpunkt überlasten. Sie können in Stapeln senden oder das Ratenlimit anpassen, um zu prüfen, ob dadurch Fehler reduziert werden.

## Erkennung ungesunder Hosts

Braze Webhooks und Connected Content verwenden einen Mechanismus zur Erkennung von ungesunden Hosts, um zu erkennen, wenn der Zielhost eine hohe Rate an signifikanter Verlangsamung oder Überlastung aufweist, die zu Timeouts, zu vielen Anfragen oder anderen Ergebnissen führt, die Braze daran hindern, erfolgreich mit dem Zielendpunkt zu kommunizieren. Sie dient als Schutzmaßnahme, um unnötige Belastungen zu reduzieren, die den Zielhost in Schwierigkeiten bringen könnten. Es dient auch der Stabilisierung der Braze-Infrastruktur und der Aufrechterhaltung schneller Nachrichtenübertragungsgeschwindigkeiten.

Wenn die Anzahl der **Ausfälle 3.000 in einem einminütigen gleitenden Zeitfenster übersteigt** (pro eindeutiger Kombination aus Hostname und Anwendungsgruppe - **nicht** pro Endpunktpfad), hält Braze Anfragen an den Zielhost vorübergehend für eine Minute an und simuliert stattdessen Antworten mit einem `598` Fehlercode, um den schlechten Zustand anzuzeigen. Nach einer Minute nimmt Braze die Anfragen mit voller Geschwindigkeit wieder auf, wenn der Host für gesund befunden wird. Wenn der Host immer noch nicht in Ordnung ist, wartet Braze eine weitere Minute, bevor es erneut versucht wird.

Die folgenden Fehlercodes tragen zur Anzahl der Ausfälle des Unhealthy Host Detectors bei: `408`, `429`, `502`, `503`, `504`, `529`.

Bei Webhooks wird Braze HTTP-Anfragen, die durch den Detektor für ungesunde Hosts angehalten wurden, automatisch wiederholen. Diese automatische Wiederholung verwendet ein exponentielles Backoff und versucht es nur wenige Male, bevor sie fehlschlägt. Weitere Informationen zu Webhook-Fehlern finden Sie unter [Fehler, Wiederholungslogik und Timeouts]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#errors-retry-logic-and-timeouts).

Wenn bei Connected Content die Anfragen an den Zielhost durch den Detektor für ungesunde Hosts angehalten werden, rendert Braze weiterhin Nachrichten und folgt Ihrer Liquid-Logik, als ob es einen Fehlerantwortcode erhalten hätte. Wenn Sie sicherstellen möchten, dass diese Connected Content-Anfragen erneut versucht werden, wenn sie durch den Unhealthy Host Detector angehalten werden, verwenden Sie die Option `:retry`. Weitere Informationen über die Option `:retry` finden Sie unter [Wiederholungsversuche für angeschlossene Inhalte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Wenn Sie glauben, dass die Erkennung eines ungesunden Hosts Probleme verursacht, wenden Sie sich an den [Braze Support]({{site.baseurl}}/support_contact/).
