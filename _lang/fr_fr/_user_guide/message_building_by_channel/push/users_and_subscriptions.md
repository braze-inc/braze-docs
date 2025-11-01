---
nav_title: "Activation de la poussée et de l'abonnement"
article_title: Activation de la poussée et abonnement
page_order: 3
page_type: reference
description: "Cet article de référence couvre les concepts d'états de push enabled et de push subscription dans Braze, y compris les différences fondamentales de comportement entre iOS, Android et le web."
channel:
  - push

---

# Activation du push et abonnement au push

> Cet article de référence couvre les concepts de l'activation du push et des états d'abonnement au push dans Braze, y compris les différences fondamentales de comportement entre iOS, Android et le Web.

## États de l'abonnement en mode push {#push-sub-states}

Un "état d'abonnement push" dans Braze identifie la préférence globale d'un **utilisateur** quant à son souhait de recevoir des notifications push. L'état de l'abonnement étant basé sur l'utilisateur, il n'est pas spécifique à une application particulière. Les états d'abonnement deviennent des indicateurs utiles lorsqu'il s'agit de décider quels utilisateurs cibler pour les notifications push.

{% alert note %}
L'état de l'abonnement push d'un utilisateur s'applique à l'ensemble de son profil utilisateur, qui comprend tous les appareils de l'utilisateur.
{% endalert %}

Il existe trois options d'état d'abonnement push : `Subscribed`, `Opted-In`, et `Unsubscribed`.

Par défaut, pour que votre utilisateur reçoive vos messages via push, l'état de son abonnement à push doit être `Subscribed` ou `Opted-In`, et il doit être [activé pour push](#foreground-push-enabled). Vous pouvez remplacer ce paramètre si nécessaire lors de la rédaction d'un message.

|État d'abonnement|Description|
|---|---|
|`Subscribed`| État de l'abonnement push par défaut lorsqu'un profil utilisateur est créé dans Braze. |
|`Opted-In`| Un utilisateur a explicitement exprimé sa préférence pour recevoir des notifications push. Braze fait automatiquement passer la demande d'abonnement d'un utilisateur à `Opted-In` s'il accepte une invitation à pousser au niveau du système d'exploitation.<br><br>Cela ne s'applique pas aux utilisateurs d'Android 12 ou d'une version inférieure.|
|`Unsubscribed`| Un utilisateur s'est explicitement désabonné de push via votre application ou d'autres méthodes proposées par votre marque. Par défaut, les campagnes de push de Braze ne ciblent que les utilisateurs qui sont `Subscribed` ou `Opted-in` pour le push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze ne modifie pas automatiquement l'état de l'abonnement push d'un utilisateur à `Unsubscribed`. Rappelez-vous que si l'état de l'abonnement push d'un utilisateur est `Unsubscribed`, le filtre `Foreground Push Enabled` de l'utilisateur dans la segmentation sera `false`.
{% endalert %}

### Mise à jour de l'état des abonnements push {#update-push-subscription-state}

Vous pouvez mettre à jour l'état de l'abonnement push d'un utilisateur de trois manières différentes :

#### Abonnement automatique (par défaut)

Par défaut, Braze définit l'état de l'abonnement push d'un utilisateur sur `Opted-In` lorsqu'il autorise pour la première fois les notifications push pour votre application. Braze procède également de la sorte lorsqu'un utilisateur réactive les autorisations push dans les paramètres de son système après les avoir précédemment désactivées.

{% tabs local %}
{% tab android %}
Pour désactiver ce comportement par défaut, ajoutez la propriété suivante au fichier `braze.xml` de votre projet Android Studio :

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
À partir de la [version 7.5.0 du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), vous pouvez désactiver ou personnaliser davantage ce comportement en ajoutant la configuration `optInWhenPushAuthorized` au fichier `AppDelegate.swift` de votre projet Xcode :

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### Intégration SDK

Vous pouvez mettre à jour l'état de l'abonnement d'un utilisateur avec le SDK de Braze à l'aide de la méthode `setPushNotificationSubscriptionType` sur le [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Par exemple, vous pouvez utiliser cette méthode pour créer une page de paramètres dans votre appli où les utilisateurs peuvent activer ou désactiver manuellement les notifications push.

#### API REST

Vous pouvez mettre à jour l'état de l'abonnement d'un utilisateur avec l'API REST de Braze en utilisant l' [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour l'attribut [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) attribut.

### Vérification de l'état de l'abonnement à Push

\![Profil utilisateur de John Doe dont l'état de l'abonnement push est défini sur Abonné.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l'état de l'abonnement push d'un utilisateur avec Braze :

1. **Profil utilisateur** Vous pouvez accéder aux profils utilisateurs individuels par le biais du tableau de bord de Braze dans la rubrique **[Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** de Braze. Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID externe), vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état de l'abonnement d'un utilisateur.
2. **Exportation de l'API REST :** Vous pouvez exporter des profils utilisateurs individuels au format JSON en utilisant les endpoints d'exportation [Utilisateurs par segmentation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze renvoie un objet de jetons de poussée qui contient des informations sur l'activation de la poussée pour chaque appareil.

## Permission de pousser

Toutes les plateformes compatibles avec le push - iOS, Web et Android - exigent un abonnement explicite via une demande d'abonnement au niveau du système d'exploitation, avec quelques légères différences décrites ci-dessous.

Parce que la décision d'un utilisateur est définitive et que vous ne pouvez pas lui demander à nouveau après son refus, l'utilisation de messages in-app d ['amorçage push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) est une stratégie importante pour augmenter vos taux d'abonnement.

**Invitations à l'autorisation de pousser le système d'exploitation natif**

|Plateforme|Capture d'écran|Description|
|--|--|--|
|iOS| \![Une invite push native iOS demandant "Mon application souhaite vous envoyer des notifications" avec deux boutons, "Ne pas autoriser" et "Autoriser" en bas du message.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Cette disposition ne s'applique pas aux demandes d'autorisation [provisoire](#provisional-push) de [pousser](#provisional-push).|
|Android| Un message push Android demandant "Allow Kitchenerie to send you notifications ?" avec deux boutons, "Allow" et "Don't allow" au bas du message.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Cette autorisation de pousser a été introduite dans Android 13. Avant Android 13, l'autorisation n'était pas nécessaire pour envoyer des messages push.|
|Web| Une invite push native d'un navigateur web demandant "Braze.com veut afficher une notification" avec deux boutons, "Bloquer" et "Autoriser" au bas du message.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Avant Android 13, l'autorisation n'était pas nécessaire pour envoyer des notifications push. Sur Android 12 et les versions inférieures, tous les utilisateurs sont considérés comme `Subscribed` lors de leur première session lorsque Braze demande automatiquement un jeton de poussée. À ce stade, l'utilisateur est **activé par push** avec un jeton push valide pour cet appareil et un état d'abonnement par défaut de `Subscribed`.

À partir d'[Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/), l'autorisation de pousser doit être demandée et accordée par l'utilisateur. Votre application peut demander manuellement l'autorisation à l'utilisateur au moment opportun, mais si ce n'est pas le cas, les utilisateurs seront automatiquement invités à le faire lorsque votre application créera un [canal de notification.](https://developer.android.com/reference/android/app/NotificationChannel)

### iOS

Une notification dans le centre de notification du système avec un message in-app demandant "Continuer à recevoir des notifications de l'application Yachtr" avec deux boutons en dessous pour "Garder" ou "Désactiver".]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Votre application peut demander un push provisoire ou un push autorisé. 

Le push autorisé requiert l'autorisation explicite d'un utilisateur avant d'envoyer toute notification, tandis que le [push provisoire](https://www.braze.com/resources/articles/mastering-provisional-push) vous permet d'envoyer des notifications __discrètement__, directement dans le centre de notification, sans aucun son ni alerte.

#### Autorisation provisoire et "quiet push {#provisional-push}

Avant iOS 12 (sorti en 2018), tous les utilisateurs doivent explicitement opter pour recevoir des notifications push.

Dans iOS 12, Apple a introduit l' [autorisation provisoire](https://www.braze.com/resources/articles/mastering-provisional-push), permettant aux marques d'envoyer des notifications push discrètes dans le centre de notification de leurs utilisateurs avant qu'ils n'aient explicitement choisi l'abonnement, ce qui vous donne une chance de démontrer la valeur de vos messages très tôt. Pour en savoir plus, reportez-vous à l'[autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications).

### Web

Pour le navigateur web, vous devez demander l'abonnement explicite de l'utilisateur via la boîte de dialogue d'autorisation du navigateur.

Contrairement à iOS et Android, qui permettent à votre application d'afficher l'invite de permission à tout moment, certains navigateurs modernes n'affichent l'invite que si elle est déclenchée par un "geste de l'utilisateur" (clic de souris ou frappe au clavier). Si votre site tente de demander l'autorisation de la notification push au chargement de la page, il sera probablement ignoré ou réduit au silence par le navigateur.

Par conséquent, vous ne devez demander une autorisation que lorsqu'un utilisateur clique quelque part sur votre site web et non pas au hasard lors du chargement d'une page.

## Jetons de poussée

Les [jetons push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) sont un identifiant anonyme unique généré par l'appareil d'un utilisateur et envoyé à Braze pour identifier où envoyer la notification de chaque destinataire.

Il existe deux façons de classer un [jeton push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) qui sont essentielles pour comprendre comment une notification push peut être envoyée à vos utilisateurs.

1. **Foreground push** permet d'envoyer régulièrement des notifications push visibles au premier plan de l'appareil d'un utilisateur.
2. Le **push en arrière-plan** est disponible indépendamment du fait qu'un appareil donné ait choisi de recevoir des notifications push de cette marque. Le push en arrière-plan permet aux marques d'envoyer des notifications push silencieuses - des notifications qui ne sont intentionnellement pas affichées - aux appareils pour prendre en charge des fonctionnalités clés telles que le [suivi de la désinstallation]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Lorsqu'un profil utilisateur dispose d'un jeton push de premier plan valide associé à une application, Braze considère que l'utilisateur est "inscrit au push" pour l'application donnée. Braze propose donc un filtre de segmentation spécifique, `Foreground Push Enabled for App,`, pour aider à identifier ces utilisateurs.

{% alert note %}
Le filtre `Foreground Push Enabled for App` ne prend en compte que la présence d'un jeton de push de premier plan et d'arrière-plan valide pour l'application donnée. Cependant, le filtre plus générique [`Foreground Push Enabled`](#foreground-push-enabled) plus générique, segmente les utilisateurs qui ont explicitement activé les notifications push pour toutes les applications de votre espace de travail. Ce décompte ne tient compte que des poussées en avant-plan et n'inclut pas les utilisateurs qui se sont désinscrits. Pour en savoir plus sur ces filtres et d'autres, consultez la rubrique [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Plusieurs utilisateurs sur un même appareil

Les jetons push sont spécifiques à un appareil et à une application. Il n'est donc pas possible d'utiliser les jetons push pour distinguer plusieurs utilisateurs utilisant le même appareil.

Par exemple, supposons que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre appli sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecter au sien, le jeton push sera réattribué au profil de Kim. Le jeton push restera alors attribué au profil de Kim sur cet appareil jusqu'à ce qu'elle se déconnecte et que Charlie se reconnecte.

Une appli ou un site web ne peut avoir qu'un seul abonnement push par appareil. Ainsi, lorsqu'un utilisateur se déconnecte d'un appareil ou d'un site web et qu'un nouvel utilisateur s'y connecte, le jeton push est réattribué au nouvel utilisateur. Cela se reflète sur le profil de l'utilisateur, dans la section **Paramètres de contact** de l'onglet **Engagement**:

Journal des modifications du jeton de poussée dans l'onglet \*\*Engagement** du profil d'un utilisateur, qui indique quand le jeton de poussée a été transféré à un autre utilisateur, et quel était le jeton.]({% image_buster /assets/img/push_token_changelog.png %})

Comme les fournisseurs de services de push (APN/FCM) n'ont aucun moyen de faire la distinction entre plusieurs utilisateurs sur un même appareil, nous transmettons le jeton de push au dernier utilisateur connecté afin de déterminer quel utilisateur doit être ciblé sur l'appareil pour le push.

### Plusieurs appareils et un seul utilisateur

L'état de l'abonnement push est basé sur l'utilisateur et n'est pas spécifique à une application individuelle. L'état de l'abonnement push est la dernière valeur définie. Ainsi, si un utilisateur a opté pour les notifications push, l'état de son abonnement push est `Opted-in` sur tous les appareils éligibles. Si, par la suite, un utilisateur se désabonne explicitement des notifications push par le biais de votre application ou d'autres méthodes proposées par votre marque, l'état de son abonnement push est mis à jour sur `Unsubscribed` et aucun appareil inscrit à push ne peut recevoir de notifications push.

## Filtre Foreground Push Enabled {#foreground-push-enabled}

`Foreground Push Enabled` est un filtre de segmentation dans Braze qui permet aux marketeurs d'identifier facilement les utilisateurs qui autorisent Braze à envoyer des notifications push et les utilisateurs qui n'ont pas exprimé de préférences pour ne pas recevoir de notifications push. 

Le filtre `Foreground Push Enabled` tient compte des éléments suivants :
- La possibilité pour Braze d'envoyer une notification push (jeton de push au premier plan).
- La préférence globale de l'utilisateur pour recevoir des push sur n'importe lequel de ses appareils (état de l'abonnement aux push).

\![Une capture d'écran du tableau de bord montrant qu'un utilisateur est "Push Registered for Marketing (iOS)".]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Un utilisateur est considéré comme "activé par push" ou "enregistré par push" s'il dispose d'un jeton push actif au premier plan pour une application au sein de votre espace de travail, ce qui signifie que le statut d'activation de push est spécifique à l'application. 

{% alert note %}
Pour savoir comment vérifier l'état de l'enregistrement push, consultez la page [état de l'enregistrement push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)
{% endalert %}

## Autres scénarios spécifiques aux plates-formes

{% tabs %}
{% tab Android %}

Si un utilisateur ayant activé le push au premier plan désactive le push dans les paramètres de son système d'exploitation, il le fera au début de la session suivante :
- Braze les marque comme étant désactivés par push au premier plan et ne tente plus de leur envoyer des messages push.
- Le filtre `Foreground Push Enabled for App (Android)` et le filtre de segmentation `Foreground Push Enabled` (en supposant qu'aucune autre application sur le profil utilisateur ne dispose d'un jeton de poussée au premier plan valide) renverront `false`.

Dans ce scénario, étant donné qu'un jeton push en arrière-plan existera toujours, vous pouvez continuer à envoyer des notifications push en arrière-plan (silencieuses) avec le filtre de segmentation `Background or Foreground Push Enabled = true`.

Pour Android, Braze considérera qu'un utilisateur a désactivé le push si :

- Un utilisateur désinstalle l'application de son appareil.
- Un message push n'a pas pu être délivré en raison d'un rebond. Cela est souvent dû à une désinstallation, mais peut aussi être dû à des mises à jour d'applis, à une nouvelle version de jeton de poussée ou à un format. 
- L'enregistrement Push échoue auprès de Firebase Cloud Messaging (parfois causé par de mauvaises connexions réseau ou un échec de la connexion à ou sur FCM pour renvoyer un jeton valide).
- L'utilisateur bloque les notifications push pour l'application dans les paramètres de son appareil et ouvre ensuite une session.

{% alert note %}
Vous ne pouvez intercepter une notification push Android que lorsque l'application est au premier plan ou en arrière-plan (mais toujours en cours d'exécution). Vous ne pouvez pas intercepter les notifications lorsque l'application est arrêtée ou complètement supprimée.
{% endalert %}

{% endtab %}
{% tab iOS %}

Qu'un utilisateur accepte ou non la demande d'abonnement au push en avant-plan, vous pourrez toujours envoyer un push en arrière-plan si les notifications à distance sont activées dans Xcode et que votre application appelle [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Si votre app est provisoirement autorisée ou si l'utilisateur a opté pour le push, il reçoit un jeton de push au premier plan, ce qui vous permet de lui envoyer tous les types de push. Au sein de Braze, nous considérons qu'un utilisateur sur iOS qui est autorisé à pousser au premier plan est autorisé à pousser, soit explicitement (au niveau de l'app), soit provisoirement (au niveau de l'appareil).

Si un utilisateur refuse de recevoir des notifications push au niveau du système d'exploitation, l'état de son abonnement push sera `Subscribed`, et son profil n'indiquera pas qu'un jeton push au premier plan a été enregistré. 

Dans le cas où un utilisateur, qui a initialement opté pour l'abonnement au niveau du système d'exploitation, désactive les notifications push dans les paramètres de son système d'exploitation, la situation suivante se produira au démarrage de la session suivante :
- Braze les marque comme étant désactivés au premier plan et ne tente plus d'envoyer des messages push.
- Le filtre `Foreground Push Enabled for App (iOS)` et le filtre de segmentation `Foreground Push Enabled` (en supposant qu'aucune autre application sur le profil utilisateur ne dispose d'un jeton de poussée au premier plan valide) renverront `false`.

Dans ce scénario, étant donné qu'un jeton push en arrière-plan existera toujours, vous pouvez continuer à envoyer des notifications push en arrière-plan (silencieuses) avec le filtre de segmentation `Background or Foreground Push Enabled = true`.

{% alert note %}
iOS ne permet pas aux apps d'intercepter une notification push avant que celle-ci ne s'affiche. Cela signifie que les apps (et Braze) n'ont aucun contrôle sur l'affichage ou le masquage de la notification. Un utilisateur peut refuser les notifications push pour une application dans les paramètres de l'appareil, mais c'est le système d'exploitation qui s'en charge.
{% endalert %}

{% endtab %}
{% tab Web %}

Lorsqu'un utilisateur accepte la demande d'autorisation de push native, son statut d'abonnement passe à `opted in`.

Pour gérer les abonnements, vous pouvez utiliser la méthode utilisateur [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) pour créer une page de paramètres de préférences sur votre site, après quoi vous pouvez filtrer les utilisateurs par statut d'abonnement sur le tableau de bord.

Si un utilisateur désactive les notifications dans son navigateur, la prochaine notification push envoyée à cet utilisateur rebondira, et Braze mettra à jour le jeton push de l'utilisateur en conséquence. Il est utilisé pour gérer l'éligibilité aux filtres activés par push (`Background or Foreground Push Enabled`, `Foreground Push Enabled` et `Foreground Push Enabled for App`). L'état de l'abonnement défini dans le profil utilisateur est un paramètre au niveau de l'utilisateur et ne change pas lorsqu'un message push est renvoyé.

{% alert note %}
Les plates-formes web ne permettent pas de pousser en arrière-plan ou de manière silencieuse.
{% endalert %}
{% endtab %}
{% endtabs %}

## Meilleures pratiques

Consultez notre article dédié aux [meilleures pratiques en matière de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) pour obtenir des conseils détaillés sur la manière d'optimiser votre utilisation du push chez Braze.

