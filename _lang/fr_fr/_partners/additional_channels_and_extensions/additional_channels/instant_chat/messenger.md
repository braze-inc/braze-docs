---
nav_title: Messager
article_title: Facebook Messenger
alias: /partners/messenger/
description: "Cet article de référence présente le partenariat entre Braze et Facebook Messenger, l'une des plateformes de messagerie instantanée les plus populaires au monde."
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) est l'une des plateformes de messagerie instantanée les plus populaires au monde, utilisée par près d'un milliard d'utilisateurs actifs par mois. Grâce à cette plateforme, les marques peuvent créer des chatbots engageants pour interagir de manière intelligente et automatique avec leurs clients.

L'intégration Braze et Facebook exploite les webhooks Braze, les fonctionnalités de segmentation, de personnalisation et de déclenchement pour envoyer des messages à vos utilisateurs dans Facebook Messenger via l'API de la plateforme Messenger. Un modèle de webhook Facebook Messenger personnalisé est inclus dans notre plateforme sous **Modèles** > **Modèles de webhook.**

La plateforme Facebook Messenger est destinée aux "messages non promotionnels qui facilitent une transaction préexistante, fournissent d'autres actions d'assistance à la clientèle ou livrent un contenu demandé par une personne." Pour en savoir plus, consultez [les lignes directrices de la plateforme Facebook](https://developers.facebook.com/docs/messenger-platform) et des [exemples de cas d'utilisation acceptables](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Conditions préalables

Prenez connaissance des éléments suivants avant de procéder à l'intégration :
- Facebook n'autorise pas l'utilisation de la plateforme Messenger pour l'envoi de messages marketing. 
- Vous devez obtenir l'autorisation explicite de l'utilisateur pour envoyer des messages à partir de votre page. 
- Pour envoyer des messages aux utilisateurs qui ne sont pas des utilisateurs de test de votre application Facebook, votre application devra passer l'[examen de validation](https://developers.facebook.com/docs/messenger-platform/app-review) de Facebook.<br><br>

| Exigence| Origine| Accès| Description|
| ---| ---| ---|
| Page Facebook Messenger| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Une page Facebook sera utilisée comme identité de votre bot. Lorsque les utilisateurs discutent avec votre application, ils voient le nom de la page et la photo de profil.|
| Application Facebook Messenger| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | L'appli Facebook contient les paramètres de votre bot Messenger, notamment les jetons d'accès.
| Vérification et approbation du robot de l’application | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | Lorsque vous êtes prêt à rendre votre bot public, vous devez le soumettre à Facebook pour examen et approbation. Ce processus d'examen nous permet de nous assurer que votre robot Messenger respecte nos politiques et fonctionne comme prévu avant de le mettre à la disposition de tous sur Messenger. |
| ID de portée de page (PSID) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Vous devez avoir des PSID d'utilisateurs pour envoyer des messages sur Facebook Messenger. Lorsqu'un utilisateur interagit avec votre appli via Messenger, Facebook crée un PSID. Ce PSID peut être envoyé à Braze sous la forme d'une chaîne de caractères d'attribut personnalisé.
| Jeton d'accès à la page | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | Ces jetons d'accès sont similaires aux jetons d'accès des utilisateurs, sauf qu'ils fournissent une autorisation aux API qui lisent, écrivent ou modifient les données appartenant à une page Facebook. Pour obtenir un jeton d'accès à une page, vous devez obtenir un jeton d'accès utilisateur et demander l’autorisation `manage_pagespermission`. Après avoir obtenu le jeton d'accès d'utilisateur, vous obtenez ensuite le jeton d'accès de la page via l'API Graph.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration

Vous trouverez ci-après des explications pour la configuration d’un webhook Facebook Messenger Braze.
Pour ceux qui ont besoin d'aide supplémentaire pour configurer leur robot, un tutoriel complet sur le robot Messenger et un code d'exemple sont disponibles dans le [dépôt GitHub de Braze](https://github.com/Appboy/appboy-fb-messenger-bot) !

### Étape 1 : Collectez vos PSID

Pour envoyer des messages sur Facebook Messenger, vous devez collecter les ID spécifiques à la page (PSID) de vos utilisateurs afin de les identifier et d'interagir avec eux de manière cohérente. Les PSID ne sont pas les mêmes que l'ID Facebook de l'utilisateur. Facebook crée cet identifiant chaque fois que vous envoyez un message à un client ou qu'un client vous envoie un message.

Les PSID peuvent être trouvés en utilisant l'un des différents [points d'entrée](https://developers.facebook.com/docs/messenger-platform/discovery) proposés par Facebook. Une fois que l'utilisateur a envoyé un message à votre application ou effectué une action dans le cadre d'une conversation, comme appuyer sur un bouton ou envoyer un message, son PSID sera inclus dans la propriété `sender.id` de l'événement webhook, afin que votre bot puisse identifier qui a effectué l'action.

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

Chaque fois que vous envoyez un message, son PSID sera inclus dans la propriété `recipient.id` de la requête afin d'identifier la personne qui doit recevoir le message.

### Étape 2 : Envoyer à Braze comme attribut personnalisé

Une fois que vous êtes certain de recevoir des PSID, coordonnez et partagez cela avec vos développeurs pour envoyer les PSID à Braze en tant qu'[attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/#custom-attributes). Les PSID sont des chaînes de caractères auxquelles on peut accéder en faisant un [appel à l'API](https://developers.facebook.com/docs/messenger-platform/reference/send-api).

### Étape 3 : Configurez votre modèle de webhook

Dans **Modèles et médias**, allez dans **Modèles de webhook** et choisissez le **modèle de webhook Facebook Messenger.**

1. Donnez un nom au modèle et ajoutez des Teams et des tags, si nécessaire.
2. Saisissez votre message ou choisissez un modèle de message parmi [ceux mis à disposition par Facebook](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages). Vous pouvez également choisir le [type](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) de message ou la [balise](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags).
3. Inclure le PSID en tant qu'attribut personnalisé. Pour ce faire, utilisez le bouton bleu et blanc **+** dans le coin de la boîte du **corps de la requête**.
3. Ajoutez votre jeton d'accès à la page dans l'URL du webhook en remplaçant `FACEBOOK_PAGE_ACCESS_TOKEN` par votre jeton.

#### Prévisualisation et test de votre webhook

Avant d'envoyer votre message, testez votre webhook. Assurez-vous que votre ID Messenger est enregistré dans Braze (ou trouvez-le et testez-le en tant qu'utilisateur personnalisé), et utilisez l'aperçu pour envoyer le message de test :

![L'onglet Test dans le modèle de webhook Facebook Messenger vous permet de prévisualiser le message en l'envoyant à un utilisateur existant.]({% image_buster /assets/img_archive/fbm-test.png %})

Si vous recevez le message avec succès, vous pouvez configurer ses paramètres de distribution.

## Grâce à cette intégration

Une fois configurée, utilisez cette intégration pour cibler les utilisateurs de Facebook Messenger. Si vous n'envoyez pas de messages en utilisant les numéros de téléphone des utilisateurs et que vous prévoyez d'envoyer des messages Messenger de manière répétée, vous devriez [créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) pour tous les utilisateurs pour lesquels l'ID Messenger existe en tant qu'attribut personnalisé et activer le [suivi analytique]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/) pour suivre vos taux d'abonnement Messenger au fil du temps. 

![Le filtre de segmentation "messenger_id" est réglé sur "is not blank".]({% image_buster /assets/img_archive/fbm-segmentation.png %})

Si vous choisissez de ne pas créer de segmentation spécifique pour les abonnés Messenger, veillez à inclure un filtre pour les ID Messenger existants afin d'éviter les erreurs.

Vous pouvez également utiliser d'autres segmentations pour cibler vos campagnes Messenger, ainsi que le reste du processus de création de campagne, comme pour toute autre campagne.

