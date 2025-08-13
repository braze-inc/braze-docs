---
nav_title: "Activation et abonnement aux notifications push"
article_title: Activation et abonnement aux notifications push
page_order: 3
page_type: reference
description: "Cet article de référence couvre les concepts des états Activé pour les notifications push et Abonnement aux notifications push dans Braze, y compris les différences fondamentales de comportement sur iOS, Android et Web."
channel:
  - push

---

# Activation et abonnement aux notifications push

> Cet article de référence couvre les concepts des statuts Activé pour les notifications push et Abonnement aux notifications push dans Braze, y compris les différences fondamentales de comportement sur iOS, Android et Web.

## Statuts d’abonnement aux notifications push {#push-sub-states}

Un "état d'abonnement push" dans Braze identifie la préférence globale d'un **utilisateur** quant à son souhait de recevoir des notifications push. Étant donné que le statut d’abonnement est basé sur l’utilisateur, il n’est pas spécifique à une application donnée. Les états de l’abonnement deviennent des indicateurs utiles lorsque vous décidez quels utilisateurs cibler avec les notifications push.

{% alert note %}
L’état de l’abonnement aux notifications push d’un utilisateur s’applique à l’ensemble de son profil utilisateur, ce qui inclut tous les appareils de celui-ci.
{% endalert %}

Il existe trois options d’état de l’abonnement aux notifications push : `Subscribed`, `Opted-In` et `Unsubscribed`.

Par défaut, pour que votre utilisateur reçoive vos messages via push, l'état de son abonnement à push doit être `Subscribed` ou `Opted-In`, et il doit être [activé pour push](#push-enabled). Vous pouvez écraser cette configuration si nécessaire lors de la rédaction d’un message.

|État autorisé|Description|
|---|---|
|`Subscribed`| État d’abonnement aux notifications push par défaut lorsqu’un profil utilisateur est créé dans Braze. |
|`Opted-In`| Un utilisateur a explicitement exprimé une préférence pour recevoir des notifications push. Braze déplace automatiquement l’état inscrit d’un utilisateur vers `Opted-In` si celui-ci accepte une invite de notification push au niveau du système d’exploitation.<br><br>Ceci ne s’applique pas aux utilisateurs d’Android 12 ou antérieur.|
|`Unsubscribed`| Un utilisateur s’est explicitement désabonné des notifications push par le biais de votre application ou d’autres méthodes fournies par votre marque. Par défaut, les campagnes de notification push de Braze ciblent uniquement les utilisateurs qui sont `Subscribed` ou `Opted-in` pour les notifications push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze ne change pas automatiquement le statut de l’abonnement aux notifications push d’un utilisateur vers `Unsubscribed`. Souvenez-vous que si le statut de l’abonnement aux notifications push d’un utilisateur est `Unsubscribed`, alors le filtre `Push Enabled` de l’utilisateur dans la segmentation sera `false`.
{% endalert %}

### Mise à jour des états d’abonnement aux notifications push {#update-push-subscription-state}

Vous pouvez mettre à jour l'état de l'abonnement push d'un utilisateur de trois manières différentes :

#### Abonnement automatique (par défaut)

Par défaut, Braze définit l'état de l'abonnement push d'un utilisateur sur `Opted-In` lorsqu'il autorise pour la première fois les notifications push pour votre application. Braze procède également de la sorte lorsqu'un utilisateur réactive les autorisations push dans les paramètres de son système après les avoir précédemment désactivées.

{% tabs local %}
{% tab android %}
Pour désactiver ce comportement par défaut, ajoutez la propriété suivante au fichier `braze.xml` de votre projet Android Studio :

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
À partir de la [version 7.5.0 du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), vous pouvez désactiver ou personnaliser davantage ce comportement en ajoutant la configuration `optInWhenPushAuthorized` au fichier `AppDelegate.swift` de votre projet Xcode :

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### Intégration SDK

Vous pouvez mettre à jour l'état de l'abonnement d'un utilisateur avec le SDK de Braze à l'aide de la méthode `setPushNotificationSubscriptionType` sur le [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS.](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)) Par exemple, vous pouvez utiliser cette méthode pour créer une page de paramètres dans votre appli où les utilisateurs peuvent activer ou désactiver manuellement les notifications push.

#### API REST

Vous pouvez mettre à jour l'état de l'abonnement d'un utilisateur avec l'API REST de Braze en utilisant l' [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour l'attribut [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) attribut.

### Vérifier le statut de l’abonnement aux notifications push

![Profil utilisateur de John Doe dont l'état de l'abonnement push est défini sur Abonné.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l’état de l’abonnement aux notifications push d’un utilisateur avec Braze :

1. **Profil utilisateur**: Vous pouvez accéder aux profils utilisateurs individuels via le tableau de bord de Braze dans la rubrique **[Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** de Braze. Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID externe), vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état de l'abonnement d'un utilisateur.
<br><br>
2. **Exportation de l'API REST**: Vous pouvez exporter des profils utilisateurs individuels au format JSON à l'aide des endpoints d'exportation [Utilisateurs par segmentation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze renvoie un objet jeton de notification push qui contient des informations sur l’activation de la notification par appareil.

## Autorisation des notifications push

Toutes les plateformes autorisant les notifications push (iOS, Web et Android) demandent un abonnement explicite à l’aide d’une invite au niveau du système d’exploitation, avec quelques différences décrites ci-dessous.

Parce que la décision d'un utilisateur est définitive et que vous ne pouvez pas lui demander à nouveau après son refus, l'utilisation de messages in-app d ['amorçage push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) est une stratégie importante pour augmenter vos taux d'abonnement.

**Invites pour autoriser les notifications push natives du système d’exploitation**

|Plateforme|Capture d’écran|Description|
|--|--|--|
|iOS| ![Une invite push native iOS demandant "Mon application souhaite vous envoyer des notifications" avec deux boutons, "Ne pas autoriser" et "Autoriser" en bas du message.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}).{: style="max-width:410px;"} | Cette disposition ne s'applique pas aux demandes d'[autorisation provisoire de notifications push](#provisional-push).|
|Android| ![Un message push Android demandant "Autorisez Kitchenerie à vous envoyer des notifications" avec deux boutons, "Autoriser" et "Ne pas autoriser" au bas du message.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Cette autorisation des notifications push a été introduite avec Android 13. Avant Android 13, il n’était pas nécessaire de demander l’autorisation pour envoyer une notification push.|
|Web| ![L'invite push native d'un navigateur web demandant "Braze.com veut afficher une notification" avec deux boutons, "Bloquer" et "Autoriser" au bas du message.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Avant Android 13, il n’était pas nécessaire de demander l’autorisation pour envoyer des notifications push. Sur Android 12 et antérieures, tous les utilisateurs étaient considérés comme étant `Subscribed` lors de leur première session lorsque Braze demande automatiquement un jeton de notification push. À ce stade, **les notifications push sont activées** pour l’utilisateur, avec un jeton de notification push valide pour cet appareil et un état d'abonnement par défaut défini sur `Subscribed`.

À partir d'[Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/), l'autorisation de pousser doit être demandée et accordée par l'utilisateur. Votre application peut demander manuellement l'autorisation à l'utilisateur au moment opportun, mais si ce n'est pas le cas, les utilisateurs seront automatiquement invités à le faire lorsque votre application créera un [canal de notification.](https://developer.android.com/reference/android/app/NotificationChannel)

### iOS

![Une notification dans le centre de notification du système avec un message en bas demandant "Continuer à recevoir des notifications de l'appli Yachtr ?" avec deux boutons en dessous pour "Garder" ou "Désactiver"]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}).{: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Votre application peut demander des notifications push provisoires ou autorisées. 

Le push autorisé requiert l'autorisation explicite d'un utilisateur avant d'envoyer toute notification, tandis que le [push provisoire](https://www.braze.com/resources/articles/mastering-provisional-push) vous permet d'envoyer des notifications __discrètement__, directement dans le centre de notification, sans aucun son ni alerte.

#### Autorisation provisoire et notifications push silencieuses {#provisional-push}

Avant iOS 12 (sorti en 2018), tous les utilisateurs devaient s’abonner explicitement pour recevoir des notifications push.

Dans iOS 12, Apple a introduit l' [autorisation provisoire](https://www.braze.com/resources/articles/mastering-provisional-push), permettant aux marques d'envoyer des notifications push discrètes dans le centre de notification de leurs utilisateurs avant qu'ils n'aient explicitement choisi l'abonnement, ce qui vous donne une chance de démontrer la valeur de vos messages très tôt. Pour en savoir plus, reportez-vous à l'[autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications).

### Web

Pour le Web, vous devez demander un abonnement explicite de l’utilisateur à l’aide du dialogue d’autorisation natif du navigateur.

Contrairement à Android et iOS qui laissent votre application afficher le dialogue d’autorisation n’importe quand, certains navigateurs modernes n’afficheront l’invite que si elle est déclenchée par une action de l’utilisateur (clic de souris ou touche du clavier). Si votre site essaie de demander une autorisation de notification push lors du chargement de la page, elle sera sûrement ignorée ou étouffée par le navigateur.

De ce fait, vous ne devriez demander l’autorisation que quand l’utilisateur clique quelque part sur votre site Internet et pas au hasard, lors du chargement d’une page.

## Jetons de notification push

Les [jetons push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) sont un identifiant anonyme unique généré par l'appareil d'un utilisateur et envoyé à Braze pour identifier où envoyer la notification de chaque destinataire.

Il existe deux façons de classer un [jeton push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) qui sont essentielles pour comprendre comment une notification push peut être envoyée à vos utilisateurs.

1. **Foreground push** permet d'envoyer régulièrement des notifications push visibles au premier plan de l'appareil d'un utilisateur.
2. Le **push en arrière-plan** est disponible indépendamment du fait qu'un appareil particulier ait choisi de recevoir des notifications push de cette marque. Le push en arrière-plan permet aux marques d'envoyer des notifications push silencieuses - des notifications qui ne sont intentionnellement pas affichées - aux appareils pour prendre en charge des fonctionnalités clés telles que le [suivi de la désinstallation]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Lorsqu’un profil d’utilisateur est associé à un jeton de notification push de premier plan valide associé à une application, Braze considère que l’utilisateur est « push registered » (abonné aux notifications push) pour l’application donnée. Braze fournit alors un filtre de segmentation spécifique, `Push Enabled for App,`, pour identifier ces utilisateurs.

{% alert note %}
Le filtre `Push Enabled for App` prend uniquement en compte la présence d’un jeton de notification push de premier plan ou d’arrière-plan valide pour l’application donnée. Cependant, le filtre plus générique [`Push Enabled`](#push-enabled) segmente les utilisateurs qui ont explicitement activé les notifications push pour toutes les applications de votre espace de travail. Ce nombre inclut uniquement les notifications push de premier plan et n’inclut pas les utilisateurs qui se sont désabonnés. Pour en savoir plus sur ces filtres et d'autres, consultez la rubrique [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Plusieurs utilisateurs sur un appareil

Les jetons de notification push sont spécifiques pour un appareil et une application, il n’est donc pas possible d’utiliser des jetons de notification push pour différencier plusieurs utilisateurs utilisant le même appareil.

Imaginons par exemple que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre application sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecte au sien, le jeton de notification push sera réaffecté au profil de Kim. Le jeton de notification push restera affecté au profil de Kim sur cet appareil jusqu’à ce qu’elle se déconnecte et que Charlie se reconnecte.

Une application ou un site Internet ne peuvent avoir qu’un seul abonnement aux notifications push par appareil. Lorsqu’un utilisateur se déconnecte d’un appareil ou d’un site Internet et qu’un utilisateur se connecte, le jeton de notification push est donc réaffecté au nouvel utilisateur. Cela se reflète sur le profil de l'utilisateur, dans la section **Paramètres de contact** de l'onglet **Engagement :** 

![Journal des modifications du jeton de poussée dans l'onglet \*\*Engagement** du profil d'un utilisateur, qui indique quand le jeton de poussée a été transféré à un autre utilisateur, et quel était le jeton.]({% image_buster /assets/img/push_token_changelog.png %})

Étant donné que les fournisseurs de notifications push (APN/FCM) n’ont aucun moyen de faire la différence entre plusieurs utilisateurs sur un même appareil, nous transmettons le jeton de notification push au dernier utilisateur qui s’est connecté pour déterminer quel utilisateur cibler sur l’appareil pour les notifications push.

### Plusieurs appareils et un seul utilisateur

Le statut d’abonnement aux notifications push est basé sur l’utilisateur et n’est pas spécifique à une application donnée. L’état de l’abonnement aux notifications push est la dernière valeur définie. Ainsi, si un utilisateur s’est abonné aux notifications push, son statut d’abonnement est `Opted-in` sur tous les appareils éligibles. Si, par la suite, un utilisateur se désabonne explicitement des notifications push par le biais de votre application ou d'autres méthodes proposées par votre marque, l'état de son abonnement push est mis à jour sur `Unsubscribed` et aucun appareil inscrit à push ne peut recevoir de notifications push.

## Filtre notifications push activées {#push-enabled}

`Push Enabled` est un filtre de segmentation dans Braze qui permet aux spécialistes du marketing d’identifier facilement les utilisateurs qui permettent à Braze d’envoyer des notifications push et les utilisateurs qui n’ont pas exprimé leurs préférences pour ne pas recevoir de notifications push. 

Le filtre `Push Enabled` tient compte des éléments suivants :
- La capacité de Braze à envoyer une notification push (jeton de notification push de premier plan)
- Les préférences générales de l’utilisateur concernant la réception de notifications push sur ses appareils (statut d’abonnement aux notifications push)

![Une capture d'écran du tableau de bord montrant qu'un utilisateur est "Push Registered for Marketing (iOS)"]({% image_buster /assets/img/push_enablement.png %}).{: style="float:right;max-width:50%;margin-left:15px;"}

Un utilisateur est considéré comme "activé par push" ou "enregistré par push" s'il dispose d'un jeton push actif au premier plan pour une application au sein de votre espace de travail, ce qui signifie que le statut d'activation de push est spécifique à l'application. 

{% alert note %}
Pour savoir comment vérifier l'état de l'enregistrement des notifications push, consultez la section [Statut d’enregistrement des notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)
{% endalert %}

## Autres scénarios dépendant de la plateforme

{% tabs %}
{% tab Android %}

Si un utilisateur activé pour les notifications push de premier plan désactive les notifications push dans les paramètres de son système d’exploitation, alors, au démarrage de la prochaine session :
- Braze marque ces utilisateurs comme ayant désactivé les notifications push de premier plan et ne tente plus de leur envoyer des messages push.
- Le filtre `Push Enabled for App (Android)` et le filtre de segmentation `Push Enabled` (en supposant qu’aucune autre application sur le profil utilisateur ne possède un jeton de notification push de premier plan valide) renvoient `false`.

Dans ce scénario, étant donné qu’un jeton de notification push d’arrière-plan existe toujours, vous pouvez continuer à envoyer des notifications push d’arrière-plan (silencieuses) avec le filtre de segmentation `Background Push Enabled = true`.

Pour Android, Braze considère un utilisateur comme ayant désactivé les notifications push si :

- Un utilisateur désinstalle l’application de son appareil.
- Un message de notification push n’est pas livré en raison d’un bounce. Ceci est généralement dû à une désinstallation, mais peut également découler d’une mise à jour de l’application, d’une nouvelle version de jeton de notification push ou du format. 
- L’inscription de la notification push échoue au niveau de Firebase Cloud Messaging (parfois causé par de mauvaises connexions réseau ou une incapacité à se connecter à ou sur FCM pour renvoyer un jeton valide).
- L’utilisateur bloque les notifications push pour l’application dans les paramètres de son appareil et ouvre ensuite une session.

{% endtab %}
{% tab iOS %}

Qu'un utilisateur accepte ou non la demande d'abonnement au push en avant-plan, vous pourrez toujours envoyer un push en arrière-plan si les notifications à distance sont activées dans Xcode et que votre application appelle [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Si votre application est provisoirement autorisée ou que l’utilisateur a autorisé les notifications push, il reçoit un jeton de notification push de premier plan, ce qui vous permet de lui envoyer tous les types de notification push. Dans Braze, nous considérons un utilisateur sur iOS, qui est activé pour les notifications push de premier plan, comme étant activé pour les notifications push, soit explicitement (au niveau de l’application), soit provisoirement (au niveau de l’appareil).

Si un utilisateur refuse de recevoir des notifications push au niveau du système d’exploitation, l’état de son abonnement sera `Subscribed` et son profil ne montrera pas qu’un jeton de notification push de premier plan a été inscrit. 

Dans le cas d’un utilisateur, qui a initialement autorisé les notifications push au niveau du système d’exploitation, puis qui les désactive dans les paramètres de son système d’exploitation, au démarrage de la session suivante, les événements suivants se produisent :
- Braze marque ces utilisateurs comme ayant désactivé les notifications push de premier plan et ne tente plus d’envoyer des messages push.
- Le filtre `Push Enabled for App (iOS)` et le filtre de segmentation `Push Enabled` (en supposant qu’aucune autre application sur le profil utilisateur ne possède un jeton de notification push de premier plan valide) renvoient `false`.

Dans ce scénario, étant donné qu’un jeton de notification push d’arrière-plan existe toujours, vous pouvez continuer à envoyer des notifications push d’arrière-plan (silencieuses) avec le filtre de segmentation `Background Push Enabled = true`.

{% endtab %}
{% tab Web %}

Lorsqu’un utilisateur accepte la demande d’autorisation des notifications push natives, son statut d’abonnement passera sur `opted in`.

Pour gérer les abonnements, vous pouvez utiliser la méthode utilisateur [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) pour créer une page de paramètres de préférences sur votre site, après quoi vous pouvez filtrer les utilisateurs par statut d'abonnement dans le tableau de bord.

Si un utilisateur désactive les notifications dans son navigateur, la prochaine notification push envoyée à cet utilisateur sera refusée et Braze mettra à jour le jeton de l’utilisateur en conséquence. Ceci permet de gérer l’éligibilité des filtres pour l’activation des notifications push (`Background Push Enabled`, `Push Enabled` et `Push Enabled for App`). L’état de l’abonnement défini sur le profil utilisateur est un paramètre de niveau utilisateur et ne change pas lorsqu’une notification push est renvoyée.

{% alert note %}
Les plateformes Web n’autorisent pas les notifications push en arrière-plan ou silencieuses.
{% endalert %}
{% endtab %}
{% endtabs %}

## Bonnes pratiques

Consultez notre article dédié aux [meilleures pratiques en matière de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) pour obtenir des conseils détaillés sur la manière d'optimiser votre utilisation du push chez Braze.

