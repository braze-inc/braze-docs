---
nav_title: Analyses Canvas
article_title: Analyses Canvas
page_order: 2
page_type: reference
description: "Cet article de référence décrit les différentes analyses et rapports que vous pouvez exploiter pour comprendre votre performance Canvas."
tool: 
  - Canvas
  - Reports
  
---

# Analytique Canvas

> Vous devez savoir si ce que vous créez est utile. Les analyses Canvas vous permet de créer un tableau complet pour comprendre comment les expériences que vous créez impactent vos objectifs. 

Une fois que vous avez construit votre Canvas et l'avez mis en ligne, accédez à la page **Canvas** et sélectionnez votre Canvas pour ouvrir la page de détails. Vous pouvez mesurer et tester ici la performance de votre Canvas.

## Overview Canvas

Le haut de la page **Canvas Details** contient les statistiques principales de Canvas. Elles comprennent le nombre de messages envoyés dans le Canvas, le nombre total de fois que des clients ont accédé à Canvas, le nombre de conversions et votre taux total, le revenu généré par le Canvas et l’audience totale estimée. 

C’est l’endroit idéal pour avoir un aperçu de niveau supérieur pour vérifier si votre Canvas ne répond pas à votre objectif.

![]({% image_buster /assets/img_archive/Journey_5.png %})

### modifications depuis la dernière consultation

Le nombre de mises à jour du Canvas effectuées par d'autres membres de votre équipe est suivi par l'indicateur *Changements depuis le dernier affichage sur* la page d'aperçu du Canvas. Sélectionnez **Modifications depuis la dernière consultation** pour afficher un journal des modifications apportées au nom de Canvas, à la planification, aux étiquettes, au message, à l'audience, à l'état d'approbation ou à la configuration de l'accès de l'équipe. Pour chaque mise à jour, vous pouvez voir qui a effectué la mise à jour et quand. Vous pouvez utiliser ce journal des modifications pour auditer les modifications apportées à vos toiles.

## Visualisation de la performance

Au fur et à mesure que vous descendez la page **Canvas Details**, vous pouvez voir les performances de chaque composant, comme le nombre d'utilisateurs qui sont entrés, ont procédé à l'étape suivante ou ont quitté le Canvas. 

{% alert note %}
Pour Canvas Flow, un utilisateur quittera le Canvas après être entré et avoir reçu la charge utile de message dans la dernière étape du parcours utilisateur.
{% endalert %}

Ces indicateurs comprennent également les impressions, les destinataires uniques, le nombre de conversions et le revenu généré. Vous pouvez cliquer sur un composant pour décomposer vos données avec plus de précision et voir la performance spécifique au canal.

![Deux exemples de détails de performance pour des composants Canvas. À gauche, les détails de la performance s’affichent pour un parcours utilisateur avec un composant Canvas. À droite, vous trouverez des détails sur les performances d'un composant Canvas étendu et d'une étape imbriquée qui indique le nombre d'impressions de messages in-app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Décomposition de performance par variante

En bas de la page **Canvas Details**, cliquez sur **Analyze Variants** pour ouvrir la fenêtre modale **Analyze Canvas**. Ce modal contient trois onglets : 

- Analyser variantes
- Rapport d’entonnoir Canvas
- Rapport de rétention Canvas

### Analyser variantes

Dans l'onglet **Analyser les variantes**, vous pouvez voir une répartition des performances par variante et groupe de contrôle, si vous en avez plus d'un. Vous pouvez également copier l’identifiant API Canvas, télécharger un fichier CSV des indicateurs et copier les cellules. L'onglet **Analyser les variantes** contient un tableau qui vous montre une répartition de chaque variante à plusieurs niveaux. 

Vous pouvez rapidement inférer les variantes efficaces et identifier les cadences, le contenu, les déclencheurs, le timing appropriés et bien plus.

![]({% image_buster /assets/img_archive/analyze_variants.png %})

Les indicateurs de base comprennent les éléments suivants :  

- **Identifiant de l'API de variante:** L’identifiant API de votre variante que vous pouvez utiliser dans vos appels API.
- **Total des entrées :** Le nombre total d’utilisateurs ayant accédé à Canvas Variant.
- **Total des envois :** Le nombre total de messages envoyés dans Canvas Variant.
- **Total des étapes :** Le nombre total d’étapes dans Canvas Variant.
- **Revenu total :** Le revenu total en dollars de destinataires de Canvas dans la fenêtre de conversion principale définie.

{% alert note %}
Comme les conversions, le revenu est soumis techniquement à un suivi au niveau de Canvas, mais il est attribué au composant le plus récent et à la variante la plus récente depuis lesquels l’utilisateur a reçu un message (ou est entré, si aucun message n’a encore été reçu).<br><br>
Par exemple, si un utilisateur exécute deux étapes puis effectue un achat, ce revenu est attribué au second composant et à la variante dans laquelle il est entré. S’il accède au Canvas, mais effectue un achat avant de recevoir le premier composant Canvas, ce revenu est attribué à la variante dans laquelle il est entré, mais pas à un composant.
{% endalert %}

Au-delà de cela, vous pouvez voir une répartition plus explicite des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), y compris les éléments suivants :

- Totaux de conversion et taux de conversion pour chaque événement de conversion
- Progression par rapport à la variante de contrôle
- Seuil de confiance des statistiques pour chaque événement de conversion

### Rapport d'entonnoir

Le rapport d’entonnoir offre un rapport visuel qui vous permet d’analyser les parcours de vos clients après la réception d’un canvas. Si votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous pourrez comprendre comment les différentes variantes ont impacté l'entonnoir de conversion à un niveau plus granulaire et optimiser en fonction de ces données. Pour plus d'informations sur les rapports d'entonnoir, voir [Rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

### Rapport de rétention

La rétention d’utilisateur est l’un des indicateurs les plus importants pour un marketeur. Gagner la confiance des utilisateurs pour les fidéliser est un indicateur de la croissance de l’entreprise. Braze vous permet désormais de mesurer la rétention des utilisateurs directement sur la page **Canvas Analytics**. Pour plus d'informations sur la façon de lire et d'interpréter votre rapport de rétention, consultez [Rapports de rétention]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

