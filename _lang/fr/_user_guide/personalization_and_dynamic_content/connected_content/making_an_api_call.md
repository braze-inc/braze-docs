---
nav_title: Effectuer un appel API
article_title: Création d’un appel API de contenu connecté
page_order: 0
description: "Le présent article de référence explique comment effectuer un appel API de contenu connecté, ainsi que des exemples utiles et des scénarios d’utilisation de contenu connecté avancés."
search_rank: 2
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Création d’un appel API de contenu connecté

Utilisez le contenu connecté pour insérer toute information accessible via API directement dans les messages que vous envoyez aux utilisateurs. Vous pouvez extraire du contenu directement à partir de votre serveur Web ou des API accessibles au public.

## Balise Contenu connecté

{% raw %}

Pour envoyer un appel de contenu connecté, utilisez la balise `{% connected_content %}`. Cette balise vous permet d’attribuer et de déclarer des variables en utilisant `:save`. Les aspects de ces variables peuvent être référencés plus tard dans le message avec [Liquid][2].

Par exemple, le corps de message suivant va accéder à l’URL `http://numbersapi.com/random/trivia` et inclure une histoire amusante dans votre message :

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is fun some trivia for you!: {{result.text}}
```

### Ajouter des variables

Vous pouvez également inclure des attributs de profil utilisateur comme variables dans la chaîne de caractères d’URL lors de la création de requêtes de contenu connecté. 

Par exemple, vous pouvez disposer d’un service Web qui renvoie le contenu en fonction de l’adresse e-mail et de l’ID d’un utilisateur. Si vous transmettez des attributs contenant des caractères spéciaux, tels que le signe (@), assurez-vous d’utiliser le filtre Liquid `url_param_escape` pour remplacer les caractères non autorisés dans les URL avec leurs versions d’échappement compatibles avec les URL, comme indiqué dans l’attribut d’e-mail suivant.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Les valeurs d’attribut doivent être entourées de `${}` pour fonctionner correctement dans la version de la syntaxe Liquid de Braze.
{% endalert %}

Les requêtes de contenu connecté prennent uniquement en charge les requêtes GET et POST.

## Gestion des erreurs

Si l’URL n’est pas disponible et qu’elle atteint une page 404, Braze renvoie une chaîne de caractères vide à sa place. Si l’URL atteint une page HTTP 500 ou 502, l’URL échoue à la nouvelle tentative de logique.

Si l’endpoint renvoie JSON, vous pouvez le détecter en vérifiant si la valeur de `connected` est nulle, puis [abandonnez le message sous condition][1]. Braze autorise uniquement les URL qui communiquent sur le port 80 (HTTP) et 443 (HTTPS).

## Performance

Étant donné que Braze délivre des messages à un débit très rapide, assurez-vous que votre serveur peut gérer des milliers de connexions simultanées afin que les serveurs ne soient pas surchargés lors de la récupération de contenus. Lorsque vous utilisez des API publiques, assurez-vous que votre utilisation n’enfreint aucune limite tarifaire que le fournisseur API peut employer. Braze exige que le temps de réponse du serveur soit inférieur à 2 secondes pour des raisons de performance ; si le serveur prend plus de 2 secondes pour répondre, le contenu ne sera pas inséré.

Les systèmes de Braze peuvent renvoyer le même appel API de contenu connecté plus d’une fois par destinataire. En effet, Braze peut avoir besoin d’un appel API de contenu connecté pour renvoyer une charge utile de message, et les charges utiles de message peuvent être renvoyées plusieurs fois par destinataire pour validation, logique de nouvelle tentative ou autres objectifs internes. Vos systèmes doivent être en mesure de tolérer le même appel de contenu connecté plus qu’une fois par destinataire.

## Choses à savoir

* Braze ne facture pas les appels API et ne les impute pas sur votre compte de points de données.
* Il y a une limite par défaut de 1 Mo pour les réponses du contenu connecté. Cette limite par défaut peut être augmentée sur demande. Contactez votre gestionnaire du succès des clients pour plus d’informations.
* Les appels de contenu connectés se produisent lorsque le message est envoyé, à l’exception des messages dans l’appli, qui effectueront cet appel lorsque le message est affiché.
* Les appels de contenu connectés ne suivent pas les redirections.

## Types d’authentifications

### Utilisation de l’authentification de base

Si l’URL nécessite une authentification de base, Braze peut générer des informations d’authentification de base pour que vous puissiez l’utiliser dans votre appel API. Vous pouvez gérer les informations d’authentification de base existantes et en ajouter de nouveaux dans l’onglet **Connected Content (Contenu connecté)** de **Manage Settings (Gérer les paramètres)**.

![][34]

Pour ajouter une nouvelle information d’identification, cliquez sur **Add Credential (Ajouter des informations d’identification)**. Nommez vos identifiants et saisissez le nom d’utilisateur et le mot de passe.

![][35]{: style="max-width:30%" }

Vous pouvez alors utiliser ces informations d’identification de base pour l’authentification dans vos appels API en faisant référence au nom du jeton :

{% raw %}
```
Hi there, here is fun some trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si vous supprimez une information d’identification, gardez à l’esprit que tout appel de Contenu connecté qui essaie de l’utiliser sera abandonné.
{% endalert %}

### Utilisation de l’authentification par jeton

Lorsque vous utilisez le contenu connecté de Braze, vous pouvez trouver que certaines API nécessitent un jeton plutôt qu’un nom d’utilisateur et un mot de passe. L’appel suivant est un extrait de code qui vous permet de référencer et de modéliser vos messages.

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://your_API_link_here/
     :method post
     :headers {
       "X-App-Id": "YOUR-APP-ID",
       "X-App-Token": "YOUR-APP-TOKEN"
  }
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Utilisation de l’authentification ouverte (OAuth)

Certaines configurations API nécessitent la récupération d’un jeton d’accès qui peut ensuite être utilisé pour authentifier l’endpoint API auquel vous souhaitez accéder.

#### Récupérer le jeton d’accès

L’exemple suivant illustre la récupération et l’enregistrement d’un jeton d’accès à une variable locale qui peut ensuite être utilisée pour authentifier l’appel API suivant. Un paramètre `:cache_max_age` peut être ajouté pour correspondre à l’heure à laquelle le jeton d’accès est valide et réduire le nombre d’appels de contenu connecté sortant. Voir [Mise en cache configurable][36] pour plus d’informations.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "Bearer YOUR-APP-TOKEN"
  }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Autoriser l’API à l’aide du jeton d’accès récupéré

Maintenant que le jeton est enregistré, il peut être placé dynamiquement dans l’appel de Contenu connecté suivant pour autoriser la demande :

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
  }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

## Whitelist d’IP de contenu connecté

Lorsqu’un message utilisant le Contenu connecté est envoyé par Braze, les serveurs Braze font automatiquement des requêtes réseau aux serveurs de nos clients ou tiers pour extraire des données. Avec la whitelist d’IP, vous pouvez vérifier que les demandes de contenu connecté proviennent réellement de Braze, ajoutant ainsi une couche de sécurité supplémentaire.

Braze envoie des demandes de Contenu connecté à partir des plages IP suivantes. Les plages répertoriées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont été choisies pour la whitelist. 

Braze dispose d’un ensemble d’IP réservé pour tous les services, qui ne sont pas tous actifs à un moment donné.  Cela garantit que si Braze a besoin d’envoyer un autre centre de données ou de procéder à la maintenance, Braze peut le faire sans impacter les clients. Braze peut utiliser un IP, un sous-ensemble d’IP ou tous les IP suivants répertoriés lors de la création de requêtes de contenu connecté.

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06` : |
|---|
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| Pour les instances `EU-01` et `EU-02` : |
|---|
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88`

| Pour l’instance `US-08` : |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#liquid-usage-use-cases--overview
[16]: [success@braze.com](mailto:success@braze.com)
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
[36]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching
