---
nav_title: Formulaire de capture d’adresses e-mail
article_title: Formulaire de capture d’adresses e-mail
page_order: 3
page_type: reference
description: "Le présent article fournit un overview du type de message in-app de capture d’e-mail."
channel:
  - in-app messages
---

# Formulaire de capture d’e-mail {#email-capture-form}

> Les messages de capture d’e-mail vous permettent d’inviter facilement les utilisateurs de votre site à soumettre leur adresse e-mail, après quoi vous en disposez dans leur profil utilisateur pour l’ensemble de vos campagnes de communication.

Lorsqu’un utilisateur final saisit son adresse e-mail dans ce formulaire, l’adresse e-mail est ajoutée à son profil utilisateur.

- Pour les [utilisateurs anonymes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) qui n'ont pas encore de compte, l'adresse e-mail sera activée dans le profil utilisateur anonyme lié à l'appareil de l'utilisateur.
- Si une adresse e-mail existe déjà dans le profil utilisateur, elle est remplacée par celle saisie.
- Si l'utilisateur connu possède une adresse e-mail signalée comme ayant fait l'objet d'un [échec d'envoi définitif]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces), nous vérifierons si l'adresse e-mail nouvellement saisie diffère de celle qui figure dans son profil Braze. Si l'adresse e-mail fournie est différente, l'adresse e-mail sera mise à jour et l'état d'échec d'envoi définitif sera supprimé. 
- Si un utilisateur saisit une adresse e-mail non valide, il reçoit le message d’erreur : "Veuillez saisir un e-mail valide."
    - Adresses e-mail non valides : 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Adresses e-mail valides : 
        - `example@gmail.com`
        - `example@gnail.com` (avec une erreur)
    - Pour plus d'informations sur la validation des e-mails dans Braze, reportez-vous aux [directives et notes techniques sur l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

{% details Plus d'informations sur les utilisateurs identifiés et anonymes %}

En général, le formulaire de capture d’e-mail obéit à une logique simple. Elle définit l’adresse e-mail dans le profil utilisateur dans Braze pour l’utilisateur actuellement actif. Cependant, le comportement diffère selon que l’utilisateur est identifié (connecté, `changeUser` appelé) ou non.

Si un utilisateur anonyme saisit son e-mail dans le formulaire et le soumet, Braze ajoute l’adresse e-mail à son profil. Si `changeUser` est appelé plus tard dans leur parcours sur le web et qu'un nouveau `external_id` est attribué (par exemple lorsqu'un nouvel utilisateur s'inscrit au service), toutes les données anonymes du profil utilisateur sont fusionnées, y compris l'adresse e-mail.

Si `changeUser` est appelé avec un `external_id` existant, le profil utilisateur anonyme est orphelin et les [champs de données spécifiques du profil utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) qui n'existent pas encore pour l'utilisateur identifié sont fusionnés, mais tous les champs qui existent déjà sont perdus, y compris l'adresse e-mail.

Pour plus d'informations, reportez-vous au [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

{% enddetails %}

## Étape 1 : Créer une campagne de communication in-app

Pour accéder à cette option, vous devez créer une campagne de messagerie in-app. Ensuite, en fonction de votre cas d'utilisation, réglez l'option **Envoyer à sur** **Navigateurs web**, **Applis mobiles** ou **Applis mobiles et Navigateurs web**, puis sélectionnez **Formulaire de capture d'e-mail** comme **Type de message.**

![][4]

{% alert note %}
Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages in-app HTML peuvent en effet exécuter du JavaScript, d’où le besoin d’un responsable de site pour les activer.
{% endalert %}

## Étape 2 : Personnaliser le formulaire {#customizable-features}

Ensuite, personnalisez votre formulaire si nécessaire. Vous pouvez personnaliser les fonctions suivantes pour votre formulaire de capture d’e-mail :

- Texte de l’en-tête, du corps et du bouton Soumettre
- Une image facultative
- Un lien facultatif aux conditions de service
- Couleurs différentes pour l’en-tête et le texte du corps, les boutons et l’arrière-plan
- Paires clé-valeur
- Style pour l’en-tête et le texte du corps, les boutons, la couleur de bordure de bouton, l’arrière-plan et l’incrustation

![Composeur pour le formulaire de capture d’e-mail.][5]

Si vous avez besoin d'une personnalisation plus poussée, choisissez le **code personnalisé** pour votre **type de message.** Vous pouvez utiliser ce [modèle modal de capture d'e-mail](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) du dépôt GitHub de [modèles Braze](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) comme code de démarrage.

## Étape 3 : Définir votre audience d’entrée

Si vous souhaitez envoyer ce formulaire à des utilisateurs sans adresses e-mail existantes, utilisez le filtre `Email Available is false`.

![Le filtre par e-mail disponible est erroné][10]{: style="max-width:50%"}

Si vous souhaitez envoyer ce formulaire à des utilisateurs sans ID externes (utilisateurs anonymes), utilisez le filtre `External User ID is blank`.

![Le filtre par ID utilisateur externe est vide][11]{: style="max-width:50%"}

Vous pouvez également combiner les deux filtres à l’aide de la logique `AND`.

## Étape 4 : Cibler les utilisateurs qui ont rempli le formulaire (facultatif)

Une fois que vous avez lancé le formulaire de capture d’e-mail et recueilli des adresses e-mail de vos utilisateurs, vous pouvez cibler ces utilisateurs avec le filtre `Clicked/Opened Campaign`. 

Définissez le filtre à `Has clicked in-app message button 1` pour la campagne `<CAMPAIGN_NAME>`. Remplacez `<CAMPAIGN_NAME>` par le nom de votre campagne de formulaire de capture d’e-mail.

![Filtre pour les clics sur le bouton 1 de message in-app pour votre campagne de formulaire de capture d’e-mail Web][12]

[4]: {% image_buster /assets/img/email_capture_config.png %}
[5]: {% image_buster /assets/img/email_capture.png %}
[10]: {% image_buster /assets/img_archive/web_email_filter_1.png %}
[11]: {% image_buster /assets/img_archive/web_email_filter_2.png %}
[12]: {% image_buster /assets/img_archive/web_email_filter_3.png %}
