---
nav_title: Fehlersuche
article_title: Fehlerbehebung bei In-App Messaging für iOS
platform: Swift
page_order: 6
description: "Dieser Artikel referenziert mögliche Themen zur Fehlerbehebung bei In-App-Nachrichten für das Swift SDK."
channel:
  - in-app messages

---

# Fehlersuche

{% multi_lang_include inapp_message_troubleshooting.md sdk="iOS" %}

### Fehlerbehebung beim Laden von Assets (`NSURLError`-Code `-1008`)

Bei der Integration von Braze zusammen mit Netzwerkprotokollierungsbibliotheken von Drittanbietern stoßen Entwickler häufig auf einen `NSURLError` mit dem Domain-Code `-1008`. Dieser Fehler zeigt an, dass Assets wie Bilder und Schriftarten nicht abgerufen werden konnten oder nicht in den Cache aufgenommen wurden. Um solche Fälle zu umgehen, müssen Sie die CDN-URLs von Braze in die Liste der Domains eintragen, die von diesen Bibliotheken ignoriert werden sollen.

#### Domains

Die vollständige Liste der CDN Domains finden Sie im Folgenden:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Beispiele

Nachfolgend finden Sie Bibliotheken, von denen bekannt ist, dass sie mit dem Asset-Caching von Braze in Konflikt stehen, sowie Beispiel-Code, um das Problem zu umgehen. Wenn Ihr Projekt eine Bibliothek verwendet, die einen Fehler wegen nicht verfügbarer Ressourcen verursacht und die unten nicht aufgeführt ist, konsultieren Sie die Dokumentation dieser Bibliothek für ähnliche APIs zur Verwendung.

##### Netfox

{% tabs %}
{% tab Swift %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];
```
{% endtab %}
{% endtabs %}

##### NetGuard

{% tabs %}
{% tab Swift %}
```swift
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;
```
{% endtab %}
{% endtabs %}

##### XNLogger

{% tabs %}
{% tab Swift %}
```swift
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])
```
{% endtab %}
{% tab Objective-C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}


