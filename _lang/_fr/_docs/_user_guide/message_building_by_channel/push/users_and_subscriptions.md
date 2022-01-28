---
nav_title: "Appuyer sur l'activation et l'abonnement"
article_title: Appuyer sur l'activation et l'abonnement
page_order: 3
page_type: Référence
description: "Cet article de référence couvre les différents états d'abonnement push ainsi qu'un aperçu de l'activation de push, couvrant la différence fondamentale de push sur iOS et Android."
channel:
  - Pousser
---

# Appuyer sur les options et l'abonnement

> Cet article de référence couvre les différents états d'abonnement push ainsi qu'un aperçu de l'activation de push, couvrant la différence fondamentale de push sur iOS et Android.

!\[Opt-in Option\]\[56\]{: style="float:right;max-width:50%;margin-left:15px;"}

Les états d'abonnement Push sont des filtres qui permettent à vos utilisateurs de contrôler s'ils reçoivent ou non des messages. Pour que votre utilisateur reçoive vos messages via push, ils doivent être `abonnés` ou `Opted-In`, ainsi que [push activé](#push-enabled).

## État de l'abonnement Push

Les états d'abonnement sont des drapeaux utiles lorsque vous décidez quels utilisateurs cibler pour les notifications push. Braze recommande de fournir des interrupteurs dans votre application pour rendre facile pour les utilisateurs de déterminer leur statut de notification push. Cela aide à empêcher les utilisateurs d'entrer dans les paramètres de l'appareil et de supprimer complètement les jetons push.

| Etat d'Opt-in | Libellé                                                                                                                                                                                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inscrit       | État par défaut.                                                                                                                                                                                                                                                             |
| Inscrit       | Un utilisateur a explicitement exprimé une préférence pour recevoir des notifications push. Braze déplacera automatiquement l'état d'Opt-in d'un utilisateur vers "Opted-In".                                                                                                |
| Désabonné     | Un utilisateur s'est désabonné explicitement de push via l'interface utilisateur de votre application ou d'autres méthodes que votre marque fournit. Par défaut, les campagnes de push Braze ciblent uniquement les utilisateurs qui sont "Abonnés" ou "Opted-in" pour push. |
{: .reset-td-br-1 .reset-td-br-2}

Si un utilisateur n'a pas de jeton push (c'est-à-dire qu'il désactive les jetons push au niveau de l'appareil via les paramètres, en choisissant de ne pas recevoir de messages), ils peuvent toujours être abonnés à push. Être abonné ne garantit pas qu'un push sera distribué — les utilisateurs doivent également être activés par push ou par push enregistrés pour recevoir ces notifications.

Ceci est principalement dû au fait que les utilisateurs ont un seul état d'abonnement à push mais peuvent avoir plusieurs périphériques avec différents niveaux de permissions push.

### Vérifier l'état de l'abonnement push de l'utilisateur

!\[Exemple\]\[3\]{: style="float:right;max-width:35%;margin-left:15px;"}

Il y a deux façons de vérifier l'état de l'abonnement push d'un utilisateur avec Braze :

1. __Profil utilisateur :__ Vous pouvez accéder à des profils utilisateur individuels via le tableau de bord Braze sur la page **Recherche d'utilisateur**. Ici, vous pouvez rechercher des profils d'utilisateurs par adresse e-mail, numéro de téléphone ou ID d'utilisateur externe. Une fois dans un profil utilisateur, vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état d'abonnement d'un utilisateur. <br><br>
2. __Exportation de l'API Rest :__ Vous pouvez exporter des profils utilisateur individuels au format JSON en utilisant l'export [Utilisateurs par segment][segment] ou [Utilisateurs par identifiant][identifier] points de terminaison. Braze retournera un objet jeton push qui contient des informations d'activation push par appareil.

## Appuyer sur l'activation {#push-enabled}

Un utilisateur est "Push Enabled" ou "Push Registered" s'il a un jeton push actif pour une application dans votre groupe d'applications.

!\[Push Enablement\]\[1\]{: style="float:right;max-width:50%;margin-left:15px;"}

Dans l'onglet **Engagement** dans le profil d'un utilisateur, vous verrez **Push Registered For** suivi d'un nom d'application ou de deux tirets (**&#45;&#45;**), si aucune information d'application n'existe pour cet appareil. Il y aura une entrée pour chaque appareil qui appartient à l'utilisateur.

Si le nom de l'application de l'entrée de l'appareil est préfixé par `au premier plan:`, l'application est autorisée à recevoir à la fois des notifications push en avant-plan (visible par l'utilisateur) et des notifications push en arrière-plan (non visibles pour l'utilisateur) sur cet appareil.

D'un autre côté, si le nom de l'application de l'entrée de l'appareil est préfixé par `Arrière-plan :`, l'application n'est autorisée à recevoir que [push en arrière-plan]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) et ne peut pas afficher de notifications visibles par l'utilisateur sur cet appareil. Cela indique généralement que l'utilisateur a désactivé les notifications pour l'application sur cet appareil. !\[Push Changelog\]\[2\]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Si un jeton de push est déplacé vers un autre utilisateur sur le même appareil, ce premier utilisateur ne sera plus enregistré.

## Détails du push {#ios-android-details}

Les sections suivantes détaillent certaines différences sur la façon dont la fonction de push est gérée entre Android, iOS et web.

### Android

Vous n'avez pas besoin de demander l'autorisation d'envoyer des notifications push aux utilisateurs Android. Cependant, Braze ne mettra pas automatiquement à jour l'état d'option [de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) jusqu'à ce que l'utilisateur demande explicitement de recevoir push. Lors de la première session d'un utilisateur sur Android, Braze demande automatiquement un nouveau jeton. Dès que ce jeton a été reçu avec succès, l'état "push" de l'utilisateur est ensuite mis à jour. À ce stade, l'utilisateur est autorisé à pousser à la fois au niveau de l'application et du périphérique.

Si l'utilisateur désactive push, Braze les marque comme push de premier plan désactivé et ne tente plus de leur envoyer des messages push. Le filtre `Push Activé` entraînera `false` pour cet utilisateur. Vous pouvez toujours continuer à envoyer des notifications en arrière-plan (silencieuse) avec le filtre de segmentation `Push d'arrière-plan Activé = true`.

Sur Android, Braze déplacera un utilisateur à pousser si :

- Un utilisateur désinstalle l'application de son appareil.
- Braze reçoit un rebond lors de l'envoi à un jeton spécifique (parfois causé par les mises à jour d'applications, les désinstallations, la nouvelle version de jeton de push, ou le format).
- L'enregistrement de Push échoue à Firebase Cloud Messaging (parfois causé par des connexions réseau médiocres ou un échec de connexion à ou sur FCM pour renvoyer un jeton valide).
- L'utilisateur bloque les notifications push pour l'application dans les paramètres de son appareil et enregistre ensuite une session.

### iOS

#### États de push iOS

Pour recevoir un jeton push pour iOS, vous devez demander si l'utilisateur souhaite recevoir un push. Selon la réponse de l'utilisateur, Braze ajuste l'état de l'abonnement push de l'utilisateur à `choisi dans` si accepté, ou conserve l'état de l'abonnement push en tant que `abonné` si rejeté. Avant cela, l'état opt-in est `souscrit`. Après avoir reçu une réponse, Braze tente d'enregistrer l'utilisateur pour push. Après que Braze ait reçu un jeton avec succès, nous mettons à jour l'état push-enabled de l'utilisateur.

- Push Activé : Braze a un jeton push pour l'appareil.
- Push Opted-In: L'utilisateur a exprimé une préférence pour leur envoyer des notifications push.

#### État activé

Il y a deux états activés :

- Push de premier plan activé (opted-in)
- Push d'arrière-plan activé (opted-out)

Indépendamment de la réponse à l'invite opt-int, l'utilisateur reçoit un jeton de Push en arrière-plan (vous devez avoir activé "Notifications distantes" dans Xcode), vous permettant de leur envoyer une Push en mode silencieux. Si votre application est provisoirement autorisée ou si l'utilisateur a opté pour push, ils reçoivent également un jeton de premier plan, vous permettant de leur envoyer tous les types de push. Au sein de Braze, nous considérons qu'un utilisateur sur iOS qui est au premier plan activé est "push enabled", soit explicitement (niveau de l'application) soit provisoirement (niveau de l'appareil).

#### État désactivé

Lors de la prochaine application ouverte dans iOS, le SDK détectera que le push a été désactivé et notifiera Braze. À ce stade, Braze mettra à jour l'état push-enabled à désactivé. Lorsque vous essayez d'envoyer un push à un utilisateur, Braze sait déjà si nous avons un jeton, de sorte que les notifications ne soient envoyées qu'aux personnes qui indiquent explicitement qu'elles le veulent.

#### Autorisation provisoire et Push silencieux

Dans iOS 12, Apple a introduit l'autorisation provisoire, permettant aux marques d'envoyer des notifications silencieuses aux centres de notification de leurs utilisateurs avant de s'inscrire, vous donnant la possibilité de démontrer la valeur de vos messages plus tôt. Consultez notre documentation pour en savoir plus sur l' [autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications).

Sur les appareils fonctionnant sous iOS 11 ou ci-dessous, vos utilisateurs doivent explicitement opter pour recevoir vos messages push. Vous devez demander si l'utilisateur souhaite recevoir des messages push de votre part.

### Web

Le comportement de l'abonnement push web fonctionne de la même façon que celui de mobile. Le statut d'abonnement par défaut pour les utilisateurs web une fois qu'ils ont opté pour la fonction `appboy.registerAppboyPushMessages()` est `abonné`. Ce statut par défaut est suffisant pour que vous puissiez envoyer des messages push aux utilisateurs du web. L'état `opté dans` implique qu'un utilisateur a opté explicitement pour pousser des notifications via le web, si permis. Cependant, cet opt-in explicite n'est pas nécessaire pour envoyer des push aux utilisateurs du web.

Pour gérer les abonnements, vous pouvez utiliser la méthode utilisateur [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html#setpushnotificationsubscriptiontype) pour créer une page de paramètres de préférences sur votre site, après quoi vous pouvez filtrer les utilisateurs par opt-out statut sur le tableau de bord.

Si un utilisateur désactive les notifications dans son navigateur, la prochaine notification push envoyée à cet utilisateur rebondira et Braze mettra à jour le jeton de push de l'utilisateur en conséquence. Ceci est utilisé pour gérer l'éligibilité des filtres activés par push (`Background Push Activé`, `Push Activé` et `Push Activé pour l'application`). Le statut d'abonnement défini sur le profil de l'utilisateur est un paramètre de niveau utilisateur et ne change pas quand un push bounce.
[1]: {% image_buster /assets/img/push_enablement.png %} [2]: {% image_buster /assets/img/push_changelog. ng %} [56]: {% image_buster /assets/img_archive/braze_optedin.png %} [3]: {% image_buster /assets/img/push_example.png %}

[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
