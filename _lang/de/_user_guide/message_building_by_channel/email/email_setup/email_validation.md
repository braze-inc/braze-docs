---
nav_title: E-Mail-Validierung
article_title: E-Mail-Validierung
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt die Validierungsregeln für den lokalen und den Host-Teil von E-Mail-Adressen."
channel: email

---

# E-Mail-Validierung

> Dieser Referenzartikel behandelt die Validierungsregeln für den lokalen und den Host-Teil von E-Mail-Adressen. Die Validierung wird für Dashboard-E-Mail-Adressen, Endbenutzer-E-Mail-Adressen (Ihre Kunden) sowie Absender- und Antwortadressen einer E-Mail-Nachricht verwendet.

## Funktionsweise

Braze validiert eine E-Mail Adresse, wenn sie aktualisiert, per API, CSV-Upload, SDK importiert oder im Dashboard geändert wird. E-Mail-Adressen dürfen keine Leerzeichen enthalten. Wenn Sie die API verwenden, gibt Whitespace einen `400` Fehler zurück.

Braze lehnt bestimmte Zeichen ab und markiert die Adresse als ungültig. Wenn eine E-Mail gebounct wird, markiert Braze die Adresse als ungültig und ändert den Status des Abos nicht. Wenn der Text der E-Mail nicht standardmäßige [ASCII-Zeichen](https://en.wikipedia.org/wiki/ASCII) enthält, sendet Braze die E-Mail nicht.

{% details Accepted characters %}
- Buchstaben (A-Z)
- Ziffern (0-9)
- Symbole
	- -
	- ^
	- +
	- $
	- '
	- &
	- #
	- /
	- %
	- *
	- =
	- \`
	- \|
	- ~
	- !
	- ?
	- . (nur zwischen Buchstaben oder anderen Zeichen)
{% enddetails %}

{% details Unaccepted characters %}
- Whitespaces (ASCII und Unicode)
{% enddetails %}

Bei dieser Überprüfung handelt es sich um eine Syntaxprüfung, nicht um einen Validierungsdienst. Ein Ziel dieses Prozesses ist die Unterstützung internationaler Zeichen (wie UTF-8) im lokalen Teil der E-Mail Adresse.

Braze überprüft die Syntax sowohl für den lokalen als auch für den Host-Teil einer E-Mail Adresse. Der lokale Teil ist alles, was vor dem Asperand (@) steht; der Host-Teil ist alles, was danach kommt. Der lokale Teil kann mit jedem zulässigen Zeichen außer einem Punkt (.) beginnen und enden. Dieser Prozess berücksichtigt nicht, ob die Domain einen gültigen MX Server hat oder ob ein Nutzer:innen in dieser Domain existiert.

{% alert important %}
Wenn der Domain-Teil nicht standardmäßige ASCII-Zeichen enthält, muss er vor der Übergabe an Braze [mit Punycode kodiert](https://www.punycoder.com/) werden.
{% endalert %}

Wenn Braze eine Anfrage zum Hinzufügen eines Nutzers:innen mit einer ungültigen E-Mail Adresse erhält, gibt die API einen Fehler zurück. Bei einem CSV-Upload erstellt Braze den Nutzer:innen, lässt aber die ungültige E-Mail Adresse weg.

## Regeln für die Validierung des lokalen Teils

### Allgemeine E-Mail-Überprüfung

Für die meisten Domänen muss der lokale Teil diesen Parametern entsprechen:
- Kann jeden Buchstaben, jede Zahl, einschließlich Unicode-Buchstaben und -Zahlen, sowie die folgenden Zeichen enthalten: (+) (&) (#) (_) (-) (^) oder (/)
- Kann das folgende Zeichen enthalten, darf aber nicht damit beginnen oder enden: (.)
- Kann keine doppelten Anführungszeichen enthalten (")
- Muss zwischen 1 und 64 Zeichen lang sein

Der folgende reguläre Ausdruck kann verwendet werden, um zu überprüfen, ob eine E-Mail-Adresse als gültig angesehen wird:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Gmail Adressen

Wenn es sich bei der Domain um Gmail handelt, muss der lokale Teil mindestens zwei Zeichen lang sein und den oben aufgeführten regulären Ausdrücken entsprechen.

### Microsoft-Domänen

Wenn die Host Domain "msn", "hotmail", "outlook" oder "live" enthält, verwendet Braze den folgenden regulären Ausdruck, um den lokalen Teil zu validieren: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

Der lokale Teil der Microsoft-Adresse muss diesen Parametern entsprechen:

- Kann mit einem Buchstaben (a-z), einem Unterstrich (_), oder einer Zahl (0-9) beginnen.  
- Kann jedes alphanumerische Zeichen (a-z oder 0-9) oder einen Unterstrich enthalten (_)
- Kann die folgenden Zeichen enthalten: (.) oder (-)
- Kann nicht mit einem Punkt (.) beginnen
- Darf nicht zwei oder mehr aufeinanderfolgende Punkte (.) enthalten.
- Kann nicht mit einem Punkt (.) enden

Der Validierungstest prüft, ob der lokale Teil vor dem "+" mit dem regulären Ausdruck übereinstimmt.

## Regeln für die Validierung des Host-Teils

Der Host-Teil kann keine IPv4- oder IPv6-Adresse sein. Die Top-Level-Domain (wie .com, .org, .net) kann nicht vollständig numerisch sein.

Der folgende reguläre Ausdruck wird zur Validierung der Domain verwendet:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

Der Domain-Name muss diese Parameter erfüllen:

- Besteht aus zwei oder mehr durch Punkte getrennten Labels
	- Jeder Teil eines Domänennamens wird als "Label" bezeichnet. Zum Beispiel besteht der Domain-Name "example.com" aus dem Label "example" und dem Label "com".
- Muss mindestens einen Punkt (.) enthalten
- Kann nicht zwei oder mehr aufeinanderfolgende Perioden enthalten
- Jede durch einen Punkt getrennte Label muss:
	- Enthält nur alphanumerische Zeichen (a-z oder 0-9) und den Bindestrich (-)
	- Beginnen Sie mit einem alphanumerischen Zeichen (a-z oder 0-9)
	- Ende mit einem alphanumerischen Zeichen (a-z oder 0-9)
	- Enthält 1 bis 63 Zeichen

### Zusätzliche Validierung erforderlich

Die endgültige Bezeichnung der Domain muss eine gültige Top-Level-Domain (TLD) sein, die durch alles nach dem letzten Punkt (.) bestimmt wird. Diese TLD sollte in der [TLD-Liste der ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) erscheinen. Der Braze Validator prüft nur die Syntax. Tippfehler oder nicht existierende Adressen werden nicht erkannt.

{% alert important %}
Unicode wird nur für den lokalen Teil der E-Mail Adresse akzeptiert. Unicode wird für den Domain-Teil nicht akzeptiert, aber er kann in Punycode kodiert werden.
{% endalert %}

