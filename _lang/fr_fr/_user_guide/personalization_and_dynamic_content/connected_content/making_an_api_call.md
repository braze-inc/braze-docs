---
nav_title: Faire un appel au contenu connecté
article_title: Création d'un appel API de contenu connecté
page_order: 0
description: "Le présent article de référence explique comment effectuer un appel API de contenu connecté, ainsi que des exemples utiles et des scénarios d'utilisation de contenu connecté avancés."
search_rank: 2
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} Faire un appel à l'API de contenu connecté

> Utilisez le contenu connecté pour insérer toute information accessible par API directement dans les messages que vous envoyez aux utilisateurs. Vous pouvez extraire du contenu directement à partir de votre serveur Web ou des API accessibles au public.<br><br>Cette page explique comment effectuer des appels à l'API du contenu connecté, les cas d'utilisation avancés du contenu connecté, la gestion des erreurs, etc.

## Comprendre le volume d'appels du contenu connecté

{% alert important %}
Un envoi ne correspond pas à un appel de contenu connecté. Braze ne garantit pas un ratio 1:1 entre les envois de messages et les requêtes de contenu connecté. Le système est conçu pour privilégier le rendu et la distribution corrects des messages plutôt que la minimisation du nombre d'appels. Vos endpoints doivent être dimensionnés pour gérer davantage de requêtes que le nombre de destinataires ou de messages envoyés.
{% endalert %}

Braze peut effectuer le même appel à l'API du contenu connecté plus d'une fois par destinataire. Les raisons courantes sont les suivantes :

- **E-mail avec plusieurs parties :** Un seul e-mail peut déclencher des passes de rendu distinctes pour le corps HTML, le corps en texte brut et la version pages mobiles accélérées (AMP) (le cas échéant). Chaque passe peut déclencher le contenu connecté dans cette partie, de sorte qu'un seul destinataire peut générer plusieurs appels identiques ou similaires.
- **Validation et nouvelles tentatives :** Les charges utiles de messages peuvent être rendues plusieurs fois par destinataire à des fins de validation, de logique de nouvelle tentative ou d'autres traitements internes.
- **Comportement selon le canal :** Le contenu connecté s'exécute lorsque le message est rendu. Pour les messages in-app, le message est rendu au moment de l'impression.

Si vous constatez dans vos journaux plus d'appels de contenu connecté que d'envois ou de destinataires, ce comportement est attendu. Pour des conseils sur la réduction de la charge et la planification de la montée en charge, consultez [Bonnes pratiques pour les endpoints à fort volume](#best-practices-for-high-volume-endpoints).

## Envoi d'un appel de contenu connecté

{% raw %}

Pour envoyer un appel de contenu connecté, utilisez la balise `{% connected_content %}`. Cette balise vous permet d'attribuer et de déclarer des variables en utilisant `:save`. Certains aspects de ces variables peuvent être référencés plus loin dans le message avec [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

Par exemple, le corps de message suivant va accéder à l'URL `http://numbersapi.com/random/trivia` et inclure une anecdote amusante dans votre message :

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Ajouter des variables

Vous pouvez également inclure des attributs de profil utilisateur comme variables dans la chaîne de caractères d'URL lors de la création de requêtes de contenu connecté. 

Par exemple, vous pouvez disposer d'un service Web qui renvoie du contenu en fonction de l'adresse e-mail et de l'ID d'un utilisateur. Si vous transmettez des attributs contenant des caractères spéciaux, tels que le signe (@), assurez-vous d'utiliser le filtre Liquid `url_param_escape` pour remplacer les caractères non autorisés dans les URL par leurs versions d'échappement compatibles avec les URL, comme indiqué dans l'attribut d'adresse e-mail suivant.

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

Si l'URL n'est pas disponible et qu'elle atteint une page 404, Braze renvoie une chaîne de caractères vide à sa place. Si l'URL atteint une page HTTP 500 ou 502, l'URL échouera dans la logique de nouvelle tentative.

Si l'endpoint renvoie du JSON, vous pouvez le détecter en vérifiant si la valeur de `connected` est nulle, puis [abandonner le message sous condition]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). Braze autorise uniquement les URL qui communiquent sur le port 80 (HTTP) et 443 (HTTPS).

### Détection d'un hôte défaillant

Le contenu connecté utilise un mécanisme de détection d'hôte défaillant pour détecter lorsque l'hôte cible connaît un taux élevé de lenteur significative ou de surcharge, ce qui se traduit par des dépassements de délai, un trop grand nombre de requêtes ou d'autres résultats qui empêchent Braze de communiquer avec succès avec l'endpoint cible. Il agit comme un garde-fou pour réduire la charge inutile qui pourrait être à l'origine des difficultés de l'hôte cible. Il sert également à stabiliser l'infrastructure de Braze et à maintenir des vitesses d'envoi de messages rapides.

Si l'hôte cible connaît un taux élevé de lenteur significative ou de surcharge, Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute, en simulant à la place des réponses indiquant la défaillance. Au bout d'une minute, Braze vérifie l'état de santé de l'hôte à l'aide d'un petit nombre de requêtes avant de reprendre les requêtes à pleine vitesse si l'hôte s'avère sain. Si l'hôte est toujours défaillant, Braze attendra encore une minute avant de réessayer.

Si les requêtes adressées à l'hôte cible sont interrompues par le détecteur d'hôte défaillant, Braze continuera de rendre les messages et de suivre votre logique Liquid comme s'il avait reçu un code de réponse d'erreur. Si vous voulez vous assurer que ces requêtes de contenu connecté sont relancées lorsqu'elles sont interrompues par le détecteur d'hôte défaillant, utilisez l'option `:retry`. Pour plus d'informations sur l'option `:retry`, reportez-vous à la section [Nouvelles tentatives de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Si vous pensez que la détection d'hôte défaillant peut être à l'origine de problèmes, contactez l'[assistance Braze]({{site.baseurl}}/support_contact/).

{% alert note %}
Vous pouvez ajouter des URL spécifiques à une liste d'autorisation pour le contenu connecté. Pour accéder à cette fonctionnalité, contactez votre Customer Success Manager.
{% endalert %}

{% alert tip %}
Consultez la page [Résolution des problèmes des requêtes de webhook et de contenu connecté]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) pour en savoir plus sur la manière de résoudre les codes d'erreur courants.
{% endalert %}

### Limites de débit (429) et détection d'hôte défaillant

Il s'agit de mécanismes différents :

- **429 Too Many Requests :** Votre endpoint (ou un service en amont) renvoie cette réponse. Cela signifie que votre serveur ou middleware refuse le trafic, souvent parce qu'il possède sa propre limite de débit. Braze n'applique pas de limite de débit distincte au contenu connecté ; le volume de requêtes de contenu connecté évolue directement avec votre [limite de débit de vitesse de distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). Étant donné que les messages peuvent être rendus plusieurs fois par destinataire (par exemple, pour le HTML de l'e-mail, le texte brut et l'AMP), le nombre de requêtes de contenu connecté peut dépasser cette limite de débit — ne supposez pas qu'il sera inférieur ou égal au nombre de messages par minute que vous avez défini. Si vous constatez des erreurs 429, dimensionnez votre endpoint ou middleware pour gérer le volume de requêtes attendu, ou réduisez la limite de débit de la campagne ou de l'étape du canvas afin que moins de messages (et donc moins d'appels de contenu connecté) soient envoyés par minute.
- **Détection d'hôte défaillant :** Un mécanisme de protection côté Braze qui se déclenche après un taux et un volume élevés d'*échecs* dans une fenêtre d'une minute. Le décompte des échecs inclut les codes de statut `408`, `429`, `502`, `503`, `504` et `529`. Lorsqu'il est déclenché, Braze interrompt temporairement les requêtes vers cet hôte et simule une réponse d'échec. Ce mécanisme est indépendant de votre propre limitation de débit. Pour les seuils de détection et plus de détails, consultez [Résolution des problèmes des requêtes de webhook et de contenu connecté]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/#unhealthy-host-detection). Pour éviter de déclencher la détection d'hôte défaillant, assurez-vous que votre endpoint peut gérer le volume d'appels décrit dans [Comprendre le volume d'appels du contenu connecté](#understanding-connected-content-call-volume) et [Bonnes pratiques pour les endpoints à fort volume](#best-practices-for-high-volume-endpoints).

## Permettre des performances efficaces

Comme Braze envoie les messages à un rythme très rapide, assurez-vous que votre serveur peut gérer des milliers de connexions simultanées afin qu'il ne soit pas surchargé lors de l'extraction du contenu. Lorsque vous utilisez des API publiques, assurez-vous que votre utilisation n'enfreindra pas les limites de débit que le fournisseur de l'API peut appliquer. Braze exige que le temps de réponse du serveur soit inférieur à deux secondes pour des raisons de performances ; si le serveur met plus de deux secondes à répondre, le contenu ne sera pas inséré.

Pour en savoir plus sur la planification de la capacité des endpoints et la réduction du volume d'appels, consultez [Bonnes pratiques pour les endpoints à fort volume](#best-practices-for-high-volume-endpoints).

## Bon à savoir

* Braze ne facture pas les appels à l'API et ceux-ci ne sont pas pris en compte dans votre consommation de points de donnée.
* Les réponses du contenu connecté sont limitées à 1 Mo.
* Le contenu connecté s'exécute lorsque le message est rendu. Pour les messages in-app, le message est rendu au moment de l'impression.
* Les appels de contenu connecté ne suivent pas les redirections.

## Bonnes pratiques pour les endpoints à fort volume

Si vos messages utilisent du contenu connecté et que vous envoyez à fort volume, prévoyez davantage de requêtes que le nombre de destinataires ou d'envois :

1. **Estimez la charge de pointe :** Utilisez un multiplicateur conservateur lors du dimensionnement de votre endpoint ou middleware — les requêtes de contenu connecté peuvent dépasser le nombre de destinataires ou de messages envoyés. Par exemple, pour l'e-mail, un seul destinataire peut générer plusieurs appels (HTML, texte brut et AMP), donc destinataires × 2 ou × 3 est souvent utilisé comme estimation prudente.
2. **Utilisez la mise en cache lorsque c'est pertinent :** Les requêtes GET sont mises en cache par défaut. Pour les requêtes POST, ajoutez `:cache_max_age` lorsque la réponse peut être réutilisée pendant une période (par exemple, un jeton ou un contenu qui ne change pas à chaque requête). Consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/) et la [FAQ sur la mise en cache POST](#what-is-caching-behavior) ci-dessous.
3. **Définissez une limite de débit de vitesse de distribution :** La [limite de débit de vitesse de distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) sur les campagnes ou les étapes du canvas est le seul levier pour limiter indirectement le volume de requêtes de contenu connecté — Braze ne limite pas le débit du contenu connecté lui-même. Ce n'est qu'un indicateur indirect, et non un contrôle parfait, car les requêtes de contenu connecté ne sont pas en ratio 1:1 avec les messages. Utilisez-le pour maintenir le volume de messages (et donc de contenu connecté) dans les limites de ce que votre endpoint peut gérer.
4. **Concevez pour l'idempotence et les nouvelles tentatives :** Braze peut appeler votre endpoint plus d'une fois par destinataire. Assurez-vous que votre endpoint peut tolérer des requêtes en double sans effets secondaires indésirables.

## Types d'authentification

### Utilisation de l'authentification de base

Si l'URL requiert une authentification de base, Braze peut stocker un identifiant d'authentification de base que vous pourrez utiliser dans votre appel API. Vous pouvez gérer les identifiants d'authentification de base existants et en ajouter de nouveaux dans **Paramètres** > **Contenu connecté**.

![Les paramètres du contenu connecté dans le tableau de bord de Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Pour ajouter un nouvel identifiant, sélectionnez **Ajouter un identifiant** > **Authentification de base**. 

![Menu déroulant « Ajouter un identifiant » avec l'option d'utiliser l'authentification de base ou l'authentification par jeton.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Nommez votre identifiant et saisissez le nom d'utilisateur et le mot de passe.

![La fenêtre « Créer un nouvel identifiant » avec la possibilité de saisir un nom, un nom d'utilisateur et un mot de passe.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Vous pouvez alors utiliser cet identifiant d'authentification de base dans vos appels API en faisant référence au nom du jeton :

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si vous supprimez un identifiant, gardez à l'esprit que tout appel de contenu connecté qui essaie de l'utiliser sera abandonné.
{% endalert %}

### Utilisation de l'authentification par jeton

Lorsque vous utilisez le contenu connecté de Braze, vous pouvez constater que certaines API nécessitent un jeton au lieu d'un nom d'utilisateur et d'un mot de passe. Braze peut également stocker des identifiants contenant des valeurs d'en-tête d'authentification par jeton.

Pour ajouter un identifiant contenant des valeurs de jeton, sélectionnez **Ajouter un identifiant** > **Authentification par jeton**. Ensuite, ajoutez les paires clé-valeur pour vos en-têtes d'appel API et le domaine autorisé.

![Un exemple de jeton « token_credential_abc » avec les détails de l'authentification par jeton.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Vous pouvez ensuite utiliser cet identifiant dans vos appels API en faisant référence au nom de l'identifiant :

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

### Utilisation de l'authentification ouverte (OAuth)

Certaines configurations d'API nécessitent la récupération d'un jeton d'accès qui peut ensuite être utilisé pour authentifier l'endpoint de l'API auquel vous souhaitez accéder.

#### Étape 1 : Récupérer le jeton d'accès

L'exemple suivant illustre la récupération et l'enregistrement d'un jeton d'accès dans une variable locale, qui peut ensuite être utilisée pour authentifier l'appel API suivant. Un paramètre `:cache_max_age` peut être ajouté pour correspondre à la durée de validité du jeton d'accès et réduire le nombre d'appels de contenu connecté sortants. Pour plus d'informations, reportez-vous à la rubrique [Mise en cache configurable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching).

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

#### Étape 2 : Autoriser l'API à l'aide du jeton d'accès récupéré

Une fois le jeton enregistré, il peut être intégré de manière dynamique dans l'appel au contenu connecté suivant afin d'autoriser la requête :

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

### Modifier les identifiants

Vous pouvez modifier le nom de l'identifiant pour les types d'authentification.

- Pour l'authentification de base, vous pouvez mettre à jour le nom d'utilisateur et le mot de passe. Notez que le mot de passe précédemment saisi ne sera pas visible.
- Pour l'authentification par jeton, vous pouvez mettre à jour les paires clé-valeur de l'en-tête et le domaine autorisé. Notez que les valeurs d'en-tête précédemment définies ne seront pas visibles.

![L'option permettant de modifier les identifiants.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## Liste d'adresses IP autorisées pour le contenu connecté

Lorsqu'un message utilisant le contenu connecté est envoyé par Braze, les serveurs Braze effectuent automatiquement des requêtes réseau vers les serveurs de nos clients ou de tiers pour extraire des données. Grâce à la liste d'autorisation d'IP, vous pouvez vérifier que les requêtes de contenu connecté proviennent bien de Braze, ce qui ajoute une couche de sécurité.

Braze envoie des requêtes de contenu connecté à partir des plages d'IP suivantes. Les plages répertoriées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont fait l'objet d'un abonnement à la liste d'autorisation. 

Braze dispose d'un ensemble d'IP réservé pour tous les services, qui ne sont pas tous actifs à un moment donné. Ce système est conçu pour permettre à Braze d'envoyer des données à partir d'un autre centre de données ou d'effectuer des travaux de maintenance, si nécessaire, sans impact pour les clients. Braze peut utiliser une, un sous-ensemble ou toutes les IP suivantes répertoriées lors de la création de requêtes de contenu connecté.

{% multi_lang_include data_centers.md datacenters='ips' %}

### En-tête `User-Agent`

Braze inclut un en-tête `User-Agent` dans toutes les requêtes de contenu connecté et de webhook, similaire à ce qui suit :

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
N'oubliez pas que la valeur de hachage change régulièrement. Si vous filtrez le trafic par `User-Agent`, autorisez toutes les valeurs commençant par `Braze Sender`.
{% endalert %}

## Résolution des problèmes

Utilisez [Webhook.site](https://webhook.site/) pour résoudre les problèmes liés à vos appels de contenu connecté. 

1. Remplacez l'URL de votre appel de contenu connecté par l'URL unique générée sur le site.
2. Prévisualisez et testez votre campagne ou votre étape du canvas pour voir les requêtes arriver sur ce site.

À l'aide de cet outil, vous pouvez diagnostiquer les problèmes liés aux en-têtes et au corps des requêtes, ainsi qu'aux autres informations envoyées lors de l'appel.

## Foire aux questions

### Pourquoi y a-t-il plus d'appels de contenu connecté que d'utilisateurs ou d'envois ? 

Ce comportement est attendu. Braze peut effectuer le même appel à l'API du contenu connecté plus d'une fois par destinataire, car les charges utiles de messages peuvent être rendues plusieurs fois (par exemple, pour le HTML de l'e-mail, le texte brut et l'AMP ; pour la validation ou la logique de nouvelle tentative ; ou pour d'autres traitements internes). Il n'y a pas de ratio garanti 1:1 entre les envois et les appels de contenu connecté. Consultez [Comprendre le volume d'appels du contenu connecté](#understanding-connected-content-call-volume) et [Bonnes pratiques pour les endpoints à fort volume](#best-practices-for-high-volume-endpoints) pour plus de détails et des pistes d'atténuation.

### Comment la limite de débit fonctionne-t-elle avec le contenu connecté ?

Le contenu connecté n'a pas de limite de débit propre. La limite de débit repose sur le taux d'envoi des messages. Nous vous recommandons de fixer la limite de débit des messages à un niveau inférieur à la limite de débit prévue pour le contenu connecté s'il y a plus d'appels de contenu connecté que de messages envoyés.  

### Quel est le comportement de mise en cache ?

Les requêtes GET sont mises en cache par défaut (voir [Mise en cache des réponses]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/)). **Les requêtes POST ne sont pas mises en cache par défaut**, mais vous pouvez activer la mise en cache en ajoutant `:cache_max_age` à l'appel de contenu connecté. Cela peut réduire la charge sur l'endpoint lorsque la même requête POST (par exemple, une requête de jeton ou de contenu) serait effectuée de manière répétée dans la fenêtre de cache.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

La mise en cache peut contribuer à réduire les appels de contenu connecté en double, mais il n'est pas garanti qu'il en résulte un seul appel par utilisateur. La durée du cache est comprise entre cinq minutes et quatre heures. Pour tous les détails, consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/).

### Quel est le comportement HTTP par défaut du contenu connecté ? 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}