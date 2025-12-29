---
nav_title: "Formulaire de capture d'e-mail"
article_title: "Formulaire de capture d'e-mail"
page_order: 3
page_type: reference
description: "Cet article donne un aperçu du type de message in-app de capture d'e-mail."
channel:
  - in-app messages
---

# Formulaire de capture d'e-mail {#email-capture-form}

> Les messages de capture d'e-mail vous permettent d'inviter facilement les utilisateurs de votre site à communiquer leur adresse e-mail. Celle-ci sera ensuite disponible dans leur profil utilisateur et pourra être utilisée dans toutes vos campagnes de communication.

Lorsqu'un utilisateur final saisit son adresse e-mail dans ce formulaire, celle-ci est ajoutée à son profil utilisateur.

- Pour les [utilisateurs anonymes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) qui n'ont pas encore de compte, l'adresse e-mail sera en ligne/en production/instantanée sur le profil utilisateur anonyme lié à l'appareil de l'utilisateur.
- Si une adresse e-mail existe déjà dans le profil utilisateur, elle sera remplacée par l'adresse e-mail nouvellement saisie.
- Si l'utilisateur connu possède une adresse e-mail signalée comme ayant fait l'objet d'un [échec d'envoi définitif]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces), nous vérifierons si l'adresse e-mail nouvellement saisie diffère de celle qui figure dans son profil Braze. Si l'adresse e-mail fournie est différente, l'adresse e-mail sera mise à jour et l'état d'échec d'envoi définitif sera supprimé. 
- Si un utilisateur saisit une adresse e-mail non valide, le message d'erreur s'affiche : "Veuillez saisir un e-mail valide."
    - Adresses e-mail non valides : 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Adresses e-mail valides : 
        - `example@gmail.com`
        - `example@gnail.com` (avec une faute de frappe)
    - Pour plus d'informations sur la validation des e-mails dans Braze, reportez-vous aux [directives et notes techniques sur l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)

{% details More on identified versus anonymous users %}

En général, la logique qui sous-tend le formulaire de capture d'e-mail est simple. L'adresse e-mail du profil utilisateur dans Braze sera définie pour l'utilisateur actuellement actif. Toutefois, cela signifie que le comportement diffère selon que l'utilisateur est identifié (connecté, `changeUser` appelé) ou non.

Si un utilisateur anonyme saisit son e-mail dans le formulaire et le soumet, Braze ajoute l'adresse e-mail à son profil. Si `changeUser` est appelé plus tard dans son parcours sur le web et qu'un nouveau `external_id` est attribué (par exemple lorsqu'un nouvel utilisateur s'inscrit au service), toutes les données anonymes du profil de l'utilisateur sont fusionnées, y compris l'adresse e-mail.

Si `changeUser` est appelé avec un `external_id` existant, le profil utilisateur anonyme est orphelin et les [champs de données spécifiques du profil utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) qui n'existent pas encore pour l'utilisateur identifié sont fusionnés, mais tous les champs qui existent déjà sont perdus, y compris l'adresse e-mail.

Pour plus d'informations, reportez-vous au [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

{% enddetails %}

## Étape 1 : Créer une campagne de messages in-app

Pour naviguer vers cette option, vous devez créer une campagne d'envoi de messages in-app. Ensuite, en fonction de votre cas d'utilisation, réglez l'option **Envoyer à** soit aux **navigateurs web**, soit aux **applications mobiles**, soit **aux deux applications mobiles & navigateurs web**, puis sélectionnez **Formulaire de capture d'e-mail** comme **Type de message.**

{% alert note %}
**Le ciblage des internautes ?** <br>Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Ceci pour des raisons de sécurité puisque les messages in-app en HTML peuvent exécuter du JavaScript, nous demandons donc à un responsable de site de les activer.
{% endalert %}

## Étape 2 : Personnaliser le formulaire {#customizable-features}

Ensuite, personnalisez votre formulaire selon vos besoins. Vous pouvez personnaliser les fonctionnalités suivantes pour votre formulaire de capture d'e-mail :

- Texte de l'en-tête, du corps et du bouton de soumission
- Une image facultative
- Un lien facultatif vers les "Conditions de service".
- Différentes couleurs pour l'en-tête et le corps du texte, les boutons et l'arrière-plan
- Paires clé-valeur
- Style pour le texte de l'en-tête et du corps, les boutons, la couleur de la bordure des boutons, l'arrière-plan et l'incrustation.

\![Composer pour le formulaire de capture d'e-mail.]({% image_buster /assets/img/email_capture.png %})

Si vous avez besoin d'une personnalisation plus poussée, choisissez le **code personnalisé** pour votre **type de message.** Vous pouvez utiliser ce [modèle de fenêtre modale/boîte de dialogue de capture d'e-mail](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) du dépôt GitHub Braze [Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) comme code de démarrage.

## Étape 3 : Définissez votre audience d'entrée

Si vous utilisez un message in-app pour capturer les e-mails des utilisateurs, vous pouvez limiter l'audience aux utilisateurs qui n'ont pas encore fourni ces informations.

- **Pour cibler les utilisateurs qui n'ont pas d'adresse e-mail :** Utilisez le filtre `Email Available` est `false`. Ainsi, le formulaire n'apparaît qu'aux utilisateurs qui n'ont pas d'e-mail dans leur dossier, ce qui vous permet d'éviter les invites redondantes pour les utilisateurs connus.
- **Pour cibler les utilisateurs anonymes sans ID externe :** Utilisez le filtre `External User ID` `is blank`. Cette fonction est utile lorsque vous souhaitez identifier des utilisateurs qui n'ont pas encore été authentifiés ou enregistrés.

Vous pouvez également combiner les deux filtres en utilisant la logique `AND`, si vous le souhaitez. Ainsi, le formulaire ne s'affiche que pour les utilisateurs auxquels il manque une adresse e-mail et un ID externe, ce qui est idéal pour capturer de nouveaux prospects ou inciter à la création d'un compte.

## Étape 4 : Cibler les utilisateurs qui ont rempli le formulaire (facultatif)

Après avoir lancé le formulaire de capture d'e-mail et collecté les adresses e-mail de vos utilisateurs, vous pouvez cibler les utilisateurs qui ont rempli le formulaire.

1. Dans n'importe quel filtre de segmentation dans Braze, sélectionnez le filtre `Clicked/Opened Campaign`. 
2. Dans la liste déroulante, sélectionnez `clicked in-app message button 1`
3. Sélectionnez la campagne de votre formulaire de capture d'e-mail.

