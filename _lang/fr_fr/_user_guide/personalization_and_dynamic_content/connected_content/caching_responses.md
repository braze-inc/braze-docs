---
nav_title: Mise en cache des réponses
article_title: Mise en cache des réponses au contenu connecté
page_order: 2.5
description: "Cet article explique comment mettre en cache les réponses de contenu connecté entre différentes campagnes ou messages dans le même espace de travail afin d'optimiser les vitesses d'envoi."
---

# Mettre en cache les réponses du contenu connecté

> Les réponses au contenu connecté peuvent être mises en cache dans différentes campagnes ou messages (dans le même espace de travail) afin d'optimiser les vitesses d'envoi.

Braze n'enregistre ni ne stocke en permanence les **corps de réponse du** contenu connecté. Pendant l'envoi des messages, les réponses peuvent être conservées temporairement (par exemple, en mémoire et en cache) afin que Braze puisse effectuer le rendu de Liquid et envoyer le message.

Pour empêcher la mise en cache, vous pouvez spécifier `:no_cache`, ce qui peut entraîner une augmentation du trafic réseau. Pour faciliter le dépannage et le contrôle de l'état du système, Braze enregistre les métadonnées des requêtes de contenu connecté (telles que l'URL de la requête entièrement rendue et le code d'état de la réponse) pour les appels réussis et échoués. Ces journaux sont conservés jusqu'à 30 jours.

{% details Connected Content rendering and data handling (advanced) %}
Cette section offre une vue plus détaillée, de bout en bout, de la manière dont Braze rend le contenu liquide et connecté et de l'endroit où les données peuvent exister temporairement avant l'envoi d'un message. Cela peut faciliter l'examen de la confidentialité et du traitement des données.

#### Ce qui est stocké et ce qui ne l'est pas

- **Contenu connecté corps de la réponse :** Non stocké de manière permanente par Braze. Il peut être conservé temporairement en mémoire et, lorsque la mise en cache est activée, stocké dans le cache avec une durée de vie (TTL).
- **Métadonnées de la demande de contenu connecté :** Les métadonnées des requêtes, telles que l'URL entièrement rendu, le code d'état HTTP et la durée de la réponse, sont enregistrées à des fins de résolution des problèmes et de surveillance. Ces journaux sont conservés jusqu'à 30 jours. 
- **Message final envoyé :** Existe en mémoire pendant le rendu. Elle peut également être stockée ailleurs en fonction de votre configuration et de votre canal (par exemple, archivage des messages ou cartes de contenu).

#### Flux de rendu (haut niveau)

Le flux suivant décrit comment Braze rend et envoie les messages pour les canaux basés sur les fournisseurs, tels que l'e-mail, le SMS et le push. Les canaux fournis par le SDK, comme les cartes de contenu, utilisent le même rendu sous-jacent de Liquid et de contenu connecté, mais diffèrent quant au moment où le contenu est généré et à la manière dont il est fourni.

1. Un agent d'arrière-plan rend le modèle Liquid pour un message lorsque le message est prêt à être envoyé.
2. Les étiquettes de contenu connecté sont évaluées lors du rendu du Liquid.
3. Pour chaque étiquette de contenu connecté, Braze vérifie un cache à plusieurs niveaux. Si aucune valeur mise en cache n'existe (ou si la mise en cache est désactivée), Braze appelle votre endpoint et reçoit la réponse.
4. La réponse est injectée dans le modèle Liquid et le message est entièrement rendu.
5. Pour les canaux basés sur le fournisseur, le message rendu est envoyé au fournisseur du canal, puis à l'utilisateur. Pour les canaux fournis par le SDK, tels que les cartes de contenu, le contenu rendu est synchronisé avec le SDK de Braze et peut être généré à la première impression ou au moment de l'affichage, moment où il est montré à l'utilisateur.

#### Où les réponses au contenu connecté peuvent en ligne/en production/instantanée

Braze utilise un cache à plusieurs niveaux pour les réponses au contenu connecté avec des TTL compris entre cinq minutes et quatre heures, en fonction de votre utilisation de `:cache_max_age` et d'autres règles de mise en cache :

- **Cache mémoire en cours de traitement :** Cache transitoire au sein du processus de travail. Les données ne peuvent être en ligne/en production/instantanée que pendant la durée du travail (jusqu'à ~11 minutes en fonction du délai d'attente du travailleur).
- **Cache de la machine locale :** Un cache par travailleur, tel qu'une instance locale de Memcached.
- **Cache à l'échelle du cluster :** Un cache distribué et partagé entre les travailleurs, tel qu'un cluster Memcached.

Ces couches de cache sont volatiles et peuvent expulser des données avant le TTL configuré.

#### Qu'est-ce qui change lorsque vous utilisez `:no_cache`

Pour les endpoints qui ne sont pas hébergés dans l'infrastructure Braze, l'utilisation de `:no_cache` empêche le corps de la réponse Connected Content d'être stocké dans Memcached. Dans ce cas, la réponse ne reste en ligne/en production/instantanée dans la mémoire du processus de travail que pendant la durée du travail de rendu (jusqu'à ~11 minutes). Pour les endpoints qui se résolvent vers des hôtes internes à Braze, les réponses peuvent toujours être mises en cache comme décrit dans [Cache busting](#cache-busting).

#### Où la production/instantanée finale peut être hébergée

- **Archivage des messages :** Si l'archivage des messages est activé, Braze peut écrire le message rendu final dans votre compartiment de stockage en nuage configuré. Si votre réponse au contenu connecté est incluse dans l'envoi connecté, elle sera incluse dans la copie archivée.
- **Appareils de l'utilisateur :** Après réception/distribution, le contenu du message entièrement rendu peut persister sur les appareils des utilisateurs pendant une durée inconnue.
- **Cartes de contenu (Content cards) :** Le contenu rendu pour les cartes de contenu est stocké dans une base de données Braze jusqu'à l'expiration de la carte.
{% enddetails %}

## Paramètres de cache par défaut

L'âge du cache peut aller jusqu'à cinq minutes (300 secondes). Vous pouvez le mettre à jour en ajoutant le paramètre `:cache_max_age` à l'appel de contenu connecté. Voici un exemple :

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

Les demandes GET sont mises en cache. Vous pouvez configurer cela en ajoutant le paramètre :no_cache à l'appel de contenu connecté.

Les requêtes POST ne sont pas mises en cache. Vous pouvez l'imposer en ajoutant le paramètre :cache_max_age à l'appel de contenu connecté. La durée minimale du cache est de 5 minutes et la durée maximale de 4 heures.

{% alert note %}
Les paramètres du cache ne sont pas garantis. La mise en cache peut réduire les appels à vos endpoints, c'est pourquoi nous vous recommandons d'utiliser plusieurs appels par endpoint pendant la durée de la mise en cache plutôt que d'être trop dépendant de la mise en cache.
{% endalert %}

### Limite de la taille du cache

Le corps de la réponse au contenu connecté peut atteindre 1 Mo. Si le corps de la réponse est supérieur à 1 Mo, il ne sera pas mis en cache.

## Temps cache 

Le contenu connecté met en cache la valeur renvoyée par les endpoints GET pendant au moins cinq minutes. Si aucune durée de cache n'est spécifiée, la durée de cache par défaut est de cinq minutes.

Le temps de cache du contenu connecté peut être configuré pour être plus long avec :cache_max_age, comme le montre l'exemple suivant. La durée minimale du cache est de cinq minutes et la durée maximale de quatre heures. Les données de contenu connecté sont mises en cache en mémoire à l’aide d’un système de cache volatil, tel que Memcached. 

Par conséquent, quelle que soit la durée de mise en cache spécifiée, les données de contenu connecté peuvent être expulsées du cache en mémoire de Braze plus tôt que prévu. Cela signifie que les durées de cache sont des suggestions et qu’elles ne représentent pas réellement la durée pendant laquelle les données sont garanties à être mises en cache par Braze et que vous pouvez voir plus de requêtes de contenu connecté que vous ne pouvez attendre avec une durée de cache donnée.

### Cache pour les secondes spécifiées

Cet exemple se cache pendant 900 secondes (ou 15 minutes).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Mise en cache du cache

Pour empêcher le contenu connecté de mettre en cache la valeur qu’il renvoie à partir d’une demande GET, vous pouvez utiliser la configuration `:no_cache`. Toutefois, les réponses provenant d'hôtes internes à Braze seront toujours mises en cache.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Assurez-vous que l’endpoint de contenu connecté fourni peut gérer de grandes quantité de trafic avant d'utiliser cette option, ou vous verrez probablement une latence d'envoi accrue (des retards accrus ou des intervalles de temps plus longs entre la demande et la réponse) en raison du fait que Braze effectue des demandes de contenu connecté pour chaque message.
{% endalert %}

Avec un POST, vous n'avez pas besoin de mettre le buste en cache, car Braze ne met jamais en cache les résultats des requêtes POST.

## Choses à savoir

- La mise en cache peut contribuer à réduire les appels au contenu connecté en double. Cependant, il n'est pas garanti qu'il en résulte toujours un seul appel au contenu connecté par utilisateur.
- La mise en cache du contenu connecté est basée sur l'URL et l'espace de travail. Si l'appel au contenu connecté se fait vers l'URL identique, il peut être mis en cache à travers les campagnes et les Canvas.
- Le cache est basé sur une URL unique, et non sur un ID d'utilisateur ou une campagne. Cela signifie que la version mise en cache d'un appel au contenu connecté peut être utilisée par plusieurs utilisateurs et campagnes dans un espace de travail si l'URL est la même.
