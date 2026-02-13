---
nav_title: Antworten zwischenspeichern
article_title: Zwischenspeichern von Connected-Content-Antworten
page_order: 2.5
description: "Dieser Artikel beschreibt, wie Sie Connected-Content-Antworten für verschiedene Kampagnen oder Nachrichten im selben Workspace zwischenspeichern können, um die Sendegeschwindigkeit zu optimieren."
---

# Zwischenspeichern von Connected-Content-Antworten

> Connected-Content-Antworten können für verschiedene Kampagnen oder Nachrichten (im selben Workspace) zwischengespeichert werden, um die Sendegeschwindigkeit zu optimieren.

Braze protokolliert und speichert die **Connected-Content-Antwortkörper** nicht permanent. Während des Renderings von Nachrichten können Antworten vorübergehend gehalten werden (z.B. im Speicher und im Cache), damit Braze Liquid rendern und die Nachricht senden kann.

Um das Zwischenspeichern zu verhindern, können Sie `:no_cache` angeben, was zu erhöhtem Netzwerkverkehr führen kann. Um die Fehlerbehebung und die Überwachung des Systemzustands zu unterstützen, protokolliert Braze die Metadaten der Connected-Content-Anfrage (wie die vollständig gerenderte Anfrage-URL und den Response Status Code) für erfolgreiche und fehlgeschlagene Aufrufe. Diese Protokolle werden bis zu 30 Tage lang aufbewahrt.

{% details Connected Content rendering and data handling (advanced) %}
Dieser Abschnitt bietet eine detailliertere End-to-End-Ansicht, wie Braze Liquid und Connected-Content darstellt und wo Daten vorübergehend existieren können, bevor eine Nachricht gesendet wird. Dies kann bei der Überprüfung des Datenschutzes und des Umgangs mit Daten helfen.

#### Was gespeichert wird und was nicht

- **Connected-Content-Antwortkörper:** Von Braze nicht dauerhaft gespeichert. Sie können vorübergehend im Speicher gehalten und, wenn das Caching aktiviert ist, mit einer Time-to-Live (TTL) im Cache gespeichert werden.
- **Connected-Content-Anfrage-Metadaten:** Metadaten der Anfrage, wie die vollständig gerenderte URL, der HTTP Status Code und die Antwortdauer, werden zur Fehlerbehebung und Überwachung protokolliert. Diese Protokolle werden bis zu 30 Tage lang aufbewahrt. 
- **Endgültig gerenderte Nachricht:** Existiert während des Renderns im Speicher. Je nach Konfiguration und Kanal (z.B. Nachrichtenarchivierung oder Content-Cards) kann dies auch an anderer Stelle gespeichert sein.

#### Rendering Fluss (hohe Ebene)

Der folgende Ablauf beschreibt, wie Braze Nachrichten für anbieterbasierte Kanäle wie E-Mail, SMS und Push rendert und versendet. SDK-vermittelte Kanäle wie Content-Cards verwenden dasselbe zugrunde liegende Liquid- und Connected-Content-Rendering, unterscheiden sich aber darin, wann die Inhalte generiert und wie sie zugestellt werden.

1. Ein Hintergrundworker rendert das Liquid Template für eine Nachricht, wenn die Nachricht für die Zustellung vorbereitet wird.
2. Connected-Content Tags werden während des Liquid-Renderings ausgewertet.
3. Für jedes Connected-Content Tag überprüft Braze einen mehrstufigen Cache. Wenn kein Wert im Cache vorhanden ist (oder das Caching deaktiviert ist), ruft Braze Ihren Endpunkt auf und empfängt die Antwort.
4. Die Antwort wird in das Liquid Template eingespeist und die Nachricht wird vollständig gerendert.
5. Bei anbieterbasierten Kanälen wird die gerenderte Nachricht an den Kanalanbieter und dann an den Nutzer:innen gesendet. Bei Kanälen, die per SDK zugestellt werden, wie z.B. Content-Cards, wird der gerenderte Inhalt mit dem Braze SDK synchronisiert und kann zum Zeitpunkt der ersten Impression oder der ersten Anzeige generiert werden, bei der er dem Nutzer:innen gezeigt wird.

#### Wo Connected-Content-Antworten vorübergehend leben können

Braze verwendet einen mehrstufigen Cache für Connected-Content-Antworten mit TTLs zwischen fünf Minuten und vier Stunden, je nachdem, wie Sie `:cache_max_age` und andere Caching-Regeln verwenden:

- **In-Prozess-Speicher-Cache:** Transienter Cache innerhalb des Worker-Prozesses. Die Daten können nur für die Dauer des Auftrags gespeichert werden (bis zu ~11 Minuten, je nach Timeout des Workers).
- **Lokaler Rechner-Cache:** Ein Cache pro Worker, wie z.B. eine lokale Memcached Instanz.
- **Clusterweiter Cache:** Ein verteilter Cache, der von mehreren Arbeitern gemeinsam genutzt wird, wie z.B. ein Memcached-Cluster.

Diese Cache-Schichten sind flüchtig und können Daten früher als die konfigurierte TTL auslagern.

#### Was ändert sich, wenn Sie die `:no_cache`

Bei Endpunkten, die nicht in der Braze Infrastruktur gehostet werden, verhindert die Verwendung von `:no_cache`, dass der Connected-Content-Antwortkörper in Memcached gespeichert wird. In diesen Fällen bleibt die Antwort nur für die Dauer des Rendering-Auftrags (bis zu ~11 Minuten) im Speicher des Worker-Prozesses. Bei Endpunkten, die auf interne Hosts von Braze verweisen, können die Antworten immer noch zwischengespeichert werden, wie unter [Cache-Busting](#cache-busting) beschrieben.

#### Wo die endgültige gerenderte Ausgabe gespeichert werden kann

- **Nachrichten archivieren:** Wenn die Nachrichtenarchivierung aktiviert ist, kann Braze die endgültig gerenderte Nachricht in Ihren konfigurierten Cloud-Speicher Bucket schreiben. Wenn Ihre Connected-Content-Antwort in der gerenderten Nachricht enthalten ist, wird sie auch in der archivierten Kopie enthalten sein.
- **Nutzer:innen-Geräte:** Nach der Zustellung kann der vollständig gerenderte Inhalt der Nachricht für eine unbekannte Zeit auf den Nutzer:innen-Geräten persistent bleiben.
- **Content-Cards:** Gerenderte Inhalte für Content-Cards werden in einer Braze-Datenbank gespeichert, bis die Karte abläuft.
{% enddetails %}

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
