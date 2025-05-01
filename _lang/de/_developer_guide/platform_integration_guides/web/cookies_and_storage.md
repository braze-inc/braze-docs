---
nav_title: Cookies und Speicherung
article_title: Cookies und Speicherung für das Internet
platform: Web
page_order: 15
page_type: reference
description: "Dieser Referenzartikel beschreibt die verschiedenen Cookies, die das Braze Web SDK verwendet."

---

# Cookies und Speicherung

> Dieser Artikel beschreibt die verschiedenen Cookies, die vom Braze Web SDK verwendet werden.

Bevor Sie weiterlesen, beachten Sie bitte, dass das Braze Web SDK keine Daten im Browser (Cookies oder andere) speichert, bis Ihre Website das SDK [initialisiert](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

Außerdem können sich diese Werte ändern und sollten nicht direkt über Ihre Integration abgerufen werden. Sehen Sie sich stattdessen unsere [JavaScript-Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) für unsere öffentlichen API-Schnittstellen an.

{% multi_lang_include archive/web-v4-rename.md %}

## Cookies {#cookies}

Dieser Abschnitt enthält Informationen darüber, wie Cookies im Braze Web SDK gesetzt und verwaltet werden können. Das Braze Web SDK wurde entwickelt, um Ihnen ein Höchstmaß an Flexibilität, Rechtssicherheit und Relevanz für das Messaging zu bieten.

Wenn Braze Cookies erstellt, werden diese mit einer Verfallszeit von 400 Tagen gespeichert, die sich bei neuen Sitzungen automatisch erneuert.

### Deaktivieren von Cookies {#disable-cookies}

Um alle Cookies zu deaktivieren, verwenden Sie die Option [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) Option, wenn Sie das Internet SDK initialisieren.
Die Deaktivierung von Cookies verhindert, dass Sie anonyme Nutzer, die über Subdomains navigieren, miteinander in Verbindung bringen können, und führt dazu, dass auf jeder Subdomain ein neuer Nutzer angelegt wird.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Um das Tracking von Braze generell zu beenden oder alle gespeicherten Daten des Browsers zu löschen, schlagen Sie in den SDK-Methoden [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) und [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata) nach. Diese beiden Methoden können nützlich sein, wenn ein Nutzer seine Zustimmung widerruft oder Sie alle Braze-Funktionen beenden möchten, nachdem das SDK bereits initialisiert wurde.

### Liste der Cookies

|Cookie|Beschreibung|Größe|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Wird verwendet, um festzustellen, ob der aktuell angemeldete Nutzer:in gewechselt hat und um Ereignisse mit dem aktuellen Nutzer:innen zu verknüpfen.|Basierend auf der Größe des Wertes, der an `changeUser` übergeben wird|
|`ab.storage.sessionId.[your-api-key]`|Zufällig generierter String, der verwendet wird, um festzustellen, ob der Nutzer:in eine neue oder eine bestehende Sitzung startet, um Nachrichten zu synchronisieren und Sitzungs-Analytics zu berechnen.|~200 Bytes|
|`ab.storage.deviceId.[your-api-key]`|Zufällig generierter String zur Identifizierung anonymer Nutzer:innen und zur Unterscheidung der Geräte der Nutzer:innen, der gerätebasiertes Messaging ermöglicht.|~200 Bytes|
|`ab.optOut`|Wird verwendet, um die Opt-out-Präferenz eines Nutzers zu speichern, wenn `disableSDK` aufgerufen wird.|~40 Bytes|
|`ab._gd`|Wird vorübergehend erstellt (und dann gelöscht), um die Root-Level-Cookie-Domain zu bestimmen, die es dem SDK erlaubt, über Sub-Domains hinweg korrekt zu arbeiten.|k.A.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Eigenschaften des Geräts

Standardmäßig erfasst Braze die folgenden Eigenschaften auf Geräteebene, um die Personalisierung von Nachrichten auf der Grundlage von Gerät, Sprache und Zeitzone zu ermöglichen:

* BROWSER
* BROWSER_VERSION
* LANGUAGE
* OS
* RESOLUTION
* ZEIT_ZONE
* USER_AGENT

Sie können die Eigenschaften, die Sie sammeln möchten, deaktivieren oder festlegen, indem Sie die Option `devicePropertyAllowlist` initialization auf eine Liste von [`DeviceProperties`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html) setzen. 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

Standardmäßig sind alle Felder aktiviert. Beachten Sie, dass ohne einige Eigenschaften nicht alle Features ordnungsgemäß funktionieren werden. Zum Beispiel funktioniert die Zustellung zur Ortszeit nicht ohne die Zeitzone.

Um mehr über die automatisch erfassten Eigenschaften des Geräts zu erfahren, besuchen Sie die [SDK-Optionen für die Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 


