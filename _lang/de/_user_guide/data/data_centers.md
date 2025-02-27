---
nav_title: Daten-Zentren
article_title: Daten-Zentren
page_order: 0.1
page_type: reference
description: "Dieser referenzierte Artikel enthält Informationen über Datenzentren, einschließlich ihrer Standorte und wie Sie sich für regionsspezifische Datenzentren registrieren können."
---

# Datenzentren

> Die Braze-Rechenzentren sind so aufgebaut, dass Sie die Wahl haben, wo die Daten Ihrer Nutzer:innen verarbeitet und gespeichert werden. Dies lässt zu, dass Sie Ihre Risiken im Zusammenhang mit der Souveränität von Daten, der Flexibilität und der Verwaltung effektiv verwalten. Wenn Sie ein Braze-Rechenzentrum auswählen, können Sie sicher sein, dass unsere Plattform alle lokalen Anforderungen an die Datenverwaltung erfüllt oder übertrifft.

## Funktionsweise

Braze betreibt mehrere Datenzentren an verschiedenen Standorten auf der ganzen Welt. Diese Datenzentren erlauben es, dass unsere Dienste zuverlässig und skalierbar sind. Diese geografische Verteilung trägt dazu bei, die Latenzzeit zu minimieren, d.h. die Zeit, die die Daten für den Weg zwischen Server und Nutzer:in benötigen. 

Das bedeutet auch, dass die Anfragen eines Nutzers:innen, der mit Ihrer App oder Website interagiert, an das nächstgelegene Rechenzentrum weitergeleitet werden, wodurch die Performance optimiert und die Ladezeiten verkürzt werden. Durch die Verbindung mit dem nächstgelegenen Datenzentrum können Ihre Nutzer:innen schnelle Ladezeiten erleben, was besonders für Realtime Messaging und das Engagement der Nutzer:innen wichtig ist.

Nehmen wir an, Sie haben eine mobile App, die Push-Benachrichtigungen an Nutzer:innen sendet. Wenn ein Nutzer:in in Melbourne eine Benachrichtigung erhält, wird die Anfrage zum Senden dieser Benachrichtigung an das nächstgelegene Datenzentrum in Australien weitergeleitet. Für den Fall, dass die mobile App während einer Aktion einen sprunghaften Anstieg der Nutzer:innen erlebt, verfügt Braze über eine skalierbare Infrastruktur mit mehreren Datenzentren, die die erhöhte Nachfrage bewältigen können.

## Liste der Datenzentren

In der folgenden Tabelle finden Sie eine Liste der verfügbaren Datenzentren.

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 33%;
}
table th:nth-child(3) {
    width: 33%;
}
table th:nth-child(4) {
    width: 24%;
}
table td {
    word-break: break-word;
}
</style>
<table>
  <thead>
    <tr>
      <th>Region des Datenzentrums</th>
      <th>Dashboard URL</th>
      <th>REST Endpunkt</th>
      <th>SDK-Endpunkt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Australien</b></td>
      <td><code>https://dashboard.au-01.braze.com</code></td>
      <td><code>https://rest.au-01.braze.com</code></td>
      <td><code>sdk.au-01.braze.com</code></td>
    </tr>
    <tr>
      <td><b>Europa</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.eu</code></li>
          <li><code>https://dashboard-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.fra-01.braze.eu</code></li>
          <li><code>https://rest.fra-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.fra-01.braze.eu</code></li>
          <li><code>sdk.fra-02.braze.eu</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>USA</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.com</code></li>
          <li><code>https://dashboard-02.braze.com</code></li>
          <li><code>https://dashboard-03.braze.com</code></li>
          <li><code>https://dashboard-04.braze.com</code></li>
          <li><code>https://dashboard-05.braze.com</code></li>
          <li><code>https://dashboard-06.braze.com</code></li>
          <li><code>https://dashboard-07.braze.com</code></li>
          <li><code>https://dashboard-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.iad-01.braze.com</code></li>
          <li><code>https://rest.iad-02.braze.com</code></li>
          <li><code>https://rest.iad-03.braze.com</code></li>
          <li><code>https://rest.iad-04.braze.com</code></li>
          <li><code>https://rest.iad-05.braze.com</code></li>
          <li><code>https://rest.iad-06.braze.com</code></li>
          <li><code>https://rest.iad-07.braze.com</code></li>
          <li><code>https://rest.iad-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.iad-01.braze.com</code></li>
          <li><code>sdk.iad-02.braze.com</code></li>
          <li><code>sdk.iad-03.braze.com</code></li>
          <li><code>sdk.iad-04.braze.com</code></li>
          <li><code>sdk.iad-05.braze.com</code></li>
          <li><code>sdk.iad-06.braze.com</code></li>
          <li><code>sdk.iad-07.braze.com</code></li>
          <li><code>sdk.iad-08.braze.com</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Registrierung für regionalspezifische Datenzentren

Wenn Sie Ihr Braze-Konto einrichten, können Sie sich für regionsspezifische Datenzentren anmelden. Wenden Sie sich an Ihren Account Manager:in, um Informationen und Empfehlungen darüber zu erhalten, welche Daten für Sie am besten geeignet sind, basierend auf den geografischen Regionen Ihrer Nutzer:innen.
