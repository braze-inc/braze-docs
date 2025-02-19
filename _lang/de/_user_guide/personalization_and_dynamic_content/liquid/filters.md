---
nav_title: Filter
article_title: Flüssigkeitsfilter
page_order: 3
description: "Auf dieser Seite finden Sie Filter zur Neuformatierung statischer oder dynamischer Inhalte."

---

# Filter

> Dieser Artikel enthält eine Übersicht zu Liquid-Filtern und beschreibt, welche Filter von Braze unterstützt werden. Suchen Sie nach Ideen, wie Sie diese Filter einsetzen können? Dann schauen Sie sich doch mal die [Liquid-Anwendungsfälle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) an.

Mit Filtern können Sie die Ausgabe von Zahlen, Strings, Variablen und Objekten in Liquid verändern. Sie können Filter verwenden, um statischen oder dynamischen Text umzuformatieren, also z.B. einen String von Kleinbuchstaben in Großbuchstaben umzuwandeln oder mathematische Berechnungen wie Addition oder Division durchzuführen.

{% alert important %}
Braze unterstützt nicht alle Liquid-Filter von Shopify. Auf dieser Seite werden die von Braze getesteten Liquid Filter aufgelistet. Die Liste ist allerdings nicht vollständig. Testen Sie Ihr Liquid immer, bevor Sie eine Nachricht verschicken. <br><br>Wenn Sie Fragen zu einem Filter haben, der hier nicht aufgeführt ist, wenden Sie sich bitte an Ihren Customer Success Manager.
{% endalert %}

## Filtersyntax

{% raw %}

Filter müssen in dem Output-Tag `{{ }}` platziert werden und werden durch einen senkrechten Strich `|` gekennzeichnet.

{% endraw %}

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

In diesem Beispiel ist `Big Sale` eine Zeichenkette und `upcase` der Filter, der angewendet wird.

### Syntax für mehrere Filter

Sie können mehrere Filter auf eine Ausgabe anwenden. Sie werden von links nach rechts angewendet.

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Array-Filter

Array-Filter werden verwendet, um die Ausgabe von Arrays zu verändern.

| Filter               | Definition                                                                                                         | Unterstützt |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join][1.1]          | Verbindet die Elemente eines Arrays mit dem als Parameter übergebenen Zeichen. Das Ergebnis ist eine einzelne Zeichenkette.          | ✅ Ja   |
| [first][1.2]         | Gibt das erste Element eines Arrays zurück. In einem benutzerdefinierten Attribut-Array ist dies der älteste hinzugefügte Wert.                | ✅ Ja   |
| [last][1.3]          | Gibt das letzte Element eines Arrays zurück. In einem benutzerdefinierten Attribut-Array ist dies der zuletzt hinzugefügte Wert.          | ✅ Ja   |
| [compact][1.4]       | Entfernt alle `nil` Elemente aus einem Array.                                                                             | ✅ Ja   |
| [concat][1.5]        | Kombiniert ein Array mit einem anderen Array.                                                                              | ✅ Ja   |
| [index][1.6]         | Gibt das Element an der angegebenen Indexposition in einem Array zurück. Das erste Element in einem Array wird mit `[0]` referenziert. | ✅ Ja   |
| [map][1.7]           | Akzeptiert das Attribut eines Array-Elements als Parameter und erstellt ein Array aus den Werten der einzelnen Array-Elemente.        | ✅ Ja   |
| [reverse][1.8]       | Kehrt die Reihenfolge der Elemente in einem Array um.                                                                       | ✅ Ja   |
| [size][1.9]          | Gibt die Größe einer Zeichenkette (die Anzahl der Zeichen) oder eines Arrays (die Anzahl der Elemente) zurück.                      | ✅ Ja   |
| [sort][1.10]         | Sortiert die Elemente eines Arrays nach einem bestimmten Attribut eines Elements im Array.                                    | ✅ Ja   |
| [sort_natural][1.11] | Sortiert die Elemente in einem Array unabhängig von der Groß-/Kleinschreibung in alphabetischer Reihenfolge.                                                | ✅ Ja   |
| [uniq][1.12]         | Entfernt alle doppelten Instanzen von Elementen in einem Array.                                                           | ✅ Ja   |
| [where][1.13]        | Filtert ein Array auf Einträge mit einem bestimmten Eigenschaftswert.                                             | ✅ Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Farbfilter

[Farbfilter][2.1] werden in Braze nicht unterstützt.

## Schriftart-Filter

[Schriftfilter][3.1] werden in Braze nicht unterstützt.

## Mathe-Filter

Mit den mathematischen Filtern können Sie mathematische Operationen durchführen. Wenn Sie mehrere Filter anwenden, werden diese von links nach rechts angewendet.

| Filter  | Definition      | Unterstützt |
| :------ |:----------------| :-------- |
| [abs][4.1]        | Gibt den absoluten Wert einer Zahl zurück.     | ✅ Ja   |
| [at_most][4.2]    | Begrenzt eine Zahl auf einen Maximalwert.   | ✅ Ja   |
| [at_least][4.3]   | Begrenzt eine Zahl auf einen Mindestwert.   | ✅ Ja   |
| [ceil][4.4]       | Rundet eine Ausgabe auf die nächste Ganzzahl auf.  | ✅ Ja   |
| [divided_by][4.5] | Dividiert eine Ausgabe durch eine Zahl. Die Ausgabe wird auf die nächstliegende Ganzzahl abgerundet. Beachten Sie den folgenden Tipp, um Rundungen zu vermeiden. | ✅ Ja   |
| [floor][4.6]      | Rundet eine Ausgabe auf die nächste Ganzzahl ab.        | ✅ Ja   |
| [minus][4.7]      | Subtrahiert eine Zahl von einer Ausgabe.          | ✅ Ja   |
| [plus][4.8]       | Fügt eine Zahl zu einer Ausgabe hinzu.     | ✅ Ja   |
| [round][4.9]      | Rundet die Ausgabe auf die nächste Ganzzahl oder die nächste angegebene Anzahl von Dezimalstellen.  | ✅ Ja   |
| [Male][4.10]     | Multipliziert eine Ausgabe mit einer Zahl.       | ✅ Ja   |
| [modulo][4.11]    | Dividiert eine Ausgabe durch eine Zahl und gibt den Rest zurück.   | ✅ Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Wenn Sie in Liquid ganze Zahlen durch ganze Zahlen dividieren, rundet Liquid automatisch auf die nächste ganze Zahl ab, wenn die Antwort eine Fließkommazahl ist. Wenn Sie jedoch ganze Zahlen durch Fließkommazahlen dividieren, erhalten Sie immer eine Fließkommazahl. Das bedeutet, dass Sie Ganzzahlen in Gleitkommazahlen (1,0, 2,0, 3,0) umwandeln können, um eine Gleitkommazahl zu erhalten.
{% raw %}
<br><br>Zum Beispiel wird bei `{{15 | divided_by: 2}}` `7` ausgeben, während `{{15 | divided_by: 2.0}}` `7.5` ausgibt.
{% endraw %}
{% endalert %}

### Mathematische Operationen mit benutzerdefinierten Attributen

Denken Sie daran, dass Sie keine mathematischen Berechnungen zwischen zwei angepassten Attributen durchführen können.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Dieses Beispiel würde nicht funktionieren, da Sie nicht mehrere benutzerdefinierte Attribute in einer Zeile von Liquid referenzieren können. Stattdessen müssen Sie mindestens einem dieser Werte eine Variable zuweisen, bevor die mathematischen Funktionen ausgeführt werden. Das Hinzufügen von zwei benutzerdefinierten Attributen würde zwei Zeilen Liquid erfordern:

1. Eines, um das angepasste Attribut einer Variablen zuzuweisen
2. Eines, das die Addition durchführt.

#### Anwendungsfall: Saldenberechnung

Nehmen wir an, wir möchten den aktuellen Kontostand eines Benutzers berechnen, indem wir sein Geschenkkartenguthaben und sein Prämienguthaben addieren.

1. Verwenden Sie das Tag `assign`, um das angepasste Attribut `current_rewards_balance` durch den Begriff "Saldo" zu ersetzen. Nun haben Sie eine Variable namens `balance`, die Sie bearbeiten können.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2\. Verwenden Sie den Filter `plus`, um das Geschenkkartenguthaben jedes Nutzers:innen mit seinem Rewards-Guthaben zu kombinieren, das durch das Objekt `{{balance}}` gekennzeichnet ist.
{% endraw %}
{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Geldfilter

Wenn Sie einen Benutzer über seine Einkäufe, seinen Kontostand oder irgendetwas anderes, das mit Geld zu tun hat, informieren möchten, sollten Sie Geldfilter verwenden. Geldfilter stellen sicher, dass Ihre Dezimalstellen an der richtigen Stelle stehen und dass kein Teil Ihrer Aktualisierung verloren geht (wie das lästige `0` am Ende).

| Filter         | Definition          | Unterstützt |
| :--------------- | :--------------- | :-------- |
| [money][5.1]      | Formatiert Zahlen, um sicherzustellen, dass die Dezimalstellen an der richtigen Stelle stehen und keine Nullen am Ende der Zahlen weggelassen werden.   | ✅ Ja   |
| [money_with_currency][5.2]    | Formatiert Zahlen mit dem Währungssymbol.     | ⛔ Nein    |
| [money_without_currency][5.4]     | Formatiert Zahlen ohne das Währungssymbol.      | ⛔ Nein    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Um eine Zahl mit dem Filter `money` richtig zu formatieren, entfernen Sie alle Kommas in der Zahl und fügen den Filter `plus: 0` vor dem Filter `money` ein. Als Beispiel das folgende Liquid:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Geldfilter bei Shopify und Braze

{% alert warning %}
Das Verhalten des `money`-Filters von Shopify unterscheidet sich von Braze. In den folgenden Beispielen finden Sie eine genaue Darstellung des erwarteten Verhaltens.
{% endalert %}

{% raw %}
Wenn Sie ein benutzerdefiniertes Attribut (wie `account_balance`) eingeben, sollten Sie immer den Filter `money` verwenden, um die Dezimalstellen an die richtige Stelle zu setzen und zu verhindern, dass Nullen am Ende einer Zahl wegfallen:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| MIT DEM GELDFILTER                       | OHNE DEN GELDFILTER                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Mit Geldfilter][1]                     | ![Ohne Geldfilter][2]                  |
| Dabei ist `account_balance` die Eingabe auf `17.8`. | Dabei ist `account_balance` die Eingabe auf `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Der Filter `money` in Braze unterscheidet sich von Shopify, da er die Dezimalpunkte nicht automatisch entsprechend einer Voreinstellung anwendet. Als Beispiel folgendes Szenario, in dem `rewards_redeemed` den Wert `145` enthält:

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Laut dem [Geldfilter][5.1] von Shopify sollte dies eine Ausgabe von `$1.45` haben, in Braze wird dies jedoch eine Ausgabe von `$145.00` haben. Als Behelfslösung kann die Zahl mit dem Filter `divided_by` in eine Dezimalzahl umgewandelt werden, bevor der Geldfilter angewendet wird:

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## String-Filter

String-Filter werden verwendet, um Ausgaben und Variablen von Strings zu verändern. Strings sind eine Kombination aus alphanumerischen Zeichen und müssen in gerade Anführungszeichen eingeschlossen werden.

{% alert note %}
Gerade Anführungszeichen unterscheiden sich von geschweiften Anführungszeichen in Liquid. Seien Sie vorsichtig, wenn Sie Liquid aus einem Texteditor in Braze kopieren und einfügen, da geschweifte Anführungszeichen zu Fehlern in Ihrem Liquid führen können. Wenn Sie Ihr Liquid direkt in Braze schreiben, werden automatisch gerade Anführungszeichen verwendet.
{% endalert %}

| Filter          | Beschreibung     | Unterstützt |
| :--------------- | ------------- | --------- |
| [append][6.1]     | Hängt Zeichen an eine Zeichenkette an.           | ✅ Ja   |
| [camelcase][6.2]     | Konvertiert eine Zeichenkette in CamelCase.             | ⛔ Nein    |
| [capitalize][6.3]     | Schreibt das erste Wort in einer Zeichenkette groß und verkleinert die übrigen Zeichen.         | ✅ Ja   |
| [downcase][6.4]      | Wandelt eine Zeichenkette in Kleinbuchstaben um.         | ✅ Ja   |
| [escape][6.5]    | Entfernt eine Zeichenkette.             | ✅ Ja   |
| [handle/handleize][6.6]        | Formatiert eine Zeichenkette in ein Handle.        | ⛔ Nein    |
| [md5][6.7]    | Konvertiert eine Zeichenkette in einen MD5-Hash. Weitere Informationen finden Sie unter [Kodierungsfilter][3] ].   | ✅ Ja   |
| [sha1][6.8]    | Konvertiert eine Zeichenkette in einen SHA-1-Hash. Weitere Informationen finden Sie unter [Kodierungsfilter][3] ].  | ✅ Ja   |
| hmac_sha1_hex<br>(previously [hmac_sha_1][6.10]) | Konvertiert einen String in einen SHA-1 Hash unter Verwendung eines Hash Message Authentication Code (HMAC). Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter. Weitere Informationen finden Sie unter [Kodierungsfilter][3] ]. | ✅ Ja   |
| [hmac_sha256][6.11]    | Konvertiert einen String per Hash Message Authentication Code (HMAC) in einen SHA-256-Hash Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter.       | ✅ Ja   |
| hmac_sha512 | Konvertiert einen String per Hash Message Authentication Code (HMAC) in einen SHA-512-Hash Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter. | ✅ Ja  |
| [newline_to_br][6.12]     | Fügt ein `<br>` Zeilenumbruch-HTML-Tag vor jedem Zeilenumbruch in einer Zeichenkette ein.        | ✅ Ja   |
| [pluralize][6.13]   | Gibt die Singular- oder Pluralversion einer englischen Zeichenkette basierend auf dem Wert einer Zahl aus.      | ⛔ Nein    |
| [vorangestellt.][6.14]     | Stellt einer Zeichenkette Zeichen voran.      | ✅ Ja   |
| [remove][6.15]      | Entfernt alle Vorkommen einer Teilzeichenkette aus einer Zeichenkette.       | ✅ Ja   |
| [remove_first][6.16]    | Entfernt nur das erste Vorkommen einer Teilzeichenkette aus einer Zeichenkette.      | ✅ Ja   |
| [replace][6.17]        | Ersetzt alle Vorkommen einer Zeichenkette durch eine Teilzeichenkette.   | ✅ Ja   |
| [replace_first][6.18]        | Ersetzt das erste Vorkommen einer Zeichenkette durch eine Teilzeichenkette.      | ✅ Ja   |
| [slice][6.19]       | Der Slice-Filter gibt eine Teilzeichenkette zurück, die mit dem angegebenen Index beginnt.       | ✅ Ja   |
| [split][6.20]  | Der Split-Filter verwendet einen Teilstring als Parameter. Der Teilstring dient als Begrenzer, der einen String in ein Array unterteilt.            | ✅ Ja   |
| [strip][6.21]   | Entfernt Tabulatoren, Leerzeichen und Zeilenumbrüche (alle Leerzeichen) von der linken und rechten Seite einer Zeichenkette.                                                                                                    | ✅ Ja   |
| [lstrip][6.22]     | Entfernt Tabulatoren, Leerzeichen und Zeilenumbrüche (alle Leerzeichen) von der linken Seite einer Zeichenkette.    | ⛔ Nein    |
| [rstrip][6.23]             | Entfernt Tabulatoren, Leerzeichen und Zeilenumbrüche (alle Leerzeichen) von der rechten Seite einer Zeichenkette.          | ⛔ Nein    |
| [strip_html][6.24]         | Entfernt alle HTML-Tags aus einer Zeichenkette.        | ✅ Ja   |
| [strip_newlines][6.25]  | Entfernt alle Zeilenumbrüche/Neuzeilen aus einer Zeichenkette.        | ✅ Ja   |
| [truncate][6.26]    | Schneidet eine Zeichenkette auf die Anzahl der Zeichen ab, die als erster Parameter übergeben wurde. Ein Auslassungszeichen (...) wird an die abgeschnittene Zeichenfolge angehängt und in die Zeichenzählung einbezogen.    | ✅ Ja   |
| [truncatewords][6.27]   | Schneidet eine Zeichenkette auf die Anzahl der Wörter ab, die als erster Parameter übergeben wurde. Eine Ellipse (...) wird an die abgeschnittene Zeichenfolge angehängt.    | ✅ Ja   |
| [upcase][6.28]   | Konvertiert eine Zeichenkette in Großbuchstaben.      | ✅ Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Zusätzliche Filter

Die folgenden allgemeinen Filter dienen unterschiedlichen Zwecken wie der Formatierung oder Konvertierung von Inhalten.

| Filter                | Beschreibung                                                                                                                      | Unterstützt |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date][7.1]           | Konvertiert einen Zeitstempel in ein anderes Datumsformat. Weitere Informationen finden Sie unter [Datumsfilter](#date-filter).         | ✅ Ja   |
| [default][7.2]        | Legt einen Standardwert für jede Variable fest, der kein Wert zugewiesen ist. Kann mit Strings, Arrays und Hashes verwendet werden.      | ✅ Ja   |
| [format_address][7.3] | Formatiert Adressen nach dem jeweiligen Gebietsschema.        | ⛔ Nein    |
| [highlight][7.4]      | Fasst Wörter in Suchergebnissen in das HTML-Tag `<strong>` mit der Klasse highlight ein, wenn sie mit den eingegebenen Suchbegriffen übereinstimmen. | ⛔ Nein    |
| `time_zone`             | Siehe [Zeitzonenfilter](#time-zone-filter).     | ✅ Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere unterstützte Filter, wie z.B. Kodierungs- und URL-Filter, finden Sie auf unserer Seite [Erweiterte Filter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Datum-Filter {#date-filter}

Der Filter `date` kann verwendet werden, um Zeitstempel in ein anderes Datumsformat zu konvertieren. Mit dem Filter `date` können Sie den Zeitstempel neu formatieren. Beispiele für diese Parameter finden Sie unter [strfti.me](http://www.strfti.me/).

Beispiel: Der Wert von `date_attribute` ist der Zeitstempel `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

Zusätzlich zu den `strftime` Formatierungsoptionen unterstützt Braze mit dem Datumsfilter `%s` auch die Umwandlung von Zeitstempeln in Unix-Zeit. Hier ein Beispiel, wie Sie das `date_attribute` in Unix-Zeit umwandeln:

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Zeitzonenfilter {#time-zone-filter}

{% raw %}
Zusätzlich zu den Filtern, die Sie in der Shopify-Dokumentation finden, unterstützt Braze auch den Filter `time_zone`.

Der Filter `time_zone` nimmt eine Zeit, eine Zeitzone und ein Datumsformat und gibt die Zeit in dieser Zeitzone im angegebenen Datumsformat zurück. Angenommen, der Wert von `{{custom_attribute.$date_attribute}}}` ist `2021-08-04 9:00:00 UTC`:
{% endraw %}

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Sie können auch die reservierte Variable `now` verwenden, um das aktuelle Datum und die Uhrzeit zu erhalten und zu bearbeiten.

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
2021-08-04 18:13:13
```
{% endraw %}
{% endtab %}
{% endtabs %}


[1.1]: https://shopify.dev/api/liquid/filters/array-filters#join
[1.2]: https://shopify.dev/api/liquid/filters/array-filters#first
[1.3]: https://shopify.dev/api/liquid/filters/array-filters#last
[1.4]: https://shopify.dev/api/liquid/filters#compact
[1.5]: https://shopify.dev/api/liquid/filters/array-filters#concat
[1.6]: https://shopify.dev/api/liquid/filters/array-filters#index
[1.7]: https://shopify.dev/api/liquid/filters/array-filters#map
[1.8]: https://shopify.dev/api/liquid/filters/array-filters#reverse
[1.9]: https://shopify.dev/api/liquid/filters/array-filters#size
[1.10]: https://shopify.dev/api/liquid/filters/array-filters#sort
[1.11]: https://shopify.dev/api/liquid/filters#sort_natural
[1.12]: https://shopify.dev/api/liquid/filters/array-filters#uniq
[1.13]: https://shopify.dev/api/liquid/filters#where

[2.1]: https://shopify.dev/api/liquid/filters/color-filters
[3.1]: https://shopify.dev/api/liquid/filters/font-filters

[4.1]: https://shopify.dev/api/liquid/filters/math-filters#abs
[4.2]: https://shopify.dev/api/liquid/filters/math-filters#at_most
[4.3]: https://shopify.dev/api/liquid/filters/math-filters#at_least
[4.4]: https://shopify.dev/api/liquid/filters/math-filters#ceil
[4.5]: https://shopify.dev/api/liquid/filters/math-filters#divided_by
[4.6]: https://shopify.dev/api/liquid/filters/math-filters#floor
[4.7]: https://shopify.dev/api/liquid/filters/math-filters#minus
[4.8]: https://shopify.dev/api/liquid/filters/math-filters#plus
[4.9]: https://shopify.dev/api/liquid/filters/math-filters#round
[4.10]: https://shopify.dev/api/liquid/filters/math-filters#times
[4.11]: https://shopify.dev/api/liquid/filters/math-filters#modulo

[5.1]: https://shopify.dev/api/liquid/filters/money-filters#money
[5.2]: https://shopify.dev/api/liquid/filters/money-filters#money_with_currency
[5.3]: https://shopify.dev/api/liquid/filters/money-filters#money_without_trailing_zeros
[5.4]: https://shopify.dev/api/liquid/filters/money-filters#money_without_currency

[6.1]: https://shopify.dev/api/liquid/filters/string-filters#append
[6.2]: https://shopify.dev/api/liquid/filters/string-filters#camelcase
[6.3]: https://shopify.dev/api/liquid/filters/string-filters#capitalize
[6.4]: https://shopify.dev/api/liquid/filters/string-filters#downcase
[6.5]: https://shopify.dev/api/liquid/filters/string-filters#escape
[6.6]: https://shopify.dev/api/liquid/filters/string-filters#handle-handleize
[6.7]: https://shopify.dev/api/liquid/filters/string-filters#md5
[6.8]: https://shopify.dev/api/liquid/filters/string-filters#sha1
[6.10]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1
[6.11]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha256
[6.12]: https://shopify.dev/api/liquid/filters/string-filters#newline_to_br
[6.13]: https://shopify.dev/api/liquid/filters/string-filters#pluralize
[6.14]: https://shopify.dev/api/liquid/filters/string-filters#prepend
[6.15]: https://shopify.dev/api/liquid/filters/string-filters#remove
[6.16]: https://shopify.dev/api/liquid/filters/string-filters#remove_first
[6.17]: https://shopify.dev/api/liquid/filters/string-filters#replace
[6.18]: https://shopify.dev/api/liquid/filters/string-filters#replace_first
[6.19]: https://shopify.dev/api/liquid/filters/string-filters#slice
[6.20]: https://shopify.dev/api/liquid/filters/string-filters#split
[6.21]: https://shopify.dev/api/liquid/filters/string-filters#strip
[6.22]: https://shopify.dev/api/liquid/filters/string-filters#lstrip
[6.23]: https://shopify.dev/api/liquid/filters/string-filters#rstrip
[6.24]: https://shopify.dev/api/liquid/filters/string-filters#strip_html
[6.25]: https://shopify.dev/api/liquid/filters/string-filters#strip_newlines
[6.26]: https://shopify.dev/api/liquid/filters/string-filters#truncate
[6.27]: https://shopify.dev/api/liquid/filters/string-filters#truncatewords
[6.28]: https://shopify.dev/api/liquid/filters/string-filters#upcase

[7.1]: https://shopify.dev/api/liquid/filters/additional-filters#date
[7.2]: https://shopify.dev/api/liquid/filters/additional-filters#default
[7.3]: https://shopify.dev/api/liquid/filters/additional-filters#format_address
[7.4]: https://shopify.dev/api/liquid/filters/additional-filters#highlight


[1]: {% image_buster /assets/img/with_money_filter.png %}
[2]: {% image_buster /assets/img/without_money_filter.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters
