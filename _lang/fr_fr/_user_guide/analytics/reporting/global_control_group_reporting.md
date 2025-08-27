---
nav_title: Groupe de contrôle global 
article_title: Rapport sur le groupe de contrôle global
page_type: reference
description: "Cette page présente les indicateurs de reporting figurant sur la page Rapports sur les groupes de contrôle global du tableau de bord."
tool: 
  - Reports

---

# Rapport sur le groupe de contrôle global

> Le rapport sur le groupe de contrôle global vous permet de comparer votre groupe à un échantillon de traitement. Votre échantillon de traitement est une sélection aléatoire d’utilisateurs ne faisant pas partie du groupe de contrôle, mais qui comporte plus ou moins le même nombre d’utilisateurs que votre groupe de contrôle. Cet échantillon est généré à l’aide de la méthode des numéros de compartiment aléatoires.

## Visualisation d'un rapport

Pour afficher un rapport pour votre [Global Control Group]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) depuis le tableau de bord, accédez à **Analytics** > **Global Control Group Report**. 

Ensuite, sélectionnez le paramètre avec lequel vous souhaitez exécuter votre rapport (sessions ou événement personnalisé particulier) et sélectionnez **Exécuter le rapport.**

![]({% image_buster /assets/img/control_group/control_group6.png %})

## Configuration de votre rapport

Au moment de générer votre rapport, choisissez un événement (soit des sessions, soit tout événement personnalisé), que vous comparerez à vos groupes de traitement et de contrôle. Choisissez ensuite une période pour laquelle vous souhaitez consulter des données. N’oubliez pas que si vous avez enregistré plusieurs expériences de groupe de contrôle à différentes périodes, vous devez éviter d’inclure des données provenant de plusieurs expériences dans votre rapport.

Gardez à l’esprit que les pourcentages de votre rapport sont arrondis. Par exemple, lorsque le nombre de conversions représente un très faible pourcentage de votre groupe de contrôle ou de traitement, le taux de conversion peut être arrondi à 0 %.

Enfin, comme pour plusieurs autres rapports sur notre plateforme, ce rapport affiche un pourcentage de [confiance]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) pour votre changement par rapport à la métrique de contrôle. Notez que si le taux de conversion entre votre groupe de contrôle et de traitement est identique, le pourcentage de confiance sera de 0 % ; cela indique qu’il y a 0 % de probabilités qu’il y ait une différence entre les deux groupes. 

### Tailles de groupe

Avant mai 2024, le groupe de contrôle global était exclu de l'archivage des utilisateurs, mais le groupe d'échantillons de traitement ne l'était pas. À partir de mai 2024, les deux groupes sont exclus de l'archivage des utilisateurs. Cela pourrait entraîner des différences significatives de taille entre votre groupe d'échantillons de traitement et le groupe de contrôle global. La prochaine fois que vous réinitialiserez votre Groupe de Contrôle Global, cette divergence sera résolue et vous verrez des tailles de groupe similaires.

{% alert note %}
Chaque espace de travail comporte au maximum un groupe de contrôle global et un groupe d'échantillons de traitement. Le groupe de l'échantillon de traitement est le même groupe d'utilisateurs, quelle que soit la manière dont vous configurez votre rapport de contrôle global.
{% endalert %}

## Indicateurs du rapport

| Indicateur | Définition | Calcul |
| -- | -- | -- |
| Changement du groupe de contrôle | Cette opération calcule l’augmentation entre le taux de conversion de vos groupes de traitement et de contrôle. | ((taux de conversion du traitement – taux de conversion du contrôle) ÷ taux de conversion du contrôle) * 100 |
| Augmentation progressive | L’augmentation progressive correspond à la différence entre les événements totaux de vos groupes de traitement et de contrôle. Cette mesure cherche à répondre à la question « Combien d’événements de conversion le groupe de traitement a-t-il atteint ? ». | Total des événements du groupe de traitement – total des événements du groupe de contrôle |
| Pourcentage d’augmentation progressive | Le pourcentage des événements totaux de votre groupe de traitement pouvant être attribués à votre groupe traitement (par rapport au comportement naturel des utilisateurs). Ce pourcentage est calculé en divisant l’augmentation progressive (le nombre) par le nombre total d’événements de votre groupe de traitement. | Augmentation progressive (nombre) ÷ Total des événements pour le groupe de traitement |
| Taux de conversion | Le pourcentage estimé d'utilisateurs de votre groupe de contrôle ou de traitement qui terminent l'événement sélectionné pendant la période choisie. Ce chiffre est calculé en additionnant le nombre d'événements de la période et en le divisant par la somme des utilisateurs du groupe chaque jour. Ce chiffre ne peut être qu'approximatif, car la taille du groupe fluctue régulièrement au fur et à mesure que de nouveaux utilisateurs entrent dans votre groupe de contrôle global, et les événements sont des événements totaux, et non uniques. Si le nombre de conversions est très faible et que vos groupes de contrôle ou de traitement sont très importants, il se peut que le taux de conversion soit arrondi à 0 %. Si le nombre d'événements est très élevé - par exemple, dans les cas où un utilisateur peut faire plus d'un événement par jour - alors le taux de conversion peut être supérieur à 100 %. | Somme du nombre d'événements pour ces utilisateurs au cours de cette période ÷ somme des utilisateurs du groupe chaque jour. |
| Taille estimée du groupe | Le nombre estimé d’utilisateurs de vos groupes de contrôle et de traitement pendant la période sélectionnée. | La taille maximale que vos groupes de traitement et de contrôle ont atteint pendant la période que vous avez choisie pour le rapport. |
| Nombre total d’événements | Le nombre total de fois que l’événement sélectionné s’est produit pendant la période choisie. Ce nombre n’est pas unique (par exemple, si un utilisateur effectue un événement deux fois pendant la période, l’événement augmentera deux fois). | Somme du nombre de fois qu'un événement s'est produit chaque jour pendant la période choisie. |
| Événements par utilisateur | L’estimation en moyenne du nombre de fois que les utilisateurs de chaque groupe ont effectué vos événements de conversion pendant la période sélectionnée. | Total des événements ÷ taille estimée du groupe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

