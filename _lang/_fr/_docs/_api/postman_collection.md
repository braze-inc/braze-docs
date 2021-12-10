---
nav_title: Postman & Exemples de demandes
article_title: Postman & Exemples de demandes
page_order: 3
description: "Cet article de référence couvre la collection Braze Postman, ce qu'elle est, comment configurer et utiliser la collection, ainsi que comment éditer et envoyer des requêtes."
page_type: Référence
---

# Postman et exemples de requêtes API

> Braze vous permet de générer des exemples de requêtes API pour tous nos points de terminaison via notre collection Postman. Cet article de référence couvre la collection Braze Postman, ce qu'elle est, comment configurer et utiliser la collection, ainsi que comment éditer et envoyer des requêtes.

## Qu'est-ce que Postman ?

Postman est un outil d'édition visuelle gratuit pour construire et tester les requêtes API. Contrairement aux autres méthodes d'interaction avec les APIs (par ex. en utilisant cURL), Postman vous permet d'éditer facilement les requêtes API, de voir les informations d'en-tête et bien plus encore. Postman a la possibilité d'enregistrer des collections ou des bibliothèques d'exemples de requêtes pré-faites de l'API. Pour faciliter la mise en œuvre de nos clients avec notre API REST, nous avons créé une collection avec des exemples préfabriqués pour tous nos terminaux API.

Vous pouvez voir ou [télécharger notre collection Postman ici.](https://www.getpostman.com/collections/29baa41d7ba930673ef0)

## Utilisation de la collection Postman de Braze

Si vous avez un compte Postman (vous pouvez télécharger les versions macOS, Windows et Linux [à partir du site Web de Postman][1]), vous pouvez ouvrir notre documentation Postman dans votre propre application Postman (cliquez sur le bouton orange **Exécuter dans Postman** ci-dessous). Vous pouvez alors [créer un environnement](#setting-up-your-postman-environment), ou utiliser notre environnement API Braze REST comme modèle, et modifiez les requêtes disponibles `POST` et `GET` pour répondre à vos propres besoins.

[![Exécuter dans Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/29baa41d7ba930673ef0?action=collection%2Fimport)

### Mise en place de votre environnement Postman

{% raw %}
La collection Braze Postman utilise une variable de template, `{{instance_url}}`, pour remplacer l'URL de l'API REST de votre instance Braze dans les requêtes pré-construites, et la variable `{{api_key}}` de votre clé API. Plutôt que d'avoir à modifier manuellement toutes les requêtes de la Collection, vous pouvez configurer cette variable dans votre environnement Postman. Vous pouvez soit sélectionner notre environnement modèle (Braze REST API Environment Template) dans la liste déroulante et remplacer les valeurs de la variable par les vôtres, ou vous pouvez configurer votre propre environnement.
{% endraw %}

Pour configurer votre propre environnement, effectuez les étapes suivantes :

1. Dans l'onglet **Espaces de travail** , sélectionnez **Environnements**.
2. Cliquez sur le bouton **+** + pour créer un nouvel environnement.
3. Donnez un nom à cet environnement (par ex. "Braze API Requests") et ajoutez des clés pour `instance_url` et `api_key` avec des valeurs correspondant à [votre instance Braze][7] et [la clé d'API Braze REST][8], comme illustré ci-dessous.
4. Cliquez sur **Enregistrer**.

{% alert note %}
Dans `POST` corps de requête, il faut encapsuler la `api_key` entre guillemets : `"MY-API-KEY-EXAMPLE"`. Dans `GET` URLs, il ne devrait pas l'être. Nous avons déjà fourni ce formatage pour vous dans les corps de la requête `POST` de cette documentation, `OBTENEZ` URLs, et modèle d'environnement pour `VOTRE API-KEY-ICI`.
{% endalert %}

!\[Ajout de variables d'environnement\]\[3\]

### Utilisation des requêtes pré-construites de la collection

Une fois que vous avez configuré votre environnement. Vous pouvez utiliser n'importe quelle requête pré-construite dans la collection comme modèle pour construire de nouvelles requêtes API. Pour commencer à utiliser une des requêtes pré-construites, cliquez dessus dans le menu **Collections** sur le côté gauche de Postman. Cela ouvrira la requête sous la forme d'un nouvel onglet dans la fenêtre principale de l'application Postman.

En général, il y a deux types de requêtes que les terminaux de l'API de Braze acceptent - `GET` et `POST`. Selon la méthode `HTTP` que le point de terminaison utilise, vous devrez modifier la requête pré-construite différemment.

#### Modifier une requête POST

Lors de l'édition d'une requête `POST` , ouvrez la requête et accédez à la section **Corps** de l'éditeur de requête. Pour être lisible, sélectionnez le bouton radio **brut** pour formater le corps de la requête `JSON`.

!\[Modifier une requête POST\]\[4\]

#### Modifier une demande GET

Lors de l'édition d'une requête `GET` , modifiez les paramètres passés dans l'URL de la requête. Pour ce faire, sélectionnez l'onglet **Params** et modifiez les paires clé-valeur dans les champs qui apparaîtront.

!\[Modifier une demande GET\]\[5\]

### Envoyer votre demande

Une fois que votre requête API est prête, cliquez sur **Envoyer**. La requête envoie et les données de réponse se remplissent dans une section sous l'éditeur de requête. À partir d'ici, vous pouvez voir les données brutes retournées par l'API de Braze, voir le code de réponse HTTP, voir combien de temps la requête a pris pour traiter, et afficher les informations d'en-tête.

!\[Données de réponse\]\[6\]
[3]: {% image_buster /assets/img_archive/postman_variable.png %} [4]: {% image_buster /assets/img_archive/postman_post. ng %} [5]: {% image_buster /assets/img_archive/postman_get.png %} [6]: {% image_buster /assets/img_archive/postman_response.png %}

[1]: https://www.getpostman.com
[7]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {{site.baseurl}}/api/api_key/
