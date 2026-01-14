---
nav_title: Mise à jour vers iOS 18
article_title: Mise à jour vers iOS 18
page_order: 7.1
platform: 
  - iOS
description: "Cet article couvre les informations sur la version iOS 18 pour vous aider à mettre à jour votre SDK de façon fluide."
---

# Mise à jour vers iOS 18

> Vous souhaitez savoir comment Braze se prépare à la prochaine version d’iOS ? Cet article résume nos informations sur la version 18 d'iOS pour vous aider à créer une expérience fluide pour vous et pour vos utilisateurs.

Le [WWDC](https://developer.apple.com/wwdc24/) d'Apple a eu lieu du 9 au 11 juin 2024. Découvrez leurs annonces dans notre [article de blog](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18), ou poursuivez votre lecture pour savoir comment vous pouvez tirer parti d'iOS 18 avec Braze.

## Changements dans iOS 18

### Activités en ligne/instantanées sur l'Apple Watch

Les [activités en ligne/instantanées](https://www.braze.com/docs/developer_guide/push_notifications/live_notifications/?sdktab=swift) seront prises en charge sur watchOS 11. Aucune configuration supplémentaire n'est nécessaire. Apple offre toutefois la possibilité de personnaliser l'interface de la montre.

### Apple Vision Pro

La Vision Pro est désormais disponible en Chine, au Japon, à Singapour, en Australie, au Canada, en France, en Allemagne et au Royaume-Uni. Consultez notre blog pour voir comment [Braze prend en charge visionOS](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### Notifications de l'iPhone sur macOS

La nouvelle fonctionnalité de [mise en miroir de l'iPhone](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) d'Apple permet aux utilisateurs de recevoir les notifications de l'iPhone sur leurs appareils macOS. Gardez à l'esprit que certains types de médias, tels que les images Push Story et les GIF, ne sont pas pris en charge, car ils ne peuvent pas être présentés sous forme de notification macOS.

### Apple Intelligence

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) est désormais disponible pour les appareils fonctionnant sous iOS 18.1 et les versions ultérieures.

En tant qu'utilisateur de Braze, la nouvelle fonctionnalité la plus importante à connaître est celle des [résumés de notification](https://support.apple.com/en-us/108781), qui utilise le traitement sur l'appareil pour regrouper et générer automatiquement des résumés de texte pour les notifications push connexes envoyées à partir d'une même app. Les utilisateurs finaux peuvent appuyer sur pour développer un résumé et voir chaque notification push telle qu'elle a été envoyée à l'origine.

En raison de la manière dont ces résumés sont générés, vous n'aurez aucun contrôle sur leur comportement spécifique ou sur le texte généré. Toutefois, cela n'aura pas d'incidence sur les fonctionnalités d'analyse/analytique (telles que le suivi des clics).

![Capture d'écran d'un résumé de l'aperçu d'une notification push.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})
