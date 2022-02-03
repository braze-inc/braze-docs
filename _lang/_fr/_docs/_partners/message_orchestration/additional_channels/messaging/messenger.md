---
nav_title: Messager
article_title: Messenger Facebook
alias: /fr/partners/messenger/
description: "Cet article décrit le partenariat entre Braze et Facebook Messenger, l’une des plateformes de messagerie instantanée les plus populaires au monde."
page_type: partenaire
search_tag: Partenaire
---

# Messenger Facebook

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) est l'une des plateformes de messagerie instantanée les plus populaires au monde, utilisée par près d'un milliard d'utilisateurs actifs mensuels. Grâce à cette plate-forme, les marques peuvent créer des chatbots attrayants pour interagir intelligemment et automatiquement avec leurs clients.

L'intégration de Braze et Facebook met à profit les webhooks, la segmentation, la personnalisation et les fonctionnalités de déclenchement de Braze pour envoyer des messages à vos utilisateurs dans Facebook Messenger à travers l'API Messenger Platform. Un modèle de webhook Facebook Messenger personnalisé est inclus dans notre plateforme sous **Modèles & Médias**.

La plateforme Facebook Messenger est destinée à « des messages non promotionnels qui facilitent une transaction préexistante, fournir d'autres actions d'assistance à la clientèle ou fournir le contenu demandé par une personne." Pour en savoir plus, consultez [les directives de plateforme Facebook](https://developers.facebook.com/docs/messenger-platform) et [les exemples de cas d'utilisation acceptables](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Pré-requis

Veuillez prendre acte de ce qui suit avant de procéder à l'intégration :
- Facebook ne permet pas l'utilisation de la plate-forme Messenger pour envoyer des messages marketing.
- Vous aurez besoin de la permission explicite de l'utilisateur pour les messages de votre page.
- Pour envoyer des messages aux utilisateurs qui ne sont pas des utilisateurs de test de votre application Facebook, votre application devra passer la révision de l'application [de Facebook](https://developers.facebook.com/docs/messenger-platform/app-review).<br><br>

| Exigences                                    | Origine  | Accès                                                                                                                                                                                                        | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Page Facebook Messenger                      | Facebook | [https://www.facebook.com/pages/creer](https://www.facebook.com/pages/create)                                                                                                                                | Une page Facebook sera utilisée comme identité de votre bot. Quand des gens discutent avec votre application, ils verront le nom de la page et la photo de profil.                                                                                                                                                                                                                                                                                            |
| Application Facebook Messenger               | Facebook | [https://developers.facebook.com/apps](https://developers.facebook.com/apps)                                                                                                                                 | L'application Facebook contient les paramètres de votre bot Messenger, y compris les jetons d'accès.                                                                                                                                                                                                                                                                                                                                                          |
| Revue et approbation du bot de l'application | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review)                                                                     | Lorsque vous êtes prêt à publier votre bot au public, vous devez le soumettre à Facebook pour vérification et approbation. Ce processus de révision nous permet de nous assurer que votre bot Messenger respecte nos politiques et nos fonctions comme prévu avant de le rendre disponible à tout le monde sur Messenger.                                                                                                                                     |
| IDs de la portée des pages (PSID)            | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages)                       | Vous devez avoir des utilisateurs PSIDs pour envoyer des messages sur Facebook Messenger. Une fois qu'un utilisateur interagit avec votre application via Messenger, Facebook créera un PSID. Ce PSID peut être envoyé à Braze comme un attribut personnalisé de chaîne.                                                                                                                                                                                      |
| Jeton d'accès à la page                      | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | Ces jetons d'accès sont similaires aux jetons d'accès des utilisateurs, sauf qu'ils fournissent la permission aux API qui lisent, écrire ou modifier les données appartenant à une page Facebook. Pour obtenir un jeton d'accès à la page, vous devez obtenir un jeton d'accès utilisateur et demander la `manage_pagespermission`. Une fois que vous avez le jeton d'accès utilisateur, vous obtenez ensuite le jeton d'accès à la page via l'API graphique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Ce qui suit montre comment mettre en place un webhook Braze Facebook Messenger. Pour ceux qui ont besoin d'aide supplémentaire pour mettre en place votre bot, un tutoriel complet sur le bot Messenger et un exemple de code peuvent être trouvés dans le dépôt [Braze GitHub](https://github.com/Appboy/appboy-fb-messenger-bot)!

### Étape 1 : Récupérez vos IDs PSID

Pour envoyer des messages sur Facebook Messenger, vous devez collecter les IDs spécifiques à la page de vos utilisateurs (PSID) pour identifier votre utilisateur et interagir avec eux de manière cohérente. Les IDP ne sont pas les mêmes que l'ID Facebook de l'utilisateur. Facebook crée cet identifiant à chaque fois que vous envoyez un message à un client ou quand un client vous envoie un message.

Les PSIDs peuvent être trouvés en utilisant l'un des différents [points d'entrée](https://developers.facebook.com/docs/messenger-platform/discovery) offres Facebook. Une fois que l'utilisateur a envoyé un message à votre application ou fait une action dans une conversation, par exemple en appuyant sur un bouton ou en envoyant un message, leur PSID sera inclus dans l'expéditeur `. d` propriété de l'événement webhook, donc votre bot peut identifier qui a pris l'action (montré ci-dessous).

```
{
  "sender":{
    "id":"<PSID>"
  },
  "destinataire":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid. 457764197618:41d102a3e1ae206a38",
    "text":"hello, world! ,
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

Chaque fois que vous envoyez un message, leur PSID sera inclus dans le destinataire `. d` propriété de la requête pour identifier qui doit recevoir le message.

### Étape 2: Envoyer à Braze en tant qu'attribut personnalisé

Une fois que vous avez la certitude que vous recevez des IDS, et partagez ceci avec vos développeurs pour envoyer les PSIDs à Braze en tant qu'attribut [personnalisé]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes). Les PSIDs sont des chaînes auxquelles on peut accéder en faisant un [appel à l'API](https://developers.facebook.com/docs/messenger-platform/reference/send-api).

### Étape 3 : Configurez votre modèle de webhook

Dans **Modèles & Média**, allez dans **Modèles de Webhook** et choisissez le **Modèle de Webhook Messenger Facebook**.

1. Indiquez un nom de modèle et ajoutez des équipes et des tags, si nécessaire.
2. Entrez votre message ou choisissez un modèle de message parmi [ceux mis à disposition par Facebook](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages). Vous pouvez également choisir votre message [type](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) ou [balise](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags).
3. Inclure le PSID comme attribut personnalisé. Cela peut être fait en utilisant le bouton bleu et blanc **+** dans le coin de la boîte **Requête**.
3. Ajoutez votre jeton d'accès à la page dans l'URL du webhook en remplaçant `FACEBOOK_PAGE_ACCESS_TOKEN` par votre jeton.

#### Prévisualisation et test de votre webhook

Avant d'envoyer votre message, testez votre webhook. Assurez-vous que votre identifiant Messenger est sauvegardé dans Braze (ou le trouver et tester en tant qu'utilisateur personnalisé), et utilisez l'aperçu pour envoyer le message de test :

!\[Envoi d'un message à vous-même\]\[60\]

Si vous recevez le message avec succès, vous pouvez configurer ses paramètres de livraison.

## Utiliser cette intégration

Une fois configuré, utilisez cette intégration pour cibler les utilisateurs de Facebook Messenger. Si vous n'envoyez pas de messages en utilisant les numéros de téléphone des utilisateurs et planifiez d'envoyer des messages de Messenger à plusieurs reprises, vous devriez [créer un segment][62] pour tous les utilisateurs pour lesquels l'ID Messenger existe en tant qu'attribut personnalisé et activer [le suivi analytique][61] pour suivre vos taux d'abonnement Messenger au fil du temps. Si vous choisissez de ne pas créer de segment spécifique pour les abonnés de Messenger, assurez-vous d'inclure un filtre pour l'identifiant Messenger existant pour éviter les erreurs :

!\[Filtre de segment pour les identifiants de messager\]\[63\]

Vous pouvez également utiliser une autre segmentation pour cibler vos campagnes Messenger, et le reste du processus de création de campagne est comme toute autre campagne.
[60]: {% image_buster /assets/img_archive/fbm-test.png %} [63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}

[61]: {{site.baseurl}}/user_guide/data_and_analytics/viewing_and_understanding_segment_data/#turning-analytics-tracking-on-and-off
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment