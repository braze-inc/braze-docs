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

## À propos des jetons de poussée {#push-tokens}

Lorsqu'une application demande des autorisations de push à un appareil, le fournisseur de services de push de l'appareil génère un jeton de push pour cette application. Chaque application se voit attribuer un jeton push unique et anonyme qui permet d'identifier l'appareil et l'instance de l'application en cours lors de l'envoi d'une notification push.

Gardez à l'esprit que les jetons push ne sont pas des identifiants statiques éternels : ils peuvent être mis à jour et [expirer](#push-token-expire).

{% alert tip %}
Pour des détails spécifiques à la plateforme, voir [Enregistrement du jeton de poussée](#push-token-registration).
{% endalert %}

### Poussée d'avant-plan ou d'arrière-plan {#foreground-vs-background}

Les jetons push sont utilisés pour envoyer des notifications push en avant-plan et en arrière-plan.

| Type       | Nécessite-t-il un abonnement ? | Description                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Poussée de premier plan | Oui       | Une notification est affichée de manière visible pour l'utilisateur lorsque l'application est au premier plan.           |
| Notification push d’arrière-plan | Non        | Une notification est délivrée silencieusement en arrière-plan sans être affichée. Souvent utilisé pour des fonctionnalités telles que le suivi des désinstallations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsqu'un utilisateur s'abonne aux notifications push pour votre application, il est considéré comme "enregistré", ce qui signifie qu'il peut désormais être ciblé à l'aide du filtre de segmentation `Push enabled for App` dans Braze.

{% alert note %}
Ceci est différent du filtre de segmentation `Push Enabled`, qui est utilisé pour identifier les utilisateurs qui se sont abonnés à au moins une de vos applications, et non à une application spécifique. Pour plus d'informations, voir [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#push-enabled).
{% endalert %}

### Plusieurs utilisateurs sur un appareil

Les jetons push sont uniques à l'appareil et à l'application, ce qui signifie que les jetons push ne peuvent pas être utilisés pour cibler des utilisateurs spécifiques si plusieurs utilisateurs utilisent le même appareil.

Imaginons par exemple que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre application sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecte au sien, le jeton de notification push sera réaffecté au profil de Kim. Le jeton de notification push restera affecté au profil de Kim sur cet appareil jusqu’à ce qu’elle se déconnecte et que Charlie se reconnecte.

Une application ou un site Internet ne peuvent avoir qu’un seul abonnement aux notifications push par appareil. Lorsqu’un utilisateur se déconnecte d’un appareil ou d’un site Internet et qu’un utilisateur se connecte, le jeton de notification push est donc réaffecté au nouvel utilisateur. Cela se reflète sur le profil de l'utilisateur dans la section **Paramètres de contact** de l'onglet **Engagement :** 

![Journal des modifications du jeton de poussée dans l'onglet \*\*Engagement** du profil d'un utilisateur, qui indique quand le jeton de poussée a été transféré à un autre utilisateur, et quel était le jeton.]({% image_buster /assets/img/push_token_changelog.png %})

Étant donné que les fournisseurs de notifications push (APN/FCM) n’ont aucun moyen de faire la différence entre plusieurs utilisateurs sur un même appareil, nous transmettons le jeton de notification push au dernier utilisateur qui s’est connecté pour déterminer quel utilisateur cibler sur l’appareil pour les notifications push.

## Inscription au jeton de notification push

Chaque plateforme d'appareil gère différemment l'enregistrement des jetons de poussée. Reportez-vous à ce qui suit pour les détails spécifiques à la plate-forme :

{% tabs local %}
{% tab android %}
Lorsque votre application est installée, un jeton push est automatiquement généré pour votre application - cependant, il ne peut être utilisé que pour les [notifications push en arrière-plan](#foreground-vs-background) jusqu'à ce que l'utilisateur opte explicitement pour cette option. En outre, l'enregistrement est géré différemment selon les versions d'Android :

| Version       | Détails                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13**         | L'autorisation de pousser doit être demandée et accordée par l'utilisateur. Votre application peut demander l'autorisation manuellement, ou les utilisateurs seront invités automatiquement à le faire après la création d'un [canal de notification](https://developer.android.com/reference/android/app/NotificationChannel). |
| **Android 12 et versions antérieures** | Tous les utilisateurs sont considérés comme `Subscribed` après leur première session. Braze demande automatiquement un jeton push à ce stade, rendant l'utilisateur activé par push avec un jeton valide et un état d'abonnement par défaut de `Subscribed`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab ios %}
iOS ne génère pas automatiquement des jetons push pour une app lorsqu'elle est installée. En outre, l'enregistrement est géré différemment selon les versions d'iOS : 

| Version                         | Autorisation provisoire ? | Détails                                                                                                                                                     |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12**      | Oui                         | Lorsqu'un utilisateur s'abonne aux notifications push, vous recevez une autorisation standard qui vous permet d'envoyer des [notifications push au premier plan](#foreground-vs-background). Toutefois, vous pouvez également demander une [autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push), qui vous permet d'envoyer des [notifications push silencieuses](#foreground-vs-background) en arrière-plan directement au centre de notification. |
| **iOS 11 et versions ultérieures** | Non                          | Tous les utilisateurs doivent s’abonner explicitement pour recevoir des notifications push. Un jeton de poussée n'est généré qu'une fois l'autorisation accordée.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}

{% tab web %}
Vous devez demander l'abonnement explicite des utilisateurs via la boîte de dialogue d'autorisation native du navigateur. Recevra un jeton après que les utilisateurs se seront abonnés. Contrairement à Android et iOS qui laissent votre application afficher le dialogue d’autorisation n’importe quand, certains navigateurs modernes n’afficheront l’invite que si elle est déclenchée par une action de l’utilisateur (clic de souris ou touche du clavier). Si votre site essaie de demander une autorisation de notification push lors du chargement de la page, elle sera sûrement ignorée ou étouffée par le navigateur.
{% endtab %}
{% endtabs %}

### Vérification de l'état de l'abonnement push de l'utilisateur

![Profil utilisateur de John Doe dont l'état de l'abonnement push est défini sur Abonné.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Il y a deux façons de vérifier l'état de l'abonnement push d'un utilisateur avec Braze :

- **Profil utilisateur**: Vous pouvez accéder aux profils utilisateurs individuels via le tableau de bord de Braze sur la page [Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID externe), vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état de l'abonnement d'un utilisateur.
- **Exportation de l'API REST**: Vous pouvez exporter des profils utilisateurs individuels au format JSON à l'aide des endpoints d'exportation [Utilisateurs par segmentation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze renvoie un objet jeton de notification push qui contient des informations sur l’activation de la notification par appareil.

### Vérifier le statut d’enregistrement aux notifications push

Dans l'onglet **Engagement** du profil d'un utilisateur, vous verrez **Push Registered For** suivi d'un nom d'app. Si aucune information sur l'application n'existe pour cet appareil, vous verrez deux tirets (**--**). Il y aura une entrée pour chaque appareil appartenant à l’utilisateur.

Si le nom de l’application de l’entrée de l’appareil est préfixé par `Foreground:`, l’application est autorisée à recevoir à la fois des notifications push de premier plan (visibles par l’utilisateur) et des notifications push d’arrière-plan (non visibles par l’utilisateur) sur cet appareil.

![Journal des modifications avec un exemple de jeton.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

En revanche, si le nom de l'application de l'entrée de l'appareil est préfixé par `Background:`, l'application est uniquement autorisée à recevoir des [push en arrière-plan]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) et ne peut pas afficher de notifications visibles par l'utilisateur sur cet appareil. Cela indique généralement que l’utilisateur a désactivé les notifications pour l’application sur cet appareil.

Si un jeton de notification push est déplacé vers un autre utilisateur sur le même appareil, ce premier utilisateur ne sera plus abonné.

## Gestion des jetons de notification push

Consultez le tableau suivant pour des actions qui permettent de changer les jetons de notification push ou de supprimer des profils utilisateur. 

| Action | Description |
| ------ | ----------- |
| Appel de la méthode `changeUser()` | La méthode `changeUser()` de Braze change l’ID utilisateur auquel les SDK attribuent les données de comportement de l’utilisateur. Cette méthode est généralement appelée lorsqu’un utilisateur se connecte à une application. Lorsque la méthode `changeUser()` est appelée avec un ID utilisateur différent ou nouveau sur un appareil spécifique, le jeton de notification push de cet appareil sera déplacé vers le profil Braze approprié avec l’ID utilisateur correspondant. |
| Erreur de notification push | Parmi les erreurs de notification push courantes qui entraînent la suppression des jetons, citons `MismatchSenderId`, `InvalidRegistration` et d’autres types de rejet de notification push. <br><br>Consultez notre liste complète des [erreurs de poussée]({{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid) les plus courantes. |
| Désinstallation de l’application | Lorsqu’un utilisateur désinstalle l’application d’un appareil, Braze supprime le jeton de notification push de l’utilisateur du profil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### À quoi cela ressemble-t-il à plus grande échelle ?

Lorsqu’un utilisateur ouvre une nouvelle application et accorde l’accès aux notifications push depuis une invite, un appel est fait aux fournisseurs de notifications push par le SDK de Braze. Lorsque cet appel est effectué, le fournisseur de notification push s’assure que tout est configuré correctement. Si c’est le cas, un jeton de notification push est transféré vers votre appareil. Lorsque ce jeton arrive, le SDK communique l’événement à Braze. Une fois que Braze reçoit le jeton du fournisseur de notifications push, nous mettons à jour ou créons un nouveau profil utilisateur. Ces utilisateurs sont maintenant considérés comme abonnés.

Si nous voulons lancer une campagne, nous créons une campagne dans Braze qui génère une charge de notifications push à envoyer au fournisseur. À partir de là, le fournisseur délivre la charge de notifications push vers l’appareil de l’utilisateur et le SDK transmet l’état de réception des messages à Braze.

![Un organigramme qui mappe le processus de push susmentionné entre Braze, le client, et le service de notification push d'Apple ou Firebase Cloud Messaging.]({% image_buster /assets/img/push_process.png %})

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
