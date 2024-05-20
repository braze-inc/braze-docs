---
nav_title: Segment Insights
article_title: Segment Insights
page_order: 4
page_type: tutorial
tool: 
  - Segments
  - Rapports
description: "Cet article vous propose de découvrir comment utiliser, interpréter et partager des Segment Insights."
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Segment Insights

> Segment Insights vous permet d’évaluer rapidement et facilement la performance d’un segment par rapport à un autre dans un ensemble d’indicateurs clés de performance présélectionnés. 

Accédez à la page **Segment Insights** de votre tableau de bord, dans **Segments**, puis cliquez sur <i class="fas fa-plus"></i> **Ajouter un segment** pour afficher jusqu’à quatre segments différents par rapport à un segment de référence. 

![Tableau de bord de Segment Insights.][1]

Le segment de référence peut être un segment de votre choix ou un segment contenant tous vos utilisateurs. Segment Insights vous permet de comparer les statistiques suivantes :

| Mesure | Description | Formule |
| --------------------- | ------------- | ------------- |
| Fréquence de session | Nombre moyen de sessions quotidiennes des utilisateurs du segment | (nombre total de sessions)/(nombre de jours depuis la première session) |
| Temps depuis la première session | Temps moyen entre la première session des utilisateurs du segment et la date en cours | today - date de la première session |
| Temps depuis la dernière session | Temps moyen entre la dernière session des utilisateurs du segment et la date en cours | today - date de la dernière session |
| Revenu à vie | Revenu à vie moyen des utilisateurs du segment | Dépenses à vie de l’utilisateur |
| Temps avant le premier achat | Temps moyen entre la première session des utilisateurs du segment et le premier achat | date date du premier achat : date de la première session |
| Temps écoulé depuis le dernier achat | Temps moyen entre le dernier achat des utilisateurs du segment et la date en cours | today - date du dernier achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Vous pouvez facilement partager des comparaisons spécifiques avec vos collègues à l’aide de l’URL unique de la page. Vous pouvez également cliquer sous chaque segment pour afficher plus d’informations sur ce segment. Ces comparaisons se réinitialiseront lorsque vous passez d’un groupe d’apps à un autre.

![][2]

## Page Segment Details (Informations relatives au segment)

Les Segment Insights ont également été intégrées à la vue **Segment Details (Informations relatives au segment)**. Lorsque vous regardez un segment que vous avez configuré précédemment, vous trouverez les six mêmes statistiques que celles décrites dans la zone dynamique Segment Statistics (Statistiques de segment) de couleur grise. À partir de là, vous pouvez lancer rapidement l’outil Segment Insights pour comparer ce segment avec d’autres segments que vous avez configurés précédemment, mais cela aura pour effet de remplacer tous les segments que vous avez sélectionnés précédemment dans l’outil Segment Insights.

![][3]

## Exemples de cas d’utilisation {#insights-use-cases}

### Comparer l’utilisation démographique et les habitudes d’achat

L’une des meilleures utilisations de Segment Insights consiste à répondre à des questions concernant l’impact des données démographiques des utilisateurs sur l’utilisation des applications et l’efficacité de la campagne, notamment :

- Certaines données démographiques de l’utilisateur sont-elles nettement meilleures ou moins bonnes que la moyenne ?
- Dois-je repenser la localisation d’une campagne donnée ?
- Une campagne est-elle plus efficace que d’autres auprès d’un certain groupe démographique ?
- Quels objectifs dois-je fixer pour une campagne destinée à un certain groupe démographique ?

Les Segment Insights peuvent aider à identifier des différences entre les données démographiques des utilisateurs. L’exemple suivant montre une comparaison de la base d’utilisateurs d’une application en fonction de leur langue, illustrant comment les anglophones ont tendance à avoir une valeur à vie et des niveaux d’activité supérieurs aux locuteurs d’autres langues.

![][5]

Dans cet exemple, les germanophones s’étaient inscrits il y a plus longtemps en moyenne, ce qui pourrait expliquer pourquoi ils ne sont plus actifs. Cela pourrait être dû à une multitude de facteurs. Par exemple, le fait que l’application ait été lancée en Europe, mais est maintenant plus populaire aux États-Unis, où la plupart des gens parlent anglais ou espagnol. Pour obtenir des résultats plus probants lorsque vous analysez les indicateurs clés de performance des données démographiques, il est judicieux de tester les résultats d’une étude générale des données démographiques (par ex., si la langue impacte la valeur à vie de tous les utilisateurs) en examinant un groupe plus restreint et plus semblable, puis en vérifiant si les résultats restent identiques.

Pour améliorer les conversions parmi les locuteurs d’autres langues que l’anglais, une bonne première étape serait de [localiser les campagnes][10] en fonction de la langue de l’appareil de l’utilisateur et de s’assurer que ces messages ont un impact auprès des utilisateurs en utilisant une [campagne multivariée][11] pour tester différentes versions du message en langue étrangère.

### Comprendre les indicateurs de revenus plus élevés

Convertir des utilisateurs en acheteurs peut être difficile, et essayer de pousser de nouveaux utilisateurs ou des utilisateurs inactifs à effectuer un achat peut amener l’utilisateur à désinstaller votre application. Les Segment Insights peuvent vous aider à découvrir des actions qui incitent les utilisateurs à progresser dans l’entonnoir d’achat sans qu’ils n’achètent quoi que ce soit, par exemple, en ajoutant des éléments à leur liste de souhaits, en partageant des messages sur les réseaux sociaux ou ajoutant du contenu dans leurs favoris. Vous pouvez par exemple représenter l’impact que différents comportements ont sur les achats dans une application de commerce électronique.

![][7]

Dans ce cas, relativement peu d’utilisateurs sont inscrits à la newsletter, mais ces utilisateurs sont généralement plus actifs. Pour intéresser de nouveaux utilisateurs, il peut être judicieux d’inclure une invitation dans les campagnes d’onboarding afin d’inciter les utilisateurs à s’inscrire à la newsletter. Pour réimpliquer des utilisateurs inactifs, un plan efficace serait d’envoyer une [campagne d’utilisateurs inactifs][9] standard et de cibler des [utilisateurs qui ont été convertis][12] par une campagne ultérieure pour qu’ils s’inscrivent à la newsletter.

[1]: {% image_buster /assets/img_archive/segment_insights.png %}
[2]: {% image_buster /assets/img_archive/Segment_Insights_Info.png %}
[3]: {% image_buster /assets/img_archive/Segment_Segment_Insights.png %}
[5]: {% image_buster /assets/img_archive/Segment_Language_Insights.png %}
[7]: {% image_buster /assets/img_archive/Segment_Insights_Events1.png %}
[8]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[10]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter
