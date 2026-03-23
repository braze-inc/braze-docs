---
nav_title: Directives de documentation des endpoints API
article_title: Directives de documentation des endpoints API
description: "Directives pour documenter les endpoints de l'API Braze."
page_order: 3
noindex: true
---

# Directives de documentation des endpoints API

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

> De manière générale, la documentation des endpoints API doit suivre les directives indiquées dans les [Directives générales]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#general-guidelines). Cependant, certains sujets spécifiques peuvent nécessiter des directives de contenu différentes, répertoriées dans ce document.

Braze prend en charge les méthodes API REST suivantes :

* GET  
* DELETE  
* PATCH  
* POST  
* PUT

## Créer un nouvel article d'endpoint

Lorsque vous créez un nouvel article d'endpoint, veillez à ajouter également cet endpoint dans le [guide de l'API Braze]({{site.baseurl}}/api/home) afin qu'il soit consultable via la recherche. Accédez au dossier **`_docs`** **`> _api`** puis au fichier **`> home.md`** pour ajouter l'endpoint avec son chemin et une description en une phrase.

## Faire référence aux endpoints

De manière générale, il n'existe pas de convention claire pour faire référence aux endpoints dans la documentation. Lorsque vous faites référence aux endpoints Braze, utilisez votre meilleur jugement pour déterminer comment désigner un endpoint en fonction de votre cas d'utilisation.

Vous pouvez faire référence à un endpoint par son chemin (par exemple, `/users/track`) ou par le nom de l'endpoint suivi du mot « endpoint » (par exemple, l'endpoint track user). Si le chemin est particulièrement long, préférez le nom de l'endpoint.

Utilisez le style de phrase lorsque vous faites référence à l'endpoint par son nom. Utilisez le texte en code lorsque vous faites référence à l'endpoint par son chemin.

Ne mettez pas de majuscule au mot « endpoint » sauf s'il fait directement référence à un nom de section. N'incluez pas le mot « API » lorsque vous faites directement référence à un endpoint.

Il existe des cas où un endpoint est désigné comme une API. Par exemple, cette affirmation est correcte : « Braze utilise une API REST avec de nombreux endpoints » lorsqu'on parle de manière générale des endpoints Braze.

Ne mettez pas de guillemets autour du nom de l'endpoint. N'utilisez pas de texte brut pour faire référence au chemin.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À ne pas faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Utilisez l'endpoint Generate preference center URL pour effectuer les étapes suivantes.</td><td style="width: 50%;">Utilisez <code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code> pour effectuer les étapes suivantes.</td></tr>
<tr><td style="width: 50%;">Utilisez l'endpoint <code>/users/track</code>.</td><td style="width: 50%;">Utilisez l'endpoint API « Users Track ».</td></tr>
</tbody>
</table>
{:/}

### Liens vers les articles d'endpoints

Lorsque vous faites référence à des articles d'endpoints, veillez à utiliser un [texte de lien explicite]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#writing-links) qui a du sens hors contexte. Si vous utilisez le chemin de l'endpoint comme lien, fournissez des détails dans le texte environnant, car le chemin ne communique pas toujours clairement la fonction de l'endpoint.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À ne pas faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Supprimez les profils utilisateur à l'aide de l'<a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">endpoint Delete user</a> de Braze.</td><td style="width: 50%;">Supprimez les profils utilisateur à l'aide de l'endpoint <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> de Braze.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/">endpoint <code>/users/export/id</code></a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

## En-têtes

L'introduction d'un article d'endpoint doit inclure les informations suivantes :

* Le type de requête et l'URL du chemin de l'endpoint  
* Une brève description de l'endpoint, commençant par « Utilisez cet endpoint pour… »  
* Le lien « Voir dans Postman »  
* Une alerte de type note avec l'autorisation de clé API REST requise

Utilisez cette liste de vérification pour vous assurer que les en-têtes appropriés (et le contenu correspondant) sont inclus dans chaque article d'endpoint et dans l'ordre indiqué. Notez qu'il peut y avoir des sous-en-têtes propres à un endpoint, comme différents types d'exemples de requêtes.

* Limite de débit  
* Paramètres de chemin  
* Corps de la requête  
* Paramètres de la requête  
* Exemple de requête  
* Paramètres de la réponse  
* Exemple de réponse  
* Résolution des problèmes (le cas échéant)

Consultez [En-têtes et titres]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#headings-and-titles) pour les directives de mise en forme.

### Paramètres de chemin

Si l'endpoint comporte des paramètres de chemin, incluez un en-tête « Paramètres de chemin » et un tableau (similaire au tableau des paramètres de la requête).

S'il n'y a pas de paramètres de chemin pour l'endpoint, incluez un en-tête « Paramètres de chemin » et le message suivant : « Il n'y a pas de paramètres de chemin pour cet endpoint. »

S'il n'y a ni paramètres de chemin ni paramètres de requête pour l'endpoint, regroupez la mention dans la même section comme indiqué ci-dessous.

{% raw %}
{::nomarkdown}
<div style="margin-left: 2em;">
<code>
## Path and request parameters <br>
There are no path or request parameters for this endpoint.
</code>
</div>
{:/}
{% endraw %}

## Conventions de nommage

Commencez chaque nom d'endpoint par un verbe d'action après sa méthode. Cela permet aux utilisateurs de connaître immédiatement la fonction de l'endpoint.

N'utilisez pas la méthode API comme verbe principal pour le nom de l'endpoint.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À ne pas faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">POST: Create new user alias</td><td style="width: 50%;">POST: New user alias</td></tr>
<tr><td style="width: 50%;">GET: Look up an existing dashboard user account</td><td style="width: 50%;">GET: Existing dashboard user account</td></tr>
</tbody>
</table>
{:/}

Les exceptions à cette convention de nommage sont les endpoints de la [section Export]({{site.baseurl}}/api/endpoints/export), car le nom de la section est un verbe qui indique que les informations répertoriées peuvent être exportées.

## Autorisations des clés API

Les autorisations des clés API sont des permissions que vous pouvez affecter à un utilisateur ou un groupe pour limiter leur accès à certains appels API. Pour chaque documentation d'endpoint, incluez le message suivant après le lien vers la documentation Postman :

> Pour utiliser cet endpoint, vous devez générer une clé API avec l'autorisation `permission_name_here`.

Pour consulter la liste complète des autorisations des clés API, accédez à **Paramètres > Clés API** sous **Configuration et test** dans le tableau de bord de Braze. Sélectionnez une clé API avec accès complet (le nom de la clé contient généralement l'expression « full access »). Chaque nom d'autorisation doit généralement correspondre au nom de l'endpoint.

Notez que les endpoints SCIM n'ont pas d'autorisations de clé API répertoriées, car ils sont spécifiques à l'intégration SCIM qui se fait en dehors de la console de développement.

## Limites de débit

De manière générale, votre limite de débit doit spécifier le nombre de requêtes et le temps alloué.

Soyez attentif aux endpoints qui partagent une limite de débit totale. Par exemple, tous les endpoints asynchrones d'éléments de catalogue partagent une limite de débit totale ; il est donc important de l'indiquer dans les articles respectifs.

### Comment mettre à jour le fichier des limites de débit

Si la documentation de votre endpoint nécessite la mise à jour ou l'ajout d'une nouvelle limite de débit, accédez à **_docs > _api > api_limits.md** pour effectuer les modifications.

## Paramètres

Définissez les paramètres de la requête et de la réponse dans deux tableaux distincts. Ces tableaux doivent contenir les colonnes suivantes :

* **Paramètre**  
* **Requis**  
* **Type de données**  
* **Description**

Lorsque vous faites directement référence aux paramètres d'un endpoint et lorsque vous listez les valeurs dans la colonne **Paramètre**, utilisez le texte en code. Lorsque vous listez les valeurs dans les colonnes **Requis**, **Type de données** et **Description**, utilisez des majuscules initiales.

### Texte de marque substitutive

Pour le texte de marque substitutive, utilisez des accolades avec une brève description de ce que l'utilisateur doit inclure.

Pour les marques substitutives de clé API, utilisez `YOUR_REST_API_KEY`, et non `YOUR-REST-API-KEY`.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À ne pas faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code></td><td style="width: 50%;"><code>/preference_center/v1/[preferenceCenterExternalId]</code></td></tr>
<tr><td style="width: 50%;"><code>/scim/v2/Users/{userId}</code></td><td style="width: 50%;"><code>/url/[userId]/scim/v2/Users/userID</code></td></tr>
</tbody>
</table>
{:/}

Pour les marques substitutives de clé API, utilisez `YOUR_REST_API_KEY` (avec des underscores), et non `YOUR-REST-API-KEY` (avec des tirets).

## Demandes et réponses

Une requête API comprend l'en-tête et les paramètres de la requête. Les paramètres de la requête doivent être formatés comme suit :

```bash
parameter": (required/optional, data type) A brief description
```

Voici un exemple de corps de requête pour l'[endpoint Create new user alias]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) :

```bash
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "user_aliases": (required, array of new user alias object)
}
```

Utilisez des guillemets droits doubles (" ") pour identifier les paramètres qui sont des chaînes de caractères ou des tableaux dans un exemple de requête. Assurez-vous que tous les crochets et parenthèses ouverts sont fermés.

Une réponse API comprend le corps de la réponse, les en-têtes et le code d'état HTTP. Incluez toujours un exemple de réponse. Cet exemple doit contenir un texte simple décrivant le paramètre. Voici un exemple de réponse pour l'[endpoint Update user alias]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/#example-request).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

### Codes d'état et codes d'erreur

Les codes d'état indiquent si la requête spécifique d'un utilisateur a été traitée avec succès. Il peut être utile d'inclure les codes d'état pour que les utilisateurs sachent ce qui est considéré comme un succès. Par exemple, les codes 400 et 404 peuvent indiquer une réponse d'erreur pour l'endpoint.

Si la documentation de votre endpoint nécessite de lister des codes d'erreur, renvoyez vers l'article [Erreurs et réponses API]({{site.baseurl}}/api/errors/) situé dans le dossier **_docs** **> _api** puis le fichier **> errors.md**.

## Exemples de code

Les exemples de code, comme les exemples de requêtes et de réponses, doivent pouvoir être copiés et utilisés avec un minimum d'effort. À l'exception du texte de marque substitutive (par exemple, la clé API dans l'en-tête), les exemples de requêtes doivent fonctionner tels quels. Utilisez Postman pour vous assurer que votre requête est correctement formatée.

### Code embelli versus code minifié

Si la requête de l'endpoint contient un corps, embellissez l'exemple dans Postman. Cela facilite la compréhension de chaque élément de la requête pour les développeurs qui découvrent les conventions Braze.

Si le corps de la requête de l'endpoint est très court ou ne contient pas de corps, minifiez la requête afin de supprimer les espaces inutiles. Utilisez un outil comme [JSON Minifier](https://codebeautify.org/jsonminifier) pour cela.

### Commentaires en ligne

Utilisez deux barres obliques (//) pour indiquer les commentaires sur une seule ligne dans les exemples de code.

Les commentaires en ligne sont des outils précieux pour attirer l'attention de l'utilisateur sur une section spécifique du code, expliquer la fonction d'un bloc de code ou fournir un contexte supplémentaire.

Utilisez les commentaires en ligne pour montrer rapidement où la couche logique de l'utilisateur serait placée et comment elle ferait référence au code du SDK. Utilisez des exemples simples mais réalistes. Par exemple, un attribut d'exemple « favorite_movie » est plus parlant que « example_attribute ». Même si l'activité de l'utilisateur ne suit pas ou ne se soucie pas du film préféré d'un utilisateur final, cet exemple montre les *types* de cas d'utilisation qui pourraient être suivis via cet attribut. Les exemples génériques ne suscitent pas la même compréhension intuitive.

Évitez les commentaires en ligne qui se contentent de reformuler du code ou des noms de méthodes lisibles par l'humain. Utilisez plutôt une variété de synonymes pour les méthodes et paramètres spécifiques à Braze afin de fournir un cadre de compréhension pour les locuteurs non natifs de l'anglais.

De manière générale, respectez les conventions standard de l'anglais lorsque vous rédigez des commentaires en ligne. Par exemple, commencez les phrases par une majuscule, écrivez les mots en entier, etc.

## Ressources supplémentaires

- [Guide de style de la documentation développeur Google](https://developers.google.com/style)  
  - [Code de référence API et commentaires](https://developers.google.com/style/api-reference-comments)