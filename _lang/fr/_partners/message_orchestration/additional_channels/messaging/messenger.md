---
nav_title: Messenger
article_title: Facebook Messenger
alias: /partners/messenger/
description: "Cet article présente le partenariat entre Braze et Facebook Messenger, l’une des plateformes de messagerie instantanée les plus populaires au monde."
page_type: partner
search_tag: Partenaire

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) est l’une des plateformes de messagerie instantanée les plus populaires au monde, utilisée par environ un milliard d’utilisateurs actifs par mois. Grâce à cette plateforme, les marques peuvent créer des chatbots engageant les interactions intelligentes et automatiques avec leurs clients.

L’intégration de Braze et Facebook exploite les webhooks de Braze, la segmentation avancée, la personnalisation et les fonctionnalités de déclenchement pour envoyer des messages à vos utilisateurs dans Facebook Messenger par le biais de l’API de la plateforme Messenger. Un modèle de webhook Facebook Messenger personnalisé est inclus dans notre plateforme sous **Templates & Media (Modèles et médias)**.

La plateforme Facebook Messenger est destinée aux « messages non promotionnels qui facilitent une transaction préexistante, fournissent d’autres actions de support client ou fournissent du contenu demandé par une personne. » Pour en savoir plus, voir les [directives de la plateforme Facebook](https://developers.facebook.com/docs/messenger-platform) et les [exemples de cas d’utilisation acceptables](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Conditions préalables

Acceptez les conditions suivantes avant de poursuivre avec l’intégration :
- Facebook ne permet pas l’utilisation de la plateforme Messenger pour envoyer des messages marketing. 
- Vous aurez besoin de l’autorisation explicite de l’utilisateur pour les messages depuis votre page. 
- Pour envoyer des messages aux utilisateurs qui ne sont pas des utilisateurs de test de votre application Facebook, votre application devra passer l’[examen de l’application](https://developers.facebook.com/docs/messenger-platform/app-review) de Facebook.<br><br>

| Condition| Origine| Accès| Description|
| ---| ---| ---|
| Page Facebook Messenger| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Une page Facebook sera utilisée comme l’identité de votre bot. Lorsque les gens discutent avec votre application, ils verront le nom de la page et l’image du profil.|
| Application Facebook Messenger| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | L’application Facebook contient les paramètres de votre bot Messenger, y compris les jetons d’accès.
| Examen et approbation du bot de l’application | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | Lorsque vous êtes prêt à publier votre bot au public, vous devez le soumettre à Facebook pour examen et approbation. Ce processus d’examen nous permet de garantir que votre bot Messenger respecte nos politiques et fonctions comme prévu avant de le mettre à disposition de tous sur Messenger. |
| ID de la page (PSID) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Les ID PSID des utilisateurs doivent envoyer des messages sur Facebook Messenger. Une fois qu’un utilisateur interagit avec votre application via Messenger, Facebook crée un PSID. Ce PSID peut être envoyé à Braze comme attribut personnalisé de chaîne de caractères.
| Jeton d’accès à la page | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | Ces jetons d’accès sont similaires aux jetons d’accès utilisateur, sauf qu’ils donnent l’autorisation aux API qui lisent, écrivent ou modifient les données appartenant à une page Facebook. Pour obtenir un jeton d’accès à la page, vous devez obtenir un jeton d’accès utilisateur et demander le `manage_pagespermission`. Une fois que vous avez le jeton d’accès utilisateur, vous obtenez alors le jeton d’accès de la page via l’API Graph.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Voici comment configurer un webhook Braze Facebook Messenger. 
Pour ceux qui ont besoin d’aide supplémentaire pour configurer le bot, un didacticiel de bot Messenger complet et un exemple de code sont disponibles dans le [référentiel GitHub de Braze](https://github.com/Appboy/appboy-fb-messenger-bot) !

### Étape 1 : Collecter vos PSID

Pour envoyer des messages dans Facebook Messenger, vous devez collecter les ID de page (PSID) de vos utilisateurs pour les identifier et interagir avec eux de manière cohérente. Les PSID ne sont pas les ID Facebook de l’utilisateur. Facebook crée cet identifiant à chaque fois que vous envoyez un message à un client ou lorsque celui-ci vous envoie un message.

Les PSID sont disponibles en utilisant l’un des différents [points d’entrée](https://developers.facebook.com/docs/messenger-platform/discovery) proposés par Facebook. Lorsque l’utilisateur envoie un message à votre application ou qu’il entreprend une action dans une conversation, comme taper un bouton ou envoyer un message, son PSID sera inclus dans le `sender.id` de l’événement webhook, afin que votre bot puisse identifier l’auteur de l’action.

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

Chaque fois que vous envoyez un message, leur PSID sera inclus dans la propriété `recipient.id` de la demande pour identifier la personne qui doit recevoir le message.

### Étape 2 : Envoyer les PSID à Braze en tant qu’attributs personnalisés

Une fois que vous êtes sûr de recevoir les PSID, coordonnez et partagez-les avec vos développeurs pour envoyer les PSID à Braze en tant qu’[attributs personnalisés]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes). Les PSID sont des chaînes de caractères accessibles via un [appel API](https://developers.facebook.com/docs/messenger-platform/reference/send-api).

### Étape 3 : Configurer votre modèle de webhook

Dans **Templates & Media (Modèles et médias)**, accédez à **Webhook Templates (Modèles de webhook)** et sélectionnez le modèle de webhook **Facebook Messenger**.

1. Fournissez un nom de modèle et ajoutez des équipes et des balises, si nécessaire.
2. Saisissez votre message ou choisissez un modèle de message à partir de [ceux mis à disposition par Facebook](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages). Vous pouvez également choisir le [type](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) ou la [balise](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags) de votre message.
3. Incluez le PSID en tant qu’attribut personnalisé. Pour cela, utilisez le bouton **+** bleu et blanc dans le coin de la zone **Request Body (Corps de la demande)**.
3. Ajoutez votre jeton d’accès à la page dans l’URL du webhook en remplaçant `FACEBOOK_PAGE_ACCESS_TOKEN` avec votre jeton.

#### Prévisualisation et test de votre webhook

Avant d’envoyer votre message, testez votre webhook. Assurez-vous que votre ID de Messenger est enregistré dans Braze (ou trouvez-le et testez-le en tant qu’utilisateur personnalisé), et utilisez l’aperçu pour envoyer le message de test :

![Onglet Test du modèle de webhook de Facebook Messenger qui affiche l’aperçu du message en l’envoyant à un utilisateur existant.][60]

Si vous recevez le message avec succès, vous pouvez configurer les paramètres de livraison.

## Comment utiliser cette intégration

Une fois configurée, utilisez cette intégration pour cibler les utilisateurs Facebook Messenger. Si vous n’envoyez pas de messages à l’aide des numéros de téléphone des utilisateurs et prévoyez d’envoyer des messages Messenger à plusieurs reprises, vous devez [créer un segment][62] pour tous les utilisateurs pour lesquels l’ID Messenger existe comme attribut personnalisé et activer le[suivi analytique][61] pour suivre vos tarifs d’abonnement Messenger au fil du temps. 

![Filtre de segment « messenger_id » défini sur « n’est pas vide ».][63]

Si vous choisissez de ne pas créer un segment spécifique pour les abonnés de Messenger, assurez-vous d’inclure un filtre pour les ID Messenger existants pour éviter les erreurs.

Vous pouvez également utiliser d’autres segmentations pour cibler vos campagnes sur Messenger et le reste du processus de création de campagne, comme c’est le cas avec toute autre campagne.

[60]: {% image_buster /assets/img_archive/fbm-test.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/viewing_and_understanding_segment_data/#turning-analytics-tracking-on-and-off
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}