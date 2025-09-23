---
nav_title: Contentful
article_title: Contentful
description: "Cet article de référence présente le partenariat entre Braze et Contentful, un système de gestion de contenu qui vous permet d'utiliser dynamiquement le contenu connecté pour tirer du contenu de Contentful dans vos campagnes Braze."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contentful

>[Contentful](https://www.contentful.com/) est un système de gestion de contenu sans tête qui vous permet de créer, gérer et distribuer du contenu sur n'importe quelle plateforme. Contrairement à un système de gestion de contenu (CMS), Contentful vous permet de créer votre modèle de contenu afin que vous puissiez décider du contenu que vous souhaitez gérer.<br><br>Cette page fournit un guide étape par étape pour configurer Braze contenu connecté afin de récupérer des données à partir de l'API de réception/distribution de contenu de Contentful. 

Une fois que vous êtes intégré, vous pouvez utiliser les API RESTful de Contentful pour diffuser votre contenu sur plusieurs canaux, tels que les sites web, les applications mobiles (iOS, Android et Windows) ou de nombreuses autres plateformes. Vous pouvez également extraire dynamiquement du contenu de Contentful pour l'utiliser dans vos campagnes Braze.

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis          | Description                        |
|-----------------------|------------------------------------|
| A Contentful débiteur | Vous devez disposer d'un compte Contentful avec accès à l'API de réception/distribution de contenu. |
| Un compte Braze | Vous devez disposer d'un compte Braze avec accès à la fonctionnalité Contenu connecté. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Obtenez vos identifiants API Contentful

1. [Connectez-vous à Contentful](https://app.contentful.com/login) avec vos identifiants.
2. Créez ou récupérez les jetons d'accès à l'API dans le tableau de bord de Contentful en allant dans **Paramètres** > **Clés API**. Si vous n'avez pas encore de clé API, créez-en une nouvelle :<br>2.1 Sélectionnez **Ajouter une clé API**.<br>2.2 Saisissez les informations requises et sélectionnez l'environnement approprié.<br>2.3 Sélectionnez **Enregistrer** et notez l'**ID de l'espace** et le **jeton d'accès à l'API de distribution de contenu**.
3. Identifiez le modèle de contenu auquel vous souhaitez accéder via l'API Contentful.

### Étape 2 : Configurer le contenu connecté de Braze

1. [Connectez-vous à Braze](https://dashboard.braze.com/sign_in) avec vos identifiants.
2. Dans le tableau de bord de Braze, allez dans **Modèles** > **Blocs de contenu** > **Créer un bloc de contenu** > **Bloc de contenu HTML**.
3. Créez une demande de contenu connecté à l'[URL de l'API de distribution de contenu de Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links). Un exemple d'URL de Contentful Content Delivery API est ```https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries```.<br><br> L'extraction de différentes ressources nécessite l'inclusion de variables spécifiques. L'exemple de demande d'URL de contenu connecté cible l'endpoint [Entry](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console) de Contentful. Cet endpoint a besoin de variables telles que `{space_id}` et `{environment_id}`, ou `{entry_id}` et `{access_token}`. Celles-ci peuvent être extraites de votre instance Contentful. Dans cet exemple de bloc de contenu, les variables doivent être remplacées par votre ID d'espace Contentful et votre ID d'environnement.<br><br>L'exemple d'URL de l'API de distribution de contenu n'utilise qu'un seul des endpoints disponibles de Contentful. Différents cas d'utilisation peuvent être réalisés en utilisant différents URL. Par exemple, l'[API Image](https://www.contentful.com/developers/docs/references/images-api/) peut être utilisée pour capturer des images stockées dans Contentful. Pour plus d'informations, consultez l'[API de réception/distribution de contenu](https://www.contentful.com/developers/docs/references/content-delivery-api/).

{% alert note %}
Différents endpoints peuvent nécessiter de nouvelles variables, par exemple l'API Images nécessite les variables `{asset_id}`, `{unique_id},` et `{name}`. Pour plus d'informations, contactez Contentful.
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4\. Utilisez "Test Endpoint" pour tester que Braze peut se connecter avec succès à l'API Contentful et récupérer les données souhaitées.
5\. Sélectionnez **Done** pour enregistrer votre bloc de contenu.
6\. Donnez à votre bloc de contenu un nom descriptif, tel que "Contentful API", puis sélectionnez **Lancer le bloc de contenu**.

### Étape 3 : Utilisez le contenu connecté dans les campagnes et les canevas

1. Dans Braze, créez une nouvelle campagne ou modifiez une campagne existante.
2. Utilisez le bloc de contenu connecté pour insérer des données extraites de Contentful. Utilisez les chemins de données que vous avez définis lors de la configuration pour alimenter dynamiquement le contenu de la campagne.<br><br>
- **Chemin de réponse :** Après avoir inclus le bloc de contenu dans une campagne ou un canvas Braze, la réponse devient disponible lorsque vous insérez la variable `{response}` dans votre message.<br><br>La notation JSON par points vous permet de spécifier quelle partie du corps de la réponse de Contentful vous souhaitez inclure dans votre message. Cela variera en fonction de votre cas d'utilisation. Par exemple, vous pouvez utiliser la valeur de titre ({% raw %}```liquid{{response.items[0].fields.title}}```{% endraw %}) de l'endpoint Entry de Contentful et recevoir une réponse comme celle-ci :

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3\. Prévisualisez et testez votre campagne pour confirmer que les données du contenu connecté s'affichent correctement.
4\. Une fois que vous êtes satisfait de la configuration, lancez votre campagne.

## Résolution des problèmes

### Réponse de l'API

Assurez-vous que vos identifiants API Contentful et l'URL de votre endpoint sont corrects. Vérifiez l'existence d'éventuels messages d'erreur dans Braze qui pourraient indiquer des problèmes avec l'appel API.

### Mappage des données

Vérifiez que les mappages des chemins de réponse sont correctement configurés et que la structure de la réponse de l'API correspond à vos attentes.

## Ressources complémentaires

- [Documentation de l'API de réception/distribution de contenu Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Contenu connecté de Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
- [Blocs de contenu Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
