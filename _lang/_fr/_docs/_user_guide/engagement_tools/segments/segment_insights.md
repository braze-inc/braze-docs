---
nav_title: Aperçus du segment
article_title: Aperçus du segment
page_order: 4
page_type: tutoriel
tool:
  - Segments
  - Rapports
description: "Cet article pratique vous guidera dans la façon d'utiliser, d'interpréter et de partager des vues sur les segments."
---

# Aperçus du segment

> Cet article pratique vous guidera dans la façon d'utiliser, d'interpréter et de partager des vues sur les segments. <br> <br> Ces informations peuvent être utilisées pour cibler les utilisateurs et développer des campagnes marketing efficaces.

!\[Segment Insights Dash\]\[1\]

Segment Insights vous permet de voir rapidement et facilement comment un segment est performant par rapport à un autre segment à travers un ensemble d'ICP présélectionnés. Depuis la section segment de votre tableau de bord, En cliquant sur le bouton « Intuition de segmentations » en haut à droite de la page, vous trouverez un écran où jusqu'à quatre segments différents peuvent être comparés par rapport à une ligne de base. La ligne de base peut être soit un segment spécifique que vous sélectionnez soit les statistiques pour tous vos utilisateurs.  Actuellement, Braze peut comparer les statistiques suivantes sur la page Segment Insights :

| Mesure                                  | Libellé                                                                               | Formule                                                         |
| --------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Fréquence de la session                 | Nombre moyen d'utilisateurs du segment par jour                                       | (nombre total de sessions)/(# jours depuis la première session) |
| Temps écoulé depuis la première session | Temps moyen entre la première session des utilisateurs du segment et maintenant       | aujourd'hui - date de la première session                       |
| Temps écoulé depuis la dernière session | Temps moyen entre la dernière session des utilisateurs du segment et maintenant       | aujourd'hui - date de la dernière session                       |
| Revenus à vie                           | Revenus moyens à vie pour les utilisateurs du segment                                 | durée de vie de l'utilisateur                                   |
| Il est temps de commencer à acheter     | Temps moyen entre la première session des utilisateurs du segment et le premier achat | date du premier achat - date de la première session             |
| Temps écoulé depuis le dernier achat    | Temps moyen entre le dernier achat des utilisateurs du segment et maintenant          | aujourd'hui - date du dernier achat                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Vous pouvez facilement partager des comparaisons spécifiques avec l'URL unique de la page, et les utilisateurs peuvent également cliquer sous chaque segment pour révéler plus d'informations sur ce segment. Ces comparaisons seront réinitialisées lorsqu'un utilisateur change de groupe d'applications.

!\[Segment Insights étendu\]\[2\]

Segment Insights a également été intégré directement dans la vue détaillée du segment. Lorsque vous regardez un segment particulier que vous avez déjà mis en place, vous pouvez trouver les six mêmes statistiques décrites dans la boîte de statistiques dynamiques et grises. À partir d’ici, vous pouvez rapidement lancer l’outil Segment Insights pour comparer ce segment particulier avec tous les autres que vous avez précédemment configurés, mais notez que cela écrasera tous les segments que vous avez précédemment sélectionnés dans l'outil Segment Insights.

!\[Détails des Insights du Segment\]\[3\]

## Exemple de cas d'utilisation {#insights-use-cases}

### Comparaison de l'utilisation démographique et des modèles d'achat

L'une des meilleures utilisations de Segment Insights est de répondre aux questions sur l'impact de la démographie des utilisateurs sur l'utilisation de l'application et l'efficacité de la campagne, telles que:

- La démographie de certains utilisateurs est-elle nettement meilleure ou pire que la moyenne?
- Devrais-je repenser la localisation d'une campagne particulière?
- Une campagne implique-t-elle une certaine démographie ?
- Quels objectifs devrais-je fixer pour une campagne visant une certaine démographie ?

Segment Insights peut aider à découvrir les différences démographiques entre les utilisateurs. L'exemple ci-dessous montre une comparaison de la base d'utilisateurs d'une application par leur langue, illustrant comment les anglophones ont tendance à avoir un niveau de télédiffusion et d'activité supérieur à celui des locuteurs d'autres langues.

!\[Segment Insights by Language\]\[5\]

Notez qu'en moyenne, les orateurs allemands se sont inscrits plus longtemps, ce qui pourrait expliquer pourquoi ils ne sont plus aussi actifs. Cela peut être dû à une multitude de facteurs, par exemple, si l'application a été lancée pour la première fois en Europe mais est maintenant plus populaire dans les États-Unis. ., où la plupart des gens parlent anglais ou espagnol. Pour obtenir des résultats plus solides, il est raisonnable de tester les résultats d'une étude générale de la démographie (e. Si le langage a un impact sur LTV dans tous les utilisateurs) en regardant une population plus petite, plus similaire et en voyant si les conclusions persistent.

Améliorer les conversions entre les locuteurs de langues autres que l'anglais, une bonne première étape serait de [localiser les campagnes][10] dans la langue de l'appareil de l'utilisateur et de s'assurer que la copie de ces messages engage les utilisateurs en utilisant une [campagne multivariée][11] pour tester différentes versions de la copie de langue étrangère.

### Comprendre les indicateurs de revenus plus élevés

Obtenir des utilisateurs à convertir en acheteurs peut être difficile, et essayer de pousser de nouvelles, les utilisateurs inactifs ou désengagés directement vers l'achat peuvent conduire l'utilisateur à désinstaller votre application. Segment Insights peut vous aider à découvrir des actions qui poussent les utilisateurs vers le bas de l'entonnoir d'achat sans les obliger à acheter tout juste pour l'instant, par exemple, en ajoutant des éléments à leur liste de souhaits, en partageant sur les réseaux sociaux ou en favorisant le contenu. Voici un exemple illustrant l'impact sur l'achat de comportements différents au sein d'une application e-commerce.

!\[Actions des utilisateurs contribuant aux achats\]\[7\]

Nous pouvons voir que relativement peu d'utilisateurs sont actuellement inscrits à la newsletter, mais ces utilisateurs sont généralement plus actifs. Pour que les nouveaux utilisateurs restent engagés, il serait bon d'inclure une invitation à commander la newsletter dans des campagnes d'intégration. Pour réengager les utilisateurs périmés, un bon plan serait d'envoyer une campagne typique [utilisateur expiré][9] et [utilisateurs cibles qui ont converti][12] avec une campagne ultérieure pour s'inscrire à la newsletter.
[1]: {% image_buster /assets/img_archive/segment_insights.png %} [2]: {% image_buster /assets/img_archive/Segment_Insights_Info.png %} [3]: {% image_buster /assets/img_archive/Segment_Segment_Insights. ng %} [5]: {% image_buster /assets/img_archive/Segment_Language_Insights.png %} [7]: {% image_buster /assets/img_archive/Segment_Insights_Events1.png %}

[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[10]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter
