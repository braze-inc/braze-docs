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

Die E-Mail-Validierung wird durchgeführt, wenn die E-Mail-Adresse eines Nutzers aktualisiert wurde oder über die API, den CSV-Upload oder das SDK in Braze importiert oder im Dashboard geändert wurde. Beachten Sie, dass Ihre E-Mail-Adressen keine Leerzeichen enthalten dürfen. Wenn Sie die API verwenden, führen Leerzeichen zu einem `400`-Fehler.

Braze akzeptiert bestimmte Zeichen nicht und erkennt sie als ungültig an. Wenn eine E-Mail gebounced wird, markiert Braze die E-Mail als ungültig, und der Status des Abos wird nicht geändert. Beachten Sie, dass die E-Mail nicht versendet werden kann, wenn sie nicht standardmäßige [ASCII-Zeichen](https://en.wikipedia.org/wiki/ASCII) enthält.

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

Diese Validierung ist nicht zu verwechseln mit einem Validierungsdienst. Dies ist eine Überprüfung, um zu überprüfen, ob die Syntax einer E-Mail-Adresse korrekt ist. Einer der Hauptgründe für die Verwendung dieses Validierungsverfahrens ist die Unterstützung internationaler Zeichen (wie UTF-8) im lokalen Teil der E-Mail-Adresse.

Bei der Überprüfung der E-Mail-Syntax werden sowohl der lokale als auch der Host-Teil einer E-Mail-Adresse geprüft. Der lokale Teil ist alles vor dem Asperand (@) und der Host-Teil ist alles nach dem Asperand. Zum Beispiel kann dieser lokale Teil einer E-Mail-Adresse mit jedem der zulässigen Zeichen beginnen und enden, außer mit einem Punkt (.). Beachten Sie, dass bei diesem Vorgang nur die Syntax der E-Mail-Adresse überprüft wird und nicht berücksichtigt wird, ob die Domäne einen gültigen MX-Server hat oder ob der Benutzer auf der aufgeführten Domäne existiert.

{% alert important %}
Wenn der Domain-Teil nicht standardmäßige ASCII-Zeichen enthält, muss er vor der Übergabe an Braze [mit Punycode kodiert](https://www.punycoder.com/) werden.
{% endalert %}

Wenn Braze eine Anfrage zum Hinzufügen eines Benutzers erhält und die E-Mail-Adresse als ungültig eingestuft wird, erhalten Sie eine Fehlerantwort in der API. Wenn Sie eine CSV-Datei hochladen, wird zwar ein Nutzer:innen angelegt, aber die E-Mail Adresse wird nicht hinzugefügt.

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

Wenn es sich bei dem Domain-Teil um eine Gmail-Adresse handelt, muss der lokale Teil mindestens zwei Zeichen lang sein und den oben aufgeführten regulären Ausdrücken entsprechen.

### Microsoft-Domänen

Wenn die Host-Domain "msn", "hotmail", "outlook" oder "live" enthält, wird der folgende reguläre Ausdruck verwendet, um den lokalen Teil zu validieren: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

Der lokale Teil der Microsoft-Adresse muss diesen Parametern entsprechen:

- Kann mit einem Buchstaben (a-z), einem Unterstrich (_), oder einer Zahl (0-9) beginnen.  
- Kann jedes alphanumerische Zeichen (a-z oder 0-9) oder einen Unterstrich enthalten (_)
- Kann die folgenden Zeichen enthalten: (.) oder (-)
- Kann nicht mit einem Punkt (.) beginnen
- Darf nicht zwei oder mehr aufeinanderfolgende Punkte (.) enthalten.
- Kann nicht mit einem Punkt (.) enden

Beachten Sie, dass der Validierungstest prüft, ob der lokale Teil, der dem "+" vorausgeht, mit dem regulären Ausdruck übereinstimmt.

## Regeln für die Validierung des Host-Teils

IPv4- oder IPv6-Adressen sind im Host-Teil einer E-Mail-Adresse nicht erlaubt. Die Top-Level-Domain (wie .com, .org, .net usw.) darf nicht vollständig numerisch sein.

Der folgende reguläre Ausdruck wird zur Validierung der Domain verwendet:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

Der Domänenname muss diesen Parametern entsprechen:

- Besteht aus zwei oder mehr durch Punkte getrennten Labels
	- Jeder Teil eines Domänennamens wird als "Label" bezeichnet. Zum Beispiel besteht der Domain-Name "example.com" aus dem Label "example" und dem Label "com".
- Muss mindestens einen Punkt (.) enthalten
- Kann nicht zwei oder mehr aufeinanderfolgende Perioden enthalten
- Jede durch einen Punkt getrennte Label muss:
	- Nur alphanumerische Zeichen (a-z oder 0-9) und den Bindestrich (-) enthalten
	- Beginnen Sie mit einem alphanumerischen Zeichen (a-z oder 0-9)
	- Ende mit einem alphanumerischen Zeichen (a-z oder 0-9)
	- Enthält 1 bis 63 Zeichen

### Zusätzliche Validierung erforderlich

Die endgültige Bezeichnung der Domain muss eine gültige Top-Level-Domain (TLD) sein, die durch alles nach dem letzten Punkt (.) bestimmt wird. Diese TLD sollte in der [TLD-Liste der ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) enthalten sein. Der Braze E-Mail-Validator prüft nur, ob die Syntax der E-Mail gemäß dem in diesem Abschnitt aufgeführten regulären Ausdruck korrekt ist. Es erkennt keine Tippfehler oder Adressen, die nicht existieren.

{% alert important %}
Unicode wird nur für den lokalen Teil der E-Mail Adresse akzeptiert. Unicode wird für den Domain-Teil nicht akzeptiert, aber er kann in Punycode kodiert werden.
{% endalert %}

