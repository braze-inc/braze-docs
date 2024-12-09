---
nav_title: Fresh Relevance
article_title: Fresh Relevance
description: "Cet article de référence présente le partenariat entre Braze et Fresh Relevance, une plateforme de personnalisation polyvalente qui vous permet d'inclure des produits pertinents dans vos campagnes et Canevas Braze."
alias: /partners/fresh_relevance/
page_type: partner
search_tag: Partner

---

# Fresh Relevance

> [Fresh Relevance][1] est une solution de personnalisation polyvalente qui permet aux entreprises axées sur le commerce de créer facilement des expériences cross-canal personnalisées. Cette plateforme vous fait gagner du temps, s'intègre à votre pile technologique et vous donne les moyens d'offrir des expériences clients personnalisées propices à la conversion sur votre site web, votre application, vos e-mails, vos SMS et vos publicités, sans dépendre de votre équipe informatique.

L'intégration de Braze et de Fresh Relevance vous permet de :
* Envoyez des campagnes d'e-mail déclenchées avancées, telles que des messages de baisse de prix, de retour en stock, de navigation en plusieurs étapes ou d'abandon de panier.
* Incluez du contenu personnalisé dans les e-mails déclenchés, comme des recommandations de produits basées sur le produit parcouru par le client ou sur des articles de la même catégorie.
* Personnalisez les campagnes d'e-mails groupés avec des recommandations basées sur l'intelligence artificielle, des comptes à rebours, des prévisions météorologiques en temps réel, des flux de réseaux sociaux, et bien plus encore.
* Développez la base de données d'e-mails grâce à de nouveaux contacts collectés par le biais de pop-ups de capture de données.
* Identifiez les visiteurs du site web qui arrivent à partir d'un lien d'e-mail de Braze.

## Conditions préalables

| Condition | Description |
|-------------| ----------- |
| Compte Fresh Relevance  | Un compte Fresh Relevance est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec des autorisations suffisantes pour les endpoints énumérés ci-dessous. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][3] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| ID de la campagne Braze | La campagne Braze par défaut que vous souhaitez utiliser pour envoyer des e-mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Pour configurer l'intégration dans Fresh Relevance, vous devez créer un canal de Braze dans **Chaînes de messages** et utiliser le canal dans les déclencheurs ou contenus Fresh Relevance appropriés, selon les besoins. 

Pour obtenir des instructions étape par étape, connectez-vous à Fresh Relevance et suivez la [documentation][2].

Le système Fresh Relevance communiquera avec Braze à l'aide de la clé API fournie. Une intégration complète fait appel aux endpoints suivants de l'API Braze :

* [`/users/alias/new`][4]
* [`/users/track`][5]
* [`/campaigns/triggers/send`][6]
* [`/users/export/ids`][7]
* [`/subscription/status/get`][8]
* [`/v2/subscription/status/set`][9]

[1]: https://www.freshrelevance.com/
[2]: https://admin.freshrelevance.com/help/esp_instructions/?esp_class_name=EspBraze
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[5]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[6]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[7]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/