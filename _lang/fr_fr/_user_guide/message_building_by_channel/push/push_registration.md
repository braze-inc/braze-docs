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

## 

 







### 



|        |  | Description                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
|  |        |            |
|  |         |   |




{% alert note %}
 


### 



Imaginons par exemple que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre application sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecte au sien, le jeton de notification push sera réaffecté au profil de Kim. Le jeton de notification push restera affecté au profil de Kim sur cet appareil jusqu’à ce qu’elle se déconnecte et que Charlie se reconnecte.

Une application ou un site Internet ne peuvent avoir qu’un seul abonnement aux notifications push par appareil. Lorsqu’un utilisateur se déconnecte d’un appareil ou d’un site Internet et qu’un utilisateur se connecte, le jeton de notification push est donc réaffecté au nouvel utilisateur. Cela se reflète sur le profil de l'utilisateur dans la section **Paramètres de contact** de l'onglet **Engagement :** 



Étant donné que les fournisseurs de notifications push (APN/FCM) n’ont aucun moyen de faire la différence entre plusieurs utilisateurs sur un même appareil, nous transmettons le jeton de notification push au dernier utilisateur qui s’est connecté pour déterminer quel utilisateur cibler sur l’appareil pour les notifications push.

## Inscription au jeton de notification push

 



 

|        |                                                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          |   |
|  |   |




  

|                          |  |                                                                                                                                                      |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       |                          |   |
|  |                           | Tous les utilisateurs doivent s’abonner explicitement pour recevoir des notifications push.                                      |




Vous devez demander l'abonnement explicite des utilisateurs via la boîte de dialogue d'autorisation native du navigateur. Recevra un jeton après que les utilisateurs se seront abonnés. Contrairement à Android et iOS qui laissent votre application afficher le dialogue d’autorisation n’importe quand, certains navigateurs modernes n’afficheront l’invite que si elle est déclenchée par une action de l’utilisateur (clic de souris ou touche du clavier). Si votre site essaie de demander une autorisation de notification push lors du chargement de la page, elle sera sûrement ignorée ou étouffée par le navigateur.



### 





- **Profil utilisateur**:  Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID externe), vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état de l'abonnement d'un utilisateur.
-   Braze renvoie un objet jeton de notification push qui contient des informations sur l’activation de la notification par appareil.

### Vérifier le statut d’enregistrement aux notifications push

Dans l'onglet **Engagement** du profil d'un utilisateur, vous verrez **Push Registered For** suivi d'un nom d'app. Si aucune information sur l'application n'existe pour cet appareil, vous verrez deux tirets (**--**). Il y aura une entrée pour chaque appareil appartenant à l’utilisateur.

Si le nom de l’application de l’entrée de l’appareil est préfixé par `Foreground:`, l’application est autorisée à recevoir à la fois des notifications push de premier plan (visibles par l’utilisateur) et des notifications push d’arrière-plan (non visibles par l’utilisateur) sur cet appareil.



En revanche, si le nom de l'application de l'entrée de l'appareil est préfixé par `Background:`, l'application est uniquement autorisée à recevoir des [push en arrière-plan]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) et ne peut pas afficher de notifications visibles par l'utilisateur sur cet appareil. Cela indique généralement que l’utilisateur a désactivé les notifications pour l’application sur cet appareil.

Si un jeton de notification push est déplacé vers un autre utilisateur sur le même appareil, ce premier utilisateur ne sera plus abonné.

## Gestion des jetons de notification push

Consultez le tableau suivant pour des actions qui permettent de changer les jetons de notification push ou de supprimer des profils utilisateur. 

| Action | Description |
| ------ | ----------- |
| Appel de la méthode `changeUser()` | La méthode `changeUser()` de Braze change l’ID utilisateur auquel les SDK attribuent les données de comportement de l’utilisateur. Cette méthode est généralement appelée lorsqu’un utilisateur se connecte à une application. Lorsque la méthode `changeUser()` est appelée avec un ID utilisateur différent ou nouveau sur un appareil spécifique, le jeton de notification push de cet appareil sera déplacé vers le profil Braze approprié avec l’ID utilisateur correspondant. |
| Erreur de notification push | Parmi les erreurs de notification push courantes qui entraînent la suppression des jetons, citons `MismatchSenderId`, `InvalidRegistration` et d’autres types de rejet de notification push. <br><br> |
| Désinstallation de l’application | Lorsqu’un utilisateur désinstalle l’application d’un appareil, Braze supprime le jeton de notification push de l’utilisateur du profil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### À quoi cela ressemble-t-il à plus grande échelle ?

Lorsqu’un utilisateur ouvre une nouvelle application et accorde l’accès aux notifications push depuis une invite, un appel est fait aux fournisseurs de notifications push par le SDK de Braze. Lorsque cet appel est effectué, le fournisseur de notification push s’assure que tout est configuré correctement. Si c’est le cas, un jeton de notification push est transféré vers votre appareil. Lorsque ce jeton arrive, le SDK communique l’événement à Braze. Une fois que Braze reçoit le jeton du fournisseur de notifications push, nous mettons à jour ou créons un nouveau profil utilisateur. Ces utilisateurs sont maintenant considérés comme abonnés.

Si nous voulons lancer une campagne, nous créons une campagne dans Braze qui génère une charge de notifications push à envoyer au fournisseur. À partir de là, le fournisseur délivre la charge de notifications push vers l’appareil de l’utilisateur et le SDK transmet l’état de réception des messages à Braze.



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
