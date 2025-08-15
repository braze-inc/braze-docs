---
nav_title: Création d’un modèle d’e-mail
article_title: Création d’un modèle d’e-mail
page_order: 0
description: "Le présent article de référence explique comment créer, personnaliser et gérer des modèles d’e-mail."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Création d’un modèle d’e-mail

> Le tableau de bord de Braze est doté d’un éditeur de modèles d’e-mails qui vous permet de créer des e-mails personnalisés et attrayants et de les enregistrer pour une utilisation ultérieure dans les campagnes. Vous pouvez également télécharger votre propre [modèle d'e-mail HTML.]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/)

## Étape 1 : Accéder à l’éditeur de modèles d’e-mail

Allez dans **Modèles** > **Modèles d'e-mail**.

## Étape 2 : Sélectionnez votre expérience en matière de modification 

Choisissez entre l'**éditeur par glisser-déposer** et l'**éditeur HTML** pour votre expérience d'édition. 

Ensuite, vous pouvez choisir parmi les modèles prédéfinis de Braze, créer un nouveau modèle ou modifier un modèle existant (simple ou [mobile responsive]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates)).

![Un modèle d'e-mail pour les soldes de printemps d'une entreprise, avec des options permettant de sélectionner l'éditeur glisser-déposer ou l'éditeur HTML, ou de choisir parmi les modèles de Braze.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Tous les modèles HTML personnalisés existants devront être recréés à l'aide de l'éditeur par glisser-déposer.
{% endalert %}

## Étape 3 : Personnaliser votre modèle

Après avoir sélectionné votre expérience d’éditeur, ceci est l'occasion de faire preuve de créativité en personnalisant votre modèle d'e-mail. Vous pouvez utiliser HTML pour créer et émuler votre image de marque dans l'éditeur HTML, ou inclure une variété de [détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) dans l'éditeur glisser-déposer.

### Inclure un lien de désabonnement

Lors de la création de votre modèle d'e-mail, si vous n'incluez pas de lien de désabonnement, Braze vous invitera à l'ajouter dans votre e-mail, étant donné que la loi l'exige pour tous les e-mails marketing. Vous pouvez ajouter ce lien de désabonnement au bas de vos e-mails à l'aide de l'étiquette Liquid {% raw %}``${email_footer}``{% endraw %}, ou en [personnalisant le pied de page]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer) dans votre modèle.

## Étape 4 : Vérifier les erreurs de courrier électronique

Les erreurs d'e-mail sont présentées dans l'onglet **Composer** du flux de travail du message. Les erreurs vous empêchent de progresser. Les « Avertissements » indiquent des rappels pour vous aider à suivre les meilleures pratiques. Selon votre entreprise, vous pouvez choisir de les ignorer.

![Liste d'erreurs et d'avertissements d'un exemple d'e-mail.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Voici une liste d’erreurs prises en compte dans notre éditeur :

- Syntaxe Liquid incorrecte
- [Les corps des e-mails sont supérieurs à 400 kb ; il est fortement recommandé que les corps soient inférieurs à 102 kb.]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)
- Modèles sans lien de désabonnement
- E-mails dont le **corps** ou l'**objet** est vide
- E-mails sans lien de désabonnement

## Étape 5 : Prévisualiser et tester votre message

Après avoir composer votre modèle, vous pouvez le tester avant de l’envoyer.

En bas de l'écran d'aperçu, sélectionnez **Prévisualiser et tester**. Ici, vous pouvez visualiser la façon dont votre e-mail apparaîtra dans la boîte de réception d’un client. Si l'option **Prévisualiser en tant qu'utilisateur** est sélectionnée, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de tester que vos appels de contenu connecté et de personnalisation fonctionnent correctement. 

Ensuite, vous pouvez **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré.

Vous pouvez également basculer entre l’affichage mobile de bureau et de texte brut pour comprendre comment votre message apparaîtra dans différents contextes.

{% alert tip %}
Vous aimeriez savoir à quoi ressemblent vos e-mails pour vos utilisateurs en mode sombre ? Sélectionnez le **Aperçu en mode sombre** situé dans la section **Aperçu et test** (éditeur par glisser-déposer uniquement).
{% endalert %}

Lorsque vous êtes prêt pour une dernière vérification, sélectionnez **Tester l'envoi** et envoyez un message test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s'affiche correctement sur une variété d'appareils et de clients de messagerie.

![Exemple d'e-mail à envoyer à des fins de test.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si vous rencontrez des problèmes avec votre modèle ou si vous souhaitez y apporter des modifications, sélectionnez **Modifier l'e-mail** pour revenir à l'éditeur.

## Étape 6 : Enregistrer votre modèle

Veillez à enregistrer votre modèle en sélectionnant **Enregistrer le modèle.** Vous êtes maintenant prêt à utiliser ce modèle dans toutes les campagnes ou Canvas de votre choix. Pour accéder à votre modèle, sélectionnez l’expérience d’édition avec laquelle vous l’avez créé puis sélectionnez-le dans la liste de modèles disponibles.

{% alert note %}
Si vous apportez des modifications à un modèle existant, ces modifications ne seront pas reflétées dans les campagnes créées qui utilisent les versions précédentes de ce modèle.
{% endalert %}

### Gérer vos modèles

Au fur et à mesure que vous créez des modèles d'e-mail, vous pouvez les [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) et les [archiver]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates). Pour en savoir plus sur la création et la gestion de votre bibliothèque de modèles et de contenus créatifs, consultez la rubrique [Modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Utilisation de vos modèles dans des campagnes API

Pour utiliser votre e-mail dans une campagne API, vous avez besoin d’un `email_template_id`, qui se trouve au bas des modèles d’e-mails créés dans Braze.

![Identifiant API situé au bas d'un modèle d'e-mail.]({% image_buster /assets/img/email_templates/template5.png %})

### Commentaires sur les modèles d'e-mail

Vous pouvez collaborer et commenter les modèles d'e-mail dans l'éditeur par glisser-déposer. 

1. Sélectionnez le bloc de contenu ou la ligne dans le corps de l'e-mail que vous souhaitez commenter.
2. Sélectionnez l'icône de commentaire <i class="fas fa-comment"></i>.
3. Saisissez votre commentaire dans la barre latérale, puis sélectionnez **Soumettre**.
4. Après avoir saisi vos commentaires, sélectionnez **Terminé**.
5. Sélectionnez **Enregistrer le modèle** pour enregistrer vos commentaires.

Une fois votre modèle enregistré, les utilisateurs peuvent voir des icônes sur les commentaires non traités. Sélectionnez **Résoudre** pour résoudre ces commentaires.

![Un commentaire de modèle d'e-mail qui se lit comme suit : "Ça m'a l'air bien".]({% image_buster /assets/img/email_templates/template_comment.png %})

Pour obtenir des réponses aux questions fréquemment posées sur les modèles d'e-mail, consultez notre [FAQ sur les modèles.]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/)

