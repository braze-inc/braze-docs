---
nav_title: Déclencheurs d’attributs
article_title: Déclencheurs d’attributs
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Le présent article de référence donne un aperçu des déclencheurs d’attributs et la manière dont vous pouvez les utiliser pour envoyer des messages basés sur des actions aux utilisateurs."
tool:
  - Campaigns

---

# Déclencheurs d’attributs

> Les déclencheurs d’attributs vous permettent d’envoyer des messages basés sur des actions lorsque le statut d’abonnement d’un utilisateur ou les valeurs d’attribut personnalisé changent. 

Les déclencheurs d’attributs sont disponibles pour les scénarios suivants :

- Mises à jour du statut d’abonnement.
- Les valeurs d’attribut personnalisé booléennes, entières, chaînes de caractères ou dates changent vers n’importe quelle valeur.
- Les valeurs d’attribut personnalisé booléennes, entières ou chaînes de caractères changent vers une valeur spécifique.

Pour commencer à utiliser les déclencheurs d'attributs, créez une campagne ou un composant Canvas et sélectionnez la **livraison par événement** comme méthode de livraison. Sélectionnez ensuite le déclencheur d’attribut que vous souhaitez utiliser.

![]({% image_buster /assets/img_archive/trigger_attribute.png %})

### Mettre à jour le statut d’abonnement

Utilisez le déclencheur `Update Subscription Status` pour cibler les utilisateurs lorsque leur statut d’abonnement est mis à jour. 

Par exemple, vous pouvez cibler les utilisateurs lorsque leur statut d’abonnement aux e-mails ou aux notifications push change vers « abonné » et les remercier de s’être abonnés. Vous pouvez également envoyer un webhook à vos systèmes chaque fois qu’un utilisateur se désinscrit des e-mails afin que vos systèmes internes soient à jour avec les dernières informations sur le statut des abonnements.

{% alert important %}
Ce déclencheur ne s'applique pas lorsqu'un nouvel utilisateur est créé avec l'état global de l'e-mail par défaut de `subscribed` et qu'il y a une demande ultérieure de mise à jour de l'état à `subscribed` puisque le statut de l'abonnement n'a pas changé.
{% endalert %}

### Mettre à jour le statut du groupe d’abonnement

Utilisez le déclencheur `Update Subscription Group Status` pour cibler les utilisateurs lorsque leur statut du groupe d’abonnement pour les e-mails, les SMS ou WhatsApp est mis à jour. 

Par exemple, vous pouvez cibler les utilisateurs en leur envoyant un message SMS de bienvenue lorsqu'ils s'inscrivent à votre programme. Vous pouvez également spécifier la source de la mise à jour afin d’obtenir un contrôle plus précis du moment où un message est envoyé. 

Les sources de mise à jour disponibles varient selon le canal :
- Importation CSV
- Centre de préférences
- API REST
- SDK
- Shopify (e-mail, SMS)
- Message entrant (SMS)

Par exemple, vous pouvez désirer envoyer votre SMS de bienvenue uniquement lorsque la mise à jour provient de l’API REST et non pas d’un message entrant puisque Braze répond déjà automatiquement à certains SMS entrants.

### Modifier la valeur d’attribut personnalisé

Pour modifier l’attribut, le déclencheur est évalué en premier, puis les critères d’audience. Cela diffère du comportement par défaut des critères d’audience évalués en premier, puis déclenchés. Pour éviter une condition de compétition, assurez-vous que l’attribut utilisé comme déclencheur n’est pas le même que l’attribut utilisé pour qualifier votre audience.

#### Toute nouvelle option de valeur

Utilisez le déclencheur `Change Custom Attribute Value` avec l’option `any new value` pour cibler les utilisateurs lorsqu’une valeur booléenne, entière, chaîne de caractères ou date change vers n’importe quelle nouvelle valeur.

Par exemple, cibler les utilisateurs lorsque leur nombre de points de fidélité change pour leur indiquer combien de points ils ont maintenant. Dans cet exemple, disons qu’un utilisateur dispose de 85 points de fidélité et que vous avez configuré une campagne pour qu’elle se déclenche lorsque l’attribut de point de fidélité change vers n’importe quelle nouvelle valeur. Si la valeur de l'attribut des points de fidélité de cet utilisateur passe à une nouvelle valeur (e.g 83, 84, 86, etc.), la campagne se déclenchera.

Examinez le prochain exemple de cas d’utilisation avec une notification de mise à jour de niveau. Vous pouvez désirer alerter les utilisateurs si leur niveau de fidélité change. Pour accomplir ce cas d’utilisation, configurez une campagne qui se déclenche à partir de `Change Custom Attribute Value` et définissez-la pour qu’elle le fasse lorsque l’attribut personnalisé de niveau de fidélité change vers n’importe quelle nouvelle valeur.

{% alert important %}
Les déclencheurs d’attributs ne sont pas actuellement disponibles pour les attributs de tableaux.
{% endalert %}

![Toute nouvelle valeur]({% image_buster /assets/img_archive/any_value.png %})

Vous pouvez également utiliser Liquid pour personnaliser le corps du message avec le nouveau niveau de fidélité du client et lui fournir plus d’informations sur le changement.

{% raw %}
```liquid
Your loyalty tier was just changed to {{custom_attribute.${loyalty_tier}}}
```
{% endraw %}

#### Valeur spécifique

Utilisez le déclencheur `Change Custom Attribute Value` avec l’option `specific value` pour cibler les utilisateurs lorsqu’un attribut personnalisé booléen, entier ou chaîne de caractères change vers n’importe quelle nouvelle valeur. 

Par exemple, cibler les utilisateurs lorsque leur niveau de fidélité passe au niveau le plus haut. Pour cet exemple, disons que le niveau de fidélité le plus haut est Super VIP. Vous pouvez configurer une campagne pour qu’elle se déclenche lorsque l’attribut personnalisé de niveau de fidélité d’un utilisateur passe à `Super VIP` afin que vous puissiez le féliciter d’être devenu un Super VIP.

![]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Les déclencheurs d’attributs pour des valeurs d’attribut personnalisé spécifiques ne sont pas disponibles pour les attributs personnalisés de tableau et de date.
- Le déclencheur de changement de valeurs d’attribut personnalisé ne se déclenche pas lorsque cette valeur est passée à néant.  
- Le déclencheur de changement de valeurs d’attribut personnalisé ne se déclenche que lorsque la valeur d’un attribut personnalisé change. Si la valeur actuelle d'un attribut personnalisé est renvoyée à Braze (e.g la valeur de l'attribut favorite color est rouge, et vous renvoyez la valeur rouge à Braze), le déclencheur de modification des valeurs des attributs personnalisés ne se produira pas.
- Le déclencheur de changement de valeurs d’attribut personnalisé s’applique également aux nouveaux utilisateurs créés.
{% endalert %}

