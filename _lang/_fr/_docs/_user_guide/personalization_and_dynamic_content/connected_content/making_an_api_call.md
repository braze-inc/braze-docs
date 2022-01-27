---
nav_title: Effectuer un appel API
article_title: Faire un appel API de contenu connecté
page_order: 0
description: "Cet article de référence couvre la façon de faire un appel à l'API de contenu connecté, ainsi que des exemples utiles et des cas avancés d'utilisation de contenu connecté."
---

# Passer un appel API

{% raw %}

Les messages envoyés par Braze peuvent récupérer le contenu d'un serveur web pour être inclus dans un message en utilisant la balise `{% connected_content %}`. En utilisant ce tag, vous pouvez assigner ou déclarer des variables en utilisant `:save`. Les aspects de ces variables peuvent être référencés plus tard dans le message avec [Liquid][2].

Par exemple, le corps du message suivant accèdera à l'URL `http://numbersapi.com/random/trivia` et inclura un fait amusant de trivia dans votre message :

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Bonjour, voici un peu amusant pour vous !: {{result.text}}
```

Vous pouvez également inclure les attributs du profil utilisateur comme variables dans la chaîne URL lorsque vous faites des requêtes de contenu connecté. Par exemple, vous pouvez avoir un service web qui renvoie du contenu en fonction de l'adresse de courriel et de l'ID d'un utilisateur. Si vous passez des attributs contenant des caractères spéciaux, comme le signe at (@), assurez-vous d'utiliser le filtre Liquid `url_param_escape` pour remplacer tous les caractères non autorisés dans les URLs par leurs versions échappées en mode URL, comme indiqué dans l'attribut d'adresse e-mail ci-dessous.

```
Bonjour, voici quelques articles qui pourraient vous intéresser :

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```

Si l'URL est indisponible et atteint une page 404, Braze renverra une chaîne vide à sa place. Si l'URL atteint une page HTTP 500/502, l'URL échouera lors d'une nouvelle tentative de logique. Parce que Braze délivre des messages à un rythme très rapide, assurez-vous que votre serveur peut gérer des milliers de connexions simultanées afin que les serveurs ne soient pas surchargés lorsque vous tirez du contenu. Lorsque vous utilisez des API publiques, assurez-vous que votre utilisation n'enfreindra pas les limites de taux que le fournisseur d'API peut employer. Braze exige que le temps de réponse du serveur soit inférieur à 2 secondes pour des raisons de performance; si le serveur prend plus de 2 secondes pour répondre, le contenu ne sera pas inséré.

Si le point de terminaison renvoie du JSON, vous pouvez le détecter en vérifiant si la valeur `connectée` est nulle, puis [interrompre conditionnellement le message][1]. Braze n'autorise que les URLs qui communiquent sur le port 80 (HTTP) et 443 (HTTPS).
{% endraw %}

{% alert note %}
* Les valeurs d'attribut doivent être entourées de `${}` pour fonctionner correctement dans la version de la syntaxe Liquid de Braze.
* Les appels de contenu connectés se produiront lorsque le message sera envoyé, à l'exception des messages In-App, qui passeront cet appel lorsque le message sera affiché.
* Les appels de contenu connectés ne suivent pas les redirections.
* Les systèmes Braze peuvent faire le même appel à l'API de contenu connecté plus d'une fois par destinataire. C'est parce que Braze peut avoir besoin de faire un appel à l'API de contenu connecté pour rendre un message payload, et les payloads de messages peuvent être rendus plusieurs fois par destinataire pour validation, réessayez la logique ou d'autres fins internes. Vos systèmes devraient être en mesure de tolérer que le même appel de contenu connecté soit effectué plus d'une fois par destinataire.
{% endalert %}

{% raw %}

## En utilisant l'authentification de base

Si l'URL nécessite une authentification de base, Braze peut générer un identifiant d'authentification basique que que vous pouvez utiliser dans votre appel API. Vous pouvez gérer les identifiants d'authentification de base existants et en ajouter de nouveaux dans l'onglet **Contenu connecté** de **Gérer les paramètres**.

!\[Gestion des identifiants d'authentification de base\]\[34\]

Pour ajouter un nouvel identifiant, cliquez sur **Ajouter un identifiant**. Donnez un nom à votre identifiant et entrez le nom d'utilisateur et le mot de passe.

!\[Création d'authentification basique\]\[35\]{: style="max-width:30%" }

Vous pouvez ensuite utiliser cette authentification de base dans vos appels API en référençant le nom du jeton :

```
Bonjour, voici un peu de trivia pour vous !: {% connected_content https://votresite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si vous supprimez un identifiant, gardez à l'esprit que tout appel de contenu connecté tentant de l'utiliser, il sera abandonné.
{% endalert %}

## Utilisation de l'authentification de jeton

Lorsque vous utilisez le contenu connecté de Brase, vous pouvez trouver que certaines API nécessitent un jeton au lieu d'un nom d'utilisateur et d'un mot de passe. Vous trouverez ci-dessous un extrait de code pour référencer et modéliser vos messages.

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://votre_API_link_here/
     :method post
     :headers {
       "X-App-Id": "VOTRE-APP-ID",
       "X-App-Token": "VOTRE APP-TOKEN"
  }
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

## Utiliser Open Authentication (OAuth)

Certaines configurations d'API nécessitent la récupération d'un jeton d'accès qui peut ensuite être utilisé pour authentifier le point d'extrémité de l'API auquel vous voulez accéder.

### Récupérer le jeton d'accès

L'exemple ci-dessous illustre la récupération et l'enregistrement d'un jeton d'accès à une variable locale qui peut ensuite être utilisé pour authentifier l'appel ultérieur à l'API. Un paramètre `:cache_max_age` peut être ajouté pour correspondre à l'heure à laquelle le jeton d'accès est valide et réduire le nombre d'appels de contenu connecté sortant. Voir [Mise en cache configurable][36] pour plus d'informations.

{% raw %}
```
{% connected_content
     https://votre_API_access_token_endpoint_here/
     :method post
     :headers {
       "Content-Type": "VOTRE CONTENT-TYPE",
       "Autorisation": "Porteur VOTRE-APP-TOKEN"
  }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

### Autoriser l'API en utilisant le jeton d'accès récupéré

Maintenant que le jeton est enregistré, il peut être dynamiquement templé dans l'appel suivant de contenu connecté pour autoriser la requête :

{% raw %}
```
{% connected_content
     https://votre_API_endpoint_here/
     :headers {
       "Content-Type": "VOTRE CONTENT-TYPE",
       "Authorization": "{{token_response}}"
  }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

## Liste blanche IP de contenu connecté

Quand un message utilisant le Contenu Connecté est envoyé depuis Braze, les serveurs Braze font automatiquement des demandes de réseau à nos clients ou à des serveurs tiers pour récupérer des données. Avec la liste blanche IP, vous pouvez vérifier que les requêtes de contenu connecté proviennent réellement de Braze, ajoutant une couche de sécurité supplémentaire.

Braze enverra des requêtes de contenu connecté depuis les plages IP ci-dessous. Les plages listées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont été optées pour la liste blanche.

Braze a un ensemble réservé d'adresses IP utilisées pour tous les services, qui ne sont pas tous actifs à un moment donné.  Cela garantit que si Braze a besoin d'envoyer depuis un centre de données différent ou de faire de la maintenance, Braze peut le faire sans affecter les clients. Braze peut utiliser un, un sous-ensemble ou toutes les adresses IP listées ci-dessous lorsque vous faites des requêtes de contenu connecté.

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`: |
| ------------------------------------------------------------------------ |
| `23.21.118.191`                                                          |
| `34.206.23.173`                                                          |
| `50.16.249.9`                                                            |
| `52.4.160.214`                                                           |
| `54.87.8.34`                                                             |
| `54.156.35.251`                                                          |
| `52.54.89.238`                                                           |
| `18.205.178.15`                                                          |

| Pour les instances `EU-01` et `EU-02`: |
| -------------------------------------- |
| `52.58.142.242`                        |
| `52.29.193.121`                        |
| `35.158.29.228`                        |
| `18.157.135.97`                        |
| `3.123.166.46`                         |
| `3.64.27.36`                           |
| `3.65.88.25`                           |
| `3.68.144.188`                         |
| `3.70.107.88`                          |

| Pour l'instance `US-08`: |
| ------------------------ |
| `52.151.246.51`          |
| `52.170.163.182`         |
| `40.76.166.157`          |
| `40.76.166.170`          |
| `40.76.166.167`          |
| `40.76.166.161`          |
| `40.76.166.156`          |
| `40.76.166.166`          |
| `40.76.166.160`          |
| `40.88.51.74`            |
| `52.154.67.17`           |
| `40.76.166.80`           |
| `40.76.166.84`           |
| `40.76.166.85`           |
| `40.76.166.81`           |
| `40.76.166.71`           |
| `40.76.166.144`          |
| `40.76.166.145`          |
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %} [35]: {% image_buster /assets/img_archive/basic_auth_token.png %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#liquid-usage-use-cases--overview
[36]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching
