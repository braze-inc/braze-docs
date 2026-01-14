---
nav_title: "Options de notification"
article_title: Options de notification iOS
page_order: 2
page_layout: reference
description: "Cet article de référence couvre les options de notification d'iOS comme les alertes critiques, les notifications silencieuses, les notifications push provisoires, et plus encore."

platform: iOS
channel:
  - push

---

# Options de notification

> Avec la sortie d'iOS 12 d'Apple, Braze offre une prise en charge de plusieurs de ses fonctionnalités, notamment les [groupes de notification](#notification-groups), les [notifications silencieuses/autorisation provisoire](#provisional-push-authentication--quiet-notifications) et les [alertes critiques.](#critical-alerts)

## Groupes de notification

Si vous souhaitez catégoriser vos messages et les regrouper dans le plateau de notification de votre utilisateur, vous pouvez utiliser la fonctionnalité Groupes de notification d'iOS par l'intermédiaire de Braze.

Créez votre campagne push iOS, puis vers l'onglet **Paramètres** et ouvrez le menu déroulant **Groupe de notification**.

\![L'onglet "Paramètres" avec un menu déroulant "Groupe de notification" qui a sélectionné la valeur "Coupons".]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Sélectionnez vos groupes de notification dans le menu déroulant. Si les paramètres de votre groupe de notification ne fonctionnent pas correctement ou si vous sélectionnez **Aucun** dans le menu déroulant, le message sera automatiquement envoyé comme d'habitude à tous les utilisateurs définis dans l'espace de travail.

Si aucun groupe de notification n'est répertorié ici, vous pouvez en ajouter un à l'aide de l'ID du fil de discussion iOS. Vous aurez besoin d'un ID de fil iOS pour chaque groupe de notification que vous souhaitez ajouter. Ensuite, ajoutez-le à vos groupes de notification en cliquant sur **Gérer les groupes de notification** dans le menu déroulant et en remplissant les champs requis dans la fenêtre **Gérer les groupes de notification iOS Push** qui s'affiche.

\![Fenêtre permettant de gérer les groupes de notification push d'iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Créez votre campagne de push iOS, puis regardez en haut du compositeur. Vous y trouverez un menu déroulant intitulé **Groupes de notification.**

### Arguments de synthèse

En plus de regrouper les notifications par ID de fil, Apple vous permet de modifier les résumés qui apparaissent lorsque les notifications sont regroupées. Les utilisateurs de Braze peuvent spécifier la catégorie de résumé, le nombre de résumés et l'argument de résumé lorsqu'ils composent une campagne push à l'aide de notre outil.

{% alert tip %}
Notez que la manière dont les notifications ayant le même ID de fil sont regroupées dans le plateau de notification est sous le contrôle du système d'exploitation. iOS peut choisir d'afficher les notifications ayant le même ID de fil séparément ou en groupe, en fonction de ce qu'il juge optimal.
{% endalert %}

Cochez la case **Options d'alerte** dans le **Push Composer**.

Ensuite, sélectionnez `summary-arg` et `summary-arg-count` comme clés et saisissez ces valeurs dans la colonne correspondante. Si vous ne définissez pas de valeur pour `summary-arg`, la valeur par défaut sera 1.

### Catégories de résumé

Les catégories de résumé vous permettent de personnaliser l'ensemble du résumé qui apparaît lorsque les notifications sont regroupées. Vous pouvez créer et appliquer plusieurs catégories.

Pour utiliser une catégorie dans votre message, travaillez avec vos développeurs pour mettre en œuvre l'exemple suivant :

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Cela ne nécessitera pas de mise à jour du SDK.
{% endalert %}

{% alert tip %}
Notez que `%u` et `%@` sont des chaînes de caractères de formatage pour le compte de résumé et l'argument de résumé, respectivement. Lors de l'affichage du résumé, ces marqueurs substitutifs seront remplacés par les valeurs de `summary-count` et `summary-arg`.
{% endalert %}

Une fois que cela est configuré sur votre application, utilisez la catégorie de résumé en cochant la case **Boutons de notification** et en sélectionnant **Entrer la catégorie iOS préenregistrée**.

Saisissez ensuite l'identifiant de la catégorie de résumé que vous avez défini dans votre application.

### Authentification push provisoire et notifications silencieuses {#provisional-push}

Apple donne aux marques la possibilité d'envoyer des notifications push discrètes dans les centres de notification de leurs utilisateurs avant qu'ils n'aient officiellement et explicitement opté pour l'abonnement, ce qui vous donne l'occasion de démontrer très tôt la valeur de vos messages. Il vous suffit de [configurer des notifications push provisoires](#set-up-provisional-push-notifications) dans votre app, puis tout utilisateur disposant d'un jeton push provisoire recevra vos messages.

Contrairement à un jeton de push iOS traditionnel, un jeton de push provisoire agit comme un "laissez-passer d'essai" qui permet aux marques d'atteindre de nouveaux utilisateurs avant qu'ils n'aient vu et cliqué sur la demande d'abonnement push native d'Apple. Grâce à cette fonctionnalité, votre notification push sera envoyée directement dans le bac de notification de votre nouvel utilisateur, avec la possibilité de "conserver" ou de "désactiver" les futures notifications. Au lieu de faire l'expérience d'un parcours "d'abonnement", les utilisateurs feront l'expérience de quelque chose qui s'apparente davantage à un parcours "d'exclusion".

{% alert tip %}
L'autorisation provisoire a le potentiel d'augmenter considérablement votre taux d'abonnement, mais seulement si les utilisateurs voient la valeur de vos messages. Veillez à utiliser nos fonctionnalités de [segmentation des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), de [ciblage de l'emplacement/localisation]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) et de [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) pour vous assurer que les utilisateurs appropriés reçoivent ces notifications "d'essai" au bon moment. Ensuite, vous pouvez encourager les utilisateurs à s'abonner pleinement à vos notifications push, sachant qu'elles ajoutent de la valeur à l'expérience de vos utilisateurs avec votre application.
{% endalert %}

Quelle que soit l'option choisie par l'utilisateur, le jeton ou le [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) approprié sera ajouté à ses [paramètres de contact]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) sous l'onglet **Engagement de** son profil utilisateur.

!Paramètres de contact avec un statut d'abonné en mode push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Vous pourrez cibler vos utilisateurs en fonction de leur autorisation provisoire ou non à l'aide de nos [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

!Panneau Segment Details avec le filtre de segmentation type "Provisionally Authorized on iOS Stopwatch (iOS) is true" pour cibler les utilisateurs.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si les utilisateurs choisissent de "Désactiver" le push provisoire de votre part, ils ne verront plus d'envoi de messages provisoires de votre part. Faites attention au contenu et à la cadence des messages envoyés à l'aide de cette fonctionnalité !
{% endalert %}

{% alert important %}
Si vous utilisez des demandes d'abonnement supplémentaires ou des [amorces de push in-app](https://www.braze.com/resources/glossary/priming-for-push/) (un message in-app qui encourage les utilisateurs à s'abonner aux notifications push), contactez votre conseiller Braze pour obtenir des conseils supplémentaires.
{% endalert %}

#### Mettre en place des notifications push provisoires

Braze vous permet de vous inscrire à l'authentification provisoire en mettant à jour votre code dans votre extrait d'enregistrement de jeton au sein de votre implémentation du SDK iOS de Braze en utilisant les extraits suivants à titre d'exemple (envoyez-les à vos développeurs ou veillez à ce qu'ils [implémentent l'authentification provisoire par push au cours du processus d'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
La mise en œuvre de l'authentification push provisoire ne prend en charge qu'iOS 12+ et génère une erreur si la cible de déploiement est antérieure à cette date. Pour en savoir plus [, consultez notre documentation plus détaillée sur la mise en œuvre ici.]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objectif-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Niveau d'interruption (iOS 15+) {#interruption-level}

Avec le nouveau mode Focus d'iOS 15, les utilisateurs contrôlent davantage le moment où les notifications des applications peuvent les "interrompre" par un son ou une vibration.

\![Page des paramètres de notification d'iOS qui montre les notifications activées pour une réception/distribution immédiate et avec les notifications sensibles au temps activées.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Les applications peuvent désormais spécifier le niveau d'interruption d'une notification, en fonction de son urgence.

Pour modifier le niveau d'interruption d'une notification push iOS, sélectionnez l'onglet **Paramètres** et choisissez le niveau souhaité dans le menu déroulant **Niveau d'interruption**.

\![Liste déroulante permettant de sélectionner le niveau d'interruption.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Cette fonctionnalité ne requiert pas de version minimale du SDK, mais elle ne s'applique qu'aux appareils fonctionnant sous iOS 15+.

Gardez à l'esprit que ce sont les utilisateurs qui, en fin de compte, contrôlent leur concentration et que, même si une notification sensible au temps est émise, ils peuvent spécifier les applications qui ne sont pas autorisées à briser leur concentration.

Reportez-vous au tableau suivant pour connaître les niveaux d'interruption et leur description.

|Niveau d'interruption|Description|Quand utiliser|Mode "Break Through Focus|
|--|--|--|--|
|[Passif](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Envoie une notification sans son, ni vibration, ni activation de l'écran.|Les notifications qui ne nécessitent pas une attention immédiate.|Non|
|[Actif](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (par défaut)|N'émet un son, une vibration et n'allume l'écran que si l'utilisateur n'est pas en mode de mise au point.|Les notifications qui requièrent une attention immédiate, à moins que l'utilisateur n'ait activé le mode "Focus".|Non|
|[Le temps est compté](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|L'appareil émet un son, vibre et allume l'écran même en mode de mise au point. Pour cela, il faut que la **fonctionnalité Notifications sensibles au temps** soit ajoutée à votre application dans Xcode.|Des notifications opportunes qui devraient déranger les utilisateurs quel que soit leur mode de focalisation, comme une notification de covoiturage ou de réception/distribution.|Oui|
|[Critique](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Il émet un son, vibre et allume l'écran même si la fonction " **Ne pas déranger** " du téléphone est activée. Cela [nécessite l'approbation explicite d'Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Urgences telles que les intempéries ou les alertes à la sécurité|Oui|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Score de pertinence (iOS 15+) {#relevance-score}

Un résumé de notification pour iOS intitulé "Votre résumé du soir" avec trois notifications.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 introduit également une nouvelle façon pour les utilisateurs de planifier de manière optionnelle un groupe de notifications multiples (digest) à des heures désignées tout au long de la journée. Cela permet d'éviter les interruptions constantes tout au long de la journée pour les notifications qui ne nécessitent pas une attention immédiate.

Les applications peuvent spécifier quelles notifications push sont les plus pertinentes en définissant un **score de pertinence.** Apple utilisera ce score pour déterminer quelles notifications doivent être mises en avant dans le résumé des notifications planifiées, tandis que d'autres sont rendues disponibles lorsque les utilisateurs cliquent dans le résumé. 

Toutes les notifications resteront accessibles dans le centre de notification de l'utilisateur.

Pour définir le score de pertinence d'une notification iOS, saisissez une valeur comprise entre `0.0` et `1.0` dans l'onglet **Paramètres**. Par exemple, le message le plus important doit être envoyé avec `1.0`, tandis qu'un message d'importance moyenne peut être envoyé avec `0.5`.

\![Score de pertinence de "0.5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Cette fonctionnalité ne requiert pas de version minimale du SDK, mais elle ne s'applique qu'aux appareils fonctionnant sous iOS 15+.

Pour plus d'informations sur la longueur maximale des messages pour les différents types de messages, consultez les ressources suivantes :

- [Spécifications des images et des textes]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Lignes directrices sur le nombre de caractères pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

