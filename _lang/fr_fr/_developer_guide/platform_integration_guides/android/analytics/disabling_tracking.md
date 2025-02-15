---
nav_title: Désactiver le suivi du SDK
article_title: Désactiver la collecte de données pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Cet article montre comment désactiver la collecte de données pour votre application Android ou FireOS."

---

# Désactiver le suivi du SDK

> Cet article montre comment désactiver la collecte de données pour votre application Android ou FireOS.

Afin de se conformer aux réglementations en matière de confidentialité des données, l’activité de suivi des données sur le SDK Android peut être entièrement arrêtée à l’aide de la méthode [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Cette méthode entraînera l’annulation de toutes les connexions réseau, et le SDK Braze ne transmettra aucune donnée aux serveurs de Braze. Si vous souhaitez reprendre le recueil de données ultérieurement, vous pouvez utiliser la méthode [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) plus tard pour reprendre la collecte des données.

En outre, vous pouvez utiliser la méthode [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) pour effacer entièrement toutes les données côté client stockées sur l’appareil.

