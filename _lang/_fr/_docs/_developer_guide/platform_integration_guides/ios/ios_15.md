---
nav_title: Guide de mise à jour iOS 15
article_title: Guide de mise à jour du SDK iOS 15
page_order: 7
platform: iOS
description: "Cet article de référence couvre les nouvelles mises à jour iOS 15, les mises à jour de SDK requises et les nouvelles fonctionnalités."
---

# Guide de mise à jour du SDK iOS 15

Ce guide décrit les changements introduits dans iOS 15 (WWDC21) et les étapes de mise à jour requises pour votre intégration à Braze iOS SDK.

> Pour une liste complète des nouvelles mises à jour iOS 15, voir [iOS 15 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) d'Apple.


## Modification de la transparence des navigations de l'interface utilisateur

Dans le cadre de nos tests annuels des bêta-iOS, nous avons identifié un changement apporté par Apple qui fait apparaître certaines barres de navigation de l'interface utilisateur transparentes au lieu d'opaque. Ceci sera visible sur iOS 15 lors de l'utilisation de l'interface par défaut de Braze pour les Cartes de Contenu, Flux d'Actualités, ou lorsque des liens web profonds sont ouverts dans votre application au lieu de dans une application de navigateur séparée.

Pour éviter ce changement visuel dans iOS 15, nous vous recommandons fortement de passer à la version [Braze iOS SDK v4.3.][1] dès que possible, avant que les utilisateurs commencent à mettre à jour leur téléphone vers le nouveau système d'exploitation iOS 15.

## Nouveaux paramètres de notification {#notification-settings}

iOS 15 a introduit de nouvelles fonctionnalités de notification pour aider les utilisateurs à rester concentrés et éviter des interruptions fréquentes tout au long de la journée. Nous sommes heureux d'offrir un support pour ces nouvelles fonctionnalités. Ces fonctionnalités ne nécessitent aucune mise à jour supplémentaire du SDK et ne seront appliquées que pour les utilisateurs sur les appareils iOS 15.

### Mode de mise au point {#focus-mode}

Les utilisateurs d'iOS 15 peuvent maintenant créer des « modes Focus » — des profils personnalisés utilisés pour déterminer quelles notifications ils veulent percer leur focus et s'afficher en priorité.

![Paramètres de notification]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### Niveaux d'interruption {#interruption-levels}

Sur iOS 15, les notifications push peuvent être envoyées avec l'un des quatre niveaux d'interruption :

* **Passif** (nouveau) - Pas de son, pas de vibration, pas de réveil de l'écran, pas de rupture des paramètres de mise au point.
* **Active** (par défaut) - Permet le son, la vibration, le réveil de l'écran, aucune rupture des paramètres de mise au point.
* **Time Sensitive** (nouveau) - Permet le son, la vibration, le réveil de l'écran, peut perturber les contrôles système si autorisé.
* **Critique** - Permet le son, les vibrations, le réveil de l'écran, peut percer les commandes du système et contourner le commutateur de sonnerie.

Pour en savoir plus sur la façon de définir cette option dans iOS Push, voir [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level).

### Résumé des notifications {#notification-summary}

![Résumé des notifications]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

Dans iOS 15, les utilisateurs peuvent (optionnellement) choisir certaines heures tout au long de la journée pour recevoir un résumé des notifications. Les notifications qui ne nécessitent pas une attention immédiate (i.e. envoyé en tant que "Passive" ou pendant que l'utilisateur est en mode Focus) sera regroupé pour éviter les interruptions constantes tout au long de la journée.

Pour chaque notification que vous envoyez, vous serez bientôt en mesure de spécifier un "score de pertinence" pour contrôler quelle notification doit apparaître en haut du résumé.

Pour en savoir plus sur la façon de définir le "score de pertinence d'une notification", voir [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score).

## Boutons de localisation {#location-buttons}

iOS 15 introduit un nouveau moyen pratique pour les utilisateurs d'accorder temporairement l'accès à la localisation dans une application.

Le nouveau bouton d'emplacement se base sur la permission existante "Autoriser une fois" sans demander à plusieurs utilisateurs qui cliquent plusieurs fois dans la même session.

Pour plus d'informations, regardez la vidéo [d'Apple sur le bouton Localisation](https://developer.apple.com/videos/play/wwdc2021/10102/) de la Conférence Mondiale des Développeurs (WWDC) de cette année.

{% alert tip %}
Cette fonctionnalité vous donne une chance supplémentaire de demander la permission aux utilisateurs ! Les utilisateurs qui ont précédemment refusé les autorisations de localisation avant iOS 15 seront affichés lorsque vous cliquez sur le bouton de localisation comme une opportunité de réinitialiser l'autorisation de l'état refusé une dernière fois.
{% endalert %}

### Utiliser les boutons de localisation avec Braze

Aucune intégration supplémentaire n'est nécessaire lorsque vous utilisez les boutons d'emplacement avec Braze. Votre application devrait continuer à passer la position d'un utilisateur (après avoir donné l'autorisation) comme d'habitude.

Selon Apple, les utilisateurs qui ont déjà partagé l'accès à la localisation en arrière-plan, l'option "Lors de l'utilisation de l'application" continuera à accorder ce niveau d'autorisation après la mise à niveau vers iOS 15.

## Messagerie Apple {#mail}

Cette année, Apple a annoncé de nombreuses mises à jour pour le suivi des e-mails et la protection de la vie privée. Pour plus d'informations, consultez notre [article de blog](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature).

## Emplacement de l'adresse IP Safari

Dans iOS 15, les utilisateurs pourront configurer Safari pour anonymiser ou généraliser l'emplacement qui peut être déterminé à partir de leurs adresses IP. Veuillez garder cela à l'esprit lors de l'utilisation du ciblage ou de la segmentation basée sur la localisation.

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2
