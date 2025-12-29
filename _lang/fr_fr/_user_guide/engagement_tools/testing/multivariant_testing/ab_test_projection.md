---
nav_title: Test A/B projection
article_title: Projection des tests A/B
page_order: 20
hidden: true
page_type: reference
description: "Cet article explique comment fonctionne la projection des tests A/B, comment exécuter une projection et comment Braze utilise vos données."
---

# Test A/B projection

> La projection de tests A/B utilise des réseaux neuronaux pour prédire quelles lignes d'objet sont les plus performantes. Notre modèle extrait les fonctionnalités linguistiques des tests A/B gagnants réalisés sur Braze et utilise ces modèles linguistiques statistiques pour apprendre à notre intelligence ce qui fait de meilleures lignes d'objet.

{% alert important %}
Cette fonctionnalité est actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client ou gestionnaire de compte Braze si vous souhaitez participer à l'accès au service de satisfaction.
{% endalert %}

## Exécution d'une projection

Dans la composition de la campagne, insérez vos variantes de messages et leurs lignes d'objet dans l'éditeur. Lorsque vous êtes prêt, passez à l'étape **Audience cible** du flux de création de la campagne. Dans le panneau **Test A/B**, sélectionnez **Exécuter la projection.**

<img width="518" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Une fenêtre modale s'ouvre avec les lignes d'objet des variantes de messages que vous avez déjà créées. En option, vous pouvez insérer des lignes d'objet supplémentaires (jusqu'à un maximum de dix) en en saisissant une manuellement dans la case et en lançant la projection. Sélectionnez **Exécuter la projection**.

<img width="722" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

La ligne d'objet que notre intelligence artificielle prédit comme étant la meilleure sera mise en évidence avec un label **Projected Winner**.

{% alert note %}
Pour les [campagnes de push rapide]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/), les tests A/B sont pris en charge lorsque vous sélectionnez plusieurs plateformes.
{% endalert %}

### Quelle est la précision des projections ?

Lors des tests, nous avons constaté que les projections étaient exactes à environ 70 % lorsqu'il s'agissait de choisir entre des paires de messages dans le cadre de tests A/B réels. Tenez-en compte lorsque vous interprétez les messages que le modèle projette pour gagner.

### Comment utilisons-nous vos données ?

Cette fonctionnalité tire les enseignements des tests A/B réalisés par le passé sur Braze. La copie réelle de vos messages ou de ceux de n'importe quel client de Braze n'est jamais fournie au modèle. Nous commençons par extraire les schémas linguistiques de haut niveau qui prédisent les messages gagnants dans les tests A/B. Ensuite, nous fournissons ces modèles à notre intelligence artificielle pour lui apprendre à discerner les fonctionnalités linguistiques qui constituent des lignes d'objet supérieures.