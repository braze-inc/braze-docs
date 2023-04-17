---
nav_title: Profils de couleurs et modèles CSS
article_title: Profils de couleurs et modèles CSS pour les messages In-App
page_order: 4
page_type: reference
description: "Le présent article fournit un aperçu des profils de couleurs des messages In-App et des modèles CSS."
channel:
  - messages In-App
---

# Profils de couleurs et modèles CSS {#reusable-color-profiles}

> Vous pouvez enregistrer sur le tableau de bord des modèles de messages In-App et dans le navigateur pour créer rapidement des campagnes et des messages avec votre style. 

Aller à **Modèles et médias**, puis à l’onglet **Modèles de messages In-App**. Dans cette page, vous pouvez modifier les modèles existants, ou cliquer sur **+ Créer** et choisir **Profil de couleur** ou **Modèle CSS** pour créer de nouveaux modèles à utiliser dans vos messages In-App.

## Profil de couleur

Vous pouvez personnaliser le schéma couleur de votre modèle de message en saisissant un code couleur HEX ou en cliquant sur la case colorée et en sélectionnant une couleur avec le sélecteur de couleur.

Cliquez sur **Enregistrer le profil de couleur** lorsque vous avez terminé.

### Gestion des profils de couleur

Vous pouvez également [dupliquer][6] et [archiver][7] vos modèles ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la section [Templates & Media (Modèles et médias)][8].

## Modèle CSS {#in-app-message-templates}

Vous pouvez personnaliser un modèle CSS complet pour votre [message In-App Web modal]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/modal_with_css/).

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

Vous pouvez également [dupliquer][6] et [archiver][7] vos modèles ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la section [Templates & Media (Modèles et médias)][8].


[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/
[7]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/
[8]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
