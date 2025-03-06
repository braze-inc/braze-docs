---
nav_title: Abrufen von Benutzerprofildaten
article_title: Abrufen von Benutzerprofildaten bei Aufrufen von Connected Content
page_order: 5
description: "In diesem Artikel erfahren Sie, wie Sie Benutzerprofile in Ihre Connected Content-Aufrufe einbinden können und wie Sie am besten mit Liquid Templates arbeiten."

---

# Abrufen von Nutzerprofildaten

> Wenn eine Connected-Content-Antwort Felder für das Nutzerprofil enthält (innerhalb eines Liquid-Personalisierungs-Tags), müssen diese Werte vor dem Aufruf von Connected-Content in der Nachricht über Liquid definiert werden, damit der Liquid-Passback korrekt wiedergegeben wird. 

Ebenso muss das `:rerender`-Flag in der Anfrage enthalten sein. Beachten Sie, dass das `:rerender`-Flag nur eine Ebene tiefer angeordnet, d. h. es gilt nicht für verschachtelte Connected-Content-Tags.

Für die Personalisierung zieht Braze die Felder des Benutzerprofils heran, bevor das Feld an Liquid weitergegeben wird. Wenn die Antwort von Connected Content also Felder des Benutzerprofils enthält, müssen diese vorher definiert werden. 

Hier ein Beispiel für einen Connected-Content-Aufruf:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
Und die Connected-Content-Antwort lautet {% raw %}`Your language is ${language}`{% endraw %}, der in diesem Szenario angezeigte Inhalt lautet `Hi Jon, your language is`. Die Sprache selbst wird nicht als Vorlage verwendet. Das liegt daran, dass Braze wissen muss, welche Felder vom Nutzer oder von der Nutzerin abgerufen werden sollen, bevor der den Connected-Content-Aufruf durchgeführt wird.

Um den Liquid-Passback richtig darzustellen, müssen Sie das Tag {% raw %}`${language}`{%endraw%} an beliebiger Stelle in die Anfrage einfügen, wie im folgenden Code-Snippet gezeigt. Der Liquid-Präprozessor weiß, dass er das „language“-Attribut vom Nutzer oder der Nutzerin abrufen muss, um es für die Erstellung der Antwort-Template bereitzuhalten.
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
Denken Sie daran, dass die Option `:rerender` nur eine Ebene tiefer angeordnet ist. Wenn die Connected-Content-Antwort selbst weitere Connected-Content-Tags enthält, gibt Braze diese zusätzlichen Tags nicht erneut wieder.
{% endalert %}
