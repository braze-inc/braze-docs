---
nav_title: Abrufen von Benutzerprofildaten
article_title: Abrufen von Benutzerprofildaten bei Aufrufen von Connected Content
page_order: 3
description: "In diesem Artikel erfahren Sie, wie Sie Benutzerprofile in Ihre Connected Content-Aufrufe einbinden können und wie Sie am besten mit Liquid Templates arbeiten."
toc_headers: h2
---

# Abrufen von Nutzerprofildaten

>  

## 

Wenn eine Connected-Content-Antwort Felder mit Nutzerprofilen (innerhalb eines Liquid-Tags zur Personalisierung) enthält, müssen diese Werte vor dem Aufruf von Connected-Content in der Nachricht mit Liquid definiert werden, damit das Liquid-Passback korrekt dargestellt wird. Ebenso muss das `:rerender`-Flag in der Anfrage enthalten sein. Beachten Sie, dass das `:rerender`-Flag nur eine Ebene tiefer angeordnet, d. h. es gilt nicht für verschachtelte Connected-Content-Tags.

## 

Für die Personalisierung zieht Braze die Felder des Benutzerprofils heran, bevor das Feld an Liquid weitergegeben wird. Wenn die Antwort von Connected Content also Felder des Benutzerprofils enthält, müssen diese vorher definiert werden. 

Hier ein Beispiel für einen Connected-Content-Aufruf:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

  

 Das liegt daran, dass Braze wissen muss, welche Felder vom Nutzer oder von der Nutzerin abgerufen werden sollen, bevor der den Connected-Content-Aufruf durchgeführt wird.

 Der Liquid-Präprozessor weiß, dass er das „language“-Attribut vom Nutzer oder der Nutzerin abrufen muss, um es für die Erstellung der Antwort-Template bereitzuhalten.


```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}


 Wenn die Connected-Content-Antwort selbst weitere Connected-Content-Tags oder Katalog-Tags enthält, wird Braze diese zusätzlichen Tags nicht erneut darstellen.


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