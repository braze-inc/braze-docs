---
nav_title: Désactivation du suivi Web SDK
article_title: Désactivation du suivi Web SDK
platform: Web
page_order: 6
page_type: Référence
description: "Cet article couvre la désactivation du suivi du Web SDK, y compris pourquoi, comment et les implications de cette désactivation."
---

# Désactiver le suivi web SDK

Pour se conformer aux règles de confidentialité des données l'activité de suivi des données sur le SDK Web peut être entièrement arrêtée en utilisant la méthode [`stopWebTracking()`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.stopWebTracking). Cette méthode va synchroniser les données enregistrées avant que `stopWebTracking()` ait été appelé, et fera que tous les appels ultérieurs au SDK Braze Web pour cette page et les prochaines pages seront ignorés. Si vous souhaitez reprendre la collecte de données à un moment ultérieur, vous pouvez utiliser la méthode [`resumeWebTracking()`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.resumeWebTracking) pour reprendre la collecte de données.

Si vous souhaitez offrir aux utilisateurs la possibilité de cesser de suivre, nous vous recommandons de créer une page simple avec deux liens ou boutons, un qui appelle `stopWebTracking()` lorsqu'il est cliqué, et un autre qui appelle `resumeWebTracking()` pour permettre aux utilisateurs de se réinscrire. Vous pouvez également utiliser ces contrôles pour démarrer ou arrêter le suivi via d'autres sous-processeurs de données.

Notez que le Braze SDK ne doit pas __ être initialisé pour appeler `stopWebTracking()`, vous permettant de désactiver le suivi pour les utilisateurs totalement anonymes. Inversement,`resumeWebTracking()` n'initialise pas le Braze SDK, vous devez donc appeler `initialize()` par la suite pour activer le suivi.
