---
nav_title: Sicherheitseinstellungen
article_title: Sicherheitseinstellungen
page_order: 2
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

Verwenden Sie dieses Feld, um festzulegen, wie lange Braze Ihre Sitzung aufrechterhalten soll. Nachdem Braze Ihre Sitzung für inaktiv hält (keine Aktivität für die festgelegte Anzahl von Minuten), wird der Benutzer abgemeldet. Die maximale Anzahl der Minuten, die Sie eingeben können, beträgt 10.080 (entspricht einer Woche), wenn für Ihr Unternehmen eine Zwei-Faktor-Authentifizierung erzwungen wird. Andernfalls beträgt die maximale Sitzungsdauer 1.440 Minuten (entspricht 24 Stunden).

### Einmalige Anmeldung (SSO) Authentifizierung

Sie können Ihre Nutzer:innen daran hindern, sich mit einem Passwort oder SSO anzumelden.

Für [SAML-SSO][15] müssen Kund:innen ihre SAML-Einstellungen vor der Durchsetzung einrichten. Wenn Kund:innen Google-SSO verwenden, müssen sie nur die Seite mit den Sicherheitseinstellungen anpassen, ohne dass ein zusätzlicher Lift erforderlich ist.

## Dashboard-IP-Allowlisting

Verwenden Sie das angezeigte Feld, um bestimmte IP-Adressen und Subnetze aufzulisten, von denen aus sich Benutzer bei Ihrem Konto anmelden können (z.B. von einem Firmennetzwerk oder VPN). Geben Sie IP-Adressen und Subnetze als CIDR-Bereiche in einer kommagetrennten Liste an. Wenn nicht angegeben, können sich Benutzer von jeder IP-Adresse aus anmelden.

## Zwei-Faktor-Authentifizierung

Die Zwei-Faktor-Authentifizierung ist für alle Braze-Benutzer erforderlich. Es fügt eine zweite Ebene der Identitätsüberprüfung zu einem Kontoprotokoll hinzu und macht es damit sicherer als nur einen Benutzernamen und ein Passwort. Wenn Ihr Dashboard keine Zwei-Faktor-Authentifizierung unterstützt, wenden Sie sich an Ihren Customer-Success-Manager. 

Wenn die Zwei-Faktor-Authentifizierung aktiviert ist, müssen Benutzer zusätzlich zur Eingabe eines Passworts einen Verifizierungscode eingeben, wenn sie sich bei ihrem Braze-Konto anmelden. Der Code kann über eine Authentifizierungs-App, per E-Mail oder SMS gesendet werden.

Nutzer:innen, die die Zwei-Faktor-Authentifizierung nicht einrichten, werden von ihrem Braze-Konto ausgesperrt. Benutzer von Braze-Konten können die Zwei-Faktor-Authentifizierung auch selbst in den **Kontoeinstellungen** einrichten, selbst wenn dies nicht vom Administrator verlangt wird.

### Speichern

![Kontrollkästchen „Dieses Konto für 30 Tage merken“][04]{: style="float:right;max-width:40%;margin-left:15px;"}

Nachdem Sie die Zwei-Faktor-Authentifizierung für Ihr Unternehmen aktiviert haben, steht den Benutzern das Kontrollkästchen **Remember Me** zur Verfügung. Diese Funktion speichert ein Cookie auf Ihrem Gerät, so dass Sie sich nur einmal im Laufe von 30 Tagen mit der Zwei-Faktor-Authentifizierung anmelden müssen.

Bei Kunden mit mehreren Konten unter einem Dashboard-Unternehmen können Probleme bei der Nutzung dieser Funktion auftreten, da das Cookie an ein bestimmtes Gerät gebunden ist. Wenn Benutzer dasselbe Gerät verwenden, um sich bei mehreren Konten anzumelden, wird das Cookie für die zuvor autorisierten Konten auf diesem Gerät ersetzt. Braze erwartet, dass nur ein Gerät mit einem Konto verknüpft wird, nicht ein Gerät für mehrere Konten.

Achten Sie darauf, Ihre Änderungen zu speichern, bevor Sie die Seite verlassen!

### Benutzerauthentifizierung zurücksetzen

Benutzer, bei denen Probleme bei der Anmeldung mit der Zwei-Faktor-Authentifizierung auftreten, können sich an die Administratoren ihres Unternehmens wenden, um die Zwei-Faktor-Authentifizierung zurückzusetzen. Lassen Sie dazu einen Administrator die folgenden Schritte durchführen:

1. Gehen Sie zu **Einstellungen** > **Firmenbenutzer**.
2. Wählen Sie den Benutzer aus der vorgegebenen Liste aus.
3. Wählen Sie **Zurücksetzen** unter **Zwei-Faktor-Authentifizierung**.

Ein Reset kann gängige Authentifizierungsprobleme lösen, wie z. B. Probleme mit Authentifizierungs-Apps, fehlende E-Mail-Verifizierung, fehlgeschlagene Anmeldung aufgrund von SMS-Ausfällen oder Benutzerfehlern und vieles mehr.

## Erweiterter Zugriff

Elevated Access bietet eine zusätzliche Sicherheitsebene für sensible Aktionen in Ihrem Braze Dashboard. Wenn Sie aktiv sind, müssen Nutzer:innen ihr Konto erneut überprüfen, bevor sie ein Segment exportieren oder einen API-Schlüssel anzeigen können. Um den erweiterten Zugriff zu verwenden, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie die Option ein. 

Wenn ein Benutzer sich nicht erneut verifizieren kann, wird er an die Stelle zurückgeleitet, an der er aufgehört hat, und kann nicht mit der sensiblen Aktion fortfahren. Nachdem sie sich erfolgreich erneut verifiziert haben, brauchen sie dies in der nächsten Stunde nicht mehr zu tun - es sei denn, sie melden sich vorher ab.

![„Erweiterter Zugriff“-Umschalter.][5]

## Herunterladen eines Sicherheits-Event-Berichts

Der Bericht über Sicherheitsereignisse ist ein CSV-Bericht über Sicherheitsereignisse wie Kontoeinladungen, Kontoentfernungen, fehlgeschlagene und erfolgreiche Anmeldeversuche und andere Aktivitäten. Sie können es für interne Audits verwenden.

Um diesen Bericht herunterzuladen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen**.
2. Wählen Sie die Registerkarte **Sicherheitseinstellungen** und gehen Sie zum Abschnitt **Download von Sicherheitsereignissen**.
2. Wählen Sie **Bericht herunterladen**. 

Dieser Bericht enthält nur die letzten 10.000 Sicherheitsereignisse für Ihr Konto. Wenn Sie bestimmte Daten zu einem Event benötigen, wenden Sie sich an den technischen Support.

{% details Gemeldete Sicherheitsereignisse %}
### Anmeldung und Konto 
- Entfernte Entwickler:in
- Zusätzlicher Entwickler:in
- Eingetragen
- Anmeldung fehlgeschlagen
- Einrichtung der Zwei-Faktoren-Authentifizierung abgeschlossen
- Zurücksetzen der Zwei-Faktor-Authentifizierung abgeschlossen
- Freigegebene Entwickler:in 2FA
- Entwickler:in suspendiert
- Entwickler:in Unsuspended

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

Die Berechtigung **PII anzeigen** ist nur für einige ausgewählte Braze-Benutzer zugänglich. Informationen zu den bestehenden Teamberechtigungen finden Sie unter [Festlegen von Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

Standardmäßig ist für alle Administratoren die Berechtigung **PII anzeigen** in den [Benutzerrechten]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions) aktiviert. Das bedeutet, dass sie die folgenden standardmäßigen und angepassten Attribute auf dem Dashboard sehen können. Wenn diese Berechtigung für Benutzer deaktiviert ist, können diese Benutzer diese Informationen nicht sehen.

### Definition von PII

Sie können festlegen, welche Felder im Dashboard als PII bezeichnet werden. Gehen Sie dazu zu **Unternehmenseinstellungen** > **Sicherheitseinstellungen**.

Die folgenden Felder können von Braze-Benutzern ausgeblendet werden, die keine Berechtigung zum **Anzeigen von PII** haben.

| Standard-Attribute | Angepasste Attribute |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>E-Mail-Adresse </li> <li> Telefonnummer </li> <li> Vorname </li> <li> Nachname </li> <li> Geschlecht </li> <li> Geburtstag </li> <li> Geräte-IDs </li> <li> Letzter Standort </li> </ul> {:/} | {::nomarkdown} <ul> <li> Alle benutzerdefinierten Attribute<ul><li>Einzelne angepasste Attribute können als PII markiert werden, wenn Sie nicht alle Attribute ausblenden müssen.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Begrenzte Gebiete

Im Folgenden wird davon ausgegangen, dass alle Felder als personenbezogene Daten eingestellt sind und dass die genannten Benutzer diejenigen sind, die die Braze-Plattform nutzen.

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

Mit dieser Einstellung können Sie festlegen, ob bestimmte Felder beim Löschen von Nutzer:innen für Events gelöscht werden sollen. Diese Einstellungen wirken sich nur auf die Daten von Benutzern aus, die bei Braze gelöscht wurden. 

Wenn ein:e Nutzer:in gelöscht wird, entfernt Braze alle PII aus den Event-Daten, behält aber die anonymisierten Daten für Analysezwecke. Einige benutzerdefinierte Felder können PII enthalten, wenn Sie Nutzer:innen Informationen an Braze senden. Wenn diese Felder personenbezogene Daten enthalten, können Sie sich dafür entscheiden, die Daten zu löschen, wenn die Ereignisdaten für gelöschte Benutzer anonymisiert werden; wenn die Felder keine personenbezogenen Daten enthalten, können sie für Analysen aufbewahrt werden.

Sie sind für die Festlegung der richtigen Einstellungen für Ihren Workspace verantwortlich. Die beste Möglichkeit, die geeigneten Einstellungen zu ermitteln, besteht darin, sich mit internen Teams, die Event-Daten an Braze senden, und mit Teams, die Nachrichten-Extras in Braze verwenden, abzustimmen, um zu bestätigen, ob die Felder möglicherweise personenbezogene Daten enthalten.  

### Relevante Felder  

| Name oder Typ des Events | Feld | Anmerkungen |
| -------------------- | ------ | ----- |
| Angepasstes Event | Eigenschaften |  |
| Kauf-Event | Eigenschaften |  |
| Nachricht senden | message_extras | Mehrere Event-Typen enthalten ein message_extras-Feld. Die Einstellung gilt für alle Event-Typen zum Senden von Nachrichten, die message_extras unterstützen, einschließlich der in Zukunft hinzukommenden Event-Typen. |

{% alert warning %}
**Die Löschung ist dauerhaft!** Wenn Sie sich dafür entscheiden, Felder für gelöschte Nutzer aus Snowflake zu entfernen, gilt diese Einstellung für alle historischen Daten in Ihren Workspaces und alle Ereignisse für Nutzer:innen, die in Zukunft gelöscht werden. Nachdem Braze den Prozess zur Anwendung der Einstellungen auf historische Ereignisdaten für gelöschte Nutzer:innen ausgeführt hat, können die Daten **nicht wiederhergestellt werden**.
{% endalert %}

### Einstellungen konfigurieren

Legen Sie Standardeinstellungen fest, indem Sie Kästchen für Felder markieren, die entfernt werden sollen, wenn ein Benutzer gelöscht wird. Wählen Sie eines der Felder aus, die PII enthalten. Diese Einstellung gilt für alle aktuellen und zukünftigen Workspaces, es sei denn, die Workspaces werden explizit einer Einstellungsgruppe hinzugefügt.

Um die Präferenzen nach Arbeitsbereich anzupassen, können Sie Präferenzgruppen mit anderen Einstellungen als den Standardeinstellungen hinzufügen. Wir wenden die Standardeinstellungen auf alle Workspaces an, die nicht zu einer zusätzlichen Einstellungsgruppe hinzugefügt wurden, einschließlich der Workspaces, die in Zukunft erstellt werden.  

![Abschnitt „Präferenzen für die Datenlöschung“ mit eingeschaltetem Umschalter zum Anpassen der Präferenzen für die Datenlöschung nach Workspace.]({% image_buster /assets/img/deletion_preferences_1.png %})


[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "Benutzerprofil obfuscated1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "Nutzerprofil obfuscated2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "Nutzerprofil obfuscated3"
[5]: {% image_buster /assets/img/elevated_access.png %}
[04]: {% image_buster /assets/img/remember_me.png %}
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
