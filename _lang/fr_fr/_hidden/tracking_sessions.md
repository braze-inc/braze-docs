---
nav_title: Suivre des sessions
article_title: Suivi des sessions pour Windows Universal
platform: Windows Universal
page_order: 0
description: "Cet article de référence explique comment suivre des sessions sur la plateforme Windows Universal."
hidden: true
---

# Analyse
{% multi_lang_include archive/windows_deprecation.md %}

## Suivi d’une session

Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analyses essentielles à la compréhension de vos utilisateurs. Sur la base de la sémantique de session suivante, notre SDK génère des points de données « démarrage de la session » et « fin de la session » qui comptent pour la longueur de session et le nombre de sessions visibles dans le tableau de bord de Braze.

### Cycle de vie de la session

Notre intégration Windows enregistre l’ouverture de session lorsque l’application est lancée et sa fermeture lorsque l’application est fermée. La valeur minimale pour `sessionTimeoutInSeconds` est de 1 seconde. Si vous devez forcer une nouvelle session, vous pouvez le faire en changeant d’utilisateur.

### Tester le suivi de session

Pour détecter les sessions à l’aide de votre utilisateur, recherchez-le sur le tableau de bord et naviguez jusqu’à « Utilisation de l’application » dans le profil utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique « session » augmente lorsque vous vous y attendez.

![Un profil utilisateur montrant l'utilisation d'une application sous forme de 25 sessions, dont la dernière utilisation remonte à deux heures et la première à vingt jours][session_tracking_7]

[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview#customizing-braze-on-startup
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

