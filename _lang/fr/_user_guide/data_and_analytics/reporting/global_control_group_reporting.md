---
nav_title: Groupe de contrôle global 
article_title: Rapport sur le groupe de contrôle global
page_type: reference
description: "Cet article de référence décrit les informations qui se trouvent sur la page Global Control Group Reporting (Rapport sur le groupe de contrôle global) du tableau de bord."
tool: 
  - Rapports

---

# Rapport sur le groupe de contrôle global

Pour consulter un rapport sur votre [Groupe de contrôle global ]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) dans le tableau de bord, accédez à **Global Control** sous **Data (Données)**. Ensuite, sélectionnez le paramètre que vous souhaitez inclure dans votre rapport (des sessions ou un événement personnalisé donné) et cliquez sur **Run Report (Exécuter le rapport)**.

![][6]

## À propos de votre rapport

Le rapport sur le groupe de contrôle global vous permet de comparer votre groupe à un échantillon de traitement. Votre échantillon de traitement est une sélection aléatoire d’utilisateurs ne faisant pas partie du groupe de contrôle, mais qui comporte plus ou moins le même nombre d’utilisateurs que votre groupe de contrôle. Cet échantillon est généré à l’aide de la méthode des numéros de compartiment aléatoires.

Au moment de générer votre rapport, choisissez un événement (soit des sessions, soit tout événement personnalisé), que vous comparerez à vos groupes de traitement et de contrôle. Choisissez ensuite une période pour laquelle vous souhaitez consulter des données. N’oubliez pas que si vous avez enregistré plusieurs expériences de groupe de contrôle à différentes périodes, vous devez éviter d’inclure des données provenant de plusieurs expériences dans votre rapport.

Gardez à l’esprit que les pourcentages de votre rapport sont arrondis. Par exemple, dans les cas où le nombre de conversions est un pourcentage très faible de votre groupe de traitement ou de contrôle global, le taux de conversion peut être arrondi à 0 %.

Enfin, comme pour d’autres rapports sur notre plateforme, ce rapport affiche un pourcentage de [confiance]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#understanding-confidence) correspondant au changement de vos mesures de contrôle. Notez que si le taux de conversion entre votre groupe de contrôle et de traitement est identique, le pourcentage de confiance sera de 0 % ; cela indique qu’il y a 0 % de probabilités qu’il y ait une différence entre les deux groupes.

## Métriques du rapport

| Métrique | Définition | Calcul |
| -- | -- | -- |
| Changement du groupe de contrôle | Cette opération calcule l’augmentation entre le taux de conversion de vos groupes de traitement et de contrôle. | ((Taux de conversion du groupe de traitement – taux de conversion du groupe de contrôle) ÷ taux de conversion du groupe de contrôle) * 100 |
| Augmentation progressive | L’augmentation progressive correspond à la différence entre les événements totaux de vos groupes de traitement et de contrôle. Cette mesure cherche à répondre à la question « Combien d’événements de conversion le groupe de traitement a-t-il atteint ? ». | Total des événements du groupe de traitement – total des événements du groupe de contrôle |
| Pourcentage d’augmentation progressive | Le pourcentage des événements totaux de votre groupe de traitement pouvant être attribués à votre groupe traitement (par rapport au comportement naturel des utilisateurs). Ce pourcentage est calculé en divisant l’augmentation progressive (le nombre) par le nombre total d’événements de votre groupe de traitement. | Augmentation progressive (nombre) ÷ Total des événements pour le groupe de traitement |
| Taux de conversion | En moyenne, le pourcentage d’utilisateurs de votre groupe de contrôle ou de traitement qui complète l’événement sélectionné chaque jour pendant la période choisie. Si le nombre de conversions est très faible et que vos groupes de contrôle ou de traitement sont très importants, il se peut que le taux de conversion soit arrondi à 0 %. | La moyenne du pourcentage d’utilisateurs qui effectuent votre événement sélectionné chaque jour pendant la période choisie. |
| Taille estimée du groupe | Le nombre estimé d’utilisateurs de vos groupes de contrôle et de traitement pendant la période sélectionnée. | La taille maximale que vos groupes de traitement et de contrôle ont atteint pendant la période que vous avez choisie pour le rapport. |
| Nombre total d’événements | Le nombre total de fois que l’événement sélectionné s’est produit pendant la période choisie. Ce nombre n’est pas unique : si un utilisateur effectue un événement deux fois pendant la période, l’événement augmentera deux fois. | La somme du nombre de fois que l’événement s’est produit chaque jour pendant la période choisie. |
| Événements par utilisateur | L’estimation en moyenne du nombre de fois que les utilisateurs de chaque groupe ont effectué vos événements de conversion pendant la période sélectionnée. | Total des événements ÷ taille estimée du groupe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[6]: {% image_buster /assets/img/control_group/control_group6.png %}