### Automatische Speicherung der anonymen Benutzerhistorie

| Identifizierung Kontext | Verhalten bei der Konservierung |
| ---------------------- | -------------------------- |
| Der Benutzer wurde zuvor **nicht** identifiziert | Der anonyme Verlauf wird bei der Identifizierung mit dem Benutzerprofil **zusammengeführt**. |
| Der Benutzer **wurde** zuvor in der App oder über die API identifiziert | Der anonyme Verlauf wird bei der Identifizierung **nicht** mit dem Benutzerprofil zusammengeführt. |
{: .reset-td-br-1 .reset-td-br-2}

Unter [Identifizierte Benutzerprofile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) finden Sie weitere Informationen darüber, was passiert, wenn Sie anonyme Benutzer identifizieren.

### Zusätzliche Hinweise und bewährte Verfahren

Beachten Sie das Folgende:

- Wenn Ihre App von mehreren Personen genutzt wird, können Sie jedem Benutzer einen eindeutigen Bezeichner zuweisen, um ihn zu verfolgen.
- Nachdem eine Benutzer-ID festgelegt wurde, können Sie diesen Benutzer nicht mehr in ein anonymes Profil zurückversetzen.
- Ändern Sie die Benutzer-ID nicht, wenn sich ein Benutzer abmeldet, da dies das Gerät vom Benutzerprofil trennen kann.
  - Infolgedessen können Sie den zuvor abgemeldeten Benutzer nicht mit Nachrichten zur Wiederanmeldung ansprechen. Wenn Sie mit mehreren Benutzern auf demselben Gerät rechnen, aber nur einen von ihnen ansprechen möchten, wenn sich Ihre App im abgemeldeten Zustand befindet, empfehlen wir Ihnen, die Benutzer-ID, die Sie ansprechen möchten, während Sie abgemeldet sind, separat zu verfolgen und im Rahmen des Abmeldevorgangs Ihrer App wieder zu dieser Benutzer-ID zu wechseln. Standardmäßig erhält nur der zuletzt eingeloggte Benutzer Push-Benachrichtigungen von Ihrer App.
- Der Wechsel von einem identifizierten Benutzer zu einem anderen ist ein relativ kostspieliger Vorgang.
  - Wenn Sie den Benutzerwechsel anfordern, wird die aktuelle Sitzung für den vorherigen Benutzer automatisch geschlossen und eine neue Sitzung gestartet. Braze wird automatisch eine Datenaktualisierungsanfrage für In-App-Nachrichten und andere Braze-Ressourcen für den neuen Benutzer stellen.

{% alert tip %}
Wenn Sie sich dafür entscheiden, einen Hash eine eindeutigen Bezeichner als Ihre Benutzer-ID zu verwenden, stellen Sie sicher, dass Sie die Eingabe für Ihre Hash-Funktion normalisieren. Wenn Sie z. B. einen Hash einer E-Mail-Adresse verwenden, sollten Sie sicherstellen, dass Sie führende und abschließende Leerzeichen aus der Eingabe entfernen und die Lokalisierung berücksichtigen.
{% endalert %}