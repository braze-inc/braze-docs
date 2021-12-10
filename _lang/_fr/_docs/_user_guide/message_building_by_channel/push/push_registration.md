---
nav_title: "Inscription Push"
article_title: Inscription Push
page_order: 2
page_type: Référence
description: "Cet article de référence décrit ce que signifie être enregistré pour push et comment nous envoyons des messages push et traitons avec des jetons push au Brésil."
channel:
  - Pousser
---

# Inscription Push

> Cet article couvre le processus par lequel un utilisateur reçoit un jeton push et comment Braze envoie des messages push à vos utilisateurs.

## Pousser les jetons

Comprendre les jetons de poussée et ce qu'ils sont est un élément fondamental de compréhension de la manière dont nous envoyons des messages push ici au Brésil. Un jeton push est un identifiant que les expéditeurs utilisent pour cibler des périphériques spécifiques avec une notification push. Si un appareil n'a pas de jeton push, il n'y a aucun moyen de lui envoyer de push.

Les jetons Push sont générés par les fournisseurs de services push. Braze se connecte avec les fournisseurs de services push comme Firebase Cloud Messaging Service (FCM) pour Android et Apple Push Notification Service (APNs) pour iOS, et ces fournisseurs envoient des jetons uniques qui identifient votre application. Chaque appareil a un jeton unique qui est utilisé pour la messagerie. Les jetons peuvent [expirer](#push-token-expire) ou être mis à jour.

## Enregistrement du jeton Push

Les plateformes traitent de l'enregistrement des jetons push de différentes manières :

- __Android__: automatiquement enregistré pour push. Recevoir un jeton dès qu'un utilisateur télécharge et ouvre une application.
- __iOS__: Pas automatiquement enregistré pour push.
    - __iOS 12 (avec autorisation provisoire)__: <br>Si vous avez [autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push) configurée, vous pouvez envoyer des notifications en mode silencieux au Centre de Notifications de l'appareil. Ces notifications peuvent inviter les utilisateurs à décider de continuer à recevoir des notifications. Leur état d'abonnement dépend de la réponse de l'utilisateur à cette invitation.
    - __iOS 11 et ultérieur & iOS 12 (sans autorisation provisoire)__: <br>La notification push native apparaît pour les nouveaux utilisateurs d'une application. Les utilisateurs répondent à cette invite en sélectionnant "autoriser" ou "refuser". __Refuser__ refuse l'enregistrement de jetons push, refusant donc les notifications push à leur téléphone depuis cette application. __Autoriser__ à s'inscrire et à créer un nouveau jeton push, puis là.
- __Web :__ Non enregistré automatiquement pour push. L'invite de notification de push natif apparaît pour les nouveaux utilisateurs de votre site web. Les utilisateurs répondent à cette invite en sélectionnant autoriser ou bloquer. __Bloquer__ refuse l'enregistrement de jetons push, refusant donc les notifications push à leur téléphone depuis cette application. __Autoriser__ à s'inscrire et à créer un nouveau jeton push, puis là.

| Obtenir un jeton push                                                                                                  | Envoyer un jeton push                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Les applications doivent s'inscrire auprès d'un fournisseur de push afin d'obtenir un jeton push pour un périphérique. | Les développeurs peuvent alors cibler l'appareil en utilisant le jeton push généré par FCM/APNs. |
{: .reset-td-br-1 .reset-td-br-2}

### Vérifier l'état de l'abonnement push de l'utilisateur

![Exemple Push]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Il y a deux façons de vérifier l'état de l'abonnement push d'un utilisateur avec Braze :

1. __Profil utilisateur :__ Vous pouvez accéder à des profils utilisateur individuels via le tableau de bord Braze sur la page **Recherche d'utilisateur**. Ici, vous pouvez rechercher des profils d'utilisateurs par adresse e-mail, numéro de téléphone ou ID d'utilisateur externe. Une fois dans un profil utilisateur, vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état d'abonnement d'un utilisateur. <br><br>
2. __Exportation de l'API Rest :__ Vous pouvez exporter des profils utilisateur individuels au format JSON en utilisant l'export [Utilisateurs par segment][segment] ou [Utilisateurs par identifiant][identifier] points de terminaison. Braze retournera un objet jeton push qui contient des informations d'activation push par appareil.

## Gestion des jetons Push

Consultez le graphique ci-dessous pour les actions qui conduisent à pousser des changements de jetons ou à les supprimer des profils d'utilisateurs.

| Action                           | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `changeUser()` méthode appelée   | La méthode Braze `changeUser()` permet de changer l'ID utilisateur auquel les SDK assignent les données de comportement de l'utilisateur. Cette méthode est généralement appelée lorsqu'un utilisateur se connecte à une application. Quand `changeUser()` est appelé avec un identifiant utilisateur différent ou nouveau sur un périphérique spécifique, le jeton push de cet appareil sera déplacé vers le profil Braze approprié avec l'identifiant d'utilisateur correspondant. |
| Une erreur est survenue          | Certaines erreurs de push courantes qui conduisent à la suppression de jetons incluent `MismatchSenderId`, `InvalidRegistration`, et d'autres types de rebonds push. <br><br>Consultez notre liste complète d'erreurs de push [courantes.][errors].                                                                                                                                                                                                                      |
| Désinstallation de l'utilisateur | Lorsqu'un utilisateur désinstalle l'application d'un périphérique, Braze supprime le jeton de push de l'utilisateur du profil.                                                                                                                                                                                                                                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

### À quoi cela ressemble-t-il à plus grande échelle?

Lorsqu'un utilisateur ouvre une nouvelle application, si push a été configuré correctement, un appel est fait à partir du Braze SDK aux fournisseurs de push. Lorsque cet appel est effectué, le fournisseur de push vérifie si tout est correctement configuré. Si c'est le cas, un jeton de push est passé dans votre appareil. Quand ce jeton arrivera, le SDK le communique à Braze. Une fois que Braze a reçu le jeton du fournisseur de push, nous mettons à jour ou créons un nouveau profil d'utilisateur. Ces utilisateurs sont maintenant considérés comme enregistrés.

Si nous voulons lancer une campagne, nous créons une campagne à Braze qui génère une charge utile push à envoyer au fournisseur de push. À partir de là, le fournisseur livre la charge utile push au périphérique de l'utilisateur et le SDK passe l'état de la messagerie à Braze.

!\[Picture\]\[push-process\]

| Étapes d'inscription                                                                                                                                        | Étapes de messagerie                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Le client (appareil) s'inscrit au fournisseur de push<br>2. Le fournisseur génère et délivre le jeton Push<br>3. Vider les jetons dans Braze | 1. Braze envoie un bloc push au fournisseur<br>2. Fournisseur délivre la charge utile de push sur l'appareil<br>3. SDK transmet les statistiques de messagerie à Braze |
{: .reset-td-br-1 .reset-td-br-2}

## Foire aux questions

### Que se passe-t-il lorsqu'un utilisateur opté supprime puis retélécharge mon application ?

Supposons qu'un utilisateur opte pour push, reçoive des messages push, puis supprime ensuite l'application. Cela supprimera le consentement push au niveau de l'appareil. À partir d'ici, le premier rebond après la désinstallation entraînera automatiquement que cet utilisateur soit exclu des futurs messages push. Après cela, si un utilisateur devait réinstaller l'application mais pas la lancer, Braze ne pourra pas envoyer de push à l'utilisateur car les jetons push n'ont pas été ré-accordés pour votre application.

De plus, si un utilisateur devait réactiver la poussée au premier plan, il faudrait un démarrage de session pour mettre à jour ces informations dans leur profil d'utilisateur pour commencer à recevoir des messages push.

### Dans quelles circonstances les jetons de poussée expirent-ils? {#push-token-expire}

Malheureusement, les APN et FCM ne le définissent pas vraiment. Les jetons Push peuvent expirer lorsqu'une application est mise à jour, lorsque les utilisateurs transfèrent leurs données vers un nouvel appareil ou lorsqu'ils réinstallent un système d'exploitation. Pour la plupart, nous n'avons pas vraiment de idée de pourquoi les fournisseurs de push expireront certains jetons de push.

Pour tenir compte de cette ambiguïté, nos intégrations push SDK s'enregistrent toujours et vider les jetons lors de la session commencent à nous assurer que nous avons le jeton le plus à jour.
[push-process]: {% image_buster /assets/img/push_process.png %}


[errors]: {{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
