---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour MacOS
platform: MacOS
page_order: 0
page_type: Référence
description: "Cette page fournit des ressources pour les étapes initiales de configuration du SDK sur macOS."
---

# Configuration initiale du SDK

Depuis la version [3.32.0][1], Braze SDK prend en charge macOS pour les applications utilisant [Mac Catalyst][2] lors de l'intégration via Swift Package Manager. Actuellement, le SDK ne prend pas en charge Mac Catalyst lors de l'utilisation de Cocoapods ou Carthage.

{% alert note %}
Pour construire votre application avec Mac Catalyst, veuillez consulter la documentation d' <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Apple ici</a>.
{% endalert %}

Une fois que votre application prend en charge Catalyst, suivez [ces instructions pour utiliser Swift Package Manager][3] pour importer le Braze SDK dans votre application.

## Fonctionnalités prises en charge

Braze prend en charge les notifications push et les fonctionnalités de localisation lors de l'exécution sur Mac Catalyst. Pour intégrer le push dans votre application Catalyst, suivez les instructions [iOS SDK ici][4]. Pour activer la collecte automatique de la localisation, suivez les instructions de configuration [ici][5].

Veuillez noter que les histoires Push Stories, Rich Push et Geofences ne sont pas supportées sur MacOS.

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]: https://developer.apple.com/mac-catalyst/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
