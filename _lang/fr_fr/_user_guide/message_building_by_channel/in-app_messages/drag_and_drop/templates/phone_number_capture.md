---
nav_title: "Formulaire d'inscription par SMS, RCS et WhatsApp"
article_title: "Formulaire d'inscription par SMS, RCS et WhatsApp"
alias: "/phone_number_capture/"
page_order: 1
description: "Cette page explique comment créer un formulaire d'inscription par SMS, RCS et WhatsApp avec l'éditeur glisser-déposer de messages in-app."
---

# Formulaire d'inscription par SMS, RCS et WhatsApp

> Les formulaires d'inscription SMS, RCS et WhatsApp sont des modèles disponibles dans l'éditeur par glisser-déposer pour les messages in-app. Utilisez ces modèles pour collecter les numéros de téléphone des utilisateurs et développer vos groupes d'abonnement SMS, MMS, RCS et WhatsApp.

Trois exemples de messages in-app créés à l'aide du modèle de formulaire d'inscription par téléphone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Création d'un formulaire d'inscription à un numéro de téléphone

### Étape 1 : Choisissez votre modèle

Lorsque vous créez un message in-app par glisser-déposer, sélectionnez l'**inscription par SMS** (cela s'adapte à l'inscription par RCS) ou l'**inscription par WhatsApp** pour votre modèle, puis sélectionnez **Créer un message.** Ces modèles sont pris en charge à la fois pour les applications mobiles et les navigateurs web.

\![Fenêtre modale pour sélectionner l'inscription par SMS ou l'inscription par WhatsApp comme modèle lors de la création d'un message in-app.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Étape 2 : Définissez les styles de vos messages

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

Workflow de téléchargement et de sélection d'une police personnalisée.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Étape 3 : Personnalisez le composant de saisie de votre numéro de téléphone

Pour commencer à créer votre formulaire d'inscription, sélectionnez le composant de saisie du numéro de téléphone dans l'éditeur.

Zone de prévisualisation lors de la création d'un formulaire d'inscription avec le composant de saisie du numéro de téléphone sélectionné.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

Dans le menu latéral, indiquez le groupe d'abonnement pour lequel ce modèle collectera des numéros de téléphone. Pour respecter les meilleures pratiques en matière de conformité, vous ne pouvez recueillir le consentement qu'à un seul groupe d'abonnement par formulaire d'inscription au numéro de téléphone. Toutefois, si vous le souhaitez, vous pouvez utiliser plusieurs formulaires afin de recueillir le consentement pour d'autres groupes d'abonnement.

\![Déroulement du groupe d'abonnement avec un groupe d'abonnement sélectionné.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

Par défaut, nous collectons les numéros dans le monde entier, mais vous pouvez limiter le nombre de pays à partir desquels nous collectons les numéros. Cette fonction est utile si vous avez l'intention de n'envoyer des messages qu'aux utilisateurs dont les numéros de téléphone se trouvent dans des pays spécifiques, et peut contribuer à la propreté de la liste. Pour ce faire, désactivez la fonction **Collecter les numéros de tous les pays** et utilisez le menu déroulant pour sélectionner des pays spécifiques. Vos utilisateurs ne pourront sélectionner que les pays que vous avez explicitement ajoutés.

\![Liste déroulante des pays pour sélectionner les pays dont vous voulez collecter les numéros.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Numéros de téléphone invalides

Si vos utilisateurs saisissent un numéro de téléphone comportant des caractères spéciaux non acceptés, ils verront apparaître un indicateur d'erreur générique non personnalisable et ne pourront pas soumettre le formulaire. Vous pouvez visualiser le comportement de l'erreur dans l'onglet **Preview & Test** et sur votre appareil de test. Consultez cet article pour savoir [comment Braze formate les numéros de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers).

### Étape 4 : Ajouter une clause de non-responsabilité (pour les formulaires d'inscription par SMS et RCS)

Pour les formulaires d'inscription par SMS et RCS, il est important de communiquer clairement le type de SMS ou RCS que vous allez envoyer. Assurez-vous que la croissance de votre liste est conforme en incluant les informations suivantes dans votre formulaire :

- Description des types d'envois SMS et RCS auxquels vos clients peuvent s'attendre (rappels de panier, promotions et offres, rappels de rendez-vous, etc.) Vous n'avez pas besoin d'énumérer tous les cas d'utilisation, mais vous devez fournir une description des types de messages que votre marque enverra.
- Notez que le consentement n'est pas une condition d'achat (le cas échéant).
- Fréquence des messages et rappel que les tarifs des messages et des données s'appliquent. Si vous ne connaissez pas la fréquence exacte des messages, vous pouvez dire que la fréquence peut varier.
- Liens vers vos Conditions & Conditions et Politique de confidentialité SMS et RCS.
- Rappel des mots-clés d'aide et d'abonnement (HELP pour l'aide ; STOP pour l'annulation).

Nous avons fourni une marque substitutive dans le modèle uniquement à titre d'exemple - elle ne constitue pas un avis juridique et ne doit pas être utilisée à des fins de conformité. Il est important de travailler avec votre équipe juridique pour élaborer un langage adapté à votre marque spécifique.

{% alert note %}
Cette documentation n'a pas pour but de fournir des conseils juridiques et ne peut être considérée comme telle.
{% endalert %}

Pour plus d'informations sur la conformité des SMS et du RCS, consultez la rubrique [Lois et réglementations relatives aux SMS, MMS et RCS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)

### Étape 5 : Donnez du style à votre message

Personnalisez l'aspect et la convivialité de votre message à l'aide des [composants de message in-app à]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) glisser-déposer.

## Analyse des résultats

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

Panneau de performance des messages in-app montrant les clics pour chaque lien dans le message in-app.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})


