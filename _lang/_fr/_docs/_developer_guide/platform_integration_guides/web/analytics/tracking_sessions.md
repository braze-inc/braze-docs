---
nav_title: Sessions de suivi
article_title: Suivi des sessions pour le Web
platform: Web
page_order: 0
description: "Cet article de référence traite de la façon de suivre les sessions sur le Web."
---

# Suivi de session pour le web

Le Braze SDK rapporte les données de session qui sont utilisées par le tableau de bord Braze pour calculer l'engagement des utilisateurs et d'autres analyses intégrales à la compréhension de vos utilisateurs. Basé sur la sémantique de session ci-dessous, notre SDK génère des points de données "démarrer la session" et "fermer la session" qui tiennent compte de la durée de la session et compte des sessions visibles dans le tableau de bord de Braze.

## Cycle de vie de session

Par défaut, les sessions commencent lorsque `appboy.openSession()` est d'abord appelé et reste ouvert jusqu'à ce qu'il y ait au moins 30 minutes d'inactivité. Cela signifie que si l'utilisateur quitte le site et retourne moins de 30 minutes plus tard, la même session sera poursuivie. S'ils reviennent après que les 30 minutes ont expiré, un point de données « session fermée » est généré automatiquement pour l'heure à laquelle ils ont navigué, et une nouvelle session s'ouvre.

**Note**: Si vous avez besoin de forcer une nouvelle session, vous pouvez le faire en changeant d'utilisateurs.

## Personnalisation du délai d'attente de la session

Pour personnaliser le timeout de la session, passez l'option `sessionTimeoutInSeconds` à votre fonction [`initialiser`][session_tracking_5].

```js
// Définit le délai de session à 15 minutes au lieu de la valeur par défaut 30
appboy.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```

Si vous avez défini un délai d'expiration de session, la sémantique de session ci-dessus s'étendent tous à ce délai personnalisé.

**Remarque**: La valeur minimale pour `sessionTimeoutInSeconds` est de 1 seconde.

### Tests de suivi de session

Pour détecter les sessions via votre utilisateur, trouvez votre utilisateur sur le tableau de bord et accédez à "Utilisation de l'application" sur le profil de l'utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique "essions" augmente quand vous vous y attendez.

!\[test_session\] \[session_tracking_7\]
[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#customizing-braze-on-startup [session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml [session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %} [session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize

