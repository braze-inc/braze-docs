---
nav_title: Corrélation de conversion
article_title: Corrélation de la conversion
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Cet article de référence explique l'analyse de corrélation des conversions sur la page Campaign Analytics (si utilisée)."
tool: 
  - Reports
  
---

# Corrélation de conversion

> L'analyse de la corrélation des conversions sur la page **Analyse/analytique des campagnes** vous donne des informations sur les attributs et les comportements des utilisateurs qui favorisent ou entravent les résultats que vous avez définis pour les campagnes. 

## Aperçu

Pour chaque campagne, Braze vérifie une liste d'attributs et de comportements des utilisateurs et calcule si les utilisateurs sont associés de manière statistiquement significative à des augmentations ou des diminutions dans chacun des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) que vous avez choisis pour la campagne. Nous calculons également l'augmentation ou la diminution de la probabilité de conversion des utilisateurs présentant l'attribut ou le comportement donné et, si elle est significative, nous l'affichons dans la partie correspondante du tableau. Les utilisateurs présentant chaque attribut ou comportement d'intérêt sont comparés aux taux de l'ensemble de l'audience de la campagne dans son ensemble. Les comportements et attributs qui n'ont pas de corrélation significative avec la conversion ne figurent pas dans le tableau.

Pour effectuer une analyse de corrélation des conversions, sélectionnez l'événement de conversion qui vous intéresse dans le menu déroulant.

Le panneau Corrélation de conversion montre un exemple où "Sélectionner un événement de conversion" est réglé sur "Événement de conversion principal - A" et où l'événement est réglé sur "Achat effectué dans les 12 heures (tout produit)".]({% image_buster /assets/img/convcorr.png %})

## Qu'est-ce qui est contrôlé ?

Nous vérifions les attributs suivants en les traitant comme des variables catégorielles. En d'autres termes, un utilisateur possède ou non chaque valeur possible de ces attributs, et nous testons s'ils affectent le taux de conversion.

-  Pays
-  Langue
-  Genre

Nous vérifions également si les éléments suivants ont une incidence sur le taux de conversion :

- Exécution de tout événement personnalisé
- Campagnes et toiles reçues au cours des 30 derniers jours (autres que la campagne en cours d'évaluation).

Enfin, nous vérifions plusieurs variables comportementales qui peuvent prendre plusieurs valeurs. Nous répartissons les éléments suivants en quatre compartiments ou quartiles, puis nous mesurons le lien entre le fait d'appartenir à un quartile donné et l'augmentation ou la diminution de la conversion :

- L'âge
- Total des dépenses
- Nombre de sessions

## Quand puis-je vérifier cette analyse ?

Cette analyse est disponible au moins 24 heures après le début de l'envoi d'une campagne et ne porte que sur les envois effectués au cours des 30 derniers jours. Si aucun comportement ou attribut ne présente de corrélation significative avec l'un des événements de conversion de la campagne, le menu déroulant sera désactivé et un message s'affichera pour vous en informer.

## Comment Braze vérifie l'importance des données

Nous vérifions la signification statistique en utilisant l'[intervalle de confiance de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Nous déterminons avec un niveau de confiance de 95 % le taux de conversion de l'ensemble de l'audience de la campagne. C'est ce qu'on appelle le taux de base. 

Ensuite, pour chacune des variables, nous calculons également le taux de conversion, avec un niveau de confiance de 95 %, des utilisateurs présentant l'attribut ou le comportement en question. En divisant ce taux par le taux de base, nous pouvons mesurer le ratio. S'il est beaucoup plus grand que 1, les utilisateurs ayant l'attribut ou le comportement en question sont plus susceptibles de se convertir. S'il est beaucoup moins élevé, il est moins probable qu'ils le soient. Nous affichons la valeur du ratio lui-même dans le tableau. La valeur n'est affichée que si elle est suffisamment éloignée de 1 pour être significative au niveau de confiance de 95 %.

