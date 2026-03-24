---
nav_title: Sicherheitseinstellungen
article_title: Sicherheitseinstellungen
page_order: 2
toc_headers: h2
page_type: reference
description: "Dieser Referenzartikel behandelt allgemeine unternehmensübergreifende Sicherheitseinstellungen, einschließlich Authentifizierungsregeln, IP-Zulassungslisten, personenbezogene Daten und Zwei-Faktor-Authentifizierung (2FA)."

---

# Sicherheitseinstellungen

> Als Administrator steht die Sicherheit ganz oben auf Ihrer Liste der Anliegen. Die Seite **Sicherheitseinstellungen** hilft Ihnen bei der Verwaltung der allgemeinen, unternehmensübergreifenden Sicherheitseinstellungen, einschließlich Authentifizierungsregeln, IP-Zulassungsliste und Zwei-Faktor-Authentifizierung.

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen**.

## Regeln für die Authentifizierung

### Passwortlänge

Verwenden Sie dieses Feld, um die erforderliche Mindestlänge des Passworts zu ändern. Der Standardwert beträgt mindestens acht Zeichen.

### Passwortkomplexität

Wählen Sie **Komplexe Passwörter erzwingen**, um zu verlangen, dass die Passwörter mindestens eines der folgenden Elemente enthalten müssen: 
- Großbuchstabe
- Kleinbuchstabe
- Zahl
- Sonderzeichen

### Wiederverwendbarkeit von Passwörtern

Legt die Mindestanzahl neuer Kennwörter fest, die festgelegt werden müssen, bevor ein Benutzer ein Kennwort erneut verwenden kann. Die Standardeinstellung ist drei.

### Regel für den Ablauf von Passwörtern

Verwenden Sie dieses Feld, um festzulegen, wann die Benutzer Ihres Braze-Kontos ihr Passwort zurücksetzen sollen.

### Regeln für die Sitzungsdauer

Verwenden Sie dieses Feld, um festzulegen, wie lange Braze Ihre Sitzung aufrechterhalten soll. Nachdem Braze Ihre Sitzung als inaktiv eingestuft hat (keine Aktivität für die festgelegte Anzahl von Minuten), meldet Braze den Nutzer:in ab. Die maximale Anzahl an Minuten, die Sie eingeben können, beträgt 10.080 (entspricht einer Woche), wenn für Ihr Unternehmen die Zwei-Faktor-Authentifizierung vorgeschrieben ist. Andernfalls beträgt die maximale Sitzungsdauer 1.440 Minuten (entspricht 24 Stunden).

### Einmalige Anmeldung (SSO) Authentifizierung

Sie können Ihre Nutzer:innen daran hindern, sich mit einem Passwort oder SSO anzumelden.

Für [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) müssen Kund:innen ihre SAML-Einstellungen vor der Erzwingung einrichten. Wenn Kund:innen Google-SSO verwenden, müssen sie nur die Seite mit den Sicherheitseinstellungen anpassen, ohne dass ein zusätzlicher Lift erforderlich ist.

## Dashboard-IP-Allowlisting

Verwenden Sie das angezeigte Feld, um bestimmte IP-Adressen und Subnetze aufzulisten, von denen aus sich Benutzer bei Ihrem Konto anmelden können (z.B. von einem Firmennetzwerk oder VPN). Geben Sie IP-Adressen und Subnetze als CIDR-Bereiche in einer kommagetrennten Liste an. Sofern nicht anders angegeben, können Nutzer:innen sich von jeder beliebigen IP-Adresse aus anmelden.

## Zwei-Faktor-Authentifizierung (2FA)

Für alle Unternehmensnutzer:innen ist eine Zwei-Faktor-Authentifizierung erforderlich. Es fügt eine zweite Ebene der Identitätsüberprüfung zu einem Kontoprotokoll hinzu und macht es damit sicherer als nur einen Benutzernamen und ein Passwort. Wenn Ihr Dashboard keine Zwei-Faktor-Authentifizierung unterstützt, wenden Sie sich an Ihren Customer-Success-Manager. 

Wenn die Zwei-Faktor-Authentifizierung aktiviert ist:

- Zusätzlich zur Eingabe eines Passworts müssen Nutzer:innen bei der Anmeldung in ihrem Braze-Konto einen Bestätigungscode eingeben. Der Code kann über eine Authentifizierungs-App, E-Mail oder SMS gesendet werden. 
- Das Kontrollkästchen **Dieses Konto 30 Tage lang speichern** wird für Nutzer:innen verfügbar.

Braze sperrt Nutzer:innen, die keine Zwei-Faktor-Authentifizierung in ihrem Braze-Konto eingerichtet haben. Benutzer von Braze-Konten können die Zwei-Faktor-Authentifizierung auch selbst in den **Kontoeinstellungen** einrichten, selbst wenn dies nicht vom Administrator verlangt wird.

Achten Sie darauf, Ihre Änderungen zu speichern, bevor Sie die Seite verlassen!

### Merken Sie sich dieses Konto für 30 Tage {#remember-me}

Dieses Feature ist verfügbar, wenn die Zwei-Faktor-Authentifizierung aktiviert ist.

Wenn Sie **Dieses Konto 30 Tage lang speichern** auswählen, wird ein Cookie auf Ihrem Gerät gespeichert, so dass Sie sich im Laufe von 30 Tagen nur einmal mit der Zwei-Faktor-Authentifizierung anmelden müssen. 

![Kontrollkästchen „Dieses Konto für 30 Tage merken“]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Bei Kunden mit mehreren Konten unter einem Dashboard-Unternehmen können Probleme bei der Nutzung dieser Funktion auftreten, da das Cookie an ein bestimmtes Gerät gebunden ist. Wenn Benutzer dasselbe Gerät verwenden, um sich bei mehreren Konten anzumelden, wird das Cookie für die zuvor autorisierten Konten auf diesem Gerät ersetzt. Braze erwartet, dass nur ein Gerät mit einem Konto verknüpft wird, nicht ein Gerät für mehrere Konten.

### Benutzerauthentifizierung zurücksetzen

Wenn Sie Probleme haben, sich mit der Zwei-Faktor-Authentifizierung anzumelden, wenden Sie sich an die Administratoren Ihres Unternehmens, um die Zwei-Faktor-Authentifizierung zurückzusetzen. Administratoren können die folgenden Schritte durchführen:

1. Gehen Sie zu **Einstellungen** > **Firmenbenutzer**.
2. Wählen Sie den Benutzer aus der vorgegebenen Liste aus.
3. Wählen Sie **Zurücksetzen** unter **Zwei-Faktor-Authentifizierung**.

Ein Reset kann gängige Authentifizierungsprobleme lösen, wie z. B. Probleme mit Authentifizierungs-Apps, fehlende E-Mail-Verifizierung, fehlgeschlagene Anmeldung aufgrund von SMS-Ausfällen oder Benutzerfehlern und vieles mehr.

### Anforderungen für 2FA auf Unternehmensebene

Bitte überprüfen Sie zunächst, ob die 2FA für Ihr Dashboard aktiviert ist, indem Sie zu **„Unternehmenseinstellungen“** > **„Sicherheitseinstellungen“** > **„Zwei-Faktor-Authentifizierung“** navigieren. Wenn der Schalter grau ist, wurde 2FA für Ihr Unternehmen nicht aktiviert und ist nicht für alle Nutzer:innen des Unternehmens eine Pflicht.

#### Benutzeroptionen, wenn 2FA nicht Pflichtfeld ist

Sollte 2FA nicht auf Unternehmensebene vorgeschrieben sein, können einzelne Nutzer:innen 2FA selbstständig auf ihrer Seite „Kontoeinstellungen“ aktivieren. In diesem Fall werden Nutzer:innen nicht aus ihren Konten ausgesperrt, wenn sie diese Funktion nicht einrichten. Sie können auf der Seite „Benutzer verwalten“ überprüfen, welche Nutzer:innen sich für die Aktivierung der 2FA entschieden haben.

#### Anforderungen, wenn 2FA eine Pflicht ist

Wenn 2FA auf Unternehmensebene vorgeschrieben ist, werden Nutzer:innen, die es bei der Anmeldung nicht in ihren eigenen Konten einrichten, aus dem Dashboard ausgesperrt. Nutzer:innen müssen die 2FA-Einrichtung abschließen, um den Zugriff aufrechtzuerhalten.

{% alert important %}
2FA ist für alle Unternehmensnutzer:innen nur dann erforderlich, wenn Single Sign-on (SSO) nicht aktiviert ist. Wenn SSO verwendet wird, muss 2FA auf Unternehmensebene nicht zwingend vorgeschrieben werden.
{% endalert %}

## Einrichtung der Zwei-Faktor-Authentifizierung (2FA)

### Einrichtung von 2FA mit Authy

1. Bitte laden Sie die Authy-App aus dem Shop Ihres Geräts herunter.
2. Bitte geben Sie in Braze Ihre Telefonnummer ein.
3. Bitte tippen Sie auf die Benachrichtigung, die an Ihr Gerät gesendet wurde und Sie dazu auffordert, die Authy-App zu öffnen.
4. Bitte starten Sie die Authy-App auf Ihrem Gerät, um den Code abzurufen.
5. Bitte geben Sie in Braze den Bestätigungscode ein, den Sie von Authy erhalten haben.

Sollten während des Einrichtungsvorgangs Probleme auftreten und Sie zur Braze-Startseite oder zum Bildschirm der Anmeldung weitergeleitet werden, versuchen Sie bitte Folgendes:

- Bitte verwenden Sie den Inkognito- oder privaten Modus: Bitte versuchen Sie die Einrichtung erneut in einem Inkognito- oder privaten Browserfenster. Dadurch können Probleme umgangen werden, die durch Browser-Erweiterungen oder Plugins verursacht werden.
- Bitte versuchen Sie es mit einem anderen Profil: Sollte das Problem persistent sein, empfehlen wir, ein anderes Profil zu verwenden, um Konflikte mit installierten Plugins zu vermeiden.

### Einrichtung von 2FA, wenn diese nicht vorgeschrieben ist

Um die Zwei-Faktor-Authentifizierung (2FA) in Ihrem Braze-Konto manuell zu aktivieren, wenn sie nicht erzwungen wird, befolgen Sie bitte die folgenden Schritte:

1. Bitte laden Sie eine 2FA-App wie Authy, Google Authenticator, Okta Verify oder eine ähnliche App aus dem App Store (iOS), Google Play Store (Android) oder dem Internet herunter. Wenn Sie es vorziehen, die 2FA per E-Mail oder SMS einzurichten, fahren Sie bitte mit Schritt 2 fort.
2. Bitte gehen Sie in Braze zu „Konto verwalten“, scrollen Sie zum Abschnitt **„Zwei-Faktor-Authentifizierung**“ und wählen Sie **„Einrichtung auswählen**“.
3. Bitte geben Sie Ihr Passwort in das Modal für die Anmeldung ein und wählen Sie anschließend **„Passwort überprüfen**“.
4. Geben Sie im Modal **„Zwei-Faktor-Authentifizierung einrichten**“ Ihre Telefonnummer ein und wählen Sie anschließend **„Auswählen**“.
5. Bitte kopieren Sie den generierten siebenstelligen Code aus Ihrer 2FA-App, E-Mail oder SMS-Nachricht, kehren Sie zu Braze zurück und fügen Sie ihn in das Modal **„Einrichtung der Zwei-Faktor-Authentifizierung“** ein. Bitte wählen Sie **„Überprüfen**“.
6. (Optional) Um die Eingabe der 2FA für die nächsten 30 Tage zu vermeiden, aktivieren Sie bitte die Option **„Dieses Konto 30 Tage lang speichern**“.

## Erweiterter Zugriff

Elevated Access bietet eine zusätzliche Sicherheitsebene für sensible Aktionen in Ihrem Braze Dashboard. Wenn Sie aktiv sind, müssen Nutzer:innen ihr Konto erneut überprüfen, bevor sie ein Segment exportieren oder einen API-Schlüssel anzeigen können. Um den erweiterten Zugriff zu verwenden, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie die Option ein. 

Wenn ein Benutzer sich nicht erneut verifizieren kann, wird er an die Stelle zurückgeleitet, an der er aufgehört hat, und kann nicht mit der sensiblen Aktion fortfahren. Nachdem sie sich erfolgreich erneut verifiziert haben, brauchen sie dies in der nächsten Stunde nicht mehr zu tun - es sei denn, sie melden sich vorher ab.

![„Erweiterter Zugriff“-Umschalter.]({% image_buster /assets/img/elevated_access.png %})

## Herunterladen eines Sicherheitsereignisberichts {#security-event-report}

Der Bericht über Sicherheitsereignisse ist ein CSV-Bericht über Sicherheitsereignisse wie Kontoeinladungen, Kontoentfernungen, fehlgeschlagene und erfolgreiche Anmeldeversuche und andere Aktivitäten. Sie können es für interne Audits verwenden.

Um diesen Bericht herunterzuladen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen**.
2. Wählen Sie die Registerkarte **Sicherheitseinstellungen** und gehen Sie zum Abschnitt **Download von Sicherheitsereignissen**.
3. Wählen Sie **Bericht herunterladen**. 

Dieser manuelle Berichtsdownload enthält lediglich die letzten 10.000 Sicherheitsereignisse für Ihr Konto.

Um Sicherheitsereignisse ohne diese Zeilenbegrenzung in Amazon S3 zu exportieren, lesen Sie [bitte den Abschnitt „Exportieren von Sicherheitsereignissen mit Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/)“.

{% details Reported security events %}
### Anmeldung und Konto
- Eingetragen
- Anmeldung fehlgeschlagen
- Einrichtung der Zwei-Faktoren-Authentifizierung abgeschlossen
- Zurücksetzen der Zwei-Faktor-Authentifizierung abgeschlossen
- Freigegebene Entwickler:in 2FA
- Zusätzlicher Entwickler:in
- Konto hinzugefügt
- Entwickler:in suspendiert
- Entwickler:in Unsuspended
- Entwickler:in Aktualisiert
- Entfernte Entwickler:in
- Entferntes Konto
- Nutzer:innen Abo-Status aktualisiert
- Nutzer:in Aktualisiert
- Entwicklerkonto mit Update

### Erhöhter Zugang
- Elevated Access Flow gestartet
- Erhöhter Zugang fertiggestellt
- Fehlgeschlagene 2FA-Überprüfung für erweiterten Zugang
- Enablement der erweiterten Zugriffskontrolle aktiviert
- Durchsetzung der Zugangsvoraussetzungen für Behinderte

Kampagne
- Kampagne hinzugefügt
- Bearbeitete Kampagne

Canvas
- Hinzugefügte Reise
- Bearbeitete Reise

### Segment
- Hinzugefügtes Segment
- Bearbeitetes Segment
- Exportierte Daten in CSV
- Exportierte Segmente über API
- Segment-Nutzer:innen gelöscht
- Freigegebene Kohorte

### REST-API-Schlüssel
- REST API-Schlüssel hinzugefügt
- Entfernter REST API-Schlüssel

### Zugangsdaten für die Basisauthentifizierung
- Zugangsdaten für Basic Auth hinzugefügt
- Aktualisierte Basic Auth Zugangsdaten
- Zugangsdaten für Basic Auth entfernt

### Erlaubnis
- Freigegebene Entwickler:in 2FA
- Aktualisierte Kontoberechtigung
- Team hinzugefügt
- Redaktionsteam
- Archiviertes Team
- Nicht archiviertes Team
- App-Gruppe-Berechtigungsgruppe erstellt
- Bearbeitete App-Gruppenberechtigungen
- App-Gruppenberechtigungen entfernt
- Angepasste Rolle erstellt
- Aktualisierte benutzerdefinierte Rolle
- Angepasste Rolle gelöscht

### Einstellungen des Unternehmens
- App-Gruppe hinzugefügt
- App hinzugefügt
- Firmeneinstellungen geändert
- Update der Sicherheitseinstellungen des Unternehmens
- Update des Exports von Sicherheitsereignissen in die Cloud
- Landing Pages hinzugefügt Angepasste Domain
- Entfernte Landing Pages Benutzerdefinierte Domain
- Angepasste Domain erstellt
- Benutzerdefinierte Domain gelöscht
- Aktivierte globale Kontrollgruppe
- Deaktivierte globale Kontrollgruppe
- Update für globale Kontrollausschlüsse
- Aktualisierte SMS-Zulassungsliste für Abo-Gruppen

### E-Mail-Vorlage
- E-Mail Template hinzugefügt
- Aktualisierte E-Mail Template

### Push-Zugangsdaten
Aktualisierte Push-Zugangsdaten
Entfernte Push-Zugangsdaten

### SDK-Debugger
- Gestartete SDK Debugger Sitzung
- Exportiertes SDK Debugger Protokoll

### Nutzer:innen
- Nutzer:innen gelöscht
- Nutzer:innen angesehen
- Nutzerimport gestartet
- Abo-Gruppenstatus aktualisiert
- Nutzer:in gelöscht
- Löschung einer einzelnen Nutzer:in wurde zurückgenommen
- Massenlöschung von Nutzern wurde abgebrochen

### Kataloge
- Katalog erstellt
- Katalog gelöscht

### Braze-Agenten
- Erstellter Agent
- Bearbeiteter Agent

### BrazeAI-Operator 
- Erbetene Anfrage des BrazeAI-Operators
- BrazeAI-Operator hat geantwortet
{% enddetails %}

## Anzeige von persönlich identifizierbaren Informationen (PII) {#view-pii}

Die Berechtigung **zum** **Anzeigen von PII-Daten** ist nur für ausgewählte Nutzer:innen des Unternehmens verfügbar. Standardmäßig haben alle Administratoren die Berechtigung **PII anzeigen** in den Nutzer:innen-Berechtigungen aktiviert. Dies bedeutet, dass sie alle Standard- und angepassten Attribute, die Ihr Unternehmen als PII definiert hat, im gesamten Dashboard einsehen können. Wenn diese Berechtigung für Nutzer:innen deaktiviert ist, können diese Nutzer:innen keine dieser Attribute sehen.

{% alert note %}
Sie benötigen die Berechtigung **„PII anzeigen“**, um [den Abfrage-Generator]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/) nutzen zu können, da dieser den direkten Zugriff auf bestimmte Kundendaten ermöglicht.
{% endalert %}

Informationen zu den bestehenden Teamberechtigungen finden Sie unter [Festlegen von Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### Definition von PII

{% alert important %}
Die Auswahl und Definition bestimmter Felder als PII-Felder wirkt sich lediglich darauf aus, was Nutzer:innen auf dem Braze-Dashboard sehen können, und hat keinen Einfluss darauf, wie die Daten der Endnutzer:innen in solchen PII-Feldern verarbeitet werden.<br><br>Bitte konsultieren Sie Ihre Rechtsabteilung, um die Einstellungen Ihres Dashboards mit allen für Ihr Unternehmen geltenden Datenschutzbestimmungen und -Richtlinien in Einklang zu bringen, einschließlich derjenigen, die sich auf [die Datenaufbewahrung]({{site.baseurl}}/data_retention/) beziehen.
{% endalert %}

Sie können die Felder, die Ihr Unternehmen als PII definiert, im Dashboard auswählen. Bitte gehen Sie dazu zu **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen**.

Die folgenden Attribute können als PII gekennzeichnet und für Unternehmensnutzer:innen, die keine Berechtigung **zum Anzeigen von PII** haben, ausgeblendet werden.

#### Mögliche PII-Attribute

| Standard-Attribute | Angepasste Attribute |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>E-Mail-Adresse </li> <li> Telefonnummer </li> <li> Vorname </li> <li> Nachname </li> <li> Geschlecht </li> <li> Geburtstag </li> <li> Geräte-IDs </li> <li> Letzter Standort </li> </ul> {:/} | {::nomarkdown} <ul> <li> Alle benutzerdefinierten Attribute<ul><li>Einzelne angepasste Attribute können als PII markiert werden, wenn Sie nicht alle Attribute ausblenden müssen.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Begrenzte Gebiete

Im Folgenden wird davon ausgegangen, dass alle Felder als PII festgelegt sind und die genannten Nutzer:innen Unternehmensnutzer:innen sind, die die Braze-Plattform nutzen. Die „vorangehenden“ Attribute referenzieren diejenigen in der Tabelle [„Potenzielle PII-Attribute](#potential-pii-attributes)“. Das Entfernen von PII-Berechtigungen für eine Nutzer:in kann sich über die aufgeführten Bereiche hinaus auf die Benutzerfreundlichkeit auswirken.

| Dashboard-Navigation | Ergebnis | Anmerkungen |
| -------------------- | ------ | ----- |
| Benutzer suchen | Der oder die Nutzer:in, der oder die sich anmeldet, kann nicht nach E-Mail-Adresse, Telefonnummer, Vorname oder Nachname suchen: {::nomarkdown} <ul> <li> Bei der Anzeige eines Benutzerprofils werden die vorangehenden Standard- und benutzerdefinierten Attribute nicht mehr angezeigt. </li> <li> Die vorangehenden Standardattribute eines Benutzerprofils können nicht über das Braze-Dashboard bearbeitet werden. </li> <li> Der Abonnementstatus im Nutzerprofil kann nicht aktualisiert werden. </li></ul> {:/} | Der Zugriff auf diesen Bereich erfordert weiterhin die Berechtigung zum Anzeigen eines Nutzerprofils. |
| Benutzer-Import | Der Benutzer kann keine Dateien von der Seite **Benutzerimport** herunterladen. | |
| {::nomarkdown} <ul> <li> Segmente </li> <li> Kampagnen </li> <li> Canvas </li> </ul> {:/} | In der Dropdown-Liste **Benutzerdaten**: {::nomarkdown} <ul> <li> Dem Benutzer steht die Option <b>CSV-E-Mail-Adresse exportieren</b> nicht zur Verfügung. </li> <li> Bei der Auswahl von <b>„CSV-Export von Nutzerdaten“</b> werden dem Nutzer die oben genannten Standard- und angepassten Attribute in der CSV-Datei nicht zur Verfügung gestellt. </li> </ul> {:/} | |
| Interne Testgruppe | Der Benutzer hat keinen Zugriff auf die vorhergehenden Standardattribute eines Benutzers, der der internen Testgruppe hinzugefügt wurde. | |
| Protokoll der Nachrichtenaktivitäten | Der Nutzer:in hat keinen Zugriff auf die vorstehenden Standardattribute für Nutzer:innen, die im Protokoll der Nachrichtenaktivität identifiziert wurden. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Bei der Vorschau einer Nachricht wird die Berechtigung **„PII anzeigen“** nicht angewendet, sodass Nutzer:innen die [vorangehenden Standardattribute](#potential-pii-attributes) sehen können, wenn sie in der Nachricht über Liquid referenziert wurden.
{% endalert %}

## Einstellungen zum Löschen von Daten 

Mit dieser Einstellung können Sie festlegen, ob Braze bestimmte Felder während des Löschvorgangs für Nutzer:innen bei Ereignissen löschen soll. Diese Einstellungen wirken sich ausschließlich auf Daten von Nutzer:innen aus, die Braze gelöscht hat. 

Wenn ein Nutzer gelöscht wird, entfernt Braze alle PII aus den Ereignisdaten, behält aber die anonymisierten Daten für Analytics-Zwecke. Einige benutzerdefinierte Felder können PII enthalten, wenn Sie Nutzer:innen Informationen an Braze senden. Wenn diese Felder PII enthalten, können Sie sich dafür entscheiden, die Daten zu löschen, wenn Braze die Ereignisdaten für gelöschte Nutzer:innen anonymisiert. Wenn die Felder keine PII enthalten, können Sie sie für Analytics aufbewahren.

Sie sind für die Festlegung der richtigen Einstellungen für Ihren Workspace verantwortlich. Die beste Möglichkeit, die geeigneten Einstellungen zu ermitteln, besteht darin, sich mit internen Teams, die Event-Daten an Braze senden, und mit Teams, die Nachrichten-Extras in Braze verwenden, abzustimmen, um zu bestätigen, ob die Felder möglicherweise personenbezogene Daten enthalten.  

### Relevante Felder  

| Name oder Typ des Events | Feld | Anmerkungen |
| -------------------- | ------ | ----- |
| Angepasstes Event | Eigenschaften |  |
| Kauf-Event | Eigenschaften |  |
| Nachricht senden | message_extras | Mehrere Ereignistypen enthalten ein Feld `message_extras`. Die Einstellung gilt für alle Ereignistypen zum Senden von Nachrichten, die `message_extras` unterstützen, einschließlich der in Zukunft hinzukommenden Ereignistypen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**Die Löschung ist dauerhaft!** Wenn Sie sich dafür entscheiden, Felder aus Snowflake für gelöschte Nutzer:innen zu entfernen, gilt diese Einstellung für alle historischen Daten in Ihren Workspaces und alle Ereignisse für Nutzer:innen, die in Zukunft gelöscht werden. Nachdem Braze den Prozess zur Anwendung der Einstellungen auf historische Ereignisdaten für gelöschte Nutzer:innen durchgeführt hat, **können** Sie die Daten **nicht mehr wiederherstellen**.
{% endalert %}

### Einstellungen konfigurieren

Legen Sie die Standard-Einstellungen fest, indem Sie die Kontrollkästchen für alle Felder aktivieren, die Braze entfernen soll, wenn eine Nutzer:in gelöscht wird. Wählen Sie eines der Felder aus, die PII enthalten. Diese Einstellung gilt für alle aktuellen und zukünftigen Workspaces, es sei denn, Workspaces werden explizit zu einer Einstellungsgruppe hinzugefügt.

Um die Einstellungen nach Workspace anzupassen, können Sie Einstellungsgruppen mit anderen Einstellungen als dem Standard hinzufügen. Wir wenden die Standardeinstellungen auf alle Workspaces an, die nicht zu einer zusätzlichen Einstellungsgruppe hinzugefügt wurden, einschließlich der Workspaces, die in Zukunft erstellt werden.  

![Abschnitt „Einstellungen zur Datenlöschung“ mit aktivierter Umschaltfunktion zum Anpassen der Einstellungen zur Datenlöschung nach Workspace.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Fehlersuche 

### Probleme bei der Einrichtung der Zwei-Faktor-Authentifizierung (2FA)

Sollten Sie nach der erfolgreichen Eingabe Ihrer Telefonnummer für die 2FA in einer Schleife gefangen sein und zurück zur Seite der Anmeldung weitergeleitet werden, liegt dies wahrscheinlich daran, dass Sie die Telefonnummer beim ersten Versuch nicht überprüft haben. Um dieses Problem zu beheben, führen Sie bitte die folgenden Schritte aus:

1. Bitte deaktivieren Sie alle Werbeblocker.
2. Bitte aktivieren Sie Cookies in Ihren Browsereinstellungen.
3. Bitte starten Sie Ihren PC oder Laptop neu.
4. Bitte versuchen Sie erneut, die 2FA einzurichten.

Sollte das Problem nach diesen Schritten persistent sein, wenden Sie sich bitte an [den Support,]({{site.baseurl}}/braze_support/) um Unterstützung zu erhalten.

### Die Zwei-Faktor-Authentifizierung (2FA) kann nicht aktiviert werden.

Wenn 2FA aktiviert ist, jedoch nichts geschieht, wenn Sie den Button **„Enablement“** auswählen, kann dies daran liegen, dass Ihr Browser die Weiterleitung blockiert, die für die Übermittlung des Codes per SMS erforderlich ist. Im Folgenden finden Sie die Schritte zur Fehlerbehebung dieses Problems:

1. Bitte deaktivieren Sie vorübergehend alle Ad-Blocker, die Sie in Ihrem Browser aktiviert haben.
2. Bitte überprüfen Sie, ob Sie in Ihren Browsereinstellungen Drittanbieter-Cookies aktiviert haben.
3. Bitte versuchen Sie, die 2FA einzurichten.

### Der Bestätigungscode wird nicht gesendet.

Sollten Sie Probleme bei der Eingabe Ihrer Telefonnummer auf der Authy-Seite haben und keine SMS erhalten, befolgen Sie bitte die folgenden Schritte:

1. Installieren Sie die Authy-App auf Ihrem Smartphone und melden Sie sich beim Authy-Authentifikator an.
2. Bitte geben Sie Ihre Telefonnummer ein und überprüfen Sie die Authy-App auf etwaige Änderungen oder SMS-Benachrichtigungen.
3. Sollten Sie die SMS weiterhin nicht erhalten, versuchen Sie es bitte mit einer anderen Netzwerkverbindung, beispielsweise Ihrem Heimnetzwerk oder einem nicht-geschäftlichen WLAN. Unternehmensnetzwerke verfügen möglicherweise über Sicherheitsrichtlinien, die die SMS-Zustellung beeinträchtigen können.

Sollten die Probleme persistent sein, löschen Sie bitte das alte Profil in der Authy-App und scannen Sie den QR-Code erneut, um die 2FA einzurichten. Bitte stellen Sie sicher, dass Sie alle Werbeblocker deaktiviert, Drittanbieter-Cookies aktiviert oder einen anderen Browser verwendet haben, bevor Sie die Einrichtung erneut versuchen.