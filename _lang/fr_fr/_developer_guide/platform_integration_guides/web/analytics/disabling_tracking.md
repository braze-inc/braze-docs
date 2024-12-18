---
nav_title: Désactiver le suivi du SDK Web
article_title: Désactiver le suivi du SDK Web
platform: Web
page_order: 6
page_type: reference
description: "Cet article couvre la désactivation du suivi du SDK Web, y compris la raison, la manière et les implications que cela a pour le Web."

---

# Désactiver le suivi du SDK Web

{% multi_lang_include archive/web-v4-rename.md %}

> Afin de se conformer aux réglementations en matière de confidentialité des données, l’activité de suivi des données sur le SDK Web peut être entièrement arrêtée à l’aide de la méthode [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). 

Cette méthode synchronisera toutes les données enregistrées avant que `disableSDK()` soit appelé et tous les appels ultérieurs vers le SDK Braze pour le Web pour cette page et les charges de page ultérieures seront ignorés. Si vous souhaitez reprendre le recueil des données ultérieurement, vous pouvez utiliser la méthode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) pour reprendre la collecte des données.

Si vous souhaitez fournir aux utilisateurs la possibilité d’arrêter le suivi, nous vous recommandons de créer une page simple avec deux liens ou boutons, un qui appellera `disableSDK()` lorsque vous cliquerez dessus, et l’autre `enableSDK()` pour permettre aux utilisateurs de se réinscrire. Vous pouvez utiliser ces contrôles pour démarrer ou arrêter le suivi via d’autres sous-processeurs de données.

Notez que le SDK Braze n’a pas besoin d’être initialisé pour appeler `disableSDK()`, vous permettant de désactiver le suivi pour les utilisateurs entièrement anonymes. Inversement,`enableSDK()` n’initialise pas le SDK Braze, vous devez donc également appeler `initialize()` ensuite pour activer le suivi.
