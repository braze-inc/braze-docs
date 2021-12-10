---
nav_title: Analyses de la toile
article_title: Analyses de la toile
page_order: 2
page_type: Référence
description: "Cet article de référence décrit les différentes analyses et rapports que vous pouvez tirer parti pour comprendre les performances de votre Canvas."
tool:
  - Toile
  - Rapports
---

# Analyses de la toile

Vous devez savoir si ce que vous construisez est de déplacer l’aiguille. Avec Canvas Analytics, vous pouvez créer une image complète pour comprendre comment les expériences que vous faites influent sur vos objectifs. Une fois que vous avez construit votre Canvas et mis en direct, accédez à la page **Canvas** et sélectionnez votre Canvas pour ouvrir la page de détails. Ici, vous pouvez mesurer et tester la performance de votre Canevas.

## Vue d'ensemble de la toile

Le haut de la page **Détails du canevas** contient les statistiques du canevas topline. Celles-ci comprennent le nombre de messages envoyés dans le Canvas, le nombre total de fois où les clients sont entrés dans le Canvas, combien de personnes ont converti et votre taux total, les revenus générés par le Canvas et le public total estimé.

C'est un endroit idéal pour avoir une vue d'ensemble de haut niveau de votre Canvas en fonction de votre objectif.

!\[Aperçu de Canvas Analytics\]\[24\]

## Visualisation des performances

Lorsque vous déplacez vers le bas la page **Détails sur le canevas** , vous pouvez voir les performances pour chaque étape. Ces mesures comprennent les envois, les bénéficiaires uniques, le nombre de conversions et les revenus générés. Vous pouvez cliquer sur une étape pour décomposer davantage vos données et voir les performances spécifiques au canal.

!\[Détails de l'étape\]\[25\]

## Répartition des performances par variante

En bas de la page **Détails du canevas** , cliquez sur **Analyser les variantes** pour ouvrir la fenêtre modale **Analyze Canvas**. Cette modale contient trois onglets :

- Analyser les variantes
- Rapport sur l'entonnoir de la toile
- Rapport de rétention de Canvas

### Analyser les variantes

Dans l’onglet **Analyser les variantes** , vous pouvez voir une ventilation des performances par variante et Groupe de contrôle, si vous en avez plusieurs. Vous pouvez également copier l'identifiant de l'API Canvase, télécharger un CSV des métriques et copier les cellules. L'onglet **Analyser les variantes** contient un tableau qui vous montre une ventilation de chaque variante à plusieurs niveaux.

Vous pouvez rapidement inférer des variantes efficaces et identifier les cadres, le contenu, les déclencheurs, le timing, et plus encore.

!\[Journey_7\]\[26\]

Les mesures de base incluent les éléments suivants :

- **Identifiant API Variante :** L'identifiant API de votre variante, que vous pouvez utiliser dans vos appels API.
- **Entrées totales :** Le nombre total d'utilisateurs qui sont entrés dans la variante Canvas .
- **Envoi total :** Le nombre total de messages envoyés dans la variante Canvas .
- **pas totaux :** Le nombre total de pas dans la variante du Canevas.
- **Revenu Total :** Le revenu total en dollars des bénéficiaires de Canvas dans la fenêtre de conversion principale définie.

{% alert note %}
Tout comme les conversions, les revenus sont techniquement suivis au niveau de Canvas mais est attribuée à l'étape la plus récente et à la variante la plus récente à partir de laquelle l'utilisateur a reçu un message (ou est entré, s'ils n'ont pas encore reçu de message).<br><br> Par exemple, si un utilisateur termine deux étapes puis effectue un achat, que les revenus sont attribués à la deuxième étape et à la variante qu'ils ont entrée. S'ils entrent dans le Canevas mais effectuent un achat avant de recevoir la première étape, que les revenus sont attribués à la variante qu'ils ont entrée, mais pas à aucune étape.
{% endalert %}

Au-delà de cela, vous pouvez voir une répartition plus explicite des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), y compris les suivants :

- Total de conversion et taux de conversion pour chaque événement de conversion
- Uplift contre la variante de contrôle
- Confiance statistique pour chaque événement de conversion

### Rapport de l'entonnoir

Funnel Reporting vous offre un rapport visuel qui vous permet d'analyser les voyages que vos clients effectuent après avoir reçu une campagne ou un Canvas. Si votre campagne ou Canvas utilise un groupe de contrôle ou plusieurs variantes, vous serez en mesure de comprendre comment les différentes variantes ont influencé l'entonnoir de conversion à un niveau plus granulaire et d'optimiser en fonction de ces données. Pour plus d'information sur les rapports d'entonnoir sur Canvas [Rapport d'entonnoir][2].

### Rapport de rétention

La conservation des utilisateurs est l'une des mesures les plus importantes pour tout commercialiste. Maintenir le retour des utilisateurs motivés indique que les affaires sont en bonne santé. Braze vous permet maintenant de mesurer la rétention des utilisateurs directement sur la page Analytiques de Canvas . Pour plus d'informations sur la façon de lire et d'interpréter votre rapport de rétention, visitez notre page [Rapport de rétention][1] de Canvas .
[24]:{% image_buster /assets/img_archive/Journey_5.png %} [25]:{% image_buster /assets/img_archive/Journey_6.png %} [26]:{% image_buster /assets/img_archive/analyze_variants.png %}

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/
