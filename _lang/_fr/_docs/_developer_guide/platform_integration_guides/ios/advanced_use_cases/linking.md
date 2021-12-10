---
nav_title: Liens profonds
article_title: Liens profonds pour iOS
platform: iOS
page_order: 0
description: "Cet article couvre comment implémenter le délégué universel de liaison profonde pour votre application iOS, ainsi que des exemples sur la façon de créer un lien profond vers les paramètres de l'application ou un fil d'actualité."
---

# Liaison en cours

## Liens profonds

Pour plus d'informations sur ce qu'est un lien profond, veuillez consulter notre [FAQ Section][4]. Si vous cherchez à implémenter des liens profonds pour la première fois, veuillez consulter la documentation ci-dessous.

### Étape 1 : Enregistrement d'un schéma

Le schéma personnalisé doit être indiqué dans le fichier `Info.plist`. La structure de navigation est définie par un tableau de dictionnaires. Chacun de ces dictionnaires contient un tableau de chaînes.

En utilisant Xcode, éditez votre fichier `Info.plist`:

1. Ajouter une nouvelle clé `types d'URL`. Xcode fera automatiquement de cela un tableau contenant un dictionnaire appelé `Élément 0`.
2. Dans le `Point 0`, ajoutez une clé `identifiant d'URL,`. Définissez la valeur à votre schéma personnalisé.
3. Dans l'élément `0`, ajoutez une clé `Schémas d'URL`. Ce sera automatiquement un tableau contenant une chaîne appelée `Item 0`.
4. Définissez `Schémas d'URL` >> `Élément 0` à votre schéma personnalisé.

Alternativement, si vous souhaitez éditer votre fichier `info.plist` directement, vous pouvez suivre la spécification ci-dessous:

```html
<key>Types CFBundleURL</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>VOUR. CHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>VOUS. CHEME</string>
        </array>
    </dict>
</array>
```

### Étape 2 : Ajout d'une liste blanche (iOS 9+)

À partir d'iOS 9, les applications doivent avoir une liste blanche de schémas personnalisés que l'application est autorisée à ouvrir. Tenter d'appeler des schémas en dehors de cette liste entraînera le système d'enregistrer une erreur dans les journaux de l'appareil et le lien profond ne s'ouvrira pas. Un exemple de cette erreur ressemblera à :

```
<Warning>: -canOpenURL: échec pour l'URL: « yourapp://deeplink» – erreur: « Cette application n'est pas autorisée à demander le schéma de votre application»
```

Par exemple, si un message dans l'application doit ouvrir l'application Facebook lorsqu'elle est activée, l'application doit avoir le schéma personnalisé Facebook (`fb`) dans la liste blanche. Dans le cas contraire, le système rejettera le lien profond. Les liens profonds qui dirigent vers une page ou une vue dans votre propre application nécessitent que le schéma personnalisé de votre application soit listé dans les infos `de votre application. liste`.

Vous devriez ajouter tous les schémas vers lesquels l'application a besoin d'un lien profond dans une liste blanche dans les infos `de votre application. liste` avec la clé `LSApplicationQueriesSchemes`. Par exemple :

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>facebook</string>
    <string>twitter</string>
</array>
```

Pour plus d'informations, reportez-vous à la [documentation d'Apple][12] sur la clé `LSApplicationQueriesSchemes`.

### Étape 3 : Implémenter un gestionnaire

Après avoir activé votre application, iOS appellera la méthode [`application:openURL:options:`][13]. L'argument important est l'objet [NSURL][2].

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path = [url path];
  NSString *query = [url query];
  // Ici tu devrais insérer du code pour faire une action basée sur le chemin et la requête.
  retourner OUI;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url. ath
  let requête = url. uery
  // Ici tu devrais insérer du code pour faire une action basée sur le chemin et la requête.
  retourner le vrai
}
```

{% endtab %}
{% endtabs %}

!\[Ouvrir le flux d'actualités\]\[10\]

# Liens universels

Pour utiliser les liens universels, assurez-vous que vous avez ajouté un domaine enregistré aux capacités de votre application et que vous avez téléchargé un fichier `apple-site-association`. Implémentez ensuite la méthode `application:continueUserActivity:restorationHandler:` dans votre AppDelegate. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application
continueUserActivity:(NSUserActivity *)userActivity
  restorationHandler:(void (^)(NSArray *restorableObjects)))restorationHandler {
  if ([userActivity. ctivityType isEqualToString:NSUserActivityTypeBrowsingWeb]) {
    NSURL *url = userActivity. ebpageURL;
    // Gérer url
  }
  retourner OUI;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  if (userActivity. ctivityType == NSUserActivityTypeBrowsingWeb) {
    let url = userActivity. ebpageURL
    // Gérer url
  }
  retourner vrai
}
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, reportez-vous à la documentation [Universal Links d'Apple][11].**

> L'intégration par défaut de Universal Link n'est pas compatible avec les notifications push de Braze, les messages dans l'application ou le fil d'actualité. Consultez notre documentation de [Linking Customization][26] pour gérer les liens universels dans votre application. Alternativement, nous vous recommandons d'utiliser [des liens profonds basés sur le schéma][25] avec des notifications push, des messages dans l'application et le flux d'actualités.

## Sécurité du transport des applications (ATS)
iOS 9 a introduit un changement ininterrompu affectant les URLs Web intégrées dans les messages de l'application, les cartes de flux d'actualités et les notifications push.

### Exigences ATS
À partir de la documentation [Apple][16]: « App Transport Security est une fonctionnalité qui améliore la sécurité des connexions entre une application et des services Web. La fonction consiste en des exigences de connexion par défaut qui sont conformes aux meilleures pratiques pour les connexions sécurisées. Les applications peuvent surcharger ce comportement par défaut et désactiver la sécurité du transport."

ATS est appliqué par défaut sur iOS 9+. Il faut que toutes les connexions utilisent HTTPS et soient chiffrées en utilisant TLS 1.2 avec le secret avant. Pour les spécifications d'Apple, reportez-vous à "[Exigences pour la connexion avec ATS][14]." Toutes les images servies par Braze vers les périphériques finaux sont gérées par un réseau de distribution de contenu ("CDN") qui prend en charge TLS 1.2 et est compatible avec ATS.

Sauf si elles sont spécifiées comme exceptions dans les infos `de votre application. liste`, les connexions qui ne suivent pas ces exigences échoueront avec des erreurs qui ressemblent à ceci :

```
CFNetwork SSLHandshake a échoué (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "Une erreur SSL s'est produite et une connexion sécurisée au serveur ne peut pas être faite."
```

```
NSURLSession/NSURLConnection HTTP chargement échoué (kCFStreamErrorDomainSSL, -9802)
```

La conformité ATS est appliquée pour les liens ouverts dans l'application mobile (gestion par défaut des liens cliqués) et ne s'applique pas aux sites ouverts à l'extérieur via un navigateur Web.

### Manipulation des exigences ATS

Vous pouvez gérer ATS de l'une des trois façons suivantes :

#### S'assurer que tous les liens sont conformes à l'ATS (recommandé)
Votre intégration à Braze peut satisfaire aux exigences ATS plus simplement en veillant à ce que tous les liens existants vers lesquels vous conduisez les utilisateurs (par le biais de campagnes de message/push in-app ou de cartes de News Feed ) satisfassent aux exigences ATS. Bien qu'il existe des moyens de contourner les restrictions ATS, les meilleures pratiques de Braze sont de s'assurer que toutes les URL liées sont conformes à l'ATS. Étant donné l'importance croissante qu'accorde Apple à la sécurité des applications, les approches listées ci-dessous pour permettre aux exceptions ATS ne sont pas garanties d'être prises en charge par Apple d'aller de l'avant.

Un outil SSL peut vous aider à identifier les problèmes de sécurité du serveur web. Ce [Test serveur SSL][15] de Qualys, Inc. fournit un élément de ligne spécifique pour la conformité Apple ATS 9 / iOS 9.

#### Désactiver partiellement ATS
Vous pouvez autoriser un sous-ensemble de liens avec certains domaines ou schémas à être traités comme des exceptions aux règles ATS. Votre intégration à Braze répondra aux exigences ATS si chaque lien que vous utilisez dans un canal de messagerie Braze est conforme à la norme ATS ou géré par une exception.

Pour ajouter un domaine à l'exception de l'ATS, ajoutez ce qui suit au fichier `Info.plist` de votre application :

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>exemple. om</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

Pour plus d'informations, veuillez vous référer à la documentation d'Apple sur [App Transport Security keys][19].

#### Désactiver ATS entièrement

Vous pouvez désactiver ATS entièrement. Veuillez noter que ce n'est pas une pratique recommandée, à la fois en raison de la perte de protections de sécurité et de la compatibilité future avec iOS. Pour désactiver ATS, insérez ce qui suit dans le fichier `Info.plist` de votre application :

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

Pour plus d'informations sur la façon de déboguer les échecs ATS, Veuillez vous référer au blog de Tim Ekl «[Expédier une application avec App Transport Security][17]».

## Encodage d'URL

Depuis Braze iOS SDK v2.21.0, le SDK contient des liens pour créer des `NSURL`valides. Tous les caractères de lien qui ne sont pas autorisés dans une URL correctement formée, comme les caractères Unicode, seront protégés par pourcentage.

Pour décoder un lien encodé, utilisez la méthode `NSString` [`stringByRemovingPercentEncoding`][8]. Veuillez noter que vous devez également retourner `OUI` dans le `ABKURLDelegate` et qu'un appel à l'action est nécessaire pour déclencher la gestion de l'URL par l'application. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  // Gérer urlString
  retourner OUES;
}
```

{% endtab %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, url ouverte: URL, options: [UIApplication. penURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url. bsoluteString.removingPercentEncoding
    // Gérer urlString
    retourner true
}
```

{% endtab %}
{% endtabs %}

## Personnalisation {#linking-customization}

### Personnalisation WebView par défaut

La classe `ABKModalWebViewController` open-source est utilisée pour afficher les URL web ouvertes par le SDK, généralement lorsque "Open Web URL Inside App" est sélectionné pour un lien web profond.

Vous pouvez déclarer une catégorie pour ou directement modifier la classe `ABKModalWebViewController` pour appliquer la personnalisation à la vue web. Veuillez vérifier le fichier [.h de la classe][6] et [.m][5] pour plus de détails.

### Personnalisation de la gestion des liens

Le protocole `ABKURLDelegate` peut être utilisé pour personnaliser la gestion des URL telles que les liens profonds, les URL web et les liens universels. Pour définir le délégué lors de l'initialisation de Braze, passer un objet délégué à la `ABKURLDelegateKey` dans les `appboyOptions` de [`startWithApiKey:inApplication:withAppboyOptions :`][22]. Braze appellera alors l'implémentation de `handleAppboyURL:fromChannel:withExtras:` avant de gérer des URIs.

#### Exemple d'intégration : ABKURLDelegate

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)handleAppboyURL:(NSURL *)url from Channel:(ABKChannel)channel withExtras:(NSDictionary *)extras {
  if ([[url.host lowercaseString] isEqualToString:@"MY-DOMAIN. om"]) {
    // Lien de gestion personnalisé ici
    retourner OUI;
  }
  // Laisser Braze gérer les liens sinon
  retourner NON;
}
```

{% endtab %}
{% tab swift %}

```swift
func handleAppboyURL(_ url: URL?, from channel: ABKChannel, withExtras extras: [AnyHashable : Any]?) -> Bool {
  if (url.host == "MY-DOMAIN. om") {
    // Lien de gestion personnalisé ici
    retourne true;
  }
  // Laisser Braze gérer les liens sinon
  retourner false;
}
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, voir [`ABKURLDelegate.h`][23].

## Cas d'utilisation fréquents

### Liaison profonde vers les paramètres de l'application

iOS peut emmener les utilisateurs de votre application dans sa page dans l'application Réglages iOS. Vous pouvez profiter de `UIApplicationOpenSettingsURLString` pour lier profondément les utilisateurs aux paramètres de Braze notifications push, des messages intégrés à l'application et du fil d'actualité.

1. Premièrement, assurez-vous que votre application est configurée pour les [liens profonds basés sur le schéma][25] ou [liens universels][27].
2. Décidez d'une URI pour un lien profond vers la page des paramètres (par exemple, `myapp://settings` ou `https://www.braze.com/settings`).
3. Si vous utilisez des liens profonds basés sur un schéma personnalisé, ajoutez le code suivant à votre `application:openURL:options:` méthode:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
  NSString *path = [url path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
  retourner OUI ;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url. ath
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplicationOpenSettingsURLString)!)
  }
  retourner vrai
}
```

{% endtab %}
{% endtabs %}
[10]: {% image_buster /assets/img_archive/deep_link.png %}

[2]: https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/ABKModalWebViewController.m
[6]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKModalWebViewController.h
[8]: https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/index.html#//apple_ref/occ/instm/NSString/stringByRemovingPercentEncoding
[11]: https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html
[12]: https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14
[13]: https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc
[14]: https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35
[15]: https://www.ssllabs.com/ssltest/index.html
[16]: https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14
[17]: http://timekl.com/blog/2015/08/21/shipping-an-app-with-app-transport-security/?utm_campaign=iOS+Dev+Weekly&utm_medium=email&utm_source=iOS_Dev_Weekly_Issue_213
[19]: https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33
[22]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24
[23]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKURLDelegate.h
[25]: #deep-links
[25]: #deep-links
[26]: #linking-customization
[27]: #universal-links
