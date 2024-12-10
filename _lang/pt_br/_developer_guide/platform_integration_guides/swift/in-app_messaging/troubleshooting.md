---
nav_title: Solução de problemas
article_title: Solução de problemas de envio de mensagens no app para iOS
platform: Swift
page_order: 6
description: "Este artigo de referência aborda os possíveis tópicos de solução de problemas com mensagens no app do iOS para o Swift SDK."
channel:
  - in-app messages

---

# Solução de problemas

{% multi_lang_include inapp_message_troubleshooting.md sdk="iOS" %}

### Solução de problemas de carregamento de ativos (`NSURLError` código `-1008`)

Ao integrar a Braze com bibliotecas de registro de rede de terceiros, os desenvolvedores geralmente se deparam com um `NSURLError` com o código de domínio `-1008`. Esse erro indica que ativos como imagens e fontes não puderam ser recuperados ou não foram armazenados em cache. Para contornar esses casos, será necessário registrar os URLs de CDN do Braze na lista de domínios que devem ser ignorados por essas bibliotecas.

#### Domínios

A lista completa de domínios CDN está listada abaixo:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Exemplos

Abaixo estão as bibliotecas que são conhecidas por entrar em conflito com o cache de ativos do Braze, juntamente com um código de exemplo para contornar o problema. Se seu projeto usa uma biblioteca que causa um erro de recurso indisponível e não está listada abaixo, consulte a documentação dessa biblioteca para obter APIs de uso semelhantes.

##### Netfox

{% tabs %}
{% tab Swift %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab Objective C %}
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
{% tab Objective C %}
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
{% tab Objective C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}


