---
nav_title: Regex Referenzblatt
permalink: /regex_cheat_sheet/
hidden: true
---

# Regex Referenzblatt

Diese Seite dient als Kurzanleitung für reguläre Ausdrücke, gängige Token, Metasequenzen, allgemeine Token, Gruppenkonstanten und mehr.

{% tabs %}
{% tab Häufige Token %}

| Häufige Token |
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
| Klammerinhalt erfassen | `(...)` |
| Entspricht entweder a oder b | `(a|b)` |
| Null oder eins von einer | `a?` |
| Null oder mehr von einem | `a*` |
| Eine oder mehrere von a | `a+` |
| Genau 3 von a | `a{3}` |
| Zwischen 3 und 6 eines | `a{3,6}` |
| Anfang der Zeichenkette | `^` |
| Ende der Zeichenkette | `$` |
| Wortgrenze | `\n` |
| Kein-Wort-Grenze | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Metasequenz %}

| Meta-Sequenz |
| ------------- |
| Beliebige Unicode-Sequenzen, einschließlich Zeilenumbrüche | `\X` |
| Eine Dateneinheit zuordnen | `\C` |
| Unicode Zeilenumbrüche | `\R` |
| Vertikales Leerzeichen | `\v` |
| Negation von \\v | `\V` |
| Horizontales Leerzeichen | `\h` |
| Negation von \\h | `\H` |
| Übereinstimmung zurücksetzen | `\K` |
| n-tes Teilmuster abgleichen | `\n` |
| Unicode-Eigenschaft X | `\pX` |
| Negation von \\pX | `\PX` |
| Unicode-Eigenschaft oder Skript-Kategorie | `\p{...}` |
| Negation von \\p | `\P{...}` |
| Zitat; als Liberals behandeln | `\Q...|E` |
| Teilmuster 'name' abgleichen | `\k<name>` | 
| Teilmuster 'name' abgleichen | `\k'name'` | 
| Teilmuster 'name' abgleichen | `\k{name}` |
| n-tes Teilmuster abgleichen | `\gn` | 
| n-tes Teilmuster abgleichen | `\g{n}` |
| Rekurs auf n-te Erfassungsgruppe | `\g<n>` |
| Rekurs auf n-te Erfassungsgruppe | `\g'n'` |
| Entspricht dem n-ten relativen vorherigen Teilmuster | `\g{-n}` |
| Rekurs auf das n-te relativ auftauchende Unter-Muster | `\g<+n>` |
| n-ten relativen kommenden Einreicher abgleichen | `\g'+n'` |
| Rekursive Namenserfassungsgruppe | `'letter'` |
| Entspricht der zuvor benannten Erfassungsgruppe 'letter'. | `\g{letter}` |
| Rekurriert auf die Namenserfassungsgruppe 'Buchstabe' | `\g<letter>` |
| Hex-Zeichen YY | `\xYY` |
| Hex-Zeichen YYYY | `\x{YYYY}` |
| Oktalzeichen ddd | `\ddd` |
| Steuerzeichen Y | `\cY` |
| Backspace-Zeichen | `[\b]` |
| Macht jedes Zeichen wörtlich | `\` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Allgemeine Token %}

| Allgemeine Token |
| -------------- |
| Zeilenumbruch | `\n` |
| Wagenrücklauf | `\r` |
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
{% tab Gruppenkonstanten %}

| Gruppen-Konstanten |
| --------------- |
| Erfasst den Klammerinhalt | `(...)` |
| Entspricht entweder a oder b | `(a|b)` |
| Klammerinhalt abgleichen | `(?:...)` |
| Atomgruppierung (ohne Erfassung) | `(?>...)` |
| Teilmuster-Gruppennummer duplizieren | `(?|...)` |
| Kommentar | `(?#...)` |
| Für Groß- und Kleinschreibung | `(?i)` |
| Benannte Erfassungsgruppe | `(?'name'...)` |
| Benannte Erfassungsgruppe | `(?<name>...)` |
| Benannte Erfassungsgruppe | `(?P<name>...)` |
| Inline-Modifikatoren | `(?imsxXU)` |
| Bedingte Anweisungen | `(?(1)yes|no)` |
| Rekursive bedingte Anweisungen | `(?(R#)yes|no)` |
| Bedingte Anweisung | `(?(R&name)yes|no)` |
| Bedingtes Lookahead | `(?(?=...)yes|no)` |
| Bedingtes Lookbehind | `(?(?<=...)yes|no)` |
| Rekurs auf gesamtes Muster | `(?R)` |
| Rekurs auf erstes Teilmuster | `(?1)` |
| Rekurs auf erstes relatives Teilmuster | `(?+1)` |
| Rekurs auf Teilmuster 'Name' | `(?&name)` |
| Teilmuster 'Name' abgleichen | `(?P=name)` |
| Rekurs auf Teilmuster 'Name' | `(?P>name)` |
| Muster vor der Verwendung definieren | `(?(DEFINE)...)` |
| Positives Lookahead | `(?=...)` |
| Negatives Lookahead | `(?!...)` |
| Positiver Rückblick | `(?<=...)` |
| Negatives Lookbehind | `(?<!...)` |
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
| Zeilenumbruchmodifikator | `(*CR)` |
| Zeilenumbruchmodifikator | `(*LF)` |
| Zeilenumbruchmodifikator | `(*CRLF)` |
| Zeilenumbruchmodifikator | `(*ANYCRLF)` |
| Zeilenumbruchmodifikator | `(*ANY)` |
| Zeilenumbruchmodifikator | `\R` |
| Zeilenumbruchmodifikator | `(*BSR_ANYCRLF)` |
| Zeilenumbruchmodifikator | `(*BSR_UNICODE)` |
| Regex-Engine-Modifikator | `(*LIMIT_MATCH=x)` |
| Regex-Engine-Modifikator | `(*LIMIT_RECURSION=d)` |
| Regex-Engine-Modifikator | `(*NO_AUTO_POSSESS)` |
| Regex-Engine-Modifikator | `(*NO_START_OPT)` |
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
| Greedy Quantifier | `a*` |
| Fauler Quantifizierer | `a*?` |
| Possessive Quanitifer | `a*+` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Anker %}

| Anker |
| ------- |
| Match-Beginn | `\G` |
| Anfang der Zeichenkette | `^` |
| Ende der Zeichenkette | `$` |
| Anfang der Zeichenkette | `\A` |
| Ende der Zeichenkette | `\Z` |
| Absolutes Ende der Zeichenkette | `\z` |
| Wortgrenze | `\b` |
| Eine Nicht-Wort-Grenze | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Flags und Modifikatoren %}

| Flags und Modifikatoren |
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
| Vollständiger Match-Inhalt | `\0` |
| Inhalt der Erfassungsgruppe 1 | `\1 or $1` |
| Inhalt der Erfassungsgruppe `foo` | `${foo}` |
| Hexidezimale Ersatzwerte | `\x20, \x{06fa}` |
| Registerkarte | `\t` |
| Wagenrücklauf | `\r` |
| Zeilenumbruch | `\n` |
| Seitenvorschub | `\f` |
| Umwandlung von Großbuchstaben | `\U` |
| Umwandlung in Kleinbuchstaben | `\L` |
| Beliebige Transformation beenden | `\E` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

