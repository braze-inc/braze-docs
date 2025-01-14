---
nav_title: Regex Referenzblatt
permalink: /regex_cheat_sheet/
hidden: true
---

# Regex Referenzblatt

Diese Seite dient als Kurzanleitung für reguläre Ausdrücke, einschließlich gängiger Token, Metasequenzen, allgemeiner Token, Gruppenkonstanten und mehr.

{% tabs %}
{% tab Gemeinsame Token %}

| Gemeinsame Token |
| ------------- |
| Ein einzelnes Zeichen aus: a, b oder c | `[abc]` |
| Ein Zeichen außer: a, b, oder c | `[^abc]` |
| Ein Zeichen aus dem Bereich: a-z | `[a-z]` |
| Ein Zeichen nicht im Bereich: a-z | `[^a-z]` |
| Ein Zeichen aus dem Bereich: a-z oder A-Z | `[a-zA-Z]` |
| Jedes einzelne Zeichen | `.` |
| Jedes beliebige Leerzeichen | `\s` |
| Jedes Zeichen, das kein Leerzeichen ist | `\S` |
| Beliebige Ziffer | `\d` |
| Jede nicht-ziffrige Stelle | `\D` |
| Jedes Wortzeichen | `\w` |
| Jedes Nicht-Wort-Zeichen | `\W` |
| Erfassen eingeschlossen | `(...)` |
| Entspricht entweder a oder b | `(a|b)` |
| Null oder eins von einer | `a?` |
| Null oder mehr von einem | `a*` |
| Eine oder mehrere von a | `a+` |
| Genau 3 von a | `a{3}` |
| Zwischen 3 und 6 eines | `a{3,6}` |
| Anfang der Zeichenkette | `^` |
| Ende der Zeichenkette | `$` |
| Eine Wort-Grenze | `\n` |
| Kein-Wort-Grenze | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Meta-Sequenz %}

| Meta-Sequenz |
| ------------- |
| Beliebige Unicode-Sequenzen, einschließlich Zeilenumbrüche | `\X` |
| Eine Dateneinheit zuordnen | `\C` |
| Unicode Zeilenumbrüche | `\R` |
| Vertikales Leerzeichen | `\v` |
| Negation von \\v | `\V` |
| Horizontales Leerzeichen | `\h` |
| Negation von \\h | `\H` |
| Spiel zurücksetzen | `\K` |
| Nächstes Teil-Muster abgleichen | `\n` |
| Unicode-Eigenschaft X | `\pX` |
| Negation von \\pX | `\PX` |
| Unicode-Eigenschaft oder Skript-Kategorie | `\p{...}` |
| Negation von \\p | `\P{...}` |
| Zitat; als Liberale behandeln | `\Q...|E` |
| Entspricht Teilmuster 'name' | `\k<name>` | 
| Entspricht Teilmuster 'name' | `\k'name'` | 
| Entspricht Teilmuster 'name' | `\k{name}` |
| Nächstes Teil-Muster abgleichen | `\gn` | 
| Nächstes Teil-Muster abgleichen | `\g{n}` |
| Rekurs auf die n-te Erfassungsgruppe | `\g<n>` |
| Rekurs auf die n-te Erfassungsgruppe | `\g'n'` |
| Entspricht dem n-ten relativen vorherigen Teilmuster | `\g{-n}` |
| Rekurs auf das n-te relativ auftauchende Unter-Muster | `\g<+n>` |
| n-ten relativen kommenden Einreicher abgleichen | `\g'+n'` |
| Rekursive Namen erfassen Gruppe | `'letter'` |
| Entspricht der zuvor benannten Capture-Gruppe 'letter'. | `\g{letter}` |
| Rekursiert Namen erfassen Gruppe 'Buchstabe' | `\g<letter>` |
| Hex-Zeichen YY | `\xYY` |
| Hex-Zeichen YYYY | `\x{YYYY}` |
| Oktalzeichen ddd | `\ddd` |
| Steuerzeichen Y | `\cY` |
| Backspace-Zeichen | `[\b]` |
| Macht jedes Zeichen wörtlich | `\` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Allgemeine Wertmarken %}

| Allgemeine Wertmarken |
| -------------- |
| Zeilenumbruch | `\n` |
| Kutschenrückfahrt | `\r` |
| Registerkarte | `\t` |
| Nullzeichen | `\0` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Charakterklassen-Modifikatoren %}

| Charakterklassen-Modifikatoren |
| ------------------------- |
| Ein einzelnes Zeichen aus: a, b oder c | `[abc]` |
| Ein Zeichen außer: a, b, oder c | `[^abc]` |
| Ein Zeichen aus dem Bereich: a-z | `[a-z]` |
| Ein Zeichen nicht im Bereich: a-z | `[^a-z]` |
| Ein Zeichen aus dem Bereich: a-z oder A-Z | `[a-zA-Z]` |
| Buchstaben und Ziffern | `[:alnum:]` |
| Briefe | `[:alpha:]` |
| ASCII-Codes 0-127 | `[:ascii:]` |
| Nur Leerzeichen oder Tabulator | `[:blank:]` |
| Steuerzeichen | `[:cntrl:]` |
| Ziffern | `[:digit:]` |
| Sichtbare Zeichen (kein Leerzeichen) | `[:word:]` |
| Kleinbuchstaben | `[:xdigit:]` |
| Großbuchstaben | `[:<:]` |
| Wortzeichen | `[:>:]` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Gruppen-Konstanten %}

| Gruppen-Konstanten |
| --------------- |
| Erfassen Sie alles, was eingeschlossen ist | `(...)` |
| Entspricht entweder a oder b | `(a|b)` |
| Passend zu allem, was beiliegt | `(?:...)` |
| Atomare Gruppierung (nicht fangend) | `(?>...)` |
| Doppelte Sub-Pattern-Gruppennummer | `(?|...)` |
| Kommentar | `(?#...)` |
| Für Groß- und Kleinschreibung | `(?i)` |
| Benannte Erfassungsgruppe | `(?'name'...)` |
| Benannte Erfassungsgruppe | `(?<name>...)` |
| Benannte Erfassungsgruppe | `(?P<name>...)` |
| Inline-Modifikatoren | `(?imsxXU)` |
| Bedingte Anweisungen | `(?(1)yes|no)` |
| Rekursive bedingte Anweisungen | `(?(R#)yes|no)` |
| Bedingte Anweisung | `(?(R&name)yes|no)` |
| Vorausschauend bedingt | `(?(?=...)yes|no)` |
| Bedingter Blick nach hinten | `(?(?<=...)yes|no)` |
| Gesamtes Muster rekursieren | `(?R)` |
| Rekurs auf das erste Untermuster | `(?1)` |
| Rekurs auf das erste relative Untermuster | `(?+1)` |
| Rekurs auf Untermuster 'Name' | `(?&name)` |
| Teilmuster 'Name' abgleichen | `(?P=name)` |
| Rekurs auf Untermuster 'Name' | `(?P>name)` |
| Muster vor der Verwendung vordefinieren | `(?(DEFINE)...)` |
| Positive Vorausschau | `(?=...)` |
| Negative Vorausschau | `(?!...)` |
| Positiver Rückblick | `(?<=...)` |
| Negative Rückblicke | `(?<!...)` |
| Verb kontrollieren | `(*ACCEPT)` |
| Verb kontrollieren | `(*FAIL)` |
| Verb kontrollieren | `(*MARK:NAME)` |
| Verb kontrollieren | `(*COMMIT)` |
| Verb kontrollieren | `(*PRUNE)` |
| Verb kontrollieren | `(*SKIP)` |
| Verb kontrollieren | `(*THEN)` |
| Muster Modifikator | `(*UTF)` |
| Muster Modifikator | `(*UTF8)` |
| Muster Modifikator | `(*UTF16)` |
| Muster Modifikator | `(*UTF32)` |
| Muster Modifikator | `(*UCP)` |
| Zeilenumbruch Modifikator | `(*CR)` |
| Zeilenumbruch Modifikator | `(*LF)` |
| Zeilenumbruch Modifikator | `(*CRLF)` |
| Zeilenumbruch Modifikator | `(*ANYCRLF)` |
| Zeilenumbruch Modifikator | `(*ANY)` |
| Zeilenumbruch Modifikator | `\R` |
| Zeilenumbruch Modifikator | `(*BSR_ANYCRLF)` |
| Zeilenumbruch Modifikator | `(*BSR_UNICODE)` |
| Regex Engine Modifikator | `(*LIMIT_MATCH=x)` |
| Regex Engine Modifikator | `(*LIMIT_RECURSION=d)` |
| Regex Engine Modifikator | `(*NO_AUTO_POSSESS)` |
| Regex Engine Modifikator | `(*NO_START_OPT)` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Quantoren %}

| Quantoren |
| ----------- |
| Null oder eins von einer | `a?` |
| Null oder mehr von einem | `a*` |
| Eine oder mehrere von a | `a+` |
| Genau 3 von a | `a{3}` |
| 3 oder mehr von einem | `a{3,}` |
| Zwischen 3 und 6 eines | `a{3,6}` |
| Gieriger Quantifizierer | `a*` |
| Fauler Quantifizierer | `a*?` |
| Possessivum quanitifer | `a*+` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Anker %}

| Anker |
| ------- |
| Beginn des Spiels | `\G` |
| Anfang der Zeichenkette | `^` |
| Ende der Zeichenkette | `$` |
| Anfang der Zeichenkette | `\A` |
| Ende der Zeichenkette | `\Z` |
| Absolutes Ende der Zeichenkette | `\z` |
| Eine Wort-Grenze | `\b` |
| Eine Nicht-Wort-Grenze | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Flaggen und Modifikatoren %}

| Flaggen und Modifikatoren |
| ------------------- | 
| Global | `g` |
| Mehrzeilig | `m` |
| Groß- und Kleinschreibung beachten | `l` |
| Whitespace ignorieren | `x` |
| Einzelne Zeile | `s` |
| Unicode | `u` |
| Erweitert | `X` |
| Ungeduldig | `U` |
| Anker | `A` |
| Doppelte Gruppennamen | `J` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Substitution %}

| Substitution |
| ------------ |
| Vollständiger Spielinhalt | `\0` |
| Inhalt der Erfassungsgruppe 1 | `\1 or $1` |
| Inhalt der Erfassungsgruppe `foo` | `${foo}` |
| Hexidezimale Ersatzwerte | `\x20, \x{06fa}` |
| Registerkarte | `\t` |
| Kutschenrückfahrt | `\r` |
| Zeilenumbruch | `\n` |
| Formular-Einzug | `\f` |
| Umwandlung von Großbuchstaben | `\U` |
| Umwandlung in Kleinbuchstaben | `\L` |
| Beenden Sie jede Transformation | `\E` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

