---
nav_title: "Activation et abonnement aux notifications push"
article_title: Activation et abonnement aux notifications push
page_order: 3
page_type: reference
description: "Cet article de référence couvre les concepts des états Activé pour les notifications push et Abonnement aux notifications push dans Braze, y compris les différences fondamentales de comportement sur iOS, Android et Web."
channel:
  - Notification push

---

# Activation et abonnement aux notifications push

> Cet article de référence couvre les concepts des statuts Activé pour les notifications push et Abonnement aux notifications push dans Braze, y compris les différences fondamentales de comportement sur iOS, Android et Web.

## États de l’abonnement aux notifications push {#push-sub-states}

Un « Statut d’abonnement aux notifications push » dans Braze identifie la préférence globale d’un **utilisateur** quant à leur souhait de recevoir des notifications push. Étant donné que le statut d’abonnement est basé sur l’utilisateur, il n’est pas spécifique à une application donnée. Les états de l’abonnement deviennent des indicateurs utiles lorsque vous décidez quels utilisateurs cibler avec les notifications push. 

{% alert note %}
L’état de l’abonnement aux notifications push d’un utilisateur s’applique à l’ensemble de son profil utilisateur, ce qui inclut tous les appareils de celui-ci. 
{% endalert %}

Il existe trois options d’état de l’abonnement aux notifications push : `Subscribed`, `Opted-In` et `Unsubscribed`.

Par défaut, pour que votre utilisateur reçoive vos messages par le biais de notifications push, le statut de son abonnement doit être soit `Subscribed` soit `Opted-In`, et il doit être [« activé pour les notifications push »](#push-enabled). Vous pouvez écraser ce paramétrage si nécessaire lors de la rédaction d’un message.

|État autorisé|Description|
|---|---|
|`Subscribed`| État d’abonnement aux notifications push par défaut lorsqu’un profil utilisateur est créé dans Braze. |
|`Opted-In`| Un utilisateur a explicitement exprimé une préférence pour recevoir des notifications push. Braze déplace automatiquement l’état inscrit d’un utilisateur vers `Opted-In` si celui-ci accepte une invite de notification push au niveau du système d’exploitation.<br><br>Ceci ne s’applique pas aux utilisateurs d’Android 12 ou antérieur.|
|`Unsubscribed`| Un utilisateur s’est explicitement désabonné des notifications push par le biais de votre application ou d’autres méthodes fournies par votre marque. Par défaut, les campagnes de notification push de Braze ciblent uniquement les utilisateurs qui sont `Subscribed` ou `Opted-in` pour les notifications push.|
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Braze ne change pas automatiquement le statut de l’abonnement aux notifications push d’un utilisateur vers `Unsubscribed`. Souvenez-vous que si le statut de l’abonnement aux notifications push d’un utilisateur est `Unsubscribed`, alors le filtre `Push Enabled` de l’utilisateur dans la segmentation sera `false`.
{% endalert %}

### Mettre à jour le statut d’abonnement aux notifications push {#update-push-subscription-state}

Il existe trois manières de mettre à jour le statut d’abonnement aux notifications push d’un utilisateur :

1. **Intégration SDK**<br>Utilisez le SDK de Braze pour mettre à jour le statut d’abonnement d’un utilisateur. Vous pouvez, par exemple, ajouter une page de paramètres à votre application, dans laquelle les utilisateurs peuvent activer ou désactiver les notifications push pour leur profil.<br>Pour ce faire, utilisez la méthode `setPushNotificationSubscriptionType` sur [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#afb2c11d1889fd08537f90ee64c94efb3).<br><br>
2. **API REST**<br>Utilisez l’[endpoint `/users/track`][users-track] pour mettre à jour l’attribut [`push_subscribe`][user_attributes_object] pour un utilisateur donné.<br><br>
3. **Automatique lors de l’abonnement** <br>Lorsqu’un utilisateur accepte la demande d’autorisation des notifications push native du système d’exploitation, Braze modifie automatiquement ce statut d’abonnement de l’utilisateur vers `Opted-In`.

### Vérifier le statut de l’abonnement aux notifications push

![Profil utilisateur de John Doe avec son état d’abonnement aux notifications push défini sur Abonné.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l’état de l’abonnement aux notifications push d’un utilisateur avec Braze :

1. **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze sur la page **[Recherche utilisateur][5]**. Après avoir trouvé un profil utilisateur (par adresse e-mail, numéro de téléphone ou ID d’utilisateur externe), vous pouvez sélectionner l’onglet **Engagement** pour afficher et ajuster manuellement l’état d’abonnement de l’utilisateur. 
<br><br>
2. **Rest API Export (Exportation d’API Rest)** : Vous pouvez exporter des profils utilisateur individuels au format JSON en utilisant les endpoints d’exportation [Utilisateurs par segment][segment] ou [Utilisateurs par identifiant][identifier]. Braze renvoie un objet jeton de notification push qui contient des informations sur l’activation de la notification par appareil.


## Autorisation des notifications push

Toutes les plateformes autorisant les notifications push (iOS, Web et Android) demandent un abonnement explicite à l’aide d’une invite au niveau du système d’exploitation, avec quelques différences décrites ci-dessous.

Étant donné que la décision de l’utilisateur est définitive et que vous ne pouvez pas demander à nouveau s’il refuse, l’utilisation de messages in-app d’[amorce de notification push][push-primers] constitue une stratégie importante pour améliorer vos taux d’abonnements.

**Demandes d’autorisation des notifications push natives du système d’exploitation**

|Plateforme|Capture d’écran|Description|
|--|--|--|
|iOS| ![Une demande d’autorisation des notifications push native d’iOS demandant « Mon application souhaite pouvoir vous envoyer des notifications » avec deux boutons, « Ne pas autoriser » et « Autoriser » au bas du message.][ios-push-prompt]{: style="max-width:410px;"} | Ceci ne s’applique pas lorsqu’une autorisation de [notification push provisoire](#provisional-push) est demandée.|
|Android| ![Un message de notification push Android demandant « Autoriser Kitchenerie à vous envoyer des notifications ? » avec les deux boutons « Autoriser » et « Ne pas autoriser » au bas du message.][android-push-prompt]{: style="max-width:410px;"} | Cette autorisation des notifications push a été introduite avec Android 13. Avant Android 13, il n’était pas nécessaire de demander l’autorisation pour envoyer une notification push.|
|Web| ![Une demande d’autorisation des notifications push native du navigateur Web demandant « Braze.com désire afficher une notification » avec deux boutons, « Bloquer » et « Autoriser » au bas du message.][web-push-prompt]{: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Android

Avant Android 13, il n’était pas nécessaire de demander l’autorisation pour envoyer des notifications push. Sur Android 12 et antérieures, tous les utilisateurs étaient considérés comme étant `Subscribed` lors de leur première session lorsque Braze demande automatiquement un jeton de notification push. À ce moment-là, l’utilisateur est **autorisé pour les notifications push** avec un jeton de notification push valide pour cet appareil et un état d’abonnement par défaut de `Subscribed`.

À partir d’[Android 13][android-13], l’autorisation des notifications push doit être demandée et obtenue auprès de l’utilisateur. Votre application peut demander l’autorisation à l’utilisateur manuellement à des moments opportuns mais, dans le cas contraire, les utilisateurs recevront une notification automatique quand votre application crée un [canal de notification](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

![Une notification dans le centre de notifications du système avec un message en bas demandant : « Continuer à recevoir des notifications de l’application Yachtr ? » avec deux boutons au bas pour « Continuer » ou « Désactiver »][ios-provisional-push]{: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Votre application peut demander des notifications push provisoires ou autorisées. 

Les notifications push autorisées nécessitent une autorisation explicite de l’utilisateur avant d’envoyer des notifications, alors que les [notifications push provisoires][provisional-blog] vous permettent d’envoyer des notifications  __discrètement__, directement dans le centre de notifications sans émettre de son ou d’alerte.

#### Autorisation provisoire et notifications push silencieuses {#provisional-push}

Avant iOS 12 (sorti en 2018), tous les utilisateurs devaient s’abonner explicitement pour recevoir des notifications push.

Dans iOS 12, Apple a introduit l’[autorisation provisoire][provisional-blog], permettant aux marques d’envoyer des notifications push discrètes vers les centres de notification de leurs utilisateurs avant que ceux-ci n’aient explicitement donné leur accord, ce qui vous donne l’occasion de montrer très tôt la valeur de vos messages. Consultez les [autorisations provisoires]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications) pour en savoir plus.

### Web

Pour le Web, vous devez demander un abonnement explicite de l’utilisateur à l’aide du dialogue d’autorisation natif du navigateur.

Contrairement à Android et iOS qui laissent votre application afficher le dialogue d’autorisation n’importe quand, certains navigateurs modernes n’afficheront l’invite que si elle est déclenchée par une action de l’utilisateur (clic de souris ou touche du clavier). Si votre site essaie de demander une autorisation de notification push lors du chargement de la page, elle sera sûrement ignorée ou étouffée par le navigateur.

De ce fait, vous ne devriez demander l’autorisation que quand l’utilisateur clique quelque part sur votre site Internet et pas au hasard, lors du chargement d’une page.

## Jetons de notification push

Les [jetons de notification push][push-tokens] constituent un identifiant anonyme unique généré par l’appareil d’un utilisateur et envoyé à Braze pour identifier où envoyer les notifications de chaque destinataire.

Il existe deux manières de classifier un [jeton de notification push][push-tokens] qui sont centrales pour comprendre comment une notification push peut être envoyée à vos utilisateurs.

1. Les **notifications push de premier plan** permettent d’envoyer des notifications push standard et visibles au premier plan de l’appareil d’un utilisateur.
2. Les **notifications push en arrière-plan** sont disponibles, qu’un appareil donné se soit abonné ou non à la réception de notifications push de cette marque. Les notifications push en arrière-plan permettent aux marques d’envoyer des notifications push silencieuses sur les appareils, c’est-à-dire des notifications push qui ne s’affichent pas intentionnellement, afin de prendre en charge des fonctionnalités clés comme le [suivi des désinstallations]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/).

Lorsqu’un profil d’utilisateur est associé à un jeton de notification push de premier plan valide associé à une application, Braze considère que l’utilisateur est « push registered » (abonné aux notifications push) pour l’application donnée. Braze fournit alors un filtre de segmentation spécifique, `Push enabled for App,`, pour identifier ces utilisateurs.

{% alert note %}
Le filtre `Push Enabled for App` prend uniquement en compte la présence d’un jeton de notification push de premier plan ou d’arrière-plan valide pour l’application donnée. Cependant, le filtre `Push Enabled` plus générique segmente les utilisateurs qui ont explicitement activé les notifications push de n’importe quelle application de votre groupe d’apps. Ce nombre inclut uniquement les notifications push de premier plan et n’inclut pas les utilisateurs qui se sont désabonnés. Vous pouvez en savoir plus sur ces filtres et d’autres dans [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Plusieurs utilisateurs sur un appareil

Les jetons de notification push sont spécifiques pour un appareil et une application, il n’est donc pas possible d’utiliser des jetons de notification push pour différencier plusieurs utilisateurs utilisant le même appareil.

Imaginons par exemple que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre application sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecte au sien, le jeton de notification push sera réaffecté au profil de Kim. Le jeton de notification push restera affecté au profil de Kim sur cet appareil jusqu’à ce qu’elle se déconnecte et que Charlie se reconnecte.

Une application ou un site Internet ne peuvent avoir qu’un seul abonnement aux notifications push par appareil. Lorsqu’un utilisateur se déconnecte d’un appareil ou d’un site Internet et qu’un utilisateur se connecte, le jeton de notification push est donc réaffecté au nouvel utilisateur. Ceci s’affiche sur le profil utilisateur, dans la section **Paramètres de contact** de l’onglet **Engagement** :

![Le journal de modifications du jeton de notification push sur l’onglet **Engagement** d’un profil utilisateur, qui répertorie quand le jeton de notification push a été transmis à un autre utilisateur et ce qu’il était.][4]

Étant donné que les fournisseurs de notifications push (APN/FCM) n’ont aucun moyen de faire la différence entre plusieurs utilisateurs sur un même appareil, nous transmettons le jeton de notification push au dernier utilisateur qui s’est connecté pour déterminer quel utilisateur cibler sur l’appareil pour les notifications push.

## Filtre Activé pour les notifications push {#push-enabled}

`Push Enabled` est un filtre de segmentation dans Braze qui permet aux marketeurs d’identifier facilement les utilisateurs qui permettent à Braze d’envoyer des notifications push et les utilisateurs qui n’ont pas exprimé leurs préférences pour ne pas recevoir de notifications push. 

Le filtre `Push Enabled` tient compte des éléments suivants :
- La capacité de Braze à envoyer une notification push (jeton de notification push de premier plan)
- Les préférences générales de l’utilisateur concernant la réception de notifications push sur ses appareils (statut d’abonnement aux notifications push)

![Une capture d’écran du tableau de bord montrant qu’un utilisateur est « Enregistré aux notifications push à des fins de marketing (iOS) »][1]{: style="float:right;max-width:50%;margin-left:15px;"}

Un utilisateur est considéré comme « activé pour les notifications push » ou « abonné aux notifications push » s’il dispose d’un jeton de notification push de premier plan actif pour une application au sein de votre groupe d’apps, ce qui signifie que le statut d’activation des notifications push est spécifique à l’application. 

{% alert note %}
Pour obtenir des informations sur la façon de vérifier l’état d’enregistrement, rendez-vous dans la section [statut d’abonnement aux notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)
{% endalert %}

## Bonnes pratiques

#### Ajouter des contrôles d’abonnement aux notifications push à votre application
Pour éviter que les utilisateurs désactivent les notifications au niveau de l’appareil, ce qui supprime complètement leur jeton de notification push en arrière-plan, Braze recommande de laisser les utilisateurs contrôler leur abonnement aux notifications push directement au sein de votre application. Consultez la section [mettre à jour le statut d’abonnement aux notifications push](#update-push-subscription-state) pour plus de détails.

#### Préparer vos utilisateurs aux notifications push avant de leur présenter l’invite du système
Vous ne pouvez demander l’autorisation des notifications push qu’une seule fois à votre utilisateur et, s’ils ont refusé, il est très difficile de les convaincre de réactiver les notifications push dans les paramètres de l’appareil. Pour cette raison, vous devriez préparer vos utilisateurs aux notifications push en utilisant un message in-app avant d’afficher l’invite système. Consultez la section [amorces de notification push][push-primers] pour en apprendre plus sur la manière d’augmenter les abonnements.

#### Le statut d’abonnement ne veut pas forcément dire que l’utilisateur peut être contacté
Si un utilisateur ne dispose pas d’un jeton de notification push de premier plan valide pour l’application (c’est-à-dire qu’il a désactivé les jetons de notification push au niveau de l’appareil par le biais des paramètres, en choisissant de ne pas recevoir de messages), son statut d’abonnement peut toujours être considéré comme étant `subscribed` aux notifications push. Cependant, cet utilisateur ne sera pas **Activé pour les notifications push de l’application** dans Braze puisque le jeton de notification push de premier plan n’est pas valide. 

En outre, si un profil utilisateur n’a pas un jeton de notification push valide ou abonné pour toute autre application, leur filtre d’activation pour les notifications push dans la segmentation sera également `false`. 

L’état de l’abonnement aux notifications push ne garantit pas la livraison des notifications push. Les utilisateurs doivent également être activés pour les notifications push pour recevoir des notifications. Cela est principalement dû au fait qu’un profil utilisateur a un seul statut d’abonnement aux notifications push mais peut avoir plusieurs appareils avec différentes autorisations pour les notifications push de premier plan.

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

Cependant, si un utilisateur accepte la demande d’inscription aux notifications push de premier plan, vous pourrez toujours envoyer une notification push en arrière-plan si vos notifications push à distance sont activées en Xcode et que votre application appelle [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Si votre application est provisoirement autorisée ou que l’utilisateur a autorisé les notifications push, il reçoit un jeton de notification push de premier plan, ce qui vous permet de lui envoyer tous les types de notification push. Dans Braze, nous considérons un utilisateur sur iOS, qui est activé pour les notifications push de premier plan, comme étant activé pour les notifications push, soit explicitement (au niveau de l’application), soit provisoirement (au niveau de l’appareil).

Si un utilisateur refuse de recevoir des notifications push au niveau du système d’exploitation, l’état de son abonnement sera `Subscribed` et son profil ne montrera pas qu’un jeton de notification push de premier plan a été inscrit. 

Dans le cas d’un utilisateur, qui a initialement autorisé les notifications push au niveau du système d’exploitation, puis qui les désactive dans les paramètres de son système d’exploitation, au démarrage de la session suivante, les événements suivants se produisent :
- Braze marque ces utilisateurs comme ayant désactivé les notifications push de premier plan et ne tente plus d’envoyer des messages push.
- Le filtre `Push Enabled for App (iOS)` et le filtre de segmentation `Push Enabled` (en supposant qu’aucune autre application sur le profil utilisateur ne possède un jeton de notification push de premier plan valide) renvoient `false`.

Dans ce scénario, étant donné qu’un jeton de notification push d’arrière-plan existe toujours, vous pouvez continuer à envoyer des notifications push d’arrière-plan (silencieuses) avec le filtre de segmentation `Background Push Enabled = true`.

{% endtab %}
{% tab Web %}

Lorsqu’un utilisateur accepte la demande d’autorisation des notifications push natives, son statut d’abonnement passera sur `opted in`.

Pour gérer les abonnements, vous pouvez utiliser la méthode utilisateur [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) pour créer une page de paramètres de préférence sur votre site, après quoi vous pouvez filtrer les utilisateurs par état de refus sur le tableau de bord.

Si un utilisateur désactive les notifications dans son navigateur, la prochaine notification push envoyée à cet utilisateur sera refusée et Braze mettra à jour le jeton de l’utilisateur en conséquence. Ceci permet de gérer l’éligibilité des filtres pour l’activation des notifications push (`Background Push Enabled`, `Push Enabled` et `Push Enabled for App`). L’état de l’abonnement défini sur le profil utilisateur est un paramètre de niveau utilisateur et ne change pas lorsqu’une notification push est renvoyée.

{% alert note %}
Les plateformes Web n’autorisent pas les notifications push en arrière-plan ou silencieuses.
{% endalert %}
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/push_enablement.png %}
[2]: {% image_buster /assets/img/push_changelog.png %}
[3]: {% image_buster /assets/img/push_example.png %}
[4]: {% image_buster /assets/img/push_token_changelog.png %}
[push-tokens]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[ios-push-prompt]: {% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}
[android-push-prompt]: {% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}
[web-push-prompt]: {% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}
[ios-provisional-push]: {% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}
[push-primers]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
[android-13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/
[provisional-blog]: https://www.braze.com/resources/articles/mastering-provisional-push
[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[users-track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
