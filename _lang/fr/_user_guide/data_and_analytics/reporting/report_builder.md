---
nav_title: Créateur de rapports
article_title: Créateur de rapports
alias: /report_builder/
page_order: 4
page_type: reference
description: "Cet article de référence explique les mises à jour de la fonctionnalité Créateur de rapports du tableau de bord."
tool: 
  - Rapports

---

# Créateur de rapports

> Le Créateur de rapports vous permet de comparer les résultats de plusieurs campagnes ou de plusieurs Canvas dans une vue unique pour déterminer rapidement quelles stratégies d’engagement ont le plus impacté vos indicateurs clés. Pour les campagnes et les Canvas, vous pouvez exporter vos données et enregistrer votre rapport pour une utilisation future.

![Exemple de comparaison de campagne][5]{: style="max-width:80%;"}

Utilisez ce rapport pour répondre aux questions clés d’engagement, par exemple :

- Quels étaient les campagnes ou les Canvas les plus performants pour une balise ou un canal spécifique ?
- Dans mes campagnes multivariantes, quelles variantes ont le mieux marché par rapport au contrôle ?  
- Quelle campagne de promotion saisonnière a eu le meilleur taux d’achat – soldes d’été, soldes d’automne ou soldes d’hiver ?
- Quelles notifications push dans ce Canvas ont les taux d’ouvertures les plus élevés ?
- Quelles sont les étapes de ce groupe de Canvas qui ont eu le plus de conversions ?
- Quelle version d’un e-mail de bienvenue (version 1 ou 2) a eu le meilleur engagement et les meilleures conversions ? Les changements ont-ils fonctionné ?
- Comment les différentes méthodes de livraison (par ex., 3 notifications push programmées, 3 notifications push basées sur les actions et 3 notifications push déclenchées par API) impactent-elles vos taux d’ouverture, de conversion ou d’achat ?
- Les améliorations continues aux messages envoyés aux utilisateurs inactifs ont-ils amélioré les indicateurs clés de performance au fil du temps ?

{% alert tip %}
Essayez d’utiliser les mêmes événements de conversion pour la conversion A, B, etc. entre les campagnes et les Canvas que vous souhaitez comparer, pour pouvoir aligner ces conversions dans vos rapports du Créateur de rapports.
{% endalert %}

## Exécuter un rapport

### Étape 1 : Créer un nouveau rapport

Dans le tableau de bord, naviguez jusqu’au **Report Builder (Créateur de rapports)** sur le panneau de gauche. Cliquez sur ** Create New Report** et sélectionnez un rapport de comparaison de campagne ou un rapport de comparaison de Canvas. 

Si vous choisissez d’exécuter un rapport sur les campagnes, vous pouvez choisir entre un rapport **Manual (Manuel)** ou **Automated (Automatisé)**. Les rapports peuvent contenir des campagnes ou des Canvas, mais pas les deux ensembles.

{% alert note %} 
Toutes les campagnes et les Canvas avec des messages envoyés au cours des 6 derniers mois peuvent être prises en compte dans un rapport. 
{% endalert %}

![Tableau de bord de la campagne][6]{: style="max-width:80%;"}

Voici les différences entre ces deux options :

| **Action** | **Manual (Manuel)** | **Automated (Automatisé)** |
| ---- | ---------- | ------------- |
| **Building Report (Créer un rapport)** | Vous pourrez affiner votre liste de campagnes à l’aide des filtres, puis cocher les campagnes spécifiques. | Vous construirez votre rapport en utilisant les options de filtre pour affiner votre liste de campagnes. |
| **Saving and Viewing Report (Enregistrement et affichage du rapport)** | Vous pouvez enregistrer votre rapport. La prochaine fois que vous l’afficherez, vous pourrez visualiser la même campagne que vous aviez précédemment ajoutée, car ces campagnes seront toujours dans la catégorie de filtre « Dernier envoi ». | Vous pouvez enregistrer votre rapport. La prochaine fois que vous l’afficherez, le rapport sera automatiquement mis à jour pour inclure toutes les campagnes qui correspondent actuellement à vos filtres. |
| **Editing Report (Modification du rapport)** | Vous pouvez cliquer sur Modifier le rapport pour ajouter ou supprimer des campagnes de votre rapport | Vous pouvez modifier votre rapport en ajustant vos critères de filtre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %} 
Qu’ils soient **Manual (Manuel)** ou **Automated (Automatisé)**, les rapports peuvent inclure un maximum de 250 campagnes. 
{% endalert %}

Les rapports Canvas fonctionnent de manière similaire à un rapport de campagne manuel, dans le sens où les sélections de Canvas et les mises à jour de rapport doivent également être faites manuellement. Vous pouvez inclure au maximum cinq Canvas dans un seul rapport.

### Étape 2 : Choisissez vos métriques

Une fois que vous avez créé votre rapport, vous trouverez un tableau vierge avec une campagne sur chaque ligne. Le tableau sera rempli une fois que vous aurez sélectionné **Edit Columns (Modifier les colonnes)** et choisi les valeurs que vous souhaitez ajouter. Ensuite, cliquez sur **Run Report** pour générer vos métriques.

![Options de campagne][15]{: style="max-width:80%;"}

Votre tableau remplira les métriques que vous choisissez. Pour les définitions de ces métriques, reportez-vous au [Glossaire des métriques du rapport][16]. Certaines métriques sont uniquement disponibles pour les rapports de comparaison de campagne.

Vous pouvez également basculer vers le calcul de la **Average (Moyenne)** pour toute métrique Numérique ou Taux (Pourcentage) ainsi que le **Total** pour toute métrique numérique.

### Étape 3 : Choisir une période

Vous pouvez sélectionner une période spécifique pour les données de votre rapport. Si une campagne, un Canvas, une variante ou un composant Canvas donnés n’ont pas de données pour la période sélectionnée, les résultats de cette ligne seront vides. 

![Indicateurs numériques de campagne][4]{: style="max-width:60%;"}

### Étape 4 : Nommez et enregistrez votre rapport

Nommez votre rapport avant de l’enregistrer. Si un rapport est enregistré sans être nommé, Braze appliquera un nom « Campaign Comparison Report » par défaut.

![Note de campagne][7]{: style="max-width:60%;"}

Lorsque vous êtes prêt, cliquez sur **Save (Enregistrer)**. Les rapports enregistrés peuvent être consultés ultérieurement sur la page **Report Builder (Créateur de rapports)**.

## Rapport de comparaison de campagnes avec campagnes multivariées

Pour toutes les campagnes multivariées, vous pouvez afficher la répartition de ces métriques pour vos variantes et le groupe de contrôle en cliquant sur la flèche à côté du nom de la campagne. Les lignes contenant vos variantes incluront les résultats de performance pour cette variante, et la ligne contenant votre contrôle inclura uniquement les résultats pour vos événements de conversion. 

![Note de campagne][3]{: style="float:right;max-width:15%;margin-left:15px;"}

Les métriques sur la ligne de votre campagne globale reflèteront la performance de ses variantes, mais pas les performances du contrôle. Par exemple, l’événement de conversion primaire A pour votre campagne globale sera la somme de l’événement de conversion primaire A pour vos variantes, et n’inclura pas l’événement de conversion primaire A pour votre contrôle.

{% alert important %} 
Si vous supprimez une variante d’une campagne multivariante, les données de cette variante ne seront pas disponibles dans les futurs rapports. 
{% endalert %}

## Ventilation du rapport de comparaison Canvas

Dans un rapport Canvas, vous pouvez afficher vos Canvas ventilés par variante, par étapes ou par message.

### Variante

Sélectionner **breakdown by variant (Ventilation par variante)** vous permettra de voir les statistiques de haut niveau pour vos Canvas globaux, ainsi que les statistiques pour chaque variante, qui peuvent être développées en cliquant sur la flèche à côté du nom de Canvas.

![Variantes][12]{: style="max-width:90%;"}

### Étapes 

Sélectionner **breakdown by steps (Ventilation par étapes)** vous permet d’afficher les métriques au niveau des étapes, chaque ligne du rapport affichant les données d’une étape.

![Étapes][13]{: style="max-width:90%;"}

### Message

Comme pour la ventilation au niveau Étapes, la sélection de **breakdown by message (Ventilation par message)** montre le nom des étapes sur chaque ligne. Dans les **edit columns (colonnes de modification)**, vous aurez cependant accès aux métriques au niveau du message, avec notamment des statistiques spécifiques aux canaux, comme les clics sur les e-mails et les ouvertures de notification push.

![Rapport][14]{: style="max-width:90%;"}

Notez que vous pouvez prévisualiser les 50 premières lignes de votre rapport Canvas dans le tableau de bord de Braze. Vous pouvez accéder au rapport complet lorsque vous exportez un CSV.

## Pour accéder aux rapports enregistrés

Quand vous accédez à un **Manual Report (Rapport manuel)** enregistré, vous pouvez voir les mêmes campagnes que lors de la dernière exécution du rapport, car ces campagnes sont toujours sous votre filtre « Dernier envoi ».

Lorsque vous accédez à un **Automatic Report (Rapport automatique)** enregistré, le rapport sera automatiquement mis à jour pour inclure toutes les campagnes qui correspondent actuellement à vos filtres. Par exemple, si votre rapport filtre les campagnes avec la balise « Promotion », chaque fois que vous affichez ce rapport, vous pourrez voir toutes les campagnes avec balise « Promotion », même si elles ont été créées après ce rapport.

## Modification des rapports

Un **Manual Report (Rapport manuel)** peut être modifié en cliquant sur **Edit (Modifier)**. À partir de là, vous pouvez sélectionner ou désélectionner des campagnes à inclure dans votre rapport.

Dans un **Automatic Report (Rapport automatique)**, il suffit de basculer les filtres pour affiner les résultats du rapport.

## Exportation de rapports

Vous pouvez également cliquer sur **Export (Exporter)** pour télécharger votre rapport au format CSV.

Si votre rapport contient des campagnes multivariantes, votre exportation inclura deux fichiers CSV : 

- Un fichier contenant uniquement les indicateurs de niveau supérieur pour chaque campagne
- Un fichier contenant des métriques de niveau variant

Le fichier contenant des métriques de variante aura un préfixe `variant_`. À la première exportation d’un rapport automatisé, vous verrez une fenêtre contextuelle vous demandant d’autoriser le téléchargement de plusieurs fichiers, cliquez sur **Allow (Autoriser)**.

![Téléchargement de campagne][8]{: style="max-width:60%;"}

### Exportation des rapports de comparaison Canvas

Votre exportation CSV reflètera la vue de ventilation sur laquelle vous étiez lorsque vous avez cliqué sur **Export (Exporter)**. Par exemple, si vous étiez sur la vue de ventilation au niveau des étapes, votre exportation contiendra des données sur vos métriques d’étapes. Pour exporter des données avec une ventilation différente, vous devez d’abord naviguer vers cette ventilation, et ensuite cliquer sur **Export (Exporter)**.

Si vous téléchargez un rapport Canvas ventilé par variante, vous recevrez deux fichiers CSV :

- Un fichier contenant uniquement des métriques de niveau supérieur pour chaque Canvas
- Un fichier contenant des métriques de niveau variant

## Création de graphiques 

{% alert important %} Les graphiques sont actuellement en accès anticipé. Nous allons souvent améliorer cette fonctionnalité, donc si vous avez un cas d’utilisation que vous ne pouvez pas faire maintenant, revenez bientôt pour voir si c’est possible. Si vous avez des commentaires sur les produits, merci de les soumettre via le [portail de commentaires sur les produits](https://dashboard.braze.com/resources/roadmap/). {% endalert %}

Utilisez des graphiques pour visualiser une métrique sélectionnée dans votre rapport. Des graphiques sont disponibles pour les rapports qui ont des campagnes et qui ont au moins une métrique ajoutée à leurs colonnes.

![Tableau Performance de campagne avec métrique Messages envoyés sélectionnée][17]

Par défaut, le graphique de chaque rapport affiche la métrique dans la première colonne du rapport. Pour sélectionner une métrique différente à représenter graphiquement, choisissez votre métrique dans la liste déroulante. Toute métrique dans votre tableau de rapport pourra être affichée sur votre graphique.

Vous pouvez représenter graphiquement trois métriques maximum. Les unités de toutes les métriques doivent être identiques, par exemple, si vous choisissez un taux dans la première liste déroulante, alors seuls les taux seront disponibles dans la deuxième liste déroulante.

Si votre graphique ne contient qu’une seule métrique, il affiche jusqu’à 30 campagnes par ordre décroissant en fonction de la métrique que vous avez sélectionnée. Par exemple, si la mesure de votre graphique est des clics d’e-mail, votre graphique affichera les 30 campagnes d’emailing avec le plus de clics, classées en ordre décroissant. Si votre rapport contient plus de 30 campagnes, seules les 30 meilleures seront affichées dans le graphique. Si vous sélectionnez plusieurs métriques, votre graphique affichera uniquement les cinq campagnes les plus récentes en fonction de la première métrique sélectionnée.

Actuellement, les graphiques ne sont pas enregistrés lorsque vous sauvegardez un rapport.




[3]: {% image_buster /assets/img/campaign_comparison/compare_note.png %}
[4]: {% image_buster /assets/img/campaign_comparison/metric.png %}
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %}
[6]: {% image_buster /assets/img/campaign_comparison/create_report.png %}
[7]: {% image_buster /assets/img/campaign_comparison/comparison_name.png %}
[8]: {% image_buster /assets/img/campaign_comparison/download.png %}
[12]: {% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}
[13]: {% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}
[14]: {% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}
[15]: {% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}
[17]: {% image_buster /assets/img/campaign_comparison/report_builder_charts.png %}

[16]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
