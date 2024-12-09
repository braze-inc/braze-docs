---
nav_title: "Enregistrement d’une notification push"
article_title: Enregistrement d’une notification push
page_order: 2
page_type: reference
description: "Cet article de référence explique ce que signifie être inscrit aux notifications push et comment nous envoyons des messages push et traitons les jetons de notification push et l’inscription aux notifications push dans Braze."
channel:
  - push

---

# Inscription aux notifications push

> Cet article couvre le processus par lequel un utilisateur reçoit un jeton de notification push et comment Braze envoie des messages push à vos utilisateurs.

## Jetons de notification push

La compréhension des jetons de notification push et de leur mécanisme est un élément fondamental pour maîtriser la manière dont nous envoyons des messages push depuis Braze. Les jetons de notification push sont un identifiant anonyme unique généré par l’appareil d’un utilisateur et envoyez à Braze pour identifier où envoyer la notification de chaque destinataire. Si un appareil n’a pas de jeton de notification push, il n’y a aucun moyen d’y envoyer de notification push.

Les jetons de notification push sont générés par des fournisseurs de services push. Braze se connecte à des fournisseurs de services push comme Firebase Cloud Messaging Service (FCMs) pour Android et Apple Push Notification Service (APN) pour iOS, et ces fournisseurs envoient des jetons d’appareil uniques qui identifient votre application. Chaque appareil possède un jeton unique utilisé pour la réception de messages. Les jetons peuvent [expirer](#push-token-expire) ou être mis à jour.

Il existe deux façons de classer un [jeton de notification push][push-tokens] qui sont centrales pour comprendre comment une notification push peut être envoyée à vos utilisateurs.

1. **Foreground push** permet d'envoyer régulièrement des notifications push visibles au premier plan de l'appareil d'un utilisateur.
2. Les **notifications push en arrière-plan** sont disponibles indépendamment du fait qu'un appareil donné ait choisi de recevoir des notifications push de cette marque. Les notifications push en arrière-plan permettent aux marques d’envoyer des notifications push silencieuses sur les appareils, c’est-à-dire des notifications push qui ne s’affichent pas intentionnellement, afin de prendre en charge des fonctionnalités clés comme le suivi des désinstallations.

Lorsqu’un profil d’utilisateur est associé à un jeton de notification push de premier plan valide associé à une application, Braze considère que l’utilisateur est « push registered » (abonné aux notifications push) pour l’application donnée. Braze fournit alors un filtre de segmentation spécifique, `Push enabled for App,`, pour identifier ces utilisateurs.

{% alert note %}
Le filtre `Push enabled for App` ne prend en compte que la présence d’un jeton de notification push de premier plan ou d’arrière-plan valide pour l’application donnée. Cependant, le filtre plus générique `Push Enabled` segmente les utilisateurs qui ont explicitement activé les notifications push pour toutes les applications de votre espace de travail. Ce nombre inclut uniquement les notifications push de premier plan et n’inclut pas les utilisateurs qui se sont désabonnés. Pour en savoir plus sur ces filtres et d'autres, consultez la rubrique [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Plusieurs utilisateurs sur un appareil

Les jetons de notification push sont spécifiques pour un appareil et une application, il n’est donc pas possible d’utiliser des jetons de notification push pour différencier plusieurs utilisateurs utilisant le même appareil.

Imaginons par exemple que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre application sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecte au sien, le jeton de notification push sera réaffecté au profil de Kim. Le jeton de notification push restera affecté au profil de Kim sur cet appareil jusqu’à ce qu’elle se déconnecte et que Charlie se reconnecte.

Une application ou un site Internet ne peuvent avoir qu’un seul abonnement aux notifications push par appareil. Lorsqu’un utilisateur se déconnecte d’un appareil ou d’un site Internet et qu’un utilisateur se connecte, le jeton de notification push est donc réaffecté au nouvel utilisateur. Cela se reflète sur le profil de l'utilisateur dans la section **Paramètres de contact** de l'onglet **Engagement :** 

![Journal des modifications du jeton de notification push dans l'onglet \*\*Engagement** du profil d'un utilisateur, qui indique quand le jeton de notification push a été transféré à un autre utilisateur, et quel était le jeton.][4]

Étant donné que les fournisseurs de notifications push (APN/FCM) n’ont aucun moyen de faire la différence entre plusieurs utilisateurs sur un même appareil, nous transmettons le jeton de notification push au dernier utilisateur qui s’est connecté pour déterminer quel utilisateur cibler sur l’appareil pour les notifications push.

## Inscription au jeton de notification push

Les plateformes gèrent l’inscription au jeton de notification push et aux permissions de différentes manières :

- **Android**:
  - **Android 13**:<br>Les autorisations de notification push doivent être demandées et accordées par l’utilisateur. Reçoit un jeton après que l'autorisation a été accordée par l'utilisateur. Votre application peut demander manuellement l'autorisation à l'utilisateur au moment opportun, mais si ce n'est pas le cas, les utilisateurs seront automatiquement invités à le faire après que votre application aura créé un [canal de notification.](https://developer.android.com/reference/android/app/NotificationChannel)
  - **Android 12 et antérieur**:<br>Tous les utilisateurs sont considérés `Subscribed` lors de leur première session quand Braze demande automatiquement un jeton de notification push. À ce stade, **les notifications push sont activées** pour l’utilisateur, avec un jeton de notification push valide pour cet appareil et un état d'abonnement par défaut défini sur `Subscribed`.<br><br>
- **iOS**: Inscription non automatique aux notifications push.
    - **iOS 12 (avec autorisation provisoire)**: <br>Votre application peut demander une [autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push) ou un push autorisé. Le push autorisé requiert l'autorisation explicite d'un utilisateur avant d'envoyer des notifications (il reçoit un jeton une fois l'autorisation accordée par l'utilisateur), tandis que [provisional push][provisional-blog] ] vous permet d'envoyer des notifications __discrètement__, directement au centre de notification, sans aucun son ni aucune alerte.
    - **iOS 11 et suivants & iOS 12 (sans autorisation provisoire)**: <br>Tous les utilisateurs doivent s’abonner explicitement pour recevoir des notifications push. Recevra un jeton après l'abonnement des utilisateurs.<br><br>
- **Web :** Vous devez demander l'abonnement explicite des utilisateurs via la boîte de dialogue d'autorisation native du navigateur. Recevra un jeton après que les utilisateurs se seront abonnés.  Contrairement à Android et iOS qui laissent votre application afficher le dialogue d’autorisation n’importe quand, certains navigateurs modernes n’afficheront l’invite que si elle est déclenchée par une action de l’utilisateur (clic de souris ou touche du clavier). Si votre site essaie de demander une autorisation de notification push lors du chargement de la page, elle sera sûrement ignorée ou étouffée par le navigateur.

| Obtenir un jeton de notification push | Envoyer un jeton de notification push |
| ---------------- | ----------------- |
| Les applications doivent être inscrites auprès d’un fournisseur de services push afin d’obtenir un jeton de notification push pour un appareil. | Les développeurs peuvent alors cibler l’appareil en utilisant le jeton de notification push généré par FCM/APN.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Vérifier l’état de l’abonnement aux notifications push de l’utilisateur

![Profil utilisateur de John Doe dont l'état de l'abonnement push est défini sur Abonné.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l’état de l’abonnement aux notifications push d’un utilisateur avec Braze :

1. **Profil utilisateur**: Vous pouvez accéder aux profils utilisateurs individuels via le tableau de bord de Braze sur la page [Recherche d'utilisateurs][5] ]. Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID externe), vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état de l'abonnement d'un utilisateur. 
<br>
2. **Exportation de l'API REST** : Vous pouvez exporter des profils utilisateurs individuels au format JSON en utilisant les endpoints d'exportation [Utilisateurs par segment][segment] ou [Utilisateurs par identifiant][identifiant]. Braze renvoie un objet jeton de notification push qui contient des informations sur l’activation de la notification par appareil.

### Vérifier le statut d’enregistrement aux notifications push

Dans l'onglet **Engagement** du profil d'un utilisateur, vous verrez **Push Registered For** suivi d'un nom d'app. Si aucune information sur l'application n'existe pour cet appareil, vous verrez deux tirets (**--**). Il y aura une entrée pour chaque appareil appartenant à l’utilisateur.

Si le nom de l’application de l’entrée de l’appareil est préfixé par `Foreground:`, l’application est autorisée à recevoir à la fois des notifications push de premier plan (visibles par l’utilisateur) et des notifications push d’arrière-plan (non visibles par l’utilisateur) sur cet appareil.

![Journal des modifications des notifications push avec un exemple de jeton de notification push.][2]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

En revanche, si le nom de l'application de l'entrée de l'appareil est préfixé par `Background:`, l'application est uniquement autorisée à recevoir des [push en arrière-plan]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) et ne peut pas afficher de notifications visibles par l'utilisateur sur cet appareil. Cela indique généralement que l’utilisateur a désactivé les notifications pour l’application sur cet appareil.

Si un jeton de notification push est déplacé vers un autre utilisateur sur le même appareil, ce premier utilisateur ne sera plus abonné.

## Gestion des jetons de notification push

Consultez le tableau suivant pour des actions qui permettent de changer les jetons de notification push ou de supprimer des profils utilisateur. 

| Action | Description |
| ------ | ----------- |
| Appel de la méthode `changeUser()` | La méthode `changeUser()` de Braze change l’ID utilisateur auquel les SDK attribuent les données de comportement de l’utilisateur. Cette méthode est généralement appelée lorsqu’un utilisateur se connecte à une application. Lorsque la méthode `changeUser()` est appelée avec un ID utilisateur différent ou nouveau sur un appareil spécifique, le jeton de notification push de cet appareil sera déplacé vers le profil Braze approprié avec l’ID utilisateur correspondant. |
| Erreur de notification push | Parmi les erreurs de notification push courantes qui entraînent la suppression des jetons, citons `MismatchSenderId`, `InvalidRegistration` et d’autres types de rejet de notification push. <br><br>Consultez notre liste complète des [erreurs de poussée][errors] les plus courantes. |
| Désinstallation de l’application | Lorsqu’un utilisateur désinstalle l’application d’un appareil, Braze supprime le jeton de notification push de l’utilisateur du profil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### À quoi cela ressemble-t-il à plus grande échelle ?

Lorsqu’un utilisateur ouvre une nouvelle application et accorde l’accès aux notifications push depuis une invite, un appel est fait aux fournisseurs de notifications push par le SDK de Braze. Lorsque cet appel est effectué, le fournisseur de notification push s’assure que tout est configuré correctement. Si c’est le cas, un jeton de notification push est transféré vers votre appareil. Lorsque ce jeton arrive, le SDK communique l’événement à Braze. Une fois que Braze reçoit le jeton du fournisseur de notifications push, nous mettons à jour ou créons un nouveau profil utilisateur. Ces utilisateurs sont maintenant considérés comme abonnés.

Si nous voulons lancer une campagne, nous créons une campagne dans Braze qui génère une charge de notifications push à envoyer au fournisseur. À partir de là, le fournisseur délivre la charge de notifications push vers l’appareil de l’utilisateur et le SDK transmet l’état de réception des messages à Braze.

![Schéma du processus de notification push susmentionné entre Braze, le client et le service de notification push d’Apple (APN) ou Firebase Cloud Messaging (FCM).][push-process]

| Étapes de l’inscription | Étapes d’envoi des messages |
| ------------------ | --------------- |
| 1\. Le client (appareil) s’inscrit auprès du fournisseur de notifications<br>2\. Le fournisseur génère et livre un jeton de notification push<br>3\. Purge des jetons dans Braze |1\. Braze envoie une charge de notifications push au fournisseur<br>2\. Le fournisseur livre la charge de notifications push à l’appareil<br>3\. SDK transmet les statistiques de messagerie à Braze |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

### Que se passe-t-il lorsqu’un utilisateur abonné supprime puis retélécharge mon application ?

Supposons qu’un utilisateur s’abonne aux notifications push, reçoit un message push, puis supprime l’application. Cela supprimera le consentement des notifications push au niveau de l’appareil. À partir de là, la première notification push renvoyée après la désinstallation entraînera automatiquement l’effacement de l’utilisateur des messages push ultérieurs. Après cela, si un utilisateur réinstalle l’application mais ne la lance pas, Braze ne sera pas en mesure d’envoyer une notification push à l’utilisateur, car les jetons de notification push n’ont pas été réautorisés pour votre application.

En outre, si un utilisateur réactive les notifications push de premier plan, il devra démarrer une session pour mettre à jour ces informations dans son profil d’utilisateur afin de commencer à recevoir des messages push.
 
### Quand les jetons de notification push expirent-ils ? {#push-token-expire}

Malheureusement, les APN et FCM ne fournissent pas vraiment ces informations. Les jetons de notification push peuvent expirer lorsqu’une application est mise à jour, lorsque les utilisateurs transfèrent leurs données vers un nouvel appareil ou lorsqu’ils réinstallent un système d’exploitation. Pour la plupart, nous n’avons pas vraiment d’informations sur les raisons pour lesquelles les fournisseurs de services push font expirer certains jetons de notification push.

Pour tenir compte de cette ambiguïté, nos intégrations de notification push SDK inscrivent toujours et purgent les jetons à l’ouverture des sessions pour assurer de disposer du jeton le plus récent.

[errors]: {{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[push-process]: {% image_buster /assets/img/push_process.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[2]: {% image_buster /assets/img/push_changelog.png %}
[push-tokens]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[3]: {% image_buster /assets/img/push_example.png %}
[4]: {% image_buster /assets/img/push_token_changelog.png %}


