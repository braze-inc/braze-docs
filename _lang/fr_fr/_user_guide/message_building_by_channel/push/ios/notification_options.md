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

> Avec la sortie d'iOS 12 d'Apple, Braze offre un support pour plusieurs de ses fonctionnalités, y compris [Groupes de notifications](#notification-groups), [Notifications silencieuses/Autorisation provisoire](#provisional-push-authentication--quiet-notifications), et [Alertes critiques](#critical-alerts).

## Groupes de notification

Si vous souhaitez catégoriser vos messages et les regrouper dans la zone de notification de votre utilisateur, vous pouvez utiliser la fonctionnalité Groupes de notification d’iOS via Braze.

Créez votre campagne push iOS, puis vers l'onglet **Paramètres** et ouvrez le menu déroulant **Groupe de notification**.

![L'onglet "Paramètres" avec un menu déroulant "Groupe de notification" qui a sélectionné la valeur "Coupons".]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Sélectionnez vos Groupes de notification dans la liste déroulante. Si les paramètres de votre groupe de notifications ne fonctionnent pas correctement ou si vous sélectionnez **Aucun** dans le menu déroulant, le message sera automatiquement envoyé normalement à tous les utilisateurs définis dans l'espace de travail.

Si vous n’avez aucun Groupe de notification listé, vous pouvez en ajouter un à l’aide de l’ID de thread iOS. Vous aurez besoin d’un ID de thread iOS pour chaque groupe de notification que vous souhaitez ajouter. Ensuite, ajoutez-le à vos groupes de notification en cliquant sur **Gérer les groupes de notification** dans le menu déroulant et en remplissant les champs requis dans la fenêtre **Gérer les groupes de notification push iOS** qui apparaît.

![Fenêtre pour gérer les groupes de notification push d'iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Créez votre campagne de notification push iOS, puis regardez en haut du volet de composition. Là, vous verrez un menu déroulant intitulé **Groupes de notification**.

### Arguments récapitulatifs

En plus de regrouper des notifications par ID de thread, Apple vous permet de modifier les récapitulatifs qui apparaissent lorsque les notifications sont groupées. Les utilisateurs de Braze peuvent spécifier la catégorie récapitulative, le nombre de récapitulatifs et l’argument récapitulatif lors de la composition d’une campagne de notifications push à l’aide de notre outil.

{% alert tip %}
Notez que les notifications avec le même ID de thread sont groupées dans le plateau de notification sous le contrôle du système d’exploitation. iOS peut choisir d’afficher des notifications avec le même ID de thread séparément ou en groupes selon ce qu’il juge optimal.
{% endalert %}

Cochez la case **Options d'alerte** dans le **Compositeur de notifications push**.

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

Une fois que cela est configuré sur votre application, utilisez la catégorie de résumé en cochant la case **Notification Buttons** et en sélectionnant **Enter Pre-registered iOS Category**.

Saisissez ensuite l’identifiant de catégorie récapitulative que vous avez définie dans votre application.

### Authentification de notification push provisoire et notifications silencieuses {#provisional-push}

Apple propose aux marques d’envoyer des notifications push discrètes vers les Centres de notification de leurs utilisateurs avant que ceux-ci n’aient officiellement et explicitement donné leur accord, ce qui vous donne l’occasion de tester très tôt la valeur de vos messages. Tout ce que vous avez à faire est de [configurer des notifications push provisoires](#set-up-provisional-push-notifications) dans votre application, puis tout utilisateur disposant d'un jeton push provisoire recevra vos messages.

Contrairement à un jeton de notification push iOS traditionnel, un jeton de notification push provisoire agit comme un « passe provisoire » qui permet aux marques d’atteindre de nouveaux utilisateurs avant qu’ils n’aient vu et cliqué sur la demande d’inscription aux notifications push natives d’Apple. Avec cette fonctionnalité, votre notification push sera envoyée directement à la barre de notification de votre nouvel utilisateur avec l’option « Keep » (Conserver) ou « Turn Off » (Désactiver) les notifications futures. Au lieu de faire l’expérience d’un parcours d’« abonnement », les utilisateurs feront l’expérience de quelque chose qui ressemble plus à un parcours de « désabonnement ».

{% alert tip %}
L’autorisation provisoire a le potentiel d’augmenter considérablement votre taux d’abonnement, mais seulement si les utilisateurs apprécient la valeur dans vos messages. Assurez-vous d'utiliser nos fonctionnalités de [segmentation des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), de [ciblage géographique]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) et de [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) pour garantir que les utilisateurs appropriés reçoivent ces notifications de "test" au bon moment. Ensuite, vous pouvez encourager les utilisateurs à s’abonner à vos notifications push, sachant qu’ils ajoutent de la valeur à l’expérience de vos utilisateurs avec votre application.
{% endalert %}

Quelle que soit l'option choisie par l'utilisateur, elle ajoutera le jeton approprié ou [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) à leurs [Paramètres de contact]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) sous l'onglet **Engagement** dans leur profil utilisateur.

![Paramètres de contact avec un statut abonné push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Vous pourrez cibler vos utilisateurs en fonction de leur autorisation provisoire ou non en utilisant nos [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

![Panneau de détails du segment avec le filtre de segment d'échantillon « Autorisé provisoirement sur iOS Stopwatch (iOS) est vrai » pour cibler les utilisateurs.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si les utilisateurs choisissent de « désactiver » vos notifications push provisoires, ils ne verront plus de messages push provisoires de votre part. Soyez attentif au contenu et à la fréquence des messages envoyés via cette fonctionnalité !
{% endalert %}

{% alert important %}
Si vous utilisez des invites push supplémentaires ou des [incitations push dans l'application](https://www.braze.com/resources/glossary/priming-for-push/) (un message dans l'application qui encourage les utilisateurs à accepter les notifications push), contactez votre représentant Braze pour obtenir des conseils supplémentaires.
{% endalert %}

#### Configurer des notifications push provisoires

Braze vous permet de vous inscrire à l'authentification provisoire en mettant à jour votre code dans votre extrait d'enregistrement de jeton au sein de votre implémentation du SDK iOS de Braze en utilisant les extraits suivants comme exemple (envoyez-les à vos développeurs ou assurez-vous qu'ils [mettent en œuvre l'authentification push provisoire pendant le processus d'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
La mise en œuvre de l’authentification de notification push provisoire prend uniquement en charge iOS 12+ et renvoie une erreur si la cible du déploiement est antérieure. Pour en savoir plus à ce sujet, consultez [notre documentation détaillée sur l’implémentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
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
  {% tab Objectif-C %}

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

Avec le nouveau mode Focus d’iOS 15, les utilisateurs contrôlent mieux le moment où les notifications des applications peuvent les « interrompre » par un son ou une vibration.

![Page des paramètres de notification iOS qui montre les notifications activées pour une livraison immédiate et avec les notifications sensibles au temps activées.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Les applications peuvent maintenant spécifier le niveau d’interruption d’une notification, en fonction de son urgence.

Pour changer le niveau d'interruption pour une notification push iOS, sélectionnez l'onglet **Paramètres** et choisissez le niveau souhaité dans le menu déroulant **Niveau d'interruption**.

![Liste déroulante permettant de sélectionner le niveau d'interruption.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Cette fonctionnalité n’a pas de configuration minimale requise pour la version SDK, mais est uniquement appliquée pour les appareils exécutant iOS 15+.

Gardez à l’esprit que les utilisateurs sont en fin de compte les maîtres de leur intérêt, et même si une notification temporelle (Time Sensitive) est livrée, ils peuvent spécifier quelles applications ne sont pas autorisées à interrompre leur intérêt.

Reportez-vous au tableau suivant pour connaître les niveaux d’interruption et leurs descriptions.

|Niveau d’interruption|Description|Quand l’utiliser|Mode Break Through Focus|
|--|--|--|--|
|[Neutre](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Envoie une notification sans son, vibration ni éclairage de l’écran.|Notifications qui ne nécessitent pas d’attention immédiate.|Non|
|[Actif](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (par défaut)|Émet juste un son, une vibration et éclaire l’écran si l’utilisateur n’est pas en mode Focus.|Notifications nécessitant une attention immédiate, sauf si l’utilisateur a activé le mode Focus.|Non|
|[Time Sensitive (Temporel)](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|Émet un son, une vibration et éclaire l’écran même si l’utilisateur est en mode Focus. Pour ceci, la **fonction de notifications temporelles** doit être ajoutée à votre application dans Xcode.|Des notifications opportunes qui devraient interrompre les utilisateurs indépendamment de leur mode Focus, comme un trajet ou une notification de livraison.|Oui|
|[Critical (Critique)](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Émettra un son, vibrera et allumera l'écran même si le commutateur **Ne Pas Déranger** du téléphone est activé. Ceci [nécessite l'approbation explicite d'Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Urgences telles que des alertes météorologiques ou de sécurité graves|Oui|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Score de pertinence (iOS 15+) {#relevance-score}

![Un résumé des notifications pour iOS intitulé "Votre résumé du soir" avec trois notifications.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 introduit également un nouveau moyen pour les utilisateurs de planifier de manière facultative un regroupement de plusieurs notifications à des moments désignés de la journée. Cela permet d’éviter les interruptions constantes tout au long de la journée pour des notifications qui ne nécessitent pas une attention immédiate.

Les applications peuvent spécifier quelles notifications push sont les plus pertinentes en définissant un **score de pertinence**. Apple utilisera ce score pour déterminer quelles notifications doivent être mises en avant dans le récapitulatif des notifications planifiées, tandis que d’autres sont rendues accessibles lorsque les utilisateurs cliquent dans le récapitulatif. 

Toutes les notifications seront toujours accessibles dans le centre de notification de l’utilisateur.

Pour définir le score de pertinence d'une notification iOS, entrez une valeur entre `0.0` et `1.0` dans l'onglet **Paramètres**. Par exemple, le message le plus important doit être envoyé avec `1.0`, alors qu’un message d’importance moyenne peut être envoyé avec `0.5`.

![Score de pertinence de "0.5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Cette fonctionnalité n’a pas de configuration minimale requise pour la version SDK, mais est uniquement appliquée pour les appareils exécutant iOS 15+.

Pour plus d’informations sur les longueurs maximales des messages selon les différents types de messages, reportez-vous aux ressources suivantes :

- [Spécifications de l’image et du texte]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Directives de comptage des caractères iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

