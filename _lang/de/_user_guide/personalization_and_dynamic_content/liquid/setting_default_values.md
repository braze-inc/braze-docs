---
nav_title: Standardwerte einstellen
article_title: Standardwerte für Flüssigkeiten einstellen
page_order: 5
description: "In diesem Artikel erfahren Sie, wie Sie Standardwerte für alle Personalisierungsattribute festlegen, die Sie in Ihren Nachrichten verwenden."

---

# Standardwerte einstellen

{% raw %}

> Sie können für jedes Personalisierungsattribut, das Sie in Ihren Nachrichten verwenden, Standardwerte festlegen. In diesem Artikel erfahren Sie, wie Standardwerte funktionieren, wie Sie sie einrichten und wie Sie sie in Ihren Nachrichten verwenden können.

## Funktionsweise

Standardwerte können hinzugefügt werden, indem Sie einen [Liquid Filter](http://docs.shopify.com/themes/liquid-documentation/filters) mit dem Namen "default" angeben (mit `|` können Sie den Filter wie in der Abbildung inline abgrenzen). 

```
| default: 'Insert Your Desired Default Here'
```

Wenn kein Standardwert angegeben wird und das Feld fehlt oder nicht auf den Benutzer eingestellt ist, bleibt das Feld in der Nachricht leer.

Das folgende Beispiel zeigt die korrekte Syntax für das Hinzufügen eines Standardwerts. In diesem Fall wird das Attribut `{{ ${first_name} }}` durch "Valued User" ersetzt, sofern das Feld `first_name` des jeweiligen Benutzers leer oder nicht verfügbar ist.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Für einen Benutzer namens Janet Doe würde die Nachricht wie folgt aussehen:

```
Hi Janet, thanks for using the App!
```

Oder...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
Der Standardwert wird für unausgefüllte Werte angezeigt, aber nicht für leere Werte. Ein unausgefüllter Wert enthält nichts, während ein leerer Wert weiße Zeichen (wie Leerzeichen) aber keine anderen Zeichen enthält. Eine leere Zeichenkette könnte zum Beispiel wie `""` aussehen und eine leere Zeichenkette wie `" "`.
{% endalert %}

## Standardwerte für verschiedene Datentypen festlegen

Das obige Beispiel zeigt, wie Sie eine Standardeinstellung für eine Zeichenkette festlegen. Sie können Standardwerte für jeden Liquid-Datentyp festlegen, der den Wert `empty`, `nil` (undefiniert) oder `false` hat. Dazu gehören Strings, Boolesche Werte, Arrays, Objekte und Zahlen.

### Anwendungsfall: Boolesche Werte

Nehmen wir an, Sie haben ein boolesches benutzerdefiniertes Attribut namens `premium_user` und möchten eine personalisierte Nachricht basierend auf dem Premium-Status des Benutzers senden. Einige Benutzer haben keinen Premium-Status eingerichtet, so dass Sie einen Standardwert einrichten müssen, um diese Benutzer zu erfassen.

1. Sie weisen dem Attribut `premium_user` die Variable `is_premium_user` zu, deren Standardwert `false` lautet. Wenn `premium_user` `nil` ist, wird der Wert von `is_premium_user` somit standardmäßig auf `false` gesetzt. 

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2\. Verwenden Sie nun eine bedingte Logik, um festzulegen, welche Nachricht gesendet werden soll, wenn `is_premium_user` `true` ist. Mit anderen Worten, was Sie senden sollen, wenn `premium_user` `true` ist. Weisen Sie dem Vornamen des Benutzers außerdem einen Standardwert zu, sofern uns der Benutzername nicht vorliegt.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3\. Schließlich geben Sie an, welche Nachricht gesendet werden soll, wenn `is_premium_user` `false` ist (und somit `premium_user` `false` oder `nil` ist). Dann schließen Sie die bedingte Logik.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### Anwendungsfall: Zahlen

Nehmen wir an, Sie haben ein numerisches benutzerdefiniertes Attribut namens `reward_points` und Sie möchten eine Nachricht mit den Belohnungspunkten des Benutzers senden. Einige Benutzer haben keine Rewards-Punkte eingerichtet, sodass Sie für diese einen Standardwert einrichten müssen.

1. Beginnen Sie die Nachricht mit dem Vornamen des Benutzers oder mit dem Standardwert `Valued User`, falls Sie den Namen des Benutzers nicht kennen.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. Beenden Sie die Nachricht mit der Anzahl an Treuepunkten des Benutzers und verwenden Sie dazu das benutzerdefinierte Attribut `reward_points` und den Standardwert `0`. Alle Benutzer, bei denen `reward_points` `nil` beträgt, erhalten in der Nachricht `0` Treuepunkte.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Anwendungsfall: Objekte

Angenommen, Sie haben das verschachtelte benutzerdefinierte Attributobjekt `location` mit den Eigenschaften `city` und `state`. Wenn eine dieser Eigenschaften nicht eingestellt ist, sollten Sie den Benutzer dazu auffordern, sie anzugeben.

1. Sprechen Sie den Benutzer mit seinem Vornamen an und geben Sie einen Standardwert an, falls Sie seinen Namen nicht kennen.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. Schreiben Sie eine Nachricht, die besagt, dass Sie den Standort des Benutzers überprüfen möchten.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3\. Fügen Sie den Benutzerstandort in die Nachricht ein und weisen Sie Standardwerte für den Fall zu, dass die Adresseigenschaft nicht eingestellt ist.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### Anwendungsfall: Arrays

Nehmen wir an, Sie haben ein benutzerdefiniertes Array-Attribut namens `upcoming_trips`, das Reisen mit den Eigenschaften `destination` und `departure_date` enthält. Sie möchten Benutzern personalisierte Nachrichten schicken, je nachdem, ob sie eine Reise geplant haben.

1. Schreiben Sie eine bedingte Logik, damit keine Nachricht gesendet wird, wenn `upcoming_trips` `empty` ist.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2\. Geben Sie an, welche Nachricht gesendet werden soll, wenn `upcoming_trips` einen Inhalt hat:<br><br>**2a.** Sprechen Sie den Benutzer an und geben Sie einen Standardwert an, falls Sie seinen Namen nicht kennen. <br>**2b.** Verwenden Sie ein `for`-Tag, um anzugeben, dass Sie Eigenschaften (oder Informationen) zu den in `upcoming_trips` enthaltenen Reisen abrufen. <br>**2c.** Listen Sie die Eigenschaften in der Nachricht auf und geben Sie einen Standardwert für den Fall an, dass `departure_date` nicht eingestellt ist. (Nehmen wir an, eine `destination` ist erforderlich, damit eine Reise erstellt werden kann, dann brauchen Sie dafür keinen Standardwert festzulegen).<br>**2\.** Schließen Sie das Tag `for` und dann die bedingte Logik.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
