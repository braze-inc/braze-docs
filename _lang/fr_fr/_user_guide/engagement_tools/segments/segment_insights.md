---
nav_title: Statistiques des segments
article_title: Statistiques des segments
page_order: 8
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "Cet article pratique vous explique comment utiliser, interpréter et partager les statistiques des segments."
---

# ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"} Statistiques des segments

> Apprenez à utiliser, interpréter et partager les statistiques des segments. 

Les statistiques des segments vous montrent les performances d'un segment par rapport à un autre sur un ensemble d'indicateurs clés de performance présélectionnés.

## Visualisation des statistiques des segments

Accédez à la page **Statistiques des segments de** votre tableau de bord, sous **Analyse/analytique**, et pour afficher jusqu'à 10 segments différents comparés à une base de référence.

!tableau de bord Segment Insights comparant trois segments, "UK Users", "FR Users", et "CA Users" à un segment de référence, "All Users".]({% image_buster /assets/img_archive/segment_insights.png %})

Le segment de référence peut être soit un segment spécifique que vous sélectionnez, soit un segment contenant tous vos utilisateurs. Vous pouvez comparer les statistiques suivantes à l'aide de Segment Insights :

| Mesures | Description | Formule |
| --------------------- | ------------- | ------------- |
| Sessions par jour | Nombre moyen de sessions par utilisateur du segment par jour | (nombre total de séances) / (nombre de jours depuis la première séance) |
| Jours depuis la première session | Nombre moyen de jours entre la première session des utilisateurs de la segmentation et maintenant | aujourd'hui - date de la première session |
| Jours écoulés depuis la dernière session | Nombre moyen de jours entre la dernière session des utilisateurs de la segmentation et maintenant | aujourd'hui - date de la dernière session |
| Chiffre d'affaires à vie en dollars | Chiffre d'affaires moyen sur la durée de vie en dollars pour les utilisateurs du segment | dépenses des utilisateurs pendant toute la durée de vie de l'appareil |
| Nombre de jours depuis le premier achat | Nombre moyen de jours entre la première session et le premier achat des utilisateurs de la segmentation | date du premier achat - date de la première session |
| Nombre de jours depuis le dernier achat | Nombre moyen de jours entre le dernier achat des utilisateurs de la segmentation et maintenant | aujourd'hui - date du dernier achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous pouvez facilement partager des comparaisons spécifiques avec vos coéquipiers en utilisant l'URL unique de la page, et vous pouvez également sélectionner l'icône de l'œil à côté de chaque segment pour révéler plus d'informations sur ce segment. Ces comparaisons sont réinitialisées lorsque vous passez d'un espace de travail à l'autre.

\![Détails pour le segment "Utilisateurs Premium (iOS VideoApp)" avec un graphique affichant l'historique des adhésions et un graphique qui décompose la taille estimée pour les différents canaux d'envoi de messages.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Page de détails sur les segments

Des statistiques des segments ont également été créées dans la vue des **détails du segment**. Lorsque vous examinez une segmentation particulière que vous avez précédemment définie, vous pouvez trouver les six mêmes statistiques dans la boîte grise dynamique "Statistiques du segment". À partir de là, vous pouvez rapidement lancer l'outil Statistiques des segments pour comparer ce segment particulier avec tous les autres que vous avez précédemment configurés, mais notez que cela écrasera tous les segments que vous avez précédemment sélectionnés dans l'outil Statistiques des segments.

\![]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Cas d'utilisation {#insights-use-cases}

### Comparaison des tendances démographiques en matière d'utilisation et d'achat

L'une des meilleures utilisations des statistiques des segments consiste à répondre aux questions concernant l'impact des données démographiques des utilisateurs sur l'utilisation de l'app et l'efficacité des campagnes, telles que :

- Certaines catégories d'utilisateurs ont-elles des performances nettement supérieures ou inférieures à la moyenne ?
- Dois-je repenser la localisation d'une campagne particulière ?
- Une campagne attire-t-elle un certain public ?
- Quels objectifs dois-je fixer pour une campagne destinée à un certain public ?

Les statistiques des segments peuvent aider à découvrir les différences entre les données démographiques des utilisateurs. L'exemple suivant montre une comparaison de la base d'utilisateurs d'une appli en fonction de leur langue, illustrant comment les anglophones ont tendance à avoir des niveaux de LTV et d'activité plus élevés que les locuteurs d'autres langues.

Statistiques des informations sur les segments pour l'anglais, l'allemand, le français et l'espagnol.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

Dans cet exemple, les germanophones se sont inscrits il y a plus longtemps en moyenne, ce qui pourrait expliquer pourquoi ils ne sont plus aussi actifs. Cela peut être dû à une multitude de facteurs. Par exemple, si l'application a d'abord été lancée en Europe, mais qu'elle est désormais plus populaire aux États-Unis, où la plupart des gens parlent anglais ou espagnol. Pour obtenir des résultats plus solides, il est judicieux, lors de l'analyse des ICP en fonction des données démographiques, de tester les conclusions d'une étude générale des données démographiques (par exemple, si la langue a une incidence sur la LTV chez tous les utilisateurs) en examinant une population plus restreinte et plus similaire et en vérifiant si les conclusions persistent.

Pour améliorer les conversions parmi les locuteurs de langues autres que l'anglais, une bonne première étape consisterait à [localiser les campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) dans la langue de l'appareil de l'utilisateur et à s'assurer que le texte de ces messages suscite l'intérêt des utilisateurs en utilisant une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests) pour tester différentes versions du texte en langue étrangère.

### Comprendre les indicateurs de l'augmentation des chiffres d'affaires

Il peut être difficile de convertir les utilisateurs en acheteurs, et le fait d'essayer de pousser les nouveaux utilisateurs, les utilisateurs inactifs ou désengagés à acheter directement peut conduire l'utilisateur à désinstaller votre application. Les informations exploitables par segment peuvent vous aider à découvrir des actions qui conduisent les utilisateurs plus loin dans l'entonnoir d'achat sans qu'ils aient besoin d'acheter tout de suite, par exemple en s'abonnant à votre newsletter, en partageant sur les réseaux sociaux ou en s'inscrivant pour recevoir des messages promotionnels. Par exemple, vous pouvez déterminer l'impact sur les achats des différents comportements au sein d'une application de commerce électronique.

Les statistiques des segments concernent les utilisateurs qui ont partagé des informations sur les réseaux sociaux, se sont inscrits à des promotions ou à des lettres d'information.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

Dans ce cas, relativement peu d'utilisateurs sont actuellement inscrits à des messages promotionnels et ne sont pas aussi actifs, mais ces utilisateurs génèrent un chiffre d'affaires à vie plus élevé. Pour augmenter le chiffre d'affaires, il peut être judicieux d'inclure une invitation à s'inscrire à des messages promotionnels dans les campagnes d'onboarding. Pour réengager les anciens utilisateurs, un bon plan consisterait à envoyer une [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) typique [pour les anciens utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) et à cibler les [utilisateurs qui se sont convertis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter) avec une campagne ultérieure pour s'inscrire à des messages promotionnels.

