---
nav_title: Analyse/analytique du canvas (si utilisé comme adjectif)
article_title: Canvas Analytics (si utilisé comme adjectif)
page_order: 2
page_type: reference
description: "Cet article de référence décrit les différentes analyses/analytiques et les rapports que vous pouvez exploiter pour comprendre les performances de vos Canvas."
tool: 
  - Canvas
  - Reports
  
---

# Analyse/analytique du canvas (si utilisé comme adjectif)

> Vous devez savoir si ce que vous créez fait bouger les choses. Avec l'analyse/analytique Canvas, vous pouvez créer une image complète pour comprendre comment les expériences que vous construisez ont un impact sur vos objectifs. 

Une fois que vous avez créé votre canvas et qu'il est en ligne/en production/instantané, naviguez vers la page **Canvas** et sélectionnez votre Canvas pour ouvrir la page de détails. Ici, vous pouvez mesurer et tester la performance de votre Canvas.

## Aperçu du canvas

La partie supérieure de la page **Détails du canevas** contient des statistiques sur le canevas. Il s'agit notamment du nombre d'envois de messages dans le Canvas, du nombre total de fois où les clients sont entrés dans le Canvas, du nombre de conversions et de votre taux total, du chiffre d'affaires généré par le Canvas et de l'estimation de l'audience totale. 

C'est l'endroit idéal pour obtenir un aperçu de haut niveau afin de vérifier les performances de votre Canvas par rapport à votre objectif.

\![]({% image_buster /assets/img_archive/Journey_5.png %})

### Changements depuis la dernière consultation

Le nombre de mises à jour du Canvas effectuées par d'autres membres de votre équipe est suivi par l'indicateur *Changements depuis le dernier affichage sur* la page d'aperçu du Canvas. Sélectionnez **Modifications depuis la dernière consultation** pour afficher un journal des modifications apportées au nom de Canvas, à la planification, aux étiquettes, au message, à l'audience, à l'état d'approbation ou à la configuration de l'accès de l'équipe. Pour chaque mise à jour, vous pouvez voir qui a effectué la mise à jour et quand. Vous pouvez utiliser ce journal des modifications pour auditer les modifications apportées à vos toiles.

## Visualisation des performances

Au fur et à mesure que vous descendez dans la page des **détails du canvas**, vous pouvez voir les performances de chaque composant, par exemple le nombre d'utilisateurs qui sont entrés, qui sont passés à l'étape suivante ou qui ont quitté le canvas. 

{% alert note %}
Dans le cas du Canvas Flow, l'utilisateur quittera le Canvas après avoir saisi et reçu l'envoi du message à la dernière étape du parcours de l'utilisateur.
{% endalert %}

Les indicateurs comprennent également les impressions, les destinataires uniques, le nombre de conversions et les chiffres d'affaires générés. Vous pouvez cliquer sur un composant pour décomposer davantage vos données et voir les performances spécifiques à chaque canal.

!Deux exemples de détails de performance pour les composants de Canvas. À gauche, vous trouverez les détails des performances d'un chemin d'utilisateur avec un composant Canvas. À droite, vous trouverez des détails sur les performances d'un composant Canvas développé et d'une étape du canvas qui affiche le nombre d'impressions de messages in-app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Ventilation des performances par variante

En bas de la page **Détails du canvas**, cliquez sur **Analyser les variantes** pour ouvrir la fenêtre **modale/boîte de** dialogue, etc. Cette fenêtre modale/boîte de dialogue contient trois onglets : 

- Analyser les variantes
- Rapport d'entonnoir Canvas
- Rapport sur la rétention dans Canvas

### Analyser les variantes

Dans l'onglet **Analyser les variantes**, vous pouvez voir une répartition des performances par variante et par groupe de contrôle, si vous en avez plusieurs. Vous pouvez également copier l'identifiant de l'API Canvas, télécharger un fichier CSV des indicateurs et copier les cellules. L'onglet **Analyser les variantes** contient un tableau qui vous présente une ventilation de chaque variante à plusieurs niveaux. 

Vous pouvez rapidement déduire les variantes efficaces et identifier les bonnes cadences, le contenu, les déclencheurs, le timing et bien plus encore.

\![]({% image_buster /assets/img_archive/analyze_variants.png %})

Les indicateurs de base sont les suivants :  

- **Identifiant API de la variante :** L'identifiant API de votre variante, que vous pouvez utiliser dans vos appels API.
- **Nombre total d'inscriptions :** Le nombre total d'utilisateurs qui ont saisi la variante du canvas.
- **Total des envois :** Nombre total de messages envoyés dans la variante du canvas.
- **Nombre total de pas :** Le nombre total d'étapes de la variante du canvas.
- **Chiffre d'affaires total :** Le chiffre d'affaires total en dollars provenant des destinataires de Canvas dans la fenêtre de conversion primaire définie.

{% alert note %}
Comme les conversions, le chiffre d'affaires est techniquement suivi au niveau du Canvas, mais il est attribué au composant le plus récent et à la variante la plus récente dont l'utilisateur a reçu un message (ou est entré, s'il n'a pas encore reçu de message).<br><br>
Par exemple, si un utilisateur franchit deux étapes et effectue ensuite un achat, ce chiffre d'affaires est attribué au deuxième élément et à la variante qu'il a saisie. S'ils entrent dans le canvas mais effectuent un achat avant de recevoir le premier composant du canvas, ce chiffre d'affaires est attribué à la variante qu'ils ont entrée, mais à aucun composant.
{% endalert %}

Au-delà, vous pouvez voir une répartition plus explicite des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), notamment les suivants :

- Totaux et taux de conversion pour chaque événement de conversion
- Amélioration par rapport à la variante de contrôle
- Confiance statistique pour chaque événement de conversion

### Comment les conversions sont-elles suivies ? 

Un utilisateur ne peut effectuer qu'une seule conversion par événement de conversion et par entrée dans le Canvas. Les conversions sont attribuées au message le plus récent reçu par l'utilisateur pour cette entrée. Le résumé Canvas reflète toutes les conversions effectuées par les utilisateurs dans ce chemin et indique s'ils ont reçu un message ou non. Chaque étape suivante n'affichera que les conversions qui se sont produites pendant l'étape la plus récente que l'utilisateur a reçue. 

Considérez l'exemple suivant : un Canvas a 10 notifications push et l'événement de conversion est " Opens App " (ou " Session Start ").
- L'utilisateur A ouvre l'appli après être entré mais avant d'avoir reçu le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

L'étape du canvas indiquera deux conversions, tandis que les étapes individuelles indiqueront une conversion pour la première étape et aucune pour toutes les étapes suivantes. Si des heures calmes sont actives au moment de l'événement de conversion, les mêmes règles s'appliquent. 

Supposons maintenant que nous ayons un canvas avec des heures calmes et que les événements suivants se produisent :

1. L'utilisateur A entre dans un Canvas.
2. La première étape est une étape de retardement dans les heures calmes définies, de sorte que le message est supprimé.
3. L'utilisateur A effectue l'événement de conversion.

L'utilisateur A sera comptabilisé comme converti dans la variante globale du canvas, mais pas dans l'étape du canvas puisqu'il n'a pas reçu l'étape.

Pour notre dernier exemple, disons que nous avons un canvas dont la rééligibilité est activée. Si un utilisateur rééligible effectue l'événement de conversion lors de la première entrée et de la deuxième entrée, deux conversions seront comptabilisées.

### Rapport d'entonnoir

Le rapport d'entonnoir offre un rapport visuel qui vous permet d'analyser les parcours de vos clients après la réception d'une toile. Si votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous serez en mesure de comprendre l'impact des différentes variantes sur l'entonnoir de conversion à un niveau plus granulaire et d'optimiser en fonction de ces données. Pour plus d'informations sur les rapports d'entonnoirs, voir [Rapports d'entonnoirs]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

### Rapport de rétention

La fidélisation des utilisateurs est l'un des indicateurs les plus importants pour tout marketeur. Le fait que les utilisateurs engagés reviennent pour en savoir plus indique que l'entreprise est en bonne santé. Braze vous permet désormais de mesurer la rétention des utilisateurs directement sur la page d'**analyse/analytique de Canvas**. Pour plus d'informations sur la manière de lire et d'interpréter votre rapport de rétention, consultez la rubrique [Rapports de rétention.]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)

