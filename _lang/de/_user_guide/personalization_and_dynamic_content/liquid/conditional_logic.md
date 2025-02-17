---
nav_title: Logik für bedingtes Messaging
article_title: Logik für bedingtes Liquid-Messaging
page_order: 6
description: "In diesem Referenzartikel erfahren Sie, wie Tags in Ihren Kampagnen verwendet werden können und sollten."

---

# Logik für bedingtes Messaging

> [Mit den Tags][7] können Sie Programmierlogik in Ihre Messaging-Kampagnen integrieren. Tags können für die Ausführung von bedingten Anweisungen sowie für fortgeschrittene Anwendungsfälle, wie die Zuweisung von Variablen oder die Iteration durch einen Codeblock, verwendet werden. <br><br>Auf dieser Seite erfahren Sie, wie Tags verwendet werden können und sollten, z. B. wie Sie null, nil und leere Attributwerte berücksichtigen und wie Sie auf benutzerdefinierte Attribute verweisen.

## Formatieren von Tags

{% raw %}
Ein Tag muss in `{% %}` verpackt sein.
{% endraw %}

{% alert tip %}
Um Ihnen das Leben ein wenig zu erleichtern, hat Braze eine Farbformatierung eingebaut, die in grün und lila aktiviert wird, wenn Sie Ihre Liquid-Syntax korrekt formatiert haben. Die grüne Formatierung hilft bei der Identifizierung von Tags, während die violette Formatierung Bereiche hervorhebt, die eine Personalisierung enthalten.
<br><br>
Wenn Sie Schwierigkeiten mit der Verwendung von bedingtem Messaging haben, versuchen Sie, die bedingte Syntax aufzuschreiben, bevor Sie Ihre angepasste Attribute und andere Liquid-Elemente einfügen.
<br><br>
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
{% endalert %}

## Bedingte Logik

Sie können viele Arten von [intelligenter Logik in Nachrichten einfügen][1], wie z. B. eine bedingte Anweisung. Sehen Sie sich das folgende Beispiel an, in dem [Bedingungen][8] verwendet werden, um eine Kampagne zu internationalisieren:
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

### Schritt-für-Schritt-Beispiel

In diesem Beispiel verwenden wir Tags mit „if“-, „elsif“- und „else“-Anweisungen, um internationalisierte Inhalte bereitzustellen.

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
```
Wenn die Sprache des Benutzers Englisch ist, ist die erste Bedingung erfüllt und der Benutzer erhält eine Nachricht auf Englisch.

```liquid
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
```

Sie können so viele bedingte Anweisungen angeben, wie Sie möchten. Nachfolgende Bedingungen werden geprüft, wenn die vorherigen Bedingungen nicht erfüllt sind. Wenn in diesem Beispiel das Gerät eines Benutzers nicht auf Englisch eingestellt ist, prüft dieser Code, ob das Gerät des Benutzers auf Spanisch oder Chinesisch eingestellt ist. Wenn das Gerät des Benutzers eine dieser Bedingungen erfüllt, erhält der Benutzer eine Nachricht in der entsprechenden Sprache.

```liquid
{% else %}
This is a message from Braze! This is going to go to anyone who didn't match the other specified languages!
```

Sie haben die Möglichkeit, eine `{% else %}`-Anweisung in Ihre bedingte Logik aufzunehmen. Wenn keine der von Ihnen festgelegten Bedingungen erfüllt ist, gibt die Anweisung `{% else %}` die Nachricht an, die gesendet werden soll. In diesem Fall verwenden wir standardmäßig Englisch, wenn die Sprache eines Nutzers:innen nicht Englisch, Spanisch oder Chinesisch ist.

```liquid
{% endif %}
```

Das Tag `{% endif %}` signalisiert, dass Sie Ihre bedingte Logik abgeschlossen haben. Sie müssen das Tag `{% endif %}` in jede Nachricht mit bedingter Logik einfügen. Wenn Sie in Ihrer bedingten Logik kein `{% endif %}`-Tag einfügen, erhalten Sie eine Fehlermeldung, da Braze Ihre Nachricht nicht analysieren kann.

{% endraw %}

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

![Eine Beispielnachricht im Braze-Dashboard, die das Attribut „Vorname“ mit Null belegt.][36]{: style="max-width:60%;"}

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

Nachdem Sie [angepasste Attribute][2] erstellt haben, können Sie diese angepassten Attribute in Ihrem Liquid-Messaging referenzieren.

Wenn Sie eine bedingte Logik verwenden, müssen Sie den Datentyp des angepassten Attributs kennen, um sicherzustellen, dass Sie die richtige Syntax verwenden. Suchen Sie auf der Seite **Benutzerdefinierte Attribute** im Dashboard nach dem Datentyp, der mit Ihrem benutzerdefinierten Attribut verknüpft ist, und verweisen Sie dann auf die folgenden Beispiele, die für jeden Datentyp aufgeführt sind.

![Auswählen eines Datentyps für ein benutzerdefiniertes Attribut. Das angegebene Beispiel zeigt ein Favorite_Category-Attribut mit dem Datentyp String.][20]{: style="max-width:80%;"}

{% alert tip %}
Bei Strings und Arrays sind gerade Apostrophe erforderlich, während Boolesche und ganze Zahlen niemals Apostrophe haben.
{% endalert %}

#### Boolesch

[Die Booleschen Werte][9] sind Binärwerte und können entweder auf `true` oder `false` festgelegt werden, z. B. `registration_complete: true`. Boolesche Werte haben keine Apostrophe um sie herum.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Zahl

[Zahlen][10] sind numerische Werte, bei denen es sich um ganze Zahlen oder Gleitkommazahlen handeln kann. Ein:e Nutzer:in kann zum Beispiel `shoe_size: 10` oder `levels_completed: 287` haben. Zahlenwerte haben keine Apostrophe um sie herum.

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

Ein [String][11] besteht aus alphanumerischen Zeichen und speichert Daten über Ihre Nutzer:innen. Sie können zum Beispiel `favorite_color: red` oder `phone_number: 3025981329` haben. String-Werte müssen mit Apostrophen versehen werden.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Für Strings können Sie sowohl „==“ als auch „contains“ in Ihrem Liquid verwenden.

#### Array

Ein [Array][12] ist eine Liste mit Informationen über Ihren Benutzer. Ein Benutzer kann zum Beispiel `last_viewed_shows: stranger things, planet earth, westworld` haben. Array-Werte müssen mit Hochkommata versehen werden.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Für Arrays müssen Sie „contains“ verwenden und können nicht „==“ verwenden. 

#### Uhrzeit

Ein Zeitstempel, der angibt, wann ein Event stattgefunden hat. [Die Werte von][13] müssen mit einem [mathematischen Filter][5] versehen sein, damit sie in der bedingten Logik verwendet werden können.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


[36]:{% image_buster /assets/img/value_null.png %}
[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags"
[9]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans
[10]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings
[12]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time
[20]: {% image_buster /assets/img_archive/custom_attribute_data_type.png %}
