---
nav_title: Profils de couleurs et modèles CSS
article_title: Profils de couleurs et modèles CSS pour les messages in-app
page_order: 4
page_type: reference
description: "Le présent article fournit un aperçu des profils de couleurs des messages in-app et des modèles CSS."
channel:
  - in-app messages
---

# Profils de couleurs et modèles CSS {#reusable-color-profiles}

> Vous pouvez enregistrer sur le tableau de bord des modèles de messages in-app et intégrés au navigateur pour créer rapidement des campagnes et des messages avec votre style. 

Allez dans **Modèles** > **Modèles de messages in-app.**

À partir de cette page, vous pouvez soit modifier les modèles existants, soit cliquer sur **\+ Créer** et choisir **Profil de couleur** ou **Modèle CSS** pour créer de nouveaux modèles à utiliser dans vos messages in-app.

## Profil de couleur

Vous pouvez personnaliser le schéma couleur de votre modèle de message en saisissant un code couleur HEX ou en cliquant sur la case colorée et en sélectionnant une couleur avec le sélecteur de couleur.

Cliquez sur **Enregistrer le profil de couleur** lorsque vous avez terminé.

### Gestion des profils de couleur

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) et [archiver des]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modèles ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la rubrique [Modèles et médias.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)

## Modèle CSS {#in-app-message-templates}

Vous pouvez personnaliser un modèle CSS complet pour votre [message in-app Web modal](#web-modal-css).

Nommez et balisez votre modèle CSS, puis choisissez s’il s’agit du modèle par défaut. Vous pouvez écrire votre propre CSS dans l’espace fourni. Cet espace est déjà pré-rempli avec le CSS affiché dans l’aperçu de votre message, et vous pouvez l’ajuster légèrement pour répondre à vos besoins.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Comme vous le constatez, vous pouvez tout modifier, de la couleur d’arrière-plan à la taille et au poids de la police, et bien plus encore.

### Gestion des modèles CSS

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) et [archiver des]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modèles ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la rubrique [Modèles et médias.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)

## Modal avec CSS (Web uniquement) {#web-modal-css}

Si vous choisissez d’utiliser un message modal Web avecCSS, vous pouvez appliquer votre propre modèle ou écrire votre propre CSS dans l’espace fourni. Cet espace est déjà pré-rempli avec le CSS affiché dans l’aperçu de votre message, et vous pouvez l’ajuster légèrement pour répondre à vos besoins.

Si vous choisissez d'appliquer votre propre modèle, cliquez sur **Appliquer un modèle** et choisissez dans la galerie de modèles de messages in-app. Si vous n'avez pas d'options, vous pouvez télécharger un [modèle CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css/#in-app-message-templates) à l'aide du générateur de modèles CSS.


