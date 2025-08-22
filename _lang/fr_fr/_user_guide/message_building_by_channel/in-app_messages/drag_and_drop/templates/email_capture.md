---
nav_title: "Formulaire d'inscription par e-mail"
article_title: "Formulaire d'inscription par e-mail"
alias: "/email_capture/"
page_order: 2
description: "Cette page explique comment créer un formulaire d'inscription par e-mail avec l'éditeur glisser-déposer de messages in-app."
---

# Formulaire d'inscription par e-mail

> Utilisez le modèle de message in-app d'inscription par e-mail par glisser-déposer pour collecter les adresses e-mail des utilisateurs et développer vos groupes d'abonnement.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Création d'un formulaire d'inscription par e-mail

### Étape 1 : Choisissez votre modèle

Lorsque vous créez un message in-app par glisser-déposer, sélectionnez **Inscription par e-mail** pour votre modèle, puis **Construire un message.** Ce modèle est pris en charge à la fois pour les applications mobiles et les navigateurs web.

![L'éditeur de messages in-app avec le modèle de formulaire de capture d'e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Étape 2 : Définissez les styles de vos messages

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Étape 3 : Personnalisez votre composant d'inscription à l'e-mail

Pour commencer à créer votre formulaire d'inscription par e-mail, sélectionnez l'élément de capture d'e-mail dans l'éditeur. Par défaut, les adresses e-mail collectées auront le groupe d'abonnement global **Abonné**. Pour abonner des utilisateurs à des groupes d'abonnement spécifiques, reportez-vous à la section [Mise à jour des états d'abonnement à l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)

Vous pouvez personnaliser le texte substitutif et le texte de l'étiquette de l'élément de capture d'e-mail.

![L'éditeur de messages in-app avec un menu latéral pour personnaliser l'élément de capture d'e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### Validation de l’e-mail

Si l'utilisateur saisit une adresse e-mail contenant des caractères spéciaux non acceptés, il verra apparaître un indicateur d'erreur générique et ne pourra pas soumettre le formulaire. Ce message d'erreur n'est pas personnalisable. Vous pouvez visualiser le comportement de l'erreur dans l'onglet **Prévisualisation et test** et sur votre appareil de test. Pour en savoir plus sur la manière dont Braze formate les adresses e-mail, consultez la rubrique [Validation de l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)

### Étape 4 : Ajouter une clause de non-responsabilité (facultatif)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Étape 5 : Donnez du style à votre message

Personnalisez l'aspect et la convivialité de votre formulaire d'inscription à l'aide des [composants de message in-app à]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) glisser-déposer.

## Analyse des résultats

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Bonnes pratiques

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

