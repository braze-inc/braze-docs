---
nav_title: Aperçu
article_title: Créer un e-mail en glisser-déposer
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "Le présent article explique comment configurer et utiliser correctement l’éditeur Drag & Drop pour les e-mails."
tool: 
  - Campagnes
  - Canvas
---

# Créer un e-mail en glisser-déposer

> Avec l’éditeur Drag & Drop, vous pouvez créer des e-mails entièrement personnalisés dans les campagnes ou les Canvas à l’aide de l’expérience de modification en glisser-déposer.

{% multi_lang_include video.html id="4dTrkxe8DLo" align="right" %}

Vous ne savez pas si votre e-mail doit être envoyé à l’aide d’une campagne ou d’un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes. 

Une fois que vous avez choisi où créer votre message, examinons les étapes pour créer un e-mail en glisser-déposer ! 

## Étape 1 : Sélectionnez votre modèle

Après avoir sélectionné l’éditeur Drag & Drop comme expérience de modification, vous pouvez choisir de :
- Commencer par un modèle vide
- Utiliser un modèle de courriel en glisser-déposer Braze 
- Sélectionner un modèle enregistré de courriel en glisser-déposer

![La section Modèles de base d’e-mail en glisser-déposer qui montre la possibilité de sélectionner un modèle vierge ou un modèle de Braze. Il existe également une section ci-dessous pour les modèles enregistrés d’e-mail en glisser-déposer.][1]

Si vous souhaitez utiliser vos modèles HTML personnalisés existants ou les modèles créés par un tiers, ils doivent être recréés dans l’éditeur Drag & Drop. 

{% alert tip %}
Vous pouvez également accéder à tous les modèles de la page **Templates & Media (Modèles et médias)** dans la section **Engagement**.
{% endalert %}

Après avoir sélectionné votre modèle, vous verrez un aperçu de votre e-mail où vous pouvez modifier les informations d’envoi et le corps de l’e-mail, et afficher les erreurs ou avertissements à résoudre avant l’envoi. Cliquez sur **Edit Email Body (Modifier le corps du courriel)** pour commencer à concevoir votre structure de courrier électronique dans l’éditeur Drag & Drop ! 

![][8]

## Étape 2 : Créez votre e-mail 

L’expérience de modification en glisser-déposer est divisée en trois sections : **Paramètres d’envoi**, **Contenu**, et **Aperçu et test**.

Avant de créer votre e-mail, il est important de comprendre les principaux composants pour vous aider à guider votre expérience de création de courrier électronique.

### Glisser-déposer les composants d’e-mail {#content}

L’éditeur Drag & Drop utilise deux composants principaux pour faciliter et accélérer la composition des e-mails : **Content (Contenu)** et **Rows (Lignes)**. 

![][10]{: style="float:right;max-width:30%;margin-left:10px;"}
![][9]{: style="float:right;max-width:30%;margin-left:10px;"}

**Content (Contenu)** comprend une série de mosaïques qui représentent différents types de contenu que vous pouvez utiliser dans votre message. Elles sont organisées en trois catégories : de base, multimédia et avancé. Les blocs de contenu de base constituent le socle de votre e-mail, tels que les blocs de titre et de paragraphe, les boutons et les espaceurs. Les blocs de contenu multimédia vous permettent d’inclure des images, des vidéos, des informations sur les réseaux sociaux et des icônes. Avec les blocs de contenu avancés, vous pouvez insérer des blocs HTML ou ajouter un menu à votre e-mail.

Il suffit d’en faire glisser un à l’intérieur d’un segment de ligne existant, et il s’ajustera automatiquement à la largeur de la colonne. Chaque bloc dans **Content (Contenu)** possède ses propres paramètres, comme un contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de propriétés pour l’élément de contenu sélectionné. Pour plus d’informations, voir [Propriétés du bloc éditeur]({{site.baseurl}}/dnd/editor_blocks/). 

Les **lignes** sont des unités structurelles qui définissent la composition horizontale d’une section du message en utilisant des colonnes. L’utilisation de plusieurs colonnes permet de placer différents éléments de contenu côte à côte. Vous pouvez ajouter tous les éléments structurels dont vous avez besoin, quel que soit le modèle que vous avez sélectionné lorsque vous avez commencé.

Le panneau **Settings (Paramètres)** dans la section **Design and Build (Conception et création)** comprend les paramètres généraux du courrier électronique. Ces paramètres sont hérités des sections **Content (Contenu)** et **Rows (Lignes)** sections. Par exemple, l’ensemble **Default Font (Polices par défaut)** de cette section est utilisé partout dans votre message, sauf si vous utilisez un paramètre personnalisé. 

![][11]{: style="width:300px;height:auto;"} 

### Utiliser le contenu de l’e-mail

Lorsque vous chargez pour la première fois dans l’éditeur Drag & Drop, vous voyez l’onglet **Design and Build (Conception et création)** dans la section **Content (Contenu)** de l’éditeur Drag & Drop. C’est là que vous pouvez tirer parti des [détails créatifs](#creative-details) dans la conception de la disposition de votre courrier électronique.

1. Sélectionnez le panneau **Rows (Lignes)**. Glissez-déposez les configurations de lignes dans l’éditeur principal. Cela permettra de définir la mise en page du contenu de votre e-mail. Notez que les nouvelles configurations doivent être déplacées au début ou à la fin d’une section existante.
- Lorsque vous sélectionnez une configuration de ligne, les paramètres **Row Properties (Propriétés de ligne)** s’affichent pour une personnalisation supplémentaire des couleurs d’arrière-plan de ligne, des images et des tailles de colonnes.
2. Sélectionnez le panneau **Content (Contenu)**. Glissez-déposez les mosaïques de contenu souhaitées sur les composants de ligne. 
- Vous pouvez affiner davantage la mosaïque en la sélectionnant et en ajustant les champs dans **Content Properties (Propriétés de contenu)** et **Block Options (Options de bloc)**. Cela inclut l’espacement des lettres, la marge intérieure, la hauteur de ligne, etc.

Lorsque vous créez votre e-mail, vous pouvez basculer entre un affichage de bureau et un affichage mobile pour visualiser la façon dont votre communication par e-mail recherchera vos groupes d’utilisateurs. Cela garantira que votre contenu est réactif et que vous pouvez effectuer tous les ajustements nécessaires au fur et à mesure. 

{% alert tip %}
Besoin d’aide pour créer un texte d’exception ? Essayez d’utiliser l’[assistant de rédaction IA]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/). Saisissez un nom ou une description du produit et l’IA générera un texte marketing semblant d’origine humaine pour une utilisation dans votre envoi de messages.

![Bouton de rédaction, situé dans le panneau Contenu à côté des paramètres de style dans l’éditeur Drag & Drop.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Détails créatifs {#creative-details}

{% alert tip %}
Vous pouvez créer un thème personnalisé pour votre éditeur Drag & Drop en utilisant les [paramètres de style globaux]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/).
{% endalert %}

#### Images de largeur automatique

Les images ajoutées à votre e-mail seront automatiquement définies sur **Largeur automatique**. Pour ajuster ce réglage, désactivez la fonction **Auto width (Largeur automatique)** et modifiez le pourcentage de largeur selon les besoins. 

![Option de largeur automatique dans l’onglet Contenu de l’éditeur Drag & Drop.][2]

#### Superposition de couleurs

L’éditeur Drag & Drop vous permet de modifier la couleur de l’arrière-plan de l’e-mail, de la zone de contenu et des différents composants de contenu. La commande couleur de l’avant à l’arrière est la couleur du composant de contenu, la couleur de l’arrière-plan de la zone de contenu et la couleur de l’arrière-plan. 

![Exemple de superposition de couleurs dans l’éditeur Drag & Drop.][3]

#### Marge intérieure de contenu

![Options de bloc de l’éditeur Drag & Drop.][4]{: style="float:right;max-width:25%;margin-left:15px;"}

Pour ajuster la marge intérieure, faites défiler jusqu’à **Block Options (Options de bloc)** et affichez **More Options (Plus d’options)**. Cela vous permettra d’ajuster votre marge intérieure pour que votre e-mail soit parfait !
<br>

#### Arrière-plan du contenu

Vous pouvez ajouter une image d’arrière-plan pour votre configuration de ligne, vous permettant d’incorporer plus d’esthétique et de contenu dans votre campagne e-mail.

#### Ajout de Liquid 

![Options d’ajout de personnalisation de l’éditeur Drag & Drop.][5]{: style="float:right;max-width:25%;margin-left:15px;"}

Le Liquid de base est pris en charge dans notre éditeur Drag & Drop. Pour ajouter du Liquid dans votre e-mail, sélectionnez **Personnalisation** sous **Design / Build (Conception/Création)**. Ici, vous pouvez ajouter différents types de personnalisation, tels que des attributs de base (par défaut), des attributs d’appareil, des attributs personnalisés, et bien plus encore ! Ensuite, prenez votre extrait de code Liquid généré et ajoutez-le à votre e-mail.

##### Images dynamiques

Vous pouvez choisir d’incorporer des images dynamiques dans vos envois de messages par e-mail en incluant du Liquid dans votre attribut de source d’image. Par exemple, au lieu d’une image statique, vous pouvez insérer {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} comme URL d’image pour inclure le prénom d’un utilisateur dans l’image. Ceci vous aide à personnaliser vos e-mails pour chaque utilisateur.

Une fois que vous avez fini de concevoir et de créer votre courrier électronique, allez sur **Sending Settings (Paramètres d’envoi)** pour ajouter des informations d’envoi.

#### Ajout d’attributs HTML à des liens

![][6]{: style="float:right;max-width:35%;margin-left:15px;"}

Grâce aux attributs, vous pouvez facilement ajouter des informations supplémentaires aux balises HTML dans les e-mails. Ces attributs peuvent être appliqués aux liens, à la fois dans les blocs de texte et les boutons, ainsi qu’aux images. Ceci peut être particulièrement utile dans le cadre de la personnalisation, de la segmentation et de la mise en page de messages. 

Un cas d’utilisation courant consiste à insérer un attribut dans votre balise d’ancrage pour désactiver le suivi des clics lors de l’envoi via Braze :

* **SendGrid :** `clicktracking = "off"`
* **SparkPost :** `data-msys-clicktrack = "0"`

Un autre cas d’utilisation courant consiste à marquer des liens spécifiques en tant que liens universels. Les liens universels sont ceux qui redirigent vers votre application :

* **SendGrid :** `universal = "true"`
* **SparkPost :** `data-msys-sublink = "open-in-app"`, un [sous-chemin personnalisé](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) doit être configuré.

## Étape 3 : Ajouter des informations d’envoi

La section **Sending Settings (Paramètres d’envoi)** vous permet de configurer votre **nom affiché et adresse d’expédition** et votre **adresse de réponse**, ainsi que de définir la ligne objet ou l’accroche. Vous pouvez également voir un aperçu de votre message.

{% alert note %}
La fonctionnalité avancée apparaîtra dans le composeur de campagne ou de Canvas. Dans la fonctionnalité avancée, vous pouvez modifier votre paramètre CSS inséré, définir une adresse e-mail CCI et saisir un en-tête ou des paires clé-valeur supplémentaire (si configuré).
{% endalert %}

## Étape 4 : Tester votre e-mail

La section **Preview & Test (Aperçu et test)** vous permet d’afficher un aperçu de vos e-mails sur différents clients et appareils de messagerie grâce à **Preview & Test Send (Aperçu et test de l’envoi)** et **Inbox Vision**.

Étant donné que vous pouvez afficher trois versions différentes du même e-mail dans l’éditeur proprement dit, dans Inbox Vision et en testant effectivement l’e-mail, il est important d’aligner les détails entre toutes vos plateformes. 

### Aperçu et envoi de test

Vous pouvez également afficher les aperçus de votre e-mail avec ces types d’utilisateurs :

- **Utilisateur aléatoire :** Braze sélectionnera de manière aléatoire un utilisateur de la base de données et prévisualisera l’e-mail en fonction de ses attributs ou informations sur l’événement.
- **Utilisateur sélectionné :** Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou `external_id`. L’aperçu de l’e-mail s’affichera en fonction des attributs et des informations d’événement de cet utilisateur
- **Utilisateur personnalisé :** Vous pouvez personnaliser un utilisateur. Braze offre des entrées pour tous les attributs et événements disponibles. Vous pouvez saisir toutes les informations que vous souhaitez voir dans l’aperçu d’e-mail.

{% alert note %}
L’utilisateur aléatoire peut ou non faire partie de vos critères de segmentation. La segmentation est sélectionnée par la suite, Braze n’est donc pas au courant de votre audience cible à ce stade.
{% endalert %}

Vous pouvez aussi utiliser ici la bascule **Dark Mode Preview (Aperçu du mode sombre)** pour prévisualiser votre e-mail en mode sombre et rectifier votre e-mail si nécessaire.

### Inbox Vision

[Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/) vous permet de consulter vos campagnes par e-mail du point de vue de différents clients par e-mail et appareils mobiles. Pour tester votre courrier électronique à l’aide d’Inbox Vision, sélectionnez **Inbox Vision** dans la section **Preview & Test (Aperçu et test)** et cliquez sur **Run Inbox Vision (Exécuter Inbox Vision)**. 

{% alert tip %}
Les images d’arrière-plan dans les envois de messages par e-mail peuvent parfois entraîner l’apparition de lignes blanches ou de déconnexions entre les images. Il est donc important de tester et de vérifier les plus petits détails de votre message par e-mail.
{% endalert %}

Après avoir utilisé l’éditeur Drag & Drop pour concevoir et créer votre courrier électronique, continuez à [créer][12] le reste de votre campagne ou Canvas.

### Moteur HTML mis à jour

Le moteur sous-jacent qui produit l’élément HTML depuis l’éditeur Drag & Drop a été optimisé et mis à jour, ce qui améliore la compression et le rendu du fichier HTML.

#### Compression des fichiers

La taille moyenne de l’empreinte de nos données HTML exportées a été réduite, ce qui permet un chargement et un rendu plus rapides, une réduction du clipping sur les appareils mobiles et une consommation réduite de bande passante.

#### Rendu HTML

Le rendu HTML s’est amélioré sur la base des mises à jour suivantes qui minimisent le nombre de commentaires conditionnels et les requêtes de médias CSS. En conséquence, les fichiers HTML sont plus petits et mieux codés. 

- Migration à partir d’une base de code formatée `<div>` element-based design to a standard `<table>`
- Des [blocs éditeur][7] ont été recodés pour plus de concision
- Le code HTML final est compressé pour supprimer les espaces blancs entre les balises
- Les lignes de séparation transparentes sont automatiquement converties en marge intérieure de contenu

[1]: {% image_buster /assets/img/dnd/dnd_template1.png %}
[2]: {% image_buster /assets/img/dnd/dnd1.png %}
[3]: {% image_buster /assets/img/dnd/dnd2.png %}
[4]: {% image_buster /assets/img/dnd/dnd3.png %}
[5]: {% image_buster /assets/img/dnd/dnd4.png %}
[6]: {% image_buster /assets/img/dnd_custom_attributes.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/
[8]: {% image_buster /assets/img/dnd/dnd_emailvariant.png %}
[9]: {% image_buster /assets/img/dnd/dnd_content.png %}
[10]: {% image_buster /assets/img/dnd/dnd_rows.png %}
[11]: {% image_buster /assets/img/dnd/dnd_contentsettings.png %}
[12]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/
