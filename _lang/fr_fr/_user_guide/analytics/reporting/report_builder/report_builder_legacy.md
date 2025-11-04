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

> Le générateur de rapports vous permet de comparer les résultats de plusieurs campagnes ou Canvas dans une seule vue afin que vous puissiez facilement déterminer quelles stratégies d'engagement ont eu le plus d'impact sur vos indicateurs clés. Pour les campagnes comme pour les toiles, vous pouvez exporter vos données et enregistrer votre rapport pour le consulter ultérieurement.<br><br>Pour obtenir une liste descriptive des indicateurs que vous trouverez dans vos rapports, reportez-vous au [glossaire des indicateurs de rapport.]({{site.baseurl}}/user_guide/data/report_metrics/)

!Exemple de comparaison de campagne]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Utilisez ce rapport pour répondre aux principales questions d'engagement, par exemple :

- Quelles ont été les campagnes ou les canevas les plus performants pour une étiquette ou un canal spécifique ?
- Quelles variantes des campagnes multivariantes ont eu le plus d'impact sur le contrôle ?  
- Quelle campagne de promotion saisonnière a conduit à un taux d'achat plus élevé - les soldes d'été, les soldes d'automne ou les soldes d'hiver ?
- Quelles notifications push au sein de ce Canvas ont eu les taux d'ouverture les plus élevés ?
- Quelles sont les étapes de ce groupe de toiles qui ont obtenu le plus de conversions ?
- La version 1 d'un e-mail de bienvenue ou la version 2 d'un e-mail de bienvenue ont-elles conduit à un engagement et à une conversion plus élevés ? Les changements ont-ils fonctionné ?
- Quel est l'impact des différentes méthodes de réception/distribution (par exemple, 3 pushs planifiés, 3 pushs basés sur des actions et 3 pushs déclenchés par l'API) sur vos taux d'ouverture, vos taux de conversion ou vos taux d'achat ?
- Les améliorations constantes apportées aux envois de messages des utilisateurs ont-elles eu un impact positif sur vos indicateurs clés de performance au fil du temps ?

{% alert tip %}
Essayez d'utiliser les mêmes événements de conversion pour la conversion A, B, et ainsi de suite dans les campagnes et les Canevas que vous souhaitez comparer, afin de pouvoir aligner ces conversions dans vos rapports Report Builder.
{% endalert %}

## Exécuter un rapport

### Étape 1 : Créer un nouveau rapport

Dans le tableau de bord, accédez à **Analyse/analytique** > Générateur de rapports (si vous l'utilisez).

Sélectionnez **Créer un nouveau rapport** et choisissez un rapport de comparaison de campagne ou un rapport de comparaison de Canvas.

Si vous choisissez d'exécuter un rapport sur les campagnes, vous pouvez choisir entre un rapport **manuel** ou **automatisé**. Les rapports peuvent contenir des campagnes ou des toiles, mais pas les deux à la fois. Toutes les campagnes et tous les Canevas dont le dernier envoi de messages remonte à moins de 12 mois pourront faire l'objet d'un rapport.

!tableau de bord de la campagne]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

Vous trouverez ci-dessous les différences entre ces deux options :

| **Action** | **Manuel** | **Automatisé** |
| ---- | ---------- | ------------- |
| **Créer un rapport** | Vous pourrez réduire la liste de vos campagnes à l'aide de filtres, puis cocher des campagnes spécifiques. | Vous créerez votre rapport en utilisant les options de filtrage pour réduire la liste de vos campagnes. |
| **Enregistrer et consulter le rapport** | Vous pouvez enregistrer votre rapport. La prochaine fois que vous la consulterez, vous pourrez voir la même campagne que celle que vous avez ajoutée précédemment, car ces campagnes relèvent toujours de votre filtre "Dernier envoi". | Vous pouvez enregistrer votre rapport. La prochaine fois que vous le consulterez, le rapport sera automatiquement mis à jour pour inclure toutes les campagnes qui correspondent actuellement à vos filtres. |
| **Modifier le rapport** | Vous pouvez sélectionner **Modifier le rapport** pour ajouter ou supprimer des campagnes de votre rapport. | Vous pouvez modifier votre rapport en ajustant vos critères de filtrage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Les rapports **manuels** et **automatisés** peuvent inclure un maximum de 250 campagnes dans un rapport.
{% endalert %}

Les rapports Canvas fonctionnent de la même manière qu'un rapport de campagne manuel dans la mesure où les sélections Canvas et les mises à jour des rapports doivent également être effectuées manuellement. Vous pouvez inclure au maximum cinq toiles dans un rapport.

### Étape 2 : Choisissez vos indicateurs

Après avoir créé votre rapport, vous trouverez un tableau vierge contenant des campagnes dans chaque ligne. Le tableau se remplit une fois que vous avez sélectionné **Modifier les colonnes** et choisi les indicateurs que vous souhaitez ajouter.

!Options de campagne]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Votre tableau se remplit avec les indicateurs que vous avez choisis. Pour connaître les définitions de ces indicateurs, reportez-vous au [glossaire des indicateurs du rapport.]({{site.baseurl}}/user_guide/data/report_metrics/) Certains indicateurs ne sont disponibles que pour les rapports de comparaison des campagnes.

Vous pouvez également basculer les calculs de la **moyenne** de n'importe quel taux ou indicateur numérique et du **total de** n'importe quel indicateur numérique.

### Étape 3 : Choisissez une période

Vous pouvez sélectionner une période spécifique pour visualiser les données de votre rapport. Si une campagne, un Canvas, une variante du Canvas ou un composant du Canvas ne dispose pas de données pour la période sélectionnée, les résultats pour cette ligne seront vides. 

!métrique numérique de la campagne]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Étape 4 : Nommez et enregistrez votre rapport

Donnez un nom à votre rapport avant de l'enregistrer. Si vous enregistrez un rapport sans lui donner de nom, Braze lui attribuera par défaut le nom de "Rapport de comparaison des campagnes".

!Note de campagne]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Lorsque vous êtes prêt, sélectionnez **Enregistrer.** Les rapports enregistrés peuvent être consultés ultérieurement sur la page du **générateur de rapports.** 

## Rapport de comparaison des campagnes avec les campagnes multivariées

Pour toutes les campagnes multivariées, vous pouvez consulter ces indicateurs ventilés par vos variantes et votre groupe de contrôle en cliquant sur la flèche située à côté du nom de la campagne. Les lignes contenant vos variantes incluront les résultats de performance pour cette variante, et la ligne contenant votre contrôle inclura uniquement les résultats de vos événements de conversion. 

!Note de campagne]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Les indicateurs qui remplissent la ligne de votre campagne globale reflètent les performances de ses variantes, mais n'incluent pas les performances du contrôle. Par exemple, l'événement de conversion principal A de votre campagne globale sera la somme des événements de conversion principaux A de vos variantes, sans compter l'événement de conversion principal A de votre contrôle.

{% alert important %}
Si vous supprimez une variante d'une campagne multivariante, les données de cette variante ne pourront plus être utilisées dans un rapport ultérieur.
{% endalert %}

## Ventilation du rapport de comparaison des toiles

Dans un rapport sur les canevas, vous pouvez visualiser vos canevas ventilés par variante, étape ou message.

### Variante

En sélectionnant la **ventilation par variante**, vous pouvez afficher les statistiques de haut niveau pour l'ensemble de vos toiles, ainsi que les statistiques pour chaque variante, qui peuvent être développées en sélectionnant la flèche située à côté du nom de la toile.

!Variantes]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Étapes 

La sélection de la **ventilation par étapes** vous permet de visualiser les indicateurs au niveau des étapes, chaque ligne du rapport contenant la ligne d'une étape.

\![Marchepieds]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Message

Comme pour l'éclatement par étapes, la sélection de l'**éclatement par message** permet d'afficher le nom des étapes dans chaque ligne. Cependant, dans les **colonnes de modification**, vous aurez accès à des indicateurs au niveau des messages, tels que des statistiques spécifiques aux canaux, comme les clics d'e-mail et les ouvertures de push.

\![Rapport]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Notez que dans le tableau de bord de Braze, vous pouvez prévisualiser les 50 premières lignes de votre rapport Canvas. Vous pouvez accéder au rapport complet lorsque vous exportez un fichier CSV.

## Accès aux rapports enregistrés

Lorsque vous accédez à un **rapport manuel** enregistré, vous pouvez visualiser les mêmes campagnes que celles que vous avez précédemment ajoutées, étant donné que ces campagnes relèvent toujours de votre filtre "Dernier envoi".

Lorsque vous accédez à un **rapport automatique** enregistré, le rapport est automatiquement mis à jour pour inclure toutes les campagnes qui correspondent actuellement à vos filtres. Par exemple, si votre rapport filtre les campagnes avec l'étiquette "Promotion", chaque fois que vous consulterez ce rapport, vous pourrez voir toutes les campagnes avec l'étiquette "Promotion", même si ces campagnes ont été créées après la création de ce rapport.

## Modifier les rapports

Dans un **rapport manuel**, vous pouvez modifier un rapport en sélectionnant **Modifier**. De là, vous pouvez sélectionner ou désélectionner les campagnes à inclure dans votre rapport.

Dans un **rapport automatique**, il vous suffit de basculer vos filtres pour réduire les résultats de votre rapport.

## Exportation de rapports

Vous pouvez également sélectionner **Exporter** pour télécharger votre rapport au format CSV.

Si votre rapport contient des campagnes multivariantes, votre exportation comprendra deux fichiers CSV : 

- Un fichier contenant uniquement les indicateurs de premier niveau pour chaque campagne.
- Un fichier contenant les indicateurs au niveau de la variante

Le fichier contenant les indicateurs variants aura `variant_` ajouté au début de son nom. La première fois que vous exportez un rapport automatisé, une fenêtre contextuelle s'affiche, vous demandant d'autoriser le téléchargement de plusieurs fichiers - cliquez sur **Autoriser**.

!Téléchargement de la campagne]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exportation des rapports de comparaison des toiles

Votre exportation CSV reflétera la vue de ventilation sur laquelle vous vous trouviez lorsque vous avez sélectionné **Exporter**. Par exemple, si vous étiez sur la vue de ventilation au niveau de l'étape, votre exportation contiendra des données sur vos indicateurs d'étape. Pour exporter des données à partir d'un autre découpage, vous devez d'abord naviguer jusqu'à ce découpage et sélectionner **Exporter** à partir de là.

Si vous téléchargez un rapport Canvas sur la répartition des variantes, vous recevrez deux fichiers CSV :

- Un fichier contenant uniquement les indicateurs de premier niveau pour chaque Canvas
- Un fichier contenant les indicateurs au niveau de la variante

## Créer des tableaux 

Utilisez des indicateurs pour visualiser une mesure sélectionnée dans votre rapport. Les graphiques sont disponibles pour les rapports qui présentent des fonctionnalités de campagnes et dont au moins un indicateur a été ajouté à ses colonnes.

Graphique des performances de la campagne avec l'indicateur Message envoyé sélectionné]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Par défaut, le graphique de chaque rapport affiche l'indicateur dans la première colonne du rapport. Pour sélectionner un indicateur différent, choisissez votre indicateur dans le menu déroulant. Tous les indicateurs de votre tableau de rapport pourront être affichés dans votre graphique.

Vous pouvez représenter graphiquement trois indicateurs au maximum. Les unités de tous les indicateurs doivent être identiques - par exemple, si vous choisissez un taux dans la première liste déroulante, seuls les taux pourront être sélectionnés dans la deuxième liste déroulante.

Si votre graphique ne contient qu'un seul indicateur, il affichera jusqu'à 30 campagnes par ordre décroissant en fonction de l'indicateur que vous avez sélectionné. Par exemple, si les indicateurs de votre graphique sont les clics sur les e-mails, votre graphique affichera les 30 campagnes d'e-mails ayant obtenu le plus grand nombre de clics, par ordre décroissant de clics. Si votre rapport contient plus de 30 campagnes, seules les 30 premières seront affichées dans le graphique. Si vous sélectionnez plusieurs indicateurs, votre graphique n'affichera que les cinq campagnes les plus performantes sur la base du premier indicateur sélectionné.

Actuellement, les graphiques ne sont pas enregistrés lorsque vous enregistrez votre rapport.



