---
nav_title: "Création d'un modèle de canvas"
article_title: "Création d'un modèle de canvas"
alias: "/canvas_templates/"
page_order: 0.5
description: "Cet article de référence explique comment créer un modèle pour Canvas."
page_type: reference
---

# Création d'un modèle de canvas

> Cet article de référence explique comment créer et gérer des modèles pour Canvas. L'utilisation de modèles permet d'affiner vos messages en créant un cadre cohérent qui peut être facilement personnalisé pour répondre à vos objectifs spécifiques sur l'ensemble de vos canevas.

{% alert tip %}
Enregistrez votre temps et rationalisez votre création de canvas en utilisant les [modèles de Braze Canvas](#available-braze-templates)! Parcourez notre bibliothèque de modèles préconstruits pour trouver celui qui correspond à votre cas d'utilisation et personnalisez-le pour répondre à vos besoins spécifiques.
{% endalert %}

## Méthode 1 : Créer à partir d'un canvas existant

### Étape 1 : Sélectionnez votre Canvas existant

Dans le tableau de bord de Braze, allez dans **Messagerie** > **Canvas** et sélectionnez un Canvas existant que vous souhaitez utiliser comme modèle.

### Étape 2 : Créez votre modèle

Dans l'éditeur de canvas, sélectionnez **Modifier le canvas** ou **Modifier le brouillon**, selon que votre canvas est actif ou en brouillon. Développez le menu déroulant **Enregistrer comme brouillon** dans le pied de page et sélectionnez **Enregistrer comme modèle**.

\![]({% image_buster /assets/img/save_canvas_as_template.png %})

### Étape 3 : Enregistrez votre modèle

Ensuite, donnez un nom à votre modèle et ajoutez toutes les étiquettes pertinentes. Sélectionnez ensuite **Enregistrer**. Votre modèle est maintenant prêt à être utilisé pour créer un canvas, ce qui vous donne une longueur d'avance avec vos paramètres et étapes de base déjà en place.

## Méthode 2 : Créer via l'éditeur de modèles Canvas

### Étape 1 : Accédez à l'éditeur de modèles Canvas

Dans le tableau de bord de Braze, allez dans **Modèles** > **Modèles de canevas**.

{% alert note %}
Si vous utilisez l'ancienne navigation, vous trouverez cette page sous **Engagement** > **Modèles & Media** > Canvas Templates.
{% endalert %}

### Étape 2 : Créer un nouveau modèle

Sélectionnez **Créer un modèle** et commencez à configurer les détails de votre Canvas. Vous pouvez commencer par donner un nom à votre modèle Canvas.

\![Un exemple de canvas nommé "Annual sale Canvas template" avec la description "Use for annual spring promotion".]({% image_buster /assets/img/canvas_template_example.png %})

### Étape 3 : Personnalisez votre modèle

Ensuite, personnalisez votre modèle en [configurant votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas). Vous pouvez décider quand les utilisateurs doivent entrer dans le Canvas, déterminer quels utilisateurs peuvent entrer dans ce Canvas, ajuster vos paramètres d'envoi et créer votre parcours utilisateur pour le modèle.

### Étape 4 : Enregistrez votre modèle

Lorsque vous avez fini de personnaliser votre modèle, cliquez sur le bouton **Enregistrer le modèle**. Sur la page du **modèle Canvas**, vous pouvez afficher les détails de votre modèle Canvas en sélectionnant <i class="fas fa-list"></i> **Détails du modèle.** 

## Utilisation des modèles Canvas

Il y a deux façons d'utiliser votre modèle lors de la composition d'un canvas :

- **De l'envoi de messages**: Allez dans **Messagerie** > **Canvas**. Sélectionnez le bouton **Créer un canevas** et **utilisez un modèle de canevas**.
- **À partir de modèles**: Allez dans **Modèles** > **Modèles de canevas** et trouvez le modèle de votre choix. Ensuite, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i> suivi de **Appliquer le modèle.** Cela vous amènera à un nouveau Canvas avec le modèle appliqué dans le compositeur de Canvas.

### Modèles de Braze disponibles

Braze met à votre disposition une sélection de modèles de Canvas que vous pouvez référencer et utiliser comme meilleures pratiques pour les cas d'utilisation courants. Bien que ces modèles ne puissent pas être modifiés, vous pouvez les visualiser dans **Modèles** > **Modèles** **de Braze** ou les utiliser dans vos toiles.

!Les modèles de Braze dans la section Modèles de canevas avec six modèles disponibles.]({% image_buster /assets/img/braze_canvas_templates.png %})

Sélectionnez l'un des modèles suivants pour vous y référer ou l'utiliser comme canevas.

{% tabs %}
{% tab Abandoned Intent %}

Dialoguez avec les utilisateurs en temps réel pour les encourager à terminer leurs achats.

Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Ajouter une audience spécifique. Actuellement, les parcours d'audience sont déclenchés sur la base de "Tout achat", mais vous pouvez les adapter aux produits spécifiques que vous souhaitez cibler.
- Ce modèle suppose que vous avez un parcours post-achat distinct, de sorte que la réalisation d'un achat amènera les utilisateurs à quitter le Canvas.
- Complétez les détails dans l'étape de synchronisation de l'audience.

{% endtab %}
{% tab Back In Stock %}

Encouragez les achats en informant vos utilisateurs lorsqu'un article est de nouveau en stock grâce à des messages personnalisés. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Dans **Entry Schedule**, sélectionnez un catalogue à utiliser. Cela vous permet d'accéder à des données, telles que les produits, les remises et les promotions, afin de mieux cibler vos utilisateurs.
- Dans **Audience cible**, ajoutez un segment pour cibler les utilisateurs qui ont manifesté de l'intérêt pour un certain article.
- Dans les étapes du message tout au long du canvas, mettez à jour le liquide pour faire référence à votre catalogue.

{% endtab %}
{% tab Feature Adoption %}

Envoyez des messages personnalisés au moment opportun pour souligner les avantages et les conseils d'utilisation. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Exclure les utilisateurs qui ont déjà utilisé le produit. Par exemple, dans **Target Audience**, ajoutez un filtre dans 
-  Pour utiliser l'étape des chemins d'expérience, définissez un événement de conversion. Cet événement devrait être le signal de l'adoption de la fonctionnalité.
- Configurez l'étape du parcours d'action dans le modèle avec des événements personnalisés pour "Activated Feature" (fonctionnalité activée) et "Taken Tour" (visite guidée).
- Configurez les attributs personnalisés dans l'étape du message intitulée "Enquête sur le retour d'information" pour capturer le sentiment du retour d'information.

{% endtab %}
{% tab Lapsed User %}

Faites revenir les utilisateurs sur votre application en leur proposant des incitations basées sur leurs engagements passés. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Dans **Basics**, sélectionnez une app spécifique pour laquelle vous souhaitez suivre les conversions.
- Dans l'éditeur de canvas, ajoutez des applications spécifiques pour les étapes des parcours d'action.
- Configurez l'étape de synchronisation de l'audience avec les partenaires et les audiences correspondant à votre cas d'utilisation.

{% endtab %}
{% tab Onboarding %}

Créez des parcours d'onboarding qui favorisent une forte adoption initiale et encouragent des relations durables avec vos utilisateurs. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Dans l'étape des parcours d'audience nommée " Fractionnement de l'audience ", pensez à personnaliser les actions clés pour les utilisateurs engagés. Dans le modèle, le filtre de segmentation est "A cliqué sur l'e-mail de bienvenue".

{% endtab %}
{% tab Post-Purchase Feedback %}

Orchestrez des expériences personnalisées qui vous permettent de répondre aux commentaires et de créer une relation avec vos utilisateurs. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Dans la première étape de l'éditeur de canvas :
    - Spécifiez les attributs personnalisés dans le message in-app pour indiquer le sentiment du retour d'information en fonction de l'option d'enquête sélectionnée. 
    - Spécifiez les attributs des liens pour chaque appel à l'action afin de déterminer l'option sélectionnée. Ces attributs sont référencés dans le parcours d'audience suivant.
- Personnalisez le parcours d'audience avec les attributs de la première étape de ce modèle.
- Configurez l'étape de synchronisation de l'audience nommée " reciblage publicitaire ".

{% endtab %}
{% endtabs %}

{% alert tip %}
Pour obtenir un guide étape par étape sur la création d'un canvas d'exemple à l'aide de ces modèles de Braze, reportez-vous à la section [Utilisation des modèles de Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates).
{% endalert %}

## Gestion des modèles de canvas

Les modèles de canvas peuvent être dupliqués et archivés, comme un vrai canvas. Pour modifier un modèle de canvas, sélectionnez le modèle puis **<i class="fas fa-pencil-alt"></i>Modifier**.

Au niveau de l'espace de travail, vous pouvez mettre à jour les autorisations des utilisateurs pour permettre ou limiter l'accès à la création, la modification, la visualisation ou l'archivage des modèles Canvas.

### Permissions pour les équipes et les espaces de travail

Pour n'autoriser que certains utilisateurs à accéder à des modèles Canvas spécifiques et à les utiliser, [ajoutez une équipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) aux modèles, puis attribuez des autorisations d'accès aux campagnes, canevas, cartes de contenu, blocs de contenu, drapeaux de fonctionnalité, segments, bibliothèque multimédia et centre de préférences au niveau de l'équipe.

Si vous attribuez l'une des autorisations suivantes au niveau de l'équipe, mais pas au niveau de l'espace de travail, vous ne pouvez effectuer que les opérations suivantes attribuées à votre équipe :

- Créer et modifier des modèles de canvas
- Voir les modèles de Canvas
- Archiver les modèles de Canvas

Si des autorisations sont accordées à la fois au niveau de l'espace de travail et au niveau des Teams, les autorisations au niveau de l'espace de travail seront prioritaires.

## Questions fréquemment posées

### Puis-je enregistrer une étape incomplète dans un modèle Canvas ?

Oui, vous pouvez enregistrer les étapes incomplètes en tant que modèle de canvas. Cependant, lorsque le modèle est utilisé, une erreur apparaît sur le bouton **Enregistrer le modèle** qui indique ce qui est nécessaire pour lancer le Canvas.

### Puis-je enregistrer les paramètres de mon générateur de canevas en tant que modèle, ou puis-je seulement enregistrer des étapes ? 

Oui, vous pouvez enregistrer les paramètres du générateur de canevas dans un modèle de canevas. Par exemple, si vous prévoyez d'utiliser souvent une combinaison de segments et de filtres, vous pouvez enregistrer ces paramètres d'**audience cible** dans le cadre de votre modèle Canvas.

