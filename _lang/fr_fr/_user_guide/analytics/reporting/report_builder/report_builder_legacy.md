---
nav_title: Générateur de rapports (ancien)
article_title: Générateur de rapports (ancien)
alias: /report_builder_legacy/
page_order: 0
page_type: reference
description: "Cette page explique comment exécuter un rapport à l'aide du générateur de rapports, notamment sur les campagnes et les toiles, en créant des rapports de comparaison et en créant des rapports et des graphiques."
tool: 
  - Reports

---

# Générateur de rapports (ancien)

> Le Créateur de rapports vous permet de comparer les résultats de plusieurs campagnes ou de plusieurs Canvas dans une vue unique pour déterminer rapidement quelles stratégies d’engagement ont le plus impacté vos indicateurs clés. Pour les campagnes et les toiles, vous pouvez exporter vos données et enregistrer votre rapport pour le consulter ultérieurement.<br><br>Pour obtenir une liste descriptive des indicateurs que vous trouverez dans vos rapports, reportez-vous au [glossaire des indicateurs de rapport.]({{site.baseurl}}/user_guide/data/report_metrics/)

![Exemple de comparaison de campagnes]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Utilisez ce rapport pour répondre aux questions clés d’engagement, par exemple :

- Quelles étaient les campagnes ou les Canvas les plus performants pour une balise ou un canal spécifique ?
- Dans mes campagnes multivariantes, quelles variantes ont le mieux marché par rapport au contrôle ?  
- Quelle campagne de promotion saisonnière a eu le meilleur taux d’achat : soldes d’été, soldes d’automne ou soldes d’hiver ?
- Quelles notifications push dans ce Canvas ont les taux d’ouvertures les plus élevés ?
- Quelles sont les étapes de ce groupe de Canvas qui ont eu le plus de conversions ?
- Quelle version d’un e-mail de bienvenue (version 1 ou 2) a eu le meilleur engagement et les meilleures conversions ? Les changements ont-ils fonctionné ?
- Quel est l'impact des différentes méthodes de réception/distribution (par exemple, 3 pushs planifiés, 3 pushs basés sur des actions et 3 pushs déclenchés par l'API) sur vos taux d'ouverture, vos taux de conversion ou vos taux d'achat ?
- Les améliorations continues aux messages envoyés aux utilisateurs inactifs ont-elles amélioré les indicateurs clés de performance au fil du temps ?

{% alert tip %}
Essayez d'utiliser les mêmes événements de conversion pour la conversion A, B, et ainsi de suite dans les campagnes et les Canevas que vous souhaitez comparer, afin de pouvoir aligner ces conversions dans vos rapports Report Builder.
{% endalert %}

## Exécuter un rapport

### Étape 1 : Créer un nouveau rapport

Dans le tableau de bord, sélectionnez **Analyse** > **Générateur de rapports**.

Sélectionnez **Créer un nouveau rapport** et choisissez soit un rapport de comparaison de campagne, soit un rapport de comparaison de Canvas.

Si vous choisissez d'exécuter un rapport sur les campagnes, vous pouvez choisir entre un rapport **manuel** ou **automatisé**. Les rapports peuvent contenir des campagnes ou des Canvas, mais pas les deux ensembles. Toutes les campagnes et les Canvas avec des messages envoyés au cours des 12 derniers mois peuvent être prises en compte dans un rapport.

![Tableau de bord de la campagne]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

Voici les différences entre ces deux options :

| **Action** | **Manual (Manuel)** | **Automatisé** |
| ---- | ---------- | ------------- |
| **Créer un rapport** | Vous pourrez affiner votre liste de campagnes à l’aide des filtres, puis cocher les campagnes spécifiques. | Vous allez créer votre rapport en utilisant les options de filtre pour affiner votre liste de campagnes. |
| **Enregistrer et afficher un rapport** | Vous pouvez enregistrer votre rapport. La prochaine fois que vous l’afficherez, vous pourrez visualiser la même campagne que vous aviez précédemment ajoutée, car ces campagnes seront toujours dans la catégorie de filtre « Dernier envoi ». | Vous pouvez enregistrer votre rapport. La prochaine fois que vous l’afficherez, le rapport sera automatiquement mis à jour pour inclure toutes les campagnes qui correspondent actuellement à vos filtres. |
| **Modifier un rapport** | Vous pouvez sélectionner **Modifier le rapport** pour ajouter ou supprimer des campagnes de votre rapport. | Vous pouvez modifier votre rapport en ajustant vos critères de filtre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Les rapports **manuels** et **automatisés** peuvent inclure un maximum de 250 campagnes dans un rapport.
{% endalert %}

Les rapports Canvas fonctionnent de manière similaire à un rapport de campagne manuel, dans le sens où les sélections de Canvas et les mises à jour de rapport doivent également être faites manuellement. Vous pouvez inclure au maximum cinq Canvas dans un seul rapport.

### Étape 2 : Choisissez vos indicateurs

Après avoir créé votre rapport, vous trouverez un tableau vierge contenant des campagnes dans chaque ligne. Le tableau se remplit une fois que vous avez sélectionné **Modifier les colonnes** et choisi les indicateurs que vous souhaitez ajouter.

![Options de campagne]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Votre tableau remplira les indicateurs que vous choisissez. Pour connaître les définitions de ces indicateurs, reportez-vous au [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/). Certains indicateurs sont uniquement disponibles pour les rapports de comparaison de campagne.

Vous pouvez également basculer vers les calculs de la **moyenne** de n'importe quel taux ou indicateur numérique et du **total** de n'importe quel indicateur numérique.

### Étape 3 : Choisir une période

Vous pouvez sélectionner une période spécifique pour les données de votre rapport. Si une campagne, un Canvas, une variante du Canvas ou un composant du Canvas ne dispose pas de données pour la période sélectionnée, les résultats pour cette ligne seront vides. 

![Indicateurs numériques de la campagne]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Étape 4 : Nommez et enregistrez votre rapport

Nommez votre rapport avant de l’enregistrer. Si un rapport est enregistré sans être nommé, Braze appliquera un nom « Campaign Comparison Report » (Rapport de comparaison de campagne) par défaut.

![Note de campagne]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Lorsque vous êtes prêt, sélectionnez **Enregistrer.** Les rapports enregistrés peuvent être consultés ultérieurement sur la page du **générateur de rapports.**

## Rapport de comparaison de campagnes avec campagnes multivariées

Pour toutes les campagnes multivariées, vous pouvez afficher la répartition de ces indicateurs pour vos variantes et le groupe de contrôle en cliquant sur la flèche à côté du nom de la campagne. Les lignes contenant vos variantes incluront les résultats de performance pour cette variante, et la ligne contenant votre contrôle inclura uniquement les résultats pour vos événements de conversion. 

![Note de campagne]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Les indicateurs qui remplissent la ligne de votre campagne globale reflètent les performances de ses variantes, mais n'incluent pas les performances du contrôle. Par exemple, l'événement de conversion principal A de votre campagne globale sera la somme des événements de conversion principaux A de vos variantes, sans compter l'événement de conversion principal A de votre contrôle.

{% alert important %}
Si vous supprimez une variante d'une campagne multivariante, les données de cette variante ne pourront plus être utilisées dans un rapport ultérieur.
{% endalert %}

## Ventilation du rapport de comparaison Canvas

Dans un rapport Canvas, vous pouvez afficher vos Canvas ventilés par variante, par étapes ou par message.

### Variante

En sélectionnant la **ventilation par variante**, vous pouvez afficher les statistiques de haut niveau pour l'ensemble de vos toiles, ainsi que les statistiques pour chaque variante, qui peuvent être développées en sélectionnant la flèche située à côté du nom de la toile.

![Variantes]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Étapes 

La sélection de la **ventilation par étapes** vous permet de visualiser les indicateurs au niveau des étapes, chaque ligne du rapport contenant la ligne d'une étape.

![Étapes]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Message

Comme pour la ventilation au niveau des étapes, la sélection de la **ventilation par message** permet d'afficher le nom des étapes dans chaque ligne. Cependant, dans les **colonnes de modification**, vous aurez accès à des indicateurs au niveau des messages, tels que des statistiques spécifiques aux canaux, comme les clics d'e-mail et les ouvertures de push.

![Rapport]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Notez que vous pouvez prévisualiser les 50 premières lignes de votre rapport Canvas dans le tableau de bord de Braze. Vous pouvez accéder au rapport complet lorsque vous exportez un CSV.

## Pour accéder aux rapports enregistrés

Lorsque vous accédez à un **rapport manuel** enregistré, vous pouvez visualiser les mêmes campagnes que celles que vous avez précédemment ajoutées, étant donné que ces campagnes relèvent toujours de votre filtre "Dernier envoi".

Lorsque vous accédez à un **rapport automatique** enregistré, le rapport est automatiquement mis à jour pour inclure toutes les campagnes qui correspondent actuellement à vos filtres. Par exemple, si votre rapport filtre les campagnes avec l'étiquette "Promotion", chaque fois que vous consulterez ce rapport, vous pourrez voir toutes les campagnes avec l'étiquette "Promotion", même si ces campagnes ont été créées après la création de ce rapport.

## Modification des rapports

Dans un **rapport manuel**, vous pouvez modifier un rapport en sélectionnant **Modifier**. À partir de là, vous pouvez sélectionner ou désélectionner des campagnes à inclure dans votre rapport.

Dans un **rapport automatique**, il suffit de basculer vos filtres pour réduire les résultats de votre rapport.

## Exportation de rapports

Vous pouvez également sélectionner **Exporter** pour télécharger votre rapport au format CSV.

Si votre rapport contient des campagnes multivariantes, votre exportation inclura deux fichiers CSV : 

- Un fichier contenant uniquement les indicateurs de niveau supérieur pour chaque campagne
- Un fichier contenant des indicateurs au niveau de la variante

Le fichier contenant des indicateurs de variante aura un préfixe `variant_`. La première fois que vous exportez un rapport automatisé, une fenêtre contextuelle s'affiche, vous demandant d'autoriser le téléchargement de plusieurs fichiers - cliquez sur **Autoriser.**

![Campagne Télécharger]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exportation des rapports de comparaison Canvas

Votre exportation CSV reflétera la vue de ventilation sur laquelle vous vous trouviez lorsque vous avez sélectionné **Exporter**. Par exemple, si vous étiez sur la vue de ventilation au niveau de l'étape, votre exportation contiendra des données sur vos indicateurs d'étape. Pour exporter des données à partir d'un autre découpage, vous devez d'abord naviguer jusqu'à ce découpage et sélectionner **Exporter** à partir de là.

Si vous téléchargez un rapport Canvas ventilé par variante, vous recevrez deux fichiers CSV :

- Un fichier contenant uniquement des indicateurs de niveau supérieur pour chaque Canvas
- Un fichier contenant des indicateurs au niveau de la variante

## Création de graphiques 

Utilisez des graphiques pour visualiser un indicateur sélectionné dans votre rapport. Des graphiques sont disponibles pour les rapports comportant des campagnes et qui ont au moins un indicateur ajouté à leurs colonnes.

![Graphique des performances de la campagne avec les indicateurs Envoi de messages sélectionnés]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Par défaut, le graphique de chaque rapport affiche l’indicateur dans la première colonne du rapport. Pour sélectionner un indicateur différent à représenter graphiquement, choisissez-le dans la liste déroulante. Tout indicateur dans votre tableau de rapport pourra être affiché sur votre graphique.

Vous pouvez représenter graphiquement trois indicateurs maximum. Les unités de tous les indicateurs doivent être identiques. Par exemple, si vous choisissez un taux dans la première liste déroulante, alors seuls les taux seront disponibles dans la deuxième liste déroulante.

Si votre graphique ne contient qu’un seul indicateur, il affiche jusqu’à 30 campagnes par ordre décroissant en fonction de celui que vous avez sélectionné. Par exemple, si l’indicateur de votre graphique est des clics d’e-mail, votre graphique affichera les 30 campagnes d’emailing avec le plus de clics, classées en ordre décroissant. Si votre rapport contient plus de 30 campagnes, seules les 30 meilleures seront affichées dans le graphique. Si vous sélectionnez plusieurs indicateurs, votre graphique affichera uniquement les cinq campagnes les plus récentes en fonction du premier indicateur sélectionné.

Actuellement, les graphiques ne sont pas enregistrés lorsque vous sauvegardez un rapport.



