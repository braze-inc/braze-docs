---
nav_title: Autres personnalisations du SDK
article_title: Autres personnalisations du SDK pour iOS
platform: iOS
description: "Ce document couvre les personnalisations SDK telles que Log Level, IDFA Collection et d’autres personnalisations."
page_order: 3

---

{% multi_lang_include deprecations/objective-c.md %}

# Autres personnalisations du SDK

## Niveau de journalisation de Braze

Le niveau de journalisation par défaut du SDK Braze pour iOS est minimal, ou `8` dans le tableau suivant. Ce niveau supprime la majeure partie de la journalisation afin qu’aucune information sensible ne soit consignée dans une application publiée en production.

Consultez la liste suivante des niveaux de journalisation disponibles :

### Niveaux de journalisation

| Niveau    | Description |
|----------|-------------|
| 0        | Prolixe. Toutes les informations du journal seront consignées sur la console iOS.  |
| 1        | Débogage. Les informations de débogage et de journalisation plus importantes seront consignées dans la console iOS.  |
| 2        | Avertissement. Les informations d’avertissement et de journal plus importantes seront consignées dans la console iOS.  |
| 4        | Erreur. Les informations d’erreur et de journal plus importantes seront consignées dans la console iOS.  |
| 8        | Minimales. Les informations minimales seront enregistrées dans la console iOS. Les paramètres par défaut du SDK. |
{: .reset-td-br-1 .reset-td-br-2}

### Consignation prolixe

Vous pouvez configurer le niveau de journalisation pour toutes les valeurs disponibles. Cependant, définir le niveau de journalisation sur prolixe, ou `0`, peut être très utile pour le débogage des problèmes avec votre intégration. Ce niveau est uniquement destiné aux environnements de développement et ne doit pas être activé dans une application publiée.

### Réglage du niveau de journalisation

Le niveau de journalisation peut être attribué soit au moment de la compilation, soit au moment de l’exécution :

{% tabs local %}
{% tab Compile Time %}

Ajouter un dictionnaire nommé `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la sous-entrée chaîne de caractères `LogLevel` et réglez la valeur sur `0`. 

{% alert note %}
Avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.
{% endalert %} 

Exemple de contenu `Info.plist` :

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Runtime %}

Ajouter la `ABKLogLevelKey` dans le `appboyOptions` paramètre transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définir sa valeur dans l’entier `0`.

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Le niveau de journalisation ne peut être défini qu’au moment de l’exécution avec le SDK Braze pour iOS v4.4.0 ou plus récent. Si vous utilisez une version antérieure du SDK, préférez plutôt le niveau de journalisation au moment de la compilation.
{% endalert %} 

{% endtab %}
{% endtabs %}

## Collecte IDFV en option - Swift

Dans les versions antérieures du SDK Swift iOS de Braze, le champ IDFV (identifiant du vendeur) était renseigné automatiquement à partir de l’ID de l’appareil de l’utilisateur. 

À partir du SDK Swift v5.7.0, le champ IDFV peut être désactivé facultativement et, à la place, Braze générera un UUID aléatoire en tant qu’ID de l’appareil. Pour plus d’informations, consultez [Recueillir les IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/swift_idfv/).

## Collecte IDFA facultative

La collecte IDFA est facultative dans le SDK Braze et désactivée par défaut. La collecte IDFA n’est requise dans Braze que si vous avez l’intention d’utiliser nos [intégrations d’attribution d’installation][21]. Si vous choisissez de stocker votre IDFA, nous le stockerons gratuitement, afin que vous puissiez profiter de ces options dès sa sortie sans travail de développement supplémentaire.

Par conséquent, nous vous recommandons de continuer à collecter l’IDFA si vous remplissez l’un des critères suivants :

- Vous attribuez l’installation de l’application à une publicité déjà diffusée
- Vous attribuez une action dans l’application à une publicité déjà diffusée

### iOS 14.5 AppTrackingTransparency

Apple demande aux utilisateurs de s’inscrire via une invite d’autorisation pour collecter l’IDFA.

Pour collecter l’IDFA, en plus de l’implémentation du protocole `ABKIDFADelegate` de Braze, votre demande devra demander une autorisation de l’utilisateur à l’aide de `ATTrackingManager` d’Apple dans l’infrastructure de transparence du suivi des applications. Se référer à l’[article de confidentialité de l’utilisateur](https://developer.apple.com/app-store/user-privacy-and-data-use/) d’Apple pour plus d’informations.

L’invite d’autorisation de transparence du suivi des applications nécessite une entrée `Info.plist` pour expliquer votre utilisation de l’identifiant :

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### Implémentation de la collection IDFA

Suivez ces étapes pour implémenter la collection IDFA :

##### Étape 1 : Implémenter ABKIDFADelegate

Créez une classe conforme au protocole [`ABKIDFADelegate`][29] :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### Étape 2 : Définir le délégué pendant l’initialisation du Braze

Dans le dictionnaire `appboyOptions` transmis à `startWithApiKey:inApplication:withAppboyOptions:`, définissez la clé `ABKIDFADelegateKey` à une instance de votre classe de conformité `ABKIDFADelegate`.

## Taille approximative du SDK {#ios-sdk-size}

La taille du fichier de l’infrastructure de SDK d’iOS est d’environ 30 Mo, et la taille approximative de .ipa (ajout à un fichier d’application) est comprise entre 1 Mo et 2 Mo.

Braze mesure la taille de notre SDK iOS en observant l’effet du SDK sur la taille `.ipa`, en fonction des [recommandations sur la taille des applications][31] d’Apple. Si vous calculez l’ajout de taille du SDK iOS à votre application, nous vous recommandons de suivre [Obtenir un rapport sur la taille de l’application][31] pour comparer la différence de taille entre votre `.ipa` avant et après l’intégration du SDK Braze pour iOS. Lorsque vous comparez les tailles à partir du rapport de taille d’amincissement des applications, nous vous recommandons également de regarder les tailles d’applications pour les fichiers `.ipa` légers, comme les fichiers `.ipa` universels seront plus volumineux que les binaires téléchargés sur l’App Store et installés sur les appareils d’utilisateur.

{% alert note %}
Si vous intégrez via CocoaPods avec `use_frameworks!`, paramétrez les paramètres de construction de la cible sur `Enable Bitcode = NO` pour obtenir des tailles précises.
{% endalert %}

[21]: {{site.baseurl}}/partners/advertising_technologies/attribution/adjust/
[29]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h
[31]: https://developer.apple.com/library/content/qa/qa1795/_index.html
