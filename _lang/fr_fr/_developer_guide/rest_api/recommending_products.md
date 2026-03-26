---
nav_title: Recommander des produits aux utilisateurs
article_title: Recommander des produits aux utilisateurs
page_order: 4
page_type: reference
description: "Cet article de référence explique comment utiliser l'API REST de Braze, les catalogues et le contenu connecté pour recommander des produits aux utilisateurs sur différents canaux de communication."
---

# Recommander des produits aux utilisateurs

> Utilisez l'API REST de Braze avec les [catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) ou le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) pour afficher des recommandations produit personnalisées dans vos messages. Cette approche vous permet de connecter votre propre moteur de recommandation à l'écosystème d'envoi de messages de Braze, afin que les utilisateurs non techniques puissent gérer le contenu et les messages associés à chaque recommandation.

Avec cette approche, vous pouvez :

- Stocker des recommandations produit sur les profils utilisateur depuis votre backend à l'aide de l'API REST.
- Récupérer les métadonnées produit au moment de l'envoi grâce aux catalogues ou au contenu connecté.
- Afficher des recommandations personnalisées sur n'importe quel canal de communication, y compris l'e-mail, les notifications push, les messages in-app, et bien plus.

## Conditions préalables

Pour suivre ce guide, vous aurez besoin de :

| Condition | Description |
| --- | --- |
| Clé API REST de Braze | Une clé disposant de l'autorisation `users.track` et, si vous gérez les catalogues via l'API, des autorisations de catalogues correspondantes. Pour en créer une, accédez à **Paramètres** > **Clés API**. |
| Catalogue Braze | Un catalogue contenant les métadonnées de vos produits (nom, catégorie, prix, URL de l'image, etc.). Pour en créer un, consultez [Créer un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create/). |
| Connaissances en Liquid | Une familiarité intermédiaire avec [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) pour créer des modèles avec des variables personnalisées et utiliser le contenu connecté. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 1 : Stocker les recommandations sur les profils utilisateur

Pour commencer, stockez les recommandations produit générées par votre moteur de recommandation sur les profils utilisateur de Braze sous forme d'attributs personnalisés. Cela vous permet de référencer les produits recommandés de chaque utilisateur au moment de l'envoi du message.

1. Déterminez quelles données de recommandation stocker, comme les ID produit ou les catégories préférées.
2. Utilisez l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour écrire la recommandation en tant qu'attribut personnalisé sur le profil utilisateur.

### Exemple de requête

```http
POST YOUR_REST_ENDPOINT/users/track
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Remplacez `YOUR_REST_ENDPOINT` par l'[URL de l'endpoint REST]({{site.baseurl}}/api/basics/#endpoints) de votre espace de travail.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "recommended_product_id": "1001"
    }
  ]
}
```

Utilisez des noms d'attributs explicites (comme `recommended_product_id`) pour faciliter leur référencement dans les modèles Liquid par la suite. Maintenez vos recommandations à jour en les actualisant régulièrement à mesure que votre moteur de recommandation produit de nouveaux résultats.

## Étape 2 : Récupérer les métadonnées produit

Après avoir stocké un identifiant de recommandation sur chaque profil utilisateur, vous devez récupérer les métadonnées complètes du produit (nom, prix, image, etc.) pour les inclure dans votre message. Deux options s'offrent à vous :

- **Option A :** [Catalogues Braze](#option-a-braze-catalogs) — stockez les informations produit directement dans Braze pour des recherches rapides et intégrées.
- **Option B :** [Contenu connecté](#option-b-connected-content) — récupérez les informations produit depuis une API externe au moment de l'envoi.

### Option A : Catalogues Braze

Si vous avez créé un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) avec votre inventaire de produits, vous pouvez rechercher des articles directement dans votre message à l'aide de Liquid. Pour un guide complet, consultez [Utiliser les catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/use/).

#### Recommander un article spécifique du catalogue

{% raw %}
Pour référencer un produit spécifique par son ID, utilisez l'étiquette Liquid `catalog_items`. Par exemple, pour recommander le produit `1001` d'un catalogue nommé `retail_products` :

```liquid
{% catalog_items retail_products 1001 %}

We have a new item we think you'll like:
Category: {{ items[0].category }}
Name: {{ items[0].name }}
Price: ${{ items[0].price }}
```
{% endraw %}

#### Recommander plusieurs articles du catalogue

{% raw %}
Vous pouvez également référencer plusieurs articles dans une seule étiquette. Par exemple, pour mettre en avant trois produits :

```liquid
{% catalog_items retail_products 1001 1003 1005 %}

New items added in:
- {{ items[0].category }}
- {{ items[1].category }}
- {{ items[2].category }}

Visit our store to learn more!
```
{% endraw %}

#### Créer un modèle d'articles à partir de la recommandation d'un utilisateur

{% raw %}
Combinez l'attribut personnalisé de l'[Étape 1](#step-1-store-recommendations-on-user-profiles) avec une recherche dans le catalogue pour personnaliser la recommandation pour chaque utilisateur :

```liquid
{% catalog_items retail_products {{custom_attribute.${recommended_product_id}}} %}

Hi {{${first_name}}}, check out our pick for you:
{{ items[0].name }} — ${{ items[0].price }}
```
{% endraw %}

### Option B : Contenu connecté

Si les métadonnées de vos produits se trouvent dans un service externe plutôt que dans un catalogue Braze, utilisez le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) pour les récupérer au moment de l'envoi.

{% raw %}
Par exemple, si votre API interne renvoie les détails d'un produit par son ID :

```liquid
{% connected_content https://api.yourcompany.com/products/{{custom_attribute.${recommended_product_id}}} :save product %}

Hi {{${first_name}}}, we think you'll love:
{{ product.name }} — ${{ product.price }}
```
{% endraw %}

Pour en savoir plus sur les appels API depuis vos messages, consultez [Effectuer un appel API]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/).

{% alert warning %}
Évitez d'utiliser le contenu connecté pour récupérer une longue liste de produits, puis d'itérer sur cette liste en Liquid au moment de l'envoi. Des PAYLOAD volumineux augmentent la latence d'envoi et peuvent provoquer des délais d'attente ou des échecs de distribution à grande échelle. Stockez plutôt uniquement les ID produit spécifiques dont un utilisateur a besoin sur son profil (voir [Étape 1](#step-1-store-recommendations-on-user-profiles)), et récupérez les métadonnées de ces articles individuels ou utilisez les [catalogues](#option-a-braze-catalogs), qui sont optimisés pour des recherches rapides.
{% endalert %}

## Étape 3 : Vérifier votre intégration

Une fois la configuration terminée, vérifiez votre intégration :

1. Utilisez l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour écrire une recommandation de test sur votre propre profil utilisateur.
2. Envoyez un message de test qui référence le produit recommandé en utilisant les catalogues ou le contenu connecté.
3. Confirmez que les détails du produit s'affichent correctement dans le message reçu.
4. Dans le tableau de bord de Braze, accédez à la page de résultats de la campagne ou du Canvas et vérifiez que l'envoi est bien enregistré.

## Points à prendre en compte

- Maintenez vos données de recommandation à jour en actualisant régulièrement les attributs personnalisés à mesure que votre moteur de recommandation produit de nouveaux résultats.
- Utilisez les [fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) de Braze pour affiner davantage vos messages, par exemple en intégrant des données spécifiques à l'utilisateur aux détails du produit.
- Envisagez d'utiliser la [distribution déclenchée par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) pour déclencher des messages depuis votre backend à l'aide de modèles définis dans le tableau de bord de Braze.