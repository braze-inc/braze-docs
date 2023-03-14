---
nav_title: Rendu HTML dans les e-mails de test
article_title: Rendu HTML dans les e-mails de test
page_order: 1

page_type: solution
description: "Cet article d’aide vous explique comment résoudre les problèmes liés au rendu HTML dans les e-mails de test."
channel: email
---

# Rendu HTML dans les e-mails de test

Si votre [e-mail test][37] n’est pas terrible, nous vous recommandons de vérifier d’abord votre configuration HTML. Ensuite, vous pouvez vérifier ces problèmes :
* [Conflits d’extension](#check-conflicts)
* [Rendu des e-mails](#check-rendering)
* [Inlining CSS](#switch-css-inlining)

### Conflits d’extension

Certaines extensions de navigateur peuvent causer des problèmes avec l’éditeur d’e-mail de Braze. Par exemple, [Grammarly][38] quand elle est utilisée avec Google Chrome. Si vous utilisez l’une de ces extensions, vous devriez : 
- Modifier les e-mails de Braze dans un navigateur qui n’a pas l’extension Grammarly
- Contactez votre gestionnaire de compte Braze et demandez à changer vos éditeurs d’e-mails en HTML uniquement ou en texte brut. 

La vue en texte brut supprime votre éditeur ```WYSIWYG``` (what you see is what you get), vous devez d’abord confirmer que tous les membres de l’équipe connaissent le HTML avant de faire cette demande.

### Rendu des e-mails

Les e-mails sont rendus différemment selon les navigateurs et les clients de messagerie, alors prenez note des navigateurs et des clients de messagerie qui vous posent des problèmes.

- Prévisualisez vos e-mails en utilisant [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) pour voir l’aspect de vos e-mails dans différents navigateurs et clients de messagerie.
- Une fois que vous avez identifié quels navigateurs ou clients e-mail causent des problèmes, informez votre équipe de développeurs qu’ils devront modifier leur HTML et faire des modifications pour s’adapter à ces navigateurs ou clients de messagerie.

### Inlining CSS

Il peut arriver que les prévisualisations Inbox Vision ne correspondent pas à ce qui est envoyé par Braze. Cela peut être causé par la différence entre l’inlining CSS effectué par Braze et celui d’autres outils. Si vous pensez que c’est le cas, contactez votre gestionnaire de compte Braze pour demander la désactivation de l’inlining CSS.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 21 décembre 2021_

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
