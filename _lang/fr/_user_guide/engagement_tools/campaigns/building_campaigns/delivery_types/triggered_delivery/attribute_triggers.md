---
nav_title: Déclencheurs d’attributs
article_title: Déclencheurs d’attributs
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Le présent article de référence donne un aperçu des déclencheurs d’attributs et la manière dont vous pouvez les utiliser pour envoyer des messages basés sur des actions aux utilisateurs."
tool:
  - Campagnes

---

# Aperçu des déclencheurs d’attributs

> Le présent article de référence donne un aperçu des déclencheurs d’attributs et la manière dont vous pouvez les utiliser pour envoyer des messages basés sur des actions.

Les déclencheurs d’attributs vous permettent d’envoyer des messages basés sur des actions lorsque le statut d’abonnement d’un utilisateur ou les valeurs d’attribut personnalisé changent. Les déclencheurs d’attributs sont disponibles pour les scénarios suivants :

- Mises à jour du statut d’abonnement.
- Les valeurs d’attribut personnalisé booléennes, entières, chaînes de caractères ou dates changent vers n’importe quelle valeur.
- Les valeurs d’attribut personnalisé booléennes, entières ou chaînes de caractères changent vers une valeur spécifique.

Pour commencer à utiliser des déclencheurs d’attributs, créez une campagne ou un composant de Canvas et sélectionnez **Livraison par événement** en tant que méthode de livraison. Sélectionnez ensuite le déclencheur d’attribut que vous souhaitez utiliser.

![][1]

### Mettre à jour le statut d’abonnement

Utilisez le déclencheur `Update Subscription Status` pour cibler les utilisateurs lorsque leur statut d’abonnement est mis à jour. 

Par exemple, vous pouvez cibler les utilisateurs lorsque leur statut d’abonnement aux e-mails ou aux notifications push change vers « abonné » et les remercier de s’être abonnés. Vous pouvez également envoyer un webhook à vos systèmes chaque fois qu’un utilisateur se désinscrit des e-mails afin que vos systèmes internes soient à jour avec les dernières informations sur le statut des abonnements.

### Mettre à jour le statut du groupe d’abonnement

Utilisez le déclencheur `Mettre à jour le statut du groupe d'abonnement`  pour cibler les utilisateurs lorsque leur statut du groupe d'abonnement pour E-mail, SMS ou WhatsApp est mis à jour. 

Par exemple, vous pouvez cibler les utilisateurs avec un message SMS de bienvenue une fois qu’ils s’abonnent à votre programme. Vous pouvez également spécifier la source de la mise à jour afin d’obtenir un contrôle plus précis du moment où un message est envoyé. 

Les sources de mise à jour disponibles varient selon le canal :
- Importation CSV
- Centre de préférences
- API REST
- SDK
- Shopify (e-mail, SMS)
- Message entrant (SMS)

Par exemple, vous pouvez désirer envoyer votre SMS de bienvenue uniquement lorsque la mise à jour provient de l’API REST et non pas d’un message entrant puisque Braze répond déjà automatiquement à certains SMS entrants.

### Modifier la valeur d’attribut personnalisé

#### Toute nouvelle option de valeur

Utilisez le déclencheur `Change Custom Attribute Value` avec l’option `any new value` pour cibler les utilisateurs lorsqu’une valeur booléenne, entière, chaîne de caractères ou date change vers n’importe quelle nouvelle valeur.

Par exemple, cibler les utilisateurs lorsque leur nombre de points de fidélité change pour leur indiquer combien de points ils ont maintenant. Dans cet exemple, disons qu’un utilisateur dispose de 85 points de fidélité et que vous avez configuré une campagne pour qu’elle se déclenche lorsque l’attribut de point de fidélité change vers n’importe quelle nouvelle valeur. Si la valeur de l’attribut de point de fidélité de cet utilisateur change vers n’importe quelle nouvelle valeur (p. ex. 83, 84, 86, etc.), la campagne se déclenchera.

Examinez le prochain exemple de cas d’utilisation avec une notification de mise à jour de niveau. Vous pouvez désirer alerter les utilisateurs si leur niveau de fidélité change. Pour accomplir ce cas d’utilisation, configurez une campagne qui se déclenche à partir de `Change Custom Attribute Value` et définissez-la pour qu’elle le fasse lorsque l’attribut personnalisé de niveau de fidélité change vers n’importe quelle nouvelle valeur.

{% alert important %}
Les déclencheurs d’attributs ne sont pas actuellement disponibles pour les attributs de tableaux.
{% endalert %}

![N’importe quelle nouvelle valeur][2]

Vous pouvez également utiliser Liquid pour personnaliser le corps du message avec le nouveau niveau de fidélité du client et lui fournir plus d’informations sur le changement.

{% raw %}
```liquid
Votre niveau de fidélité vient d'être changé en {{custom_attribute.${loyalty_tier}}}
```
{% endraw %}


#### Valeur spécifique

Utilisez le déclencheur `Change Custom Attribute Value` avec l’option `specific value` pour cibler les utilisateurs lorsqu’un attribut personnalisé booléen, entier ou chaîne de caractères change vers n’importe quelle nouvelle valeur. 

Par exemple, cibler les utilisateurs lorsque leur niveau de fidélité passe au niveau le plus haut. Pour cet exemple, disons que le niveau de fidélité le plus haut est Super VIP. Vous pouvez configurer une campagne pour qu’elle se déclenche lorsque l’attribut personnalisé de niveau de fidélité d’un utilisateur passe à `Super VIP` afin que vous puissiez le féliciter d’être devenu un Super VIP.

![][4]

{% alert important %}
- Les déclencheurs d’attributs pour des valeurs d’attribut personnalisé spécifiques ne sont pas disponibles pour les attributs personnalisés de tableau et de date.
- Le déclencheur de changement de valeurs d’attribut personnalisé ne se déclenche pas lorsque cette valeur est passée à néant.  
- Le déclencheur de changement de valeurs d’attribut personnalisé ne se déclenche que lorsque la valeur d’un attribut personnalisé change. Si la valeur actuelle d’un attribut personnalisé est envoyée à nouveau à Braze (par ex. la valeur de l’attribut de couleur préféré est rouge et que vous envoyez à nouveau la valeur rouge à Braze), le déclenchement de changement de valeurs d’attribut personnalisé n’aura pas lieu.
- Le déclencheur de changement de valeurs d’attribut personnalisé s’applique également aux nouveaux utilisateurs créés. 
{% endalert %}



[1]:{% image_buster /assets/img_archive/trigger_attribute.png %}
[2]:{% image_buster /assets/img_archive/any_value.png %}
[4]:{% image_buster /assets/img_archive/super_vip.png %}
