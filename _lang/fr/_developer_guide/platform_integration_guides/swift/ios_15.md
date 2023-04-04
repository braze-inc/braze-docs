---
hidden: true
nav_title: Guide de mise à jour iOS 15
article_title: Guide de mise à jour SDK iOS 15
page_order: 7
platform: iOS
description: "Cet article de référence couvre les nouvelles mises à jour du système d’exploitation iOS 15, les mises à jour SDK requises et les nouvelles fonctionnalités."

---

# Guide de mise à jour SDK iOS 15

Ce guide décrit les modifications introduites dans iOS 15 (WWDC21) et les étapes de mise à niveau requises pour votre intégration SDK Braze pour iOS.

> Pour obtenir une liste complète des nouvelles mises à jour iOS 15, consultez les [notes de publication iOS 15](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) d’Apple.


## Changements de transparence dans les navigations de l’interface utilisateur

Dans le cadre de nos tests annuels des versions bêta d’iOS, nous avons identifié une modification apportée par Apple qui fait que certaines barres de navigation de l’interface utilisateur apparaissent transparentes et non opaques. Cela sera visible dans iOS 15 lors de l’utilisation de l’interface utilisateur par défaut de Braze pour les cartes de contenu ou lorsque des liens profonds Web sont ouverts dans votre application plutôt que dans une application de navigateur distincte.

Pour éviter ce changement visuel dans iOS 15, nous vous recommandons fortement de mettre à niveau vers la version [SDK Braze pour iOS v4.3.2][1] dès que possible, avant que les utilisateurs commencent à mettre leur téléphone à niveau vers le nouveau système d’exploitation iOS 15.

## Nouveaux paramètres de notification {#notification-settings}

iOS 15 a introduit de nouvelles fonctionnalités de notification pour aider les utilisateurs à rester focalisés et à éviter de fréquentes interruptions tout au long de la journée. Nous sommes ravis d’offrir une assistance pour ces nouvelles fonctionnalités. Ces fonctionnalités ne nécessitent aucune mise à niveau supplémentaire du SDK et ne seront appliquées qu’aux utilisateurs de périphériques iOS 15.

### Modes de concentration {#focus-mode}

Les utilisateurs d’iOS 15 peuvent désormais créer des « Modes de Concentration », des profils personnalisés utilisés pour déterminer les notifications qu’ils souhaitent voir franchir le mode de concentration et afficher en évidence.

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### Niveaux d’interruption {#interruption-levels}

Dans iOS 15, les notifications push peuvent être envoyées avec l’un des quatre niveaux d’interruption :

* **Passive** (nouveau) : Pas de son, aucune vibration, pas de sortie de veille, pas de franchissement des paramètres du mode de concentration.
* **Active** (par défaut) : Permet les sons, les vibrations, la sortie de veille, pas de franchissement des paramètres du mode de concentration.
* **Contrainte de temps** (nouveau) : Permet les sons, les vibrations, la sortie de veille, peut franchir les commandes système si autorisé.
* **Critique** : Permet les sons, les vibrations, la sortie de veille, peut franchir les commandes système et contourner le commutateur de sonnerie.

Voir [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level) pour en savoir plus sur la manière de configurer cette option dans les notifications push iOS.

### Résumé de la notification {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

Dans iOS 15, les utilisateurs peuvent (facultativement) choisir certaines heures de la journée pour recevoir un résumé des notifications. Les notifications qui ne nécessitent pas une attention immédiate (c’est-à-dire envoyées comme « passives » ou lorsque l’utilisateur est en mode de concentration) seront regroupées pour éviter les interruptions constantes tout au long de la journée.

Pour chaque notification que vous envoyez, vous serez bientôt en mesure de spécifier un « score de pertinence » pour contrôler la notification devant apparaître en haut du résumé.

Voir [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score) pour en savoir plus sur la manière de définir le « score de pertinence » d’une notification.

## Boutons de localisation {#location-buttons}

iOS 15 introduit un nouveau moyen pratique pour les utilisateurs d’accorder temporairement l’accès à la position au sein d’une application. 

Le nouveau bouton de localisation s’appuie sur l’autorisation existante « Autoriser une fois » sans le proposer à plusieurs reprises aux utilisateurs qui cliquent plusieurs fois dans la même session.

Pour plus d’informations, regardez la vidéo d’Apple sur le [Bouton de localisation](https://developer.apple.com/videos/play/wwdc2021/10102/) diffusée lors de la Conférence mondiale des développeurs (WWDC) de cette année.

{% alert tip %}
Cette fonctionnalité vous donne une chance supplémentaire d’inviter les utilisateurs à obtenir leur autorisation ! Les utilisateurs ayant précédemment refusé des autorisations de localisation avant iOS 15 verront une invite lorsque vous cliquez sur le bouton de localisation comme une dernière opportunité de réinitialiser l’autorisation de l’état refusé.
{% endalert %}

### Utilisation des boutons de localisation avec Braze

Aucune intégration supplémentaire n’est requise lors de l’utilisation des boutons de localisation avec Braze. Votre application doit continuer à transmettre la localisation d’un utilisateur (une fois qu’il a accordé l’autorisation) comme d’habitude.

Selon Apple, pour les utilisateurs qui ont déjà partagé l’accès au site d’arrière-plan, l’option « While Using App » continuera à accorder ce niveau d’autorisation après qu’elles auront été mises à niveau vers iOS 15.

## Apple Mail {#mail}

Cette année, Apple a annoncé de nombreuses mises à jour du suivi des e-mails et de la confidentialité. Pour plus d’informations, consultez notre [blog post](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature).

## Localisation de l’adresse IP dans Safari

Dans iOS 15, les utilisateurs pourront configurer Safari pour rendre anonymes ou généraliser la localisation déterminée à partir de leurs adresses IP. Gardez cela à l’esprit lorsque vous utilisez un ciblage ou une segmentation basé sur la localisation.

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level
