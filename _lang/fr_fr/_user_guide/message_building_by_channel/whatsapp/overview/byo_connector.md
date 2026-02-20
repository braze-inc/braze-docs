---
nav_title: Connecteur WhatsApp BYO
article_title: Apportez votre propre connecteur WhatsApp
page_order: 0
description: "Cet article de référence fournit une marche à suivre étape par étape pour gérer un connecteur WhatsApp Bring Your Own, qui permet à Braze d'accéder à votre gestionnaire WhatsApp Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Apportez votre propre connecteur WhatsApp

> Le connecteur WhatsApp Bring Your Own (BYO) propose un partenariat entre Braze et Infobip, dans le cadre duquel vous donnez à Braze l'accès à votre gestionnaire WhatsApp d'Infobip (WABA). Cela vous permet de gérer et de payer les coûts d'envoi de messages directement avec Infobip tout en utilisant Braze pour la segmentation, la personnalisation et l'orchestration des campagnes. Braze conserve toutes les fonctionnalités existantes offertes par le canal WhatsApp, telles que les messages sortants, le traitement des messages entrants, les flux WhatsApp et l'analyse/analytique.

## Conditions 

| Exigence | Description |
| --- | --- |
| Compte Infobip | Un compte Infobip est nécessaire pour utiliser le connecteur WhatsApp BYO.
| Crédits d'envoi de messages | Vous consommez des crédits d'envoi de messages Braze lorsque vous envoyez des messages WhatsApp. |
| Exigences de WhatsApp | Remplir toutes les [conditions requises par WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#prerequisites). |
| Numéro de téléphone | Nous vous suggérons d'[acquérir un numéro de téléphone par l'intermédiaire d'Infobip](https://www.infobip.com/docs/numbers/getting-started) pour plus de commodité. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Mise en place 

Avant de configurer le connecteur WhatsApp BYO, confirmez que les précédents envois de votre compte WhatsApp Business n'ont pas été effectués par l'intermédiaire d'Infobip.

### Cas pris en charge

- Le compte WhatsApp Business et le numéro de téléphone n'ont jamais été connectés à un partenaire auparavant.
- Le compte professionnel WhatsApp est directement connecté à Braze grâce à l'intégration native.
    - Suivez les étapes de la [migration des]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/) numéros de téléphone [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/) pour migrer vos numéros de téléphone vers un nouveau compte WhatsApp Business, un numéro de téléphone à la fois.
- Le compte professionnel WhatsApp est connecté à un fournisseur de solutions différent de Braze et d'Infobip.
    - Suivez les étapes de la [migration des]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/) numéros de téléphone [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/) pour migrer vos numéros de téléphone vers un nouveau compte WhatsApp Business, un numéro de téléphone à la fois.

## Étape 1 : Récupérer les informations du compte Infobip {#step-1}

1. Dans Infobip, identifiez le compte que vous souhaitez utiliser avec votre compte WhatsApp Business. 
2. Allez dans **Outils du développeur** > **Clés API** et sélectionnez **Créer une clé API.**

![Page "Créer une clé API" avec une date de création de "16/12/2025" et une date d'expiration de "16/12/36".]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3\. Donnez à la clé un nom significatif, tel que "Braze - Nom de mon espace de travail - Nom de mon WABA".
4\. Ajoutez une date d'expiration éloignée dans le temps pour éviter les problèmes liés à l'expiration des jetons.
    \- Prenez note de générer une nouvelle clé API et de reconnecter votre WABA avant la date d'expiration.
5\. Sélectionnez ces champs d'application :
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. Après avoir créé la clé, copiez la clé API.
    - La clé ne peut être copiée que pendant une période limitée après sa création. Vous pouvez répéter ces étapes pour créer une nouvelle clé si vous devez connecter un autre compte WhatsApp Business à l'avenir.

!["Braze Example API clé" avec 6 champs d'application ajoutés.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7\. Copiez l'URL de base de l'API du compte.

![Page "clés API" avec mise en évidence de l'URl de base de l'API.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## Étape 2 : Lancez l'inscription intégrée

1. Dans Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** > **WhatsApp**.
2. Sélectionnez l'onglet **BYO Connector - Infobip**.

![La page de partenaires technologiques de WhatsApp.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3\. Saisissez la clé API et l'URL de base de l'[étape 1.](#step-1)
4\. Sélectionnez **Connecter**.
5\. Procédez à l'[inscription intégrée en]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/#whatsapp-embedded-signup-workflow) tenant compte de ces considérations :
- Vous ne pouvez pas sélectionner le même portefeuille d'activités qui est utilisé par un autre fournisseur de solutions d'affaires.
- Vous ne pouvez pas sélectionner un numéro de téléphone utilisé par un autre Business Solution Provider.
- Vous devez créer un nouveau WABA, et non pas sélectionner un WABA existant.

{% alert note %}
Pour recevoir le code de vérification, allez dans votre tableau de bord Infobip > **Analyser** > **Journaux**, et extrayez le code du message SMS entrant.  
{% endalert %}

![Envoi de messages montrant un message SMS entrant avec le code de vérification.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Une fois la configuration terminée, votre numéro de téléphone est répertorié en tant que groupe d'abonnement sous votre WhatsApp Business Group. Le groupe d'entreprises WhatsApp contient le nom du compte Infobip et l'URL de base de l'API à laquelle il est connecté. Les comptes connectés via l'intégration native n'ont pas de nom de compte Infobip.

{% alert note %}
Connectez chaque compte WhatsApp Business à un seul compte Infobip. Chaque fois que vous connectez un numéro de téléphone ou un groupe d'abonnement supplémentaire, si le compte WhatsApp Business est déjà connecté à un compte Infobip, vous devez saisir à nouveau les identifiants API du compte existant.
{% endalert %}

## Étape 3 : Envoi de messages

Suivez le processus d'envoi de l'intégration native, y compris :
- [Abonner des utilisateurs au groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)
- [Créer un message WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)

## Résolution des problèmes de configuration

### Impossible de récupérer l'ID du compte WhatsApp Business

Confirmez que votre compte WhatsApp Business n'est pas connecté à un autre espace de travail Braze.

### Impossible de partager l'ID du compte WhatsApp Business avec Infobip

1. Confirmez que votre compte WhatsApp Business n'est pas connecté à Braze ou à un autre partenaire.
2. Confirmez qu'aucun numéro de téléphone de votre compte WhatsApp Business n'est connecté à un autre compte Infobip. Pour les numéros importés, vous pouvez trouver le numéro dans Infobip et sélectionner **Annuler le numéro**.

![Le bouton "Annuler le numéro" pour un numéro Infobip.]({% image_buster /assets/img/whatsapp/byo_connector/cancel_number.png %})

## Considérations 


Bien que toutes les fonctionnalités existantes de Braze soient prises en charge, ces cas d'utilisation ne sont actuellement pas pris en charge.

| Cas d’utilisation | Raison |
| --- | --- |
| Traitement des messages entrants dans Braze et Infobip | Cela permet d'éviter les trains logiques qui sont déclenchés par l'un ou l'autre système, générant ainsi des fils de messages en double et potentiellement contradictoires. |
| Envoi de messages depuis Braze et Infobip | Pour les comptes WhatsApp Business connectés à Braze, tous les envois proviennent de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

