{% multi_lang_include inapp_message_troubleshooting.md sdk="iOS" %}

### Résolution des problèmes de chargement des ressources (`NSURLError` code `-1008`)

Lors de l'intégration de Braze avec des bibliothèques de journalisation réseau tierces, les développeurs peuvent fréquemment rencontrer une `NSURLError` avec le code de domaine `-1008`. Cette erreur indique que des ressources telles que des images et des polices n'ont pas pu être récupérées ou que leur mise en cache a échoué. Pour contourner ces cas, vous devrez enregistrer les URL de diffusion de contenu de Braze dans la liste des domaines qui doivent être ignorés par ces bibliothèques.

#### Domaines

La liste complète des domaines de diffusion de contenu est indiquée ci-dessous :

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Exemples

Vous trouverez ci-dessous les bibliothèques connues pour être en conflit avec la mise en cache des ressources de Braze, ainsi qu'un exemple de code permettant de contourner le problème. Si votre projet utilise une bibliothèque qui provoque une erreur de ressource indisponible et qui n'est pas répertoriée ci-dessous, consultez la documentation de cette bibliothèque pour connaître les API d'utilisation similaires.

##### Netfox

{% tabs %}
{% tab Swift %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab Objectif-C %}
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
{% tab Objectif-C %}
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
{% tab Objectif-C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}


