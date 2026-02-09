---
nav_title: Logik für bedingtes Messaging
article_title: Logik für bedingtes Liquid-Messaging
page_order: 6
description: "In diesem Referenzartikel erfahren Sie, wie Tags in Ihren Kampagnen verwendet werden können und sollten."

---

# Logik für bedingtes Messaging

> [Tags](https://docs.shopify.com/themes/liquid-documentation/tags) erlauben es Ihnen, Programmierlogik in Ihre Messaging-Kampagnen einzubauen. Tags können für die Ausführung von bedingten Anweisungen sowie für fortgeschrittene Anwendungsfälle, wie die Zuweisung von Variablen oder die Iteration durch einen Codeblock, verwendet werden. <br><br>Auf dieser Seite erfahren Sie, wie Tags verwendet werden können und sollten, z. B. wie Sie null, nil und leere Attributwerte berücksichtigen und wie Sie auf benutzerdefinierte Attribute verweisen.

## Formatieren von Tags

{% raw %}
Ein Tag muss in `{% %}` verpackt sein.
{% endraw %}

Um Ihnen das Leben ein wenig zu erleichtern, hat Braze eine Farbformatierung eingebaut, die in grün und lila aktiviert wird, wenn Sie Ihre Liquid-Syntax korrekt formatiert haben. Die grüne Formatierung hilft bei der Identifizierung von Tags, während die violette Formatierung Bereiche hervorhebt, die eine Personalisierung enthalten.

Wenn Sie Schwierigkeiten mit der Verwendung von bedingtem Messaging haben, versuchen Sie, die bedingte Syntax aufzuschreiben, bevor Sie Ihre angepasste Attribute und andere Liquid-Elemente einfügen.

Fügen Sie zum Beispiel zuerst den folgenden Text in das Nachrichtenfeld ein:  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Vergewissern Sie sich, dass es grün hervorgehoben ist, und ersetzen Sie dann die `X` mit dem von Ihnen gewählten Liquid oder Connected Content, indem Sie die blaue `+` in der Ecke des Nachrichtenfeldes verwenden, und die `0` mit dem von Ihnen gewünschten Wert.
<br><br>
Fügen Sie dann Ihre Nachrichtenvariationen nach Bedarf zwischen den `else` Bedingungen ein:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## Bedingte Logik

Sie können viele Arten von [intelligenter Logik in Nachrichten](http://docs.shopify.com/themes/liquid-documentation/basics) einfügen, z.B. eine bedingte Anweisung. Das folgende Beispiel verwendet [Konditionalitäten](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags), um eine Kampagne zu internationalisieren:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### Bedingte Tags

#### `if` und `elsif`

Die bedingte Logik beginnt mit dem Tag `if`, der die erste zu prüfende Bedingung angibt. Nachfolgende Bedingungen verwenden den Tag `elsif` und werden überprüft, wenn die vorherigen Bedingungen nicht erfüllt sind. Wenn in diesem Beispiel das Gerät eines Nutzers:innen nicht auf Englisch eingestellt ist, prüft dieser Code, ob das Gerät des Nutzers:innen auf Spanisch eingestellt ist, und wenn das nicht der Fall ist, prüft er, ob das Gerät auf. Wenn das Gerät des Benutzers eine dieser Bedingungen erfüllt, erhält der Benutzer eine Nachricht in der entsprechenden Sprache.

#### `else`

Sie haben die Möglichkeit, eine `{% else %}`-Anweisung in Ihre bedingte Logik aufzunehmen. Wenn keine der von Ihnen festgelegten Bedingungen erfüllt ist, gibt die Anweisung `{% else %}` die Nachricht an, die gesendet werden soll. In diesem Beispiel verwenden wir standardmäßig Englisch, wenn die Sprache eines Nutzers:innen nicht Englisch, Spanisch oder Chinesisch ist.

#### `endif`

Das Tag `{% endif %}` signalisiert, dass Sie Ihre bedingte Logik abgeschlossen haben. Sie müssen das Tag `{% endif %}` in jede Nachricht mit bedingter Logik einfügen. Wenn Sie in Ihrer bedingten Logik kein `{% endif %}`-Tag einfügen, erhalten Sie eine Fehlermeldung, da Braze Ihre Nachricht nicht analysieren kann.

### Anleitung: Standortbezogene Inhalte zustellen

Wenn Sie mit diesem Tutorial fertig sind, werden Sie in der Lage sein, Tags mit "if"-, "elsif"- und "else"-Anweisungen zu verwenden, um Inhalte abhängig vom Standort eines Nutzers zuzustellen.

1. Beginnen Sie mit einem `if` Tag, um festzulegen, welche Nachricht gesendet werden soll, wenn sich der Ort des Nutzers:in New York befindet. Wenn der Ort des Nutzers:innen New York ist, ist diese erste Bedingung erfüllt und der Nutzer:innen erhält eine Nachricht, die seine New Yorker Identität angibt.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at your local Sandwich Emperor. 
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2\. Als nächstes verwenden Sie den Tag `elseif`, um festzulegen, welche Nachricht gesendet werden soll, wenn die Stadt des Nutzers:innen in Los Angeles liegt.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3\. Lassen Sie uns einen weiteren `elseif` Tag verwenden, um festzulegen, welche Nachricht gesendet werden soll, wenn der Ort des Nutzers:innen in Chicago liegt.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
```

{: start="4"}
4\. Lassen Sie uns nun den Tag `{% else %}` verwenden, um festzulegen, welche Nachricht gesendet werden soll, wenn die Stadt des Nutzers:innen nicht in San Francisco, New York oder Chicago liegt.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5\. Schließlich verwenden wir den Tag `{% endif %}`, um anzugeben, dass unsere bedingte Logik abgeschlossen ist.

```liquid
{% endif %}
```

{% endraw %}

{% details Full Liquid code %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at our New York location. 
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## Berücksichtigung von null, nil und leeren Attributwerten

Die bedingte Logik ist eine nützliche Methode, um Attributwerte zu berücksichtigen, die nicht in Nutzerprofilen festgelegt sind.

### Attributwerte Null und NULL

Ein Nullwert tritt auf, wenn der Wert eines angepassten Attributs nicht festgelegt wurde. Ein Nutzer:innen, der seinen Vornamen noch nicht festgelegt hat, wird in Braze nicht mit einem Vornamen angemeldet.

Unter Umständen möchten Sie Benutzern, die einen Vornamen angegeben haben, eine völlig andere Nachricht schicken als Benutzern, die keinen Vornamen angegeben haben.

Mit dem folgenden Tag können Sie eine Nachricht für Nutzer:innen mit einem Attribut "Vorname" von Null angeben:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

![Eine Beispielnachricht im Braze-Dashboard, die das Attribut „Vorname“ mit Null belegt.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Beachten Sie, dass ein Null-Attributwert nicht streng mit einem Wertetyp verbunden ist (ein "Null"-String ist beispielsweise dasselbe wie ein "Null"-Array). Im obigen Beispiel bezieht sich der Null-Attributwert also auf einen nicht gesetzten Vornamen, der ein String wäre.

{% endraw %}

### Leere Attributwerte

Ein leerer Wert tritt auf, wenn das Attribut in einem Nutzerprofil nicht festgelegt ist, mit einem Leerzeichen-String (` `) festgelegt ist oder als `false` festgelegt ist. Leere Werte sollten vor anderen Variablen geprüft werden, um einen Liquid-Verarbeitungsfehler zu vermeiden.

Mit dem folgenden Tag können Sie eine Nachricht für Nutzer:innen angeben, die ein leeres Attribut "Vorname" haben.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## Verweis auf angepasste Attribute

Nachdem Sie [angepasste Attribute erstellt]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) haben, können Sie diese angepassten Attribute in Ihrem Liquid Messaging referenzieren.

Wenn Sie eine bedingte Logik verwenden, müssen Sie den Datentyp des angepassten Attributs kennen, um sicherzustellen, dass Sie die richtige Syntax verwenden. Suchen Sie auf der Seite **Benutzerdefinierte Attribute** im Dashboard nach dem Datentyp, der mit Ihrem benutzerdefinierten Attribut verknüpft ist, und verweisen Sie dann auf die folgenden Beispiele, die für jeden Datentyp aufgeführt sind.

![Auswählen eines Datentyps für ein benutzerdefiniertes Attribut. Das Beispiel zeigt ein Attribut von Favorite_Category mit dem Datentyp String.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
Bei Strings und Arrays sind gerade Apostrophe erforderlich, während Boolesche und ganze Zahlen niemals Apostrophe haben.
{% endalert %}

#### Boolesch

[Boolesche]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans) Werte sind binäre Werte und können entweder auf `true` oder `false` gesetzt werden, wie z.B. `registration_complete: true`. Boolesche Werte haben keine Apostrophe um sie herum.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Zahl

[Zahlen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers) sind numerische Werte, die ganze Zahlen oder Gleitkommazahlen sein können. Ein:e Nutzer:in kann zum Beispiel `shoe_size: 10` oder `levels_completed: 287` haben. Zahlenwerte haben keine Apostrophe um sie herum.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Sie können auch andere [grundlegende Operatoren](https://shopify.dev/docs/themes/liquid/reference/basics/operators) wie kleiner als (<) oder größer als (>) für ganze Zahlen verwenden:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### String

Ein [String]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings) besteht aus alphanumerischen Zeichen und speichert Daten über Ihre Nutzer:innen. Sie können zum Beispiel `favorite_color: red` oder `phone_number: 3025981329` haben. String-Werte müssen mit Apostrophen versehen werden.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Für Strings können Sie sowohl „==“ als auch „contains“ in Ihrem Liquid verwenden.

#### Array

Ein [Array]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays) ist eine Liste mit Informationen über Ihre Nutzer:innen. Ein Benutzer kann zum Beispiel `last_viewed_shows: stranger things, planet earth, westworld` haben. Array-Werte müssen mit Hochkommata versehen werden.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Für Arrays müssen Sie „contains“ verwenden und können nicht „==“ verwenden. 

#### Uhrzeit

Ein Zeitstempel, wann ein Ereignis stattgefunden hat. [Zeitwerte]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) müssen mit einem [mathematischen Filter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters) versehen sein, damit sie in der bedingten Logik verwendet werden können.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


