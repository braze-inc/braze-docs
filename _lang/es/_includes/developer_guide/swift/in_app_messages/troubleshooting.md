{% multi_lang_include inapp_message_troubleshooting.md sdk="iOS" %}

### Solución de problemas de carga de activos (`NSURLError` código `-1008`)

Al integrar Braze junto con bibliotecas de registro de red de terceros, los desarrolladores pueden encontrarse habitualmente con un `NSURLError` con el código del dominio `-1008`. Este error indica que activos como imágenes y fuentes no se han podido recuperar o no se han almacenado en caché. Para evitar estos casos, tendrás que registrar las URL de CDN de Braze en la lista de dominios que deben ser ignorados por estas bibliotecas.

#### Dominios

La lista completa de dominios CDN es la siguiente:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Ejemplos

A continuación se muestran las bibliotecas que se sabe que entran en conflicto con el almacenamiento en caché de activos de Braze, junto con un código de ejemplo para solucionar el problema. Si tu proyecto utiliza una biblioteca que provoca un error de recurso no disponible y no aparece en la lista siguiente, consulta la documentación de esa biblioteca para conocer las API de uso similares.

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


