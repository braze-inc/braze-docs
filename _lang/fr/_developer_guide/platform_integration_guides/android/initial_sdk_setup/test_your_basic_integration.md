---
nav_title: Testez votre intégration de base
article_title: Testez votre intégration de base pour Android et FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment tester l’intégration de base pour votre application Android ou FireOS."

---

# Testez votre intégration de base

## Confirmer que le suivi de session fonctionne

À ce stade, vous devriez avoir un suivi de session dans votre intégration Braze. Pour la tester, allez dans **Overview**, sélectionnez votre application dans le menu déroulant de l’application sélectionnée (par défaut « Toutes les applications ») et définissez **Display Data For (Afficher les données pour)** sur « Aujourd’hui ». Ouvrez ensuite votre application et actualisez la page. Vos principales métriques devraient toutes avoir augmenté de 1.

![][55]

Vous devriez continuer à tester votre intégration en naviguant dans votre application et en vous assurant qu’une seule session a été enregistrée. Puis, passez l’application en arrière-plan pendant au moins 10 secondes et remettez-la au premier plan. Par défaut, une nouvelle session est créée si l’application est remise au premier plan après avoir été mise en arrière-plan ou fermée pendant plus de 10 secondes. Une fois que vous l’avez fait, vérifiez qu’une autre session a été enregistrée.

## Déboguer le suivi de session
Si le suivi de la session agit de manière inattendue, activez la [journalisation verbeuse][56] et observez votre application pendant que vous reproduisez les étapes de déclenchement de session. Observez les relevés de Braze dans le logcat pour détecter où vous avez pu omettre de journaliser les appels `openSession` et `closeSession` dans vos activités.

[55]: {% image_buster /assets/img_archive/android_sessions.png %}
[56]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#android-verbose-logging