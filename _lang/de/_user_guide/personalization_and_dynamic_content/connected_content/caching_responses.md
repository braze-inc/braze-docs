---
nav_title: Caching-Antworten
article_title: Cache-Connected-Content-Antworten
page_order: 2.5
description: "Dieser Artikel beschreibt, wie Sie Connected-Content-Antworten für verschiedene Kampagnen oder Nachrichten im selben Workspace zwischenspeichern können, um die Sendegeschwindigkeit zu optimieren."
---

# Cache-Connected-Content-Antworten

> Connected-Content-Antworten können für verschiedene Kampagnen oder Nachrichten (im selben Workspace) zwischengespeichert werden, um die Sendegeschwindigkeit zu optimieren.

Braze protokolliert oder speichert **die Antworttexte** von Connected-Content nicht dauerhaft. Während der Rendering-Prozesse für Nachrichten können Antworten vorübergehend gespeichert werden (beispielsweise im Speicher und im Cache), damit Braze Liquid rendern und die Nachricht versenden kann.

Um das Zwischenspeichern zu verhindern, können Sie `:no_cache` angeben, was zu erhöhtem Netzwerkverkehr führen kann. Zur Fehlerbehebung und Überwachung des Systemzustands protokolliert Braze die Metadaten von Connected-Content-Anfragen (wie die vollständig gerenderte Anfrage-URL und den Antwortstatuscode) für erfolgreiche und fehlgeschlagene Aufrufe. Diese Protokolle werden bis zu 30 Tage lang aufbewahrt.

{% details Connected Content rendering and data handling (advanced) %}
Dieser Abschnitt bietet einen detaillierteren Überblick darüber, wie Braze Liquid- und Connected-Content rendert und wo Daten vorübergehend gespeichert werden können, bevor eine Nachricht versendet wird. Dies könnte bei Datenschutz- und Datenverarbeitungsprüfungen hilfreich sein.

#### Was wird gespeichert und was nicht?

- **Antworttext für Connected-Content:** Wird von Braze nicht dauerhaft gespeichert. Es kann vorübergehend im Speicher gehalten und, wenn das Caching aktiviert ist, mit einer TTL im Cache gespeichert werden.
- **Anfrage für Metadaten für Connected-Content:** Anfrage-Metadaten wie die vollständig gerenderte URL, der HTTP-Statuscode und die Antwortdauer werden zur Fehlerbehebung und Überwachung protokolliert. Diese Protokolle werden bis zu 30 Tage lang aufbewahrt. 
- **Endgültige gerenderte Nachricht:** Existiert während des Renderings im Speicher. Je nach Ihrer Konfiguration und Ihrem Kanal kann dies auch an anderer Stelle gespeichert werden (z. B. in der Nachrichtenarchivierung oder in Content-Cards).

#### Rendering-Ablauf (allgemein)

Der folgende Ablauf beschreibt, wie Braze Nachrichten für providerbasierte Kanäle wie E-Mail, SMS und Push rendert und versendet. SDK-bereitgestellte Kanäle wie Content-Cards verwenden dieselbe zugrunde liegende Liquid- und Connected-Content-Darstellung, unterscheiden sich jedoch hinsichtlich des Zeitpunkts der Inhaltsgenerierung und der Weise der Zustellung.

1. Ein Hintergrundprozess rendert das Liquid-Template für eine Nachricht, wenn die Nachricht zur Zustellung vorbereitet wird.
2. Connected-Content-Tags werden während der Liquid-Rendering-Phase ausgewertet.
3. Für jedes Connected-Content-Tag überprüft Braze einen mehrstufigen Cache. Wenn kein zwischengespeicherter Wert vorhanden ist (oder das Caching deaktiviert ist), ruft Braze Ihren Endpunkt auf und empfängt die Antwort.
4. Die Antwort wird in das Liquid-Template eingespeist und die Nachricht vollständig gerendert.
5. Bei anbieterbasierten Kanälen wird die gerenderte Nachricht zunächst an den Kanalanbieter und anschließend an den Nutzer:in gesendet. Bei SDK-zugestellten Kanälen wie Content-Cards wird der gerenderte Inhalt mit dem Braze SDK synchronisiert und kann beim ersten Aufruf oder bei der ersten Anzeige generiert werden, woraufhin er den Nutzern angezeigt wird.

#### Wo Connected-Content-Antworten vorübergehend gespeichert werden können

Braze verwendet einen mehrstufigen Cache für Connected-Content-Antworten mit TTLs zwischen fünf Minuten und vier Stunden, abhängig von Ihrer Nutzung und`:cache_max_age` anderen Caching-Regeln:

- **In-Process-Speicher-Cache:** Temporärer Cache innerhalb des Worker-Prozesses. Daten können nur für die Dauer des Auftrags gespeichert werden (bis zu ~11 Minuten, basierend auf der Zeitüberschreitung des Arbeiters).
- **Lokaler Maschinen-Cache:** Ein Cache pro Mitarbeiter, beispielsweise eine lokale Memcached-Instanz.
- **Clusterweiter Cache:** Ein verteilter Cache, der von mehreren Arbeitern gemeinsam genutzt wird, beispielsweise ein Memcached-Cluster.

Diese Cache-Ebenen sind flüchtig und können Daten vor Ablauf des konfigurierten TTL entfernen.

#### Was ändert sich bei der Verwendung von `:no_cache`

Für Endpunkte, die nicht innerhalb der Braze-Infrastruktur gehostet werden, verhindert die`:no_cache` Verwendung von, dass der Antworttext von Connected-Content in Memcached gespeichert wird. In diesen Fällen verbleibt die Antwort nur für die Dauer des Rendering-Auftrags (bis zu ~11 Minuten) im Arbeitsspeicher des Worker-Prozesses. Bei Endpunkten, die zu internen Hosts von Braze aufgelöst werden, können Antworten weiterhin wie unter [„Cache-Busting“](#cache-busting) beschrieben zwischengespeichert werden.

#### Wo die endgültige gerenderte Ausgabe gespeichert werden kann

- **Nachrichtenarchivierung:** Wenn die Nachrichtenarchivierung aktiviert ist, kann Braze die endgültig gerenderte Nachricht in Ihren konfigurierten Cloud-Speicher-Bucket schreiben. Wenn Ihre Antwort auf den Connected-Content in der gerenderten Nachricht enthalten ist, wird sie in die archivierte Kopie aufgenommen.
- **Benutzergeräte:** Nach der Zustellung kann der vollständig gerenderte Inhalt der Nachrichten für einen unbekannten Zeitraum auf den Geräten der Nutzer:innen persistent bleiben.
- **Content-Cards:** Die gerenderten Inhalte für Content-Cards werden in einer Braze-Datenbank gespeichert, bis die Karte abläuft.
{% enddetails %}

## Standard-Cache-Einstellungen

Das Cache-Alter kann bis zu fünf Minuten (300 Sekunden) betragen. Sie können dies aktualisieren, indem Sie den Parameter `:cache_max_age` zum Aufruf von Connected-Content hinzufügen. Ein Beispiel ist:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

GET-Anfragen werden zwischengespeichert. Sie können dies konfigurieren, indem Sie den:no_cacheParameter zum Aufruf von „Connected-Content“ hinzufügen.

POST-Anfragen werden nicht zwischengespeichert. Dies kann durch Hinzufügen des:cache_max_ageParameters zum Aufruf von „Connected-Content“ erzwungen werden. Die minimale Cache-Zeit beträgt 5 Minuten und die maximale Cache-Zeit beträgt 4 Stunden.

{% alert note %}
Die Cache-Einstellungen sind nicht garantiert. Das Caching kann die Anzahl der Aufrufe Ihrer Endpunkte reduzieren. Wir empfehlen daher, mehrere Aufrufe pro Endpunkt innerhalb der Cache-Dauer zu verwenden, anstatt sich zu sehr auf das Caching zu verlassen.
{% endalert %}

### Begrenzung der Cache-Größe

Der Antwortkörper von Connected-Content kann bis zu 1 MB groß sein. Wenn der Antwortkörper größer als 1 MB ist, wird er nicht zwischengespeichert.

## Cache-Zeit 

Connected-Content speichert den Wert, den es von GET-Endpunkten zurückgibt, mindestens fünf Minuten lang. Wenn keine Cache-Zeit angegeben wird, beträgt die Standard-Cache-Zeit fünf Minuten.

Die Cache-Zeit für Connected-Content kann,:cache_max_age,wie im folgenden Beispiel gezeigt, auf einen längeren Zeitraum konfiguriert werden. Die minimale Cache-Zeit beträgt fünf Minuten und die maximale Cache-Zeit beträgt vier Stunden. Connected-Content-Daten werden mit einem flüchtigen Cache-System, wie z. B. Memcached, im Speicher zwischengespeichert. 

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
