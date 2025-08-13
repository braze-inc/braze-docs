---
nav_title: Corrélation de conversion
article_title: Corrélation de conversion
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Cet article de référence explique l’analyse de corrélation de conversion sur la page Analyse de campagne."
tool: 
  - Reports
  
---

# Corrélation de conversion

> L'analyse de la corrélation des conversions sur la page **Analyse/analytique des campagnes** vous donne des informations sur les attributs et les comportements des utilisateurs qui favorisent ou entravent les résultats que vous avez définis pour les campagnes. 

## Aperçu

Pour chaque campagne, Braze vérifie une liste d'attributs et de comportements des utilisateurs et calcule si les utilisateurs sont associés de manière statistiquement significative à des augmentations ou des diminutions dans chacun des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) que vous avez choisis pour la campagne. Nous calculons également la probabilité de conversion des utilisateurs qui possédaient un attribut ou un comportement donné, et si la probabilité est importante, nous les affichons sur le côté correspondant du tableau. Les utilisateurs possédant chaque attribut ou comportement d’intérêt sont comparés aux taux de l’audience de la campagne dans son ensemble. Les comportements et les attributs qui n’ont pas de corrélation significative avec le taux de conversion ne sont pas affichés dans le tableau.

Pour effectuer une analyse de corrélation de conversion, sélectionnez l'événement de conversion qui vous intéresse dans le menu déroulant.

![Le panneau de corrélation des conversions montre un exemple où l'option "Sélectionner un événement de conversion" est réglée sur "Événement de conversion principal - A" et où le paramètre de l'événement est "Achat effectué dans les 12 heures (tout produit)".]({% image_buster /assets/img/convcorr.png %})

## Quels éléments Braze vérifie-t-il ?

Nous vérifions les attributs suivants en les traitant comme des variables catégorielles. En d’autres termes, un utilisateur peut avoir (ou non) chaque valeur possible pour ces attributs, et nous vérifions s’ils affectent le taux de conversion.

-  Pays
-  Langue
-  Genre

Nous vérifions également si les éléments suivants affectent le taux de conversion :

- Réalisation d’événements personnalisés
- Campagnes et Canvas reçus au cours des 30 derniers jours (autres que la campagne actuellement évaluée)

Enfin, nous vérifions plusieurs variables comportementales qui peuvent inclure plusieurs valeurs. Nous divisons les éléments suivants en quatre compartiments ou quartiles, puis nous évaluons le lien entre le fait de faire partie de ces quartiles et les augmentations ou diminutions des conversions :

- Âge
- Total dépensé
- Nombre de sessions

## Quand ai-je accès à cette analyse ?

Cette analyse devient disponible au moins 24 heures après l’envoi d’une campagne et s’intéresse uniquement aux envois effectués au cours des 30 derniers jours. Si aucun comportement ou attribut ne présente de lien direct avec l’un des événements de conversion de la campagne, le menu déroulant sera désactivé et un message s’affichera pour vous en informer.

## Vérification de la pertinence statistique par Braze

Nous vérifions la signification statistique en utilisant l'[intervalle de confiance de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Nous déterminons le taux avec lequel l’ensemble de l’audience de la campagne a été converti avec un niveau de confiance de 95 % . C’est ce que l’on appelle le taux de base. 

Ensuite, pour chacune des variables, nous calculons également le taux auquel les utilisateurs avec cet attribut ou comportement particulier sont convertis avec un niveau de confiance de 95 %. En divisant ce taux par le taux de base, nous sommes en mesure de mesurer le ratio. Si le ratio est beaucoup plus grand que 1, les utilisateurs ayant cet attribut ou comportement particulier sont plus susceptibles d’être convertis. Si le ratio est nettement inférieur à 1, ces utilisateurs sont moins susceptibles d’être convertis. Nous affichons la valeur du ratio lui-même dans le tableau. La valeur n’est affichée que si elle est assez loin de 1 pour être pertinente avec un niveau de confiance de 95 %.

