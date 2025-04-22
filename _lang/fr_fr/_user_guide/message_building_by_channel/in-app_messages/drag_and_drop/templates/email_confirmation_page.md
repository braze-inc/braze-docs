---
nav_title: Inscription par e-mail avec confirmation
article_title: Inscription par e-mail avec page de confirmation
alias: "/email_confirmation_page/"
page_order: 6
description: "Cette page explique comment utiliser l'éditeur glisser-déposer des messages in-app pour créer un formulaire d'inscription par e-mail comportant une page de confirmation."
---

# Inscription aux e-mails avec page de confirmation

> Utilisez l'éditeur par glisser-déposer des messages in-app pour créer un formulaire d'inscription par e-mail avec une page de confirmation.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Création d'un formulaire d'inscription par e-mail avec une page de confirmation

### Étape 1 : Choisissez votre modèle

 Ce modèle est pris en charge à la fois pour les applications mobiles et les navigateurs web.



### Étape 2 : Définissez les styles de vos messages

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Étape 3 : Personnalisez votre composant d'inscription à l'e-mail

Pour commencer à créer votre formulaire d'inscription par e-mail, sélectionnez l'élément de capture d'e-mail dans l'éditeur. Par défaut, les adresses e-mail collectées auront le groupe d'abonnement global **Abonné**. Pour abonner des utilisateurs à des groupes d'abonnement spécifiques, reportez-vous à la section [Mise à jour des états d'abonnement à l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)

Vous pouvez personnaliser le texte substitutif et le texte de l'étiquette de l'élément de capture d'e-mail.

![L'éditeur de messages in-app avec un menu latéral pour personnaliser l'élément de capture d'e-mail.][img2]

#### Validation de l’e-mail

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Étape 4 : Ajouter une clause de non-responsabilité (facultatif)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Étape 5 : Donnez du style à votre message

Personnalisez l'aspect et la convivialité de votre formulaire d'inscription par e-mail et de votre page de confirmation à l'aide des [composants de message in-app à][3] glisser-déposer.

## Analyse des résultats

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Bonnes pratiques

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

[img1]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %}
[img2]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %} 

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components
