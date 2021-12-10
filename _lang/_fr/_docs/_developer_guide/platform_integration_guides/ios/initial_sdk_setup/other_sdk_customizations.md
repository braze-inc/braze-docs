---
nav_title: Autres personnalisations du SDK
article_title: Autres personnalisations SDK pour iOS
platform: iOS
description: "Ce document couvre les personnalisations SDK telles que le niveau de log, la collecte IDFA et d'autres personnalisations."
page_order: 3
---

# Autres personnalisations du SDK

## Niveau de la bûche de Braze

Le LogLevel par défaut pour Braze iOS SDK est `8`. Ce niveau supprime la plupart des logs afin qu'aucune information sensible ne soit enregistrée dans une application en production.

Vous pouvez définir le niveau de connexion à `0` pour activer la journalisation verbeuse pour le débogage. Ce niveau est destiné uniquement à être utilisé dans des environnements de développement et ne doit pas être défini dans une application publiée.

Ceci peut être assigné soit à la compilation, soit à l'exécution:

{% tabs local %}
{% tab Compile Time %}

#### Réglage du niveau de log au moment de la compilation

Ajouter un dictionnaire nommé `Braze` à votre fichier `Info.plist`. Dans le dictionnaire `Braze` , ajoutez la sous-entrée String `LogLevel` et définissez la valeur à `0`.

{% alert note %}
Avant Braze iOS SDK v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.
{% endalert %}

Exemple `Info.plist` contenu:

```
<key>Braze</key>
<dict>
    <key>Niveau de log</key>
    <string>0</string>
</dict>
```

{% endtab %}
{% tab Runtime %}

#### Réglage de LogLevel à l'exécution

Ajoute la `ABKLogLevelKey` dans le paramètre `appboyOptions` passé à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définit sa valeur à l'entier `0`.

{% alert note %}
LogLevel ne peut être configuré qu'au moment de l'exécution avec Braze iOS SDK v4.4.0 ou plus récent. Si vous utilisez une version antérieure du SDK, définissez LogLevel au moment de la compilation.
{% endalert %}

{% endtab %}
{% endtabs %}

### Description de LogLevels

| Niveau de log | Libellé                                                                |
| ------------- | ---------------------------------------------------------------------- |
| 0             | Toutes les informations de log seront enregistrées dans la console iOS |
| 8             | Par défaut, enregistrement minimal.                                    |
{: .reset-td-br-1 .reset-td-br-2}

## Collection facultative IDFA

La collection IDFA est optionnelle dans le SDK Braze et désactivée par défaut. La collecte IDFA n'est requise que dans Braze si vous avez l'intention d'utiliser nos [intégrations d'attribution d'installation][21]. Si vous choisissez de stocker votre IDFA, Nous le stockerons gratuitement afin que vous puissiez profiter de ces options immédiatement après la publication sans aucun développement supplémentaire.

Par conséquent, nous vous recommandons de continuer à collecter l'IDFA si vous remplissez l'un des critères suivants :

- Vous attribuez l'installation de l'application à une annonce précédemment diffusée
- Vous attribuez une action dans la demande à une annonce précédemment diffusée

### Transparence de suivi d'applications iOS 14
Dans le futur, Apple aura besoin d’une nouvelle invite d’autorisation pour collecter IDFA. Pour l'instant, la demande d'autorisation IDFA avec `AppTrackingTransparency` n'est pas requise. mais vous devriez être préparé pour une future version d'iOS d'Apple qui nécessitera la participation de l'utilisateur.

Lorsque l'invite `AppTrackingTransparency` est requise, en plus d'implémenter le protocole `ABKIDFADelegate` de Braze, votre application devra demander une autorisation en utilisant le `ATTrackingManager` d'Apple dans le framework de transparence de suivi des applications. Pour plus d'informations, veuillez consulter ce guide [Braze iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa-and-app-tracking-transparency), [Aperçu d'Apple](https://developer.apple.com/app-store/user-privacy-and-data-use/), et [Documentation des développeurs d'Apple](https://developer.apple.com/documentation/apptrackingtransparency). Dans iOS 14, la collecte IDFA nécessitera la construction avec Xcode 12.

L'invite d'autorisation pour la transparence du suivi des applications nécessite également une entrée `Info.plist` pour expliquer votre utilisation de l'identifiant :

```
<key>NSUserTrackingUsageDescription</key>
<string>Pour retarget des publicités et construire un profil global pour mieux vous servir des choses que vous souhaitez.</string>
```

### Implémentation de la collection IDFA

Suivez ces étapes pour implémenter la collection IDFA :

##### Étape 1 : Implémenter ABKIDFADelegate

Créer une classe conforme au protocole [`ABKIDFADelegate`][29].

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import "IDFADelegate. "
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorization;
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

classe IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager. dit().publicitaireIdentifiant. uidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager. rackingAuthorizationStatus == ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### Étape 2 : Définir le délégué lors de l'initialisation de Braze

Dans le dictionnaire `appboyOptions` passé à `startWithApiKey:inApplication:withAppboyOptions:`, définissez la clé `ABKIDFADelegateKey` sur une instance de votre classe conforme à `ABKIDFADelegate`.

## Taille approximative du SDK iOS {#ios-sdk-size}

La taille approximative du fichier du framework iOS SDK est de 30 Mo et la taille approximative du fichier .ipa (ajout au fichier d'application) est comprise entre 1 Mo et 2 Mo.

Braze mesure la taille de notre SDK iOS en observant l'effet du SDK sur `. pa` taille, par [recommandations d'Apple sur le dimensionnement de l'application][31]. Si vous calculez l'ajout de taille du SDK iOS à votre application, nous vous recommandons de suivre les étapes sous ["Obtenir un rapport de taille d'application"][31] pour comparer la différence de taille dans votre `. pa` avant et après l'intégration de Braze iOS SDK. Lorsque vous comparez les tailles de l'App Thinning Size Report, nous vous recommandons également de regarder les tailles des applications pour affiner `. pa` fichiers, en tant qu'universel `. pa` les fichiers seront plus grands que les binaires téléchargés depuis l'App Store et installés sur les appareils de l'utilisateur.

> Si vous intégrez via CocoaPods avec `use_frameworks!`, définissez `Activez Bitcode = NO` dans les paramètres de compilation de la cible pour une taille précise.


[21]: {{site.baseurl}}/partners/advertising_technologies/attribution/adjust/
[29]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h
[31]: https://developer.apple.com/library/content/qa/qa1795/_index.html
[31]: https://developer.apple.com/library/content/qa/qa1795/_index.html
