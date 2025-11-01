---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes
page_order: 9
description: "Cet article d'aide vous explique comment résoudre les problèmes liés aux e-mails HTML."
channel: email
---

# Résolution des problèmes 

## Le HTML s'affiche de manière incorrecte dans les e-mails de test

Si votre [e-mail de test]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) ne vous semble pas correct, nous vous recommandons de vérifier tout d'abord votre configuration HTML. Ensuite, vous pouvez vérifier les points suivants :
* [Conflits liés à l'extension](#check-conflicts)
* [Rendu de l'e-mail](#check-rendering)
* [Insertion CSS](#switch-css-inlining)

### Conflits liés à l'extension

Certaines extensions de navigateur peuvent causer des problèmes avec notre éditeur d'e-mails. [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) en est un exemple lorsqu'il est utilisé avec Google Chrome. Si vous utilisez l'une de ces extensions, vous devez soit : 
- Modifier les e-mails de Braze dans un navigateur qui n'a pas Grammarly comme extension de navigateur.
- Contactez votre gestionnaire de compte Braze et demandez à changer vos éditeurs d'e-mail en HTML uniquement ou en texte brut. 

L'affichage en texte brut supprime votre éditeur ```WYSIWYG``` (what you see is what you get). Vous devez donc vous assurer que tous les membres de l'équipe sont à l'aise avec le langage HTML avant de faire cette demande.

### Rendu de l'e-mail

Les e-mails s'affichent différemment selon les navigateurs et les clients de messagerie. Prenez donc note des navigateurs et des clients de messagerie avec lesquels vous rencontrez des problèmes.

- Prévisualisez vos e-mails à l'aide de [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) pour voir à quoi ressemblent vos e-mails dans différents navigateurs et clients de messagerie.
- Après avoir identifié les navigateurs ou les clients de messagerie qui posent problème, informez votre équipe de développeurs qu'ils devront modifier leur code HTML et faire des modifications pour s'adapter à ces navigateurs ou clients de messagerie.

### Insertion CSS

Il arrive que les aperçus dans la boîte de réception Vision ne correspondent toujours pas à ce qui est envoyé avec Braze. Cela peut être dû à la différence d'insertion CSS effectuée par Braze et par d'autres outils. Si vous pensez que c'est le cas, désactivez l'insertion CSS.

Vous avez encore besoin d'aide ? Ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).
