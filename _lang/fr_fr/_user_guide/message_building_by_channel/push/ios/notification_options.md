---
nav_title: "Options de notification"
article_title: Options de notification iOS
page_order: 2
page_layout: reference
description: "Cet article de référence couvre les options de notification iOS comme les alertes critiques, les notifications silencieuses, les notifications push provisoires et plus encore."

platform: iOS
channel:
  - push

---

# Options de notification

> Avec la sortie d'iOS 12 d'Apple, Braze prend en charge plusieurs de ses fonctionnalités, notamment les [groupes de notification](#notification-groups), les [notifications silencieuses/autorisation provisoire](#provisional-push-authentication--quiet-notifications) et les [alertes critiques](#critical-alerts).

## Groupes de notification

Si vous souhaitez catégoriser vos messages et les regrouper dans la zone de notification de votre utilisateur, vous pouvez utiliser la fonctionnalité Groupes de notification d'iOS via Braze.

Créez votre campagne push iOS, puis accédez à l'onglet **Paramètres** et ouvrez le menu déroulant **Groupe de notification**.

![L'onglet « Paramètres » avec un menu déroulant « Groupe de notification » qui a sélectionné la valeur « Coupons ».]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Sélectionnez vos groupes de notification dans la liste déroulante. Si les paramètres de votre groupe de notification ne fonctionnent pas correctement ou si vous sélectionnez **Aucun** dans le menu déroulant, le message sera automatiquement envoyé normalement à tous les utilisateurs définis dans l'espace de travail.

Si aucun groupe de notification n'est listé, vous pouvez en ajouter un à l'aide de l'ID de thread iOS. Vous aurez besoin d'un ID de thread iOS pour chaque groupe de notification que vous souhaitez ajouter. Ensuite, ajoutez-le à vos groupes de notification en cliquant sur **Gérer les groupes de notification** dans le menu déroulant et en remplissant les champs requis dans la fenêtre **Gérer les groupes de notification push iOS** qui apparaît.

![Fenêtre permettant la gestion des groupes de notifications push iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Créez votre campagne push iOS, puis regardez en haut du volet de composition. Vous y verrez un menu déroulant intitulé **Groupes de notification**.

### Arguments récapitulatifs

En plus de regrouper les notifications par ID de thread, Apple vous permet de modifier les récapitulatifs qui apparaissent lorsque les notifications sont groupées. Les utilisateurs de Braze peuvent spécifier la catégorie récapitulative, le nombre récapitulatif et l'argument récapitulatif lors de la composition d'une campagne push à l'aide de notre outil.

{% alert tip %}
Notez que le regroupement des notifications avec le même ID de thread dans le plateau de notification est contrôlé par le système d'exploitation. iOS peut choisir d'afficher les notifications avec le même ID de thread séparément ou en groupes selon ce qu'il juge optimal.
{% endalert %}

Cochez la case **Options d'alerte** dans le **compositeur de notifications push**.

Ensuite, sélectionnez `summary-arg` et `summary-arg-count` en tant que clés et saisissez ces valeurs dans la colonne correspondante. Si vous ne définissez pas de valeur pour `summary-arg`, la valeur par défaut sera 1.

### Catégories récapitulatives

Les catégories récapitulatives vous permettent de personnaliser l'ensemble du récapitulatif qui apparaît lorsque les notifications sont groupées. Vous pouvez créer et appliquer plusieurs catégories.

Pour utiliser une catégorie dans votre message, collaborez avec vos développeurs pour l'implémenter en suivant l'exemple ci-dessous :

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Cela ne nécessite pas de mise à jour du SDK.
{% endalert %}

{% alert tip %}
Notez que `%u` et `%@` sont des chaînes de formatage pour le nombre récapitulatif et l'argument récapitulatif, respectivement. Lorsque le récapitulatif est affiché, ces marques substitutives seront remplacées par les valeurs de `summary-count` et de `summary-arg`.
{% endalert %}

Une fois cette configuration effectuée dans votre application, utilisez la catégorie récapitulative en cochant la case **Notification Buttons** et en sélectionnant **Enter Pre-registered iOS Category**.

Saisissez ensuite l'identifiant de catégorie récapitulative que vous avez défini dans votre application.

### Authentification push provisoire et notifications silencieuses {#provisional-push}

Apple propose aux marques d'envoyer des notifications push silencieuses vers les centres de notification de leurs utilisateurs avant que ceux-ci n'aient officiellement et explicitement donné leur accord, ce qui vous donne l'occasion de démontrer très tôt la valeur de vos messages. Il vous suffit de [configurer les notifications push provisoires](#set-up-provisional-push-notifications) dans votre application : tout utilisateur disposant d'un jeton de notification push provisoire recevra alors vos messages.

Contrairement à un jeton de notification push iOS traditionnel, un jeton de notification push provisoire agit comme un « laissez-passer d'essai » qui permet aux marques d'atteindre de nouveaux utilisateurs avant qu'ils n'aient vu et cliqué sur la demande d'abonnement native d'Apple pour les notifications push. Avec cette fonctionnalité, votre notification push sera envoyée directement dans le plateau de notification de votre nouvel utilisateur avec l'option « Conserver » ou « Désactiver » les notifications futures. Au lieu de vivre un parcours d'« abonnement », les utilisateurs vivront plutôt un parcours de « désabonnement ».

{% alert tip %}
L'autorisation provisoire a le potentiel d'augmenter considérablement votre taux d'abonnement, mais uniquement si les utilisateurs perçoivent la valeur de vos messages. Assurez-vous d'utiliser nos fonctionnalités de [segmentation des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), de [ciblage géographique]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) et de [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) pour garantir que les bons utilisateurs reçoivent ces notifications « d'essai » au bon moment. Vous pourrez ensuite encourager les utilisateurs à s'abonner pleinement à vos notifications push, sachant qu'elles apportent une réelle valeur ajoutée à leur expérience avec votre application.
{% endalert %}

Quelle que soit l'option choisie par l'utilisateur, le jeton approprié ou le [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) sera ajouté à ses [paramètres de contact]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) sous l'onglet **Engagement** de son profil utilisateur.

![Paramètres de contact avec un statut d'abonnement push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Vous pourrez cibler vos utilisateurs selon qu'ils disposent ou non de l'autorisation provisoire en utilisant nos [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

![Panneau Détails du segment avec l'exemple de filtre de segment « Provisoirement autorisé sur Stopwatch iOS est vrai » pour cibler les utilisateurs.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si les utilisateurs choisissent de « désactiver » vos notifications push provisoires, ils ne verront plus de messages push provisoires de votre part. Soyez attentif au contenu et à la fréquence des messages envoyés via cette fonctionnalité !
{% endalert %}

{% alert important %}
Si vous utilisez des invites push supplémentaires ou des [amorces push in-app](https://www.braze.com/resources/glossary/priming-for-push/) (un message in-app qui encourage les utilisateurs à s'abonner aux notifications push), contactez votre conseiller Braze pour obtenir des conseils supplémentaires.
{% endalert %}

#### Configurer les notifications push provisoires

Braze vous permet de vous inscrire à l'authentification provisoire en mettant à jour votre code dans votre extrait de code d'enregistrement de jeton au sein de votre implémentation du SDK iOS de Braze, en utilisant les extraits suivants comme exemple (envoyez-les à vos développeurs ou assurez-vous qu'ils [implémentent l'authentification push provisoire pendant le processus d'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
L'implémentation de l'authentification push provisoire prend uniquement en charge iOS 12+ et génère une erreur si la cible de déploiement est antérieure. Pour en savoir plus, consultez [notre documentation détaillée sur l'implémentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
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

**Objective-C**

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

Avec le nouveau mode Concentration d'iOS 15, les utilisateurs contrôlent mieux le moment où les notifications des applications peuvent les « interrompre » par un son ou une vibration.

![Page des paramètres de notification iOS affichant les notifications activées pour une réception immédiate et les notifications urgentes activées.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Les applications peuvent désormais spécifier le niveau d'interruption d'une notification en fonction de son urgence.

Pour modifier le niveau d'interruption d'une notification push iOS, sélectionnez l'onglet **Paramètres** et choisissez le niveau souhaité dans le menu déroulant **Niveau d'interruption**.

![Menu déroulant permettant de sélectionner le niveau d'interruption.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Cette fonctionnalité ne nécessite pas de version minimale du SDK, mais s'applique uniquement aux appareils sous iOS 15+.

Gardez à l'esprit que ce sont les utilisateurs qui contrôlent en fin de compte leur mode Concentration : même si une notification Time Sensitive est livrée, ils peuvent spécifier quelles applications ne sont pas autorisées à passer outre leur mode Concentration.

Reportez-vous au tableau suivant pour connaître les niveaux d'interruption et leurs descriptions.

|Niveau d'interruption|Description|Quand l'utiliser|Passe outre le mode Concentration|
|--|--|--|--|
|[Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Envoie une notification sans son, vibration ni allumage de l'écran.|Notifications qui ne nécessitent pas d'attention immédiate.|Non|
|[Actif](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (par défaut)|Émet un son, une vibration et allume l'écran uniquement si l'utilisateur n'est pas en mode Concentration.|Notifications nécessitant une attention immédiate, sauf si l'utilisateur a activé le mode Concentration.|Non|
|[Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|Émet un son, une vibration et allume l'écran même en mode Concentration. La **capacité Time Sensitive Notifications** doit être ajoutée à votre application dans Xcode.|Notifications urgentes qui doivent interrompre les utilisateurs quel que soit leur mode Concentration, comme une notification de covoiturage ou de livraison.|Oui|
|[Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Émet un son, une vibration et allume l'écran même si le mode **Ne pas déranger** du téléphone est activé. Ceci [nécessite l'approbation explicite d'Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Urgences telles que des alertes météorologiques ou de sécurité graves.|Oui|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Score de pertinence (iOS 15+) {#relevance-score}

![Un résumé des notifications pour iOS intitulé « Your Evening Summary » avec trois notifications.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 introduit également un nouveau moyen pour les utilisateurs de planifier un regroupement de plusieurs notifications à des moments précis de la journée. Cela permet d'éviter les interruptions constantes pour des notifications qui ne nécessitent pas une attention immédiate.

Les applications peuvent indiquer quelles notifications push sont les plus pertinentes en définissant un **score de pertinence**. Apple utilisera ce score pour déterminer quelles notifications doivent être mises en avant dans le récapitulatif planifié, tandis que les autres restent accessibles lorsque les utilisateurs consultent le récapitulatif.

Toutes les notifications restent accessibles dans le centre de notification de l'utilisateur.

Pour définir le score de pertinence d'une notification iOS, saisissez une valeur entre `0.0` et `1.0` dans l'onglet **Paramètres**. Par exemple, le message le plus important doit être envoyé avec `1.0`, tandis qu'un message d'importance moyenne peut être envoyé avec `0.5`.

![Score de pertinence de « 0.5 ».]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Cette fonctionnalité ne nécessite pas de version minimale du SDK, mais s'applique uniquement aux appareils sous iOS 15+.

Pour plus d'informations sur les longueurs maximales des messages selon les différents types, consultez les ressources suivantes :

- [Spécifications des images et du texte pour les notifications push]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)
- [Recommandations sur le nombre de caractères pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)