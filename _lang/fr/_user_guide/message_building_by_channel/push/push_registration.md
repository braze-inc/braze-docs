---
nav_title: "Inscription aux notifications push"
article_title: Inscription aux notifications push
page_order: 2
page_type: reference
description: "Cet article de référence explique ce que signifie être inscrit aux notifications push et comment nous envoyons des messages push et nous traitons les jetons de notification push dans Braze."
channel:
  - notification push

---

# Inscription aux notifications push

> Cet article couvre le processus par lequel un utilisateur reçoit un jeton de notification push et comment Braze envoie des messages push à vos utilisateurs.

## Jetons de notification push

La compréhension des jetons de notification push et de leur mécanisme est un élément fondamental pour maîtriser la manière dont nous envoyons des messages push depuis Braze. Un jeton de notification push est un identifiant qui permet aux expéditeurs de cibler des appareils spécifiques avec une notification push. Si un appareil n’a pas de jeton de notification push, il n’y a aucun moyen d’y envoyer de notification push.

Les jetons de notification push sont générés par des fournisseurs de services push. Braze se connecte à des fournisseurs de services push comme Firebase Cloud Messaging Service (FCMs) pour Android et Apple Push Notification Service (APN) pour iOS, et ces fournisseurs envoient des jetons d’appareil uniques qui identifient votre application. Chaque appareil possède un jeton unique utilisé pour la réception de messages. Les jetons peuvent [expirer](#push-token-expire) ou être mis à jour.

## Inscription au jeton de notification push

Les plateformes gèrent l’inscription au jeton de notification push de différentes manières :

- **Android**: Inscription automatique aux notifications push. Reçoit un jeton dès que l’utilisateur télécharge et ouvre une application.
- **iOS**: Inscription non automatique aux notifications push.
    - **iOS 12 (avec autorisation provisoire)** : <br>
Si vous avez configuré l’[autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push), vous pouvez envoyer des notifications silencieuses au Centre de notification de l’appareil. Ces notifications peuvent inviter les utilisateurs à décider de continuer à recevoir des notifications. Leur état d’abonnement aux notifications push varie selon la réponse de l’utilisateur à cette invite. 
    - **iOS 11 et versions ultérieures et iOS 12 (sans autorisation provisoire)** : <br>
L’invite de notification push native s’affiche pour les nouveaux utilisateurs d’une application. Les utilisateurs répondent à cette invite en sélectionnant Allow (Autoriser) ou Deny (Refuser). **Deny** refuse l’inscription au jeton de notification push, ce qui rejette les notifications push de cette application sur leur téléphone. **Allow** inscrit et crée un nouveau jeton de notification push, à l’instant pour l’application.
- **Web :** Inscription non automatique aux notifications push. L’invite de notification push native s’affiche pour les nouveaux utilisateurs de votre site Web. Les utilisateurs répondent à cette invite en sélectionnant Allow (Autoriser) ou Block (Bloquer). **Block** bloque l’inscription au jeton de notification push, ce qui rejette les notifications push de cette application sur leur téléphone. **Allow** inscrit et crée un nouveau jeton de notification push, à l’instant pour l’application.

| Obtenir un jeton de notification push | Envoyer un jeton de notification push |
| ---------------- | ----------------- |
| Les applications doivent être inscrites auprès d’un fournisseur de services push afin d’obtenir un jeton de notification push pour un appareil. | Les développeurs peuvent alors cibler l’appareil en utilisant le jeton de notification push généré par FCM/APN.|
{: .reset-td-br-1 .reset-td-br-2}

### Vérifier l’état de l’abonnement aux notifications push de l’utilisateur

![Profil utilisateur de John Doe avec son état d’abonnement dans l’onglet Engagement comme Subscribed to Email (Abonné à E-mail) et Subscribed to Push (Abonné à notification push).]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l’état de l’abonnement aux notifications push d’un utilisateur avec Braze :

1. **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze sur la page **User Search** (Recherche utilisateur). Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Une fois dans un profil utilisateur, sous l’onglet **Engagement**, vous pouvez afficher et modifier manuellement l’état d’abonnement de l’utilisateur. <br>
<br>

2. **Rest API Export (Exportation d’API Rest) :** Vous pouvez exporter des profils utilisateur individuels au format JSON en utilisant les endpoints d’exportation [Users by segment][segment] (Utilisateurs par segment) ou [Users by identifier][identifier] (Utilisateurs par identifiant). Braze renvoie un objet jeton de notification push qui contient des informations sur l’activation de la notification par appareil.

## Gestion des jetons de notification push

Consultez le tableau suivant pour des actions qui permettent de changer les jetons de notification push ou de supprimer des profils utilisateur. 

| Action | Description |
| ------ | ----------- |
| Appel de la méthode `changeUser()` | La méthode `changeUser()` de Braze change l’ID utilisateur auquel les SDK attribuent les données de comportement de l’utilisateur. Cette méthode est généralement appelée lorsqu’un utilisateur se connecte à une application. Lorsque la méthode `changeUser()` est appelée avec un ID utilisateur différent ou nouveau sur un appareil spécifique, le jeton de notification push de cet appareil sera déplacé vers le profil Braze approprié avec l’ID utilisateur correspondant. |
| Erreur de notification push | Parmi les erreurs de notification push courantes qui entraînent la suppression des jetons, citons `MismatchSenderId`, `InvalidRegistration` et d’autres types de rejet de notification push. <br>
<br>
Consultez notre liste complète des erreurs courantes de [notification push][errors]. |
| Désinstallation de l’application | Lorsqu’un utilisateur désinstalle l’application d’un appareil, Braze supprime le jeton de notification push de l’utilisateur du profil. |
{: .reset-td-br-1 .reset-td-br-2}

### À quoi cela ressemble-t-il à plus grande échelle ?

Lorsqu’un utilisateur ouvre une nouvelle application, si la notification push a été configurée correctement, un appel est effectué depuis le SDK Braze vers les fournisseurs de notification push. Lorsque cet appel est effectué, le fournisseur de notification push s’assure que tout est configuré correctement. Si c’est le cas, un jeton de notification push est transféré vers votre appareil. Lorsque ce jeton arrive, le SDK communique l’événement à Braze. Une fois que Braze reçoit le jeton du fournisseur de notification push, nous mettons à jour ou créons un nouveau profil utilisateur. Ces utilisateurs sont maintenant considérés comme abonnés.

Si nous voulons lancer une campagne, nous créons une campagne dans Braze qui génère une charge de notifications push à envoyer au fournisseur. À partir de là, le fournisseur délivre la charge de notifications push vers l’appareil de l’utilisateur et le SDK transmet l’état de réception des messages à Braze.

![Schéma du processus de notification push susmentionné entre Braze, le client et le service de notification push d’Apple (APN) ou la messagerie cloud de Firebase (FCM).][push-process]

| Étapes de l’inscription | Étapes d’envoi des messages |
| ------------------ | --------------- |
| 1. Le client (appareil) s’inscrit auprès du fournisseur de notifications push<br>
2. Le fournisseur génère et livre un jeton de notification push<br>
3. Purge des jetons dans Braze |1. Braze envoie une charge de notifications push au fournisseur<br>
2. Le fournisseur livre la charge de notifications push à l’appareil<br>
3. SDK transmet les statistiques de messagerie à Braze |
{: .reset-td-br-1 .reset-td-br-2}

## Foire aux Questions

### Que se passe-t-il lorsqu’un utilisateur abonné supprime puis retélécharge mon application ?

Supposons qu’un utilisateur s’abonne aux notifications push, reçoit un message push, puis supprime l’application. Cela supprimera le consentement des notifications push au niveau de l’appareil. À partir de là, la première notification push renvoyée après la désinstallation entraînera automatiquement l’effacement de l’utilisateur des messages push ultérieurs. Après cela, si un utilisateur réinstalle l’application mais ne la lance pas, Braze ne sera pas en mesure d’envoyer une notification push à l’utilisateur, car les jetons de notification push n’ont pas été réautorisés pour votre application.

En outre, si un utilisateur réactive les notifications push de premier plan, il devra démarrer une session pour mettre à jour ces informations dans son profil d’utilisateur afin de commencer à recevoir des messages push.

### Dans quelles circonstances les jetons de notification push expirent-ils ? {#push-token-expire}

Malheureusement, les APN et FCM ne fournissent pas vraiment ces informations. Les jetons de notification push peuvent expirer lorsqu’une application est mise à jour, lorsque les utilisateurs transfèrent leurs données vers un nouvel appareil ou lorsqu’ils réinstallent un système d’exploitation. Pour la plupart, nous n’avons pas vraiment d’informations sur les raisons pour lesquelles les fournisseurs de services push font expirer certains jetons de notification push.

Pour tenir compte de cette ambiguïté, nos intégrations de notification push SDK inscrivent toujours et purgent les jetons à l’ouverture des sessions pour assurer de disposer du jeton le plus récent.


[errors]: {{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[push-process]: {% image_buster /assets/img/push_process.png %}
