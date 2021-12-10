---
nav_title: Sessions de suivi
article_title: Suivi des sessions pour Windows Universal
platform: Univers Windows
page_order: 0
description: "Cet article de référence traite de la façon de suivre les sessions sur la plate-forme Windows Universelle."
---

# Analyses

## Suivi de session

Le Braze SDK rapporte les données de session qui sont utilisées par le tableau de bord Braze pour calculer l'engagement des utilisateurs et d'autres analyses intégrales à la compréhension de vos utilisateurs. Basé sur la sémantique de session ci-dessous, notre SDK génère des points de données "démarrer la session" et "fermer la session" qui tiennent compte de la durée de la session et compte des sessions visibles dans le tableau de bord de Braze.

### Cycle de vie de session

Notre session de journaux d’intégration Windows s’ouvre lorsque l’application est lancée et que la session de log se ferme lorsque l’application est fermée.

**Note**: Si vous avez besoin de forcer une nouvelle session, vous pouvez le faire en changeant d'utilisateurs.

**Remarque**: La valeur minimale pour `sessionTimeoutInSeconds` est de 1 seconde.

### Tests de suivi de session

Pour détecter les sessions via votre utilisateur, trouvez votre utilisateur sur le tableau de bord et accédez à "Utilisation de l'application" sur le profil de l'utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique "essions" augmente quand vous vous y attendez.

!\[test_session\] \[session_tracking_7\]
[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#customizing-braze-on-startup [session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml [session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %} [session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

