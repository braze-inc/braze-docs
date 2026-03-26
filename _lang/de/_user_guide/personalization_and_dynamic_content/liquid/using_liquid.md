---
nav_title: Liquid verwenden
article_title: Liquid Anwendungsfälle und Übersicht
page_order: 0
description: "Dieser Referenzartikel bietet einen Überblick über häufige Anwendungsfälle von Liquid und darüber, wie Sie Liquid-Tags in Ihre Nachrichten integrieren können."
search_rank: 2
---

# [![Braze Lernangebote-Kurs: ]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Verwendung von Liquid

> Dieser Artikel zeigt, wie Sie verschiedene Attribute von Nutzer:innen verwenden können, um persönliche Informationen dynamisch in Ihr Messaging einzufügen.

Liquid ist eine quelloffene Template-Sprache, die von Shopify entwickelt und in Ruby geschrieben wurde. Sie können es in Braze verwenden, um Nutzerprofil-Daten in Ihre Nachrichten zu ziehen und diese Daten anzupassen. Sie können beispielsweise Liquid-Tags verwenden, um bedingte Nachrichten zu erstellen, wie z. B. das Versenden verschiedener Angebote basierend auf dem Jahrestag des Abos einer Nutzerin oder eines Nutzers . Darüber hinaus können Filter Daten bearbeiten, z. B. das Registrierungsdatum einer Nutzerin oder eines Nutzers  von einem Zeitstempel in ein besser lesbares Format umwandeln, wie z. B. "15\. Januar 2022". Weitere Einzelheiten zur Liquid-Syntax und ihren Möglichkeiten finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## Funktionsweise

Liquid Tags fungieren als Platzhalter in Ihren Nachrichten, die zustimmende Informationen aus dem Konto Ihres Benutzers abrufen können und die Personalisierung und relevante Nachrichtenpraktiken ermöglichen.

Im folgenden Block sehen Sie die doppelte Verwendung eines Liquid-Tags, um den Vornamen der Nutzerin oder des Nutzers aufzurufen, sowie eines Standard-Tags für den Fall, dass ein:e Nutzer:in ihren:seinen Vornamen nicht registriert hat.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Für einen Benutzer namens Janet Doe würde die Nachricht wie folgt aussehen:

```
Hi Janet, thanks for using the App!
```

Oder...

```
Hi Valued User, thanks for using the App!
```

{% alert important %}
HTML-Kommentare (`<!-- -->`) werden entfernt, bevor Liquid gelesen wird, sodass Liquid-Tags innerhalb von HTML-Kommentaren **nicht** in Ihrer Nachricht dargestellt **werden**. Für eine korrekte Darstellung stellen Sie bitte sicher, dass sich alle Liquid-Tags, die Sie verwenden möchten, außerhalb von HTML-Kommentaren befinden.
{% endalert %}

## Unterstützte Werte zum Ersetzen

Die folgenden Werte können in eine Nachricht eingefügt werden, je nach ihrer Verfügbarkeit:

- [Grundlegende Benutzerinformationen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) (zum Beispiel `first_name`, `last_name`, `email_address`)
- [Angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)
    - [Verschachtelte benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#liquid-templating)
- [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- [Zuletzt verwendete Geräteinformationen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information)
- [Targeting-Geräteinformationen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information)

Über Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) können Sie Inhalte auch direkt von einem Webserver abrufen.

{% alert important %}
Braze unterstützt derzeit Liquid bis einschließlich Liquid 5 von Shopify.
{% endalert %}

## Liquid verwenden

Mit [Liquid Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) können Sie die Qualität Ihrer Nachrichten erhöhen, indem Sie sie mit einer persönlichen Note versehen. 

### Liquid-Syntax

Liquid folgt einer bestimmten Struktur oder Syntax, die Sie bei der dynamischen Personalisierung im Auge behalten müssen. Hier sind ein paar Grundregeln, die Sie beachten sollten:

1. **Verwenden Sie gerade Anführungszeichen in Braze:** Es gibt einen Unterschied zwischen geschweiften Anführungszeichen ('**')** und geraden Anführungszeichen ('**')**. Verwenden Sie gerade Anführungszeichen (**' '**) in Ihrem Liquid in Braze. Beim Kopieren und Einfügen aus bestimmten Texteditoren werden möglicherweise geschweifte Anführungszeichen angezeigt, was zu Problemen in Ihrem Liquid führen kann. Wenn Sie Angebote direkt in das Braze Dashboard eingeben, ist alles in Ordnung!
2. **Die Klammern werden paarweise geliefert:** Jede Klammer muss sowohl geöffnet als auch geschlossen werden **{ }**. Achten Sie darauf, geschweifte Klammern zu verwenden!
3. **If-Aussagen gibt es paarweise:** Für jede `if` benötigen Sie eine `endif`, um anzuzeigen, dass die Anweisung `if` beendet ist.
4. **Variablennamen müssen ASCII-Zeichen verwenden:** Variablennamen für Liquids (erstellt mit`assign`  oder `capture`) unterstützen nur ASCII-Buchstaben, Ziffern und Unterstriche. Die Namen der Attribute der Personalisierung von Braze (innerhalb von`custom_attribute.${...}`  oder `event_properties.${...}`) können Nicht-ASCII-Zeichen enthalten.

#### Wo werden Operatoren und Filter verwendet?

Operatoren (wie `==`, `!=`, `>`, `and`, `or`) und Filter (wie `| size`, `| plus`) können jeweils nur in bestimmten Liquid-Kontexten verwendet werden.

| Kontext | Operatoren | Filter |
|-----------|-----------|---------|
| `assign` | Nicht unterstützt | Unterstützt |
| `if`, `elsif`, `unless` | Unterstützt | Nicht unterstützt |
| `case`, `when` | Nicht unterstützt | Nicht unterstützt |
| `for` | Nicht unterstützt | Nicht unterstützt |
| Array-Zugriff (`[ ]`) | Nicht unterstützt | Nicht unterstützt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wenn Sie einen gefilterten Wert in einem Kontext benötigen, der keine Filter unterstützt, weisen Sie das Ergebnis zunächst einer Variablen zu.

{% raw %}

##### Verwenden Sie ein Filterergebnis in einer Bedingung.

Es ist nicht möglich, einen Filter direkt in einer bedingten Anweisung zu verwenden. Dies ist unkorrekt:

```liquid
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}
```

Weisen Sie stattdessen das Ergebnis des Filters einer Variablen zu:

```liquid
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}
```

##### Verwenden Sie ein Ergebnis des Filters in einer for-Schleife

Es ist nicht möglich, einen Filter auf das Iterable in einer`for`Schleife anzuwenden. Dies ist unkorrekt:

```liquid
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}
```

Weisen Sie stattdessen den gefilterten Wert einer Variablen zu:

```liquid
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}
```

##### Verwenden Sie ein Ergebnis des Filters für den Array-Zugriff.

Es ist nicht möglich, einen Filter innerhalb von eckigen Klammern zu verwenden. Dies ist unkorrekt:

```liquid
{{ my_array[my_var | minus: 1] }}
```

Weisen Sie stattdessen zuerst den Wert, der durch den Filter gefiltert wurde, zu:

```liquid
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}
```

##### Speichern Sie ein Vergleichsergebnis in einer Variablen.

Es ist nicht möglich, einen Operator in einer`assign`Anweisung zu verwenden. Dies ist unkorrekt:

```liquid
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

Verwenden Sie stattdessen eine Bedingung, um die Variable festzulegen:

```liquid
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

{% endraw %}

#### Standardattribute und benutzerdefinierte Attribute

{% raw %}

Wenn Sie den folgenden Text in Ihre Nachricht einfügen: `{{${first_name}}}` einfügen, wird der Vorname der Nutzerin oder des Nutzers (aus dem Profil der Nutzerin oder des Nutzers) ersetzt, wenn die Nachricht gesendet wird. Sie können dasselbe Format auch für andere Standardbenutzerattribute verwenden.

Wenn Sie den Wert eines angepassten Attributs verwenden möchten, müssen Sie den Namespace"custom_attribute"zur Variablen hinzufügen. Wenn Sie zum Beispiel ein angepasstes Attribut mit dem Namen "Postleitzahl" verwenden möchten, würden Sie `{{custom_attribute.${zip code}}}` in Ihre Nachricht aufnehmen.

### Einfügen von Tags

Sie können Tags einfügen, indem Sie zwei geöffnete geschweifte Klammern `{{` in eine beliebige Nachricht eingeben. Dies triggert ein Feature zur automatischen Vervollständigung, das während der Eingabe weiter aktualisiert wird. Sie können sogar eine Variable aus den Optionen auswählen, die während der Eingabe erscheinen.

Wenn Sie einen benutzerdefinierten Tag verwenden, können Sie diesen kopieren und in die gewünschte Nachricht einfügen.

#### Ausnahmen für doppelte Klammern

Wenn Sie ein Tag innerhalb eines anderen Liquid-Tags verwenden, wie beispielsweise`{% assign %}`  oder `{% if %}`, können Sie entweder doppelte Klammern oder keine Klammern verwenden. Nur wenn der Tag allein steht, muss er in doppelte Klammern gesetzt werden. Zur Vereinfachung können Sie jederzeit doppelte Klammern verwenden. 

Die folgenden Tags sind alle korrekt:

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

Wenn Sie Liquid in Ihren E-Mail-Nachrichten verwenden, sollten Sie darauf achten:

1. Fügen Sie sie mit dem HTML-Editor und nicht mit dem klassischen Editor ein. Der klassische Editor kann das Liquid als Klartext parsen. Zum Beispiel würde das Liquid als {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} geparst werden, anstatt als Template den Vornamen der Nutzerin oder des Nutzers einzugeben.
2. Platzieren Sie den Liquid Code nur innerhalb des Tags `<body>`. Wenn Sie es außerhalb dieses Tags platzieren, kann es bei der Auslieferung zu einer inkonsistenten Darstellung kommen.

{% endalert %}

### Einfügen von vorformatierten Variablen

You can insert pre-formatted variables with defaults through the **Add Personalization** modal located near any templated text field.

![Das Modal "Personalisierung hinzufügen", das nach dem Auswählen von "Personalisierung einfügen" erscheint. Das Modal verfügt über Felder für den Typ der Personalisierung, das Attribut und den optionalen Standardwert und zeigt eine Vorschau der Liquid-Syntax an.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

The modal will insert Liquid with your specified default value at the point where your cursor was. Die Einfügemarke wird auch durch das Vorschau-Feld angegeben, das den Text vor und nach dem Einfügen enthält. Wenn ein Textblock hervorgehoben ist, wird der hervorgehobene Text ersetzt.

![Ein GIF des Modals Personalisierung hinzufügen, das zeigt, wie der Nutzer:innen "Mitreisender" als Standardwert einfügt und das Modal den hervorgehobenen Text "Name" im Composer durch das Liquid Snippet ersetzt.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

### Variablen zuweisen

{% raw %}
Einige Operationen in Liquid erfordern, dass Sie den Wert, den Sie bearbeiten möchten, als Variable speichern. Dies ist häufig der Fall, wenn Ihre Liquid-Anweisung mehrere Attribute, Event-Eigenschaften oder Filter enthält.

Nehmen wir zum Beispiel an, Sie möchten zwei angepasste Ganzzahlen zusammenfügen. 

#### Falsches Liquid Beispiel

Sie können nicht verwenden:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Dieses Liquid funktioniert nicht, weil Sie nicht mehrere Attribute in einer Zeile referenzieren können. Sie müssen mindestens einem dieser Werte eine Variable zuweisen, bevor die mathematischen Funktionen ausgeführt werden. Das Hinzufügen von zwei benutzerdefinierten Attributen würde zwei Zeilen Liquid erfordern: eine, um das benutzerdefinierte Attribut einer Variablen zuzuweisen, und eine, um die Addition durchzuführen.

#### Korrektes Liquid Beispiel

Sie können Folgendes verwenden:

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Anleitung: Verwendung von Variablen zur Berechnung einer Bilanz

Berechnen wir den aktuellen Saldo einer Nutzerin oder eines Nutzers , indem wir seinen Geschenkkartensaldo und seinen Rewards-Saldo addieren:

Verwenden Sie zunächst den Tag `assign`, um das angepasste Attribut von `current_rewards_balance` durch den Begriff "Saldo" zu ersetzen. Das bedeutet, dass Sie jetzt eine Variable namens `balance` haben, die Sie bearbeiten können.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Als Nächstes verwenden wir den Filter `plus`, um das Guthaben jedes Nutzers und jeder Nutzerin mit seinem Rewards-Saldo zu kombinieren, das durch `{{balance}}` gekennzeichnet ist.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
Haben Sie das Gefühl, dass Sie in jeder Nachricht die gleichen Variablen zuweisen? Anstatt den `assign` Tag immer wieder auszuschreiben, können Sie diesen Tag als Inhaltsblock speichern und ihn stattdessen am Anfang Ihrer Nachricht einfügen.

1. [Erstellen Sie einen Content-Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Geben Sie Ihrem Inhaltsblock einen Namen (keine Leerzeichen oder Sonderzeichen).
3. Wählen Sie unten auf der Seite **Bearbeiten**.
4. Geben Sie Ihre `assign` Tags ein.

Solange sich der Inhaltsblock am Anfang Ihrer Nachricht befindet, wird die Variable jedes Mal, wenn sie als Objekt in Ihre Nachricht eingefügt wird, auf das von Ihnen gewählte benutzerdefinierte Attribut verweisen!
{% endalert %}

