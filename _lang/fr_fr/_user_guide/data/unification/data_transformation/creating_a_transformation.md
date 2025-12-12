---
nav_title: Créer une transformation
article_title: Créer une transformation
page_order: 1
page_type: reference
description: "Cet article de référence fournit des étapes pour créer une transformation à l'aide de Braze Data Transformation."
---

# Créer une transformation

> Braze Data Transformation vous permet de créer et de gérer des intégrations webhook pour automatiser le flux de données depuis des plateformes externes vers Braze. Ces intégrations webhook peuvent ensuite alimenter des cas d'utilisation marketing encore plus sophistiqués. Vous pouvez créer votre transformation de données à partir d'un code par défaut, ou en utilisant notre bibliothèque de modèles dédiée pour vous aider à démarrer avec certaines plateformes externes.

## Conditions préalables 

| Exigence | Description |
| --- | --- |
| Authentification à deux facteurs ou SSO | Vous devez avoir activé l'[authentification à deux facteurs]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) ou l'[authentification unique]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO) pour votre compte. |
| Permissions correctes | Vous devez être administrateur d'un compte ou d'un espace de travail, ou disposer des droits d'utilisateur "Gérer les transformations". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Étape 1 : Identifier une plateforme source

Identifiez une plateforme externe que vous souhaitez connecter à Braze et vérifiez que la plateforme prend en charge les webhooks. Ces paramètres sont parfois appelés "notifications API" ou "demandes de service web".

Voici un exemple de [webhook de Typeform](https://www.typeform.com/help/a/webhooks-360029573471/), qui est configurable en se connectant à leur plateforme :

\![]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Étape 2 : Créer une transformation

{% multi_lang_include create_transformation.md location="default" %}

## Étape 3 : Envoyez un webhook de test (recommandé)

Cette étape est facultative, mais nous vous recommandons d'envoyer un webhook de test depuis votre plateforme source vers votre transformation nouvellement créée.

1. Copiez l'URL de votre transformation.
2. Dans votre plateforme source, trouvez une capacité "Envoyer un test" pour qu'elle génère un exemple de webhook à envoyer à cette URL. 
- Si votre plate-forme source vous demande un type de requête, sélectionnez **POST.**
- Si votre plateforme source propose des options d'authentification, sélectionnez **Pas d'authentification**.
- Si votre plateforme source demande des secrets, sélectionnez **Pas de secrets.**
3. Actualisez votre page dans le tableau de bord de Braze pour voir si le webhook a été reçu. S'il a été reçu, vous devriez voir un webhook payload sous **Most recent webhook**.

Voici à quoi cela ressemble pour Typeform :

Exemple de code de transformation des données qui mappe le webhook aux profils utilisateurs de Braze.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Il se peut que Braze Data Transformation ne prenne pas encore en charge les plateformes externes qui exigent une vérification ou une authentification spéciale pour les webhooks. Pensez à laisser un [commentaire sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) si vous souhaitez utiliser ce type de plateforme avec Braze Data Transformation.
{% endalert %}

## Étape 4 : Écrire le code de transformation

Si vous avez peu ou pas d'expérience avec le code JavaScript ou si vous préférez des instructions plus détaillées, suivez les instructions de **Beginner - POST : Suivre les utilisateurs** ou **Débutant - PUT : Mise à jour de plusieurs éléments du catalogue** onglet pour l'écriture de votre code de transformation.

Si vous êtes développeur ou si vous avez une expérience significative du code JavaScript, suivez les instructions de **Advanced - POST : Suivez les utilisateurs** onglet pour des instructions de haut niveau sur l'écriture de votre code de transformation.

{% alert tip %}
Braze Data Transformation dispose d'un copilote d'intelligence artificielle qui demande à ChatGPT de vous aider à écrire votre code. Pour accéder au copilote d'intelligence artificielle, sélectionnez <i class="fa-solid fa-wand-magic-sparkles"></i> **Generate transformation code.** Pour l'utiliser, un webhook doit être envoyé à votre transformation. Vous pouvez également accéder à la bibliothèque de modèles en sélectionnant **Insérer un code** > **Insérer un modèle**.

\![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Beginner - Track users %}

Ici, écrivez le code de transformation pour définir comment mapper diverses valeurs de webhook à des profils utilisateurs Braze.

1. Les nouvelles transformations ont ce modèle par défaut dans la section **Code de transformation :** 

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. Pour inclure des attributs personnalisés, des événements personnalisés et des achats dans vos appels de transformation, passez à l'étape 3. Sinon, supprimez les sections dont vous n'avez pas besoin.<br><br>
3\. Chaque attribut, événement et objet d'achat nécessite un identifiant utilisateur, soit `external_id`, `user_alias`, `braze_id`, `email`, ou `phone`. Trouvez l'identifiant de l'utilisateur dans le payload du webhook entrant, et intégrez cette valeur dans votre code de transformation via une ligne de payload. Utilisez la notation point pour accéder aux propriétés de l'objet de la charge utile. <br><br>
4\. Trouvez les valeurs du webhook que vous souhaitez conseiller en tant qu'attributs, événements ou achats, et intégrez ces valeurs dans votre code de transformation par le biais d'une ligne de charge utile. Utilisez la notation point pour accéder aux propriétés de l'objet de la charge utile.<br><br>
5\. Pour chaque attribut, événement et objet d'achat, examinez la valeur `_update_existing_only`. Définissez cette valeur sur `false` si vous souhaitez que la transformation crée un nouvel utilisateur qui n'existe peut-être pas. Laissez cette option sur `true` pour ne mettre à jour que les profils existants.<br><br>
6\. Cliquez sur **Valider** pour obtenir un aperçu de la sortie de votre code et vérifier s'il s'agit d'une demande `/users/track` acceptable.<br><br>
7\. Activez votre transformation. Pour obtenir une aide supplémentaire concernant votre code avant de l'activer, contactez votre gestionnaire de compte Braze.<br><br>
7\. Demandez à votre plateforme source de commencer à envoyer des webhooks. Votre code de transformation s'exécutera pour chaque webhook entrant, et les profils utilisateurs commenceront à se mettre à jour. 

L'intégration de votre webhook est maintenant terminée !

{% endtab %}
{% tab Beginner - Update catalog items %}

Ici, vous pouvez écrire un code de transformation pour définir comment vous souhaitez mapper différentes valeurs de webhook à des mises à jour d'éléments du catalogue Braze.

1. Les nouvelles transformations incluront ce modèle par défaut dans la section **Code de transformation :** 

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",
  
  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. Les transformations pour les destinations `/catalogs` nécessitent une `catalog_name` pour définir le catalogue spécifique à mettre à jour. Vous pouvez coder ce champ en dur ou le modeler avec un champ webhook via une ligne de payload. Utilisez la notation point pour accéder aux propriétés de l'objet de la charge utile.<br><br>
3\. Définissez les éléments que vous souhaitez mettre à jour dans le catalogue à l'aide des champs `id` dans le tableau des éléments. Vous pouvez coder ces champs en dur ou les insérer dans un champ de webhook via une ligne de payload. <br><br> N'oubliez pas que `catalog_column` est une valeur marque substitutive. Assurez-vous que les objets d'articles ne contiennent que des champs qui existent dans le catalogue.<br><br>
4\. Sélectionnez **Valider** pour obtenir un aperçu du résultat de votre code et vérifier s'il s'agit d'une demande acceptable pour le [point de terminaison Mettre à jour plusieurs éléments du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items).<br><br>
5\. Activez votre transformation. Pour obtenir une aide supplémentaire concernant votre code avant de l'activer, contactez votre gestionnaire de compte Braze.<br><br>
6\. Veillez à vérifier si votre plateforme source dispose d'un paramètre permettant de lancer l'envoi de webhooks. Votre code de transformation s'exécutera pour chaque webhook entrant, et les éléments du catalogue commenceront à être mis à jour.

L'intégration de votre webhook est maintenant terminée !

{% endtab %}
{% tab Advanced - Track users %}

Dans cette étape, vous transformerez la charge utile du webhook de la plateforme source en une valeur de retour d'un objet JavaScript. Cette valeur de retour doit respecter le format du corps de la requête de l'endpoint `/users/track`:

- Le code de transformation est accepté dans le langage de programmation JavaScript. Tout flux de contrôle JavaScript standard, tel que la logique if/else, est pris en charge.
- Le code de transformation accède au corps de la demande de webhook via la variable `payload`. Cette variable est un objet rempli en analysant le JSON du corps de la demande.
- Toutes les fonctionnalités prises en charge dans notre endpoint `/users/track` sont prises en charge, y compris :
  - Objets d'attributs utilisateur, objets d'événements et objets d'achat
  - Attributs et propriétés d'événements personnalisés imbriqués
  - Mise à jour des groupes d'abonnement
  - L'adresse e-mail comme identifiant

Sélectionnez **Valider** pour obtenir un aperçu du résultat de votre code et vérifier s'il s'agit d'une demande `/users/track` acceptable.

{% alert note %}
Les requêtes réseau externes, les bibliothèques tierces et les webhooks non JSON ne sont actuellement pas pris en charge.
{% endalert %}

{% endtab %}
{% endtabs %}

## Étape 5 : Suivez votre transformation

Après avoir activé votre transformation, consultez les analyses sur la page principale des **transformations** pour obtenir un résumé des performances.

* **Demandes entrantes :** Il s'agit du nombre de webhooks reçus à l'URL de cette transformation. Si le nombre de demandes entrantes est égal à 0, cela signifie que votre plateforme source n'a envoyé aucun webhook ou que la connexion ne peut pas être établie.
* **Réceptions/distributions :** Après avoir reçu les demandes entrantes, la transformation des données applique votre code de transformation pour l'envoyer à la destination de Braze que vous avez sélectionnée.

Il est souhaitable que 100 % des demandes entrantes aboutissent à une réception/distribution. Le nombre de réception/distribution ne dépassera jamais le nombre de demandes entrantes.

### Résolution des problèmes

Pour une surveillance et une résolution des problèmes plus détaillées, consultez la page **Journaux** pour des journaux spécifiques, où sont consignées les 1 000 dernières demandes entrantes adressées à toutes les transformations de vos espaces de travail. Vous pouvez sélectionner chaque journal pour afficher le corps de la requête entrante, la sortie de la transformation et le corps de la réponse de la destination de la transformation.

S'il n'y a pas de réception/distribution, vérifiez que votre code de transformation ne contient pas d'erreurs de syntaxe et confirmez que le code se compile. Vérifiez ensuite si la sortie est une demande de destination valide.

Une réception/distribution inférieure au nombre de demandes entrantes indique qu'au moins certains webhooks sont délivrés avec succès. Consultez les journaux de transformation pour trouver des exemples d'erreurs et vérifiez si la sortie de la transformation est conforme aux attentes. Il est possible que votre code de transformation ne prenne pas en compte toutes les variations des webhooks reçus.


