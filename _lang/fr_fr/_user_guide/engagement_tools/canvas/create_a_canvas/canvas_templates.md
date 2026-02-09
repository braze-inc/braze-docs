---
nav_title: Créer un modèle de canvas
article_title: Créer un modèle de canvas
alias: "/canvas_templates/"
page_order: 0.5
description: "Cet article de référence explique comment créer un modèle pour Canvas."
page_type: reference
---

# Créer un modèle de canvas

> Cet article de référence explique comment créer et gérer des modèles pour Canvas. L'utilisation de modèles permet d'affiner vos messages en créant un cadre cohérent qui peut être facilement personnalisé pour répondre à vos objectifs spécifiques sur l'ensemble de vos canvas.

{% alert tip %}
Enregistrez votre temps et rationalisez votre création de canvas en utilisant les [modèles de Braze Canvas](#available-braze-templates)! Parcourez notre bibliothèque de modèles préconstruits pour trouver celui qui correspond à votre cas d'utilisation et personnalisez-le pour répondre à vos besoins spécifiques.
{% endalert %}

## Méthode 1  : Créer à partir d'un canvas existant

### Étape 1 : Sélectionnez votre Canvas existant

Dans le tableau de bord de Braze, allez dans **Messagerie** > **Canvas** et sélectionnez un Canvas existant que vous souhaitez utiliser comme modèle.

### Étape 2 : Créez votre modèle

Dans l'éditeur de canvas, sélectionnez **Modifier le canvas** ou **Modifier le brouillon**, selon que votre canvas est actif ou en brouillon. Développez le menu déroulant **Enregistrer comme brouillon** dans le pied de page et sélectionnez **Enregistrer comme modèle**.

![]({% image_buster /assets/img/save_canvas_as_template.png %})

### Étape 3 : Enregistrer votre modèle

Ensuite, attribuez un nom à votre modèle et ajoutez les éventuelles étiquettes pertinentes. Sélectionnez ensuite **Enregistrer**. Votre modèle est maintenant prêt à être utilisé pour créer un canvas, ce qui vous donne une longueur d'avance avec vos paramètres et étapes de base déjà en place.

## Méthode 2 : Créer via l'éditeur de modèles Canvas

### Étape 1 : Accédez à l'éditeur de modèles Canvas

Dans le tableau de bord de Braze, sélectionnez **Modèles** > **Modèles de canvas**.

{% alert note %}
Si vous utilisez l'ancienne navigation, vous trouverez cette page sous **Engagement** > **Modèles & Media** > Canvas Templates.
{% endalert %}

### Étape 2 : Créer un nouveau modèle

Sélectionnez **Créer un modèle** et commencez à configurer les détails de votre Canvas. Vous pouvez commencer par donner un nom à votre modèle Canvas.

![Exemple de canvas nommé « Modèle Canvas pour ventes annuelles » avec la description « Utilisation pour la promotion annuelle du printemps ».]({% image_buster /assets/img/canvas_template_example.png %})

### Étape 3 : Personnaliser votre modèle

Ensuite, personnalisez votre modèle en [configurant votre Canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas) Vous pouvez décider quand les utilisateurs doivent entrer dans le Canvas, déterminer quels utilisateurs peuvent entrer dans ce Canvas, ajuster vos paramètres d'envoi et créer votre parcours utilisateur pour le modèle.

### Étape 4 : Enregistrer votre modèle

Lorsque vous avez fini de personnaliser votre modèle, cliquez sur le bouton **Enregistrer le modèle**. Sur la page du **modèle Canvas**, vous pouvez afficher les détails de votre modèle Canvas en sélectionnant <i class="fas fa-list"></i> **Détails du modèle.** 

## Utilisation des modèles Canvas

Il existe deux façons d'utiliser votre modèle lors de la composition d'un canvas :

- **De l'envoi de messages**: Allez dans **Messagerie** > **Canvas.** Sélectionnez le bouton **Créer un canvas** et **utilisez un modèle de canvas**.
- **À partir de modèles** : Allez dans **Modèles** > **Modèles de canvas** et trouvez le modèle de votre choix. Ensuite, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i> suivi de **Appliquer le modèle.** Cela vous amènera à un nouveau Canvas avec le modèle appliqué dans le compositeur de Canvas.

### Modèles de Braze disponibles

Pour obtenir une liste des modèles Canvas disponibles, reportez-vous à la section [Modèles Canvas]({{site.baseurl}}/canvas_templates/templates/). Pour plus de détails sur l'utilisation des modèles eCommerce Canvas, reportez-vous à la section [Comment utiliser les événements recommandés par eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

## Gestion des modèles de Canvas

Les modèles de canvas peuvent être dupliqués et archivés, comme un vrai canvas. Pour modifier un modèle de canvas, sélectionnez le modèle, puis choisissez **<i class="fas fa-pencil-alt"></i>Modifier**.

Au niveau de l'espace de travail, vous pouvez mettre à jour les autorisations des utilisateurs pour permettre ou limiter l'accès à la création, la modification, la visualisation ou l'archivage des modèles Canvas.

### Permissions pour les équipes et les espaces de travail

Pour n'autoriser que certains utilisateurs à accéder à des modèles Canvas spécifiques et à les utiliser, [ajoutez une équipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) aux modèles, puis attribuez des autorisations d'accès aux campagnes, canevas, cartes de contenu, blocs de contenu, drapeaux de fonctionnalité, segments, bibliothèque multimédia et centre de préférences au niveau de l'équipe.

Si vous attribuez l'une des autorisations suivantes au niveau de l'équipe, mais pas au niveau de l'espace de travail, vous ne pouvez effectuer que les opérations suivantes attribuées à votre équipe :

- Créer et modifier des modèles de canvas
- Voir les modèles de Canvas
- Archiver les modèles de Canvas

Si des autorisations sont accordées à la fois au niveau de l'espace de travail et au niveau des Teams, les autorisations au niveau de l'espace de travail seront prioritaires.

## Foire aux questions

### Puis-je enregistrer une étape incomplète dans un modèle Canvas ?

Oui, vous pouvez enregistrer les étapes incomplètes en tant que modèle de canvas. Cependant, lorsque le modèle est utilisé, une erreur apparaît sur le bouton **Enregistrer le modèle** qui indique ce qui est nécessaire pour lancer le Canvas.

### Puis-je enregistrer les paramètres de mon générateur de canvas en tant que modèle, ou puis-je seulement enregistrer des étapes ? 

Oui, vous pouvez enregistrer les paramètres du générateur de canvas dans un modèle de canvas. Par exemple, si vous prévoyez d'utiliser souvent une combinaison de segments et de filtres, vous pouvez enregistrer ces paramètres d'**audience cible** dans le cadre de votre modèle Canvas.

