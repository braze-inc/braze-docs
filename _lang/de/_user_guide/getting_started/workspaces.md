---
nav_title: Workspaces
article_title: "Erste Schritte: Workspaces"
page_order: 3
page_type: reference
description: "Alles, was Sie auf der Braze-Plattform tun, geschieht innerhalb eines Workspace. Dieser Artikel beschreibt, wie sie funktionieren und was Sie bei der Planung Ihrer Workspaces in Braze beachten sollten."
---

# Erste Schritte: Workspaces

Alles, was Sie auf der Braze-Plattform tun, geschieht innerhalb eines Workspace. Workspaces fungieren als separate Silos von Daten und ermöglichen es Ihnen, verschiedene Marken oder Aktivitäten getrennt zu halten. Mehrere Versionen Ihrer Website oder mobilen Anwendung können Daten an denselben Arbeitsbereich senden. Wir bezeichnen die verschiedenen Websites und Apps, die innerhalb eines Workspace gesammelt werden, als "App-Instanzen"

## Arbeitsbereiche verstehen

Arbeitsbereiche dienen zwei wichtigen Zwecken:

- **Nutzerdaten vereinheitlichen:** Wenn sich mehrere App-Instanzen in einem Workspace befinden, können Sie Nutzerdaten nahtlos über verschiedene Versionen Ihrer App, wie iOS, Android und Internet, zusammenstellen und adressieren. So stellen Sie sicher, dass Sie immer über aktuelle Informationen zu jedem Nutzer:innen verfügen, unabhängig von der Plattform, die er verwendet.
- **Trennen Sie verschiedene Aktivitäten:** Workspaces bieten auch die Möglichkeit, verschiedene Marken oder Aktivitäten voneinander zu trennen. Wenn Sie zum Beispiel mehrere Untermarken mit unterschiedlichen Nutzerbasen haben, ist es von Vorteil, für jede Marke einen eigenen Workspace zu erstellen.

{% alert tip %}
Dieser Ansatz ist besonders nützlich für Unternehmen wie Firmen für mobile Spiele, die individuelle Workspaces für jedes ihrer Spiele verwalten können, oder für E-Commerce-Websites, die für jede Region, in der sie tätig sind, separate Workspaces wünschen.
{% endalert %}

## Workspaces planen

Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie entscheiden, welche App-Instanzen in einen Workspace aufgenommen werden sollen, denken Sie an die Nutzer:innen, die Sie ansprechen möchten, und stellen Sie sie entsprechend zusammen.

Die Möglichkeit, mehrere App-Instanzen in einem Workspace zu haben, kann verlockend sein, denn so können Sie Rate-Limits für das Messaging in Ihrem gesamten App-Portfolio festlegen. Es empfiehlt sich jedoch, verschiedene Versionen derselben (oder sehr ähnlicher) Apps nur in einem Workspace zusammenzufassen.

### Gemeinsame Arbeitsbereiche

Häufige Beispiele dafür, dass Sie mehrere App-Instanzen im selben Workspace haben möchten:

- Wenn Sie mehrere, fast identische Apps auf verschiedenen Plattformen haben
- Wenn Sie verschiedene Hauptversionen der App haben, aber dieselben Nutzer:innen beim Upgraden weiterhin einbeziehen möchten
- Wenn Sie verschiedene Versionen der App haben, die ein und derselbe Benutzer wechseln kann (z. B. von kostenlos zu Premium)

#### Auswirkungen auf Segmentierungsfilter

Die Daten aller Apps, die Sie in einem Workspace haben möchten, werden aggregiert. Dies hat erhebliche Auswirkungen auf die folgenden Filter zur Segmentierung in Braze (diese Liste ist nicht vollständig):

- Letzte App-Nutzung
- Erste App-Nutzung
- Sitzungsanzahl
- In-App ausgegebenes Geld
- Push-Abonnement (Dies wird zu einer Alles-oder-Nichts-Situation - wenn Ihre Nutzer:innen sich von einer App abmelden, werden sie von allen Apps im Workspace abgemeldet).
- E-Mail-Abo (Dies wird zu einer Alles-oder-nichts-Situation und kann zu Compliance-Problemen führen.)

{% alert note %}
Die Aggregation von Daten über App-Instanzen hinweg in diesen Filtern ist der Grund, warum wir nicht empfehlen, wesentlich unterschiedliche Apps im selben Workspace unterzubringen. Das kann die Zielfindung erschweren!
{% endalert %}

### Getrennte Arbeitsbereiche

In anderen Fällen möchten Sie vielleicht mehrere, separate Workspaces haben. Gängige Beispiele hierfür sind:

- Getrennte Arbeitsbereiche für Entwicklungs- und Produktionsumgebungen der gleichen Anwendung
- Verschiedene Untermarken, z. B. ein Handyspiel-Unternehmen, das mehrere Spiele anbietet
- Unterschiedliche Lokalisierungen derselben App oder Website, die in verschiedenen Ländern funktionieren oder auf verschiedene Sprachen abzielen

### Wichtige Überlegungen

Denken Sie daran, dass Arbeitsbereiche wie separate Datensilos funktionieren. Alle Daten, seien es Nutzerdaten oder Marketing-Assets, werden in einem Workspace gespeichert. Diese Daten können nicht ohne weiteres außerhalb dieses Workspace weitergegeben werden. 

Im Folgenden finden Sie alle wichtigen Elemente, die in einem Workspace konfiguriert werden:

- [App-Instanzen](#app-instances)
- [Teams](#teams)
- [Braze-Benutzerberechtigungen](#braze-user-permissions) (aber nicht Braze-Benutzer)
- [Currents Konnektoren](#currents-connectors)
- [Benutzerprofile](#user-profiles) und die zugehörigen Benutzerdaten
- [Segmente, Kampagnen und Leinwände](#segments-campaigns-and-canvases)

#### App-Instanzen

Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie zum Beispiel eine kostenlose und eine Pro-Version Ihrer App für iOS und Android haben, erstellen Sie vier App-Instanzen in Ihrem Arbeitsbereich (kostenlose iOS-App, kostenlose Android-App, Pro-iOS-App und Pro-Android-App). So erhalten Sie vier API-Schlüssel, die Sie verwenden können, einen für jede App-Instanz.

#### Teams

[Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) können nach Kundenstandort, Sprache und benutzerdefinierten Attributen eingerichtet werden, so dass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging-Funktionen und Kundendaten haben.

#### Braze Benutzerberechtigungen

Arbeitsbereiche haben unabhängige Zugriffs- und Benutzerberechtigungsdefinitionen. Mit [Benutzerrechten]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) können Sie genau festlegen, worauf ein einzelner Dashboard-Benutzer oder ein Team innerhalb eines einzelnen Arbeitsbereichs Zugriff hat.

#### Currents Konnektoren

Das [Currents-Tool]({{site.baseurl}}/user_guide/data/braze_currents/) ist ein Realtime-Daten-Stream zu Ihren Engagement-Events. Es ist der robusteste und zugleich granularste Export der Braze-Plattform. Currents-Konnektoren sind in bestimmten Braze-Paketen enthalten, und vielleicht haben Sie zunächst einen erhalten, der einen einzigen Workspace voraussetzt.

Wenn Sie sich entscheiden, ob Sie getrennte oder kombinierte Workspaces erstellen möchten, sollten Sie die Anzahl Ihrer Currents Konnektoren berücksichtigen, da Currents Konnektoren nicht über Workspaces hinweg gemeinsam genutzt werden. 

Wenn Sie beispielsweise getrennte Workspaces für die Entwicklungs- und die Produktionsumgebung derselben App haben, aktivieren Sie Ihren Currents Konnektor im Workspace der Produktionsumgebung. Um Currents in beiden Workspaces zu aktivieren, müssen Sie einen zusätzlichen Currents Konnektor erwerben.

#### Benutzerprofile

Alle dauerhaften Daten, die mit einem Benutzer verbunden sind, werden in seinem [Benutzerprofil]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) gespeichert. Benutzerprofile sind jedoch auch eine großartige Ressource für die Fehlersuche und das Testen, da Sie ganz einfach auf Informationen über die Engagement-Historie eines Benutzers, seine Segmentzugehörigkeit, sein Gerät und sein Betriebssystem zugreifen können.

#### Segmente, Kampagnen und Leinwände

Ein Segment, eine Kampagne oder ein Canvas kann nicht auf Daten referenzieren oder zugreifen, die sich in einem anderen Workspace befinden. Befinden sich dagegen mehrere Apps im selben Workspace, werden die Daten aller Apps zusammengefasst. Dies wird sich [auf die Filter in Braze auswirken](#impact-on-segmentation-filters).

### Überblick über die einzelnen Ansätze

Die folgende Tabelle beschreibt die Vor- und Nachteile dieser beiden Ansätze zur Workspace-Planung:

- **Separate Arbeitsbereiche und Benutzerprofile:** Ein Workspace hat eine App-Instanz und eine Person hat ein Nutzerprofil für diese App-Instanz.
- **Gemeinsame Arbeitsbereiche und Benutzerprofile:** Ein Workspace hat mehrere App-Instanzen und eine Person hat ein Nutzerprofil für alle diese App-Instanzen.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
</style>

<table>
    <tr>
        <th></th>
        <th colspan="2">Getrennte Arbeitsbereiche</th>
        <th colspan="2">Gemeinsame Arbeitsbereiche</th>
    </tr>
    <tr>
        <th></th>
        <th>Vorteile</th>
        <th>Beeinträchtigungen</th>
        <th>Vorteile</th>
        <th>Beeinträchtigungen</th>
    </tr>
    <tr>
        <td>Targeting</td>
        <td>Der sicherste Weg, um die Kommunikation zu trennen. Die Kampagnen sind garantiert nur auf bestimmte Nutzerprofile ausgerichtet.</td>
        <td>Sie können keine werbeübergreifenden Nachrichten senden, auch wenn Sie wissen, dass ein:e Nutzer:in ein anderes Nutzerprofil in einem anderen Workspace hat.</td>
        <td>Sie können werbeübergreifende Nachrichten senden, wenn Sie wissen, dass ein Benutzer mehrere Apps in Ihrem Arbeitsbereich verwendet.<br><br>Kann Benutzerdaten aus verschiedenen Anwendungen referenzieren. Zum Beispiel hat John ein Attribut X, das für App 1 relevant ist, und ein Attribut Y, das für App 2 relevant ist, die beide in einer Kampagne referenziert werden können.</td>
        <td>Mehr Raum für menschliche Fehler - Sie könnten versehentlich Benutzer über mehrere App-Instanzen hinweg anvisieren.<br><br>Um In-App-Nachrichten zu senden, müssen Sie app-spezifische benutzerdefinierte Ereignisse haben, damit eine Kampagne nicht versehentlich in einer anderen App angezeigt wird. Zum Beispiel, <code>app_1_action</code> gegen <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <td>Benutzerdefinierte Ereignisse und Attribute</td>
        <td>Benutzerdefinierte Attribute und Ereignisse sind garantiert spezifisch für eine App-Instanz.</td>
        <td>Das Benutzerverhalten kann nicht über Arbeitsbereiche hinweg verfolgt werden.<br><br><b>Tipp:</b> Dazu können Sie mehrere Currents-Verbindungen nutzen.</td>
        <td>Kann das Benutzerverhalten über alle App-Instanzen im Arbeitsbereich verfolgen.</td>
        <td>Benutzerdefinierte Attribute und Ereignisse würden für alle App-Instanzen gelten, wodurch es schwierig werden könnte, zu erkennen, welche Daten in einem Benutzerprofil für welche App-Instanz relevant sind. Ist "date_of_parking" zum Beispiel für App 1 oder App 2 relevant? Um dem entgegenzuwirken, sollten Sie gut strukturierte Namenskonventionen verwenden.</td>
    </tr>
    <tr>
        <td>Frequency-Capping</td>
        <td>Frequency-Capping kann für jede App-Instanz separat definiert werden (basierend auf dem Workspace).</td>
        <td>--</td>
        <td>--</td>
        <td>Frequency-Capping gilt für alle Kampagnen, nicht für einzelne Apps, was es schwieriger macht, zu viele Nachrichten an Kund:innen zu verhindern.</td>
    </tr>
    <tr>
        <td>Abo-Status für Nutzer:in-Profile</td>
        <td>Der Abo-Status jedes Nutzerprofils ist für jede App-Instanz eindeutig.</td>
        <td>--</td>
        <td>--</td>
        <td>Die Abo-Status eines Nutzerprofils werden über App-Instanzen hinweg kombiniert.<br><br><b>Tipp:</b> Sie könnten stattdessen <a href='/docs/user_guide/data/custom_data/custom_attributes'>angepasste Attribute</a> verwenden, um die Abos Ihrer Nutzer:innen zu verwalten.</td>
    </tr>
    <tr>
        <td>Braze Benutzerberechtigungen</td>
        <td>--</td>
        <td>Das Update der <a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>Benutzerberechtigungen</a> für einen Nutzer:innen des Dashboards muss für jeden Workspace, auf den der Nutzer:innen Zugriff benötigt, separat durchgeführt werden.</td>
        <td><a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>Nutzer</a>:innen können einmal für einen Nutzer des Dashboards festgelegt werden und haben dann dieselben Berechtigungen für alle App-Instanzen im Workspace.</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Duplizieren von Inhalten</td>
        <td>--</td>
        <td>Sie können keine Segmente, Push- oder Content-Card-Kampagnen oder Canvase in verschiedenen Workspaces duplizieren.</td>
        <td>Kann [doppelte Kampagnen über workspaces]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/copying_across_workspaces/) für die folgenden unterstützten Kanäle: SMS, In-App-Nachrichten, E-Mail, E-Mail-Vorlagen und Inhaltsblöcke. <br><br>Sie können Segmente, Kampagnen und Canvases duplizieren, um Inhalte von einer App-Instanz zur anderen wiederzuverwenden.</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Analytics</td>
        <td>Die globalen Statistiken werden auf der Startseite korrekt angezeigt.</td>
        <td>--</td>
        <td>--</td>
        <td>Die globalen Statistiken werden für alle App-Instanzen im Arbeitsbereich auf der Startseite zusammengefasst.</td>
    </tr>
</table>

## Bewährte Praktiken

### Einen Arbeitsbereich für Tests einrichten

Wenn Sie planen, einen Workspace für die Produktion einzurichten (einen Workspace, der Nachrichten an echte Nutzer:innen sendet), sollten Sie auch einen Test-Workspace einrichten. Ein Testarbeitsbereich ist ein Duplikat Ihres Produktionsarbeitsbereichs ohne echte Benutzerdaten. 

Dies wird aus mehreren Gründen als beste Praxis angesehen:

- **Isolierung von Änderungen:** Sie erlaubt es Ihnen, neue Features, Konfigurationen oder Updates in einer isolierten Umgebung zu testen, ohne Ihre Produktionsumgebung zu beeinträchtigen. Wenn also während der Tests etwas schief geht, bleibt Ihre Produktionsumgebung davon unberührt.
- **Genaues Testen:** Dies lässt genauere Tests zu, da die Daten in der Testumgebung kontrolliert und bearbeitet werden können, ohne dass Sie sich Gedanken über die realen Daten machen müssen.
- **Fehlersuche:** Es ist einfacher, Probleme in einer Testumgebung zu beheben, da Sie die Umgebung frei bearbeiten können, ohne sich Gedanken über die Auswirkungen auf die Produktionsumgebung zu machen.
- **Training:** Neue Teammitglieder können sich in einer sicheren Umgebung mit dem Workspace vertraut machen, in der Fehler keine realen Konsequenzen haben.

{% alert tip %}
Die Reihenfolge, in der Sie einen Workspace zum Testen und einen Workspace für die Produktion einrichten, kann von Ihren spezifischen Bedürfnissen und Umständen abhängen. Es ist jedoch generell eine gute Idee, zunächst einen Workspace zum Testen einzurichten. Dies erlaubt es Ihnen, Features, Konfigurationen und Updates zu testen, bevor sie im Workspace der Produktion implementiert werden. Wenn Sie mit den Tests und Ergebnissen zufrieden sind, können Sie Ihren Workspace für die Produktion einrichten.
{% endalert %}

### Administratoren hinzufügen

Sie sollten mehr als einen Braze-Benutzer mit Admin-Rechten für einen einzelnen Arbeitsbereich haben. So stellen Sie sicher, dass es in Ihrem Unternehmen genügend Personen gibt, die die Berechtigungen anderer Benutzer verwalten können.

## Nächste Schritte

Nachdem Sie Ihren Workspace-Plan festgelegt haben, ist es an der Zeit, Ihren Workspace zu erstellen und App-Instanzen hinzuzufügen. Weitere Schritte finden Sie unter [Erstellen und Verwalten von Arbeitsbereichen]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/).

