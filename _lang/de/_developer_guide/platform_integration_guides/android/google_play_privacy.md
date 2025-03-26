---
nav_title: Fragebogen zum Datenschutz bei Google Play
article_title: Antworten auf Fragen zum Datenschutz im Google Play Store
page_order: 9
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel beschreibt, wie Sie Fragen zum Datenschutz bei Google Play beantworten können."

---
<style>
table td {
    word-break: break-word;
}
</style>

# Fragebogen zum Datenschutz bei Google Play

> Ab April 2022 müssen Android-Entwickler das [Datensicherheitsformular](https://support.google.com/googleplay/android-developer/answer/10787469) von Google Play ausfüllen, um ihre Datenschutz- und Sicherheitspraktiken offenzulegen. In diesem Leitfaden finden Sie Anweisungen zum Ausfüllen dieses neuen Formulars sowie Informationen darüber, wie Braze Ihre App-Daten verarbeitet. 

Als App-Entwickler haben Sie die Kontrolle darüber, welche Daten Sie an Braze senden. Die von Braze erhaltenen Daten werden gemäß Ihren Anweisungen verarbeitet. Das ist es, was Google als [Dienstanbieter](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform) klassifiziert. 

{% alert important %}
Dieser Artikel enthält Informationen zu den Daten, die das Braze SDK im Zusammenhang mit dem Fragebogen im Abschnitt zur Datensicherheit von Google Play verarbeitet. Dieser Artikel stellt keine Rechtsberatung dar. Wir empfehlen Ihnen daher, sich mit Ihrer Rechtsabteilung zu beraten, bevor Sie Informationen an Google übermitteln.
{% endalert %}

## Fragen

|Fragen|Antworten für Braze SDK|
|---|---|
|Werden die erforderlichen Nutzerdatentypen von Ihrer App erfasst oder geteilt?|Ja, das Braze Android SDK erfasst Daten entsprechend der vom App-Entwickler vorgenommenen Konfiguration. |
|Sind alle von Ihrer App gesammelten Benutzerdaten während der Übertragung verschlüsselt?|Ja|
|Können Nutzer eine Anfrage zur Löschung ihrer Daten stellen?|Ja|

Weitere Informationen über den Umgang mit Benutzeranfragen zu ihren Daten und deren Löschung finden Sie unter [Braze Data Retention Information]({{site.baseurl}}/api/data_retention/).

## Datenerfassung

Die von Braze erfassten Daten sind von der jeweiligen Integration und den Nutzerdaten abhängig, die Sie sammeln möchten. Weitere Informationen darüber, welche Daten standardmäßig von Braze erfasst werden und wie Sie bestimmte Attribute deaktivieren können, finden Sie unter [Optionen für die SDK-Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration).

<table id="datatypes">
    <thead>
        <tr>
            <th width="25%">Kategorie</th>
            <th width="25%">Datentyp</th>
            <th width="50%">Nutzung durch Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Standort</td>
            <td>Ungefährer Standort</td>
            <td rowspan="15">Wird standardmäßig nicht erhoben.</td>
        </tr>
        <tr>
            <td>Genauer Standort</td>
        </tr>
        <tr>
            <td rowspan="9">Persönliche Infos</td>
            <td>Name</td>
        </tr>
        <tr>
            <td>E-Mail-Adresse</td>
        </tr>
        <tr>
            <td>Benutzer-IDs</td>
        </tr>
        <tr>
            <td>Adresse</td>
        </tr>
        <tr>
            <td>Telefonnummer</td>
        </tr>
        <tr>
            <td>Ethnie und Ethnizität</td>
        </tr>
        <tr>
            <td>Politische oder religiöse Überzeugungen</td>
        </tr>
        <tr>
            <td>Sexuelle Orientierung</td>
        </tr>
        <tr>
            <td>Andere Infos</td>
        </tr>
        <tr>
            <td rowspan="4">Finanzielle Informationen</td>
            <td>Zahlungsinformationen von Nutzern</td>
        </tr>
        <tr>
            <td>Kaufhistorie</td>
        </tr>
        <tr>
            <td>Kreditwürdigkeit</td>
        </tr>
        <tr>
            <td>Andere Finanzinformationen</td>      
        </tr>
        <tr>
            <td rowspan="2">Gesundheit und Fitness</td>
            <td>Informationen zur Gesundheit</td>
            <td rowspan="2">Wird standardmäßig nicht erhoben.</td>
        </tr>
        <tr>
            <td>Informationen zur Fitness</td>     
        </tr>
        <tr>
            <td rowspan="3">Nachrichten</td>
            <td>E-Mails</td>
            <td rowspan="2">Wird standardmäßig nicht erhoben.</td>
        </tr>
        <tr>
            <td>SMS oder MMS</td>          
        </tr>
        <tr>
            <td>Andere In-App-Nachrichten</td>
            <td>Wenn Sie In-App-Nachrichten oder Push-Benachrichtigungen über Braze senden, sammeln wir Informationen darüber, wann Benutzer diese Nachrichten geöffnet oder gelesen haben.</td>
        </tr>
        <tr>
            <td rowspan="2">Fotos und Videos</td>
            <td>Fotos</td>
            <td rowspan="8">Nicht gesammelt.</td>
        </tr>
        <tr>
            <td>Videos</td>
        </tr>
        <tr>
            <td rowspan="3">Audio-Dateien</td>
            <td>Sprach- oder Tonaufnahmen</td>
        </tr>        
        <tr>
            <td>Musikdateien</td>
        </tr>
        <tr>
            <td>Andere Audiodateien</td>
        </tr>
        <tr>
            <td>Dateien und Dokumente</td>
            <td>Dateien und Dokumente</td>
        </tr>
        <tr>
            <td>Kalender</td>
            <td>Kalender-Events</td>
        </tr>
        <tr>
            <td>Kontakte</td>
            <td>Kontakte</td>
        </tr>
        <tr>
            <td rowspan="5">App-Aktivität</td>
            <td>App-Interaktionen</td>
            <td>Braze erfasst standardmäßig Daten zur Sitzungsaktivität. Alle anderen Interaktionen und Aktivitäten werden von der individuellen Integration Ihrer App bestimmt.</td>
        </tr>
        <tr>
            <td>In-App-Suchverlauf</td>
            <td>Nicht gesammelt.</td>            
        </tr>
        <tr>
            <td>Installierte Apps</td>
            <td>Nicht gesammelt.</td>            
        </tr>
        <tr>
            <td>Sonstige von Nutzern generierte Inhalte</td>
            <td rowspan="2">Wird standardmäßig nicht erhoben.</td>            
        </tr>
        <tr>
            <td>Andere Aktionen</td>
        </tr>
        <tr>
            <td>Besuchte Internetseiten</td>
            <td>Internetverlauf</td>
            <td>Nicht gesammelt.</td>
        </tr>
        <tr>
            <td rowspan="3">Informationen und Leistung der App</td>
            <td>Absturzprotokolle</td>
            <td>Braze erfasst Absturzprotokolle für Fehler, die innerhalb des SDK auftreten. Diese enthalten Angaben zum Smartphone-Modell und Betriebssystem des Nutzers sowie eine Braze-spezifische Nutzer-ID.</td>
        </tr>
        <tr>
            <td>Diagnostik</td>
            <td>Nicht gesammelt.</td>            
        </tr>
        <tr>
            <td>Andere Leistungsdaten der App</td>
            <td>Nicht gesammelt.</td>
        </tr>
        <tr>
            <td>Gerät oder andere IDs</td>
            <td>Gerät oder andere IDs</td>
            <td>Braze generiert eine Geräte-ID, um die Geräte der Benutzer zu unterscheiden, und überprüft, ob die Nachrichten an das richtige Gerät gesendet werden.</td>
        </tr>
    </tbody>
</table>

Wenn Sie mehr über andere Gerätedaten erfahren möchten, die Braze sammelt und die möglicherweise nicht in den Geltungsbereich der Google Play-Datenschutzrichtlinien fallen, lesen Sie unsere [Übersicht über Android-Speicher]({{site.baseurl}}/developer_guide/platform_integration_guides/android/storage) und unsere [SDK-Datenerfassungsoptionen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration).

