---
nav_title: Vision de la boîte de réception
article_title: Vision de la boîte de réception
page_order: 6
description: "Inbox Vision permet aux marketeurs de visualiser leurs courriels du point de vue de divers clients de messagerie et appareils mobiles. Cet article de référence traite de la façon de mettre en place et d'utiliser Inbox Vision."
tool:
  - Tableau de bord
channel:
  - Email
---

# Vision de la boîte de réception

Inbox Vision permet aux marketeurs de visualiser leurs courriels du point de vue de divers clients de messagerie et appareils mobiles. Accédez à la Vision de boîte de réception à partir de l'éditeur d'e-mail en cliquant sur **Aperçu et test**.  Il vous permet également de spam test depuis l'onglet **Spam Test**.

{% alert important %}
Vision de la boîte de réception pour [l'expérience d'édition par glisser & déposer]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#editing-experience/) est actuellement en accès anticipé. Veuillez contacter votre responsable de compte Braze si vous êtes intéressé à participer à un accès anticipé.
{% endalert %}


## Testez votre adresse e-mail

Pour tester votre message dans Réception Vision, cliquez sur **Aperçu et Tester** dans le compositeur de courriel. Braze envoie ensuite une version HTML de votre e-mail à divers clients de messagerie utilisés à travers le monde, qui peut prendre entre deux et dix minutes à compléter.

Braze affichera ensuite des captures d'écran d'un échantillon, du HTML affiché sur les ordinateurs de bureau, les appareils mobiles et les tablettes. Les périphériques dans lesquels les captures d'écran sont affichées sont scrollable, pour permettre une meilleure vue. Si vous rencontrez des captures d'écran non claires pour certains clients de messagerie, cliquez sur **Retraiter la capture d'écran** pour créer une autre capture d'écran.

Si vous effectuez un test de Vision Boîte de réception, vous recevrez également des résultats d'analyse de code et de test de spam.

!\[Vue d'ensemble de la boîte de réception\]\[1\]

Une fois que vous apportez des modifications à un modèle, vous devrez cliquer sur **Re-Run Test** pour voir l'effet des modifications sur les aperçus.

{% alert important %}
En général, votre courriel ne fonctionnera pas avec la Vision Boîte de réception si votre contenu de courrier électronique repose sur des informations de modèle telles que les informations de profil de l'utilisateur. Ceci est dû au fait que les modèles Braze dans un utilisateur vide lorsque nous envoyons des e-mails en utilisant cette fonctionnalité.
{% endalert %}

## Analyse de code

L'analyse de code est un moyen pour Braze de mettre en évidence les problèmes qui peuvent exister avec votre HTML, indiquant le nombre d'occurrences de chaque fiche et fournissant un aperçu des éléments HTML qui ne sont pas pris en charge. Cette information se trouve sur la page Aperçu de la Vision de la boîte de réception en sélectionnant l'icône de la liste dans le coin supérieur gauche.

!\[Analyse du code de la Vision de la Boîte de récep\]\[2\]

!\[Analyse du Code de la Vision de la Boîte de réception 2\]\[3\]

{% alert note %}
Parfois, l'analyse de code s'affiche plus rapidement que l'aperçu d'un client de messagerie particulier. C'est parce que nous attendons que l'email arrive dans la boîte de réception avant de prendre la capture d'écran.
{% endalert %}

## Tests de spam

[Le test de spam][4] tente de prédire si votre e-mail va atterrir dans des dossiers de spam ou dans les boîtes de réception de vos clients.  Les tests de spam se déroulent sur les principaux filtres de spam tels que IronPort, SpamAssassin, Barracuda, ainsi que sur les principaux filtres ISP tels que Gmail.com et Outlook.com.

## Précision du test

Tous nos tests sont exécutés par des clients de messagerie réels. Nous nous efforçons de nous assurer que tous les renders sont aussi précis que possible.  Si vous constatez un problème avec un client de messagerie, veuillez ouvrir un [ticket de support]({{site.baseurl}}/braze_support/).
[1]: {% image_buster /assets/img_archive/inboxvision1.png %} [2]: {% image_buster /assets/img_archive/inboxvision2.png %} [3]: {% image_buster /assets/img_archive/inboxvision3.png %}

[4]: {{site.baseurl}}/email_spam_testing/
