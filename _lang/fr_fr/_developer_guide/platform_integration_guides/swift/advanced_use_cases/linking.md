---
nav_title: Création de liens profonds
article_title: Création de liens profonds pour iOS
platform: Swift
page_order: 1
description: "Cet article explique comment implémenter le délégué universel de création de liens profonds pour votre application iOS. Il fournit également des exemples sur la manière de créer des liens profonds vers des paramètres d’applications pour le SDK Swift."

---

# Création de liens profonds

> La création de liens profonds est un moyen de fournir un lien qui lance une application native, affiche un contenu spécifique ou effectue une action spécifique. Si vous souhaitez mettre en place des liens profonds dans votre application iOS pour la première fois, procédez comme suit.

Pour des informations générales sur ce que sont les liens profonds, consultez notre [article FAQ.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking) 

## Étape 1 : Enregistrement d’un schéma

Pour gérer les liens profonds, un schéma personnalisé doit être défini dans votre fichier `Info.plist`. La structure de navigation est définie par un ensemble de dictionnaires. Chacun de ces dictionnaires contient un tableau de chaînes de caractères.

Utiliser l’éditeur Xcode pour modifier votre fichier `Info.plist` :

1. Ajouter une nouvelle clé, `URL types`. Xcode fera automatiquement en sorte qu’un tableau contenant un dictionnaire appelé `Item 0`.
2. Dans `Item 0`, ajouter une clé `URL identifier`. Définissez la valeur sur votre schéma personnalisé.
3. Dans `Item 0`, ajouter une clé `URL Schemes`. Ce sera automatiquement un tableau contenant une chaîne `Item 0`.
4. Définir `URL Schemes` >> `Item 0` à votre schéma personnalisé.

Sinon, si vous souhaitez modifier votre fichier `Info.plist` directement, vous pouvez suivre cette spécification :

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

## Étape 2 : Ajout d'une liste d'autorisation de schémas

Vous devez déclarer les schémas d'URL que vous souhaitez transmettre à `canOpenURL(_:)` en ajoutant la clé `LSApplicationQueriesSchemes` au fichier Info.plist de votre application. Si vous tentez d’appeler des schémas en dehors de cette liste, le système enregistrera une erreur dans les journaux de l’appareil et le lien profond ne s’ouvrira pas. Un exemple de cette erreur ressemblera à ceci :

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Par exemple, si un message in-app doit ouvrir l'application Facebook lorsqu'on appuie dessus, l'application doit avoir le schéma personnalisé de Facebook (`fb`) dans votre liste d'autorisations. Sinon, le système rejettera le lien profond. Les liens profonds qui dirigent vers une page ou s’affichent dans votre propre application nécessitent toujours que le schéma personnalisé de votre application soit répertorié dans le `Info.plist` de votre application.

Votre liste d'autorisations pourrait ressembler à ce qui suit :

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

Pour plus d'informations, reportez-vous à la [documentation d'Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) sur la clé `LSApplicationQueriesSchemes`.

## Étape 3 : Implémenter un gestionnaire

Après avoir activé votre application, iOS appellera la méthode [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc). L'argument important est l'objet [NSURL.](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL) 

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Application Transport Security (ATS)

### Prérequis ATS
Extrait de la [documentation d'Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14): « App Transport Security est une fonctionnalité qui améliore la sécurité des connexions entre une application et des services Web. » La fonctionnalité consiste en des exigences de connexion par défaut conformes aux meilleures pratiques visant les connexions sécurisées. Les applications peuvent remplacer ce comportement par défaut et désactiver la sécurité du transport. »

L'ATS est appliqué par défaut. Il nécessite que toutes les connexions utilisent HTTPS et soient chiffrées à l’aide de TLS 1.2 avec confidentialité de transmission. Pour plus d'informations, reportez-vous à la section [Exigences pour la connexion à l'aide de l'ATS.](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35)  Toutes les images servies par Braze aux terminaux sont gérées par un réseau de diffusion de contenu (« CDN ») qui prend en charge TLS 1.2 et est compatible avec ATS.

Sauf s’ils sont spécifiés comme des exceptions dans le `Info.plist` de votre application, les connexions qui ne suivent pas ces exigences échoueront avec des erreurs qui ressemblent à ceci :

```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

La conformité ATS est appliquée aux liens ouverts dans l'application mobile (notre gestion par défaut des liens cliqués) et ne s'applique pas aux sites ouverts à l'extérieur via un navigateur web.

### Gestion des exigences ATS

Vous pouvez gérer l’ATS de l’une des trois manières suivantes :

#### Assurez-vous que tous les liens sont conformes aux ATS (recommandé)
Votre intégration Braze peut satisfaire aux exigences ATS en s'assurant que tous les liens existants vers lesquels vous amenez les utilisateurs (par exemple, par le biais de messages in-app et de campagnes de notifications push) satisfont aux exigences ATS. Bien qu'il existe des moyens de contourner les restrictions ATS, nous vous recommandons de vous assurer que tous les liens URL sont conformes aux exigences ATS. Compte tenu de l’importance croissante accordée par Apple à la sécurité des applications, il n’est pas garanti que les approches suivantes pour autoriser les exceptions ATS soient prises en charge par Apple.

#### Désactiver partiellement l’ATS
Vous pouvez autoriser un sous-ensemble de liens avec certains domaines ou programmes à traiter comme des exceptions aux règles ATS. Votre intégration Braze satisfera aux exigences ATS si chaque lien que vous utilisez dans un canal de communication Braze est soit conforme ATS, soit géré par une exception.

Pour ajouter un domaine à une exception de l’ATS, ajoutez-le au fichier `Info.plist` de votre application :

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

Pour plus d'informations, consultez l'article d'Apple sur les [clés de sécurité pour le transport d'applications](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33).

#### Désactiver complètement ATS

Vous pouvez désactiver complètement ATS. Notez que ce n’est pas une pratique recommandée, en raison à la fois des protections de sécurité perdues et de la future compatibilité iOS. Pour désactiver ATS, insérez les éléments suivants dans le fichier `Info.plist` de votre application :

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

## Encodage d’URL

Le SDK encode les liens en pourcentage pour créer des `URL`valides. Tous les caractères de lien qui ne sont pas autorisés dans une URL correctement formée, tels que les caractères Unicode, seront échappés en pourcentage.

Pour décoder un lien codé, utilisez la propriété `String` [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding). Vous devez également renvoyer `true` dans le site `BrazeDelegate.braze(_:shouldOpenURL:)`. Un appel à l'action est nécessaire pour déclencher le traitement de l'URL par votre application. 

Par exemple :

{% tabs %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% endtabs %}


## Création de liens profonds vers les paramètres d’application

Vous pouvez tirer parti de `UIApplicationOpenSettingsURLString` pour établir un lien profond entre les utilisateurs et les paramètres de votre application à partir des notifications push de Braze, des messages in-app et du fil d'actualité.

Pour faire passer les utilisateurs de votre application aux paramètres d'iOS :
1. Tout d'abord, assurez-vous que votre application est configurée pour des [liens profonds basés sur des schémas](##step-1-registering-a-scheme) ou des [liens universels](#universal-links).
2. Décidez d'un URI pour le lien profond vers la page **Paramètres** (par exemple, `myapp://settings` ou `https://www.braze.com/settings`).
3. Si vous utilisez des liens profonds basés sur un schéma personnalisé, ajoutez le code suivant à votre méthode `application:openURL:options:` :

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
  NSString *path  = [url path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Personnalisation {#linking-customization}

### Personnalisation de WebView par défaut

La classe `Braze.WebViewController` affiche les URL Web ouvertes par le SDK, généralement lorsque l'option « Ouvrir l’URL Web dans l’application » est sélectionnée pour un lien profond Web.

Vous pouvez personnaliser le `Braze.WebViewController` au moyen de la méthode de délégué [`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/).

### Gestion de la personnalisation des liens

Le protocole `BrazeDelegate` peut être utilisé pour personnaliser la gestion des URL telles que les liens profonds, les URL Web et les liens universels. Pour définir le délégué lors de l'initialisation de Braze, définissez un objet délégué sur l'instance `Braze`. Braze appellera ensuite l’implémentation de votre délégué `shouldOpenURL` avant de gérer les URI.

#### Liens universels

Braze prend en charge les liens universels dans les notifications push, les messages in-app et les cartes de contenu. Pour activer la prise en charge des liens universels, [`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) doit être défini sur `true`.

Lorsque cette option est activée, Braze transmet les liens universels à l'adresse `AppDelegate` de votre application via la méthode [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) méthode. 

Votre application doit également être configurée pour gérer les liens universels. Reportez-vous à la [documentation d'Apple](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) pour vous assurer que votre application est configurée correctement pour les liens universels.

{% alert warning %}
Le transfert de lien universel nécessite l'accès aux droits de l'application. Lorsque l'application est exécutée dans un simulateur, ces droits ne sont pas directement disponibles et les liens universels ne sont pas transmis aux gestionnaires du système.
Pour ajouter la prise en charge aux constructions de simulateurs, vous pouvez ajouter le fichier de l'application `.entitlements` à la phase de création de _Copy Bundle Resources._  Pour plus d’informations, reportez-vous à [`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks).
{% endalert %}

{% alert note %}
Le SDK n'interroge pas le fichier `apple-app-site-association` de vos domaines. Il fait la différence entre les liens universels et les URL ordinaires en ne tenant compte que du nom de domaine. Par conséquent, le SDK ne respecte aucune règle d'exclusion définie dans l’`apple-app-site-association` selon les [domaines associés](https://developer.apple.com/documentation/xcode/supporting-associated-domains).
{% endalert %}

### Exemple d’intégration : BrazeDelegate

{% tabs %}
{% tab swift %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, voir [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate).


