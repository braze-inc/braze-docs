---
nav_title: Déclencheurs d'attributs
article_title: Déclencheurs d'attributs
page_order: 1
alias: /attribut_triggers/
page_type: Référence
description: "Cet article de référence donne une vue d'ensemble des déclencheurs d'attributs et comment vous pouvez les utiliser pour envoyer des messages basés sur l'action aux utilisateurs."
tool:
  - Campagnes
---

# Vue d'ensemble des déclencheurs d'attributs

> Cet article de référence donne une vue d'ensemble des déclencheurs d'attributs et comment vous pouvez les utiliser pour envoyer des messages basés sur des actions.

Les déclencheurs d'attributs vous permettent d'envoyer des messages basés sur l'action lorsque l'état d'abonnement d'un utilisateur ou les valeurs d'attributs personnalisés changent. Les déclencheurs d'attributs sont disponibles pour les scénarios suivants :

- Mises à jour de l'état de l'abonnement.
- Les valeurs de l'attribut personnalisé Boolean, integer, string ou date changent pour n'importe quelle valeur.
- Les valeurs de l'attribut personnalisé booléen, entier ou chaîne de caractères changent pour une valeur spécifique.

Pour commencer à utiliser les déclencheurs d'attributs, créez une campagne ou une étape de Canvas et sélectionnez la distribution basée sur l'action. Ensuite, sélectionnez le déclencheur d'attribut que vous souhaitez utiliser.

!\[déclencheurs d'attribut\]\[1\]

### Mettre à jour le statut d'abonnement

Utilisez le déclencheur `Mettre à jour le statut d'abonnement` pour cibler les utilisateurs lorsque leur statut d'abonnement est mis à jour. Par exemple, vous pouvez cibler les utilisateurs lorsque leur statut de courrier électronique ou de push de l'abonnement change pour vous inscrire, et les remercier de vous être engagés. Vous pouvez également envoyer un webhook à vos systèmes chaque fois qu'un utilisateur se désabonne de l'e-mail afin que vos systèmes internes soient à jour avec les dernières informations d'état d'abonnement.

### Mettre à jour le statut du groupe d'abonnement

Utilisez le déclencheur `Mettre à jour le statut du groupe d'abonnement` pour cibler les utilisateurs lorsque leur statut de groupe d'abonnement pour les e-mails ou SMS est mis à jour. Par exemple, vous pouvez cibler les utilisateurs avec un message SMS de bienvenue une fois qu'ils ont choisi votre programme. Vous pouvez également spécifier la source de la mise à jour pour avoir un contrôle plus précis sur le moment où un message s'allume.

Les sources de mise à jour peuvent être REST API, le centre de préférences (email) ou les messages entrants (SMS). Par exemple, vous pouvez ne vouloir envoyer votre SMS de bienvenue que lorsque la mise à jour provient de l'API REST et non d'un message entrant. car Braze répond déjà automatiquement à certains SMS entrants.

### Changer la valeur de l'attribut personnalisé

#### Toute nouvelle valeur

Utilisez le trigger `Modifier la valeur d'attribut personnalisée` avec l'option `toute nouvelle valeur` pour cibler les utilisateurs lorsqu'un booléen, integer, chaîne de caractères ou valeur de date change à toute nouvelle valeur. Par exemple, les utilisateurs ciblés lorsque leur nombre de points de fidélité change pour leur permettre de savoir combien de points ils ont maintenant. Dans cet exemple, disons qu'un utilisateur a 85 points de fidélité et vous avez mis en place une campagne pour déclencher lorsque l'attribut point de fidélité change à toute nouvelle valeur. Si l'attribut point de fidélité de cet utilisateur change à une nouvelle valeur (par exemple 83, 84, 86, etc.) la campagne se déclenchera.

Un autre exemple de cas d'utilisation est une notification de mise à jour de niveau. Vous pouvez avertir les utilisateurs si leur niveau de fidélité change. Pour accomplir ce cas d'utilisation, mettre en place une campagne qui déclenche la désactivation de `Modifier la valeur d'attribut personnalisé` et le définir pour le déclencher lorsque le niveau de fidélité de l'attribut personnalisé change à toute nouvelle valeur.

{% alert important %}
Les déclencheurs d'attributs ne sont actuellement pas disponibles pour les attributs de tableau.
{% endalert %}

!\[n'importe quelle valeur\]\[2\]

Vous pouvez également utiliser Liquid pour personnaliser le corps du message avec le nouveau niveau de fidélité du client et fournir au client plus d'informations sur le changement.

{% raw %}
```liquid
Votre niveau de fidélité vient d'être changé en {{custom_attribute.${loyalty_tier}}}
```
{% endraw %}


#### Valeur spécifique

Utilisez le trigger `Modifier la valeur d'attribut personnalisée` avec l'option `valeur spécifique` pour cibler les utilisateurs lorsqu'un booléen, l'attribut personnalisé entier ou chaîne de caractères change à une valeur spécifique. Par exemple, les utilisateurs ciblés lorsque leur niveau de fidélité passe au niveau supérieur. Pour cet exemple, dites que le meilleur niveau de fidélité est Super VIP. Vous pouvez configurer une campagne à déclencher lorsque l'attribut personnalisé du niveau de fidélité d'un utilisateur change à `Super VIP` pour que vous puissiez féliciter l'utilisateur d'être devenu un Super VIP.

!\[super vip\]\[4\]

{% alert important %}
- Les déclencheurs d'attributs pour des valeurs d'attributs personnalisés spécifiques ne sont pas disponibles pour les attributs personnalisés de tableau et de date.
- Le déclencheur de changement d'attribut personnalisé ne se déclenche pas lorsque la valeur de l'attribut personnalisé est mise à jour à NULL.
- Le trigger de changement de valeur d'attribut personnalisé ne se déclenchera que lorsque la valeur d'un attribut personnalisé change. Si la valeur actuelle d'un attribut personnalisé est renvoyée à Braze (e. la valeur de l'attribut de couleur favori est rouge, et vous renvoyez la valeur rouge à Braze), le trigger de changement de valeur d'attribut personnalisé ne se produira pas.
- Le trigger de changement des valeurs d'attributs personnalisés s'applique également aux nouveaux utilisateurs créés.
{% endalert %}
[1]:{% image_buster /assets/img_archive/trigger_attribute.png %} [2]:{% image_buster /assets/img_archive/any_value.png %} [4]:{% image_buster /assets/img_archive/super_vip.png %}
