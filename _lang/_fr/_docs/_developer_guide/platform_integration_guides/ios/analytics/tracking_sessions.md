---
nav_title: Sessions de suivi
article_title: Suivi des sessions pour iOS
platform: iOS
page_order: 0
description: "Cet article de référence montre comment s'abonner aux mises à jour de session pour votre application iOS."
---

# Suivi de session pour iOS

Le Braze SDK rapporte les données de session qui sont utilisées par le tableau de bord Braze pour calculer l'engagement des utilisateurs et d'autres analyses intégrales à la compréhension de vos utilisateurs. Basé sur la sémantique de session ci-dessous, notre SDK génère des points de données "démarrer la session" et "fermer la session" qui tiennent compte de la durée de la session et compte des sessions visibles dans le tableau de bord de Braze.

## Cycle de vie de session

A session is started when you call `[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]`, after which by default sessions start when the `UIApplicationWillEnterForegroundNotification` notification is fired (i.e. the app enters the foreground) and end when the app leaves the foreground (i.e. when the `UIApplicationDidEnterBackgroundNotification` notification is fired or when the app dies).

**Note**: Si vous avez besoin de forcer une nouvelle session, vous pouvez le faire en changeant d'utilisateurs.

## Personnalisation du délai d'attente de la session

À partir de Braze iOS SDK v3.14.1, vous pouvez définir le délai de session en utilisant le fichier Info.plist . Ajoutez le dictionnaire `Braze` à votre fichier Info.plist . À l'intérieur du dictionnaire `Braze` , ajoutez la sous-entrée numéro `SessionTimeout` et définissez la valeur à votre session personnalisée expirée. Notez qu'avant Braze iOS SDK v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Vous pouvez également définir la clé `ABKSessionTimeoutKey` à la valeur entière souhaitée dans votre objet `appboyOptions` passé à [`startWithApiKey`][session_tracking_1].

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Définit le délai d'attente de la session à 60 secondes
[Appboy startWithApiKey:@"VOTRE API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab swift %}

```swift
// Définit le délai d'attente de la session à 60 secondes
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

Si vous avez défini un délai d'expiration de session, la sémantique de session ci-dessus s'étendent tous à ce délai personnalisé.

**Remarque**: La valeur minimale pour `sessionTimeoutInSeconds` est de 1 seconde.

## Tests de suivi de session

Pour détecter des sessions via votre utilisateur, trouvez votre utilisateur sur le tableau de bord et accédez à __App Usage__ sur le profil de l'utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique "essions" augmente quand vous vous y attendez.

!\[test_session\] \[session_tracking_7\]
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml [session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %} [session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

[session_tracking_1]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#afd911d60dfe7e5361afbfb364f5d20f9
