---
nav_title: "Comptes d'entreprise multiples" 
article_title: Plusieurs comptes et numéros de téléphone WhatsApp pour les entreprises
page_order: 2
description: "Cet article de référence décrit les étapes à suivre pour ajouter des comptes et des numéros de téléphone WhatsApp Business."
page_type: reference
channel:
  - WhatsApp
---

# Plusieurs comptes et numéros de téléphone WhatsApp Business

> Vous pouvez ajouter plusieurs comptes WhatsApp Business et groupes d'abonnement (et numéros de téléphone) à chaque espace de travail. <br><br>Chaque groupe d'abonnement est connecté à un numéro de téléphone unique. Vous ne pouvez donc pas connecter le même numéro de téléphone à plusieurs groupes d'abonnement ou connecter plusieurs numéros de téléphone à un groupe d'abonnement.

## Plusieurs comptes WhatsApp Business 

Disposer de plusieurs comptes WhatsApp Business est utile si vous souhaitez envoyer des messages WhatsApp aux utilisateurs d'un espace de travail Braze qui compte plusieurs marques. En effet, chaque compte professionnel fonctionne séparément au sein de WhatsApp et dispose de son propre numéro de téléphone, de son propre modèle de message et de sa propre note de qualité.

Les comptes commerciaux imbriqués dans le même gestionnaire Meta Business Manager partageront également la gestion des autorisations d'accès des utilisateurs et les catalogues (pas encore pris en charge sur Braze).

![Diagramme de l'écosystème Braze et WhatsApp, montrant comment les espaces de travail et les comptes WhatsApp Business se connectent les uns aux autres : vous pouvez connecter un groupe d'abonnement à un numéro de téléphone, plusieurs comptes WhatsApp Business à un espace de travail, et un espace de travail à plusieurs portefeuilles Meta Business.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}). 

### Ajouter un compte WhatsApp Business

Vous pouvez ajouter jusqu'à 10 comptes WhatsApp Business par espace de travail. Les comptes commerciaux peuvent être imbriqués dans différents gestionnaires de méta-domaines d'activité. Pour ajouter un compte :

1. Allez dans **Partenaires technologiques** > **WhatsApp** et sélectionnez **Ajouter un compte professionnel WhatsApp.** 

![Section sur l'intégration de l'envoi de messages WhatsApp avec des options permettant d'ajouter un compte professionnel ou d'ajouter un groupe d'abonnement et un numéro.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Suivez le processus d'inscription. Pour une description détaillée des étapes, reportez-vous à l'[inscription intégrée à WhatsApp.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)

{% alert important %}
Votre numéro de téléphone doit répondre à toutes les exigences d'un numéro de téléphone WhatsApp, notamment ne pas être associé à d'autres comptes WhatsApp.
{% endalert %}

## Groupes d'abonnement et numéros de téléphone multiples

Les modèles de messages sont partagés entre tous les numéros de téléphone d'un même compte WhatsApp Business. Pour en savoir plus sur les groupes d'abonnement WhatsApp, consultez la section [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).

Chaque numéro de téléphone WhatsApp apparaîtra comme une discussion WhatsApp distincte pour les utilisateurs. Chaque numéro de téléphone d'un compte WhatsApp Business fonctionne indépendamment des autres, de sorte qu'ils peuvent avoir les mêmes valeurs ou des valeurs différentes pour les éléments suivants : 
- Nom d'affichage 
- État 
- Note de qualité 
- Limite d'envoi de messages 

### Ajout d'un groupe d'abonnement et d'un numéro de téléphone

Vous pouvez ajouter jusqu'à 20 groupes d'abonnement (et numéros de téléphone d'envoi) par compte WhatsApp Business. Pour ajouter un groupe d'abonnement et un numéro de téléphone :

1. Allez dans **Partenaires technologiques** > **WhatsApp** et sélectionnez **Ajouter un groupe d'abonnement et un numéro.**

![Section sur l'intégration de l'envoi de messages WhatsApp avec des options permettant d'ajouter un compte professionnel ou d'ajouter un groupe d'abonnement et un numéro.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Suivez le processus d'inscription. <br><br> À l'étape **Sélectionner votre compte WhatsApp Business**, sélectionnez votre compte WhatsApp Business existant et ajoutez un nouveau numéro de téléphone. Ce numéro doit répondre à toutes les exigences d'un numéro de téléphone WhatsApp, notamment ne pas être associé à d'autres comptes WhatsApp.

### Suppression d'un groupe d'abonnement et d'un numéro de téléphone 

1. Allez dans **Audience** > **Abonnements** et archivez le groupe d'abonnement.
2. Allez dans votre gestionnaire Meta Business et supprimez le numéro de téléphone.
