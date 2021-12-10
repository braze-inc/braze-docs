---
nav_title: Aperçu de l'intégration
article_title: Aperçu de l’intégration des flux d’actualités pour Android/FireOS
page_order: 1
platform:
  - Android
  - Pare-feu
description: "Cet article couvre un aperçu de la façon d'intégrer le fil d'actualité dans votre application Android."
channel:
  - fil d'actualité
---

# Vue d'ensemble de l'intégration des fils d'actualité

Dans Android, le flux d'actualités est implémenté en tant que [Fragment][2] qui sont disponibles dans le projet d'interface d'Android Braze. Consultez la documentation de [Google sur Fragments][3] pour plus d'informations sur comment ajouter un fragment à une activité.

> Les Fragments d'interface utilisateur d'Android ne suivent pas automatiquement les analyses de session. Pour vous assurer que les sessions sont suivies correctement, vous devez appeler `IAppboy. penSession()` lorsque votre application est ouverte (en savoir plus sur [le suivi des sessions utilisateur][4]).

La classe `AppboyFeedFragment` actualisera automatiquement et affichera le contenu du flux d'actualités et enregistrera les analyses d'utilisation. Les cartes qui peuvent apparaître dans le fil d'actualité d'un utilisateur sont définies sur le tableau de bord Braze.

La connexion au fil d'actualité à partir d'un message intégré à l'application doit être activée en enregistrant l' `AppboyFeedActivity` dans votre `AndroidManifest.xml`.


[2]: http://developer.android.com/guide/components/fragments.html
[3]: http://developer.android.com/guide/components/fragments.html#Adding "Android Documentation: Fragments"
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
