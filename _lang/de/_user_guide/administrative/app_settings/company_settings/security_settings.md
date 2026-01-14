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

Verwenden Sie dieses Feld, um festzulegen, wie lange Braze Ihre Sitzung aufrechterhalten soll. Nachdem Braze Ihre Sitzung für inaktiv hält (keine Aktivität für die festgelegte Anzahl von Minuten), wird der Benutzer abgemeldet. Die maximale Anzahl von Minuten, die Sie eingeben können, beträgt 10.080 (entspricht einer Woche), wenn die Zwei-Faktor-Authentifizierung für Ihr Unternehmen erzwungen wird. Andernfalls beträgt die maximale Sitzungsdauer 1.440 Minuten (entspricht 24 Stunden).

### Einmalige Anmeldung (SSO) Authentifizierung

Sie können Ihre Nutzer:innen daran hindern, sich mit einem Passwort oder SSO anzumelden.

Für [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) müssen Kund:innen ihre SAML-Einstellungen vor der Erzwingung einrichten. Wenn Kund:innen Google-SSO verwenden, müssen sie nur die Seite mit den Sicherheitseinstellungen anpassen, ohne dass ein zusätzlicher Lift erforderlich ist.

## Dashboard-IP-Allowlisting

Verwenden Sie das angezeigte Feld, um bestimmte IP-Adressen und Subnetze aufzulisten, von denen aus sich Benutzer bei Ihrem Konto anmelden können (z.B. von einem Firmennetzwerk oder VPN). Geben Sie IP-Adressen und Subnetze als CIDR-Bereiche in einer kommagetrennten Liste an. Wenn nicht angegeben, können sich Benutzer von jeder IP-Adresse aus anmelden.

## Zwei-Faktor-Authentifizierung (2FA)

Die Zwei-Faktor-Authentifizierung ist für alle Braze-Benutzer erforderlich. Es fügt eine zweite Ebene der Identitätsüberprüfung zu einem Kontoprotokoll hinzu und macht es damit sicherer als nur einen Benutzernamen und ein Passwort. Wenn Ihr Dashboard keine Zwei-Faktor-Authentifizierung unterstützt, wenden Sie sich an Ihren Customer-Success-Manager. 

Wenn die Zwei-Faktor-Authentifizierung aktiviert ist:

- Zusätzlich zur Eingabe eines Passworts müssen Nutzer:innen einen Code eingeben, wenn sie sich bei ihrem Braze-Konto anmelden. Der Code kann über eine Authentifizierungs-App, E-Mail oder SMS gesendet werden. 
- Das Kontrollkästchen **Dieses Konto 30 Tage lang speichern** wird für Nutzer:innen verfügbar.

Nutzer:innen, die die Zwei-Faktor-Authentifizierung nicht einrichten, werden von ihrem Braze-Konto ausgesperrt. Benutzer von Braze-Konten können die Zwei-Faktor-Authentifizierung auch selbst in den **Kontoeinstellungen** einrichten, selbst wenn dies nicht vom Administrator verlangt wird.

Achten Sie darauf, Ihre Änderungen zu speichern, bevor Sie die Seite verlassen!

### Merken Sie sich dieses Konto für 30 Tage {#remember-me}

Dieses Feature ist verfügbar, wenn die Zwei-Faktor-Authentifizierung aktiviert ist.

Wenn Sie **Dieses Konto 30 Tage lang speichern** auswählen, wird ein Cookie auf Ihrem Gerät gespeichert, so dass Sie sich im Laufe von 30 Tagen nur einmal mit der Zwei-Faktor-Authentifizierung anmelden müssen. 

\![Dieses Konto für 30 Tage speichern Checkbox]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Bei Kunden mit mehreren Konten unter einem Dashboard-Unternehmen können Probleme bei der Nutzung dieser Funktion auftreten, da das Cookie an ein bestimmtes Gerät gebunden ist. Wenn Benutzer dasselbe Gerät verwenden, um sich bei mehreren Konten anzumelden, wird das Cookie für die zuvor autorisierten Konten auf diesem Gerät ersetzt. Braze erwartet, dass nur ein Gerät mit einem Konto verknüpft wird, nicht ein Gerät für mehrere Konten.

### Benutzerauthentifizierung zurücksetzen

Wenn Sie Probleme haben, sich mit der Zwei-Faktor-Authentifizierung anzumelden, wenden Sie sich an die Administratoren Ihres Unternehmens, um die Zwei-Faktor-Authentifizierung zurückzusetzen. Administratoren können die folgenden Schritte durchführen:

1. Gehen Sie zu **Einstellungen** > **Firmenbenutzer**.
2. Wählen Sie den Benutzer aus der vorgegebenen Liste aus.
3. Wählen Sie **Zurücksetzen** unter **Zwei-Faktor-Authentifizierung**.

Ein Reset kann gängige Authentifizierungsprobleme lösen, wie z. B. Probleme mit Authentifizierungs-Apps, fehlende E-Mail-Verifizierung, fehlgeschlagene Anmeldung aufgrund von SMS-Ausfällen oder Benutzerfehlern und vieles mehr.

### Anforderungen für 2FA auf Unternehmensebene

Überprüfen Sie zunächst, ob 2FA für Ihr Dashboard aktiviert ist, indem Sie zu **Unternehmenseinstellungen** > **Sicherheitseinstellungen** > **Zwei-Faktor-Authentifizierung** gehen. Wenn das Kästchen grau umgeschaltet ist, wurde 2FA in Ihrem Unternehmen nicht aktiviert und ist nicht für alle Nutzer:innen des Dashboards Pflichtfeld.

#### Nutzer:innen Optionen, wenn 2FA nicht Pflichtfeld ist

Wenn 2FA nicht auf Unternehmensebene durchgesetzt wird, können einzelne Nutzer:innen 2FA für sich selbst auf ihrer Kontoeinstellungsseite einrichten. In diesem Fall werden die Nutzer:innen nicht von ihren Konten ausgesperrt, wenn sie es nicht einrichten. Sie können feststellen, welche Nutzer:innen sich für die Aktivierung von 2FA entschieden haben, indem Sie die Seite Nutzer:innen verwalten aufrufen.

#### Anforderungen, wenn 2FA ein Pflichtfeld ist

Wenn 2FA auf Unternehmensebene erzwungen wird, werden Nutzer:innen, die es bei der Anmeldung nicht für ihr eigenes Konto einrichten, vom Dashboard ausgesperrt. Nutzer:innen müssen die 2FA-Einrichtung abschließen, um den Zugang zu erhalten.

{% alert important %}
2FA ist für alle Braze Nutzer:innen nur dann erforderlich, wenn Single Sign-on (SSO) nicht aktiviert ist. Wenn SSO im Einsatz ist, muss 2FA nicht auf Unternehmensebene erzwungen werden.
{% endalert %}

## Zwei-Faktor-Authentifizierung (2FA) einrichten

### 2FA mit Authy einrichten

1. Laden Sie die Authy App aus dem App Shop Ihres Geräts herunter.
2. Geben Sie in Braze Ihre Rufnummer ein.
3. Tippen Sie auf die Benachrichtigung, die an Ihr Gerät gesendet wurde und Sie auffordert, die Authy App zu öffnen.
4. Starten Sie die Authy App auf Ihrem Gerät, um den Code abzurufen.
5. Geben Sie in Braze den Verifizierungscode ein, den Sie von Authy erhalten haben.

Wenn Sie während des Einrichtungsvorgangs auf Probleme stoßen und auf die Homepage von Braze oder den Anmeldebildschirm umgeleitet werden, versuchen Sie Folgendes:

- Verwenden Sie den Inkognito-Modus oder den privaten Browsing-Modus: Versuchen Sie die Einrichtung erneut in einem Inkognito-Fenster oder einem privaten Fenster. Damit können Sie Probleme umgehen, die durch Browser-Erweiterungen oder Plugins verursacht werden.
- Versuchen Sie ein anderes Browser-Profil: Wenn das Problem weiterhin besteht, sollten Sie ein anderes Browser-Profil verwenden, um Konflikte mit installierten Plugins zu vermeiden.

### 2FA einrichten, wenn sie nicht erzwungen wird

Um die Zwei-Faktor-Authentifizierung (2FA) auf Ihrem Braze-Konto manuell zu aktivieren, wenn sie nicht erzwungen wird, folgen Sie diesen Schritten:

1. Laden Sie eine 2FA App wie Authy, Google Authenticator, Okta Verify oder eine ähnliche App aus dem App Store (iOS), Google Play Store (Android) oder dem Internet herunter. Wenn Sie die 2FA lieber per E-Mail oder SMS einrichten möchten, fahren Sie mit Schritt 2 fort.
2. Gehen Sie in Braze zu Konto verwalten, blättern Sie zum Abschnitt **Zwei-Faktor-Authentifizierung** und wählen Sie **Einrichtung starten**.
3. Geben Sie Ihr Passwort in das Modal für die Anmeldung ein und wählen Sie dann **Passwort prüfen**.
4. Geben Sie im Modal **für die Einrichtung der Zwei-Faktor-Authentifizierung** Ihre Telefonnummer ein und wählen Sie dann **Enablement**.
5. Kopieren Sie den generierten siebenstelligen Code aus Ihrer 2FA App, E-Mail oder SMS-Nachricht, gehen Sie zurück zu Braze und fügen Sie ihn in das Modal **für die Einrichtung der Zwei-Faktor-Authentifizierung** ein. Wählen Sie **Überprüfen**.
6. (Optional) Um die Eingabe von 2FA für die nächsten 30 Tage zu vermeiden, aktivieren Sie die Option **Dieses Konto für 30 Tage speichern**.

## Erweiterter Zugriff

Elevated Access bietet eine zusätzliche Sicherheitsebene für sensible Aktionen in Ihrem Braze Dashboard. Wenn Sie aktiv sind, müssen Nutzer:innen ihr Konto erneut überprüfen, bevor sie ein Segment exportieren oder einen API-Schlüssel anzeigen können. Um den erweiterten Zugriff zu verwenden, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie die Option ein. 

Wenn ein Benutzer sich nicht erneut verifizieren kann, wird er an die Stelle zurückgeleitet, an der er aufgehört hat, und kann nicht mit der sensiblen Aktion fortfahren. Nachdem sie sich erfolgreich erneut verifiziert haben, brauchen sie dies in der nächsten Stunde nicht mehr zu tun - es sei denn, sie melden sich vorher ab.

\![Erhöhter Zugang umschalten.]({% image_buster /assets/img/elevated_access.png %})

## Herunterladen eines Sicherheitsberichts {#security-event-report}

Der Bericht über Sicherheitsereignisse ist ein CSV-Bericht über Sicherheitsereignisse wie Kontoeinladungen, Kontoentfernungen, fehlgeschlagene und erfolgreiche Anmeldeversuche und andere Aktivitäten. Sie können es für interne Audits verwenden.

Um diesen Bericht herunterzuladen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen**.
2. Wählen Sie die Registerkarte **Sicherheitseinstellungen** und gehen Sie zum Abschnitt **Download von Sicherheitsereignissen**.
2. Wählen Sie **Bericht herunterladen**. 

Dieser Bericht enthält nur die letzten 10.000 Sicherheitsereignisse für Ihr Konto. Wenn Sie bestimmte Daten zu einem Event benötigen, wenden Sie sich an den technischen Support.

{% details Reported security events %}

### Anmeldung und Konto 
- Eingetragen
- Anmeldung fehlgeschlagen
- Einrichtung der Zwei-Faktoren-Authentifizierung abgeschlossen
- Zurücksetzen der Zwei-Faktor-Authentifizierung abgeschlossen
- Freigegebene Entwickler:in 2FA
- Zusätzlicher Entwickler:in
- Hinzugefügtes Konto
- Entwickler:in suspendiert
- Entwickler:in Unsuspended
- Entwickler:in Aktualisiert
- Entfernte Entwickler:in
- Entferntes Konto
- Nutzer:innen Abo-Status aktualisiert
- Nutzer:in Aktualisiert

### Erhöhter Zugang
- Elevated Access Flow gestartet
- Erhöhter Zugang fertiggestellt
- Fehlgeschlagene 2FA-Überprüfung für erweiterten Zugang

### Kampagne
- Kampagne hinzugefügt
- Bearbeitete Kampagne

### Canvas
- Hinzugefügte Reise
- Bearbeitete Reise

### Segment
- Hinzugefügtes Segment
- Bearbeitetes Segment
- Exportierte Daten in CSV
- Exportierte Segmente über API

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

### Einstellungen des Unternehmens
- App-Gruppe hinzugefügt
- App hinzugefügt
- Firmeneinstellungen geändert

### E-Mail-Vorlage
- E-Mail Template hinzugefügt
- Aktualisierte E-Mail Template

### Push-Zugangsdaten
- Aktualisierte Push-Zugangsdaten
- Entfernte Push-Zugangsdaten

### SDK-Debugger
- Gestartete SDK Debugger Sitzung
- Exportiertes SDK Debugger Protokoll
{% enddetails %}

## Anzeige von persönlich identifizierbaren Informationen (PII) {#view-pii}

Die Berechtigung **PII anzeigen** ist nur für einige ausgewählte Braze-Benutzer zugänglich. Standardmäßig haben alle Administratoren die Berechtigung **PII anzeigen** in den Nutzer:innen-Berechtigungen aktiviert. Das bedeutet, dass sie alle standardmäßigen und angepassten Attribute, die Ihr Unternehmen als PII definiert hat, im gesamten Dashboard sehen können. Wenn diese Berechtigung für Nutzer:innen deaktiviert ist, können diese Nutzer:innen keines dieser Attribute sehen.

Informationen zu den bestehenden Teamberechtigungen finden Sie unter [Festlegen von Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### Definition von PII

{% alert important %}
Das Auswählen und Definieren bestimmter Felder als PII-Felder wirkt sich nur darauf aus, was Nutzer:innen auf dem Braze-Dashboard sehen können und hat keinen Einfluss darauf, wie die Daten der Endnutzer:innen in solchen PII-Feldern behandelt werden.<br><br>Wenden Sie sich an Ihr juristisches Team, um die Einstellungen Ihres Dashboards mit den für Ihr Unternehmen geltenden Datenschutzbestimmungen und -richtlinien abzustimmen, einschließlich derjenigen, die sich auf die [Bindung von Daten]({{site.baseurl}}/data_retention/) beziehen.
{% endalert %}

Sie können die Felder, die Ihr Unternehmen als PII bezeichnet, im Dashboard auswählen. Gehen Sie dazu zu **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen**.

Die folgenden Attribute können als PII gekennzeichnet und vor Nutzer:innen ausgeblendet werden, die nicht über die Berechtigung zum **Anzeigen von PII** verfügen.

| Standard-Attribute | Angepasste Attribute |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>E-Mail-Adresse </li> <li> Telefonnummer </li> <li> Vorname </li> <li> Nachname </li> <li> Geschlecht </li> <li> Geburtstag </li> <li> Geräte-IDs </li> <li> Letzter Standort </li> </ul> {:/} | {::nomarkdown} <ul> <li> Alle benutzerdefinierten Attribute<ul><li>Einzelne angepasste Attribute können als PII markiert werden, wenn Sie nicht alle Attribute ausblenden müssen.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Begrenzte Gebiete

Im Folgenden wird davon ausgegangen, dass alle Felder als PII eingestuft sind und dass es sich bei den genannten Nutzer:innen um diejenigen handelt, die die Braze-Plattform nutzen.

| Dashboard-Navigation | Ergebnis | Anmerkungen |
| -------------------- | ------ | ----- |
| Benutzer suchen | Der oder die Nutzer:in, der oder die sich anmeldet, kann nicht nach E-Mail-Adresse, Telefonnummer, Vorname oder Nachname suchen: {::nomarkdown} <ul> <li> Bei der Anzeige eines Benutzerprofils werden die vorangehenden Standard- und benutzerdefinierten Attribute nicht mehr angezeigt. </li> <li> Die vorangehenden Standardattribute eines Benutzerprofils können nicht über das Braze-Dashboard bearbeitet werden. </li> </ul> {:/} | Der Zugang zu diesem Bereich erfordert weiterhin den Zugang zur Ansicht des Benutzerprofils. |
| Benutzer-Import | Der Benutzer kann keine Dateien von der Seite **Benutzerimport** herunterladen. | |
| {::nomarkdown} <ul> <li> Segmente </li> <li> Kampagnen </li> <li> Canvas </li> </ul> {:/} | In der Dropdown-Liste **Benutzerdaten**: {::nomarkdown} <ul> <li> Dem Benutzer steht die Option <b>CSV-E-Mail-Adresse exportieren</b> nicht zur Verfügung. </li> <li> Wenn Sie <b>CSV-Benutzerdaten exportieren</b> wählen, werden dem Benutzer die vorangehenden Standard- und Kundenattribute in der CSV-Datei nicht zur Verfügung gestellt. </li> </ul> {:/} | |
| Interne Testgruppe | Der Benutzer hat keinen Zugriff auf die vorhergehenden Standardattribute eines Benutzers, der der internen Testgruppe hinzugefügt wurde. | |
| Protokoll der Nachrichtenaktivitäten | Der Nutzer:in hat keinen Zugriff auf die vorstehenden Standardattribute für Nutzer:innen, die im Protokoll der Nachrichtenaktivität identifiziert wurden. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Bei der Vorschau einer Nachricht wird die Berechtigung **PII anzeigen** nicht angewendet, so dass Nutzer:innen die vorangehenden Standardattribute sehen können, wenn sie in der Nachricht durch Liquid referenziert wurden.
{% endalert %}

## Einstellungen zum Löschen von Daten 

Mit dieser Einstellung können Sie festlegen, ob bestimmte Felder beim Löschen von Nutzer:innen für Events gelöscht werden sollen. Diese Einstellungen wirken sich nur auf Daten von Nutzer:innen aus, die von Braze gelöscht wurden. 

Wenn ein Nutzer gelöscht wird, entfernt Braze alle PII aus den Ereignisdaten, behält aber die anonymisierten Daten für Analytics-Zwecke. Einige benutzerdefinierte Felder können PII enthalten, wenn Sie Nutzer:innen Informationen an Braze senden. Wenn diese Felder personenbezogene Daten enthalten, können Sie sich dafür entscheiden, die Daten zu löschen, wenn die Ereignisdaten für gelöschte Benutzer anonymisiert werden; wenn die Felder keine personenbezogenen Daten enthalten, können sie für Analysen aufbewahrt werden.

Sie sind für die Festlegung der richtigen Einstellungen für Ihren Workspace verantwortlich. Die beste Möglichkeit, die geeigneten Einstellungen zu ermitteln, besteht darin, sich mit internen Teams, die Event-Daten an Braze senden, und mit Teams, die Nachrichten-Extras in Braze verwenden, abzustimmen, um zu bestätigen, ob die Felder möglicherweise personenbezogene Daten enthalten.  

### Relevante Felder  

| Name oder Typ des Events | Feld | Anmerkungen |
| -------------------- | ------ | ----- |
| Angepasstes Event | Eigenschaften |  |
| Kauf-Event | Eigenschaften |  |
| Nachricht senden | message_extras | Mehrere Ereignistypen enthalten ein Feld `message_extras`. Die Einstellung gilt für alle Ereignistypen zum Senden von Nachrichten, die `message_extras` unterstützen, einschließlich der in Zukunft hinzukommenden Ereignistypen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**Die Löschung ist dauerhaft!** Wenn Sie sich dafür entscheiden, Felder für gelöschte Nutzer aus Snowflake zu entfernen, gilt diese Einstellung für alle historischen Daten in Ihren Workspaces und alle Ereignisse für Nutzer:innen, die in Zukunft gelöscht werden. Nachdem Braze den Prozess zur Anwendung der Einstellungen auf historische Ereignisdaten für gelöschte Nutzer:innen ausgeführt hat, können die Daten **nicht wiederhergestellt werden**.
{% endalert %}

### Einstellungen konfigurieren

Legen Sie Standardeinstellungen fest, indem Sie Kästchen für Felder markieren, die entfernt werden sollen, wenn ein Benutzer gelöscht wird. Wählen Sie eines der Felder aus, die PII enthalten. Diese Einstellung gilt für alle aktuellen und zukünftigen Workspaces, es sei denn, die Workspaces werden explizit einer Einstellungsgruppe hinzugefügt.

Um die Einstellungen nach Workspace anzupassen, können Sie Einstellungsgruppen mit anderen Einstellungen als dem Standard hinzufügen. Wir wenden die Standardeinstellungen auf alle Workspaces an, die nicht zu einer zusätzlichen Einstellungsgruppe hinzugefügt wurden, einschließlich der Workspaces, die in Zukunft erstellt werden.  

\![Abschnitt Datenlöschungspräferenzen mit eingeschaltetem Umschalter zum Anpassen der Datenlöschungspräferenzen nach Workspace.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Fehlersuche 

### Probleme bei der Einrichtung der Zwei-Faktor-Authentifizierung (2FA)

Wenn Sie nach der erfolgreichen Eingabe Ihrer Telefonnummer für 2FA in einer Schleife gefangen sind und zur Anmeldeseite zurückgeleitet werden, liegt das wahrscheinlich daran, dass die Überprüfung beim ersten Versuch fehlgeschlagen ist. Um dieses Problem zu beheben, gehen Sie folgendermaßen vor:

1. Deaktivieren Sie alle Werbeblocker.
2. Aktivieren Sie Cookies in den Einstellungen Ihres Browsers.
3. Starten Sie Ihren PC oder Laptop neu.
4. Versuchen Sie erneut, 2FA einzurichten.

Wenn das Problem nach diesen Schritten weiterhin besteht, wenden Sie sich an den [Support]({{site.baseurl}}/braze_support/).

### Enablement der Zwei-Faktor-Authentifizierung (2FA) nicht möglich

Wenn 2FA aktiviert ist, aber nichts passiert, wenn Sie den **Enable** Button auswählen, kann es daran liegen, dass Ihr Browser die Umleitung blockiert, die zum Senden des Verifizierungscodes per SMS erforderlich ist. Hier finden Sie die Schritte zur Fehlerbehebung dieses Problems:

1. Schalten Sie vorübergehend alle Ad-Blocker aus, die Sie in Ihrem Browser aktiviert haben.
2. Vergewissern Sie sich, dass Sie die Drittanbieter-Cookies in Ihren Browsereinstellungen aktiviert haben.
3. Versuchen Sie, 2FA einzurichten.

### Der Verifizierungscode wird nicht gesendet

Wenn Sie Probleme bei der Eingabe Ihrer Telefonnummer auf der Authy-Seite haben und keine SMS erhalten, befolgen Sie diese Schritte:

1. Installieren Sie die Authy App auf Ihrem Telefon und melden Sie sich beim Authy Authentifikator an.
2. Geben Sie Ihre Telefonnummer ein und überprüfen Sie die Authy App auf eventuelle Änderungen oder SMS-Benachrichtigungen.
3. Wenn Sie die SMS immer noch nicht erhalten, versuchen Sie, eine andere Netzwerkverbindung zu verwenden, z. B. Ihr Heimnetzwerk oder ein unternehmensfremdes Wi-Fi. In Unternehmensnetzwerken können Sicherheitsrichtlinien gelten, die die SMS-Zustellung behindern.

Wenn die Probleme weiterhin bestehen, löschen Sie das alte Profil in der Authy App und scannen Sie den QR Code erneut, um 2FA einzurichten. Vergewissern Sie sich, dass Sie alle Werbeblocker deaktiviert, Drittanbieter-Cookies aktiviert oder einen anderen Browser verwendet haben, bevor Sie die Einrichtung erneut versuchen.