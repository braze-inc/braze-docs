---
nav_title: Corrélation de conversion
article_title: Corrélation de conversion
alias: /fr/conversion_corrélation/
page_order: 3
page_type: Référence
description: "Cet article de référence explique l'analyse de la corrélation de conversion sur la page Analytiques de campagne."
tool:
  - Rapports
---

# Corrélation de conversion

> L'analyse de corrélation de conversion sur la page Analytics de campagne vous donne un aperçu des attributs et des comportements des utilisateurs qui aident ou nuisent aux résultats que vous avez définis pour les campagnes.

## Aperçu

Pour chaque campagne, nous vérifions une liste d'attributs et de comportements utilisateur et calculons s'ils sont statistiquement significativement associés à des augmentations ou des baisses dans chacun des [événements de conversion](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/) que vous avez choisi pour la campagne. Nous calculons également à quel point les utilisateurs plus ou moins probables avec l'attribut ou le comportement donné ont été à convertir, et si c'est significatif, afficher cela sur le côté gauche ou droit correspondant de la table. Les utilisateurs avec chaque attribut ou comportement d'intérêt sont comparés aux taux de l'ensemble du public de la campagne. Les comportements et les attributs qui n'ont pas de corrélation significative avec la conversion ne sont pas affichés dans la table.

__Pour exécuter une analyse de corrélation de conversion :__<br> Utilisez le menu déroulant pour sélectionner l'événement de conversion qui vous intéresse.

!\[Table de corrélation de conversion\]\[1\]

## Qu'est-ce qui est vérifié?

Nous vérifions les attributs suivants en les traitant comme des variables catégoriques. En d'autres termes, un utilisateur a ou non chaque valeur possible de ces attributs, et nous testons s'ils affectent le taux de conversion.

-  Pays
-  Langue
-  Sexe

Nous vérifions également si ce qui suit affecte le taux de conversion :

- Effectuer des événements personnalisés
- Campagnes et Canvases reçues au cours des 30 derniers jours (autres que la campagne actuellement en cours d'évaluation)

Enfin, nous vérifions plusieurs variables comportementales qui peuvent prendre plusieurs valeurs. Nous divisons ce qui suit en 4 compartiments ou quartiles et mesurons ensuite l'association de ce quartile avec des augmentations ou des diminutions de conversion :

- Âge
- Total des dollars dépensés
- Nombre de sessions

## Quand puis-je vérifier cette analyse ?

Cette analyse devient disponible au moins 24 heures après l'envoi d'une campagne et ne regarde que les envois qui se sont produits au cours des 30 derniers jours. Si aucun comportement ou attribut ne correspond significativement à aucun des événements de conversion de la campagne, la liste déroulante sera désactivée et un message s'affichera vous informant que c'est le cas.

## Comment Braze vérifie son importance

Nous vérifions l'importance statistique en utilisant quelque chose appelé [l'intervalle de confiance Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Nous déterminons avec 95% de confiance le taux de conversion de l’ensemble de l’auditoire de la campagne. Ceci est appelé le taux de base.

Ensuite, pour chacune des variables, nous calculons également le taux auquel les utilisateurs avec cet attribut particulier ou comportement d'intérêt converti à 95% de confiance. En divisant cela par le taux de base, nous sommes en mesure de mesurer le ratio. Si c'est beaucoup plus grand que 1, les utilisateurs avec l'attribut ou le comportement sont plus susceptibles de convertir. Si c'est beaucoup moins, ils sont moins probables. Nous affichons la valeur du ratio lui-même dans le tableau. La valeur n'est affichée que si elle est assez éloignée de 1 pour être significative au niveau de confiance de 95%.
[1]: {% image_buster /assets/img/convcorr.png %}
