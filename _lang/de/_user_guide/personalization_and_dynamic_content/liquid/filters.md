---
nav_title: Filter
article_title: Liquid-Filter
page_order: 3
description: "Auf dieser Referenzseite finden Sie Filter zur Neuformatierung statischer oder dynamischer Inhalte."

---

# Filter

> Dieser Referenzartikel enthält eine Übersicht zu Filtern in Liquid und beschreibt, welche Filter von Braze unterstützt werden. Suchen Sie nach Ideen, wie Sie diese Filter einsetzen können? Dann schauen Sie sich unsere [Liquid-Anwendungsfallbibliothek]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) an.

Mit Filtern können Sie die Ausgabe von Zahlen, Strings, Variablen und Objekten in Liquid verändern. Sie können Filter verwenden, um statischen oder dynamischen Text umzuformatieren, also z. B. einen String von Kleinbuchstaben in Großbuchstaben umzuwandeln oder mathematische Berechnungen wie Addition oder Division durchzuführen.

{% alert important %}
Braze unterstützt nicht alle Liquid-Filter von Shopify. Auf dieser Seite werden die von Braze getesteten Liquid-Filter aufgelistet. Die Liste ist allerdings möglicherweise nicht vollständig. Testen Sie Ihr Liquid immer, bevor Sie Nachrichten verschicken. <br><br>Wenn Sie Fragen zu einem Filter haben, der hier nicht aufgeführt ist, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Filtersyntax

{% raw %}

Filter müssen innerhalb eines Output-Tags `{{ }}` platziert werden und werden durch einen senkrechten Strich `|` gekennzeichnet.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

In diesem Beispiel ist `Big Sale` ein String und `upcase` der angewendete Filter.

{% alert note %}
Filter können in `assign`-Anweisungen und Output-Tags {% raw %}(`{{ }}`){% endraw %} verwendet werden, aber nicht in Bedingungen (`if`, `elsif`, `unless`), `case`/`when`, `for`-Schleifen oder Array-Zugriffsklammern. Um einen gefilterten Wert in einem dieser Kontexte zu verwenden, weisen Sie das Ergebnis zuerst einer Variablen zu. Weitere Details finden Sie unter [Wo Operatoren und Filter verwendet werden können]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Syntax für mehrere Filter

Sie können mehrere Filter auf eine Ausgabe anwenden. Sie werden von links nach rechts angewendet.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
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
| [join](https://shopify.dev/docs/api/liquid/filters/join)          | Verbindet die Elemente eines Arrays mit dem als Parameter übergebenen Zeichen. Das Ergebnis ist ein einzelner String.          | ✅  Ja   |
| [first](https://shopify.dev/docs/api/liquid/filters/first)         | Gibt das erste Element eines Arrays zurück. In einem angepassten Attribut-Array ist dies der älteste hinzugefügte Wert.                | ✅  Ja   |
| [last](https://shopify.dev/docs/api/liquid/filters/last)          | Gibt das letzte Element eines Arrays zurück. In einem angepassten Attribut-Array ist dies der zuletzt hinzugefügte Wert.          | ✅  Ja   |
| [compact](https://shopify.dev/api/liquid/filters/compact)       | Entfernt alle `nil`-Elemente aus einem Array.                                                                             | ✅  Ja   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | Kombiniert ein Array mit einem anderen Array.                                                                              | ✅  Ja   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Gibt das Element an der angegebenen Indexposition in einem Array zurück. Das erste Element in einem Array wird mit `[0]` referenziert. | ⛔  Nein   |
| [map](https://shopify.dev/api/liquid/filters/map)           | Akzeptiert das Attribut eines Array-Elements als Parameter und erstellt ein Array aus den Werten der einzelnen Array-Elemente.        | ✅  Ja   |
| [reverse](https://shopify.dev/api/liquid/filters/reverse)       | Kehrt die Reihenfolge der Elemente in einem Array um.                                                                       | ✅  Ja   |
| [size](https://shopify.dev/api/liquid/filters/size)          | Gibt die Größe eines Strings (die Anzahl der Zeichen) oder eines Arrays (die Anzahl der Elemente) zurück.                      | ✅  Ja   |
| [slice](https://shopify.dev/api/liquid/filters/slice)        | Gibt einen Teilstring eines Strings oder eine Teilmenge eines Arrays zurück, beginnend mit dem angegebenen Index.                          | ✅  Ja   |
| [sort](https://shopify.dev/api/liquid/filters/sort)         | Sortiert die Elemente eines Arrays nach einem bestimmten Attribut eines Elements im Array.                                    | ✅  Ja   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Sortiert die Elemente in einem Array unabhängig von der Groß-/Kleinschreibung in alphabetischer Reihenfolge.                                                | ✅  Ja   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Entfernt alle doppelten Instanzen von Elementen in einem Array.                                                           | ✅  Ja   |
| [where](https://shopify.dev/api/liquid/where)        | Filtert ein Array auf Einträge mit einem bestimmten Eigenschaftswert.                                             | ✅  Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Farbfilter

[Farbfilter](https://shopify.dev/api/liquid/filters/color-filters) werden in Braze nicht unterstützt.

## Schriftart-Filter

[Schriftart-Filter](https://shopify.dev/api/liquid/filters/font-filters) werden in Braze nicht unterstützt.

## Mathe-Filter

Mit den mathematischen Filtern können Sie mathematische Operationen durchführen. Wenn Sie mehrere Filter auf eine Ausgabe anwenden, werden diese von links nach rechts angewendet.

| Filter  | Definition      | Unterstützt |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Gibt den absoluten Wert einer Zahl zurück.     | ✅  Ja   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Begrenzt eine Zahl auf einen Maximalwert.   | ✅  Ja   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Begrenzt eine Zahl auf einen Mindestwert.   | ✅  Ja   |
| [ceil](https://shopify.dev/api/liquid/filters/ceil)       | Rundet eine Ausgabe auf die nächste Ganzzahl auf.  | ✅  Ja   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Dividiert eine Ausgabe durch eine Zahl. Die Ausgabe wird auf die nächstliegende Ganzzahl abgerundet. Beachten Sie den folgenden Tipp, um Rundungen zu vermeiden. | ✅  Ja   |
| [floor](https://shopify.dev/api/liquid/filters/floor)      | Rundet eine Ausgabe auf die nächste Ganzzahl ab.        | ✅  Ja   |
| [minus](https://shopify.dev/api/liquid/filters/minus)      | Subtrahiert eine Zahl von einer Ausgabe.          | ✅  Ja   |
| [plus](https://shopify.dev/api/liquid/filters/plus)       | Addiert eine Zahl zu einer Ausgabe.     | ✅  Ja   |
| [round](https://shopify.dev/api/liquid/filters/round)      | Rundet die Ausgabe auf die nächste Ganzzahl oder die angegebene Anzahl von Dezimalstellen.  | ✅  Ja   |
| [times](https://shopify.dev/api/liquid/filters/times)     | Multipliziert eine Ausgabe mit einer Zahl.       | ✅  Ja   |
| [modulo](https://shopify.dev/api/liquid/filters/modulo)    | Dividiert eine Ausgabe durch eine Zahl und gibt den Rest zurück.   | ✅  Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Wenn Sie in Liquid ganze Zahlen durch ganze Zahlen dividieren, rundet Liquid automatisch auf die nächste ganze Zahl ab, wenn das Ergebnis eine Gleitkommazahl ist. Wenn Sie jedoch ganze Zahlen durch Gleitkommazahlen dividieren, erhalten Sie immer eine Gleitkommazahl. Das bedeutet, dass Sie Ganzzahlen in Gleitkommazahlen (1.0, 2.0, 3.0) umwandeln können, um eine Gleitkommazahl zu erhalten.
{% raw %}
<br><br>Zum Beispiel gibt `{{15 | divided_by: 2}}` den Wert `7` aus, während `{{15 | divided_by: 2.0}}` den Wert `7.5` ausgibt.
{% endraw %}
{% endalert %}

### Mathematische Operationen mit angepassten Attributen

Beachten Sie, dass Sie keine mathematischen Berechnungen zwischen zwei angepassten Attributen durchführen können.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Dieses Beispiel würde nicht funktionieren, da Sie nicht mehrere angepasste Attribute in einer Zeile Liquid referenzieren können. Stattdessen müssen Sie mindestens einem dieser Werte eine Variable zuweisen, bevor die mathematischen Funktionen ausgeführt werden. Das Addieren von zwei angepassten Attributen erfordert zwei Zeilen Liquid:

1. Eine, um das angepasste Attribut einer Variablen zuzuweisen,
2. Eine, um die Addition durchzuführen.

#### Anwendungsfall: Aktuellen Kontostand berechnen

Nehmen wir an, wir möchten den aktuellen Kontostand einer Nutzerin oder eines Nutzers berechnen, indem wir das Geschenkkartenguthaben und das Rewards-Guthaben addieren.

1. Verwenden Sie das Tag `assign`, um das angepasste Attribut `current_rewards_balance` durch den Begriff „balance" zu ersetzen. Nun haben Sie eine Variable namens `balance`, die Sie bearbeiten können.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2. Verwenden Sie den Filter `plus`, um das Geschenkkartenguthaben jeder Nutzerin bzw. jedes Nutzers mit dem Rewards-Guthaben zu kombinieren, das durch das Objekt `{{balance}}` dargestellt wird.
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Geldfilter

Wenn Sie Nutzer:innen über ihre Einkäufe, ihren Kontostand oder irgendetwas anderes informieren möchten, das mit Geld zu tun hat, sollten Sie Geldfilter verwenden. Geldfilter stellen sicher, dass Ihre Dezimalstellen an der richtigen Stelle stehen und dass kein Teil Ihres Updates verloren geht (wie die lästige `0` am Ende).

| Filter         | Definition          | Unterstützt |
| :--------------- | :--------------- | :-------- |
| [money](https://shopify.dev/api/liquid/filters/money)      | Formatiert Zahlen, um sicherzustellen, dass die Dezimalstellen an der richtigen Stelle stehen und keine Nullen am Ende der Zahlen weggelassen werden.   | ✅  Ja   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formatiert Zahlen mit dem Währungssymbol.     | ⛔  Nein    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formatiert Zahlen ohne das Währungssymbol.      | ⛔  Nein    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Um eine Zahl mit dem Filter `money` richtig zu formatieren, entfernen Sie alle Kommas in der Zahl und fügen Sie den Filter `plus: 0` vor dem Filter `money` ein. Beispiel:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Shopify-Geldfilter vs. Braze-Geldfilter

{% alert warning %}
Das Verhalten des Shopify-Filters `money` unterscheidet sich von der Verwendung in Braze. In den folgenden Beispielen finden Sie eine genaue Darstellung des erwarteten Verhaltens.
{% endalert %}

{% raw %}
Wenn Sie ein angepasstes Attribut (wie `account_balance`) eingeben, sollten Sie immer den Filter `money` verwenden, um die Dezimalstellen an die richtige Stelle zu setzen und zu verhindern, dass Nullen am Ende einer Zahl wegfallen:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| MIT DEM GELDFILTER                       | OHNE DEN GELDFILTER                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Mit Geldfilter]({% image_buster /assets/img/with_money_filter.png %})                     | ![Ohne Geldfilter]({% image_buster /assets/img/without_money_filter.png %})                  |
| Dabei wird `account_balance` mit `17.8` eingegeben. | Dabei wird `account_balance` mit `17.8` eingegeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Der Filter `money` in Braze unterscheidet sich von Shopify, da er die Dezimalpunkte nicht automatisch entsprechend einer Voreinstellung anwendet. Nehmen wir als Beispiel folgendes Szenario, in dem `rewards_redeemed` den Wert `145` enthält:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Laut dem [Geldfilter](https://shopify.dev/api/liquid/filters/money) von Shopify sollte die Ausgabe `$1.45` lauten, in Braze wird jedoch `$145.00` ausgegeben. Als Behelfslösung können Sie die Zahl mit dem Filter `divided_by` in eine Dezimalzahl umwandeln, bevor der Geldfilter angewendet wird:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
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
Gerade Anführungszeichen unterscheiden sich von typografischen Anführungszeichen in Liquid. Seien Sie vorsichtig, wenn Sie Liquid aus einem Texteditor in Braze kopieren und einfügen, da typografische Anführungszeichen zu Fehlern in Ihrem Liquid führen können. Wenn Sie Ihr Liquid direkt in Braze schreiben, werden automatisch gerade Anführungszeichen verwendet.
{% endalert %}

| Filter          | Beschreibung     | Unterstützt |
| :--------------- | ------------- | --------- |
| [append](https://shopify.dev/api/liquid/filters/append)     | Hängt Zeichen an einen String an.           | ✅  Ja   |
| [camelize](https://shopify.dev/docs/api/liquid/filters/camelize)     | Konvertiert einen String in CamelCase.             | ⛔  Nein    |
| [capitalize](https://shopify.dev/api/liquid/filters/capitalize)     | Schreibt das erste Wort in einem String groß und wandelt die übrigen Zeichen in Kleinbuchstaben um.         | ✅  Ja   |
| [downcase](https://shopify.dev/api/liquid/filters/downcase)      | Wandelt einen String in Kleinbuchstaben um.         | ✅  Ja   |
| [escape](https://shopify.dev/api/liquid/filters/escape)    | Escaped einen String.             | ✅  Ja   |
| [handleize](https://shopify.dev/api/liquid/filters/handleize)        | Formatiert einen String in ein Handle.        | ⛔  Nein    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Konvertiert einen String in einen MD5-Hash. Weitere Informationen finden Sie unter [Kodierungsfilter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).   | ✅  Ja   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Konvertiert einen String in einen SHA-1-Hash. Weitere Informationen finden Sie unter [Kodierungsfilter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).  | ✅  Ja   |
| hmac_sha1_hex<br>(vorher [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Konvertiert einen String in einen SHA-1-Hash unter Verwendung eines Hash Message Authentication Code (HMAC). Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter. Weitere Informationen finden Sie unter [Kodierungsfilter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters). | ✅  Ja   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Konvertiert einen String per Hash Message Authentication Code (HMAC) in einen SHA-256-Hash. Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter.       | ✅  Ja   |
| hmac_sha512 | Konvertiert einen String per Hash Message Authentication Code (HMAC) in einen SHA-512-Hash. Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter. | ✅  Ja  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Fügt ein `<br>`-Zeilenumbruch-HTML-Tag vor jedem Zeilenumbruch in einem String ein.        | ✅  Ja   |
| [pluralize](https://shopify.dev/api/liquid/filters/pluralize)   | Gibt die Singular- oder Pluralversion eines englischen Strings basierend auf dem Wert einer Zahl aus.      | ⛔  Nein    |
| [prepend](https://shopify.dev/api/liquid/filters/prepend)     | Stellt einem String Zeichen voran.      | ✅  Ja   |
| [remove](https://shopify.dev/api/liquid/filters/remove)      | Entfernt alle Vorkommen eines Teilstrings aus einem String.       | ✅  Ja   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Entfernt nur das erste Vorkommen eines Teilstrings aus einem String.      | ✅  Ja   |
| [replace](https://shopify.dev/api/liquid/filters/replace)        | Ersetzt alle Vorkommen eines Strings durch einen Teilstring.   | ✅  Ja   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Ersetzt das erste Vorkommen eines Strings durch einen Teilstring.      | ✅  Ja   |
| [slice](https://shopify.dev/api/liquid/filters/slice)       | Der Slice-Filter gibt einen Teilstring zurück, der am angegebenen Index beginnt.       | ✅  Ja   |
| [split](https://shopify.dev/api/liquid/filters/split)  | Der Split-Filter verwendet einen Teilstring als Parameter. Der Teilstring dient als Trennzeichen, um einen String in ein Array aufzuteilen.            | ✅  Ja   |
| [strip](https://shopify.dev/api/liquid/filters/strip)   | Entfernt Tabulatoren, Leerzeichen und Zeilenumbrüche (alle Whitespace-Zeichen) von der linken und rechten Seite eines Strings.                                                                                                    | ✅  Ja   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Entfernt Tabulatoren, Leerzeichen und Zeilenumbrüche (alle Whitespace-Zeichen) von der linken Seite eines Strings.    | ⛔  Nein    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Entfernt Tabulatoren, Leerzeichen und Zeilenumbrüche (alle Whitespace-Zeichen) von der rechten Seite eines Strings.          | ⛔  Nein    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Entfernt alle HTML-Tags aus einem String.        | ✅  Ja   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Entfernt alle Zeilenumbrüche aus einem String.        | ✅  Ja   |
| [truncate](https://shopify.dev/api/liquid/filters/truncate)    | Kürzt einen String auf die Anzahl der Zeichen, die als erster Parameter übergeben wurde. Ein Auslassungszeichen (...) wird an den gekürzten String angehängt und in die Zeichenzählung einbezogen.    | ✅  Ja   |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords)   | Kürzt einen String auf die Anzahl der Wörter, die als erster Parameter übergeben wurde. Ein Auslassungszeichen (...) wird an den gekürzten String angehängt.    | ✅  Ja   |
| [upcase](https://shopify.dev/api/liquid/filters/upcase)   | Konvertiert einen String in Großbuchstaben.      | ✅  Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Zusätzliche Filter

Die folgenden allgemeinen Filter dienen unterschiedlichen Zwecken wie der Formatierung oder Konvertierung von Inhalten.

| Filter                | Beschreibung                                                                                                                      | Unterstützt |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/date)           | Konvertiert einen Zeitstempel in ein anderes Datumsformat. Weitere Informationen finden Sie unter [Datumsfilter](#date-filter).         | ✅  Ja   |
| [default](https://shopify.dev/api/liquid/filters/default)        | Legt einen Standardwert für jede Variable fest, der kein Wert zugewiesen ist. Kann mit Strings, Arrays und Hashes verwendet werden.      | ✅  Ja   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formatiert eine Adresse, um die Adresselemente entsprechend dem jeweiligen Gebietsschema in der richtigen Reihenfolge auszugeben.        | ⛔  Nein    |
| [highlight](https://shopify.dev/api/liquid/filters/highlight)      | Umschließt Wörter in Suchergebnissen mit dem HTML-Tag `<strong>` und der Klasse highlight, wenn sie mit den eingegebenen Suchbegriffen übereinstimmen. | ⛔  Nein    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere unterstützte Filter, wie z. B. Kodierungs- und URL-Filter, finden Sie auf unserer Seite [Erweiterte Filter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Datumsfilter {#date-filter}

Der Filter `date` kann verwendet werden, um einen Zeitstempel in ein anderes Datumsformat zu konvertieren. Sie können Parameter an den Filter `date` übergeben, um den Zeitstempel neu zu formatieren. Beispiele für diese Parameter finden Sie unter [strfti.me](http://www.strfti.me/).

Nehmen wir beispielsweise an, dass der Wert von `date_attribute` der Zeitstempel `2021-06-03 17:13:41 UTC` ist.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

Zusätzlich zu den `strftime`-Formatierungsoptionen unterstützt Braze mit dem Datumsfilter `%s` auch die Umwandlung eines Zeitstempels in Unix-Zeit. Um beispielsweise das `date_attribute` in Unix-Zeit zu erhalten:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}