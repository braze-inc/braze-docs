---
nav_title: Signaler le constructeur
article_title: Signaler le constructeur
alias: /fr/rapport_builder/
page_order: 4
page_type: Référence
description: "Cet article de référence note les mises à jour de la fonction de création de rapport dans le tableau de bord."
tool:
  - Rapports
---

# Signaler le constructeur

> Le constructeur de rapports vous permet de comparer les résultats de plusieurs campagnes ou Canvases en une seule vue afin de déterminer facilement les stratégies d'engagement qui ont le plus d'impact sur vos indicateurs clés. Pour les campagnes et les Canvases, vous pouvez exporter vos données et enregistrer votre rapport pour le voir dans le futur.

!\[Exemple de comparaison de campagne\]\[5\]{: style="max-width:80%;"}

Utilisez ce rapport pour répondre aux questions clés d'engagement, par exemple:

- Quelles étaient les campagnes les plus performantes ou les Canvases pour un tag ou un canal spécifique?
- Quelles variantes de campagnes multivariantes ont eu le plus de relèvement sur le contrôle?
- Quelle campagne de promotion saisonnière a conduit à un taux d'achat plus élevé : la vente d'été, la vente d'automne ou la vente d'hiver?
- Quelles notifications push dans ce Canvas avaient les taux d'ouverture les plus élevés ?
- Quelles étapes dans ce groupe de Canvases ont eu le plus de conversions?
- Est-ce que la version 1 d'un email de bienvenue ou la version 2 d'un e-mail de bienvenue a conduit à un engagement et une conversion plus élevés ? Les changements ont-ils fonctionné ?
- Comment différentes méthodes de livraison (par exemple, 3 Push programmé vs. 3 Push basé sur l'action vs. 3 poussées déclenchées par l’API) ont un impact sur vos taux d’ouverture, vos taux de conversion ou vos taux d’achat ?
- Est-ce que les améliorations en cours apportées à la suppression des messages d'utilisateurs ont eu un impact positif sur vos indicateurs de performance (KPI) au fil du temps ?

{% alert tip %}
Essayez d'utiliser les mêmes événements de conversion pour les conversions A, B, etc à travers les campagnes et les Canvases que vous souhaitez comparer, pour que vous puissiez aligner ces conversions dans vos rapports de construction de rapports.
{% endalert %}

## Exécuter un rapport

### Étape 1 : Créer un nouveau rapport

Dans le tableau de bord, accédez à la page **Outil de création de rapport** dans la navigation de gauche. Cliquez sur **Créer un nouveau rapport** et sélectionnez soit un rapport de comparaison de campagne, soit un rapport de comparaison de Canvas .

Si vous choisissez d'exécuter un rapport sur les campagnes, vous pouvez choisir entre un rapport __Manuel__ ou __Automatisé__. Les rapports peuvent contenir soit des campagnes soit des Canvases, mais pas les deux ensemble.

{% alert note %} Les campagnes et les toiles qui ont envoyé les derniers messages au cours des 12 derniers mois seront admissibles à un rapport. {% endalert %}

!\[Tableau de bord de la campagne\]\[6\]{: style="max-width:80%;"}

Voici les différences entre ces deux options :

| __Action__                                     | __Manuelle__                                                                                                                                                                                                                               | __Automatisé__                                                                                                                                                                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __Rapport de Construction__                    | Vous serez en mesure de restreindre votre liste de campagnes en utilisant des filtres, puis de cocher des campagnes spécifiques.                                                                                                           | Vous construirez votre rapport en utilisant les options de filtre pour affiner votre liste de campagnes.                                                                                                      |
| __Enregistrement et visualisation du rapport__ | Vous pouvez enregistrer votre rapport. La prochaine fois que vous la visualiserez, vous pourrez voir la même campagne que celle que vous avez précédemment ajoutée, car ces campagnes tombent toujours sous votre filtre "Dernier Envoyé". | Vous pouvez enregistrer votre rapport. La prochaine fois que vous la visualiserez, le rapport sera automatiquement mis à jour pour inclure toutes les campagnes qui correspondent actuellement à vos filtres. |
| __Édition du rapport__                         | Vous pouvez cliquer sur Modifier le rapport pour ajouter ou supprimer des campagnes de votre rapport                                                                                                                                       | Vous pouvez modifier votre rapport en ajustant vos critères de filtre.                                                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %} Les deux rapports **Manuel** et **automatisés** peuvent inclure un maximum de 50 campagnes dans un rapport. {% endalert %}

Les rapports de Canvas fonctionnent de la même façon qu'un rapport de campagne manuel dans la mesure où les sélections de Canvas et les mises à jour de rapports doivent également être faites manuellement. Vous pouvez inclure au plus cinq toiles dans un seul rapport.

### Étape 2 : Choisissez vos mesures

Une fois que vous avez créé votre rapport, vous trouverez une table vide contenant des campagnes à chaque ligne. La table sera remplie une fois que vous aurez sélectionné __Modifier les colonnes__ et choisi les métriques que vous souhaitez ajouter. À partir d'ici, cliquez sur __Exécuter le rapport__ pour générer vos métriques.

!\[Options de la campagne\]\[15\]{: style="max-width:80%;"}

Votre tableau sera rempli avec les paramètres que vous aurez choisis. Pour les définitions de ces métriques, reportez-vous au [Glossaire des métriques][16]. Certaines mesures ne sont disponibles que pour les rapports de comparaison de campagne.

Vous pouvez également activer/désactiver les calculs pour la __moyenne__ de n'importe quel taux ou métrique numérique et __Total__ pour n'importe quelle métrique numérique.

### Étape 3 : Choisissez une période de temps

Vous pouvez sélectionner une période de temps spécifique pour afficher les données de votre rapport. Si une campagne particulière, Canvas, variante de Canvas, ou l'étape Canvas n'a aucune donnée pour la période de temps que vous avez sélectionnée, les résultats pour cette ligne seront vides.

!\[Campagne numerical metric\]\[4\]{: style="max-width:60%;"}

### Étape 4: Nommez et enregistrez votre rapport

Nommez votre rapport avant de l'enregistrer. Si un rapport est enregistré sans être nommé, Braze appliquera un nom par défaut de "Campaign Comparison Report".

!\[Campaign Note\]\[7\]{: style="max-width:60%;"}

Lorsque vous êtes prêt, cliquez sur __Enregistrer__. Les rapports enregistrés peuvent être consultés à un point ultérieur sur la page **Constructeur de rapport**.

## Rapport de comparaison de campagne avec des campagnes multivariées

Pour toutes les campagnes multivariées, vous pouvez voir ces métriques décomposées par vos variantes et votre groupe de contrôle en cliquant sur la flèche à côté du nom de la campagne. Les lignes contenant vos variantes incluront des résultats de performance pour cette variante, et la ligne contenant votre contrôle n'inclura que les résultats de vos événements de conversion.

!\[Campaign Note\]\[3\]{: style="float:right;max-width:15%;margin-left:15px;"}

Les métriques remplissant la rangée pour votre campagne globale refléteront la performance de ses variantes, mais n'incluront pas la performance du contrôle. Par exemple, l'événement de conversion primaire A pour votre campagne globale sera la somme de l'événement de conversion primaire A pour vos variantes, et cela n'inclura pas l'évènement de conversion primaire A pour votre contrôle.

{% alert important %} Si vous supprimez une variante d'une campagne multivariante, les données de cette variante ne seront pas disponibles pour un futur rapport. {% endalert %}

## Décomposition du rapport de comparaison de Canvas

Dans un rapport Canvas vous pouvez visualiser vos toiles ventilées par variante, par étape ou par message.

### Variante

En sélectionnant **ventilation par variante** vous pourrez voir les statistiques de haut niveau pour vos toiles globales, ainsi que les statistiques pour chaque variante, qui peuvent être développées en cliquant sur la flèche à côté du nom de la toile.

!\[Variants\]\[12\]{: style="max-width:90%;"}

### Étapes

La sélection de la répartition **par étapes** vous permettra de voir les métriques de niveau d'étape, à chaque ligne du rapport contenant la ligne d'une étape.

!\[Steps\]\[13\]{: style="max-width:90%;"}

### Message

Similaire à une répartition au niveau des étapes, la sélection de **répartition par message** montre le nom des étapes dans chaque ligne. cependant, dans les **colonnes d'édition**, vous aurez accès aux métriques de niveau de message, telles que les statistiques spécifiques à un canal comme les clics par e-mail et les poussées ouvertes.

!\[Report\]\[14\]{: style="max-width:90%;"}

Notez que dans le tableau de bord Braze, vous pouvez prévisualiser les 50 premières lignes de votre rapport Canvas . Vous pouvez accéder au rapport complet lorsque vous exportez un CSV.

## Accès aux rapports enregistrés

Lorsque vous accédez à un __Rapport Manuel__enregistré, vous serez en mesure d'afficher les mêmes campagnes que celles que vous avez précédemment ajoutées, car ces campagnes tombent toujours sous votre filtre « Dernier Envoyé ».

Lorsque vous accédez à un __rapport automatique__enregistré, le rapport sera automatiquement mis à jour pour inclure toutes les campagnes qui correspondent actuellement à vos filtres. Par exemple, si votre rapport a filtré les campagnes avec le tag "Promotion", alors à chaque fois que vous consultez ce rapport, vous serez en mesure de voir toutes les campagnes avec la balise « Promotion », même si ces campagnes ont été créées après que vous ayez fait ce rapport.

## Édition des rapports

Dans un __Rapport Manuel__, vous pouvez modifier un rapport en cliquant sur **Modifier**. À partir de là, vous pouvez sélectionner ou désélectionner des campagnes à inclure dans votre rapport.

Dans un __rapport automatique__, il suffit de basculer vos filtres pour affiner les résultats de votre rapport.

## Exportation des rapports

Vous pouvez également cliquer sur **Exporter** pour télécharger votre rapport vers CSV.

Si votre rapport contient des campagnes multivariantes, votre exportation inclura deux fichiers CSV :

- Un fichier contenant uniquement les métriques de niveau supérieur pour chaque campagne
- Un fichier qui contient des métriques de niveau variant

Le fichier contenant des métriques de variantes aura `variant_` ajouté au début de son nom. La première fois que vous exportez un rapport automatisé, vous recevrez une fenêtre pop-up vous demandant d'autoriser le téléchargement de plusieurs fichiers — cliquez sur __Autoriser__.

!\[Téléchargement de la campagne\]\[8\]{: style="max-width:60%;"}

### Exportation des rapports de comparaison de toiles

Votre exportation CSV reflétera la vue de répartition que vous avez affichée lorsque vous avez cliqué sur **Exporter**. Par exemple, si vous étiez dans la vue de répartition par étapes, votre export contiendra des données sur vos métriques d'étape. Pour exporter des données à partir d'une ventilation différente, vous devez d'abord naviguer vers cette ventilation et cliquer sur __Exporter__ à partir de là.

Si vous téléchargez un rapport Canvas de ventilation de variante, vous recevrez deux fichiers CSV :

- Un fichier contenant uniquement des métriques de niveau supérieur pour chaque Canvas
- Un fichier qui contient des métriques de niveau variant

## Graphiques de Bâtiments

Les cartes {% alert important %} sont actuellement en accès anticipé. Nous apporterons des améliorations fréquentes à cette fonctionnalité, donc s'il y a un cas d'utilisation que vous ne pouvez pas accomplir en ce moment, assurez-vous de revenir à nouveau dans un avenir proche. Si vous avez des commentaires sur les produits, veuillez les résumer à travers le [portail de commentaires produits](https://dashboard.braze.com/resources/roadmap/). {% endalert %}

Utilisez des graphiques pour visualiser une métrique sélectionnée dans votre rapport. Des graphiques sont disponibles pour les rapports qui comportent des campagnes et ont au moins une métrique ajoutée à ses colonnes.

!\[Graphique des performances de la campagne avec message métrique envoyé\]\[17\]

Par défaut, le graphique de chaque rapport affichera la métrique dans la première colonne du rapport. Pour sélectionner une métrique différente au graphique, choisissez votre métrique dans la liste déroulante. Toute métrique dans votre tableau de rapport sera disponible à afficher dans votre graphique.

Vous pouvez représenter au maximum trois métriques. Les unités pour toutes les métriques doivent être les mêmes — par exemple, si vous choisissez un taux dans la première liste déroulante, alors seulement les tarifs seront disponibles pour la sélection dans la deuxième liste déroulante.

Si votre graphique ne contient qu'une seule métrique, alors il affichera jusqu'à 30 campagnes en ordre décroissant en fonction de la métrique que vous avez sélectionnée. Par exemple, si la métrique de votre graphique est un clic par e-mail, alors votre diagramme affichera les 30 campagnes de courriel avec le plus de clics, classés de la plupart à moins de clics. Si votre rapport contient plus de 30 campagnes, seuls les 30 premiers seront affichés dans le graphique. Si vous sélectionnez plus d'une métrique, alors votre graphique n'affichera que les cinq premières campagnes en fonction de la première métrique sélectionnée.

Les cartes ne sont actuellement pas sauvegardées lorsque vous enregistrez votre rapport.
[3]: {% image_buster /assets/img/campaign_comparison/compare_note.png %} [4]: {% image_buster /assets/img/campaign_comparison/metric.png %} [5]: {% image_buster /assets/img/campaign_comparison/campaign_main. ng %} [6]: {% image_buster /assets/img/campaign_comparison/create_report.png %} [7]: {% image_buster /assets/img/campaign_comparison/comparison_name.png %} [8]: {% image_buster /assets/img/campaign_comparison/download. ng %} [12]: {% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %} [13]: {% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %} [14]: {% image_buster /assets/img/campaign_comparison/campaign_comparison3. ng %} [15]: {% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %} [17]: {% image_buster /assets/img/campaign_comparison/report_builder_charts.png %}

[16]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
