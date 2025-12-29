---
nav_title: Operatoren
article_title: Liquid-Operatoren
page_order: 2
description: "Auf dieser Referenzseite finden Sie die von Liquid unterstützten Operatoren sowie entsprechende Beispiele."

---

# Operatoren

> Liquid unterstützt viele [Operatoren](https://docs.shopify.com/themes/liquid/basics/operators), die Sie in Ihren bedingten Anweisungen verwenden können. Auf dieser Seite finden Sie die von Liquid unterstützten Operatoren und Anwendungsbeispiele, wie Sie sie in Ihren Nachrichten verwenden können.

Diese Tabelle enthält die unterstützten Operatoren. Beachten Sie, dass Klammern in Liquid ungültig sind und verhindern, dass Tags funktionieren.

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

## Tutorials

Gehen wir ein paar Tutorials durch, um zu lernen, wie Sie diese Operatoren für Ihre Kampagnen nutzen können:

### Nachricht mit einem ganzzahligen benutzerdefinierten Attribut auswählen

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

Ein Push-Benachrichtigung Composer mit dem vollständigen Liquid Code aus dem Tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

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

Wenn das angepasste Attribut "Gesamtausgaben" eines Nutzers:in größer ist als `0`, erhält er jetzt die Nachricht:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Wenn das angepasste Attribut "Gesamtausgaben" eines Nutzers nicht existiert oder gleich `0` ist, erhält er folgende Nachricht:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Nachricht mit einem benutzerdefinierten String-Attribut auswählen

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
3\. Verwenden Sie den Tag `elsif` mit den Operatoren "does not equal" (`!=`) und "and" (`&&`), um zu überprüfen, ob der Nutzer:in ein aktuelles Spiel hat (d.h. der Wert ist nicht leer) und ob es sich bei dem Spiel nicht um *Awkward Dinner Party* oder *Proxy War 3 handelt: Krieg des Durstes*. Dann erstellen Sie eine Nachricht, die Sie an diese Nutzer:innen senden.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
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
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

Ein Push-Benachrichtigung Composer mit dem vollständigen Liquid Code aus dem Tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

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

Ein Push-Benachrichtigung Composer mit dem vollständigen Liquid Code aus dem Tutorial.]({% image_buster /assets/img/abort-if.png %})

Sie können Nachrichten auch auf Grundlage verbundener Inhalte [abbrechen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/).


