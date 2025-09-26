---
nav_title: Inscription intégrée
article_title: Inscription intégrée à WhatsApp
page_order: 0
description: "Cet article de référence fournit une marche à suivre étape par étape pour le flux de travail d'inscription intégré à WhatsApp dans Braze."
page_type: reference
channel:
  - WhatsApp
---

# Inscription intégrée à WhatsApp

> Cet article de référence fournit une marche à suivre étape par étape pour le flux de travail d'inscription intégré à WhatsApp dans Braze.

Le flux d'inscription intégré à WhatsApp est accessible lorsque vous [intégrez WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) pour la première fois dans votre espace de travail Braze, et lorsque vous [ajoutez un compte WhatsApp Business]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/) à une intégration WhatsApp existante.

{% alert note %}
Vous pouvez ajouter [plusieurs comptes WhatsApp Business](({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)) à un espace de travail Braze. Cependant, chaque compte professionnel WhatsApp spécifique ne peut être ajouté qu'à un seul espace de travail Braze.
{% endalert %}

## Accéder au flux de travail

Allez dans **Intégrations partenaires** > **Partenaires technologiques**, puis recherchez et sélectionnez **WhatsApp.** Le choix suivant dépend de votre cas d'utilisation :

- Si vous intégrez WhatsApp à votre espace de travail, sélectionnez **Commencer l'intégration**. <br><br>![Page partenaire de WhatsApp avec un bouton pour commencer l'intégration.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- Si vous ajoutez un compte WhatsApp Business à une intégration WhatsApp existante, sélectionnez **Ajouter un compte WhatsApp Business**. <br><br>!["Intégration de l'envoi de messages WhatsApp" avec des options permettant d'ajouter un compte professionnel WhatsApp ou un groupe d'abonnement et un numéro.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}).{: style="max-width:80%;"}

À partir de là, le flux de travail est le même pour les deux cas d'utilisation.

## Processus d'inscription intégré à WhatsApp

1. Dans la fenêtre de connexion à Meta (Facebook), sélectionnez **Se connecter en tant que** ou **Continuer**. <br><br>![Fenêtre d'identification Meta.]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Lisez les autorisations que vous partagerez avec Braze, puis sélectionnez **Démarrer**. <br><br>![Liste des autorisations que vous partagerez avec Braze pour l'intégration.]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. Dans la liste déroulante **Portefeuille d'activités**, sélectionnez votre portefeuille d'activités, puis cliquez sur **Suivant**. Cette fonction se connecte à votre compte WhatsApp Business. Si vous ne voyez pas votre portefeuille professionnel prévu, vérifiez vos autorisations.<br><br>![Une fenêtre avec des champs pour saisir les informations relatives à votre entreprise, y compris le nom de votre portefeuille d'entreprise.]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. Sélectionnez les éléments suivants pour les champs déroulants, puis sélectionnez **Suivant**.
- **Choisissez un compte WhatsApp Business :** Créez un compte professionnel WhatsApp
- **Créez ou sélectionnez un profil WhatsApp Business :** Créez un nouveau profil professionnel WhatsApp <br><br>![Champs à spécifier si vous choisissez ou créez un compte et un profil WhatsApp Business.]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. Fournissez les informations suivantes, puis sélectionnez **Suivant**.
- Nom du compte professionnel WhatsApp
- Nom d'affichage de l'entreprise WhatsApp
- Catégorie <br><br>![Champs permettant de fournir des détails sur le nouveau compte WhatsApp Business.]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. Saisissez votre numéro de téléphone et choisissez entre le **message texte** et l'**appel téléphonique**. Ce numéro doit répondre à toutes les exigences d'un numéro de téléphone WhatsApp, notamment ne pas être associé à d'autres comptes WhatsApp. <br><br>![Champs pour ajouter un numéro de téléphone.]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. Saisissez votre code d'authentification à deux facteurs, puis sélectionnez **Suivant**. <br><br>![Champ de saisie d'un code d'authentification à deux facteurs.]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. Passez en revue les autorisations que votre compte WhatsApp Business recevra, puis sélectionnez **Continuer**. <br><br>![Liste des autorisations demandées par le compte WhatsApp Business.]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. Vous avez terminé ! <br><br>![Fenêtre indiquant que vous êtes prêt à envoyer des messages.]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}

