---
nav_title: Shopify checkout.liquid
page_order: 7
description: "Cet article explique la dépréciation de Shopify checkout.liquid, y compris l'impact sur votre intégration Shopify et les conseils pour les développeurs."
page_type: update

---

# Shopify checkout.liquid deprecation

Shopify a informé tous les marchands de la dépréciation de `checkout.liquid`, et de la migration vers [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), une nouvelle base pour créer des expériences de paiement personnalisées. 

Shopify va supprimer `checkout.liquid` en deux phases :

1. **Le [13 août 2024](#phase-one-august-13-2024):** Délai pour mettre à jour vos pages d'information, d'expédition et de paiement.
2. **[28 août 2025](#phase-two-august-28-2025):** Statut de commande pour la mise à jour de vos pages de remerciement et d'état de la commande, y compris vos applications utilisant des étiquettes de script et des scripts supplémentaires.

Pour obtenir des informations générales sur la mise à niveau vers Checkout Extensibilty, consultez le [guide de mise à niveau de Shopify.](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility)

## Impact sur votre intégration

L'intégration de Braze et Shopify utilise les [ScriptTags de Shopify](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) pour charger le SDK Web de Braze pour les sites sans tête. Nous prévoyons de lancer une nouvelle version de l'intégration avant la date limite de 2025 afin de prendre en charge tous les clients avant que `checkout.liquid` ne soit entièrement déprécié. 

Pour les changements à venir le 13 août 2024, vérifiez les détails ci-dessous pour savoir si vous serez impacté par votre équipe de développement.

### Première phase : 13 août 2024

L'intégration par défaut de Braze et Shopify n'utilise pas les pages d'information, d'expédition et de paiement au sein de l'expérience de paiement. Par conséquent, l'intégration par défaut ne sera pas affectée. 

#### Shopify Plus

Pour les clients Shopify Plus, tous les extraits de code SDK personnalisés qui modifient `checkout.liquid` pour les pages d'information, d'expédition ou de paiement deviendront inactifs après cette date. Par exemple, le code personnalisé qui enregistre les événements de ces pages ne fonctionnera plus. Si vous avez un code SDK personnalisé, consultez nos [conseils aux développeurs](#developer-guidance) pour la migration.

#### Non-Shopify Plus

Pour les clients non-Shopify Plus, si vous avez besoin de personnaliser les pages d'information, de paiement et d'expédition, vous [devez passer à Shopify Plus](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility), puis suivre les [conseils du développeur](#developer-guidance).

### Deuxième phase : 28 août 2025

Shopify va supprimer la prise en charge des [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) sur les pages `checkout.liquid`, qui sont utilisés dans l'intégration. En réponse, nous créons activement une nouvelle version de l'intégration de Shopify que nous prévoyons de publier bien avant l'échéance d'août 2025. Restez à l'écoute pour plus d'informations de la part de l'équipe produit de Braze. 

## Conseils aux développeurs

Ces conseils s'appliquent aux clients de Shopify Plus qui ont ajouté des extraits de code SDK personnalisés aux pages d'information, d'expédition ou de paiement sur `checkout.liquid`. Si vous n'avez pas effectué ces personnalisations, vous pouvez ignorer ces conseils.

Vous ne pourrez plus ajouter d'extraits de code SDK personnalisés aux pages d'information, d'expédition ou de paiement sur `checkout.liquid`. Au lieu de cela, vous devrez ajouter des extraits de code SDK personnalisés aux pages de remerciement ou d'état de la commande. Cela vous permet de réconcilier les utilisateurs qui ont passé la caisse.
1. Chargez le SDK web de Braze sur les pages de remerciement et de statut de la commande.
2. Récupérer l'e-mail de l'utilisateur.
3. Appelez `setEmail`.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4\. Sur Braze, fusionnez les profils utilisateurs sur l'e-mail.

Si vous rencontrez des profils utilisateurs en double, vous pouvez utiliser notre [outil de fusion en bloc]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) pour vous aider à rationaliser vos données. 
