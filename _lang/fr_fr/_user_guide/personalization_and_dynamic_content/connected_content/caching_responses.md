---
nav_title: Mise en cache des réponses
article_title: Mise en cache des réponses au contenu connecté
page_order: 2.5
description: "Cet article explique comment mettre en cache les réponses de contenu connecté entre différentes campagnes ou messages dans le même espace de travail afin d'optimiser les vitesses d'envoi."
---

# Mise en cache des réponses du contenu connecté

> Les réponses au contenu connecté peuvent être mises en cache dans différentes campagnes ou messages (dans le même espace de travail) afin d'optimiser les vitesses d'envoi.

Braze n'enregistre ni ne stocke en permanence les réponses au contenu connecté. Si vous choisissez explicitement de stocker une réponse à un appel de contenu connecté en tant que variable Liquid, Braze ne la stocke qu'en mémoire, c'est-à-dire sur un stockage temporaire qui est supprimé après un court laps de temps, pour effectuer le rendu de la variable Liquid et envoyer le message.

Pour empêcher la mise en cache, vous pouvez spécifier `:no_cache`, ce qui peut entraîner une augmentation du trafic réseau. Pour faciliter la résolution des problèmes et le suivi de l'état du système, Braze peut également enregistrer les appels au contenu connecté qui échouent (tels que `404` et `429`). Ces journaux sont conservés jusqu'à 30 jours.

## Paramètres de cache par défaut

L'âge du cache peut aller jusqu'à cinq minutes (300 secondes). Vous pouvez le mettre à jour en ajoutant le paramètre `:cache_max_age` à l'appel de contenu connecté. En voici un exemple :

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

## Temps de cache 

Le contenu connecté met en cache la valeur renvoyée par les endpoints GET pendant au moins cinq minutes. Si aucune durée de cache n'est spécifiée, la durée de cache par défaut est de cinq minutes.

Le temps de cache du contenu connecté peut être configuré pour être plus long avec :cache_max_age, comme le montre l'exemple suivant. La durée minimale du cache est de cinq minutes et la durée maximale de quatre heures. Les données du contenu connecté sont mises en cache en mémoire à l'aide d'un système de cache volatile, tel que Memcached. 

Par conséquent, quelle que soit la durée de mise en cache spécifiée, les données de contenu connecté peuvent être expulsées du cache en mémoire de Braze plus tôt que prévu. Cela signifie que les durées de cache sont des suggestions et peuvent ne pas représenter réellement la durée pendant laquelle les données sont garanties d'être mises en cache par Braze, et vous pouvez voir plus de demandes de contenu connecté que ce à quoi vous vous attendez avec une durée de cache donnée.

### Cache pour les secondes spécifiées

Dans cet exemple, la durée de la mise en cache est de 900 secondes (ou 15 minutes).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Cache busting

Pour empêcher le contenu connecté de mettre en cache la valeur qu'il renvoie à partir d'une requête GET, vous pouvez utiliser la configuration `:no_cache`. Toutefois, les réponses provenant d'hôtes internes à Braze seront toujours mises en cache.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Assurez-vous que l'endpoint de contenu connecté fourni peut gérer d'importants flux de trafic avant d'utiliser cette option, sinon vous constaterez probablement une augmentation de la latence d'envoi (délais accrus ou intervalles de temps plus longs entre la demande et la réponse) due au fait que Braze effectue des requêtes de contenu connecté pour chaque message.
{% endalert %}

Avec un POST, vous n'avez pas besoin de mettre le buste en cache, car Braze ne met jamais en cache les résultats des requêtes POST.

## Ce qu'il faut savoir

- La mise en cache peut contribuer à réduire les appels au contenu connecté en double. Cependant, il n'est pas garanti qu'il en résulte toujours un seul appel au contenu connecté par utilisateur.
- La mise en cache du contenu connecté est basée sur l'URL et l'espace de travail. Si l'appel au contenu connecté se fait vers l'URL identique, il peut être mis en cache à travers les campagnes et les Canvas.
- Le cache est basé sur une URL unique, et non sur un ID d'utilisateur ou une campagne. Cela signifie que la version mise en cache d'un appel au contenu connecté peut être utilisée par plusieurs utilisateurs et campagnes dans un espace de travail si l'URL est la même.
