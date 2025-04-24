---
nav_title: Connected-Content-Aufrufe tätigen
article_title: Aufruf einer Connected-Content-API
page_order: 0
description: "In diesem Referenzartikel erfahren Sie, wie Sie einen Connected-Content-API-Aufruf durchführen. Zudem erhalten Sie hier hilfreiche Beispiele und fortgeschrittene Anwendungsfälle für Connected Content."
search_rank: 2
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Aufruf einer Connected-Content API

> Verwenden Sie Connected-Content, um alle über APIs zugänglichen Informationen direkt in Nachrichten einzufügen, die Sie an Nutzer:innen senden. Sie können Inhalte entweder direkt von Ihrem Webserver oder von öffentlich zugänglichen APIs beziehen.<br><br>Auf dieser Seite erfahren Sie, wie Sie Connected-Content API-Aufrufe tätigen, fortgeschrittene Connected-Content-Anwendungsfälle, Fehlerbehandlung und mehr.

## Senden eines Connected-Content-Aufrufs

{% raw %}

Um einen Connected-Content-Aufruf zu senden, verwenden Sie das Tag `{% connected_content %}`. Mit diesem Tag können Sie Variablen zuweisen oder deklarieren, indem Sie `:save` verwenden. Auf Aspekte dieser Variablen kann später in der Nachricht mit [Liquid][2] Bezug genommen werden.

Der folgende Nachrichtentext greift beispielsweise auf die URL `http://numbersapi.com/random/trivia` zu und fügt einen witzigen Wissenswert in Ihre Nachricht ein:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is fun some trivia for you!: {{result.text}}
```

### Hinzufügen von Variablen

Sie können bei Connected-Content-Anfragen auch Attribute des Nutzerprofils als Variablen in den String der URL aufnehmen. 

Sie können zum Beispiel einen Webdienst haben, der Content auf der Grundlage der E-Mail Adresse und ID eines Nutzers oder einer Nutzerin zurückgibt. Wenn Sie Attribute übergeben, die Sonderzeichen enthalten, wie z. B. das at-Zeichen (@), stellen Sie sicher, dass Sie den Liquid-Filter `url_param_escape` verwenden, um alle Zeichen, die in URLs nicht zulässig sind, durch ihre URL-freundliche, maskierte Version zu ersetzen, wie im folgenden Attribut für E-Mail-Adressen gezeigt.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Attribut-Werte müssen von `${}` umgeben sein, um in unserer Version der Liquid-Syntax korrekt zu funktionieren.
{% endalert %}

Connected Content-Anfragen unterstützen nur GET- und POST-Anfragen.

## Fehlerbehandlung

Wenn die URL nicht verfügbar ist und eine 404-Seite erreicht, rendert Braze einen leeren String an ihrer Stelle. Wenn die URL eine HTTP 500- oder 502-Seite erreicht, schlägt die URL bei der Wiederholungslogik fehl.

Wenn der Endpunkt JSON zurückgibt, können Sie dies erkennen, indem Sie prüfen, ob der Wert `connected` null ist, und dann [die Nachricht bedingt abbrechen][1]. Braze lässt nur URLs zu, die über Port 80 (HTTP) und 443 (HTTPS) kommunizieren.

### Erkennung fehlerhafter Hosts

Connected Content verwendet einen Mechanismus zur Erkennung von ungesunden Hosts, um zu erkennen, wenn der Zielhost eine hohe Rate an signifikanter Verlangsamung oder Überlastung aufweist, die zu Timeouts, zu vielen Anfragen oder anderen Ergebnissen führt, die Braze daran hindern, erfolgreich mit dem Zielendpunkt zu kommunizieren. Diese Funktion dient als Schutzmaßnahme, um unnötige Belastungen zu reduzieren, die dem Zielhost Probleme bereiten könnten. Es dient auch der Stabilisierung der Braze-Infrastruktur und der Aufrechterhaltung schneller Nachrichtenübertragungsgeschwindigkeiten.

Wenn der Zielhost eine hohe Rate an erheblicher Langsamkeit oder Überlastung aufweist, hält Braze die Anfragen an den Zielhost vorübergehend für eine Minute an und simuliert stattdessen Antworten, die auf den Fehler hinweisen. Nach einer Minute prüft Braze den Zustand des Hosts mit einer kleinen Anzahl von Anfragen, bevor es die Anfragen mit voller Geschwindigkeit wieder aufnimmt, wenn der Host als gesund befunden wird. Wenn der Host immer noch ungesund ist, wartet Braze eine weitere Minute, bevor es erneut versucht wird.

Wenn Anfragen an den Zielhost durch den Detektor für fehlerhafte Hosts gestoppt werden, rendert Braze weiterhin Nachrichten und folgt Ihrer Liquid-Logik, als hätte es einen Fehlerantwortcode erhalten. Wenn Sie sicherstellen möchten, dass diese Connected-Content-Anfragen erneut versucht werden, wenn sie vom Detektor für fehlerhafte Hosts angehalten werden, verwenden Sie die Option `:retry`. Weitere Informationen über die Option `:retry` finden Sie unter [Wiederholungsversuche für angeschlossene Inhalte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Wenn Sie glauben, dass die Erkennung eines ungesunden Hosts Probleme verursacht, wenden Sie sich an den [Braze Support]({{site.baseurl}}/support_contact/).

{% alert tip %}
Besuchen Sie die Seite [Fehlerbehebung bei Webhook- und Connected Content-Anfragen]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection), um mehr darüber zu erfahren, wie Sie häufige Fehlercodes beheben können.
{% endalert %}

## Zulässig für effiziente Performance

Da Braze Nachrichten sehr schnell zustellt, sollten Sie sicherstellen, dass Ihr Server Tausende von gleichzeitigen Verbindungen verarbeiten kann, damit die Server beim Abrufen von Inhalten nicht überlastet werden. Wenn Sie öffentliche APIs verwenden, vergewissern Sie sich, dass Ihre Nutzung nicht gegen die Rate-Limits verstößt, die der API-Anbieter möglicherweise einsetzt. Braze verlangt aus Performance-Gründen, dass die Antwortzeit des Servers weniger als zwei Sekunden beträgt. Wenn der Server länger als zwei Sekunden braucht, um zu antworten, werden die Inhalte nicht eingefügt.

Braze-Systeme können denselben Connected-Content-API-Aufruf mehr als einmal pro Empfänger:in tätigen. Das liegt daran, dass Braze möglicherweise einen Connected-Content-API-Aufruf tätigen muss, um eine Nachricht zu rendern, und dass Nachrichten für die Validierung, Wiederholungslogik oder andere interne Zwecke mehrmals pro Empfänger:in gerendert werden können. Ihre Systeme sollten in der Lage sein, denselben Connected-Content-Aufruf mehr als einmal pro Empfänger:in zuzulassen.

## Was Sie wissen sollten

* Braze erhebt keine Gebühren für API-Aufrufe und wird nicht auf Ihr Datenpunkt-Kontingent angerechnet.
* Es gibt ein Limit von einem MB für Connected-Content-Antworten.
* Connected-Content-Aufrufe erfolgen, wenn die Nachricht gesendet wird, mit Ausnahme von In-App-Nachrichten, die diesen Aufruf tätigen, wenn die Nachricht angesehen wird.
* Connected Content-Aufrufe folgen keinen Umleitungen.

## Authentifizierungsarten

### Einfache Authentifizierung verwenden

Wenn die URL eine grundlegende Authentifizierung erfordert, kann Braze für Sie Zugangsdaten zur grundlegenden Authentifizierung generieren, die Sie in Ihrem API-Aufruf verwenden können. Unter **Einstellungen** > **Verbundene Inhalte** können Sie vorhandene Anmeldedaten für die Basisauthentifizierung verwalten und neue hinzufügen.

![Die Einstellungen für 'Verbundene Inhalte' im Braze Dashboard.][34]

Um eine neue Zugangsdaten hinzuzufügen, wählen Sie **Zugangsdaten hinzufügen**. Geben Sie Ihren Zugangsdaten einen Namen und geben Sie den Nutzernamen und das Passwort ein.

![Das Fenster „Neue Zugangsdaten erstellen“ mit der Option, einen Namen, einen Nutzernamen und ein Passwort einzugeben.][35]{: style="max-width:30%" }

Sie können diese grundlegenden Zugangsdaten dann in Ihren API-Aufrufen verwenden, indem Sie auf den Namen des Tokens verweisen:

{% raw %}
```
Hi there, here is fun some trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Wenn Sie eine Zugangsdaten löschen, denken Sie daran, dass alle Connected-Content-Aufrufe, die versuchen, sie zu verwenden, abgebrochen werden.
{% endalert %}

### Token-Authentifizierung verwenden

Bei der Verwendung von Braze Connected Content kann es vorkommen, dass Sie für bestimmte APIs ein Token anstelle eines Benutzernamens und eines Passworts benötigen. Der folgende Aufruf enthält einen Codeschnipsel, auf den Sie sich beziehen können und der als Vorlage für Ihre Nachrichten dient.

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://your_API_link_here/
     :method post
     :headers {
       "X-App-Id": "YOUR-APP-ID",
       "X-App-Token": "YOUR-APP-TOKEN"
     }
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Offene Authentifizierung (OAuth) verwenden

Einige API-Konfigurationen erfordern den Abruf eines Tokens, das zur Authentifizierung des API-Endpunkts verwendet werden kann, auf den Sie zugreifen möchten.

#### Schritt 1: Zugriffstoken abrufen

Das folgende Beispiel veranschaulicht das Abrufen und Speichern eines Zugriffstokens in einer lokalen Variable, die dann zur Authentifizierung des nachfolgenden API-Aufrufs verwendet werden kann. Ein `:cache_max_age`-Parameter kann hinzugefügt werden, um die Gültigkeitsdauer des Tokens zu bestimmen und die Anzahl der ausgehenden Connected-Content-Aufrufe zu reduzieren. Weitere Informationen finden Sie unter [Konfigurierbares Caching][36] ].

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "Bearer YOUR-APP-TOKEN"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Schritt 2: Autorisieren Sie die API mit dem abgerufenen Zugriffstoken

Nachdem das Token gespeichert wurde, kann es als dynamisches Template in den nachfolgenden Connected-Content-Aufruf eingefügt werden, um die Anfrage zu autorisieren:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

## Connected-Content-IP-Allowlisting

Wenn eine Nachricht mit Connected Content von Braze gesendet wird, stellen die Braze-Server automatisch Netzwerkanfragen an die Server unserer Kunden oder Dritter, um Daten zurückzuholen. Mit der IP-Zulassungsliste können Sie überprüfen, ob die Anfragen für Connected-Content tatsächlich von Braze stammen, was eine zusätzliche Sicherheitsebene darstellt.

Braze sendet Anfragen zu Connected Content von den folgenden IP-Bereichen. Die aufgelisteten Bereiche werden automatisch und dynamisch zu allen API-Schlüsseln hinzugefügt, für die ein Opt-in für das Zulassen von Listen vorgenommen wurde. 

Braze verfügt über einen reservierten Satz von IPs, die für alle Dienste verwendet werden, von denen nicht alle zu einem bestimmten Zeitpunkt aktiv sind. So kann Braze bei Bedarf von einem anderen Rechenzentrum aus senden oder Wartungsarbeiten durchführen, ohne die Kunden zu beeinträchtigen. Braze kann eine, eine Teilmenge oder alle der folgenden IPs verwenden, wenn Sie Connected-Content-Anfragen stellen.

{% multi_lang_include data_centers.md datacenters='ips' %}

## Fehlersuche

Verwenden Sie [Webhook.site](https://webhook.site/), um Fehlerbehebungen für Ihre Connected-Content-Aufrufe vorzunehmen. 

1. Tauschen Sie die URL in Ihrem Aufruf von Connected Content gegen die eindeutige URL aus, die auf der Website generiert wurde.
2. Testen Sie Ihre Kampagne oder Ihren Canvas-Schritt in der Vorschau, um zu sehen, wie die Anfragen auf dieser Website ankommen.

Mit diesem Tool können Sie Probleme mit den Anfrage-Headern, dem Anfragetext und anderen Informationen, die beim Aufruf gesendet werden, diagnostizieren.

## Häufig gestellte Fragen

### Warum gibt es mehr Connected-Content-Aufrufe als Nutzer:innen oder Sendungen? 

Es kann sein, dass Braze denselben Connected-Content-API-Aufruf mehr als einmal pro Empfänger:in tätigt, da wir möglicherweise einen Connected-Content-API-Aufruf tätigen müssen, um eine Nachricht zu rendern. Nachrichten können für Validierung, Wiederholungslogik oder andere interne Zwecke mehrmals pro Empfänger:in gerendert werden.

Es wird erwartet, dass ein Connected-Content API-Aufruf mehr als einmal pro Empfänger:in erfolgen kann, auch wenn die Wiederholungslogik nicht in dem Aufruf verwendet wird. Wir empfehlen, das Rate-Limits für Nachrichten mit Connected-Content einzustellen oder Ihre Server so zu konfigurieren, dass sie das erwartete Volumen besser bewältigen können.

### Wie funktioniert das Rate-Limiting bei Connected-Content?

Connected-Content hat kein eigenes Rate-Limit. Stattdessen basiert das Rate-Limit auf der Rate, mit der Nachrichten versendet werden. Wir empfehlen, das Rate-Limits für Messaging unter das von Ihnen beabsichtigte Rate-Limits für Connected-Content zu setzen, wenn mehr Connected-Content-Anrufe als Nachrichten gesendet werden.  

### Was ist Caching-Verhalten?

Standardmäßig werden POST-Anfragen nicht zwischengespeichert. Sie können jedoch den Parameter `:cache_max_age` hinzufügen, um den POST-Aufruf in den Cache zu zwingen.
Caching kann dazu beitragen, doppelte Connected-Content-Aufrufe zu vermeiden. Es ist jedoch nicht garantiert, dass dies immer zu einem einzigen Connected-Content-Aufruf pro Nutzer:in führt.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#liquid-usage-use-cases--overview
[16]: [success@braze.com](mailto:success@braze.com)
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
[36]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching
