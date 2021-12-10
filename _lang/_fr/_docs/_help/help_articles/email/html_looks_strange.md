---
nav_title: Dépannage du rendu HTML dans les e-mails de test
article_title: Dépannage du rendu HTML dans les e-mails de test
page_order: 0
page_type: Solution
description: "Cet article d'aide vous guide dans la façon de résoudre les problèmes de rendu HTML dans les courriels de test."
channel: Email
---

# Dépannage du rendu HTML dans les e-mails de test

Si votre [e-mail de test][37] vous regarde, nous vous recommandons de le faire...

* [Vérifier le code HTML](#check-html-setup),
* [Vérifier les conflits](#check-conflicts),
* [Vérifier le rendu](#check-rendering), ou
* [Commuter CSS en ligne](#switch-css-in-lining).

### Vérifier la configuration HTML

Tout d'abord, confirmez avec vos développeurs que votre HTML est correctement configuré.

### Vérifier les conflits

Certaines extensions Chrome poseront des problèmes avec l'éditeur de courriel de Braze (un exemple est [Grammarly][38]). Si vous utilisez l'un de ces éléments, vous devriez soit :
- éditer les e-mails Braze dans un navigateur qui n'a pas Grammarly
- contactez votre responsable de compte Braze et demandez à retourner vos éditeurs de courriels en HTML seulement/texte brut.

NB vue en texte brut supprime votre éditeur `WYSIWYG` (ce que vous voyez est ce que vous obtenez), donc vous devez d'abord vous assurer que tous les membres de l'équipe sont à l'aise avec HTML avant de faire cette requête.

### Vérifier le rendu

Les courriels sont affichés différemment selon les navigateurs et les clients de messagerie. Enregistrez les navigateurs et les clients de messagerie avec lesquels vous rencontrez des problèmes.

- Prévisualisez vos e-mails dans un programme comme [Email sur Acid][39] ou [Litmus][40]. Celles-ci vous permettent de prévisualiser à quoi ressemblent les courriels dans différents navigateurs et clients de messagerie.

- Une fois que vous avez identifié quels navigateurs/clients de messagerie causent des problèmes, informez votre équipe de développeurs qu'ils devront modifier leur HTML et faire des modifications pour s'adapter à ces navigateurs/clients de messagerie.

### Basculer CSS en ligne

Il y a des moments où l'aperçu dans Email sur Acid ou Litmus ne correspond toujours pas à ce qui est envoyé via le tableau de bord Braze. Une des raisons possibles pour cela est que le CSS en ligne qui est effectué par Braze peut différer de la ligne CSS effectuée par d'autres outils. Si vous soupçonnez que c'est le cas, contactez votre responsable de compte Braze pour demander que le CSS en ligne soit désactivé.

Vous avez encore besoin d'aide ? Ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) ou laissez un commentaire ci-dessous.

_Dernière mise à jour le 12 décembre 2019_

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
