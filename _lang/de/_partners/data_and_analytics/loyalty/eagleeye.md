---
nav_title: Eagle Eye
article_title: Eagle Eye
description: "Erfahren Sie, wie Sie Eagle Eye in Braze integrieren können."
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Eagle Eye

> [Eagle Eye](https://eagleeye.com/) ist ein führendes Unternehmen für SaaS- und KI-Technologien, das es Marken aus den Bereichen Einzelhandel, Reisen und HOSPITALITY ermöglicht, die Loyalität ihrer Verbraucher:in Echtzeit, Omnichannel und personalisierten Marketing-Aktivitäten in großem Umfang zu gewinnen.

_Diese Integration wird von Eppo verwaltet._

## Übersicht

Eagle Eye Connect ist eine bidirektionale Integration zwischen Braze und AIR, die es Marken ermöglicht, Treue- und Aktionsdaten direkt in Braze zu aktivieren. Clients können in AIR Rewards an Verbraucher:in ausgeben, die eine Zielgruppe in AIR betreten.  Dies erlaubt Marketern, das Customer-Engagement anhand von Echtzeitdaten wie Punktesalden, Aktionen und Belohnungsaktivitäten anzupassen.

## Anwendungsfälle

- Triggern Sie Braze-Kampagnen auf der Grundlage von Treueereignissen wie Punkteschwellen oder verdienten Rewards.
- Reichern Sie Nutzerprofile von Braze mit Realtime-Daten an, um ein personalisiertes Targeting zu ermöglichen.
- Verfolgen Sie die Wirksamkeit von Kampagnen in Verbindung mit der Einlösung von Rewards und erstellen Sie Berichte darüber.
- Geben Sie Rewards in AIR aus, wenn Nutzer:innen Kampagnen in Braze eingeben.

## Voraussetzungen

| Anforderung              | Beschreibung |
|--------------------------|-------------|
| Eagle Eye AIR Konto    | Sie benötigen ein aktives Eagle Eye AIR-Konto, um von dieser Partnerschaft zu profitieren. Wenden Sie sich an das Team von Eagle Eye für Partnerschaften unter [partnerships@eagleeye.com](mailto:partnerships@eagleeye.com). |
| Braze REST API-Schlüssel       | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen > API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt      | [Ihre URL für den REST-Endpunkt](https://www.braze.com/docs/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Ausgehend vs. eingehend

In den folgenden Tabellen werden die beiden Arten von Integrationen beschrieben, die zwischen Braze und Eagle Eye AIR unterstützt werden. Eagle Eye Connect ist die Middleware, die den Datenaustausch zwischen AIR und Partnersystemen wie Braze ermöglicht. Wenn Sie mehr erfahren möchten, lesen Sie die [Dokumentation zu Braze von Eagle Eye.](https://developer.eagleeye.com/docs/braze)

{% tabs local %}
{% tab ausgehend %}
<table>
  <thead>
    <tr>
      <th>Richtung</th>
      <th>Initiiert von</th>
      <th>Datenfluss</th>
      <th>Zweck</th>
      <th>Beispiel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Eagle Eye</td>
      <td>Zur Braze API</td>
      <td>
        Senden Sie Kundenbindungsdaten als angepasste Attribute über angepasste Events in Nutzerprofile von Braze. Innerhalb von Braze können die aufgenommenen Daten verwendet werden, um:
        <ul>
          <li>Segmentierung von Nutzer:innen, Triggern von Kampagnen</li>
          <li>Nachrichten personalisieren</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Senden von Treuepunkten oder Tier-Status an Braze (<code>ee_loyalty.points.current</code>, <code>ee_loyalty.tier.tierId</code>)</li>
          <li>Update des Profils eines Nutzers:in, wenn er einen Coupon erhält oder einlöst.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}
{% endtab %}

{% tab eingehend %}
<table>
  <thead>
    <tr>
      <th>Richtung</th>
      <th>Initiiert von</th>
      <th>Datenfluss</th>
      <th>Zweck</th>
      <th>Beispiel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>Zur Eagle Eye API über Webhook</td>
      <td>
        Wenn ein Verbraucher:in Braze eine Zielgruppe aus einer beliebigen Quelle eingibt, kann Braze einen Braze-to-Braze-Webhook an EE Connect triggern, so dass EE eine Rewards (Coupon oder Punkte) ausgeben kann.<br><br>
        Nach Abschluss der Aktion in AIR würde Braze ein ausgehendes Ereignis von AIR erhalten.
      </td>
      <td>
        <ul>
          <li>Rewards (Coupon oder Punkte) werden an einen Verbraucher:in für die Teilnahme am Kundenbindungs-Programm ausgegeben</li>
          <li>Rewards werden an einen Verbraucher:in ausgegeben, der eine verspätete Zustellung hatte</li>
          <li>Geburtstag Rewards</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}
{% endtab %}
{% endtabs %}

{% alert tip %}
Weitere Informationen zu den angepassten Daten, die Sie als angepasste Attribute oder Events an Braze senden können, finden Sie in [der Dokumentation zu Braze von Eagle Eye](https://developer.eagleeye.com/docs/braze#data-model).
{% endalert %}

## Überblick über die Integration

Eingehende und ausgehende Konnektoren können derzeit nur über APIs mit direkter Unterstützung durch das Eagle Eye Team eingerichtet werden. Eine Selbstbedienungsoption im AIR Dashboard ist jedoch in Vorbereitung!

Wenn Sie mit Ihrem Eagle Eye Team zusammenarbeiten, werden Sie Folgendes erledigen:

### Schritt 1: Details zur Konfiguration bereitstellen

Zunächst geben Sie Ihrem Eagle Eye Team die folgenden Informationen:

| Sie liefern            | Beschreibung |
|------------------------|-------------|
| Braze API-Zugangsdaten  | Teilen Sie Ihren Braze REST Endpunkt, Ihren App Bezeichner und Ihren API-Schlüssel sicher mit Ihrem Eagle Eye Kontakt. |
| Bezeichner-Abgleich    | Bestimmen und teilen Sie den primären Nutzer:innen-Bezeichner für Profil-Updates, der in AIR und Braze üblich ist, z.B. Externe ID oder E-Mail. |
| Autorisierungsschlüssel               | Legen Sie für jeden eingehenden und ausgehenden Konnektor einen geheimen Authentifizierungsschlüssel fest und teilen Sie ihn. |
| Währung Codes          | Geben Sie den 3-stelligen Währungscode für die Anzeige von Geldbeträgen an (e.g., USD). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Schritt 2: Eagle Eye Connect konfigurieren 

Ihr Eagle Eye Team konfiguriert Eagle Eye Connect unter Verwendung der von Ihnen bereitgestellten Details sowie der eindeutigen AIR API Zugangsdaten und ausgehenden Ereignisse für die Konnektoren.

### Schritt 3: Konfigurieren Sie Aktionen für soziales Verhalten in AIR

Als nächstes richten Sie in AIR eine oder mehrere Social Behavioral Actions mit eindeutigen Aktionsreferenzen ein, um Punkte oder Coupons auszugeben.

### Schritt 4: Braze konfigurieren

In Braze werden Sie Folgendes erledigen:

- Richten Sie Kampagnen in Braze ein, um Rewards in AIR auszugeben  
- Richten Sie alle Mitteilungen an Verbraucher:in ein, wenn AIR-Ereignisse empfangen werden.

### Schritt 5: Testen Sie Ihre Integration

Führen Sie API-Aufrufe in AIR durch und beobachten Sie den Fluss von Ereignisdaten in Ihre Braze workspace.Validate Daten, die Sie von AIR erhalten, und bestätigen Sie, dass die Attribute wie erwartet aktualisiert werden.  

Fügen Sie außerdem Nutzer:innen zu Zielgruppen hinzu und bestätigen Sie, dass Rewards in AIR ausgegeben werden.

### Schritt 6: Einführung in die Produktion

Nachdem die Tests erfolgreich verlaufen sind, kann die Integration in Betrieb genommen werden, um kontinuierlich Daten an Braze zu senden. Die gleichen Konfigurationsschritte sind für Produktionsumgebungen in AIR und Braze erforderlich

Wenden Sie sich an Ihren Eagle Eye Customer Success Manager:in, damit Ihnen eine Ressource zugewiesen wird, um EE Connect einzurichten.

## Support

Wenn Sie Unterstützung bei der Integration oder Fehlerbehebung benötigen, wenden Sie sich bitte an das Eagle Eye Team unter [support@eagleeye.com](mailto:support@eagleeye.com).
