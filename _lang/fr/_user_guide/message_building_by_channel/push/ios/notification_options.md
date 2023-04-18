---
nav_title: "Options de notification"
article_title: Options de notification iOS
page_order: 2
page_layout: reference
description: "Cet article de référence couvre les options de notification iOS comme les alertes critiques, les notifications silencieuses, les notifications push provisoires et plus encore."

platform: iOS
channel:
  - Notification push

---

# Options de notification

> Avec la sortie d’iOS 12 d’Apple, Braze offre une prise en charge de plusieurs de ses fonctionnalités, notamment [Groupes de notification](#notification-groups), Notifications [silencieusesNotifications/Provisional/Autorisation](#provisional-push-authentication--quiet-notifications) provisoire et [Alertes critiques](#critical-alerts).

## Groupes de notification

Si vous souhaitez catégoriser vos messages et les regrouper dans la zone de notification de votre utilisateur, vous pouvez utiliser la fonctionnalité Groupes de notification d’iOS via Braze.

Créez votre campagne de notification push iOS, puis regardez en haut de l’onglet **Compose (Composer)** pour trouver la liste déroulante **Notification Groups (Groupes de notification)**.

![][26]{: style="max-width:60%;" }

Sélectionnez vos Groupes de notification dans la liste déroulante. Si les paramètres de votre groupe de notification fonctionnent mal ou si vous sélectionnez **None** (Aucun) dans la liste déroulante, le message sera automatiquement envoyé comme d’habitude à tous les utilisateurs définis dans le groupe d’apps.

Si vous n’avez aucun Groupe de notification listé, vous pouvez en ajouter un à l’aide de l’ID de thread iOS. Vous aurez besoin d’un ID de thread iOS pour chaque groupe de notification que vous souhaitez ajouter. Ensuite, ajoutez-le à vos groupes de notification en cliquant sur **Manage Notification Groups** (Gérer les groupes de notification) dans la liste déroulante et en remplissant les champs requis dans la fenêtre **Manage iOS Push Notification Groups** (Gérer les groupes de notification push iOS) qui apparaît.

![][27]

Créez votre campagne de notification push iOS, puis regardez en haut du volet de composition. Vous y trouverez la liste déroulante **Notification Groups** (Groupes de notification).

### Arguments récapitulatifs

En plus de regrouper des notifications par ID de thread, Apple vous permet de modifier les récapitulatifs qui apparaissent lorsque les notifications sont groupées. Les utilisateurs de Braze peuvent spécifier la catégorie récapitulative, le nombre de récapitulatifs et l’argument récapitulatif lors de la composition d’une campagne de notifications push à l’aide de notre outil.

{% alert tip %}
Notez que les notifications avec le même ID de thread sont groupées dans le plateau de notification sous le contrôle du système d’exploitation. iOS peut choisir d’afficher des notifications avec le même ID de thread séparément ou en groupes selon ce qu’il juge optimal.
{% endalert %}

Cochez la case **Alert Options** (Options d’alerte) dans le volet **Push Composer** (Composition de notification push).

Ensuite, sélectionnez `summary-arg` et `summary-arg-count` en tant que clés et saisissez ces valeurs dans la colonne correspondante. Si vous ne définissez pas de valeur pour `summary-arg`, sa valeur par défaut est 1.

### Catégories récapitulatives

Les catégories récapitulatives vous permettent de personnaliser l’ensemble du récapitulatif qui apparaît lorsque les notifications sont groupées. Vous pouvez créer et appliquer plusieurs catégories.

Pour utiliser une catégorie dans votre message, travaillez avec vos développeurs pour la mise en œuvre en utilisant l’exemple suivant :

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Cela ne nécessite pas de mise à jour SDK.
{% endalert %}

{% alert tip %}
Notez que `%u` et `%@` sont des chaînes de formatage pour le décompte récapitulatif et l’argument récapitulatif, respectivement. Lorsque le récapitulatif est affiché, ces variables seront remplacées par les valeurs de `summary-count` et de `summary-arg`.
{% endalert %}

Une fois que cela est configuré sur votre application, utilisez la catégorie récapitulative en cochant la case **Notification Buttons** (Boutons de notification) et en sélectionnant **Enter Pre-registered iOS Category** (Entrer la catégorie iOS préenregistrée).

Saisissez ensuite l’identifiant de catégorie récapitulative que vous avez définie dans votre application.

### Authentification de notification push provisoire et notifications silencieuses {#provisional-push}

Apple propose aux marques d’envoyer des notifications push discrètes vers les Centres de notification de leurs utilisateurs avant que ceux-ci n’aient officiellement et explicitement donné leur accord, ce qui vous donne l’occasion de tester très tôt la valeur de vos messages. Il vous suffit de [configurer des notifications push provisoires](#set-up-provisional-push-notifications) dans votre application, puis tout utilisateur possédant un jeton de notification push provisoire recevra vos messages.

Contrairement à un jeton de notification push iOS traditionnel, un jeton de notification push provisoire agit comme un « passe provisoire » qui permet aux marques d’atteindre de nouveaux utilisateurs avant qu’ils n’aient vu et cliqué sur la demande d’inscription aux notifications push natives d’Apple. Avec cette fonctionnalité, votre notification push sera envoyée directement à la barre de notification de votre nouvel utilisateur avec l’option « Keep » (Conserver) ou « Turn Off » (Désactiver) les notifications futures. Au lieu de faire l’expérience d’un parcours d’« abonnement », les utilisateurs feront l’expérience de quelque chose qui ressemble plus à un parcours de « désabonnement ».

{% alert tip %}
L’autorisation provisoire a le potentiel d’augmenter considérablement votre taux d’abonnement, mais seulement si les utilisateurs apprécient la valeur dans vos messages. Exploitez nos fonctionnalités de [segmentation utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [ciblage de site]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) et [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) pour vous assurer que les utilisateurs appropriés reçoivent ces notifications « provisoires » au bon moment. Ensuite, vous pouvez encourager les utilisateurs à s’abonner à vos notifications push, sachant qu’ils ajoutent de la valeur à l’expérience de vos utilisateurs avec votre application.
{% endalert %}

Quelle que soit l’option choisie par l’utilisateur, le jeton approprié ou le [statut d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) sera ajouté à leur [Contact Settings (Paramètres de contact)]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) sous l’onglet **Engagement** dans leur profil utilisateur.

![]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Vous pourrez cibler vos utilisateurs selon qu’ils sont provisoirement autorisés ou non en utilisant nos [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

![Panneau Détails du segment avec l’exemple de filtre de segment « Provisoirement autorisé sur Stopwatch iOS est vrai » pour cibler les utilisateurs.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si les utilisateurs choisissent de « désactiver » vos notifications push provisoires, ils ne verront plus de messages push provisoires de votre part. Soyez attentif au contenu et à la fréquence des messages envoyés via cette fonctionnalité !
{% endalert %}

{% alert important %}
Si vous utilisez des invites de notification push supplémentaires ou des [amorces de notification push in-app](https://www.braze.com/resources/glossary/priming-for-push/) (un message in-app qui encourage les utilisateurs à recevoir les notifications push), contactez votre représentant Braze pour obtenir des conseils supplémentaires.
{% endalert %}

#### Configurer des notifications push provisoires

Braze vous permet de vous inscrire à l’authentification provisoire en mettant à jour votre code dans votre extrait de code d’enregistrement de jeton au sein de votre implémentation SDK iOS Braze en utilisant les extraits de code suivants à titre d’exemple (envoyez-les à vos développeurs ou assurez-vous qu’ils [mettent en œuvre l’authentification de notification push provisoire au cours du processus d’intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
La mise en œuvre de l’authentification de notification push provisoire prend uniquement en charge iOS 12+ et renvoie une erreur si la cible du déploiement est antérieure. Vous pouvez en savoir plus [dans notre documentation sur la mise en œuvre ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#using-usernotification-framework-ios-10).
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

### Niveau d’interruption (iOS 15+) {#interruption-level}

![Page des paramètres de notification iOS qui montre les notifications activées pour une livraison immédiate et avec des notifications temporelles activées.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

Avec le nouveau mode Focus d’iOS 15, les utilisateurs contrôlent mieux le moment où les notifications des applications peuvent les « interrompre » par un son ou une vibration.

Les applications peuvent maintenant spécifier le niveau d’interruption d’une notification, en fonction de son urgence.

Gardez à l’esprit que les utilisateurs sont en fin de compte les maîtres de leur intérêt, et même si une notification temporelle (Time Sensitive) est livrée, ils peuvent spécifier quelles applications ne sont pas autorisées à interrompre leur intérêt.

Reportez-vous au tableau suivant pour connaître les niveaux d’interruption et leurs descriptions.

|Niveau d’interruption|Description|Quand l’utiliser|Mode Break Through Focus|
|--|--|--|--|
|[Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) (Passif)|Envoie une notification sans son, vibration ni éclairage de l’écran.|Notifications qui ne nécessitent pas d’attention immédiate.|Non|
|[Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (Actif, par défaut)|Émet juste un son, une vibration et éclaire l’écran si l’utilisateur n’est pas en mode Focus.|Notifications nécessitant une attention immédiate, sauf si l’utilisateur a activé le mode Focus.|Non|
|[Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) (Temporel)|Émet un son, une vibration et éclaire l’écran même si l’utilisateur est en mode Focus. Cela exige que la fonction **Time Sensitive Notifications** (Notifications temporelles) soit ajoutée à votre application dans Xcode|Des notifications opportunes qui devraient interrompre les utilisateurs indépendamment de leur mode Focus, comme un trajet ou une notification de livraison.|Oui|
|[Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) (Critique)|Émet un son, une vibration et éclaire l’écran même si l’option **Ne pas déranger** du téléphone est activée. Ceci [exige une approbation explicite par Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Urgences telles que des alertes météorologiques ou de sécurité graves|Oui|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

Pour modifier le niveau d’interruption d’une notification push iOS, sélectionnez l’onglet **Settings (Paramètres)** et choisissez le niveau souhaité dans le menu déroulant **Interruption Level (Niveau d’interruption)**.

![Niveau d’interruption défini sur Active (Actif, par défaut) et développé pour afficher tous les niveaux d’interruption disponibles : Passive (Passif), Active (Actif, par défaut), Time Sensitive (Temporel) et Critical (Critique).][28]

Cette fonctionnalité n’a pas de configuration minimale requise pour la version SDK, mais est uniquement appliquée pour les périphériques exécutant iOS 15+.

### Score de pertinence (iOS 15+) {#relevance-score}

![Récapitulatif de notification pour iOS intitulé « Récapitulatif de votre soirée » avec trois notifications.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 introduit également un nouveau moyen pour les utilisateurs de planifier de manière facultative un regroupement de plusieurs notifications à des moments désignés de la journée. Cela permet d’éviter les interruptions constantes tout au long de la journée pour des notifications qui ne nécessitent pas une attention immédiate.

Les applications peuvent spécifier quelles notifications push sont les plus pertinentes en définissant un **Score de pertinence**. Apple utilisera ce score pour déterminer quelles notifications doivent être mises en avant dans le récapitulatif des notifications planifiées, tandis que d’autres sont rendues accessibles lorsque les utilisateurs cliquent dans le récapitulatif. 

Toutes les notifications seront toujours accessibles dans le centre de notification de l’utilisateur.

Pour définir le score de pertinence d’une notification iOS, saisissez une valeur comprise entre `0.0` et `1.0` dans l’onglet **Settings (Paramètres)**. Par exemple, le message le plus important doit être envoyé avec `1.0`, alors qu’un message d’importance moyenne peut être envoyé avec `0.5`.

![][29]

Cette fonctionnalité n’a pas de configuration minimale requise pour la version SDK, mais est uniquement appliquée pour les périphériques exécutant iOS 15+.

Pour plus d’informations sur les longueurs maximales des messages selon les différents types de messages, reportez-vous aux ressources suivantes :

- [Spécifications de l’image et du texte]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Directives iOS sur le nombre de caractères]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

[26]: {% image_buster /assets/img_archive/notification_group_dropdown.png %}
[27]: {% image_buster /assets/img_archive/managenotgroups.png %}
[28]: {% image_buster /assets/img/ios/interruption-level.png %}
[29]: {% image_buster /assets/img/ios/relevance-score.png %}
