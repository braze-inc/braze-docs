---
nav_title: "Pousser l'enregistrement"
article_title: "Pousser l'enregistrement"
page_order: 2
page_type: reference
description: "Cet article de référence traite de ce que signifie être enregistré pour push et de la manière dont nous envoyons des messages push et traitons les jetons push et l'enregistrement push chez Braze."
channel:
 - push

---

# Pousser l'enregistrement

> Cet article couvre le processus par lequel un utilisateur se voit attribuer un jeton push, et comment Braze envoie des messages push à vos utilisateurs.

## À propos des jetons de poussée {#push-tokens}

Lorsqu'une application demande des autorisations de push à un appareil, le fournisseur de services de push de l'appareil génère un jeton de push pour cette application. Chaque application se voit attribuer un jeton push unique et anonyme qui permet d'identifier l'appareil et l'instance de l'application en cours lors de l'envoi d'une notification push.

Gardez à l'esprit que les jetons push ne sont pas des identifiants statiques qui durent éternellement : ils peuvent être mis à jour et ils peuvent [expirer](#push-token-expire).

{% alert tip %}
Pour des détails spécifiques à la plateforme, voir [Enregistrement du jeton de poussée](#push-token-registration).
{% endalert %}

### Poussée d'avant-plan ou d'arrière-plan {#foreground-vs-background}

Les jetons push sont utilisés pour envoyer des notifications push en avant-plan et en arrière-plan.

| Type       | Nécessite-t-il un abonnement ? | Description                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Poussée d'avant-plan | Oui       | Une notification est affichée de manière visible pour l'utilisateur lorsque l'application est au premier plan.           |
| Poussée de fond | Non        | Une notification est délivrée silencieusement en arrière-plan sans être affichée. Souvent utilisé pour des fonctionnalités telles que le suivi des désinstallations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsqu'un utilisateur s'abonne aux notifications push pour votre application, il est considéré comme "enregistré", ce qui signifie qu'il peut désormais être ciblé à l'aide du filtre de segmentation `Foreground Push Enabled for App` dans Braze.

{% alert note %}
Ceci est différent du filtre de segmentation `Foreground Push Enabled`, qui est utilisé pour identifier les utilisateurs qui se sont abonnés à au moins une de vos applications, et non à une application spécifique. Pour plus d'informations, voir [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#foreground-push-enabled).
{% endalert %}

### Plusieurs utilisateurs sur un appareil

Les jetons push sont uniques à l'appareil et à l'application, ce qui signifie que les jetons push ne peuvent pas être utilisés pour cibler des utilisateurs spécifiques si plusieurs utilisateurs utilisent le même appareil.

Par exemple, supposons que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre appli sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecter au sien, le jeton push sera réattribué au profil de Kim. Le jeton push restera alors attribué au profil de Kim sur cet appareil jusqu'à ce qu'elle se déconnecte et que Charlie se reconnecte.

Une appli ou un site web ne peut avoir qu'un seul abonnement push par appareil. Ainsi, lorsqu'un utilisateur se déconnecte d'un appareil ou d'un site web et qu'un nouvel utilisateur s'y connecte, le jeton push est réattribué au nouvel utilisateur. Cela se reflète sur le profil de l'utilisateur dans la section **Paramètres de contact** de l'onglet **Engagement**:

Journal des modifications du jeton de poussée dans l'onglet \*\*Engagement** du profil d'un utilisateur, qui indique quand le jeton de poussée a été transféré à un autre utilisateur, et quel était le jeton.]({% image_buster /assets/img/push_token_changelog.png %})

Comme les fournisseurs de services de push (APN/FCM) n'ont aucun moyen de faire la distinction entre plusieurs utilisateurs sur un même appareil, nous transmettons le jeton de push au dernier utilisateur connecté afin de déterminer quel utilisateur doit être ciblé sur l'appareil pour le push.

## Enregistrement du jeton de poussée

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
| **iOS 12**      | Oui                         | Lorsqu'un utilisateur s'abonne aux notifications push, vous recevez une autorisation standard qui vous permet d'envoyer des [notifications push au premier plan](#foreground-vs-background). Toutefois, vous pouvez également demander une [autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push), qui vous permet d'envoyer des [notifications push](#foreground-vs-background) silencieuses [en arrière-plan](#foreground-vs-background) directement au centre de notification. |
| **iOS 11 et versions ultérieures** | Non                          | Tous les utilisateurs doivent explicitement s'abonner pour recevoir des notifications push. Un jeton de poussée n'est généré qu'une fois l'autorisation accordée.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}

{% tab web %}
Vous devez demander l'abonnement explicite des utilisateurs via la boîte de dialogue d'autorisation native du navigateur. Recevra un jeton après que les utilisateurs se soient abonnés. Contrairement à iOS et Android, qui permettent à votre application d'afficher l'invite de permission à tout moment, certains navigateurs modernes n'affichent l'invite que si elle est déclenchée par un "geste de l'utilisateur" (clic de souris ou frappe au clavier). Si votre site tente de demander l'autorisation de la notification push au chargement de la page, il sera probablement ignoré ou réduit au silence par le navigateur.
{% endtab %}
{% endtabs %}

### Vérification de l'état de l'abonnement push de l'utilisateur

\![Profil utilisateur de John Doe dont l'état de l'abonnement push est défini sur Abonné.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Il y a deux façons de vérifier l'état de l'abonnement push d'un utilisateur avec Braze :

- **Profil utilisateur**: Vous pouvez accéder aux profils utilisateurs individuels via le tableau de bord de Braze sur la page [Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID externe), vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état de l'abonnement d'un utilisateur.
- **Exportation de l'API REST**: Vous pouvez exporter des profils utilisateurs individuels au format JSON en utilisant les endpoints d'exportation [Utilisateurs par segmentation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze renvoie un objet de jetons de poussée qui contient des informations sur l'activation de la poussée pour chaque appareil.

### Vérification de l'état de l'enregistrement des poussées

Dans l'onglet **Engagement** du profil d'un utilisateur, vous verrez **Push Registered For** suivi d'un nom d'app. Si aucune information sur l'application n'existe pour cet appareil, vous verrez deux tirets**(--**). Il y aura une entrée pour chaque appareil appartenant à l'utilisateur.

Si le nom de l'application de l'entrée de l'appareil est préfixé par `Foreground:`, l'application est autorisée à recevoir des notifications push au premier plan (visibles par l'utilisateur) et des notifications push en arrière-plan (non visibles par l'utilisateur) sur cet appareil.

\![Journal des modifications avec un exemple de jeton de poussée.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

En revanche, si le nom de l'application de l'entrée de l'appareil est précédé de `Background:`, l'application est uniquement autorisée à recevoir des [push en arrière-plan]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) et ne peut pas afficher de notifications visibles par l'utilisateur sur cet appareil. Cela indique généralement que l'utilisateur a désactivé les notifications pour l'appli sur cet appareil.

Si un jeton push est transféré à un autre utilisateur sur le même appareil, ce premier utilisateur ne sera plus enregistré en push.

## Gestion des jetons d'accès (push token)

Consultez le tableau suivant pour connaître les actions qui conduisent à la modification ou à la suppression des jetons de poussée dans les profils utilisateurs. 

| Action | Description |
| ------ | ----------- |
| `changeUser()` méthode appelée | La méthode Braze `changeUser()` modifie l'ID de l'utilisateur auquel les SDK attribuent les données comportementales. Cette méthode est généralement appelée lorsqu'un utilisateur se connecte à une application. Lorsque `changeUser()` est appelé avec un ID utilisateur différent ou nouveau sur un appareil spécifique, le jeton push de cet appareil sera déplacé vers le profil utilisateur approprié de Braze avec l'ID utilisateur correspondant. |
| Une erreur de poussée se produit | Parmi les erreurs de push les plus courantes qui entraînent la suppression du jeton, citons `MismatchSenderId`, `InvalidRegistration`, et d'autres types de rebonds de push. <br><br>Consultez notre liste complète des [erreurs de poussée]({{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid) les plus courantes. |
| Désinstallation par l'utilisateur | Lorsqu'un utilisateur désinstalle l'application d'un appareil, Braze supprime le jeton push de l'utilisateur du profil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### À quoi cela ressemble-t-il à plus grande échelle ?

Lorsqu'un utilisateur ouvre une nouvelle application et accorde l'accès push à partir d'une invite push, un appel est effectué depuis le SDK Braze vers les fournisseurs push. Lors de cet appel, le fournisseur de services push vérifie que tout est correctement configuré. Si c'est le cas, un jeton de poussée est transmis à votre appareil. Lorsque ce jeton arrive, le SDK le communique à Braze. Une fois que Braze a reçu le jeton du fournisseur de push, nous mettons à jour ou créons un nouveau profil utilisateur. Ces utilisateurs sont désormais considérés comme enregistrés.

Si nous voulons lancer une campagne, nous créons une campagne dans Braze qui génère une charge utile push à envoyer au fournisseur push. À partir de là, le fournisseur transmet la charge utile push à l'appareil de l'utilisateur et le SDK transmet l'état de l'envoi des messages à Braze.

Un organigramme qui mappe le processus de push susmentionné entre Braze, le personnalisé, et Apple Push Notification Service ou Firebase Cloud Messaging.]({% image_buster /assets/img/push_process.png %})

| Les étapes de l'inscription | Étapes de l'envoi des messages |
| ------------------ | --------------- |
| 1\. Le client (appareil) s'inscrit auprès du fournisseur de services push<br>2\. Le fournisseur génère et délivre un jeton de poussée.<br>3\. Jetons de chasse en Braze |1\. Braze envoie une charge utile "push" au fournisseur<br>2\. Le fournisseur transmet la charge utile push à l'appareil.<br>3\. Le SDK transmet les statistiques d'envoi des messages à Braze |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Questions fréquemment posées

### Que se passe-t-il lorsqu'un utilisateur bénéficiant d'un abonnement supprime mon application et la télécharge à nouveau ?

Supposons qu'un utilisateur s'abonne à la fonction "push", qu'il reçoive des messages push et qu'il supprime l'application par la suite. Cela supprimera le consentement poussé au niveau de l'appareil. À partir de là, le premier message push renvoyé après la désinstallation entraînera automatiquement l'abonnement de cet utilisateur aux futurs envois de messages push. Après cela, si un utilisateur réinstalle l'application mais ne la lance pas, Braze ne pourra pas lui envoyer de push car les jetons de push n'ont pas été réattribués pour votre application.

En outre, si un utilisateur devait réactiver l'envoi de messages en avant-plan, il lui faudrait démarrer une session pour mettre à jour ces informations dans son profil utilisateur afin de commencer à recevoir des messages en avant-plan.
 
### Quand les jetons de poussée expirent-ils ? {#push-token-expire}

Malheureusement, les APN et les FCM ne définissent pas vraiment cette notion. Les jetons push peuvent expirer lorsqu'une appli est mise à jour, lorsque les utilisateurs transfèrent leurs données sur un nouvel appareil ou lorsqu'ils réinstallent un système d'exploitation. Pour la plupart, nous n'avons pas vraiment d'informations sur les raisons pour lesquelles les fournisseurs de services de push expirent certains jetons de push.

Pour tenir compte de cette ambiguïté, nos intégrations SDK push enregistrent et purgent toujours les jetons au début de la session pour s'assurer que nous disposons du jeton le plus récent.
