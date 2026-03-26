---
nav_title: Création de liens profonds
article_title: Création de liens profonds pour iOS
platform: iOS
page_order: 0
description: "Cet article explique comment implémenter le délégué universel de création de liens profonds pour votre application iOS, ainsi que des exemples sur la manière de créer des liens profonds vers les paramètres d'application."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Création de liens profonds pour iOS

Pour obtenir des informations de base sur les liens profonds, consultez notre [article du Guide de l'utilisateur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking). Si vous souhaitez implémenter des liens profonds pour la première fois dans votre application Braze, les étapes ci-dessous vous aideront à démarrer.

## Étape 1 : Enregistrer un schéma

Vous devez déclarer un schéma personnalisé dans le fichier `Info.plist`. La structure de navigation est définie par un ensemble de dictionnaires. Chacun de ces dictionnaires contient un tableau de chaînes de caractères.

Utilisez Xcode pour modifier votre fichier `Info.plist` :

1. Ajoutez une nouvelle clé, `URL types`. Xcode en fera automatiquement un tableau contenant un dictionnaire appelé `Item 0`.
2. Dans `Item 0`, ajoutez une clé `URL identifier`. Définissez la valeur sur votre schéma personnalisé.
3. Dans `Item 0`, ajoutez une clé `URL Schemes`. Ce sera automatiquement un tableau contenant une chaîne `Item 0`.
4. Définissez `URL Schemes` >> `Item 0` sur votre schéma personnalisé.

Sinon, si vous souhaitez modifier votre fichier `Info.plist` directement, vous pouvez suivre cette spécification :

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>{YOUR.SCHEME}</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>{YOUR.SCHEME}</string>
        </array>
    </dict>
</array>
```

## Étape 2 : Ajouter le schéma personnalisé à la liste autorisée (iOS 9+)

À partir d'iOS 9, les applications doivent disposer d'une liste autorisée de schémas personnalisés que l'application est autorisée à ouvrir. Toute tentative d'appel de schémas en dehors de cette liste entraînera l'enregistrement d'une erreur dans les journaux de l'appareil, et le lien profond ne s'ouvrira pas. Voici un exemple de cette erreur :

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Par exemple, si un message in-app doit ouvrir l'application Facebook lorsqu'il est touché, l'application doit avoir le schéma personnalisé Facebook (`fb`) dans la liste autorisée. Sinon, le système rejettera le lien profond. Les liens profonds qui dirigent vers une page ou une vue au sein de votre propre application nécessitent toujours que le schéma personnalisé de votre application soit répertorié dans le `Info.plist` de votre application.

Vous devez ajouter tous les schémas dont l'application a besoin pour créer des liens profonds dans une liste autorisée dans le `Info.plist` de votre application avec la clé `LSApplicationQueriesSchemes`. Par exemple :

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>facebook</string>
    <string>twitter</string>
</array>
```

Pour plus d'informations, consultez la [documentation d'Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) sur la clé `LSApplicationQueriesSchemes`.

## Étape 3 : Implémenter un gestionnaire

Après l'activation de votre application, iOS appellera la méthode [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc). L'argument important est l'objet [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL).

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Here you should insert code to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Here you should insert code to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% endtabs %}

![]({% image_buster /assets/img_archive/deep_link.png %})

# Liens universels

Pour utiliser des liens universels, assurez-vous d'avoir ajouté un domaine enregistré aux capacités de votre application et d'avoir téléchargé un fichier `apple-app-site-association`. Implémentez ensuite la méthode `application:continueUserActivity:restorationHandler:` dans votre `AppDelegate`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application
continueUserActivity:(NSUserActivity *)userActivity
  restorationHandler:(void (^)(NSArray *restorableObjects))restorationHandler {
  if ([userActivity.activityType isEqualToString:NSUserActivityTypeBrowsingWeb]) {
    NSURL *url = userActivity.webpageURL;
    // Handle url
  }
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  if (userActivity.activityType == NSUserActivityTypeBrowsingWeb) {
    let url = userActivity.webpageURL
    // Handle url
  }
  return true
}
```

{% endtab %}
{% endtabs %}

Consultez la [documentation d'Apple](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html) pour plus d'informations.

{% alert note %}
L'intégration par défaut des liens universels n'est pas compatible avec les notifications push ni les messages in-app de Braze. Consultez la section [personnalisation de la gestion des liens](#linking-handling-customization) pour gérer les liens universels au sein de votre application. Sinon, nous vous recommandons d'utiliser des [liens profonds basés sur des schémas](#step-1-registering-a-scheme) avec les notifications push et les messages in-app.
{% endalert%}

## App Transport Security (ATS)
iOS 9 a introduit un changement majeur affectant les URL web intégrées dans les messages in-app et les notifications push.

### Prérequis ATS
Extrait de la [documentation d'Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14) : « App Transport Security est une fonctionnalité qui améliore la sécurité des connexions entre une application et des services web. Cette fonctionnalité consiste en des exigences de connexion par défaut conformes aux meilleures pratiques en matière de connexions sécurisées. Les applications peuvent remplacer ce comportement par défaut et désactiver la sécurité du transport. »

L'ATS est appliqué par défaut sur iOS 9+. Il nécessite que toutes les connexions utilisent HTTPS et soient chiffrées à l'aide de TLS 1.2 avec confidentialité de transmission. Pour plus d'informations, consultez la section [Exigences pour la connexion à l'aide de l'ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35). Toutes les images servies par Braze aux appareils finaux sont gérées par un réseau de diffusion de contenu (« CDN ») qui prend en charge TLS 1.2 et est compatible avec ATS.

Sauf si elles sont spécifiées comme exceptions dans le `Info.plist` de votre application, les connexions qui ne respectent pas ces exigences échoueront avec des erreurs ressemblant à ceci :

```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

La conformité ATS est appliquée aux liens ouverts dans l'application mobile (notre gestion par défaut des liens cliqués) et ne s'applique pas aux sites ouverts à l'extérieur via un navigateur web.

### Gestion des exigences ATS

Vous pouvez gérer l'ATS de l'une des trois manières suivantes :

#### Confirmer que tous les liens sont conformes à l'ATS (recommandé)
Votre intégration Braze peut satisfaire aux exigences de l'ATS en veillant à ce que tous les liens existants vers lesquels vous dirigez les utilisateurs (via des messages in-app et des campagnes push) respectent les exigences de l'ATS. Bien qu'il existe des moyens de contourner les restrictions ATS, nous vous recommandons de vérifier que toutes les URL liées sont conformes à l'ATS. Compte tenu de l'importance croissante accordée par Apple à la sécurité des applications, il n'est pas garanti que les approches suivantes pour autoriser les exceptions ATS soient prises en charge par Apple.

Un outil SSL peut vous aider à identifier les problèmes de sécurité du serveur web. Ce [test de serveur SSL](https://www.ssllabs.com/ssltest/index.html) de Qualys, Inc. fournit un élément spécifiquement dédié à la conformité Apple ATS 9 et iOS 9.

#### Désactiver partiellement l'ATS
Vous pouvez autoriser un sous-ensemble de liens avec certains domaines ou schémas à être traités comme des exceptions aux règles ATS. Votre intégration Braze satisfera aux exigences ATS si chaque lien que vous utilisez dans un canal de communication Braze est soit conforme à l'ATS, soit géré par une exception.

Pour ajouter un domaine comme exception de l'ATS, ajoutez l'élément suivant au fichier `Info.plist` de votre application :

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

#### Désactiver complètement l'ATS

Vous pouvez désactiver complètement l'ATS. Notez que cette pratique n'est pas recommandée, en raison à la fois de la perte des protections de sécurité et de la compatibilité future avec iOS. Pour désactiver l'ATS, insérez les éléments suivants dans le fichier `Info.plist` de votre application :

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

Consultez [Shipping an App With App Transport Security](http://timekl.com/blog/2015/08/21/shipping-an-app-with-app-transport-security/?utm_campaign=iOS+Dev+Weekly&utm_medium=email&utm_source=iOS_Dev_Weekly_Issue_213) pour plus d'informations sur le débogage des échecs ATS.

## Encodage d'URL

À partir du SDK Braze pour iOS v2.21.0, le SDK encode les liens en pourcentage pour créer des `NSURL` valides. Tous les caractères de lien qui ne sont pas autorisés dans une URL correctement formée, tels que les caractères Unicode, seront échappés en pourcentage.

Pour décoder un lien encodé, utilisez la méthode `NSString` [`stringByRemovingPercentEncoding`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/index.html#//apple_ref/occ/instm/NSString/stringByRemovingPercentEncoding). Notez que vous devez également renvoyer `YES` dans le `ABKURLDelegate` et qu'un appel à l'action est nécessaire pour déclencher la gestion de l'URL par l'application. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% endtabs %}

## Personnalisation {#linking-customization}

### Personnalisation de la WebView par défaut

La classe personnalisable `ABKModalWebViewController` affiche les URL web ouvertes par le SDK, généralement lorsque l'option « Ouvrir l'URL web dans l'application » est sélectionnée pour un lien profond web.

Vous pouvez déclarer une catégorie ou modifier directement la classe `ABKModalWebViewController` pour appliquer la personnalisation à la vue web. Consultez le fichier [.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKModalWebViewController.h) et le fichier [.m](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/ABKModalWebViewController.m) de la classe pour plus de détails.

### Personnalisation de la gestion des liens {#linking-handling-customization}

Le protocole `ABKURLDelegate` peut être utilisé pour personnaliser la gestion des URL telles que les liens profonds, les URL web et les liens universels. Pour définir le délégué lors de l'initialisation de Braze, passez un objet délégué à `ABKURLDelegateKey` dans les `appboyOptions` de [`startWithApiKey:inApplication:withAppboyOptions:`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Braze appellera ensuite l'implémentation de votre délégué `handleAppboyURL:fromChannel:withExtras:` avant de gérer les URI.

#### Exemple d'intégration : ABKURLDelegate

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)handleAppboyURL:(NSURL *)url fromChannel:(ABKChannel)channel withExtras:(NSDictionary *)extras {
  if ([[url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return YES;
  }
  // Let Braze handle links otherwise
  return NO;
}
```

{% endtab %}
{% tab swift %}

```swift
func handleAppboyURL(_ url: URL?, from channel: ABKChannel, withExtras extras: [AnyHashable : Any]?) -> Bool {
  if (url.host == "MY-DOMAIN.com") {
    // Custom handle link here
    return true;
  }
  // Let Braze handle links otherwise
  return false;
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Lorsque `handleAppboyURL:fromChannel:withExtras:` renvoie `YES`, Braze considère que votre application gère l'URL et ne l'ouvrira pas. Si vous gérez des liens universels, vous devez explicitement router l'URL vers le gestionnaire de liens universels de votre application, par exemple en appelant vous-même `application:continueUserActivity:restorationHandler:`. Renvoyer `YES` sans gérer l'URL entraînera la fermeture du message in-app ou de la carte de contenu sans action visible.

Renvoyez `NO` si vous souhaitez que Braze gère l'URL avec son comportement par défaut.
{% endalert %}

Pour plus d'informations, consultez [`ABKURLDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKURLDelegate.h).

## Cas d'utilisation fréquents

### Création de liens profonds vers les paramètres d'application

iOS peut diriger les utilisateurs de votre application vers sa page dans l'application Réglages d'iOS. Vous pouvez tirer parti de `UIApplicationOpenSettingsURLString` pour créer des liens profonds vers les paramètres depuis les notifications push et les messages in-app.

1. Tout d'abord, assurez-vous que votre application est configurée pour les [liens profonds basés sur des schémas](#deep-links) ou les [liens universels](#universal-links).
2. Choisissez un URI pour le lien profond vers la page **Paramètres** (par exemple, `myapp://settings` ou `https://www.braze.com/settings`).
3. Si vous utilisez des liens profonds basés sur un schéma personnalisé, ajoutez le code suivant à votre méthode `application:openURL:options:` :

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplicationOpenSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% endtabs %}