---
nav_title: Mise en cache des réponses
article_title: Mettre en cache les réponses de contenu connecté
page_order: 2.5
description: "Cet article explique comment mettre en cache les réponses de contenu connecté entre différentes campagnes ou messages dans le même espace de travail afin d'optimiser les vitesses d'envoi."
---

# Mettre en cache les réponses de contenu connecté

> Les réponses au contenu connecté peuvent être mises en cache dans différentes campagnes ou messages (dans le même espace de travail) afin d'optimiser les vitesses d'envoi.

Braze n'enregistre ni ne stocke de manière permanente **les corps de réponse** du contenu connecté. Lors du rendu des messages, les réponses peuvent être conservées temporairement (par exemple, en mémoire et dans le cache) afin que Braze puisse effectuer le rendu Liquid et envoyer le message.

Pour empêcher la mise en cache, vous pouvez spécifier `:no_cache`, ce qui peut entraîner une augmentation du trafic réseau. Afin de faciliter la résolution des problèmes et la surveillance de l'état du système, Braze enregistre les métadonnées des requêtes de contenu connecté (telles que l'URL de la requête entièrement rendue et le code d'état de la réponse) pour les appels réussis et échoués. Ces journaux sont conservés jusqu'à 30 jours.

{% details Rendu du contenu connecté et traitement des données (avancé) %}
Cette section fournit une vue d'ensemble plus détaillée sur la manière dont Braze effectue le rendu Liquid et du contenu connecté, ainsi que sur les emplacements où les données peuvent exister temporairement avant l'envoi d'un message. Cela peut être utile pour les évaluations en matière de confidentialité et de traitement des données.

#### Ce qui est et ce qui n'est pas stocké

- **Corps de la réponse du contenu connecté :** Non stocké de manière permanente par Braze. Il peut être conservé temporairement en mémoire et, lorsque la mise en cache est activée, stocké dans le cache avec une durée de vie (TTL).
- **Métadonnées de requête du contenu connecté :** Les métadonnées de requête, telles que l'URL entièrement rendue, le code d'état HTTP et la durée de réponse, sont enregistrées à des fins de résolution des problèmes et de surveillance. Ces journaux sont conservés jusqu'à 30 jours. 
- **Message final rendu :** Existe en mémoire pendant le rendu. Il peut également être stocké ailleurs en fonction de votre configuration et de votre canal (par exemple, l'archivage des messages ou les Cartes de contenu).

#### Flux de rendu (vue d'ensemble)

Le flux suivant décrit comment Braze effectue le rendu et envoie des messages pour les canaux basés sur des fournisseurs tels que les e-mails, les SMS et les notifications push. Les canaux fournis par le SDK, tels que les Cartes de contenu, utilisent le même rendu Liquid et contenu connecté sous-jacent, mais diffèrent quant au moment où le contenu est généré et à la manière dont il est distribué.

1. Un processus d'arrière-plan effectue le rendu du modèle Liquid pour un message lorsque celui-ci est prêt à être envoyé.
2. Les étiquettes de contenu connecté sont évaluées lors du rendu Liquid.
3. Pour chaque étiquette de contenu connecté, Braze vérifie un cache à plusieurs niveaux. Si aucune valeur mise en cache n'existe (ou si la mise en cache est désactivée), Braze contacte votre endpoint et reçoit la réponse.
4. La réponse est intégrée au modèle Liquid et le message est entièrement rendu.
5. Pour les canaux basés sur un fournisseur, le message rendu est envoyé au fournisseur du canal, puis à l'utilisateur. Pour les canaux fournis par le SDK, tels que les Cartes de contenu, le contenu rendu est synchronisé avec le SDK Braze et peut être généré lors de la première impression ou au moment de l'affichage, moment auquel il est présenté à l'utilisateur.

#### Où les réponses au contenu connecté peuvent résider temporairement

Braze utilise un cache à plusieurs niveaux pour les réponses de contenu connecté avec des TTL compris entre cinq minutes et quatre heures, en fonction de votre utilisation de `:cache_max_age` et d'autres règles de mise en cache :

- **Cache mémoire en cours de traitement :** Cache temporaire au sein du processus de travail. Les données ne peuvent exister que pendant la durée de la tâche (jusqu'à environ 11 minutes, en fonction du délai d'expiration du processus).
- **Cache de la machine locale :** Un cache par processus, tel qu'une instance Memcached locale.
- **Cache à l'échelle du cluster :** Cache distribué partagé entre les processus, tel qu'un cluster Memcached.

Ces couches de cache sont volatiles et peuvent supprimer des données avant l'expiration du TTL configuré.

#### Ce qui change lorsque vous utilisez `:no_cache`

Pour les endpoints qui ne sont pas hébergés au sein de l'infrastructure Braze, l'utilisation de `:no_cache` empêche le corps de réponse du contenu connecté d'être stocké dans Memcached. Dans ces cas, la réponse réside uniquement dans la mémoire du processus de travail pendant la durée du travail de rendu (jusqu'à environ 11 minutes). Pour les endpoints qui renvoient vers des hôtes internes à Braze, les réponses peuvent toujours être mises en cache, comme décrit dans la section [Vider le cache](#cache-busting).

#### Où le résultat final rendu peut résider

- **Archivage des messages :** Si l'archivage des messages est activé, Braze peut enregistrer le message final rendu dans votre compartiment de stockage cloud configuré. Si votre réponse au contenu connecté est incluse dans le message rendu, elle sera également incluse dans la copie archivée.
- **Appareils des utilisateurs :** Après la distribution, le contenu complet du message rendu peut persister sur les appareils des utilisateurs pendant une durée indéterminée.
- **Cartes de contenu :** Le contenu rendu pour les Cartes de contenu est stocké dans une base de données Braze jusqu'à l'expiration de la carte.
{% enddetails %}

## Paramètres de cache par défaut

La durée du cache peut aller jusqu'à cinq minutes (300 secondes). Vous pouvez la modifier en ajoutant le paramètre `:cache_max_age` à l'appel de contenu connecté. Voici un exemple :

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

Les requêtes GET sont mises en cache. Vous pouvez configurer ce comportement en ajoutant le paramètre `:no_cache` à l'appel de contenu connecté.

Les requêtes POST ne sont pas mises en cache par défaut, mais peuvent l'être en ajoutant le paramètre `:cache_max_age` à l'appel de contenu connecté. La durée minimale du cache est de 5 minutes et la durée maximale de 4 heures.

{% alert note %}
Les paramètres du cache ne sont pas garantis. La mise en cache peut réduire les appels à vos endpoints, c'est pourquoi nous vous recommandons d'effectuer plusieurs appels par endpoint pendant la durée de la mise en cache plutôt que de dépendre excessivement de la mise en cache.
{% endalert %}

### Limite de la taille du cache

Le corps de la réponse au contenu connecté peut atteindre 1&nbsp;Mo. Si le corps de la réponse dépasse 1&nbsp;Mo, il ne sera pas mis en cache.

## Durée du cache 

Le contenu connecté met en cache la valeur renvoyée par les endpoints GET pendant au moins cinq minutes. Si aucune durée de cache n'est spécifiée, la durée par défaut est de cinq minutes.

La durée de mise en cache du contenu connecté peut être allongée avec `:cache_max_age`, comme illustré dans l'exemple suivant. La durée minimale du cache est de cinq minutes et la durée maximale de quatre heures. Les données de contenu connecté sont mises en cache en mémoire à l'aide d'un système de cache volatil, tel que Memcached. 

Par conséquent, quelle que soit la durée de mise en cache spécifiée, les données de contenu connecté peuvent être supprimées du cache en mémoire de Braze plus tôt que prévu. Cela signifie que les durées de cache sont indicatives et ne représentent pas nécessairement la durée pendant laquelle les données sont effectivement conservées en cache par Braze. Vous pourriez donc observer davantage de requêtes de contenu connecté que prévu pour une durée de cache donnée.

### Cache pour une durée spécifiée en secondes

Cet exemple met en cache pendant 900 secondes (soit 15 minutes).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Vider le cache

Pour empêcher le contenu connecté de mettre en cache la valeur renvoyée par une requête GET, vous pouvez utiliser la configuration `:no_cache`. Toutefois, les réponses provenant d'hôtes internes à Braze seront toujours mises en cache.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Assurez-vous que l'endpoint de contenu connecté fourni peut gérer de grandes quantités de trafic avant d'utiliser cette option, sinon vous constaterez probablement une latence d'envoi accrue (des délais plus importants ou des intervalles de temps plus longs entre la requête et la réponse) du fait que Braze effectue des requêtes de contenu connecté pour chaque message.
{% endalert %}

Avec une requête POST, il n'est pas nécessaire de vider le cache, car les requêtes POST ne sont pas mises en cache par défaut. Pour mettre en cache une réponse POST, ajoutez `:cache_max_age` ; pour éviter la mise en cache d'une requête POST, omettez simplement `:cache_max_age`.

## Bon à savoir

- La mise en cache peut contribuer à réduire les appels de contenu connecté en double. Cependant, il n'est pas garanti qu'elle aboutisse systématiquement à un seul appel de contenu connecté par utilisateur.
- La mise en cache du contenu connecté est basée sur l'URL et l'espace de travail. Si l'appel de contenu connecté pointe vers une URL identique, il peut être mis en cache à travers les campagnes et les Canvas.
- Le cache est basé sur une URL unique, et non sur un ID utilisateur ou une campagne. Cela signifie que la version mise en cache d'un appel de contenu connecté peut être utilisée par plusieurs utilisateurs et campagnes dans un espace de travail si l'URL est la même.