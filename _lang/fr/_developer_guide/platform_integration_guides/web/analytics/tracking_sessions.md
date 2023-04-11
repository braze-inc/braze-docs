---
nav_title: Suivre des sessions
article_title: Suivre des sessions pour le Web
platform: Web
page_order: 0
description: "Cet article de référence explique comment suivre les sessions pour le Web."

---

# Suivre une session pour le Web

Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analytiques essentielles à la compréhension de vos utilisateurs. Sur la base de la sémantique de session suivante, notre SDK génère des points de données « démarrage de la session » et « fin de la session » qui comptent pour la longueur de session et le nombre de sessions visibles dans le tableau de bord de Braze.

## Cycle de vie de la session

Par défaut, les sessions débutent lorsque `braze.openSession()` est appelé pour la première fois et restent ouvertes jusqu’à ce qu’il y ait eu au moins 30 minutes d’inactivité. Cela signifie que si l’utilisateur quitte le site et y retourne moins de 30 minutes plus tard, la même session continuera. S’ils reviennent après que les 30 minutes ont expiré, un point de données de « fermeture de session » est automatiquement généré pour le temps passé ailleurs et une nouvelle session s’ouvre.

{% alert note %}
Si vous devez forcer une nouvelle session, vous pouvez le faire en changeant d’utilisateur.
{% endalert %}

## Personnaliser la libération sur temporisation de session

Pour personnaliser la libération sur temporisation de session, transmettez l’option `sessionTimeoutInSeconds` à votre fonction [`initialize`][session_tracking_5]. La valeur minimale pour `sessionTimeoutInSeconds` est de 1 seconde.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

Si vous avez défini un délai de libération sur temporisation de session, les sémantiques de session s’étendent à toute cette temporisation personnalisée.

## Tester le suivi de session

Pour détecter les sessions à l’aide de votre utilisateur, recherchez-le sur le tableau de bord et naviguez jusqu’à **Utilisation de l’application** dans le profil utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique de session augmente lorsque vous vous y attendez.

![Un composant de profil utilisateur indiquant le nombre de sessions survenues, quand l’application a été utilisée pour la première fois et quand elle a été utilisée pour la dernière fois.][session_tracking_7]

[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#customizing-braze-on-startup
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
