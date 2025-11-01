---
nav_title: Groupe de contrôle global
article_title: Rapport sur le groupe de contrôle global
page_type: reference
description: "Cette page présente les indicateurs de reporting figurant sur la page Rapports sur les groupes de contrôle global du tableau de bord."
tool: 
  - Reports

---

# Rapport du groupe de contrôle global

> Le rapport sur le groupe de contrôle global vous permet de comparer votre groupe à un échantillon de traitement. Votre échantillon de traitement est une sélection aléatoire d'utilisateurs non-contrôle, approximativement le même nombre d'utilisateurs que votre contrôle, générée à l'aide de la méthode du nombre compartiment aléatoire.

## Visualisation d'un rapport

Pour afficher un rapport sur votre [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) à partir du tableau de bord, accédez à **Analyse** > **Rapport sur le groupe de contrôle global.** 

Ensuite, sélectionnez le paramètre avec lequel vous souhaitez exécuter votre rapport (sessions ou événement personnalisé particulier) et sélectionnez **Exécuter le rapport.**

\![]({% image_buster /assets/img/control_group/control_group6.png %})

## Configuration de votre rapport

Lors de la création de votre rapport, choisissez un événement (sessions ou tout autre événement personnalisé) pour comparer les groupes de traitement et de contrôle. Choisissez ensuite une période pour laquelle vous souhaitez consulter les données. Gardez à l'esprit que si vous avez enregistré plusieurs expériences de groupe de contrôle à des périodes différentes, vous devez éviter d'inclure les données de plus d'une expérience dans votre rapport.

N'oubliez pas que les indicateurs en pourcentage figurant dans votre rapport sont arrondis. Par exemple, lorsque le nombre de conversions représente un très faible pourcentage de votre groupe de contrôle ou de traitement, le taux de conversion peut être arrondi à 0 %.

Enfin, comme plusieurs autres rapports sur notre plateforme, ce rapport affiche un pourcentage de [confiance]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) pour votre indicateur de changement de contrôle. Notez que dans les cas où le taux de conversion entre votre groupe de contrôle et votre groupe de traitement sont identiques, il faut s'attendre à un taux de confiance de 0 % ; cela indique qu'il y a 0 % de chances qu'il y ait une différence de performance entre les deux groupes. 

### Taille des groupes

Avant mai 2024, le groupe de contrôle global a été exclu de l'archivage utilisateur, mais pas le groupe de l'échantillon de traitement. À partir de mai 2024, ces deux groupes sont exclus de l'archivage de l'utilisateur. Ainsi, votre groupe de traitement et le groupe de contrôle global pourraient avoir des tailles significativement différentes. La prochaine fois que vous réinitialiserez votre groupe de contrôle global, cet écart se résorbera et vous observerez des tailles de groupe similaires.

{% alert note %}
Chaque espace de travail comporte au maximum un groupe de contrôle global et un groupe d'échantillons de traitement. Le groupe de l'échantillon de traitement est le même groupe d'utilisateurs, quelle que soit la manière dont vous configurez votre rapport de contrôle global.
{% endalert %}

## Indicateurs de rapport

| Indicateurs | Définition | Calcul |
| -- | -- | -- |
| Changement de contrôle | Il s'agit de calculer l'écart entre le taux de conversion de votre groupe de traitement et celui de votre groupe de contrôle. | ((taux de conversion du traitement - taux de conversion du contrôle) ÷ taux de conversion du contrôle) * 100 |
| Augmentation progressive | La différence du nombre total d'événements entre votre groupe de traitement et votre groupe de contrôle. Cet indicateur vise à répondre à la question suivante : "Combien d'événements de conversion supplémentaires le groupe de traitement a-t-il obtenus ?". | Nombre total d'événements pour le traitement - nombre total d'événements pour le contrôle |
| Remontée incrémentale Pourcentage | Le pourcentage des événements totaux de votre traitement qui peuvent être attribués à votre traitement (par rapport au comportement naturel de l'utilisateur). Ce chiffre est calculé en divisant l'augmentation incrémentale (nombre) par le nombre total d'événements pour votre groupe de traitement. | Augmentation différentielle (nombre) ÷ Nombre total d'événements pour le groupe de traitement |
| Taux de conversion | Le pourcentage estimé d'utilisateurs de votre groupe de contrôle ou de traitement qui terminent l'événement sélectionné pendant la période choisie. Ce chiffre est calculé en additionnant le nombre d'événements de la période et en le divisant par la somme des utilisateurs du groupe chaque jour. Ce chiffre ne peut être qu'approximatif, car la taille du groupe fluctue régulièrement au fur et à mesure que de nouveaux utilisateurs entrent dans votre groupe de contrôle global, et les événements sont des événements totaux, et non uniques. Si le nombre de conversions est très faible et que vos groupes de contrôle ou de traitement sont très importants, le taux de conversion peut être arrondi à 0 %. Si le nombre d'événements est très élevé - par exemple, dans les cas où un utilisateur peut faire plus d'un événement par jour - alors le taux de conversion peut être supérieur à 100 %. | Somme du nombre d'événements pour ces utilisateurs au cours de cette période ÷ somme des utilisateurs du groupe chaque jour. |
| Taille estimée du groupe | Le nombre estimé d'utilisateurs dans vos groupes de contrôle et de traitement pendant la période sélectionnée. | Le nombre maximum de membres que vos groupes de contrôle et de traitement ont atteint au cours de la période que vous avez choisie pour le rapport. |
| Nombre total d'événements | Nombre total de fois où l'événement sélectionné s'est produit au cours de la période choisie. Celui-ci n'est pas unique (par exemple, si un utilisateur effectue un événement deux fois au cours de la période, l'événement est incrémenté deux fois). | Somme du nombre de fois qu'un événement s'est produit chaque jour pendant la période choisie. |
| Événements par utilisateur | Le nombre moyen estimé de fois où les utilisateurs de chaque groupe ont terminé vos événements de conversion au cours de la période sélectionnée. | Total des événements ÷ taille estimée du groupe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

