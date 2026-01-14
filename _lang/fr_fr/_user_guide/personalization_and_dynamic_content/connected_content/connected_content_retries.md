---
nav_title: Connecté Tentatives de contenu connecté
article_title: Répétitions du contenu connecté
page_order: 5
description: "Cet article de référence explique comment traiter les tentatives de relance du contenu connecté."

---

# Utilisation de la logique de relance pour le contenu connecté

> Cette page explique comment ajouter des tentatives à vos appels de contenu connecté.

## Fonctionnement des tentatives 

Le contenu connecté reposant sur la réception de données provenant d'API, une API peut être indisponible par intermittence pendant que Braze effectue l'appel. Dans ce cas, Braze prend en charge la logique de réessai pour réessayer la demande en utilisant des délais exponentiels.

{% alert note %}
Le contenu connecté `:retry` n'est pas disponible pour les messages in-app.
{% endalert %}

## Utilisation de la logique de réessai

Pour utiliser la logique de réessai, ajoutez l'étiquette `:retry` à l'appel au contenu connecté, comme le montre l'extrait de code suivant :

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Lorsqu'une étiquette `:retry` est incluse dans l'appel de contenu connecté, Braze tente de réessayer l'appel jusqu'à cinq fois.

### Résultats des tentatives

#### Lorsqu'une nouvelle tentative réussit

Si une nouvelle tentative réussit, le message est envoyé et aucune autre tentative n'est effectuée pour ce message.

#### Lorsque l'appel API échoue et que les tentatives sont activées

Si l'appel API échoue et que cette option est activée, Braze relance l'appel tout en respectant la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) que vous avez définie pour chaque nouvel envoi. Braze placera les messages qui n'ont pas abouti en fin de file d'attente et ajoutera, si nécessaire, des minutes supplémentaires au nombre total de minutes nécessaires à l'envoi de votre message.

Si l'appel au contenu connecté échoue plus de cinq fois, l'envoi de messages est interrompu, de la même manière qu'une [étiquette de message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) déclenché.