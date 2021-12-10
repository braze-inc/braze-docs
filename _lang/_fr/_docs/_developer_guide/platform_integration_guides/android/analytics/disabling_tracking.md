---
nav_title: Désactivation du suivi des SDK Android
article_title: Désactivation de la collecte de données pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 8
description: "Cet article montre comment désactiver la collecte de données pour votre application Android."
---

# Désactivation de la collecte de données pour Android/FireOS

Afin de se conformer à la réglementation en matière de confidentialité des données, l'activité de suivi des données sur le SDK Android peut être arrêtée entièrement en utilisant la méthode [`disableSDK()`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#disableSdk-android.content.Context-). Cette méthode entraînera l'annulation de toutes les connexions réseau, et le Braze SDK ne transmettra aucune donnée aux serveurs de Brase. Si vous souhaitez reprendre la collecte de données à un moment ultérieur, vous pouvez utiliser la méthode [`enableSDK()`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#enableSdk-android.content.Context-) pour reprendre la collecte de données.

De plus, vous pouvez utiliser la méthode [`wipeData()`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#wipeData-android.content.Context-) pour effacer complètement toutes les données côté client stockées sur l'appareil.
