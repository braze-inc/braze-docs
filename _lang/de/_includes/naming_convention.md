Wir bei Braze **empfehlen dringend**, Benutzer-IDs, die auch als externe IDs bezeichnet werden, in einem [UUIDs und GUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier) Format zu benennen. UUIDs und GUIDs sind universell eindeutige Bezeichner, die aus einer 128-Bit-Zahl bestehen und zur Identifizierung von Informationen in Computersystemen verwendet werden. Das bedeutet, dass diese UUIDs lang, zufällig und gut verteilt sind. Wenn Sie eine andere Methode wählen, um Ihre Benutzer-IDs zu benennen, müssen diese ebenfalls lang, zufällig und gut verteilt sein. Beachten Sie bitte auch, dass bei Benutzer-IDs **zwischen Groß- und Kleinschreibung** unterschieden wird. Zum Beispiel ist "Abcdef" ein anderer Benutzer als "abcdef".

Wenn Sie feststellen, dass Ihre Benutzer-IDs Namen, E-Mail-Adressen, Zeitstempel oder Inkrementoren enthalten, empfehlen wir Ihnen, eine neue, sicherere Benennungsmethode zu verwenden, damit Ihre Benutzer-IDs nicht so leicht zu erraten oder nachzuahmen sind. Wenn Sie dies in Ihre Nutzer:innen IDs aufnehmen möchten, **empfehlen wir Ihnen dringend,** unser [SDK Authentifizierungs]({{site.baseurl}}/developer_guide/authentication/) Feature hinzuzufügen, um Nutzer:innen vor Identitätswechseln zu schützen.

Die Weitergabe dieser Informationen an Dritte kann es Personen außerhalb Ihres Unternehmens ermöglichen, Informationen über die Struktur Ihrer Benutzer-IDs zu erhalten, wodurch Ihr Unternehmen für potenziell böswillige Aktualisierungen oder die Entfernung von Informationen anfällig wird. Die Wahl der richtigen Namenskonvention von Anfang an ist einer der wichtigsten Schritte bei der Einrichtung von Benutzer-IDs. Eine Migration ist jedoch über unseren [externen ID-Migrationsendpunkt]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) möglich.

| Benutzer-ID Benennung |
| Empfohlen | Nicht empfohlen |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | Firmenname-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}