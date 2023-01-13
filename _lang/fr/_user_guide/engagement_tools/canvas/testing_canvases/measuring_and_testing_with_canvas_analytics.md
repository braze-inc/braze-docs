---
nav_title: Analytique Canvas
article_title: Analytique Canvas
page_order: 2
page_type: reference
description: "Cet article de référence décrit les différents analytiques et rapports que vous pouvez utiliser pour comprendre votre performance Canvas."
tool: 
  - Canvas
  - Rapports
  
---

# Analytique Canvas

Vous devez savoir si ce que vous créez est utile. L’analytique Canvas vous permet de créer un tableau complet pour comprendre comment les expériences que vous créez impactent vos objectifs. Une fois que vous avez créé et activé Canvas, naviguez jusqu’à la page **Canvas** et sélectionnez votre Canvas pour ouvrir la page des détails. Vous pouvez mesurer et tester la performance de votre Canvas.

## Overview Canvas

En haut de la page **Détails de Canvas** figurent les statistiques supérieures de Canvas. Elles comprennent le nombre de messages envoyés dans le Canvas, le nombre total de fois que des clients ont accédé à Canvas, le nombre de conversions et votre taux total, le revenu généré par le Canvas et le public total estimé. 

C’est l’endroit idéal pour avoir une overview de niveau supérieur si votre Canvas ne répond pas à votre objectif.

![][24]

## Visualisation de la performance

À mesure que vous vous déplacez dans la page **Détails de Canvas**, vous pouvez voir la performance pour chaque étape. Ces métriques comprennent les envois, les destinataires uniques, le nombre de conversions et le revenu généré. Vous pouvez cliquer sur une étape pour décomposer vos données avec plus de précision et voir la performance spécifique au canal.

![Deux exemples de détails de performance pour Canvas Steps. À gauche, les détails de la performance s’affichent pour un chemin d’utilisateur avec un Canvas Step. À droite, les détails de la performance s’affichent pour une Canvas Step développée et pour l’Étape 1, l’Étape 2 et l’Étape 3 imbriquées.][25]

## Décomposition de performance par variante

En bas de la page **Détails de Canvas**, cliquez sur **Analyser variantes** pour ouvrir le modal **Analyser Canvas**. Ce modal contient trois onglets : 

- Analyser variantes
- Rapport d’entonnoir Canvas
- Rapport de rétention Canvas

### Analyser variantes

Dans l’onglet **Analyser variantes**, vous pouvez voir la décomposition de la performance par variante et le groupe de contrôle, si vous en avez plusieurs. Vous pouvez également copier l’identifiant API Canvas, télécharger un fichier CSV des métriques et copier les cellules. L’onglet **Analyser variantes** contient une table indiquant chaque variante décomposée à plusieurs niveaux. 

Vous pouvez rapidement inférer les variantes efficaces et identifier les cadences, le contenu, les déclencheurs, le timing appropriés et bien plus.

![][26]

Les métriques de base comprennent les éléments suivants :  

- **Identifiant API de variante :** L’identifiant API de votre variante que vous pouvez utiliser dans vos appels API.
- **Total des entrées :** Le nombre total d’utilisateurs ayant accédé à Canvas Variant.
- **Total des envois :** Le nombre total de messages envoyés dans Canvas Variant.
- **Total des étapes :** Le nombre total d’étapes dans Canvas Variant.
- **Total des revenus :** Le revenu total en dollars de destinataires de Canvas dans la fenêtre de conversion principale définie.

{% alert note %}
Comme les conversions, le revenu est soumis techniquement à un suivi au niveau de Canvas, mais il est attribué à l’étape la plus récente et à la variante la plus récente depuis lesquelles l’utilisateur a reçu un message (ou saisi, si aucun message n’a encore été reçu).<br><br>
Par exemple, si un utilisateur exécute deux étapes puis effectue un achat, ce revenu est attribué à la seconde étape et à la variante saisie. S’il accède au Canvas, mais effectue un achat avant de recevoir la première étape, ce revenu est attribué à la variante saisie, mais pas à une étape.
{% endalert %}

Au-delà de cela, vous verrez une décomposition plus explicite d’[événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), dont les éléments suivants :

- Totaux de conversion et taux de conversion pour chaque événement de conversion
- Progression par rapport à la variante de contrôle
- Seuil de confiance des statistiques pour chaque événement de conversion

### Rapport d’entonnoir

Le rapport d’entonnoir offre un rapport visuel qui vous permet d’analyser les parcours effectués par vos clients après la réception d’une campagne ou d’un Canvas. Si votre campagne ou votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous serez en mesure de comprendre comment les différentes variantes ont impacté l’entonnoir de conversion à un niveau plus précis et de l’optimiser en fonction de ces données. Pour plus d’informations sur les rapports d’entonnoir, voir [Rapport d’entonnoir][2].

### Rapport de rétention

La rétention d’utilisateur est l’une des métriques les plus importantes pour un marketeur. Gagner la confiance des utilisateurs pour les fidéliser est un indicateur de la croissance de l’entreprise. Braze vous permet désormais de mesurer la fidélité de l’utilisateur, directement sur la page Analytics Canvas. Pour plus d’informations sur la façon de lire et d’interpréter votre rapport de rétention, consultez [Rapports de rétention][1].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/
[24]:{% image_buster /assets/img_archive/Journey_5.png %}
[25]:{% image_buster /assets/img_archive/Journey_6.png %}
[26]:{% image_buster /assets/img_archive/analyze_variants.png %}
