---
nav_title: "Activation et abonnement aux notifications push"
article_title: Activation et abonnement aux notifications push
page_order: 3
page_type: reference
description: "Cet article de référence couvre les concepts des états Activé pour les notifications push et Abonnement aux notifications push dans Braze, y compris les différences fondamentales de comportement sur iOS, Android et Web."
channel:
  - notification push

---

# Activation et abonnement aux notifications push

> Cet article de référence couvre les concepts des états Activé pour les notifications push et Abonnement aux notifications push dans Braze, y compris les différences fondamentales de comportement sur iOS, Android et Web.

## Activation des notifications push {#push-enabled}

**Push Enabled** (Activé pour les notifications push) est un filtre de segmentation dans Braze qui permet aux marketeurs d’identifier facilement les utilisateurs qui permettent à Braze d’envoyer des notifications  push et les utilisateurs qui n’ont pas exprimé leurs préférences pour ne pas recevoir de notifications push. Par définition, ce filtre **Push Enabled** (Activé pour les notifications push) prend en compte les éléments suivants :
- La capacité de Braze à envoyer une notification push
- L’état de l’abonnement aux notifications push de l’utilisateur

![][1]{: style="float:right;max-width:50%;margin-left:15px;"}

Un utilisateur est considéré comme « push enabled » (activé pour les notifications push) ou « push registered » (abonné aux notifications push) s’il dispose d’un jeton de notification push actif pour une application au sein de votre groupe d’apps, ce qui signifie que le statut d’activation des notifications push est spécifique à l’application. 

### Types de jetons de notification push

Il existe deux types de [jetons de notification push][4] qui sont essentiels pour comprendre comment une notification push est envoyée avec succès à vos utilisateurs :
- Jetons de notification push de premier plan
- Jetons de notification push d’arrière-plan

Les jetons de notification push de premier plan permettent d’envoyer des notifications push standard au premier plan de l’appareil d’un utilisateur. Les jetons de notification push en arrière-plan, ou silencieux, sont attribués à tous les appareils qui ont téléchargé l’application d’une marque, indépendamment du fait si l’appareil en question ait ou non choisi de recevoir des notifications push de cette marque. Les jetons de notification push en arrière-plan permettent aux marques d’envoyer des notifications push silencieuses, c’est-à-dire des notifications push qui ne s’affichent pas intentionnellement sur les appareils afin de prendre en charge des fonctionnalités clés comme le suivi des désinstallations.

Lorsqu’un profil d’utilisateur est associé à un jeton de notification push de premier plan valide associé à une application, Braze considère que l’utilisateur est « push registered » (abonné aux notifications push) pour l’application donnée. Braze fournit alors un filtre de segmentation spécifique `Push enabled for App` pour identifier ces utilisateurs.

Notez que le filtre `Push enabled for App` ne prend en compte que la présence d’un jeton de notification push de premier plan ou d’arrière-plan valide pour l’application donnée. Cependant, le filtre `Push Enabled` plus générique segmente vos utilisateurs qui ont explicitement activé les notifications push de n’importe quelle application de votre groupe d’apps. Ce nombre inclut uniquement les notifications push de premier plan, et n’inclut pas les utilisateurs qui se sont désabonnés. Vous pouvez en savoir plus sur ces filtres et d’autres dans [Segmentation Filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) (Filtres de segmentation).

### Vérifier l’état de l’activation des notifications push de l’utilisateur

Dans l’onglet **Engagement** du profil utilisateur, vous verrez **Push Registered For** (Abonné aux notifications push pour) suivi d’un nom d’application. Si aucune information d’application n’existe pour cet appareil, vous verrez deux tirets (**&#45;&#45;**). Il y aura une entrée pour chaque appareil appartenant à l’utilisateur.

Si le nom de l’application de l’entrée de l’appareil est préfixé par `Foreground:`, l’application est autorisée à recevoir à la fois des notifications push de premier plan (visibles par l’utilisateur) et des notifications push d’arrière-plan (non visibles par l’utilisateur) sur cet appareil.
![Journal de modifications des notifications push avec un exemple de jeton de notification push.][2]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

D’autre part, si le nom de l’application de l’entrée de l’appareil est préfixé par `Background:`, l’application est autorisée à recevoir uniquement des [notifications push d’arrière-plan]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) et ne peut pas afficher des notifications visibles par l’utilisateur sur cet appareil. Cela indique généralement que l’utilisateur a désactivé les notifications pour l’application sur cet appareil.

Si un jeton de notification push est déplacé vers un autre utilisateur sur le même appareil, ce premier utilisateur ne sera plus abonné.

## États de l’abonnement aux notifications push {#push-sub-states}

![États de l’abonnement aux notifications push défini sur Opted In (Autorisé).][56]{: style="float:right;max-width:50%;margin-left:15px;"}

Les états de l’abonnement aux notifications push dans Braze identifient la préférence globale d’un utilisateur quant à leur souhait de recevoir ou pas des notifications push. Les états de l’abonnement deviennent des indicateurs utiles lorsque vous décidez quels utilisateurs cibler avec les notifications push. 

{% alert important %}
Pour que votre utilisateur reçoive vos messages par le biais de notifications push, l’état de son abonnement doit être soit `Subscribed` soit `Opted-In`, et il doit être [« push enabled »](#push-enabled) (activé pour les notifications push). 
{% endalert %}

Braze recommande de prévoir des boutons bascule dans votre application pour permettre aux utilisateurs de déterminer facilement l’état de leurs notifications push. Cela permet d’empêcher les utilisateurs d’accéder aux paramètres de leur appareil et de désactiver les notifications push au niveau de l’application, ce qui entraîne la suppression complète du jeton de premier plan dans Braze.

{% alert note %}
L’état de l’abonnement aux notifications push d’un utilisateur s’applique à l’ensemble de son profil utilisateur, ce qui inclut tous les appareils de celui-ci. 
{% endalert %}

Il existe trois options d’état de l’abonnement aux notifications push : `Subscribed`, `Opted-In` et `Unsubscribed`. Braze suggère que les marques suivent les définitions d’état d’abonnement suivantes lors de la gestion des préférences des notifications push de leurs utilisateurs.

|État autorisé|Description|
|---|---|
|Abonné| État d’abonnement aux notifications push par défaut lorsqu’un profil utilisateur est créé dans Braze. |
|Autorisé| Un utilisateur a explicitement exprimé une préférence pour recevoir des notifications push. Pour iOS et le Web, Braze déplace automatiquement l’état autorisé d’un utilisateur vers `Opted-In` si celui-ci accepte une invite de notification push au niveau du système d’exploitation. Cela ne s’applique pas à Android. |
|Désabonné| Un utilisateur s’est explicitement désabonné des notifications push par le biais de l’interface utilisateur de votre application ou d’autres méthodes fournies par votre marque. Par défaut, les campagnes de notification push de Braze ciblent uniquement les utilisateurs qui sont `Subscribed` ou `Opted-in` pour les notifications push.|
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Braze ne changera jamais automatiquement l’état de l’abonnement aux notifications push d’un utilisateur à `Unsubscribed`. Gardez à l’esprit que si l’état de l’abonnement aux notifications push d’un utilisateur est `Unsubscribed`, alors le filtre `Push Enabled` de l’utilisateur dans la segmentation sera `false`.
{% endalert %}

Si un utilisateur n’a pas autorisé le jeton de notification push de premier plan (c’est-à-dire qu’il a désactivé les jetons de notification push au niveau de l’appareil par le biais des paramètres, en choisissant de ne pas recevoir de messages), il peut toujours être abonné aux notifications push. Cependant, l’utilisateur ne sera pas **Push Enabled for App** (Activé pour les notifications push de l’application) dans Braze puisque le jeton de notification push de premier plan n’est pas valide. En outre, si un profil utilisateur n’a pas d’autre jeton de notification push valide ou abonné pour toute autre application, leur filtre `Push Enabled` dans la segmentation sera également `false`. 

L’état de l’abonnement aux notifications push ne garantit pas la livraison des notifications push. Les utilisateurs doivent également être activés pour les notifications push ou abonnés aux notifications push pour recevoir ces notifications. Ceci est principalement dû au fait que les utilisateurs ont un seul état d’abonnement aux notifications push mais peuvent avoir plusieurs appareils avec différents niveaux d’autorisation pour les notifications push.

### Vérifier l’état de l’abonnement aux notifications push de l’utilisateur

![Profil utilisateur de John Doe avec son état d’abonnement aux notifications push défini sur Abonné.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l’état de l’abonnement aux notifications push d’un utilisateur avec Braze :

1. **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze sur la page **User Search** (Recherche utilisateur). Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Une fois dans un profil utilisateur, sous l’onglet **Engagement**, vous pouvez afficher et modifier manuellement l’état d’abonnement de l’utilisateur. <br><br>
2. **Rest API Export (Exportation d’API Rest)** : Vous pouvez exporter des profils utilisateur individuels au format JSON en utilisant les endpoints d’exportation [Users by segment][segment] (Utilisateurs par segment) ou [Users by identifier][identifier] (Utilisateurs par identifiant). Braze renvoie un objet jeton de notification push qui contient des informations sur l’activation de la notification par appareil.

## Différences de comportement des notifications push {#ios-android-details}

Les sections suivantes détaillent certaines différences de traitement de l’activation des notifications push entre Android, iOS et Web. 

### Android

Vous n’avez pas besoin de demander l’autorisation d’envoyer des notifications push aux utilisateurs Android. Cependant, Braze ne met pas automatiquement à jour l’[état Autorisé]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) de l’utilisateur jusqu’à ce que ce dernier demande explicitement à recevoir des notifications push. Lors de la première session d’un utilisateur sur Android, Braze demande automatiquement un nouveau jeton. Une fois ce jeton reçu avec succès, l’état Activé pour les notifications push de l’utilisateur est alors mis à jour. À ce stade, l’utilisateur est activé à la fois au niveau de l’application et au niveau de l’appareil.

Les jetons de notification push de premier plan peuvent être inscrits immédiatement pendant la première session de l’application sans que les préférences de l’utilisateur ne soient saisies dans le système d’exploitation. Cela signifie que pour les nouveaux utilisateurs Android, après leur première session dans l’application, l’état de l’abonnement aux notifications push de l’utilisateur affichera `Subscribed` et le profil affichera `Push registered for App: Android`.

Si l’utilisateur Android désactive par la suite les paramètres de notification push dans son système d’exploitation, au début de la session suivante, les événements suivants se produisent :
- Braze marque ces utilisateurs comme ayant désactivé les notifications push de premier plan et ne tente plus de leur envoyer des messages push.
- Le filtre `Push Enabled for App (Android)` et le filtre de segmentation `Push Enabled` (en supposant qu’aucune autre application sur le profil utilisateur ne possède un jeton de notification push de premier plan valide) renvoient `false`.

Dans ce scénario, étant donné qu’un jeton de notification push d’arrière-plan existe toujours, vous pouvez toujours continuer à envoyer des notifications push d’arrière-plan (silencieuses) avec le filtre de segmentation `Background Push Enabled = true`.

Pour Android, Braze considère un utilisateur comme ayant désactivé les notifications push si :

- Un utilisateur désinstalle l’application de son appareil.
- Braze reçoit un rejet lors de l’envoi vers un jeton spécifique (parfois causé par des mises à jour de l’application, des désinstallations, une nouvelle version du jeton de notification push ou un nouveau format du jeton).
- L’inscription de la notification push échoue au niveau de Firebase Cloud Messaging (parfois causé par de mauvaises connexions réseau ou une incapacité à se connecter à ou sur FCM pour renvoyer un jeton valide).
- L’utilisateur bloque les notifications push pour l’application dans les paramètres de son appareil et ouvre ensuite une session.

### iOS

La principale différence de comportement en matière de notification push entre Android et iOS est que, pour inscrire un jeton de notification push pour iOS, les utilisateurs doivent explicitement autoriser au niveau du système d’exploitation via l’invite de notification push d’iOS.

Lorsque cette invite s’affiche, si un utilisateur choisit explicitement d’autoriser, Braze mettra automatiquement à jour l’état de l’abonnement aux notifications push de l’utilisateur à partir de `Subscribed`, qui est l’état par défaut, à `Opted in`. C’est le seul scénario où Braze modifiera activement l’état de l’abonnement aux notifications push. Si l’utilisateur décide de ne pas autoriser, alors son état d’abonnement aux notifications push reste `Subscribed`. 

Ainsi, pour les nouveaux utilisateurs iOS, s’ils ont activement choisi de recevoir des notifications push à l’aide de l’invite du système d’exploitation, l’état de leur abonnement aux notifications push sera `Opted in` et leur profil affichera `Push registered for App: iOS`.

Si un utilisateur refuse de recevoir des notifications push au niveau du système d’exploitation, l’état de son abonnement sera `Subscribed` et son profil ne montrera pas qu’un jeton de notification push de premier plan a été inscrit. 

Dans le cas d’un utilisateur, qui a initialement autorisé les notifications push au niveau du système d’exploitation, puis qui les désactive dans les paramètres de son système d’exploitation, au démarrage de la session suivante, les événements suivants se produisent :
- Braze marque ces utilisateurs comme ayant désactivé les notifications push de premier plan et ne tente plus d’envoyer des messages push.
- Le filtre `Push Enabled for App (iOS)` et le filtre de segmentation `Push Enabled` (en supposant qu’aucune autre application sur le profil utilisateur ne possède un jeton de notification push de premier plan valide) renvoient `false`.

Dans ce scénario, étant donné qu’un jeton de notification push d’arrière-plan existe toujours, vous pouvez toujours continuer à envoyer des notifications push d’arrière-plan (silencieuses) avec le filtre de segmentation `Background Push Enabled = true`.

#### Notification push d’arrière-plan

Quelle que soit la réponse à la demande d’inscription, l’utilisateur reçoit un jeton de notification push d’arrière-plan (vous devez avoir activé « Remote Notifications » (Notifications à distance) dans Xcode), ce qui vous permet de lui envoyer une notification push silencieuse. Si votre application est provisoirement autorisée ou si l’utilisateur a autorisé les notifications push, il reçoit également un jeton de notification push de premier plan, ce qui vous permet de lui envoyer tous les types de notification push. Dans Braze, nous considérons un utilisateur sur iOS, qui est activé pour les notifications push de premier plan, comme « push enabled » (activé pour les notifications push), soit explicitement (au niveau de l’application), soit provisoirement (au niveau de l’appareil).

#### Autorisation provisoire et notifications push silencieuses

Dans iOS 12, Apple a introduit l’autorisation provisoire, permettant aux marques d’envoyer des notifications push discrètes vers les Centres de notification de leurs utilisateurs avant que ceux-ci n’aient explicitement donné leur accord, ce qui vous donne l’occasion de tester très tôt la valeur de vos messages. Consultez notre documentation pour en savoir plus sur les [autorisations provisoires]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications).

Sur les appareils fonctionnant sous iOS 11 ou antérieur, vos utilisateurs doivent explicitement autoriser de recevoir vos messages de notification push. Vous devez demander si l’utilisateur souhaite recevoir des notifications push de votre part.

### Web

Le comportement de l’abonnement aux notifications push sur le Web fonctionne de manière similaire à celui d’iOS. L’état de l’abonnement par défaut des utilisateurs Web une fois qu’ils ont donné leur autorisation via le `requestPushPermission()` est `subscribed`. Cet état par défaut est suffisant pour envoyer des messages de notification push aux utilisateurs Web. L’état `opted in` implique qu’un utilisateur a explicitement autorisé les notifications push via le Web, si cela est possible. Cependant, cet abonnement explicit n’est pas requis pour envoyer des notifications push vers des utilisateurs Web.

Pour gérer les abonnements, vous pouvez utiliser la méthode utilisateur [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) pour créer une page de paramètres de préférence sur votre site, après quoi vous pouvez filtrer les utilisateurs par état de refus sur le tableau de bord.

Si un utilisateur désactive les notifications dans son navigateur, la prochaine notification push envoyée à cet utilisateur sera refusée et Braze mettra à jour le jeton de l’utilisateur en conséquence. Ceci permet de gérer l’éligibilité des filtres activés pour les notifications push (`Background Push Enabled`, `Push Enabled` et `Push Enabled for App`). L’état de l’abonnement défini sur le profil utilisateur est un paramètre de niveau utilisateur et ne change pas lorsqu’une notification push est renvoyée.

[1]: {% image_buster /assets/img/push_enablement.png %}
[2]: {% image_buster /assets/img/push_changelog.png %}
[3]: {% image_buster /assets/img/push_example.png %}
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[56]: {% image_buster /assets/img_archive/braze_optedin.png %}
