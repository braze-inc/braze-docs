---
nav_title: "Déclencheurs d'attributs"
article_title: "Déclencheurs d'attributs"
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Cet article de référence donne un aperçu des déclencheurs d'attributs et de la manière dont vous pouvez les utiliser pour envoyer aux utilisateurs des messages basés sur des actions."
tool:
  - Campaigns

---

# Déclencheurs d'attributs

> Les déclencheurs d'attributs vous permettent d'envoyer des messages basés sur des actions lorsque l'état de l'abonnement d'un utilisateur ou les valeurs d'un attribut personnalisé changent. 

Les déclencheurs d'attributs sont disponibles pour les scénarios suivants :

- Mise à jour de l'état de l'abonnement.
- Les valeurs booléennes, entières, chaînes de caractères ou dates des attributs personnalisés sont remplacées par n'importe quelle valeur.
- Les valeurs booléennes, entières ou de chaînes de caractères des attributs personnalisés sont remplacées par une valeur spécifique.

Pour commencer à utiliser les déclencheurs d'attributs, créez une campagne ou un composant Canvas et sélectionnez la **livraison par événement** comme méthode de **réception/distribution**. Sélectionnez ensuite le déclencheur d'attributs que vous souhaitez utiliser.

\!["Livraison par événement" avec une liste déroulante permettant de sélectionner un déclencheur.]({% image_buster /assets/img_archive/trigger_attribute.png %})

### Mise à jour de l'état de l'abonnement

Utilisez le déclencheur `Update Subscription Status` pour cibler les utilisateurs lorsque leur statut d'abonnement est mis à jour. 

Par exemple, vous pouvez cibler les utilisateurs lorsque leur statut d'abonnement à un e-mail ou à un service de push passe à l'état d'abonnement, et les remercier d'avoir accepté. Vous pouvez également envoyer un webhook à vos systèmes chaque fois qu'un utilisateur se désabonne d'un e-mail afin que vos systèmes internes soient à jour avec les dernières informations sur l'état de l'abonnement.

{% alert important %}
Ce déclencheur ne s'applique pas lorsqu'un nouvel utilisateur est créé avec l'état global de l'e-mail par défaut de `subscribed` et qu'il y a une demande ultérieure de mise à jour de l'état à `subscribed` puisque le statut de l'abonnement n'a pas changé.
{% endalert %}

### Mise à jour du statut du groupe d'abonnement

Utilisez le déclencheur `Update Subscription Group Status` pour cibler les utilisateurs lorsque leur statut du groupe d'abonnement pour l'e-mail, le SMS ou WhatsApp est mis à jour. 

Par exemple, vous pouvez cibler les utilisateurs avec un message SMS de bienvenue lorsqu'ils s'inscrivent à votre programme. Vous pouvez également spécifier la source de la mise à jour afin de mieux contrôler le moment où un message est envoyé. 

Les sources de mise à jour disponibles varient d'un canal à l'autre :
- Étape de mise à jour de l'utilisateur de Canvas
- Importation CSV
- List-Unsubscribe
- Centre de préférences
- API REST
- SDK
- Shopify (e-mail, SMS)
- Message entrant (SMS)

Par exemple, vous pouvez vouloir envoyer votre SMS de bienvenue uniquement lorsque la mise à jour provient de l'API REST et non d'un message entrant, puisque Braze répond déjà automatiquement à certains SMS entrants.

### Modifier la valeur d'un attribut personnalisé

Pour les attributs de changement, le déclencheur est évalué en premier, puis les critères d'audience. Cela diffère du comportement par défaut qui consiste à évaluer d'abord les critères d'audience, puis le déclencheur. Pour éviter une condition de concurrence, assurez-vous que l'attribut utilisé comme déclencheur n'est pas le même que l'attribut utilisé pour qualifier votre audience.

#### Toute nouvelle option de valeur

Utilisez le déclencheur `Change Custom Attribute Value` avec l'option `any new value` pour cibler les utilisateurs lorsque la valeur d'un booléen, d'un entier, d'une chaîne de caractères ou d'une date passe à une nouvelle valeur.

Par exemple, ciblez les utilisateurs lorsque leur nombre de points de récompense change pour leur faire savoir combien de points ils ont désormais. Dans cet exemple, disons qu'un utilisateur a 85 points de récompense et que vous avez implémenté une campagne qui se déclenche lorsque l'attribut du point de récompense change de valeur. Si la valeur de l'attribut de points de récompense de cet utilisateur passe à une nouvelle valeur (telle que 83, 84, 86, etc.), la campagne se déclenche.

Prenons l'exemple suivant d'une notification de mise à jour d'un niveau. Vous pourriez vouloir alerter les utilisateurs en cas de changement de leur niveau de récompense. Pour réaliser ce cas d'utilisation, configurez une campagne qui s'implémente à partir de `Change Custom Attribute Value` et définissez-la pour qu'elle se déclenche lorsque l'attribut personnalisé du niveau de récompense passe à une nouvelle valeur.

{% alert important %}
Les déclencheurs d'attributs ne sont actuellement pas disponibles pour les attributs de tableau.
{% endalert %}

\![Un déclencheur "Changer la valeur de l'attribut personnalisé" pour que l'adresse "AA_current_rewards_tier" prenne n'importe quelle valeur.]({% image_buster /assets/img_archive/any_value.png %})

Vous pouvez également utiliser Liquid pour personnaliser le corps du message avec le nouveau niveau de récompense du client et lui fournir plus d'informations sur le changement.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

#### Valeur spécifique

Utilisez le déclencheur `Change Custom Attribute Value` avec l'option `specific value` pour cibler les utilisateurs lorsqu'un attribut personnalisé de type booléen, entier ou chaîne de caractères passe à une valeur spécifique. 

Par exemple, ciblez les utilisateurs lorsque leur niveau de récompense passe au meilleur niveau. Pour cet exemple, disons que le meilleur niveau de récompense est Super VIP. Vous pouvez implémenter des campagnes qui se déclenchent lorsque l'attribut personnalisé du niveau de récompenses d'un utilisateur devient `Super VIP` afin de le féliciter d'être devenu un Super VIP.

\![Un déclencheur "Change Custom Attribute Value" pour que le site "AA_current_rewards_tier" prenne la valeur spécifique de "super vip".]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Les déclencheurs d'attributs pour des valeurs d'attributs personnalisés spécifiques ne sont pas disponibles pour les attributs personnalisés de type tableau et date.
- Le déclencheur de modification des valeurs d'attributs personnalisés ne se déclenche pas lorsque la valeur de l'attribut personnalisé est mise à jour et devient nulle.  
- Le déclencheur de modification des valeurs d'attributs personnalisés ne se déclenche que lorsque la valeur d'un attribut personnalisé change. Si la valeur actuelle d'un attribut personnalisé est renvoyée à Braze (e.g la valeur de l'attribut favorite color est rouge, et vous renvoyez la valeur rouge à Braze), le déclencheur de modification des valeurs des attributs personnalisés ne se produira pas.
- Le déclencheur de modification des valeurs des attributs personnalisés s'applique également aux nouveaux utilisateurs créés.
{% endalert %}

