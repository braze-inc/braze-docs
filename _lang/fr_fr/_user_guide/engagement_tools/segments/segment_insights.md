---
nav_title: Statistiques des segments
article_title: Statistiques des segments
page_order: 4
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "Cet article vous propose de découvrir comment utiliser, interpréter et partager des Segment Insights."
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Statistiques des segments

> Apprenez à utiliser, interpréter et partager les statistiques des segments. 

Les informations sur les segments vous montrent comment un segment se comporte par rapport à un autre sur un ensemble de KPI pré-sélectionnés.

## Affichage des informations sur le segment

Accédez à la page **Segment Insights** de votre tableau de bord, sous **Analytics**, et cliquez sur <i class="fas fa-plus"></i> **Ajouter un segment** pour voir jusqu'à quatre segments différents comparés à une référence.

![Tableau de bord de Segment Insights.][1]

Le segment de référence peut être un segment de votre choix ou un segment contenant tous vos utilisateurs. Segment Insights vous permet de comparer les statistiques suivantes :

| Mesure | Description | Formule |
| --------------------- | ------------- | ------------- |
| Fréquence des sessions | Nombre moyen de sessions quotidiennes des utilisateurs du segment | (nombre total de sessions)/(nombre de jours depuis la première session) |
| Temps depuis la première session | Temps moyen entre la première session des utilisateurs du segment et la date en cours | aujourd’hui : date de la première session |
| Temps depuis la dernière session | Temps moyen entre la dernière session des utilisateurs du segment et la date en cours | aujourd’hui : date de la dernière session |
| Revenus à vie | Revenu à vie moyen des utilisateurs du segment | Dépenses à vie de l’utilisateur |
| Délai avant le premier achat | Temps moyen entre la première session des utilisateurs du segment et le premier achat | date du premier achat : date de la première session |
| Temps écoulé depuis le dernier achat | Temps moyen entre le dernier achat des utilisateurs du segment et la date en cours | aujourd’hui : date du dernier achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous pouvez facilement partager des comparaisons spécifiques avec vos collègues à l’aide de l’URL unique de la page. Vous pouvez également cliquer sous chaque segment pour afficher plus d’informations sur ce segment. Ces comparaisons seront réinitialisées lorsque vous changerez d'espace de travail.

![][2]

## Page Segment Details (Informations relatives au segment)

Les informations sur les segments ont également été intégrées directement dans la vue **Segment Details**. Lors de l'examen d'un segment particulier que vous avez précédemment configuré, vous pouvez trouver les mêmes six statistiques décrites dans la boîte grise dynamique des statistiques de segment. À partir de là, vous pouvez lancer rapidement l’outil Segment Insights pour comparer ce segment avec d’autres segments que vous avez configurés précédemment, mais cela aura pour effet de remplacer tous les segments que vous avez sélectionnés précédemment dans l’outil Segment Insights.

![][3]

## Cas d'utilisation {#insights-use-cases}

### Comparer l’utilisation démographique et les habitudes d’achat

L’une des meilleures utilisations de Segment Insights consiste à répondre à des questions concernant l’impact des données démographiques des utilisateurs sur l’utilisation des applications et l’efficacité de la campagne, notamment :

- Certaines données démographiques de l’utilisateur sont-elles nettement meilleures ou moins bonnes que la moyenne ?
- Dois-je repenser la localisation d’une campagne donnée ?
- Une campagne est-elle plus efficace que d’autres auprès d’un certain groupe démographique ?
- Quels objectifs dois-je fixer pour une campagne destinée à un certain groupe démographique ?

Les Segment Insights peuvent aider à identifier des différences entre les données démographiques des utilisateurs. L’exemple suivant montre une comparaison de la base d’utilisateurs d’une application en fonction de leur langue, illustrant comment les anglophones ont tendance à avoir une valeur à vie et des niveaux d’activité supérieurs aux locuteurs d’autres langues.

![][5]

Dans cet exemple, les germanophones s’étaient inscrits il y a plus longtemps en moyenne, ce qui pourrait expliquer pourquoi ils ne sont plus actifs. Cela pourrait être dû à une multitude de facteurs. Par exemple, le fait que l’application ait été lancée en Europe, mais est maintenant plus populaire aux États-Unis, où la plupart des gens parlent anglais ou espagnol. Pour des résultats plus robustes, lors de l'analyse des KPI à travers les données démographiques, il est judicieux de tester les résultats d'une étude générale des données démographiques (par exemple, si la langue impacte la valeur à vie des utilisateurs) en examinant une population plus petite et plus similaire pour voir si les résultats persistent.

Pour améliorer les conversions parmi les locuteurs de langues autres que l'anglais, une bonne première étape serait de [localiser les campagnes][10] dans la langue de l'appareil de l'utilisateur et de s'assurer que le texte de ces messages engage les utilisateurs en utilisant une [campagne multivariée][11] pour tester différentes versions du texte en langue étrangère.

### Comprendre les indicateurs de revenus plus élevés

Convertir des utilisateurs en acheteurs peut être difficile, et essayer de pousser de nouveaux utilisateurs ou des utilisateurs inactifs à effectuer un achat peut amener l’utilisateur à désinstaller votre application. Les Segment Insights peuvent vous aider à découvrir des actions qui incitent les utilisateurs à progresser dans l’entonnoir d’achat sans qu’ils n’achètent quoi que ce soit, par exemple, en ajoutant des éléments à leur liste de souhaits, en partageant des messages sur les réseaux sociaux ou ajoutant du contenu dans leurs favoris. Par exemple, vous pouvez déterminer l'impact sur les achats des différents comportements au sein d'une application de commerce électronique.

![][7]

Dans ce cas, relativement peu d’utilisateurs sont inscrits à la newsletter, mais ces utilisateurs sont généralement plus actifs. Pour intéresser de nouveaux utilisateurs, il peut être judicieux d’inclure une invitation dans les campagnes d’onboarding afin d’inciter les utilisateurs à s’inscrire à la newsletter. Pour réengager les utilisateurs inactifs, un bon plan serait d'envoyer une [campagne typique pour les utilisateurs inactifs][9] et de cibler [les utilisateurs qui ont converti][12] avec une campagne ultérieure pour s'inscrire à la newsletter.

[1]: {% image_buster /assets/img_archive/segment_insights.png %}
[2]: {% image_buster /assets/img_archive/Segment_Insights_Info.png %}
[3]: {% image_buster /assets/img_archive/Segment_Segment_Insights.png %}
[5]: {% image_buster /assets/img_archive/Segment_Language_Insights.png %}
[7]: {% image_buster /assets/img_archive/Segment_Insights_Events1.png %}
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[10]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter
