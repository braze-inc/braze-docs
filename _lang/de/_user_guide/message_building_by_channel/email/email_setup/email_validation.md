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

Braze überprüft eine E-Mail-Adresse, wenn sie ein Update erhält, per API, CSV-Upload oder über das SDK importiert oder im Braze-Dashboard geändert wird. E-Mail-Adressen dürfen keine Leerzeichen enthalten. Bei Verwendung der API führt ein Leerzeichen zu einem`400`Fehler.

Braze lehnt bestimmte Zeichen ab und kennzeichnet die Adresse als ungültig. Wenn eine E-Mail zurückkommt, markiert Braze die Adresse als ungültig und ändert den Status des Abos nicht. Wenn der Textkörper der E-Mail nicht standardmäßige [ASCII](https://en.wikipedia.org/wiki/ASCII)-Zeichen enthält, versendet Braze die E-Mail nicht.

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

Diese Validierung ist eine Syntaxprüfung und kein Validierungsdienst. Ein Ziel dieses Prozesses ist es, internationale Zeichen (wie UTF-8) im lokalen Teil der E-Mail-Adresse zu unterstützen.

Braze überprüft die Syntax sowohl für den lokalen als auch für den Host-Teil einer E-Mail-Adresse. Der lokale Teil ist alles vor dem At-Zeichen (@); der Host-Teil ist alles danach. Der lokale Teil kann mit jedem zulässigen Zeichen außer einem Punkt (.) beginnen und enden. Bei diesem Vorgang wird nicht berücksichtigt, ob die Domain über einen gültigen MX-Server verfügt oder ob ein Nutzer:in in dieser Domain vorhanden ist.

{% alert important %}
Wenn der Domain-Teil nicht standardmäßige ASCII-Zeichen enthält, muss er vor der Übermittlung an Braze [in Punycode kodiert](https://www.punycoder.com/) werden.
{% endalert %}

Sollte Braze eine Anfrage zum Hinzufügen eines Nutzers mit einer ungültigen E-Mail-Adresse erhalten, gibt die API einen Fehler zurück. Bei einem CSV-Upload erstellt Braze den Nutzer:in, lässt jedoch die ungültige E-Mail-Adresse weg.

## Regeln für die Validierung des lokalen Teils

### Allgemeine E-Mail-Überprüfung

Für die meisten Domänen muss der lokale Teil diesen Parametern entsprechen:
- Kann beliebige Buchstaben und Zahlen enthalten, einschließlich Unicode-Zeichen sowie die folgenden Sonderzeichen: (+)(&)(#)(_)(-) (^) oder (/)
- Kann das folgende Zeichen enthalten, darf aber nicht damit beginnen oder enden: (.)
- Kann keine doppelten Anführungszeichen enthalten (")
- Muss zwischen 1 und 64 Zeichen lang sein

Der folgende reguläre Ausdruck kann verwendet werden, um zu überprüfen, ob eine E-Mail-Adresse als gültig angesehen wird:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Gmail Adressen

Wenn der Domain-Teil „Gmail“ lautet, muss der lokale Teil mindestens zwei Zeichen lang sein und der oben aufgeführten Validierung durch reguläre Ausdrücke entsprechen.

### Microsoft-Domänen

Wenn die Host-Domain „msn“, „hotmail“, „outlook“ oder „live“ enthält, verwendet Braze den folgenden regulären Ausdruck, um den lokalen Teil zu validieren: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

Der lokale Teil der Microsoft-Adresse muss diesen Parametern entsprechen:

- Kann mit einem Buchstaben (a-z), einem Unterstrich(_),oder einer Ziffer (0-9) beginnen.  
- Kann beliebige alphanumerische Zeichen (a-z oder 0-9) oder einen Unterstrich enthalten. (_)
- Kann die folgenden Zeichen enthalten: (.) oder (-)
- Kann nicht mit einem Punkt (.) beginnen
- Darf nicht zwei oder mehr aufeinanderfolgende Punkte (.) enthalten.
- Kann nicht mit einem Punkt (.) enden

Der Validierungstest überprüft, ob der lokale Teil vor dem „+“ mit dem regulären Ausdruck übereinstimmt.

## Regeln für die Validierung des Host-Teils

Der Hostteil darf keine IPv4- oder IPv6-Adresse sein. Die Top-Level-Domain (wie z. B. .com, .org, .net) darf nicht vollständig aus Zahlen bestehen.

Der folgende reguläre Ausdruck wird zur Validierung der Domain verwendet:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

Die Domain muss die folgenden Parameter erfüllen:

- Besteht aus zwei oder mehr durch Punkte getrennten Labels
	- Jeder Teil eines Domänennamens wird als "Label" bezeichnet. Zum Beispiel besteht der Domain-Name "example.com" aus dem Label "example" und dem Label "com".
- Muss mindestens einen Punkt (.) enthalten
- Kann nicht zwei oder mehr aufeinanderfolgende Perioden enthalten
- Jede durch einen Punkt getrennte Label muss:
	- Bitte verwenden Sie ausschließlich alphanumerische Zeichen (a-z oder 0-9) und den Bindestrich (-).
	- Beginnen Sie mit einem alphanumerischen Zeichen (a-z oder 0-9)
	- Ende mit einem alphanumerischen Zeichen (a-z oder 0-9)
	- Enthält 1 bis 63 Zeichen

### Zusätzliche Validierung erforderlich

Das letzte Label der Domain muss eine gültige Top-Level-Domain (TLD) sein, die durch alles nach dem letzten Punkt (.) bestimmt wird. Diese TLD sollte in [der TLD-Liste der ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) aufgeführt sein. Der Braze-Validator überprüft lediglich die Syntax. Es erkennt keine Tippfehler oder nicht existierende Adressen.

{% alert important %}
Unicode wird nur für den lokalen Teil der E-Mail Adresse akzeptiert. Unicode wird für den Domain-Teil nicht akzeptiert, aber er kann in Punycode kodiert werden.
{% endalert %}

