---
nav_title: Postman et demandes d’exemples
article_title: Postman et demandes d’échantillons
page_order: 3
description: "Cet article de référence couvre la collection Braze Postman, ce qu’elle est, comment la configurer et l’utiliser, ainsi que la façon de modifier et d’envoyer des demandes."
page_type: reference

---

# Postman et demandes d’exemples

> Braze vous permet de générer des exemples de requêtes API pour tous nos endpoints grâce à notre collection Postman. Cet article de référence couvre la collection Braze Postman, ce qu’elle est, comment la configurer et l’utiliser, ainsi que la façon de modifier et d’envoyer des demandes.

## Qu’est-ce que Postman ?

Postman est un outil d’édition visuelle gratuit pour la création et l’analyse des demandes API. Contrairement à d'autres méthodes d'interaction avec les API (par exemple, l'utilisation de cURL), Postman vous permet de modifier facilement les demandes d'API, d'afficher les informations d'en-tête, et bien plus encore. Postman a la possibilité d’enregistrer les collections ou bibliothèques d’échantillons de demandes API prédéfinis. Afin de faciliter la mise en service et l’exécution de nos API REST pour nos clients, nous avons créé une collection avec des exemples prédéfinis pour tous nos endpoints d’API.

Consultez ou téléchargez notre collection Postman en cliquant sur **Exécuter dans Postman** dans notre [documentation Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) pour commencer.

## Utilisation de la collection Braze Postman

Si vous disposez d'un compte Postman (vous pouvez télécharger les versions macOS, Windows et Linux depuis le [site web de Postman](https://www.getpostman.com)), vous pouvez ouvrir notre documentation Postman dans votre propre application Postman en cliquant sur le bouton orange **Exécuter dans Postman.**  Vous pouvez ensuite [créer un environnement](#setting-up-your-postman-environment), ou utiliser notre environnement API REST de Braze comme modèle, et modifier les requêtes `POST` et `GET` disponibles pour répondre à vos propres besoins.

### Configuration de votre environnement Postman

{% raw %}
La collection Braze Postman utilise une variable de modèle, `{{instance_url}}`, pour remplacer l’URL d’API REST de votre instance Braze dans les demandes prédéfinies, et la variable `{{api_key}}` de votre clé API. Au lieu de devoir modifier manuellement toutes les demandes de la collection, vous pouvez configurer cette variable dans votre environnement Postman. Vous pouvez sélectionner notre environnement modèle (modèle de l’environnement de l’API REST Braze) dans la liste déroulante, puis remplacer les valeurs de variables par les vôtres, ou créer votre propre environnement.
{% endraw %}

Pour créer votre propre environnement, procédez comme suit :

1. Dans l'onglet **Espaces de travail**, sélectionnez **Environnements**.
2. Cliquez sur le bouton **+** plus pour créer un nouvel environnement.
3. Donnez un nom à cet environnement (par exemple, "Braze API Requests") et ajoutez des clés pour `instance_url` et `api_key` avec des valeurs correspondant à votre [instance Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) et à la [clé REST API de Braze]({{site.baseurl}}/api/api_key/).
4. Cliquez sur **Enregistrer**.

{% alert note %}
Dans les corps de requête `POST`, la `api_key` doit être comprise entre des guillemets : `"MY-API-KEY-EXAMPLE"`. Dans les URL `GET`, elle ne doit pas l’être. Nous vous avons déjà fourni ce formatage pour les corps de demande `POST`, les URL `GET` et le modèle d’environnement de `YOUR-API-KEY-HERE` dans cette documentation.
{% endalert %}

![Ajout de variables pour la clé API et l’URL d’instance à l’environnement API REST de Braze dans Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Utiliser les demandes prédéfinies de la collection

Après avoir configuré votre environnement, vous pouvez utiliser l'une des demandes prédéfinies de la collection comme modèle pour créer de nouvelles demandes d'API. Pour commencer à utiliser l'une des requêtes préconstruites, cliquez dessus dans le menu **Collections** de Postman. Cela ouvrira la demande sous forme de nouvel onglet dans la fenêtre principale de l’application Postman.

En général, il existe deux types de requêtes que les endpoints API de Braze acceptent : `GET` et `POST`. Selon la méthode `HTTP` que l’endpoint utilise, vous devrez modifier la demande prédéfinie différemment.

#### Modifier une demande POST

Lorsque vous modifiez une demande `POST`, ouvrez la demande et accédez à la section **Corps** dans l'éditeur de demande. Pour des raisons de lisibilité, sélectionnez le bouton radio **raw** pour formater le corps de la requête `JSON`.

![Onglet Corps lors de la modification d’une demande POST Suivi de l’utilisateur dans Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Modifier une demande GET

Lors de la modification d’une demande `GET`, changez les paramètres transmis dans l’URL de demande. Pour ce faire, sélectionnez l'onglet **Params** et modifiez les paires clé-valeur dans les champs qui apparaissent.

![Onglet Paramètres lors de la modification d’une demande GET Demander la liste des adresses e-mail désinscrites dans Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Envoyer votre demande

Lorsque votre demande d'API est prête, cliquez sur **Envoyer.** La demande est envoyée et les données de réponse s’affichent dans une section sous l’éditeur de demande. À partir de là, vous pouvez afficher les données brutes renvoyées par l'API de Braze, le code de réponse HTTP, le temps de traitement de la demande et les informations d'en-tête.

![Exemples de données de réponse de corps d’une demande POST avec un statut de 201 Créés et un temps de réponse de 269 millisecondes.]({% image_buster /assets/img_archive/postman_response.png %})

