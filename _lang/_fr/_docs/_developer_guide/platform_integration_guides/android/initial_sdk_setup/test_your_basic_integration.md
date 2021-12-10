---
nav_title: Testez votre intégration de base
article_title: Testez votre intégration de base pour Android/FireOS
page_order: 1
platform:
  - Android
  - Pare-feu
description: "Cet article explique comment tester votre intégration de base pour votre application Android."
---

# Testez votre intégration de base

## Le suivi de la session est en cours

À ce stade, vous devriez avoir un suivi de session fonctionnant dans votre intégration à Braze.  Pour tester ceci, allez à **Aperçu**, sélectionnez votre application dans la liste déroulante du nom de l'application sélectionnée (par défaut, "Toutes les applications"), et mettez **Afficher les données pour** à "Aujourd'hui". Ensuite, ouvrez votre application et actualisez la page - vos mesures principales devraient toutes avoir augmenté de 1.

!\[Sessions fonctionnent\]\[55\]

Vous devriez continuer à tester votre intégration en naviguant dans votre application et en vous assurant qu'une seule session a été enregistrée. Ensuite, l'arrière-plan de l'application pendant au moins 10 secondes et ramenez-la au premier plan à nouveau. Par défaut, une nouvelle session est créée si l'application est au premier plan après plus de 10 secondes, pas au premier plan (arrière-plan ou fermé). Une fois que vous avez fait cela, confirmez qu'une autre session a été enregistrée.

## Suivi de session de débogage
Si le suivi de session se comporte de manière inattendue, activez [Journal détaillé][56] et observez votre application pendant que vous reproduisez les étapes déclenchant la session. Observez les instructions Braze dans le logcat pour détecter où vous avez peut-être manqué l'enregistrement des appels `openSession` et `closeSession` dans vos activités.
[55]: {% image_buster /assets/img_archive/android_sessions.png %}

[56]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#android-verbose-logging