---
nav_title: Inscription par e-mail avec réduction
article_title: Inscription par e-mail avec réduction
alias: "/email_discount/"
page_order: 3
description: "Cette page de référence explique comment utiliser l'éditeur par glisser-déposer des messages in-app pour créer un formulaire d'inscription par e-mail qui offre une remise aux nouveaux abonnés."
---

# Inscription par e-mail avec réduction

> Utilisez l'éditeur par glisser-déposer de messages in-app pour créer un formulaire d'inscription à un e-mail qui offre une réduction aux nouveaux abonnés.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Création d'un formulaire d'inscription par e-mail avec remise

### Étape 1 : Choisissez votre modèle

Lorsque vous créez un message in-app par glisser-déposer, sélectionnez **Inscription par e-mail avec remise de bienvenue** pour votre modèle, puis sélectionnez **Créer un message.** Ce modèle est pris en charge à la fois pour les applications mobiles et les navigateurs web.

L'éditeur de messages in-app avec le modèle d'un formulaire d'inscription par e-mail avec remise.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_discount.png %})

### Étape 2 : Définissez les styles de vos messages

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Étape 3 : Personnalisez votre composant d'inscription à l'e-mail

Pour commencer à créer votre formulaire d'inscription par e-mail, sélectionnez l'élément de capture d'e-mail dans l'éditeur. Par défaut, les adresses e-mail collectées auront le groupe d'abonnement global **Abonné**. Pour abonner des utilisateurs à des groupes d'abonnement spécifiques, reportez-vous à la section [Mise à jour des états d'abonnement à l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)

Vous pouvez personnaliser le texte substitutif et le texte de l'étiquette de l'élément de capture d'e-mail.

L'éditeur de messages in-app avec un menu latéral pour personnaliser l'élément de capture d'e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field.png %})

#### Validation de l'e-mail

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Étape 4 : Ajouter une clause de non-responsabilité (facultatif)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Étape 5 : Donnez du style à votre message

Personnalisez l'aspect et la convivialité de votre formulaire d'inscription et de votre remise à l'aide des [composants de message in-app par]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) glisser-déposer.

## Analyse des résultats

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Meilleures pratiques

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}



