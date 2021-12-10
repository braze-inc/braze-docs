---
nav_title: Créer un modèle d'e-mail
article_title: Création d'un modèle d'e-mail
page_order: 2
description: "Les messages électroniques sont parfaits pour diffuser du contenu à l'utilisateur selon ses conditions. Cet article de référence couvre la façon de créer, personnaliser et gérer les modèles de courriels."
tool:
  - Modèles
channel:
  - Email
alias: "/dnd/email_template/"
---

# Comment créer un modèle d'e-mail

> Cet article traite de la façon de créer, personnaliser et gérer les modèles de courriels.

Les messages électroniques sont parfaits pour diffuser du contenu à l'utilisateur selon ses conditions. Ce sont également de merveilleux outils pour réengager les utilisateurs qui ont même désinstallé votre application. Le tableau de bord de Braze a un éditeur de modèle d'e-mail qui vous permet de créer des e-mails personnalisés et attractifs et de les enregistrer pour une utilisation ultérieure dans des campagnes. Vous pouvez également télécharger votre propre [modèle d'e-mail HTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/).

## Création de votre modèle

### Étape 1 : Accédez à l'éditeur de modèle d'e-mail

Dans la navigation de gauche, cliquez sur __Modèles & Médias__, dans la section __Engagement__. Ceci ouvrira la __Galerie de modèles d'e-mail__.

### Étape 2 : Créer ou choisir un modèle

Maintenant, vous pouvez créer un nouveau modèle ou modifier un modèle existant (simple ou [mobile responsive][8]) en utilisant soit l'expérience d'édition par glisser & déposer soit l'expérience HTML standard. Si vous souhaitez créer un nouveau modèle, vous pouvez choisir parmi les modèles préconçus de Braze, ou vous pouvez choisir de créer une nouvelle mise en page.

!\[Nouveau modèle\]\[2\]

{% alert note %}
Tous les modèles HTML personnalisés existants devront être recréés en utilisant l'éditeur Glisser & Déposer.
{% endalert %}

### Étape 3 : Personnaliser votre modèle

Vous pouvez écrire votre message dans l'éditeur de texte riche ou retourner optionnellement à notre éditeur HTML ou à l'éditeur Glisser & Déposer pour personnaliser votre contenu. Une fois sélectionné, vous serez guidé vers l'expérience de l'éditeur que vous avez choisi. Un badge 'Éditeur HTML' ou 'Glisser & Déposer Éditeur' va apparaître, indiquant que vous êtes sur le point d'utiliser cette expérience d'édition pour la création de modèles.

{% alert important %}
Lors de la rédaction de votre modèle de courriel, ne pas basculer entre les différents types d'éditeur (HTML/Block/Classic) car cela peut déplacer le HTML précédemment créé menant à des problèmes de rendu.
{% endalert %}

![Icône de l'éditeur de glisser-déposer]({% image_buster /assets/img/dnd_badge_icon.png %})

{% tabs %}
{% tab HTML Editor %}

Braze ajoutera un pied de page avec un lien de désinscription au bas de vos e-mails HTML par défaut. Vous pouvez personnaliser ce pied de page dans l'onglet **Paramètres de messagerie** de la page **Gérer les paramètres**. Pour plus d'informations, veuillez lire notre [documentation personnalisée de pied de page]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer).

Pour entrer une ligne d'objet, cliquez sur <i class="fas fa-pencil-alt"></i> **Modifier l'info d'envoi**.

![Saisir l'édition du modèle d'e-mail]({%image_buster/assets/img/email_templates/template3.png %})
<br>
<br>

Pour entrer dans l'éditeur de courrier électronique robuste, cliquez sur <i class="fas fa-pencil-alt"></i> **Modifier le corps du message**. Si vous le souhaitez, utilisez le menu déroulant dans l'onglet **Body** pour sélectionner l'éditeur d'email Classic, Block, HTML ou Texte Plain. Le panneau de droite affiche un aperçu en temps réel de l'e-mail en cours de création.

{% alert important %}
N'oubliez pas — en écrivant votre modèle de courriel, ne pas basculer entre les différents types d'éditeur (HTML/Block/Classic) car cela peut déplacer le HTML précédemment créé menant à des problèmes de rendu.
{% endalert %}

![Guide de l'éditeur de modèle d'e-mail]({%image_buster/assets/img/email_templates/template4.png %})

Notre éditeur prend en charge **la saisie automatique HTML** déclenchée par la touche `Tab`.  Cette fonctionnalité doit être utilisée sur les balises HTML nues. Par exemple, en utilisant `Tab` sur une balise `<head>` se traduira dans:
{% raw %}
```
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />

  <title>`substitute(Filename('', 'Titre de la page'), '^.', '\u&', '')`</title>

</head>
```
{% endraw %}
{% endtab %}
{% tab Drag & Drop Editor %}

L'expérience d'édition par glisser & déposer est divisée en trois sections : __Paramètres d'envoi__, __Contenu__et __Aperçu & Test__.

{% subtabs %}
{% subtab Send Settings %}

#### __Envoi des paramètres__

La section Paramètres d'envoi vous permet de configurer votre adresse de départ et de réponse ainsi que de définir la ligne de sujet ou le pré-en-tête.

{% alert note %}
Des fonctionnalités avancées apparaîtront dans la campagne ou dans le compositeur de pas de Canvas . Dans les fonctionnalités avancées, vous pouvez modifier vos paramètres CSS en ligne, définir une adresse email BCC, et entrer dans un en-tête ou des paires de valeur clé supplémentaire (si configuré).
{% endalert %}

{% endsubtab %}
{% subtab Content %}

#### __Contenus__

La section Contenu contient l'éditeur. Il y a trois composants clés dans cette section.

- __Contenu__: Cette section comprend une série de tuiles qui représentent les différents types de contenu que vous pouvez utiliser dans votre message. D'autres seront disponibles à l'avenir. Pour les utiliser, faites simplement glisser un à l'intérieur d'un segment de ligne existant; il s'ajustera automatiquement à la largeur de la colonne. Chaque bloc a ses propres paramètres, tels que le contrôle granulaire du remplissage. Le panneau de droite passe automatiquement à un panneau de propriétés pour l'élément de contenu sélectionné.<br><br> Pour plus d'informations, voir [Propriétés de bloc de l'éditeur]({{site.baseurl}}/dnd/editor_blocks/)<br><br>
- __Lignes__: Les lignes sont des unités de structure qui définissent la composition horizontale d'une section du message en utilisant des colonnes. L'utilisation de plus d'une colonne vous permet de mettre différents éléments de contenu côte à côte. Vous pouvez ajouter tous les éléments structurels dont vous avez besoin à votre message, quel que soit le modèle que vous avez sélectionné au démarrage.<br><br>
- __Paramètres__: Paramètres généraux du message. Ils sont hérités par les sections Lignes et Contenus. Par exemple, la famille de police définie dans les paramètres du message sera utilisée partout dans votre message, sauf lorsque vous utilisez un paramètre personnalisé.

Ceci est très utile pour construire un message cohérent très rapidement.
{% endsubtab %}
{% subtab Preview and Test %}

#### __Aperçu & Test__

La section Aperçu & Test vous permet de prévisualiser votre e-mail en fonction de différents utilisateurs.

- __Utilisateur Aléatoire__: Braze sélectionnera aléatoirement un utilisateur dans la base de données et prévisualisera l'email en fonction de ses attributs/informations sur l'événement. Note: Cet utilisateur peut ou non faire partie de vos critères de segmentation. La segmentation est ensuite sélectionnée, de sorte que Braze ne connaît pas votre public cible à ce stade.<br><br>
- __Sélectionner l'utilisateur__: Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou `external_id`. L'e-mail sera prévisualisé en fonction des attributs et des informations de l'événement de cet utilisateur<br><br>
- __Utilisateur personnalisé__: Vous pouvez personnaliser un utilisateur. Braze offrira des entrées pour tous les attributs et événements disponibles. Vous pouvez entrer toutes les informations que vous souhaitez voir dans l'e-mail de prévisualisation.
{% endsubtab %}
{% endsubtabs %}

Vision Boîte de réception est actuellement indisponible durant cette phase de test et sera disponible dans le futur.

{% alert tip %}
Pour en savoir plus sur les différents composants de l'expérience de glisser & déposer visitez nos articles de documentation de drag & Drop Editor [ici]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/).
{% endalert %}

{% endtab %}
{% endtabs %}

Braze va ajouter un pied de page avec un lien de désinscription au bas de votre e-mail par défaut. Vous pouvez personnaliser ce pied de page dans l'onglet **Paramètres de messagerie** de la page **Gérer les paramètres**. Pour plus d'informations, veuillez lire notre article sur [les pieds de page personnalisés][cf].

#### Étape 4 : Vérifier les erreurs de messagerie

Les erreurs de courriel sont présentées dans l'onglet **Composer** du flux de travail des messages. Les erreurs vous empêchent de progresser, tandis que les « Avertissements » indiquent des rappels pour vous aider à suivre les meilleures pratiques. Selon votre entreprise, vous pouvez choisir de les ignorer.

!\[Drag & Drop Compose Error\]\[1\]{: style="float:right;max-width:40%;margin-left:15px;"}

Voici une liste d'erreurs qui sont comptabilisées dans notre éditeur :

- Syntaxe de liquides incorrecte
- [Corps de courrier électronique de plus de 400kb; les corps sont fortement recommandés pour être inférieur à 102kb][7]
- Modèles sans lien de désinscription
- Emails avec un **corps ** vide** ou **sujet**.</li>
- E-mails sans lien de désinscription.</ul>

#### Étape 4b: Prévisualiser et tester votre message

Une fois que vous avez fini de composer votre modèle, vous pouvez le tester avant de l'envoyer.

À partir du bas de l'écran d'aperçu, cliquez sur **Aperçu et Tester**. Ici vous pouvez prévisualiser comment votre e-mail apparaîtra dans la boîte de réception d'un client. Avec **Aperçu en tant qu'utilisateur** sélectionné, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique, ou créer un utilisateur personnalisé. Cela vous permet de tester que vos appels de contenu connecté et de personnalisation fonctionnent comme ils le devraient.

Vous pouvez également basculer entre les vues bureau, mobile et texte en clair pour avoir une idée de la façon dont votre message apparaîtra dans différents contextes.

Quand vous êtes prêt pour une vérification finale, sélectionnez **Test Send** et envoyez un message de test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s'affiche correctement sur une variété de périphériques et de clients de messagerie.

!\[Nouveau aperçu de courriel\]\[15\]

Si vous voyez des problèmes avec votre modèle ou si vous souhaitez apporter des modifications, cliquez sur **Modifier l'e-mail** pour retourner à l'éditeur.

### Étape 5 : Enregistrez votre modèle

Assurez-vous de sauvegarder votre modèle en cliquant sur **Enregistrer le modèle** dans le coin inférieur droit de l'éditeur. Vous êtes maintenant prêt à utiliser ce modèle dans toutes les étapes de campagne ou de Canvas que vous choisissez.

{% alert note %}
Si vous faites des modifications à un modèle existant, ces modifications ne seront pas prises en compte dans les campagnes créées en utilisant les versions précédentes de ce modèle.
{% endalert %}

## Utiliser vos modèles dans les campagnes API

Pour utiliser votre email pour une campagne API, vous avez besoin d'un `email_template_id`, qui peuvent être trouvés au bas de n'importe quel modèle d'e-mail créé en Brésil.

!\[Enregistrer le modèle\]\[6\]

## Gestion des modèles d'e-mails

Vous pouvez [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) et [archiver]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) modèles d'e-mails ! En savoir plus sur la création et la gestion de modèles et de contenus créatifs dans [Modèles & Médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Foire aux questions

Pour obtenir des réponses aux questions les plus fréquemment posées sur les modèles de courriel, consultez notre page [FAQ][9] sur les modèles d'e-mails et de liens.
[2]: {% image_buster /assets/img/email_templates/template2.png %} [1]: {% image_buster /assets/img/dnd_compose_error.png %} [3]: {% image_buster /assets/img/email_templates/template3. ng %} [4]: {% image_buster /assets/img/email_templates/template4.png %} [6]: {% image_buster /assets/img/email_templates/template5. ng %} [15]: {% image_buster /assets/img_archive/newEmailTest.png %}

[cf]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[8]: {{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
