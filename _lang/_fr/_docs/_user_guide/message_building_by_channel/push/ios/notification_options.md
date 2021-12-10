---
nav_title: "Options de notification (iOS)"
article_title: Options de notification push
page_order: 2
page_layout: Référence
description: "Cet article de référence couvre les options de notification iOS telles que les alertes critiques, les notifications silencieuses, les notifications push provisoires, et plus encore."
platform: iOS
channel:
  - Pousser
---

# Options de notification iOS

> Avec la sortie d'iOS 12 d'Apple, Braze offre la prise en charge de plusieurs de ses fonctionnalités, y compris [Groupes de Notification](#notification-groups), [Notifications silencieuses / Autorisation provisoire](#provisional-push-authentication--quiet-notifications), et [Alertes critiques](#critical-alerts).

## Groupes de notifications

Si vous souhaitez catégoriser vos messages et les regrouper dans la barre de notification de votre utilisateur, vous pouvez utiliser la fonctionnalité Groupes de notifications d'iOS via Braze.

Créez votre campagne de push iOS, puis regardez en haut de l'onglet **Composer** pour le menu déroulant **Groupes de Notification**.

!\[notificationgroupsdropdown\]\[26\]{: style="max-width:60%;" }

Sélectionnez vos groupes de notification dans la liste déroulante. Si les paramètres de votre groupe de notification ne fonctionnent pas ou si vous sélectionnez __Aucun__ dans la liste déroulante, le message enverra automatiquement comme normal à tous les utilisateurs définis dans le groupe d'applications.

Si vous n'avez aucun groupe de notification listé ici, vous pouvez en ajouter un en utilisant l'identifiant de discussion iOS. Vous aurez besoin d'un ID de sujet iOS pour chaque groupe de notification que vous souhaitez ajouter. Ensuite, ajoutez-la à vos groupes de notification en cliquant sur __Gérer les groupes de notification__ dans la liste déroulante et en remplissant les champs requis dans la fenêtre __Gérer les groupes de notification__ iOS qui apparaît.

!\[Gérer les groupes de notifications\]\[27\]

Créez votre campagne de push iOS, puis regardez en haut du compositeur. Là, vous verrez un menu déroulant étiqueté **Groupes de notification**.

### Arguments sommaires

En plus de regrouper les notifications par ID de thread, Apple vous permet de modifier les résumés qui apparaissent lorsque les notifications sont groupées. Les utilisateurs de Braze peuvent spécifier la catégorie récapitulative, le nombre de résumés et l'argument de résumé lors de la rédaction d'une campagne de push en utilisant notre outil.

{% alert tip %}
Notez que la façon dont les notifications avec le même ID de discussion sont regroupées dans la zone de notification est sous le contrôle de l'OS. iOS peut choisir d'afficher les notifications avec le même ID de discussion séparément ou dans les groupes selon ce qu'il juge optimal.
{% endalert %}

Vérifiez la case __Options d'alerte__ dans le __Composer Push__.

Ensuite, sélectionnez `summary-arg` et `summary-arg-count` comme clés et saisissez ces valeurs dans la colonne correspondante. Si vous ne définissez pas de valeur pour `summary-arg`, elle sera par défaut 1.

### Catégories sommaires

Les catégories résumées vous permettent de personnaliser le résumé complet qui apparaît lorsque les notifications sont groupées. Vous pouvez créer et appliquer plusieurs catégories.

Pour utiliser une catégorie dans votre message, travaillez avec vos développeurs pour implémenter en utilisant l'exemple suivant :

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u articles de nouvelles supplémentaires de %@"
                                                       Options:0];
```

{% alert important %}
Cela ne nécessitera pas de mise à jour du SDK.
{% endalert %}

{% alert tip %}
Veuillez noter que `%u` et `%@` sont en train de formater des chaînes pour le nombre de résumés et l'argument de récapitulation, respectivement. Lorsque le résumé est affiché, ces espaces réservés seront remplacés par les valeurs pour `résumé-count` et `résumé-arg`.
{% endalert %}

Une fois que cela est configuré sur votre application, utilisez la catégorie de résumé en cochant la case __Boutons de notification__ et en sélectionnant __Entrer dans la catégorie iOS préenregistrée__.

Ensuite, entrez l'identifiant de la catégorie récapitulative que vous avez défini dans votre application.

### Authentification provisoire push et notifications silencieuses {#provisional-push}

Apple permet aux marques d'envoyer des notifications push silencieuses aux centres de notification de leurs utilisateurs avant de les envoyer officiellement, explicitement opt-in, vous donnant la possibilité de démontrer la valeur de vos messages plus tôt. Tout ce que vous avez à faire est de [configurer des notifications push provisoires](#set-up-provisional-push-notifications) dans votre application, alors tout utilisateur ayant un jeton de push provisoire recevra vos messages.

Contrairement à un jeton de poussée traditionnel pour iOS, Un jeton de push provisoire agit comme un "passe d'essai" qui permet aux marques de rejoindre de nouveaux utilisateurs avant qu'ils n'aient vu et cliqué sur l'invite native d'Apple. Avec cette fonctionnalité, votre notification push sera envoyée directement dans la zone de notification de votre nouvel utilisateur avec l'option de « Garder » ou « Désactiver » les futures notifications. Au lieu de faire l'expérience d'un voyage "opt-in", les utilisateurs verront quelque chose de plus similaire à un voyage "opt-out".

{% alert tip %}
L'autorisation provisoire peut augmenter considérablement votre taux d'opt-in, mais seulement si les utilisateurs voient de la valeur dans vos messages. N'oubliez pas d'utiliser notre segmentation [utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [localisation ciblée]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/), et [la personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) des fonctionnalités pour s'assurer que les utilisateurs appropriés reçoivent ces notifications « d'essai » au bon moment. Ensuite, vous pouvez encourager les utilisateurs à opter pleinement pour vos notifications push, sachant qu'elles ajoutent de la valeur à l'expérience de vos utilisateurs avec votre application.
{% endalert %}

Quelle que soit l'option choisie par l'utilisateur, l'utilisateur ajoutera le jeton approprié ou le [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) à son [Paramètres de contact]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) (sous l'onglet **Engagement** dans son profil d'utilisateur, montrée ci-dessous).

![Profil utilisateur provisoirement autorisé]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Vous serez en mesure de cibler vos utilisateurs en fonction de s'ils sont provisoirement autorisés ou non à utiliser nos [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) (illustrés ci-dessous).

![Segment provisoirement autorisé]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si les utilisateurs choisissent de « désactiver » les push provisoires de votre part, ils ne verront plus de messages push provisoires de votre part. Soyez attentif au contenu et à la cadence du message envoyé en utilisant cette fonctionnalité!
{% endalert %}

{% alert important %}
Si vous utilisez des messages push supplémentaires ou des [primers de push dans l'application](https://www.braze.com/resources/glossary/priming-for-push/) (un message dans l'application qui encourage les utilisateurs à opter pour les notifications push), veuillez contacter votre représentant de Braze pour obtenir des conseils supplémentaires.
{% endalert %}

#### Mettre en place des notifications push provisoires

Braze vous permet de vous inscrire à l'authentification provisoire en mettant à jour votre code dans votre _snippet d'enregistrement de jetons_ dans l'implémentation de Braze iOS SDK en utilisant les snippets ci-dessous comme exemple (envoyez-les à vos développeurs ou assurez-vous qu'ils [implémentent une authentification push provisoire pendant le processus d'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
L'implémentation de l'authentification Provisional Push prend uniquement en charge iOS 12+ et échouera si la cible de déploiement est avant cela. Vous pouvez en apprendre plus à ce sujet [dans notre documentation d'implémentation plus détaillée ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
__Rapide__

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

__Objectif-C__

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
centre. elegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12. , *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Niveau d'interruption (iOS 15+) {#interruption-level}

![Paramètres de notification]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

Avec le nouveau mode Focus d'iOS 15, les utilisateurs contrôlent davantage quand les notifications des applications peuvent les "interrompre" avec un son ou une vibration.

Les applications peuvent maintenant spécifier quel niveau d'interruption doit inclure une notification, en fonction de son urgence.

Gardez à l'esprit que les utilisateurs sont en fin de compte ceux qui contrôlent leur attention, et même si une notification sensible au temps est envoyée, ils peuvent spécifier quelles applications ne sont pas autorisées à perturber leur focalisation.

Les quatre nouvelles options de niveau d'interruption sont :

| Niveau d'interruption                                                                                                          | Libellé                                                                                                                                                                                                                                                  | Quand utiliser                                                                                                                                                 | Mode pause à travers la mise au point |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| [Passif](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)                  | Envoie une notification sans son, vibration ou activation de l'écran.                                                                                                                                                                                    | Les notifications qui ne nécessitent pas une attention immédiate.                                                                                              | Non                                   |
| [Actif](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (par défaut)       | Ne fera un son, des vibrations et allumera l'écran que si l'utilisateur n'est pas en mode Focus.                                                                                                                                                         | Notifications nécessitant une attention immédiate, sauf si le mode Focus de l'utilisateur est activé.                                                          | Non                                   |
| [Sensible au temps](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) | Faire un son, vibrer et allumer l'écran, même en mode Focus. Cela nécessite que la fonctionnalité __Notifications sensibles au temps__ soit ajoutée à votre application en Xcode                                                                         | Notifications opportunes qui devraient perturber les utilisateurs quel que soit leur mode Focus, comme un partage de courses ou une notification de livraison. | Oui                                   |
| [Critique](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)               | Fait un son, vibreur et allumera l'écran même si le commutateur **Ne pas déranger** du téléphone est activé. Ce [nécessite une approbation explicite par Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/). | Des urgences telles que des avertissements météorologiques sévères ou des alertes de sécurité                                                                  | Oui                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

Pour modifier le niveau d'interruption pour une notification push iOS, choisissez le niveau souhaité dans l'onglet **Paramètres** de votre message :

!\[Option de Niveau d'Interruption\]\[28\]

Cette fonctionnalité n'a pas de version de SDK minimale requise, mais n'est appliquée que pour les appareils fonctionnant sous iOS 15+.

### Score de pertinence (iOS 15+) {#relevance-score}

![Résumé des notifications]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 introduit également une nouvelle façon pour les utilisateurs de programmer (optionnellement) un regroupement de plusieurs notifications à des heures désignées tout au long de la journée. Ceci est fait pour éviter des interruptions constantes tout au long de la journée pour les notifications qui n'ont pas besoin d'une attention immédiate.

Les applications peuvent spécifier quelles notifications push sont les plus pertinentes en définissant un __Score de Pertinence__. Apple utilisera ce score pour déterminer quelles notifications doivent être affichées dans le Résumé de la notification programmée tandis que d'autres seront disponibles lorsque les utilisateurs cliqueront dans le résumé.

Toutes les notifications seront toujours accessibles dans le centre de notification de l'utilisateur.

Pour définir le score de pertinence d'une notification iOS, entrez une valeur entre `0.0` et `1.0` dans l'onglet **Paramètres**. Par exemple, le message le plus important doit être envoyé avec `1.`, alors qu'un message de moyenne importance peut être envoyé avec `0.5`.

!\[Option de Score de Relevance\]\[29\]

Cette fonctionnalité n'a pas de version de SDK minimale requise, mais n'est appliquée que pour les appareils fonctionnant sous iOS 15+.

Pour plus d'informations sur la longueur maximale des messages pour les différents types de messages, reportez-vous aux ressources suivantes :

- [Caractéristiques de l'image et du texte]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Règles pour le nombre de caractères iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)
[26]: {% image_buster /assets/img_archive/notification_group_dropdown.png %} [27]: {% image_buster /assets/img_archive/managenotgroups. ng %} [28]: {% image_buster /assets/img/ios/interruption-level.png %} [29]: {% image_buster /assets/img/ios/relevance-score.png %}
