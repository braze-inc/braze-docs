---
nav_title: Modèles de canvas
article_title: Modèles de canvas
alias: "/canvas_templates/templates/"
page_order: 0
description: "Cet article de référence explique comment créer les modèles Canvas disponibles."
page_type: reference
---

# Modèles de canvas

> Braze met à votre disposition une sélection de modèles de Canvas que vous pouvez référencer et utiliser comme meilleures pratiques pour les cas d'utilisation courants. Bien que ces modèles ne puissent pas être modifiés, vous pouvez les visualiser dans **Modèles** > **Modèles Braze** ou les utiliser dans vos canvas.

![Braze propose treize modèles dans la section "Canvas templates".]({% image_buster /assets/img/braze_canvas_templates.png %})

Sélectionnez l'un des modèles suivants pour vous y référer ou l'utiliser comme canevas.

## Modèles de canevas standard

{% tabs %}
{% tab Abandoned Intent %}

### Intention abandonnée

Dialoguez avec les utilisateurs en temps réel pour les encourager à terminer leurs achats.

Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Ajouter une audience spécifique. Actuellement, les parcours d'audience sont déclenchés sur la base de "Tout achat", mais vous pouvez les adapter aux produits spécifiques que vous souhaitez cibler.
- Ce modèle suppose que vous avez un parcours post-achat distinct, de sorte que la réalisation d'un achat amènera les utilisateurs à quitter le Canvas.
- Complétez les détails dans l'étape de synchronisation de l'audience.

{% endtab %}
{% tab Back In Stock %}

### De retour en stock

Encouragez les achats en informant vos utilisateurs lorsqu'un article est de nouveau en stock grâce à des messages personnalisés. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Dans **Entry Schedule**, sélectionnez un catalogue à utiliser. Cela vous permet d'accéder à des données, telles que les produits, les remises et les promotions, afin de mieux cibler vos utilisateurs.
- Dans **Audience cible**, ajoutez un segment pour cibler les utilisateurs qui ont manifesté de l'intérêt pour un certain article.
- Dans les étapes du message tout au long du canvas, mettez à jour le code  Liquid pour faire référence à votre catalogue.

{% endtab %}
{% tab Feature Adoption %}

### Adoption de fonctionnalités

Envoyez des messages personnalisés au moment opportun pour souligner les avantages et les conseils d'utilisation. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Exclure les utilisateurs qui ont déjà adopté la fonctionnalité. Par exemple, dans **Target Audience**, ajoutez un filtre pour un événement personnalisé tel que "Activated Feature" qui s'est déjà produit.
- Pour utiliser l'étape des chemins d'expérience, définissez un événement de conversion. Cet événement devrait être le signal de l'adoption de la fonctionnalité.
- Configurez l'étape du parcours d'action dans le modèle avec des événements personnalisés pour "Activated Feature" (fonctionnalité activée) et "Taken Tour" (visite guidée).
- Configurez les attributs personnalisés dans l'étape du message intitulée "Enquête sur le retour d'information" pour capturer le sentiment du retour d'information.

{% endtab %}
{% tab Lapsed User %}

### Utilisateur déchu

Faites revenir les utilisateurs sur votre application en leur proposant des incitations basées sur leurs engagements passés. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Dans **Basics**, sélectionnez une app spécifique pour laquelle vous souhaitez suivre les conversions.
- Dans l'éditeur de canvas, ajoutez des applications spécifiques pour les étapes des parcours d'action.
- Configurez l'étape de synchronisation de l'audience avec les partenaires et les audiences correspondant à votre cas d'utilisation.

{% endtab %}
{% tab Onboarding %}

### Onboarding

Créez des parcours d'onboarding qui favorisent une forte adoption initiale et encouragent des relations durables avec vos utilisateurs. Tenez compte des éléments suivants lorsque vous utilisez ce modèle :

- Dans l'étape des parcours d'audience nommée " Fractionnement de l'audience ", pensez à personnaliser les actions clés pour les utilisateurs engagés. Dans le modèle, le filtre de segmentation est "A cliqué sur l'e-mail de bienvenue".

{% endtab %}
{% tab Post-Purchase Feedback %}

### Retour d'information après l'achat

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

## Modèles de canevas pour le commerce électronique

Les modèles eCommerce Canvas sont conçus spécifiquement pour les marketeurs du commerce électronique, ce qui facilite la mise en œuvre des stratégies essentielles.

{% multi_lang_include canvas/ecommerce_templates.md %}