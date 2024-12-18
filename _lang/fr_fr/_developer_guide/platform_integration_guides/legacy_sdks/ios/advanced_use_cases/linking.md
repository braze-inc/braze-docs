---
nav_title: Création de liens profonds
article_title: Création de liens profonds pour iOS
platform: iOS
page_order: 0
description: "Cet article explique comment implémenter le délégué universel de création de liens profonds pour votre application iOS, ainsi que des exemples sur la manière de créer des liens profonds avec des paramètres d’application ou un fil d’actualités."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Création de liens profonds pour iOS

Pour obtenir des informations de base sur les liens profonds, consultez notre [article sur le Guide de l’utilisateur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking). Si vous souhaitez implémenter des liens profonds pour la première fois dans votre application Braze, veuillez suivre les étapes ci-dessous pour commencer.

{% alert note %}
Cet article comprend des informations sur les fils d’actualité, qui deviennent obsolètes. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

## Étape 1 : Enregistrement d’un schéma

Le schéma personnalisé doit être indiqué dans le fichier `Info.plist`. La structure de navigation est définie par un ensemble de dictionnaires. Chacun de ces dictionnaires contient un tableau de chaînes de caractères.

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
        <string>{YOUR.SCHEME}</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>{YOUR.SCHEME}</string>
        </array>
    </dict>
</array>
```

## Étape 2 : Autoriser la liste blanche du schéma personnalisé (iOS 9+)

À partir d’iOS 9, les applications doivent avoir une liste blanche de schémas personnalisés que l’application est autorisée à ouvrir. Si vous tentez d’appeler des schémas en dehors de cette liste, le système enregistrera une erreur dans les journaux d’appareil et le lien profond ne s’ouvrira pas. Voici un exemple de cette erreur :

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Par exemple, si un message intégré à l'application doit ouvrir l'application Facebook lorsqu'il est tapé, l'application doit avoir le schéma personnalisé Facebook (`fb`) dans la liste autorisée. Sinon, le système rejettera le lien profond. Les liens profonds qui dirigent vers une page ou s’affichent dans votre propre application nécessitent toujours que le schéma personnalisé de votre application soit répertorié dans le `Info.plist` de votre application.

Vous devez ajouter tous les schémas dont l'application a besoin pour créer des liens profonds dans une liste blanche dans le `Info.plist` de votre application avec la clé `LSApplicationQueriesSchemes`. Par exemple :

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>facebook</string>
    <string>twitter</string>
</array>
```

Pour plus d'informations, reportez-vous à la [documentation d'Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) sur la clé `LSApplicationQueriesSchemes`.

## Étape 3 : Implémenter un gestionnaire

Après avoir activé votre application, iOS appellera la méthode [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc). L'argument important est l'objet [NSURL.](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL)

{% tabs %}
{% tab OBJECTIF-C %}

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

Pour utiliser des liens universels, assurez-vous d’avoir ajouté un domaine enregistré aux capacités de votre application et avez téléchargé un fichier `apple-app-site-association`. Puis implémentez la méthode `application:continueUserActivity:restorationHandler:` dans votre `AppDelegate`. Par exemple :

{% tabs %}
{% tab OBJECTIF-C %}

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

Consultez [Apple](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html) pour plus d'informations.

{% alert note %}
L'intégration de lien universel par défaut n'est pas compatible avec les notifications push Braze, les messages intégrés à l'application ou le fil d'actualité. Voir [la personnalisation des liens](#linking-handling-customization) pour gérer les liens universels dans votre application. Nous recommandons plutôt d'utiliser des [liens profonds basés sur des schémas](#step-1-registering-a-scheme) avec des notifications push, des messages intégrés à l'application et le fil d'actualité.
{% endalert%}

## Application Transport Security (ATS)
iOS 9 a introduit une modification de la casse affectant les URL Web intégrées dans les messages in-app, les cartes d’actualités et les notifications push.

### Prérequis ATS
Extrait de la [documentation d'Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14): « App Transport Security est une fonctionnalité qui améliore la sécurité des connexions entre une application et des services Web. » La fonctionnalité consiste en des exigences de connexion par défaut conformes aux meilleures pratiques visant les connexions sécurisées. Les applications peuvent remplacer ce comportement par défaut et désactiver la sécurité du transport. »

L’ATS est appliqué par défaut sur iOS 9+. Il nécessite que toutes les connexions utilisent HTTPS et soient chiffrées à l’aide de TLS 1.2 avec confidentialité de transmission. Pour plus d'informations, reportez-vous à la section [Exigences pour la connexion à l'aide de l'ATS.](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35)  Toutes les images servies par Braze aux terminaux sont gérées par un réseau de diffusion de contenu (« CDN ») qui prend en charge TLS 1.2 et est compatible avec ATS.

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

#### Confirmez que tous les liens sont conformes aux ATS (recommandé)
Votre intégration Braze peut satisfaire les exigences ATS en s’assurant que les liens existants que vous amenez aux utilisateurs (par message in-app et campagnes de notifications push ou cartes d’actualités) répondent aux exigences ATS. Bien qu'il existe des moyens de contourner les restrictions ATS, nous vous recommandons de vous assurer que tous les liens URL sont conformes aux exigences ATS. Compte tenu de l’importance croissante accordée par Apple à la sécurité des applications, il n’est pas garanti que les approches suivantes pour autoriser les exceptions ATS soient prises en charge par Apple.

Un outil SSL peut vous aider à identifier les problèmes de sécurité du serveur Web. Ce [test de serveur SSL](https://www.ssllabs.com/ssltest/index.html) de Qualys, Inc. fournit un élément de ligne spécifiquement pour la conformité à Apple ATS 9 et iOS 9.

#### Désactiver partiellement l’ATS
Vous pouvez autoriser un sous-ensemble de liens avec certains domaines ou programmes à traiter comme des exceptions aux règles ATS. Votre intégration Braze satisfera aux exigences ATS si chaque lien que vous utilisez dans un canal de communication Braze est soit conforme ATS, soit géré par une exception.

Pour ajouter un domaine à une exception de l’ATS, ajoutez l’élément suivant au fichier `Info.plist` de votre application :

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

Reportez-vous à la section [Expédition d'une application avec App Transport Security](http://timekl.com/blog/2015/08/21/shipping-an-app-with-app-transport-security/?utm_campaign=iOS+Dev+Weekly&utm_medium=email&utm_source=iOS_Dev_Weekly_Issue_213) pour plus d'informations sur le débogage des échecs ATS.

## Encodage d’URL

À partir de SDK Braze pour iOS v2.21.0, SDK encode les liens en pourcentage pour créer des `NSURL` valides. Tous les caractères de lien qui ne sont pas autorisés dans une URL correctement formée, tels que les caractères Unicode, seront échappés en pourcentage.

Pour décoder un lien encodé, utilisez la méthode `NSString` [`stringByRemovingPercentEncoding`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/index.html#//apple_ref/occ/instm/NSString/stringByRemovingPercentEncoding). Notez que vous devez également renvoyer `YES` dans le `ABKURLDelegate` et qu’un appel à l’action est nécessaire pour déclencher la gestion de l’URL par l’application. Par exemple :

{% tabs %}
{% tab OBJECTIF-C %}

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

### Personnalisation de WebView par défaut

La classe personnalisable `ABKModalWebViewController` affiche les URL Web ouvertes par le SDK, généralement lorsque l’option « Ouvrir l'URL Web dans l'application » est sélectionnée pour un lien profond Web.

Vous pouvez déclarer une catégorie ou modifier directement la classe `ABKModalWebViewController` pour appliquer la personnalisation à la vue Web. Vérifiez le fichier [.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKModalWebViewController.h) de la classe et le fichier [.m](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/ABKModalWebViewController.m) pour plus de détails.

### Gestion de la personnalisation des liens

Le protocole `ABKURLDelegate` peut être utilisé pour personnaliser la gestion des URL telles que les liens profonds, les URL Web et les liens universels. `appboyOptions` Pour définir le délégué lors de l'initialisation de Braze, passez un objet délégué à l'adresse `ABKURLDelegateKey` dans la section [`startWithApiKey:inApplication:withAppboyOptions:`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Braze appellera ensuite l’implémentation de votre délégué `handleAppboyURL:fromChannel:withExtras:` avant de gérer les URI.

#### Exemple d’intégration : ABKURLDelegate

{% tabs %}
{% tab OBJECTIF-C %}

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

Pour plus d'informations, voir [`ABKURLDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKURLDelegate.h).

## Cas d’utilisation fréquents

### Création de liens profonds vers les paramètres d’application

iOS peut conduire les utilisateurs de votre application vers sa page dans l’application de paramètres iOS. Vous pouvez profiter de `UIApplicationOpenSettingsURLString` pour créer des liens profonds vers les paramètres à partir des notifications push, des messages in-app et du fil d'actualité.

1. Tout d'abord, assurez-vous que votre application est configurée pour des [liens profonds basés sur des schémas](#deep-links) ou des [liens universels](#universal-links).
2. Décidez d'un URI pour le lien profond vers la page **Paramètres** (par exemple, `myapp://settings` ou `https://www.braze.com/settings`).
3. Si vous utilisez des liens profonds basés sur un schéma personnalisé, ajoutez le code suivant à votre méthode `application:openURL:options:` :

{% tabs %}
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

