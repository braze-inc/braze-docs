---
nav_title: Abrufen von Nutzerprofildaten
article_title: Abrufen von Benutzerprofildaten bei Aufrufen von Connected Content
page_order: 3
description: "In diesem Artikel erfahren Sie, wie Sie Benutzerprofile in Ihre Connected Content-Aufrufe einbinden können und wie Sie am besten mit Liquid Templates arbeiten."
toc_headers: h2
---

# Abrufen von Nutzerprofildaten

> Auf dieser Seite erfahren Sie, wie Sie Nutzerprofile in Ihre Connected-Content-Aufrufe einbinden und wie Sie am besten mit Liquid-Templates arbeiten. 

## Voraussetzungen

Wenn eine Connected-Content-Antwort Felder mit Nutzerprofilen (innerhalb eines Liquid-Tags zur Personalisierung) enthält, müssen diese Werte vor dem Aufruf von Connected-Content in der Nachricht mit Liquid definiert werden, damit das Liquid-Passback korrekt dargestellt wird. Ebenso muss das `:rerender`-Flag in der Anfrage enthalten sein. Beachten Sie, dass das `:rerender`-Flag nur eine Ebene tiefer angeordnet, d. h. es gilt nicht für verschachtelte Connected-Content-Tags.

## Liquid-Templates in Connected-Content-Aufrufen

Für die Personalisierung zieht Braze die Felder des Benutzerprofils heran, bevor das Feld an Liquid weitergegeben wird. Wenn die Antwort von Connected Content also Felder des Benutzerprofils enthält, müssen diese vorher definiert werden. 

Hier ein Beispiel für einen Connected-Content-Aufruf:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

Die Connected-Content-Antwort lautet {% raw %}`Your language is ${language}`{% endraw %}. Der in diesem Beispiel angezeigte Inhalt ist `Hi Jon, your language is`. 

Die Sprache selbst wird nicht mit einem Template versehen. Das liegt daran, dass Braze wissen muss, welche Felder vom Nutzer oder von der Nutzerin abgerufen werden sollen, bevor der den Connected-Content-Aufruf durchgeführt wird.

Um das Liquid-Passback korrekt wiederzugeben, müssen Sie den Tag {% raw %}`${language}`{% endraw %} an einer beliebigen Stelle in der Anfrage einfügen, wie im folgenden Code-Snippet gezeigt. Der Liquid-Präprozessor weiß, dass er das „language“-Attribut vom Nutzer oder der Nutzerin abrufen muss, um es für die Erstellung der Antwort-Template bereitzuhalten.

{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Denken Sie daran, dass die Option `:rerender` nur eine Ebene tiefer angeordnet ist. Wenn die Connected-Content-Antwort selbst weitere Connected-Content-Tags oder Katalog-Tags enthält, wird Braze diese zusätzlichen Tags nicht erneut darstellen.
{% endalert %}

## Bewährte Praktiken

### Verwenden Sie `json_escape` mit Liquid-Tags, die das JSON-Format zerstören könnten.

Wenn Sie `:rerender` verwenden, fügen Sie den Filter `json_escape` zu jedem Liquid-Tag hinzu, der möglicherweise das JSON-Format verändern könnte. Wenn Ihre Liquid-Tags Zeichen enthalten, die das JSON-Format verletzen, wird die gesamte Connected-Content-Antwort als Text interpretiert und als Template in die Nachricht eingefügt, und keine der Variablen wird gespeichert.

Wenn zum Beispiel die Eigenschaft `message` im folgenden Beispiel Zeichen enthält, die das JSON-Format zerstören könnten, fügen Sie den Filter `json_escape` wie in diesem Beispiel hinzu:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}