---
nav_title: Faire un appel au contenu connecté
article_title: Création d’un appel API de contenu connecté
page_order: 0
description: "Le présent article de référence explique comment effectuer un appel API de contenu connecté, ainsi que des exemples utiles et des scénarios d’utilisation de contenu connecté avancés."
search_rank: 2
---

# [![Braze](https://learning.braze.com/connected-content)[cours d'apprentissage]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} Faire un appel à l'API du contenu connecté

> Utilisez le contenu connecté pour insérer toute information accessible par API directement dans les messages que vous envoyez aux utilisateurs. Vous pouvez extraire du contenu directement à partir de votre serveur Web ou des API accessibles au public.<br><br>Cette page explique comment effectuer des appels à l'API du contenu connecté, les cas d'utilisation avancés du contenu connecté, la gestion des erreurs, etc.

## Envoi d'un appel de contenu connecté

{% raw %}

Pour envoyer un appel de contenu connecté, utilisez la balise `{% connected_content %}`. Cette balise vous permet d’attribuer et de déclarer des variables en utilisant `:save`. Certains aspects de ces variables peuvent être référencés plus loin dans le message avec [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

Par exemple, le corps de message suivant va accéder à l’URL `http://numbersapi.com/random/trivia` et inclure une histoire amusante dans votre message :

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
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
Les valeurs d'attributs doivent être entourées de `${}` pour fonctionner correctement dans notre version de la syntaxe Liquid.
{% endalert %}

Les requêtes de contenu connecté prennent uniquement en charge les requêtes GET et POST.

## Gestion des erreurs

Si l’URL n’est pas disponible et qu’elle atteint une page 404, Braze renvoie une chaîne de caractères vide à sa place. Si l'URL atteint une page HTTP 500 ou 502, l'URL échouera dans la logique de réessai.

Si l’endpoint renvoie du JSON, vous pouvez le détecter en vérifiant si la valeur de `connected` est nulle, puis [abandonnez le message sous condition]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). Braze autorise uniquement les URL qui communiquent sur le port 80 (HTTP) et 443 (HTTPS).

### Détection d'un hôte malsain

Le contenu connecté utilise un mécanisme de détection d'hôte malsain pour détecter lorsque l'hôte cible connaît un taux élevé de lenteur significative ou de surcharge, ce qui se traduit par des dépassements de délai, un trop grand nombre de demandes ou d'autres résultats qui empêchent Braze de communiquer avec succès avec l'endpoint cible. Il agit comme un garde-fou pour réduire la charge inutile qui pourrait être à l'origine des difficultés de l'hôte cible. Il sert également à stabiliser l'infrastructure de Braze et à maintenir des vitesses d'envoi de messages rapides.

Si l'hôte cible connaît un taux élevé de lenteur significative ou de surcharge, Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute, en simulant à la place des réponses indiquant la défaillance. Au bout d'une minute, Braze vérifie l'état de santé de l'hôte à l'aide d'un petit nombre de requêtes avant de reprendre les requêtes à pleine vitesse si l'hôte s'avère sain. Si l'hôte est toujours en mauvaise santé, Braze attendra encore une minute avant de réessayer.

Si les requêtes adressées à l'hôte cible sont interrompues par le détecteur d'hôte malsain, Braze continuera d'afficher les messages et de suivre votre logique Liquid comme s'il avait reçu un code de réponse d'erreur. Si vous voulez vous assurer que ces demandes de contenu connecté sont relancées lorsqu'elles sont interrompues par le détecteur d'hôte malsain, utilisez l'option `:retry`. Pour plus d'informations sur l'option `:retry`, reportez-vous à la section [Tentatives de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Si vous pensez que la détection des hôtes malsains peut être à l'origine de problèmes, contactez l'[assistance de Braze]({{site.baseurl}}/support_contact/).

{% alert note %}
Vous pouvez autoriser l'utilisation d'URL spécifiques pour le contenu connecté. Pour accéder à cette fonctionnalité, contactez votre gestionnaire de satisfaction client.
{% endalert %}

{% alert tip %}
Consultez la page [Résolution des problèmes des demandes de webhook et de contenu connecté]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) pour en savoir plus sur la manière de résoudre les codes d'erreur courants.
{% endalert %}

## Permettre des performances efficaces

Comme Braze envoie les messages à un rythme très rapide, assurez-vous que votre serveur peut gérer des milliers de connexions simultanées afin que les serveurs ne soient pas surchargés lors de l'extraction du contenu. Lorsque vous utilisez des API publiques, assurez-vous que votre utilisation n'enfreindra pas les limites de débit que le fournisseur de l'API peut appliquer. Braze exige que le temps de réponse du serveur soit inférieur à deux secondes pour des raisons de performances ; si le serveur met plus de deux secondes à répondre, le contenu ne sera pas inséré.

Les systèmes Braze peuvent effectuer le même appel API de contenu connecté plusieurs fois par destinataire. En effet, Braze peut avoir besoin d’un appel API de contenu connecté pour renvoyer une charge utile de message, et les charges utiles de message peuvent être renvoyées plusieurs fois par destinataire pour validation, logique de nouvelle tentative ou autres objectifs internes. Vos systèmes doivent pouvoir tolérer que le même appel au contenu connecté soit effectué plus d'une fois par destinataire.

## Choses à savoir

* Braze ne facture pas les appels à l'API et ceux-ci ne sont pas pris en compte dans votre consommation de points données.
* Les réponses au contenu connecté sont limitées à 1 Mo.
* Les appels de contenu connectés se produisent lorsque le message est envoyé, à l’exception des messages dans l’application, qui effectueront cet appel lorsque le message est affiché.
* Les appels de contenu connectés ne suivent pas les redirections.

## Types d’authentifications

### Utilisation de l’authentification de base

Si l'URL requiert une authentification de base, Braze peut stocker un justificatif d'authentification de base que vous pourrez utiliser dans votre appel API. Vous pouvez gérer les identifiants d'authentification de base existants et en ajouter de nouveaux dans **Paramètres** > Contenu connecté.

![Les paramètres du contenu connecté dans le tableau de bord de Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Pour ajouter un nouvel identifiant, sélectionnez **Ajouter un identifiant** > **Authentification de base**. 

!["Add credential" dropdown avec l'option d'utiliser l'authentification de base ou l'authentification par jeton.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Nommez vos identifiants et saisissez le nom d’utilisateur et le mot de passe.

![La fenêtre "Create New Credential" (Créer un nouveau justificatif) avec la possibilité de saisir un nom, un nom d'utilisateur et un mot de passe.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Vous pouvez alors utiliser ces informations d’identification de base pour l’authentification dans vos appels API en faisant référence au nom du jeton :

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si vous supprimez une information d’identification, gardez à l’esprit que tout appel de Contenu connecté qui essaie de l’utiliser sera abandonné.
{% endalert %}

### Utilisation de l’authentification par jeton

Lorsque vous utilisez le contenu connecté de Braze, vous pouvez constater que certaines API nécessitent un jeton au lieu d'un nom d'utilisateur et d'un mot de passe. Braze peut également stocker des informations d'identification qui contiennent des valeurs d'en-tête d'authentification par jeton.

Pour ajouter un justificatif d'identité contenant des valeurs de jeton, sélectionnez **Ajouter un justificatif d'identité** > **Authentification par jeton**. Ensuite, ajoutez les paires clé-valeur pour vos en-têtes d'appel API et le domaine autorisé.

![Un exemple de jeton "token_credential_abc" avec les détails de l'authentification du jeton.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Vous pouvez ensuite utiliser ce justificatif dans vos appels à l'API en faisant référence au nom du justificatif :

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Utilisation de l’authentification ouverte (OAuth)

Certaines configurations d'API nécessitent la récupération d'un jeton d'accès qui peut ensuite être utilisé pour authentifier l'endpoint de l'API auquel vous souhaitez accéder.

#### Étape 1 : Récupérer le jeton d’accès

L'exemple suivant illustre la récupération et l'enregistrement d'un jeton d'accès dans une variable locale, qui peut ensuite être utilisé pour authentifier l'appel API suivant. Un paramètre `:cache_max_age` peut être ajouté pour correspondre à l’heure à laquelle le jeton d’accès est valide et réduire le nombre d’appels de contenu connecté sortant. Pour plus d'informations, reportez-vous à la rubrique [Mise en cache configurable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching).

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Étape 2 : Autoriser l’API à l’aide du jeton d’accès récupéré

Une fois le jeton enregistré, il peut être intégré de manière dynamique dans l'appel au contenu connecté suivant afin d'autoriser la demande :

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

### Modifier les données d'identification

Vous pouvez modifier le nom de l'identifiant pour les types d'authentification.

- Pour l'authentification de base, vous pouvez mettre à jour le nom d'utilisateur et le mot de passe. Notez que le mot de passe précédemment saisi ne sera pas visible.
- Pour l'authentification par jeton, vous pouvez mettre à jour les paires clé-valeur de l'en-tête et le domaine autorisé. Notez que les valeurs d'en-tête précédemment définies ne seront pas visibles.

![L'option permettant de modifier les informations d'identification.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## Liste d’adresses IP autorisées pour le contenu connecté

Lorsqu’un message utilisant le Contenu connecté est envoyé par Braze, les serveurs Braze font automatiquement des requêtes réseau aux serveurs de nos clients ou tiers pour extraire des données. Grâce à l'IP allowlisting, vous pouvez vérifier que les demandes de contenu connecté proviennent bien de Braze, ce qui ajoute une couche de sécurité.

Braze envoie des demandes de Contenu connecté à partir des plages IP suivantes. Les plages répertoriées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont fait l'objet d'un abonnement à la liste d'autorisation. 

Braze dispose d’un ensemble d’IP réservé pour tous les services, qui ne sont pas tous actifs à un moment donné. Ce système est conçu pour permettre à Braze d'envoyer des données à partir d'un autre centre de données ou d'effectuer des travaux de maintenance, si nécessaire, sans que les clients ne soient affectés. Braze peut utiliser un IP, un sous-ensemble d’IP ou tous les IP suivants répertoriés lors de la création de requêtes de contenu connecté.

{% multi_lang_include data_centers.md datacenters='ips' %}

### `User-Agent` en-tête

Braze inclut un en-tête `User-Agent` dans toutes les demandes de contenu connecté et de webhook qui est similaire à ce qui suit :

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
N'oubliez pas que la valeur de hachage change régulièrement. Si vous filtrez le trafic par `User-Agent`, autorisez toutes les valeurs commençant par `Braze Sender`.
{% endalert %}

## Résolution des problèmes

Utilisez [Webhook.site](https://webhook.site/) pour résoudre les problèmes liés à vos appels au contenu connecté. 

1. Changez l’URL de votre appel de contenu connecté avec l’URL unique générée sur le site.
2. Prévisualisez et testez votre campagne ou votre étape Canvas pour voir les requêtes arriver sur ce site Internet.

À l’aide de cet outil, vous pouvez diagnostiquer les problèmes avec les en-têtes et le corps des requêtes, ainsi que d’autres informations envoyées lors de l’appel.

## Foire aux questions

### Pourquoi y a-t-il plus d'appels au contenu connecté que d'utilisateurs ou d'envois ? 

Braze peut effectuer le même appel à l'API du contenu connecté plus d'une fois par destinataire, car nous pouvons avoir besoin d'effectuer un appel à l'API du contenu connecté pour rendre l'envoi d'un message. Les messages peuvent être affichés plusieurs fois par destinataire à des fins de validation, de relance ou à d'autres fins internes.

Il est prévu qu'un appel à l'API Contenu connecté puisse être effectué plus d'une fois par destinataire, même si la logique de relance n'est pas utilisée dans l'appel. Nous vous recommandons de fixer la limite de débit de tout message contenant du contenu connecté ou de configurer vos serveurs de manière à ce qu'ils soient mieux à même de gérer le volume attendu.

### Comment la limite débit fonctionne-t-elle avec le contenu connecté ?

Le contenu connecté n'a pas de limite de débit propre. Au lieu de cela, la limite de débit est basée sur le taux d'envoi des messages. Nous vous recommandons de fixer la limite de débit des messages à un niveau inférieur à la limite de débit prévue pour le contenu connecté s'il y a plus d'appels au contenu connecté que de messages envoyés.  

### Qu'est-ce que la mise en cache ?

Par défaut, les requêtes POST ne sont pas mises en cache. Cependant, vous pouvez ajouter le paramètre `:cache_max_age` pour forcer l'appel POST à la mise en cache.

La mise en cache peut contribuer à réduire les appels au contenu connecté en double. Cependant, il n'est pas garanti qu'il en résulte toujours un seul appel au contenu connecté par utilisateur.

### Quel est le comportement par défaut de Connected Content HTTP ? 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}
