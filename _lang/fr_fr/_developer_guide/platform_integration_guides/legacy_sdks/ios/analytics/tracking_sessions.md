---
nav_title: Suivre des sessions
article_title: Suivre des sessions pour iOS
platform: iOS
page_order: 0
description: "Cet article de référence montre comment vous abonner aux mises à jour de session pour votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Suivre une session pour iOS

Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analyses essentielles à une meilleure connaissance de vos utilisateurs. Notre SDK génère des points de données « démarrage de session » et « fin de session » qui comptent pour la longueur de session et le comptage de sessions visibles dans le tableau de bord de Braze en fonction des sémantiques de session suivantes.

## Cycle de vie de la session

Une session est lancée lorsque vous appelez `[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]`, après quoi les sessions commencent par défaut lorsque la notification `UIApplicationWillEnterForegroundNotification` est déclenchée (par exemple, lorsque l'application entre au premier plan) et se terminent lorsque l'application quitte le premier plan (par exemple, lorsque la notification `UIApplicationDidEnterBackgroundNotification` est déclenchée ou lorsque l'application meurt).

{% alert note %}
Si vous devez forcer une nouvelle session, vous pouvez le faire en changeant d’utilisateur.
{% endalert %}

## Personnaliser la libération sur temporisation de session

À partir de la version 3.14.1 du SDK iOS de Braze, vous pouvez définir le délai d'expiration de la session à l'aide du fichier Info.plist. Ajouter le dictionnaire `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la de sous-entrée numérique `SessionTimeout` et définissez la valeur sur votre délai d’expiration de session personnalisé. Notez qu’avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Vous pouvez également attribuer à la clé `ABKSessionTimeoutKey` la valeur entière souhaitée dans votre objet `appboyOptions` transmis à [`startWithApiKey`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#afd911d60dfe7e5361afbfb364f5d20f9).

{% tabs %}
{% tab OBJECTIF-C %}

```objc
// Sets the session timeout to 60 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab swift %}

```swift
// Sets the session timeout to 60 seconds
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

Si vous avez défini un délai de libération sur temporisation de session, les sémantiques de session s’étendent à toute cette temporisation personnalisée.

{% alert note %}
La valeur minimale pour `sessionTimeoutInSeconds` est de 1 seconde. La valeur par défaut est 10 secondes.
{% endalert %}

## Tester le suivi de session

Pour détecter les sessions via votre utilisateur, trouvez votre utilisateur sur le tableau de bord et naviguez vers **App Usage** sur le profil utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique « session » augmente lorsque vous vous y attendez.

![La section d'utilisation des applications d'un profil utilisateur indiquant le nombre de sessions, la date de la dernière utilisation et la date de la première utilisation.]({% image_buster /assets/img_archive/test_session.png %})

