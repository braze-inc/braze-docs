---
nav_title: Rendu HTML dans les e-mails de test
article_title: Rendu HTML dans les e-mails de test
page_order: 0
page_type: Solution
description: "Cet article d'aide vous guide dans la façon de résoudre les problèmes de rendu HTML dans les courriels de test."
channel: Email
---

# Rendu HTML dans les e-mails de test

Si votre [e-mail de test][37] s'arrête, nous vous recommandons de vérifier d'abord votre configuration HTML. Ensuite, vous pouvez vérifier :

* [Conflit d'extension](#check-conflicts)
* [Email rendering](#check-rendering)
* [CSS inlining](#switch-css-inlining)

### Conflit d'extension

Certaines extensions de navigateur peuvent causer des problèmes avec l'éditeur de courriel de Brase. Un exemple est [Grammarly][38]) lorsqu'il est utilisé avec Google Chrome. Si vous utilisez une de ces extensions, vous devriez soit :
- Modifier les e-mails Braze dans un navigateur qui n'a pas Grammarly comme extension de navigateur
- Contactez votre responsable de compte Braze et demandez à changer vos éditeurs de courriels en HTML ou en texte brut.

La vue en texte brut supprime votre éditeur `WYSIWYG` (ce que vous voyez est ce que vous obtenez), donc vous devez d'abord confirmer que tous les membres de l'équipe sont à l'aise avec HTML avant de faire cette requête.

### Email rendering

Les courriels apparaissent différemment en fonction des navigateurs et des clients de messagerie, alors prenez note des navigateurs et des clients de messagerie avec lesquels vous rencontrez des problèmes.

- Prévisualisez vos e-mails à l'aide de la [Vision de boîte de réception]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) pour voir à quoi ressemblent vos e-mails dans différents navigateurs et clients de messagerie.
- Une fois que vous avez identifié quels navigateurs ou clients de messagerie causent des problèmes, informez votre équipe de développeurs qu'ils devront modifier leur HTML et faire des modifications pour s'adapter à ces navigateurs ou à ces clients de messagerie.

### CSS inlining

Il y a des moments où les aperçus de la Vision Boîte de réception ne correspondent toujours pas à ce qui est envoyé avec Braze. Cela peut être causé par la différence dans l'inlining CSS effectuée par Braze et par d'autres outils. Si vous soupçonnez que c'est le cas, contactez votre responsable de compte Braze pour demander que l'inlining CSS soit désactivée.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 21 décembre 2021_

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
