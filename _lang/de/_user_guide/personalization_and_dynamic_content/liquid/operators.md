---
nav_title: Operatoren
article_title: Liquid-Operatoren
page_order: 2
description: "Auf dieser Referenzseite finden Sie die von Liquid unterstützten Operatoren sowie entsprechende Beispiele."

---

# Operatoren

> Liquid unterstützt viele [Operatoren](https://docs.shopify.com/themes/liquid/basics/operators), die Sie in Ihren bedingten Anweisungen verwenden können. Auf dieser Seite finden Sie die von Liquid unterstützten Operatoren und Anwendungsbeispiele, wie Sie sie in Ihren Nachrichten verwenden können.

Diese Tabelle enthält die unterstützten Operatoren. Bitte beachten Sie, dass Klammern in Liquid ungültige Zeichen sind und die Funktion Ihrer Tags beeinträchtigen können.

|   Syntax| Beschreibung|
|---------|-----------|
| ==  | ist gleich        |
| !=  | ist nicht gleich|
|  >  | größer als  |
| <   | weniger als     |
| >=| größer als oder gleich|
| <= | kleiner als oder gleich |
| oder | Bedingung A oder Bedingung B|
| und | Bedingung A und Bedingung B|
| enthält | prüft, ob ein String oder ein String-Array einen String enthält|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Operatoren können in bedingten Anweisungen (`if`, `elsif`, `unless`) verwendet werden, jedoch nicht in`assign`  Anweisungen,`for`  Schleifen, `case`/`when` Anweisungen oder Array-Zugriffsklammern. Eine vollständige Aufschlüsselung finden Sie unter [Wo werden Operatoren und Filter verwendet]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters)?
{% endalert %}

### Gruppierungsbedingungen ohne Klammern

Liquid unterstützt keine Klammern zum Gruppieren von Ausdrücken. Um komplexe Boolesche Logik wie zu bewerten`(a and b) or c`, verwenden Sie bitte verschachtelte`if`Anweisungen oder Zwischenvariablen.

Um beispielsweise zu überprüfen, ob ein Wert eine zusammengesetzte Bedingung erfüllt, weisen Sie eine Zwischenvariable zu:

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## Tutorials

Gehen wir ein paar Tutorials durch, um zu lernen, wie Sie diese Operatoren für Ihre Kampagnen nutzen können:

### Bitte wählen Sie eine Nachricht mit einem angepassten Attribut vom Typ „Ganzzahl“ aus.

Lassen Sie sich Push-Benachrichtigungen mit personalisierten Aktionen an Nutzer:innen schicken, die eingekauft haben oder nicht. Die Push-Benachrichtigung verwendet ein ganzzahliges angepasstes Attribut namens `total_spend`, um die Gesamtausgaben eines Nutzers:innen zu überprüfen.

1. Schreiben Sie eine bedingte Anweisung mit dem Operator größer als (`>`), um zu prüfen, ob die Gesamtausgaben eines Nutzers:innen größer sind als `0`, was bedeutet, dass sie einen Kauf getätigt haben. Dann erstellen Sie eine Nachricht, die Sie an diese Nutzer:innen senden.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2\. Fügen Sie den Tag {% raw %}`{% else %}`{% endraw %} hinzu, um Nutzer:in zu erfassen, deren Gesamtausgaben gleich `0` sind oder nicht existieren. Dann erstellen Sie eine Nachricht, die Sie an diese Nutzer:innen senden.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3\. Schließen Sie die bedingte Logik mit dem Tag {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![Ein Composer für Push-Benachrichtigungen mit dem vollständigen Liquid Code aus dem Tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Wenn das angepasste Attribut „Gesamtausgaben“ eines Nutzers größer als ist`0`, erhält er die folgende Nachricht:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Wenn das angepasste Attribut "Gesamtausgaben" eines Nutzers nicht existiert oder gleich `0` ist, erhält er folgende Nachricht:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Bitte wählen Sie eine Nachricht mit einem angepassten Attribut aus.

Senden Sie Push-Benachrichtigungen an Nutzer:innen und personalisieren Sie die Nachricht auf der Grundlage des zuletzt gespielten Spiels des jeweiligen Nutzers. Hier wird ein angepasstes String Attribut namens `recent_game` verwendet, um zu überprüfen, welches Spiel ein Nutzer:in zuletzt gespielt hat.

1. Schreiben Sie eine bedingte Anweisung mit dem Operator equals (`==`), um zu prüfen, ob das letzte Spiel eines Nutzers: *in Awkward Dinner Party* ist. Dann erstellen Sie eine Nachricht, die Sie an diese Nutzer:innen senden.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2\. Verwenden Sie den Tag `elsif` mit dem Operator equals (`==`), um zu prüfen, ob das letzte Spiel des Nutzers:in *Proxy War 3 ist: Krieg des Durstes*. Dann erstellen Sie eine Nachricht, die Sie an diese Nutzer:innen senden.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3\. Verwenden Sie das`elsif`Tag mit den Operatoren „ist nicht gleich“ (`!=`) und „und“ (`and`), um zu überprüfen, ob die Nutzer:in ein aktuelles Spiel hat (d. h. der Wert ist nicht leer) und dass es sich bei dem Spiel nicht um *„Awkward Dinner Party“* oder *„Proxy War 3“ handelt: Krieg des Durstes*. Dann erstellen Sie eine Nachricht, die Sie an diese Nutzer:innen senden.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4\. Fügen Sie den Tag {% raw %}`{% else %}`{% endraw %} hinzu, um Nutzer:innen zu erfassen, die kein aktuelles Spiel haben. Dann erstellen Sie eine Nachricht, die Sie an diese Nutzer:innen senden.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5\. Schließen Sie die bedingte Logik mit dem Tag {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![Ein Composer für Push-Benachrichtigungen mit dem vollständigen Liquid Code aus dem Tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Wenn ein Nutzer:innen zuletzt *Awkward Dinner Party* gespielt hat, erhält er jetzt diese Nachricht:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Wenn das letzte Spiel eines Nutzers:innen *Proxy War 3 ist: War of Thirst*, erhalten sie diese Nachricht:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Wenn ein Nutzer:innen kürzlich ein Spiel gespielt hat, das nicht *Awkward Dinner Party* oder *Proxy War 3 war: War of Thirst*, werden sie diese Nachricht erhalten:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Wenn ein Nutzer:in noch kein Spiel gespielt hat oder das angepasste Attribut in seinem Profil nicht existiert, erhält er diese Nachricht:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Nachricht standortabhängig abbrechen

Sie können eine Nachricht aufgrund von so gut wie allem abbrechen. Brechen Sie eine Nachricht ab, wenn ein Nutzer:in nicht in einem bestimmten Gebiet ansässig ist, da er sich möglicherweise nicht für die Aktion, die Show oder die Zustellung qualifiziert.

1. Schreiben Sie eine bedingte Anweisung mit dem Operator equals (`==`), um zu prüfen, ob die Zeitzone des Nutzers:in `America/Los_Angeles` ist, und erstellen Sie dann eine Nachricht, die an diese Nutzer:innen gesendet wird. 

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2\. Um zu vermeiden, dass Nachrichten an Nutzer:in außerhalb der Zeitzone `America/Los_Angeles` gesendet werden, umschließen Sie die Tags {% raw %}`{% else %}`{% endraw %} und {% raw %}`{% endif %}`{% endraw %} mit einem Tag {% raw %}`{% abort_message () %}`{% endraw %}.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![Ein Composer für Push-Benachrichtigungen mit dem vollständigen Liquid Code aus dem Tutorial.]({% image_buster /assets/img/abort-if.png %})

Sie können Nachrichten auch auf Grundlage verbundener Inhalte [abbrechen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/).

## Fehlersuche

### Die Vorschau kann Eigenschaftstypen möglicherweise falsch erzwingen. 

Bei der Vorschau einer Nachricht im Dashboard werden die meisten Variablen (wie benutzerdefinierte Attribute) in den korrekten Typ umgewandelt. Einige Variablen verfügen jedoch nicht über einen definierten Typ, den die Vorschau nachschlagen kann:

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

Bei diesen Eigenschaften versucht die Vorschau, den Typ aus dem Wert abzuleiten. Dies bedeutet, dass ein Wert, den Sie als **String**-Wert beabsichtigen, möglicherweise fälschlicherweise als **Zahl** interpretiert wird. Wenn beispielsweise ein String-Wert eine Zeichenfolge ist, kann die Vorschau ihn `"3"`in eine Ganzzahl `3`umwandeln, was zu unerwartetem Verhalten bei Zeichenfolgenoperationen wie`contains`oder `split`führen kann.

Wenn Sie bei der Verwendung dieser Eigenschaftstypen unerwartete Ergebnisse der Vorschau sehen, beachten Sie bitte, dass die Typinferenz der Vorschau möglicherweise nicht mit dem übereinstimmt, was zum Zeitpunkt des Sendens geschieht. Zum Zeitpunkt des Versands werden die tatsächlichen Datentypen aus dem auslösenden Ereignis oder API-Aufruf beibehalten.

Um einen bestimmten Typ in der Vorschau zu erzwingen, können Sie den Wert explizit umwandeln:

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}