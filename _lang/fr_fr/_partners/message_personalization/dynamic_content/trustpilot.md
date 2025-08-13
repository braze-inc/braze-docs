---
nav_title: Trustpilot
article_title: Trustpilot
description: "Cette page explique comment intégrer Trustpilot à Braze, envoyer des invitations à commenter et personnaliser les messages avec des informations sur les produits."
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# Trustpilot

> [Trustpilot](https://www.trustpilot.com/) est une plateforme d'évaluation en ligne qui permet aux clients de partager leurs commentaires et vous permet de gérer les évaluations et d'y répondre.

Cette page fournit un guide étape par étape pour :

* Créer des invitations à participer à un examen à l'aide de l'API de création d'invitations de Trustpilot  
* Personnalisation des messages avec des avis sur les produits grâce à l'API des avis sur les produits de Trustpilot.

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis | Description |
| --- | --- |
| Un compte Trustpilot | Vous avez besoin d'un compte Trustpilot avec un accès à l'API de Trustpilot. |
| Une clé d'authentification Trustpilot | Vous devrez configurer une clé API et demander un jeton d'accès. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Intégration

### Étape 1 : Obtenez vos identifiants API Trustpilot

1. [Connectez-vous à Trustpilot](https://app.contentful.com/login) avec vos identifiants.  
2. Créez ou récupérez la clé et le secret de l'API dans le tableau de bord de Trustpilot en allant dans **Intégrations** > **Développeurs** > **API.** Si vous n'avez pas encore de clé API, créez-en une nouvelle :  
   1. Allez dans **Nom de l'application** > **Créer une application**  
   2. Copiez votre clé API et votre secret, qui seront utilisés pour authentifier vos demandes de contenu connecté.

## Envoi d'invitations à effectuer un examen sur Trustpilot

### Étape 1 : Implanter une campagne webhook Braze 

Configurez une campagne webhook Braze à Braze basée sur des actions pour déclencher les API Trustpilot afin d'envoyer des invitations d'examen par e-mail aux utilisateurs. Par exemple, vous pouvez envoyer une invitation à passer un examen après qu'un utilisateur a passé une commande avec les détails du webhook suivants :
   * [URL de webhook](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)) : `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`  
   * Méthode : POST  
   * Ajoutez les informations personnalisées sous forme de paires clé-valeur.

### Étape 2 : Récupérer le jeton d’accès

1. Utilisez le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) pour faire une demande au [endpoint d'authentification de Trustpilot](https://documentation-apidocumentation.trustpilot.com/authentication?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..) afin de récupérer le jeton d'accès.
2. Utilisez le type de subvention **client_credentials** et entrez votre clé API et votre secret dans une étiquette de contenu connecté pour récupérer un jeton. La demande de contenu connecté peut être saisie dans l'en-tête de la demande. Le contenu connecté peut se présenter comme suit :
  
{% raw %}

```liquid
{% connected_content 
https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken
:method post
:headers {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic {{'API_KEY:API_SECRET' | base64_encode}}" }
:body grant_type=client_credentials
:save token
:retry
:cache_max_age 3600 %}

{{token.access_token}}

```

{% endraw %}

{: start="3"}
3\. Ajoutez le jeton d'accès à l'en-tête de requête de votre campagne webhook.

{% alert tip %}
Reportez-vous à la [documentation de Trustpilot](https://support.trustpilot.com/hc/en-us/community/posts/11947443933074-Braze-Trustpilot-Setup-Instructions-for-triggering-API-invites) pour des instructions plus détaillées.
{% endalert %}

## Personnalisation des messages à l'aide d'informations sur les produits.

Dans votre campagne Braze, effectuez un appel de contenu connecté pour demander des données à l'[endpoint Récapitulatif des avis sur les produits de](https://developers.trustpilot.com/product-reviews-api#get-product-reviews-summary) Trustpilot ({% raw %}`https://api.trustpilot.com/v1/product-reviews/business-units/{businessUnitId}`{% endraw %}). Cette méthode permet de récupérer les avis sur les produits pour des UGS spécifiques de l'unité commerciale. L'exemple suivant spécifie l'unité de gestion des stocks spécifique au produit et filtre les avis cinq étoiles.

{% raw %}
```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}

![Contenu connecté dans l'e-mail utilisant Liquid pour attirer l'information.]({% image_buster /assets/img/trustpilot_connected_content_example.png %}){:style="max-width:38%;"}

La demande de contenu connecté renverra les avis sur les produits.

{% raw %}
```liquid
  {
   "productReviews": [
       {
           "id": "670d5810ba62e6b31de97de9",
           "createdAt": "2024-10-14T17:42:40.286Z",
           "stars": 5,
           "content": "Such a great toy truck, my kids really enjoy it! ",
           "consumer": {
               "id": "6176xxxx",
               "displayName": "Kevin Bob"
           },
           "language": "en",
           "attributeRatings": [],
           "attachments": [],
           "firstCompanyComment": null
       }
   ],
   "links": []
 ```
{% endraw %}

{: start="2"}
2\. Utilisez la syntaxe Liquid pour intégrer le contenu pertinent dans votre message. Par exemple, pour extraire le contenu de l'avis sur le produit, utilisez l'étiquette Liquid {% raw %}`{{result.productReviews[0].content}}`{% endraw %}.

![E-mail personnalisé contenant un avis sur un camion jouet que l'utilisateur a laissé dans son panier.]({% image_buster /assets/img/trustpilot_personalized_email.png %}){:style="max-width:38%;"}