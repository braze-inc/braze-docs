---
nav_title: Antworten zwischenspeichern
article_title: Caching von Connected-Content-Antworten
page_order: 2.5
description: "Dieser Artikel beschreibt, wie Sie Connected-Content-Antworten für verschiedene Kampagnen oder Nachrichten im selben Workspace zwischenspeichern können, um die Sendegeschwindigkeit zu optimieren."
---

# Zwischenspeichern von Connected-Content-Antworten

> Connected-Content-Antworten können für verschiedene Kampagnen oder Nachrichten (im selben Workspace) zwischengespeichert werden, um die Sendegeschwindigkeit zu optimieren.

Braze protokolliert oder speichert Connected-Content-Antworten nicht permanent. Wenn Sie sich explizit dafür entscheiden, die Antwort auf einen Connected-Content-Aufruf als Liquid-Variable zu speichern, speichert Braze diese nur im Arbeitsspeicher, d.h. in einem temporären Speicher, der nach kurzer Zeit gelöscht wird, um die Liquid-Variable zu rendern und die Nachricht zu senden.

Um das Zwischenspeichern zu verhindern, können Sie `:no_cache` angeben, was zu erhöhtem Netzwerkverkehr führen kann. Zur Fehlerbehebung und Überwachung des Systemzustands kann Braze auch fehlgeschlagene Connected-Content-Aufrufe (wie `404` und `429`) protokollieren. Diese Protokolle werden bis zu 30 Tage lang aufbewahrt.

## Standard-Cache-Einstellungen

Das Cache-Alter kann bis zu fünf Minuten (300 Sekunden) betragen. Sie können dies aktualisieren, indem Sie den Parameter `:cache_max_age` zum Aufruf von Connected-Content hinzufügen. Ein Beispiel ist:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

GET-Anfragen werden zwischengespeichert. Sie können dies konfigurieren, indem Sie den Parameter :no_cache zum Aufruf von Connected-Content hinzufügen.

POST-Anfragen werden nicht zwischengespeichert. Dies kann durch Hinzufügen des Parameters :cache_max_age zum Aufruf von Connected-Content erzwungen werden. Die minimale Cache-Zeit beträgt 5 Minuten und die maximale Cache-Zeit beträgt 4 Stunden.

{% alert note %}
Die Cache-Einstellungen sind nicht garantiert. Das Caching kann die Anzahl der Aufrufe Ihrer Endpunkte reduzieren. Wir empfehlen daher, mehrere Aufrufe pro Endpunkt innerhalb der Cache-Dauer zu verwenden, anstatt sich zu sehr auf das Caching zu verlassen.
{% endalert %}

### Begrenzung der Cache-Größe

Der Antwortkörper von Connected-Content kann bis zu 1 MB groß sein. Wenn der Antwortkörper größer als 1 MB ist, wird er nicht zwischengespeichert.

## Cache-Zeit 

Connected-Content speichert den Wert, den es von GET-Endpunkten zurückgibt, mindestens fünf Minuten lang. Wenn keine Cache-Zeit angegeben wird, beträgt die Standard-Cache-Zeit fünf Minuten.

Die Cache-Zeit von Connected-Content kann mit :cache_max_age, länger eingestellt werden, wie im folgenden Beispiel gezeigt. Die minimale Cache-Zeit beträgt fünf Minuten und die maximale Cache-Zeit beträgt vier Stunden. Connected-Content-Daten werden mit einem flüchtigen Cache-System, wie z. B. Memcached, im Speicher zwischengespeichert. 

Daher kann es vorkommen, dass Connected-Content-Daten unabhängig von der angegebenen Cache-Zeit früher als angegeben aus dem In-Memory-Cache von Braze entfernt werden. Das bedeutet, dass es sich bei den Cache-Dauern um Vorschläge handelt, die nicht unbedingt der Dauer entsprechen, die Braze für die Daten im Cache garantiert, und dass Sie möglicherweise mehr Connected Content-Anfragen sehen, als Sie bei einer bestimmten Cache-Dauer erwarten.

### Cache für bestimmte Sekunden

Dieses Beispiel wird für 900 Sekunden (oder 15 Minuten) zwischengespeichert.

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Cache-Busting

Um zu verhindern, dass Connected-Content den Wert, den es von einer GET-Anfrage zurückgibt, zwischenspeichert, können Sie die Konfiguration `:no_cache` verwenden. Antworten von Braze-internen Hosts werden jedoch weiterhin zwischengespeichert.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Vergewissern Sie sich, dass der bereitgestellte Connected-Content-Endpunkt große Datenmengen verarbeiten kann, bevor Sie diese Option verwenden. Andernfalls werden Sie wahrscheinlich eine erhöhte Versandlatenz (größere Verzögerungen oder längere Zeitabstände zwischen Anfrage und Antwort) feststellen, da Braze für jede einzelne Nachricht Connected-Content-Anfragen stellt.
{% endalert %}

Bei einer POST brauchen Sie keine Büste zu cachen, da Braze die Ergebnisse von POST-Anfragen nie cacht.

## Was Sie wissen sollten

- Caching kann dazu beitragen, doppelte Connected-Content-Aufrufe zu vermeiden. Es ist jedoch nicht garantiert, dass dies immer zu einem einzigen Connected-Content-Aufruf pro Nutzer:in führt.
- Die Zwischenspeicherung von Connected-Content basiert auf der URL und dem Workspace. Wenn der Aufruf von Connected-Content auf die identische URL erfolgt, kann er über Kampagnen und Canvase hinweg zwischengespeichert werden.
- Der Cache basiert auf einer eindeutigen URL, nicht auf einer Nutzer:in oder Kampagne. Das bedeutet, dass die zwischengespeicherte Version eines Connected-Content-Aufrufs von mehreren Nutzer:innen und Kampagnen in einem Workspace verwendet werden kann, wenn die URL dieselbe ist.
