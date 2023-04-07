---
nav_title: Désactiver le suivi du SDK Android
article_title: Désactiver la collecte de données pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Cet article montre comment désactiver la collecte de données pour votre application Android ou FireOS."

---

# Désactiver la collecte de données pour Android et FireOS

Afin de se conformer aux réglementations de confidentialité des données, l’activité de suivi des données sur le SDK Android peut être entièrement arrêtée à l’aide de la méthode [`disableSDK()`][1]. Cette méthode entraînera l’annulation de toutes les connexions réseau, et le SDK Braze ne transmettra aucune donnée aux serveurs de Braze. Si vous souhaitez reprendre le recueil des données ultérieurement, vous pouvez utiliser la méthode [`enableSDK()`][2] plus tard pour reprendre la collecte des données.

En outre, vous pouvez utiliser la méthode [`wipeData()`][3] pour effacer entièrement toutes les données côté client stockées sur le périphérique.

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html
