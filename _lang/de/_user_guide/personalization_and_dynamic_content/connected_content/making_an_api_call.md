---
nav_title: Einen Connected-Content-Aufruf tätigen
article_title: Aufruf einer Connected-Content-API
page_order: 0
description: "In diesem Referenzartikel erfahren Sie, wie Sie einen Connected-Content-API-Aufruf durchführen. Zudem erhalten Sie hier hilfreiche Beispiele und fortgeschrittene Anwendungsfälle für Connected-Content."
search_rank: 2
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} Aufruf einer Connected-Content-API

> Verwenden Sie Connected-Content, um alle über APIs zugänglichen Informationen direkt in Nachrichten einzufügen, die Sie an Nutzer:innen senden. Sie können Inhalte entweder direkt von Ihrem Webserver oder von öffentlich zugänglichen APIs beziehen.<br><br>Auf dieser Seite erfahren Sie, wie Sie Connected-Content-API-Aufrufe tätigen, fortgeschrittene Connected-Content-Anwendungsfälle nutzen, Fehler behandeln und mehr.

## Connected-Content-Aufrufvolumen verstehen

{% alert important %}
Ein Versand entspricht nicht einem Connected-Content-Aufruf. Braze garantiert kein 1:1-Verhältnis zwischen Nachrichtenversand und Connected-Content-Anfragen. Das System ist darauf ausgelegt, korrektes Nachrichten-Rendering und korrekte Zustellung gegenüber der Minimierung der Aufrufanzahl zu bevorzugen. Ihre Endpunkte müssen so konzipiert sein, dass sie mehr Anfragen verarbeiten können als die Anzahl der Empfänger:innen oder gesendeten Nachrichten.
{% endalert %}

Braze kann denselben Connected-Content-API-Aufruf mehr als einmal pro Empfänger:in tätigen. Häufige Gründe dafür sind:

- **E-Mail mit mehreren Teilen:** Eine einzelne E-Mail kann separate Rendering-Durchläufe für den HTML-Body, den Nur-Text-Body und die Accelerated Mobile Pages (AMP)-Version (falls vorhanden) auslösen. Jeder Durchlauf kann Connected-Content in diesem Teil auslösen, sodass eine Empfängerin oder ein Empfänger mehrere identische oder ähnliche Aufrufe erzeugen kann.
- **Validierung und Wiederholungsversuche:** Nachrichten-Payloads können pro Empfänger:in mehrfach gerendert werden – für Validierung, Wiederholungslogik oder andere interne Zwecke.
- **Kanalverhalten:** Connected-Content wird ausgeführt, wenn die Nachricht gerendert wird. Bei In-App-Nachrichten wird die Nachricht zum Zeitpunkt der Impression gerendert.

Wenn Sie in Ihren Logs mehr Connected-Content-Aufrufe als Sendungen oder Empfänger:innen sehen, ist dieses Verhalten erwartungsgemäß. Hinweise zur Reduzierung der Last und zur Skalierungsplanung finden Sie unter [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints).

## Senden eines Connected-Content-Aufrufs

{% raw %}

Um einen Connected-Content-Aufruf zu senden, verwenden Sie das Tag `{% connected_content %}`. Mit diesem Tag können Sie Variablen zuweisen oder deklarieren, indem Sie `:save` verwenden. Auf Aspekte dieser Variablen kann später in der Nachricht mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid) Bezug genommen werden.

Der folgende Nachrichtentext greift beispielsweise auf die URL `http://numbersapi.com/random/trivia` zu und fügt einen witzigen Wissenswert in Ihre Nachricht ein:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Hinzufügen von Variablen

Sie können bei Connected-Content-Anfragen auch Nutzerprofil-Attribute als Variablen in den URL-String aufnehmen. 

Sie können zum Beispiel einen Webdienst haben, der Inhalte auf der Grundlage der E-Mail-Adresse und ID einer Nutzerin oder eines Nutzers zurückgibt. Wenn Sie Attribute übergeben, die Sonderzeichen enthalten, wie z. B. das at-Zeichen (@), stellen Sie sicher, dass Sie den Liquid-Filter `url_param_escape` verwenden, um alle Zeichen, die in URLs nicht zulässig sind, durch ihre URL-freundliche, maskierte Version zu ersetzen, wie im folgenden Attribut für E-Mail-Adressen gezeigt.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Attribut-Werte müssen von `${}` umgeben sein, um in unserer Version der Liquid-Syntax korrekt zu funktionieren.
{% endalert %}

Connected-Content-Anfragen unterstützen nur GET- und POST-Anfragen.

## Fehlerbehandlung

Wenn die URL nicht verfügbar ist und eine 404-Seite erreicht, rendert Braze einen leeren String an ihrer Stelle. Wenn die URL eine HTTP-500- oder -502-Seite erreicht, schlägt die URL bei der Wiederholungslogik fehl.

Wenn der Endpunkt JSON zurückgibt, können Sie dies erkennen, indem Sie prüfen, ob der Wert `connected` null ist, und dann [die Nachricht bedingt abbrechen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). Braze lässt nur URLs zu, die über Port 80 (HTTP) und 443 (HTTPS) kommunizieren.

### Erkennung fehlerhafter Hosts

Connected-Content verwendet einen Mechanismus zur Erkennung fehlerhafter Hosts, um zu erkennen, wenn der Zielhost eine hohe Rate an erheblicher Verlangsamung oder Überlastung aufweist, was zu Timeouts, zu vielen Anfragen oder anderen Ergebnissen führt, die verhindern, dass Braze erfolgreich mit dem Ziel-Endpunkt kommunizieren kann. Diese Funktion dient als Schutzmaßnahme, um unnötige Last zu reduzieren, die dem Zielhost Probleme bereiten könnte. Sie dient auch der Stabilisierung der Braze-Infrastruktur und der Aufrechterhaltung schneller Nachrichtenübertragungsgeschwindigkeiten.

Wenn der Zielhost eine hohe Rate an erheblicher Verlangsamung oder Überlastung aufweist, hält Braze Anfragen an den Zielhost für eine Minute vorübergehend an und simuliert stattdessen Antworten, die den Fehler anzeigen. Nach einer Minute prüft Braze den Zustand des Hosts mit einer kleinen Anzahl von Anfragen, bevor die Anfragen mit voller Geschwindigkeit wieder aufgenommen werden, wenn der Host als gesund befunden wird. Wenn der Host immer noch fehlerhaft ist, wartet Braze eine weitere Minute, bevor ein erneuter Versuch gestartet wird.

Wenn Anfragen an den Zielhost durch den Detektor für fehlerhafte Hosts gestoppt werden, rendert Braze weiterhin Nachrichten und folgt Ihrer Liquid-Logik, als hätte es einen Fehlerantwortcode erhalten. Wenn Sie sicherstellen möchten, dass diese Connected-Content-Anfragen erneut versucht werden, wenn sie vom Detektor für fehlerhafte Hosts angehalten werden, verwenden Sie die Option `:retry`. Weitere Informationen über die Option `:retry` finden Sie unter [Connected-Content-Wiederholungsversuche]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Wenn Sie glauben, dass die Erkennung fehlerhafter Hosts Probleme verursacht, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/support_contact/).

{% alert note %}
Sie können bestimmte URLs auf eine Zulassungsliste setzen, die für Connected-Content verwendet werden. Um auf dieses Feature zuzugreifen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

{% alert tip %}
Besuchen Sie die Seite [Fehlerbehebung für Webhook- und Connected-Content-Anfragen]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection), um mehr darüber zu erfahren, wie Sie häufige Fehlercodes beheben können.
{% endalert %}

### Rate-Limits (429) im Vergleich zur Erkennung fehlerhafter Hosts

Hierbei handelt es sich um unterschiedliche Mechanismen:

- **429 Too Many Requests:** Ihr Endpunkt (oder ein vorgelagerter Dienst) gibt diese Antwort zurück. Das bedeutet, dass Ihr Server oder Ihre Middleware den Datenverkehr ablehnt, oft weil ein eigenes Rate-Limit besteht. Braze wendet kein separates Rate-Limit auf Connected-Content an; das Connected-Content-Anfragevolumen skaliert direkt mit Ihrem [Rate-Limit für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). Da Nachrichten pro Empfänger:in mehrfach gerendert werden können (z. B. für E-Mail-HTML, Nur-Text und AMP), kann die Anzahl der Connected-Content-Anfragen dieses Rate-Limit überschreiten – gehen Sie nicht davon aus, dass sie kleiner oder gleich der von Ihnen eingestellten Nachrichten pro Minute ist. Wenn Sie 429-Fehler sehen, skalieren Sie Ihren Endpunkt oder Ihre Middleware, um das erwartete Anfragevolumen zu bewältigen, oder senken Sie das Rate-Limit der Kampagne oder des Canvas-Schritts, damit weniger Nachrichten (und somit weniger Connected-Content-Aufrufe) pro Minute gesendet werden.
- **Erkennung fehlerhafter Hosts:** Eine Braze-seitige Schutzmaßnahme, die nach einer hohen Rate und einem hohen Volumen an *Fehlern* innerhalb eines Einminuten-Fensters ausgelöst wird. Die Fehlerzählung umfasst die Statuscodes `408`, `429`, `502`, `503`, `504` und `529`. Wenn ausgelöst, hält Braze Anfragen an diesen Host vorübergehend an und simuliert eine Fehlerantwort. Dies ist unabhängig von Ihrem eigenen Rate-Limiting. Für Erkennungsschwellenwerte und weitere Details siehe [Fehlerbehebung für Webhook- und Connected-Content-Anfragen]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/#unhealthy-host-detection). Um die Erkennung fehlerhafter Hosts zu vermeiden, stellen Sie sicher, dass Ihr Endpunkt das unter [Connected-Content-Aufrufvolumen verstehen](#understanding-connected-content-call-volume) und [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints) beschriebene Aufrufvolumen bewältigen kann.

## Effiziente Performance ermöglichen

Da Braze Nachrichten sehr schnell zustellt, sollten Sie sicherstellen, dass Ihr Server Tausende von gleichzeitigen Verbindungen verarbeiten kann, damit er beim Abrufen von Inhalten nicht überlastet wird. Wenn Sie öffentliche APIs verwenden, vergewissern Sie sich, dass Ihre Nutzung nicht gegen die Rate-Limits verstößt, die der API-Anbieter möglicherweise einsetzt. Braze verlangt aus Performance-Gründen, dass die Antwortzeit des Servers weniger als zwei Sekunden beträgt. Wenn der Server länger als zwei Sekunden braucht, um zu antworten, werden die Inhalte nicht eingefügt.

Weitere Informationen zur Planung der Endpunkt-Kapazität und zur Reduzierung des Aufrufvolumens finden Sie unter [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints).

## Was Sie wissen sollten

* Braze erhebt keine Gebühren für API-Aufrufe, und diese werden nicht auf Ihre Datenpunkt-Nutzung angerechnet.
* Für Connected-Content-Antworten gibt es ein Limit von 1 MB.
* Connected-Content wird ausgeführt, wenn die Nachricht gerendert wird. Bei In-App-Nachrichten wird die Nachricht zum Zeitpunkt der Impression gerendert.
* Connected-Content-Aufrufe folgen keinen Weiterleitungen.

## Best Practices für Endpunkte mit hohem Volumen

Wenn Ihre Nachrichten Connected-Content verwenden und Sie mit hohem Volumen versenden, planen Sie mehr Anfragen ein als die Anzahl der Empfänger:innen oder Sendungen:

1. **Spitzenlast abschätzen:** Verwenden Sie einen konservativen Multiplikator bei der Dimensionierung Ihres Endpunkts oder Ihrer Middleware – Connected-Content-Anfragen können die Anzahl der Empfänger:innen oder gesendeten Nachrichten übersteigen. Beispielsweise kann bei E-Mails eine einzelne Empfängerin oder ein einzelner Empfänger mehrere Aufrufe erzeugen (HTML, Nur-Text und AMP), sodass Empfänger:innen × 2 oder × 3 oft als konservative Schätzung verwendet wird.
2. **Caching nutzen, wo es sinnvoll ist:** GET-Anfragen werden standardmäßig zwischengespeichert. Für POST-Anfragen fügen Sie `:cache_max_age` hinzu, wenn die Antwort für einen Zeitraum wiederverwendet werden kann (z. B. Token oder Inhalte, die sich nicht pro Anfrage ändern). Siehe [Antworten zwischenspeichern]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/) und die [FAQ zum POST-Caching](#what-is-caching-behavior) weiter unten.
3. **Rate-Limit für die Zustellgeschwindigkeit festlegen:** Das [Rate-Limit für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) bei Kampagnen oder Canvas-Schritten ist der einzige Hebel, um das Connected-Content-Anfragevolumen indirekt zu begrenzen – Braze wendet kein eigenes Rate-Limit auf Connected-Content an. Es ist nur ein Näherungswert und kein perfekter, da Connected-Content-Anfragen nicht im Verhältnis 1:1 zu Nachrichten stehen. Verwenden Sie es, um das Nachrichten- (und damit Connected-Content-) Volumen innerhalb dessen zu halten, was Ihr Endpunkt bewältigen kann.
4. **Auf Idempotenz und Wiederholungsversuche auslegen:** Braze kann Ihren Endpunkt mehr als einmal pro Empfänger:in aufrufen. Stellen Sie sicher, dass Ihr Endpunkt doppelte Anfragen ohne unerwünschte Nebeneffekte tolerieren kann.

## Authentifizierungsarten

### Einfache Authentifizierung verwenden

Wenn die URL eine Basisauthentifizierung erfordert, kann Braze Zugangsdaten für Sie speichern, die Sie in Ihrem API-Aufruf verwenden können. Unter **Einstellungen** > **Connected Content** können Sie bestehende Zugangsdaten verwalten und neue hinzufügen.

![Die Connected-Content-Einstellungen im Braze-Dashboard.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Um neue Zugangsdaten hinzuzufügen, wählen Sie **Zugangsdaten hinzufügen** > **Basisauthentifizierung**. 

![Dropdown-Menü „Zugangsdaten hinzufügen" mit der Option, die Basisauthentifizierung oder die Token-Authentifizierung zu verwenden.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Geben Sie Ihren Zugangsdaten einen Namen und geben Sie den Benutzernamen und das Passwort ein.

![Das Fenster „Neue Zugangsdaten erstellen" mit der Möglichkeit, einen Namen, einen Benutzernamen und ein Passwort einzugeben.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Sie können diese Zugangsdaten dann in Ihren API-Aufrufen verwenden, indem Sie auf den Namen des Tokens verweisen:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Wenn Sie Zugangsdaten löschen, denken Sie daran, dass alle Connected-Content-Aufrufe, die versuchen, diese zu verwenden, abgebrochen werden.
{% endalert %}

### Token-Authentifizierung verwenden

Bei der Verwendung von Braze Connected-Content kann es vorkommen, dass bestimmte APIs ein Token anstelle eines Benutzernamens und eines Passworts erfordern. Braze kann auch Zugangsdaten speichern, die Token-Authentifizierungs-Headerwerte enthalten.

Um Zugangsdaten mit Token-Werten hinzuzufügen, wählen Sie **Zugangsdaten hinzufügen** > **Token-Authentifizierung**. Fügen Sie dann die Schlüssel-Wert-Paare für Ihre API-Aufruf-Header und die zulässige Domain hinzu.

![Ein Beispiel für ein Token „token_credential_abc" mit Details zur Token-Authentifizierung.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Sie können diese Zugangsdaten dann in Ihren API-Aufrufen verwenden, indem Sie auf den Namen der Zugangsdaten verweisen:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Offene Authentifizierung (OAuth) verwenden

Einige API-Konfigurationen erfordern den Abruf eines Zugriffstokens, das dann zur Authentifizierung des API-Endpunkts verwendet werden kann, auf den Sie zugreifen möchten.

#### 1. Schritt: Zugriffstoken abrufen

Das folgende Beispiel veranschaulicht das Abrufen und Speichern eines Zugriffstokens in einer lokalen Variablen, das dann zur Authentifizierung des nachfolgenden API-Aufrufs verwendet werden kann. Ein `:cache_max_age`-Parameter kann hinzugefügt werden, um die Gültigkeitsdauer des Zugriffstokens abzugleichen und die Anzahl der ausgehenden Connected-Content-Aufrufe zu reduzieren. Siehe [Konfigurierbares Caching]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching) für weitere Informationen.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### 2. Schritt: API mit dem abgerufenen Zugriffstoken autorisieren

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

### Bearbeitung der Zugangsdaten

Sie können den Namen der Zugangsdaten für die Authentifizierungsarten bearbeiten.

- Bei der einfachen Authentifizierung können Sie den Benutzernamen und das Passwort aktualisieren. Beachten Sie, dass das zuvor eingegebene Passwort nicht sichtbar ist.
- Bei der Token-Authentifizierung können Sie die Schlüssel-Wert-Paare des Headers und die zulässige Domain aktualisieren. Beachten Sie, dass die zuvor eingestellten Header-Werte nicht sichtbar sind.

![Die Möglichkeit, Zugangsdaten zu bearbeiten.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## Connected-Content-IP-Allowlisting

Wenn eine Nachricht mit Connected-Content von Braze gesendet wird, stellen die Braze-Server automatisch Netzwerkanfragen an die Server unserer Kund:innen oder Dritter, um Daten abzurufen. Mit der IP-Zulassungsliste können Sie überprüfen, ob die Connected-Content-Anfragen tatsächlich von Braze stammen, was eine zusätzliche Sicherheitsebene darstellt.

Braze sendet Connected-Content-Anfragen von den folgenden IP-Bereichen. Die aufgelisteten Bereiche werden automatisch und dynamisch zu allen API-Schlüsseln hinzugefügt, für die ein Opt-in für das Allowlisting vorgenommen wurde. 

Braze verfügt über einen reservierten Satz von IPs, die für alle Dienste verwendet werden, von denen nicht alle zu einem bestimmten Zeitpunkt aktiv sind. Damit kann Braze bei Bedarf Daten von einem anderen Rechenzentrum aus versenden oder Wartungsarbeiten durchführen, ohne dass dies Auswirkungen auf die Kund:innen hat. Braze kann eine, eine Teilmenge oder alle der folgenden aufgelisteten IPs verwenden, wenn Connected-Content-Anfragen gestellt werden.

{% multi_lang_include data_centers.md datacenters='ips' %}

### `User-Agent`-Header

Braze fügt in alle Connected-Content- und Webhook-Anfragen einen `User-Agent`-Header ein, der in etwa wie folgt aussieht:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Denken Sie daran, dass sich der Hash-Wert regelmäßig ändert. Wenn Sie den Datenverkehr nach `User-Agent` filtern, lassen Sie alle Werte zu, die mit `Braze Sender` beginnen.
{% endalert %}

## Fehlerbehebung

Verwenden Sie [Webhook.site](https://webhook.site/), um Ihre Connected-Content-Aufrufe zu debuggen. 

1. Tauschen Sie die URL in Ihrem Connected-Content-Aufruf gegen die eindeutige URL aus, die auf der Website generiert wurde.
2. Testen Sie Ihre Kampagne oder Ihren Canvas-Schritt in der Vorschau, um zu sehen, wie die Anfragen auf dieser Website ankommen.

Mit diesem Tool können Sie Probleme mit den Anfrage-Headern, dem Anfragetext und anderen Informationen diagnostizieren, die beim Aufruf gesendet werden.

## Häufig gestellte Fragen

### Warum gibt es mehr Connected-Content-Aufrufe als Nutzer:innen oder Sendungen? 

Dies ist erwartungsgemäßes Verhalten. Braze kann denselben Connected-Content-API-Aufruf mehr als einmal pro Empfänger:in tätigen, da Nachrichten-Payloads mehrfach gerendert werden können (z. B. für E-Mail-HTML, Nur-Text und AMP; für Validierung oder Wiederholungslogik; oder andere interne Zwecke). Es gibt kein garantiertes 1:1-Verhältnis zwischen Sendungen und Connected-Content-Aufrufen. Siehe [Connected-Content-Aufrufvolumen verstehen](#understanding-connected-content-call-volume) und [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints) für Details und Gegenmaßnahmen.

### Wie funktioniert das Rate-Limiting bei Connected-Content?

Connected-Content hat kein eigenes Rate-Limit. Stattdessen basiert das Rate-Limit auf der Rate, mit der Nachrichten versendet werden. Wir empfehlen, das Messaging-Rate-Limit unter das von Ihnen beabsichtigte Connected-Content-Rate-Limit zu setzen, wenn mehr Connected-Content-Aufrufe als Nachrichten gesendet werden.  

### Was ist das Caching-Verhalten?

GET-Anfragen werden standardmäßig zwischengespeichert (siehe [Antworten zwischenspeichern]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/)). **POST-Anfragen werden standardmäßig nicht zwischengespeichert**, aber Sie können das Caching aktivieren, indem Sie `:cache_max_age` zum Connected-Content-Aufruf hinzufügen. Dies kann die Endpunkt-Last reduzieren, wenn derselbe POST (z. B. eine Token- oder Inhaltsanfrage) innerhalb des Cache-Fensters wiederholt ausgeführt würde.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

Caching kann dazu beitragen, doppelte Connected-Content-Aufrufe zu reduzieren, garantiert aber nicht einen einzigen Aufruf pro Nutzer:in. Die Cache-Dauer liegt zwischen fünf Minuten und vier Stunden. Alle Details finden Sie unter [Antworten zwischenspeichern]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/).

### Was ist das Standard-HTTP-Verhalten von Connected-Content? 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}