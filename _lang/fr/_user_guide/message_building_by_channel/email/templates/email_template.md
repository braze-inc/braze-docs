---
nav_title: Création d’un modèle d’e-mail
article_title: Création d’un modèle d’e-mail
page_order: 2
description: "Le présent article de référence explique comment créer, personnaliser et gérer des modèles d’e-mail."
tool:
  - Templates
channel:
  - e-mail
alias: "/dnd/email_template/"
search_rank: 1
---

# Création d’un modèle d’e-mail

> Le présent article explique comment créer, personnaliser et gérer des modèles d’e-mail.

Le tableau de bord de Braze est doté d’un éditeur de modèles d’e-mails qui vous permet de créer des e-mails personnalisés et attrayants et de les enregistrer pour une utilisation ultérieure dans les campagnes. Vous pouvez également télécharger votre propre [modèle d’e-mail HTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/).

## Création de votre modèle

### Étape 1 : Accéder à l’éditeur de modèles d’e-mail

Dans la navigation à gauche, cliquez sur **Templates & Media (Modèles et médias)** de la section **Engagement**. Cela ouvrira le **galerie de modèles d’e-mail**.

### Étape 2 : Créer ou choisir un modèle

Vous pouvez maintenant créer un nouveau modèle ou modifier un modèle existant (brut ou [adapté aux besoins des utilisateurs][8]) à l’aide de l’expérience de modification en glisser-déposer ou de l’expérience HTML standard. Si vous souhaitez créer un nouveau modèle, vous pouvez choisir parmi les modèles préconçus de Braze ou créer une nouvelle mise en page.

![Nouveau modèle][2]

{% alert note %}
Tous les modèles HTML personnalisés existants devront être recréés à l’aide de l’éditeur Drag & Drop.
{% endalert %}

### Étape 3 : Personnaliser votre modèle

Vous pouvez écrire votre message dans l’éditeur de texte enrichi ou revenir éventuellement à notre éditeur HTML ou à l’éditeur Drag & Drop pour personnaliser votre contenu. Une fois sélectionné, vous serez guidé vers l’expérience de l’éditeur que vous aurez choisie. Un badge d’**éditeur HTML** ou d’**éditeur Drag & Drop** apparaîtra, indiquant que vous êtes sur le point d’utiliser cette expérience de modification pour la création de modèle.

{% alert important %}
Lors de la rédaction de votre modèle de courrier électronique, ne basculez pas entre différents types d’éditeur (HTML/Block/Classic) car cela peut déplacer l’élément HTML précédemment créé, entraînant alors des problèmes. 
{% endalert %}

![Badge de l’éditeur Drag & Drop dans la section Corps de l’e-mail]({% image_buster /assets/img/dnd_badge_icon.png %})

{% tabs %}
{% tab HTML Editor %}

Braze ajoutera par défaut un pied de page avec un lien de désabonnement au bas de vos e-mails HTML. Vous pouvez personnaliser ce pied de page dans l’onglet **Email Settings (Paramètres d’e-mail)** de la page **Manage Settings (Gérer les paramètres)**. Pour plus d’informations, lisez notre [documentation sur les pieds de page personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer).

Pour saisir une ligne d’objet, cliquez sur <i class="fas fa-pencil-alt"></i> **Edit Sending Info (Modifier les informations d’envoi)**. 

![Panneau Détails du modèle d’e-mail dans l’éditeur HTML.]({% image_buster/assets/img/email_templates/template3.png %})
<br>
<br>

Pour entrer dans l’éditeur d’e-mail robuste, cliquez sur <i class="fas fa-pencil-alt"></i> **Edit Email Body (Modifier le corps de l’e-mail)**. Si vous le souhaitez, utilisez la liste déroulante dans l’onglet **Body (Corps)** pour sélectionner l’éditeur d’e-mail Classic, Block, HTML ou Plaintext. Le panneau adjacent affiche un aperçu en temps réel de l’e-mail créé.

{% alert important %}
Rappelez-vous : lors de la rédaction de votre modèle de courrier électronique, ne basculez pas entre différents types d’éditeur (HTML/Block/Classic) car cela peut déplacer l’élément HTML précédemment créé, entraînant alors des problèmes. 
{% endalert %}

![Menu déroulant dans l’onglet Corps qui affiche les options des types d’éditeurs.]({% image_buster/assets/img/email_templates/template4.png %})

Notre éditeur prend en charge l’**HTML automatique** déclenché par la clé `Tab`.  Cette fonctionnalité doit être utilisée sur des balises HTML avec l’attribut « naked ». Par exemple, utiliser `Tab` sur une balise `<head>` se traduira par :
{% raw %}
```
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />

  <title>`substitute(Filename('', 'Page Title'), '^.', '\u&', '')`</title>

</head>
```
{% endraw %}
{% endtab %}
{% tab Drag & Drop Editor %}

L’expérience de modification en glisser-déposer est divisée en trois sections : **Paramètres d’envoi**, **Contenu**, et **Aperçu et test**.

{% subtabs %}
{% subtab Send Settings %}

#### Paramètres d’envoi

La section **Sending Settings (Paramètres d’envoi)** vous permet de configurer votre adresse d’expédition et votre adresse de réponse, ainsi que de définir la ligne objet ou l’accroche. 

{% alert note %}
La fonctionnalité avancée apparaîtra dans le composeur de campagne ou de Canvas. Dans la fonctionnalité avancée, vous pouvez modifier votre paramètre CSS inséré, définir une adresse e-mail CCI et saisir un en-tête ou des paires clé-valeur supplémentaire (si configuré).
{% endalert %}

{% endsubtab %}
{% subtab Content %}

#### Contenu

La section **Content (Contenu)** comprend l’éditeur. Cette section comporte trois composants principaux.

- **Contenu** : Cette section comprend une série de mosaïques qui représentent les différents types de contenu que vous pouvez utiliser dans votre message. D’autres informations seront disponibles à l’avenir. Pour les utiliser, il suffit d’en faire glisser une à l’intérieur d’un segment de ligne existant, et elle s’ajustera automatiquement à la largeur de la colonne. Chaque bloc possède ses propres paramètres, comme un contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de propriétés pour l’élément de contenu sélectionné.<br><br> Pour plus d’informations, voir [Editor Block Properties (Propriétés du bloc éditeur)]({{site.baseurl}}/dnd/editor_blocks/)<br><br>
- **Lignes :** Les lignes sont des unités structurelles qui définissent la composition horizontale d’une section du message en utilisant des colonnes. L’utilisation de plusieurs colonnes permet de placer différents éléments de contenu côte à côte. Vous pouvez ajouter tous les éléments structurels dont vous avez besoin, quel que soit le modèle que vous avez sélectionné lorsque vous avez commencé.<br><br>
- **Paramètres :** Paramètres généraux du message. Ils sont héritées des sections Rows (Lignes) et Content (Contenu). Par exemple, la famille de polices définie dans les paramètres de message sera utilisée partout dans votre message, sauf si vous utilisez un paramètre personnalisé.

Ceci est très utile pour créer un message cohérent très rapidement.
{% endsubtab %}
{% subtab Preview and Test %}

#### Aperçu et test

La section **Preview & Test (Aperçu et test)** vous permet d’afficher un aperçu de votre e-mail en fonction des différents utilisateurs.

- **Utilisateur aléatoire :** Braze sélectionnera de manière aléatoire un utilisateur de la base de données et prévisualisera l’e-mail en fonction de ses attributs/informations sur l’événement.
Remarque : Cet utilisateur peut ou non faire partie de vos critères de segmentation. La segmentation est sélectionnée par la suite, Braze n’est donc pas au courant de votre audience cible à ce stade.<br><br>
- **Utilisateur sélectionné :** Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou `external_id`. L’aperçu de l’e-mail s’affichera en fonction des attributs et des informations d’événement de cet utilisateur<br><br>
- **Utilisateur personnalisé :** Vous pouvez personnaliser un utilisateur. Braze offre des entrées pour tous les attributs et événements disponibles. Vous pouvez saisir toutes les informations que vous souhaitez voir dans l’aperçu d’e-mail.
{% endsubtab %}
{% endsubtabs %}

Inbox Vision n’est actuellement pas disponible pendant cette phase de test et le sera à l’avenir.

{% alert tip %}
Pour en savoir plus sur les différents composants de l’expérience de modification en glisser-déposer, consultez nos articles de documentation sur l’éditeur Drag & Drop [ici]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/). 
{% endalert %}

{% endtab %}
{% endtabs %}

Braze ajoutera par défaut un pied de page avec un lien de désabonnement au bas de votre e-mail. Vous pouvez [personnaliser ce pied de page]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer) dans l’onglet **Email Settings (Paramètres d’e-mail)** de la page **Manage Settings (Gérer les paramètres)**.

#### Étape 4a : Vérifier les erreurs de courrier électronique

Les erreurs de courrier électronique sont présentées dans l’onglet **Compose (Composer)** du flux de travail du message. Les erreurs vous empêchent de progresser. Les « Avertissements » indiquent des rappels pour vous aider à suivre les meilleures pratiques. Selon votre entreprise, vous pouvez choisir de les ignorer.

![Liste d’erreurs et d’avertissements dans un exemple d’e-mail.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Voici une liste d’erreurs prises en compte dans notre éditeur :

- Syntaxe Liquid incorrecte
- [Corps d’e-mail supérieurs à 400 Ko ; il est fortement recommandé que les corps ne dépassent pas 102 Ko][7]
- Modèles sans lien de désabonnement
- E-mails avec **Corps** ou **Sujet** vide
- E-mails sans lien de désabonnement

#### Étape 4b : Prévisualiser et tester votre message

Après avoir composer votre modèle, vous pouvez le tester avant de l’envoyer.

En bas de l’écran d’aperçu, cliquez sur **Preview and Test (Aperçu et test)**. Ici, vous pouvez visualiser la façon dont votre e-mail apparaîtra dans la boîte de réception d’un client. En sélectionnant **Aperçu en tant qu’utilisateur**, vous pouvez prévisualiser votre e-mail en tant qu’utilisateur aléatoire, sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de tester que vos appels de contenu connecté et de personnalisation fonctionnent correctement.

Vous pouvez également basculer entre l’affichage mobile de bureau et de texte brut pour comprendre comment votre message apparaîtra dans différents contextes.

Lorsque vous êtes prêt pour une vérification finale, sélectionnez **Test Send (Envoi de test)** et envoyez un message de test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s’affiche correctement sur une variété d’appareils et de clients par e-mail.

![Exemple d’aperçu d’e-mail à envoyer pour test.][6]

Si vous rencontrez des problèmes avec votre modèle ou si vous souhaitez apporter des modifications, cliquez sur **Edit Email (Modifier l’e-mail)** pour revenir à l’éditeur.

### Étape 5 : Enregistrer votre modèle

Assurez-vous d’enregistrer votre modèle en cliquant sur **Save Template (Enregistrer le modèle)**. Vous êtes maintenant prêt à utiliser ce modèle dans toutes les campagnes ou Canvas de votre choix. Pour accéder à votre modèle, sélectionnez l’expérience d’édition avec laquelle vous l’avez construit puis sélectionnez-le dans la liste de modèles disponibles.

{% alert note %}
Si vous apportez des modifications à un modèle existant, ces modifications ne seront pas reflétées dans les campagnes créées qui utilisent les versions précédentes de ce modèle.
{% endalert %}

## Utilisation de vos modèles dans des campagnes API

Pour utiliser votre e-mail dans une campagne API, vous avez besoin d’un `email_template_id`, qui se trouve au bas des modèles d’e-mails créés dans Braze.

![Exemple de modèle d’identificateur d’API.][5]

## Gestion des modèles d’e-mail

Vous pouvez [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) et [archiver]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) vos modèles d’e-mail ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la section [Templates & Media (Modèles et médias)]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## FAQ

Pour obtenir des réponses aux questions fréquemment posées sur les modèles d’e-mail, consultez notre page [Templates FAQs (FAQ sur les modèles)][9].


[1]: {% image_buster /assets/img/dnd_compose_error.png %}
[2]: {% image_buster /assets/img/email_templates/template2.png %}
[3]: {% image_buster /assets/img/email_templates/template3.png %}
[4]: {% image_buster /assets/img/email_templates/template4.png %}
[5]: {% image_buster /assets/img/email_templates/template5.png %}
[6]: {% image_buster /assets/img_archive/newEmailTest.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[8]: {{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/