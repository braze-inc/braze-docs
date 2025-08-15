---
nav_title: Rendu HTML dans les e-mails de test
article_title: Rendu HTML dans les e-mails de test
page_order: 2

page_type: solution
description: "Cet article d’aide vous explique comment résoudre les problèmes liés au rendu HTML dans les e-mails de test."
channel: email
---

# Résolution des problèmes de rendu HTML dans les e-mails de test

Si votre [e-mail de test]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) ne vous semble pas correct, nous vous recommandons de vérifier tout d'abord votre configuration HTML. Ensuite, vous pouvez vérifier ces problèmes :
* [Conflits d’extension](#check-conflicts)
* [Rendu des e-mails](#check-rendering)
* [Inclusion CSS](#switch-css-inlining)

### Conflits d’extension

Certaines extensions de navigateur peuvent causer des problèmes avec notre éditeur d'e-mails. Un exemple est [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)) lorsqu'il est utilisé avec Google Chrome. Si vous utilisez l’une de ces extensions, vous devriez : 
- Modifier les e-mails de Braze dans un navigateur qui n’a pas l’extension Grammarly
- Contactez votre gestionnaire de compte Braze et demandez à changer vos éditeurs d’e-mails en HTML uniquement ou en texte brut. 

Dans la mesure où la vue en texte brut supprime votre éditeur WYSIWYG ```WYSIWYG```, vous devez commencer par confirmer que tous les membres de l’équipe connaissent le HTML avant de soumettre cette requête.

### Rendu des e-mails

Les e-mails sont rendus différemment selon les navigateurs et les clients de messagerie, alors prenez note des navigateurs et des clients de messagerie qui vous posent des problèmes.

- Prévisualisez vos e-mails à l'aide de [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) pour voir à quoi ressemblent vos e-mails dans différents navigateurs et clients de messagerie.
- Après avoir identifié les navigateurs ou les clients de messagerie qui posent problème, informez votre équipe de développeurs qu'ils devront modifier leur code HTML et faire des modifications pour s'adapter à ces navigateurs ou clients de messagerie.

### Inclusion CSS

Il peut arriver que les prévisualisations Inbox Vision ne correspondent pas à ce qui est envoyé par Braze. Cela peut être dû à la différence entre l’inclusion CSS effectuée par Braze et celle effectuée par d’autres outils. Si vous pensez que c’est le cas, contactez votre gestionnaire de compte Braze pour demander la désactivation de l’inclusion CSS.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 21 décembre 2021_

