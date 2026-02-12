---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes
page_order: 9
description: "Cet article d'aide vous explique comment résoudre les problèmes liés aux e-mails HTML."
channel: email
---

# Résolution des problèmes 

## Le HTML s'affiche de manière incorrecte dans les e-mails de test

Si votre [e-mail de test]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) ne vous semble pas correct, nous vous recommandons de vérifier tout d'abord votre configuration HTML. Ensuite, vous pouvez vérifier ces problèmes :
* [Conflits d’extension](#check-conflicts)
* [Rendu des e-mails](#check-rendering)
* [Inclusion CSS](#switch-css-inlining)

### Conflits d’extension

Certaines extensions de navigateur peuvent causer des problèmes avec notre éditeur d'e-mails. [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) en est un exemple lorsqu'il est utilisé avec Google Chrome. Si vous utilisez l’une de ces extensions, vous devriez : 
- Modifier les e-mails de Braze dans un navigateur qui n’a pas l’extension Grammarly
- Contactez votre gestionnaire de compte Braze et demandez à changer vos éditeurs d’e-mails en HTML uniquement ou en texte brut. 

Dans la mesure où la vue en texte brut supprime votre éditeur WYSIWYG ```WYSIWYG```, vous devez commencer par confirmer que tous les membres de l’équipe connaissent le HTML avant de soumettre cette requête.

### Rendu des e-mails

Les e-mails sont rendus différemment selon les navigateurs et les clients de messagerie, alors prenez note des navigateurs et des clients de messagerie qui vous posent des problèmes.

- Prévisualisez vos e-mails à l'aide de [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) pour voir à quoi ressemblent vos e-mails dans différents navigateurs et clients de messagerie.
- Après avoir identifié les navigateurs ou les clients de messagerie qui posent problème, informez votre équipe de développeurs qu'ils devront modifier leur code HTML et faire des modifications pour s'adapter à ces navigateurs ou clients de messagerie.

### Inclusion CSS

Il arrive que les aperçus dans Inbox réception Vision ne correspondent toujours pas à ce qui est envoyé avec Braze. Cela peut être dû à la différence entre l’inclusion CSS effectuée par Braze et celle effectuée par d’autres outils. Si vous pensez que c'est le cas, désactivez l'insertion CSS.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).
