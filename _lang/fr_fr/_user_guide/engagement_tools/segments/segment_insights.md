---
nav_title: Statistiques des segments
article_title: Statistiques des segments
page_order: 8
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

Accédez à la page **Statistiques des segments de** votre tableau de bord, sous **Analyse/analytique**, et pour afficher jusqu'à 10 segments différents comparés à une base de référence.

![Tableau de bord des informations segments comparant trois segments, "Utilisateurs britanniques", "Utilisateurs français" et "Utilisateurs canadiens", à un segment de référence, "Tous les utilisateurs".]({% image_buster /assets/img_archive/segment_insights.png %})

Le segment de référence peut être un segment de votre choix ou un segment contenant tous vos utilisateurs. Segment Insights vous permet de comparer les statistiques suivantes :

| Mesure | Description | Formule |
| --------------------- | ------------- | ------------- |
| Nombre de sessions par jour | Nombre moyen de sessions quotidiennes des utilisateurs du segment | (nombre total de sessions)/(nombre de jours depuis la première session) |
| Nombre de jours depuis la première session | Nombre moyen de jours entre la première session des utilisateurs de la segmentation et maintenant | aujourd’hui : date de la première session |
| Nombre de jours écoulés depuis la dernière session | Nombre moyen de jours entre la dernière session des utilisateurs de la segmentation et maintenant | aujourd’hui : date de la dernière session |
| Revenus à vie en dollars | Chiffre d'affaires moyen sur la durée de vie en dollars pour les utilisateurs du segment | Dépenses à vie de l’utilisateur |
| Nombre de jours depuis le premier achat | Nombre moyen de jours entre la première session et le premier achat des utilisateurs de la segmentation | date du premier achat : date de la première session |
| Nombre de jours depuis le dernier achat | Nombre moyen de jours entre le dernier achat des utilisateurs de la segmentation et maintenant | aujourd’hui : date du dernier achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous pouvez facilement partager des comparaisons spécifiques avec vos coéquipiers en utilisant l'URL unique de la page, et vous pouvez également sélectionner l'icône de l'œil à côté de chaque segment pour révéler plus d'informations sur ce segment. Ces comparaisons seront réinitialisées lorsque vous changerez d'espace de travail.

![Détails du segment "Utilisateurs Premium (iOS VideoApp)" avec un graphique affichant l'historique des adhésions et un graphique qui décompose la taille estimée pour les différents canaux d'envoi de messages.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}).{: style="max-width:50%;"}

## Page Segment Details (Informations relatives au segment)

Les informations sur les segments ont également été intégrées directement dans la vue **Segment Details**. Lors de l'examen d'un segment particulier que vous avez précédemment configuré, vous pouvez trouver les mêmes six statistiques décrites dans la boîte grise dynamique des statistiques de segment. À partir de là, vous pouvez lancer rapidement l’outil Segment Insights pour comparer ce segment avec d’autres segments que vous avez configurés précédemment, mais cela aura pour effet de remplacer tous les segments que vous avez sélectionnés précédemment dans l’outil Segment Insights.

![]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Cas d'utilisation {#insights-use-cases}

### Comparer l’utilisation démographique et les habitudes d’achat

L’une des meilleures utilisations de Segment Insights consiste à répondre à des questions concernant l’impact des données démographiques des utilisateurs sur l’utilisation des applications et l’efficacité de la campagne, notamment :

- Certaines données démographiques de l’utilisateur sont-elles nettement meilleures ou moins bonnes que la moyenne ?
- Dois-je repenser la localisation d’une campagne donnée ?
- Une campagne est-elle plus efficace que d’autres auprès d’un certain groupe démographique ?
- Quels objectifs dois-je fixer pour une campagne destinée à un certain groupe démographique ?

Les Segment Insights peuvent aider à identifier des différences entre les données démographiques des utilisateurs. L’exemple suivant montre une comparaison de la base d’utilisateurs d’une application en fonction de leur langue, illustrant comment les anglophones ont tendance à avoir une valeur à vie et des niveaux d’activité supérieurs aux locuteurs d’autres langues.

![Statistiques des segments ventilées pour les segments anglais, allemand, français et espagnol.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

Dans cet exemple, les germanophones s’étaient inscrits il y a plus longtemps en moyenne, ce qui pourrait expliquer pourquoi ils ne sont plus actifs. Cela pourrait être dû à une multitude de facteurs. Par exemple, le fait que l’application ait été lancée en Europe, mais est maintenant plus populaire aux États-Unis, où la plupart des gens parlent anglais ou espagnol. Pour des résultats plus robustes, lors de l'analyse des KPI à travers les données démographiques, il est judicieux de tester les résultats d'une étude générale des données démographiques (par exemple, si la langue impacte la valeur à vie des utilisateurs) en examinant une population plus petite et plus similaire pour voir si les résultats persistent.

Pour améliorer les conversions parmi les locuteurs de langues autres que l'anglais, une bonne première étape consisterait à [localiser les campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) dans la langue de l'appareil de l'utilisateur et à s'assurer que le texte de ces messages suscite l'intérêt des utilisateurs en utilisant une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests) pour tester différentes versions du texte en langue étrangère.

### Comprendre les indicateurs de revenus plus élevés

Convertir des utilisateurs en acheteurs peut être difficile, et essayer de pousser de nouveaux utilisateurs ou des utilisateurs inactifs à effectuer un achat peut amener l’utilisateur à désinstaller votre application. Les informations exploitables par segment peuvent vous aider à découvrir des actions qui conduisent les utilisateurs plus loin dans l'entonnoir d'achat sans qu'ils aient besoin d'acheter tout de suite, par exemple en s'abonnant à votre newsletter, en partageant sur les réseaux sociaux ou en s'inscrivant pour recevoir des messages promotionnels. Par exemple, vous pouvez déterminer l'impact sur les achats des différents comportements au sein d'une application de commerce électronique.

![Statistiques des segments pour les utilisateurs qui ont partagé sur les réseaux sociaux, se sont inscrits à des promotions et à des bulletins d'information.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

Dans ce cas, relativement peu d'utilisateurs sont actuellement inscrits à des messages promotionnels et ne sont pas aussi actifs, mais ces utilisateurs génèrent un chiffre d'affaires à vie plus élevé. Pour augmenter le chiffre d'affaires, il peut être judicieux d'inclure une invitation à s'inscrire à des messages promotionnels dans les campagnes d'onboarding. Pour réengager les anciens utilisateurs, un bon plan consisterait à envoyer une [campagne type pour les anciens utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) et à cibler les [utilisateurs qui se sont convertis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter) avec une campagne ultérieure pour s'inscrire à des messages promotionnels.

