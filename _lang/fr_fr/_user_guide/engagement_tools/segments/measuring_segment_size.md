---
nav_title: Mesure de la taille des segments
article_title: Mesure de la taille des segments
page_order: 9
page_type: reference
tool: 
- Segments
description: "Cette page explique comment vous pouvez contrôler la composition et la taille de votre segmentation."
---

# Mesurer la taille des segments

> Cette page explique comment vous pouvez contrôler la composition et la taille de votre segmentation.

## Calcul de l'appartenance à un segmentation

Braze met à jour l’appartenance des utilisateurs à un segment au fur et à mesure que nos serveurs reçoivent et traitent les données, ce qui se produit généralement de manière instantanée. L’appartenance d’un utilisateur à un segment donné ne changera pas tant que cette session n’a pas été traitée. Par exemple, un utilisateur faisant partie d’un segment d’utilisateurs inactifs au début d’une session sera immédiatement sorti du segment d’utilisateurs inactifs une fois la session traitée.

### Calcul du nombre total d’utilisateurs pouvant être atteints

Chaque segment affiche le nombre total d’utilisateurs qui sont membres de ce segment. Lorsque vous filtrez pour les **utilisateurs de toutes les applications**, il affiche également certains des canaux d'envoi de messages les plus fréquemment utilisés (tels que le push web ou l'e-mail) et le nombre d'utilisateurs joignables pour ces canaux spécifiques. 

Il est possible que le nombre total d’utilisateurs diffère du nombre d’utilisateurs pouvant être atteints par chaque canal. En outre, tous les canaux ne sont pas répertoriés dans le tableau des utilisateurs joignables. Par exemple, les cartes de contenu, les webhooks et WhatsApp n'apparaissent pas dans la répartition. Cela signifie que le nombre total d'utilisateurs joignables peut être supérieur à la somme des utilisateurs de chaque canal affiché.

![Tableau affichant le nombre total d'utilisateurs atteignables, réparti entre les utilisateurs atteignables par e-mail, notification push iOS, notification push Android, notification push Web, notification push Kindle et notification push Android Chine.][3]

Pour qu’un utilisateur soit indiqué comme pouvant être atteint par un canal donné, il doit avoir à la fois :
* Une adresse e-mail valide ou un jeton de poussée associé à leur profil ; et
* Être abonné ou inscrit à votre application.

Un utilisateur donné peut appartenir à plusieurs groupes d’utilisateurs atteignables. Par exemple, un utilisateur peut disposer d’une adresse e-mail valide et d’un jeton de notification push Android valide et être abonné aux deux, mais ne pas avoir de jeton de notification push associé. L'écart entre le nombre total d'utilisateurs joignables et la somme des différents canaux correspond au nombre d'utilisateurs qui se sont qualifiés pour le segment mais qui ne sont pas joignables par ces canaux de communication.

## Statistiques sur la taille des segments

Les statistiques estimées sont obtenues par échantillonnage d'une partie seulement de votre segmentation. Vous devez donc vous attendre à ce que les tailles estimées soient supérieures ou inférieures à la valeur réelle, les marges d'erreur étant potentiellement plus importantes pour les espaces de travail de grande taille. Pour obtenir un nombre précis d'utilisateurs dans votre segmentation, sélectionnez **Calculer les statistiques exactes**. L'appartenance exacte à un segment sera toujours calculée avant qu'un segment ne soit affecté par un message envoyé dans le cadre d'une campagne ou d'un Canvas.

Braze fournit les statistiques suivantes sur la taille des segments. 

### Statistiques sur les filtres

Pour chaque groupe de filtres, vous pouvez afficher le nombre estimé d'utilisateurs joignables. Sélectionnez **Développer les statistiques d’entonnoir supplémentaires** pour afficher la répartition entre les différents canaux.

![Un groupe de filtres avec un filtre pour un sexe qui n'est pas inconnu.][2]{: style="max-width:80%;"}

### Statistiques de segment

Pour l'ensemble d'un segment, vous pouvez voir, au bas de la page, une estimation des utilisateurs atteignables, ainsi qu’une estimation du nombre d’utilisateurs pour chaque canal. Vous pouvez également obtenir le nombre exact d'utilisateurs joignables (pour l'ensemble du segment et pour chaque canal) en sélectionnant **Calculer les statistiques exactes.**

Remarques :
- Le calcul de statistiques exactes peut prendre quelques minutes. Cette fonction ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres.
- Pour les segments de grande taille, il est normal de constater de légères variations, même en calculant des statistiques exactes. La précision de cette fonctionnalité devrait être égale ou supérieure à 99,999 %.

## Visualisation de l'historique du nombre de membres des segments

Pour tous les segments, vous pouvez consulter un graphique de l'historique des membres qui indique le nombre estimé de membres du segment pour chaque jour. Ce graphique montre comment la taille de votre segmentation a évolué dans le temps. Utilisez la liste déroulante pour filtrer l’appartenance au segment par plage de dates.

![Utilisez la liste déroulante Historique des inscriptions pour filtrer l’appartenance au segment par plage de dates.][1]

L'objectif de ce graphique étant de vous donner une idée de l'évolution globale du nombre de membres d'un segment, le nombre de jours est une estimation, de la même manière que la taille du segment est une estimation avant que vous ne sélectionniez **Calculer les statistiques exactes**. Et comme ce graphique présente des estimations, il est possible que la taille de votre segment apparaisse comme "0" dans ce graphique, même si sa taille réelle (qui peut être déterminée après avoir sélectionné **Calculer les statistiques exactes**) n'est pas "0". Il est particulièrement probable que le graphique affiche une estimation de "0" si votre segmentation est très petite par rapport à la taille de la population de votre espace de travail.

Braze estime le nombre de membres d'un segment en interrogeant un sous-ensemble de vos utilisateurs, puis en extrapolant ces résultats à l'ensemble de votre audience. Cela signifie que les résultats du graphique ne fournissent qu'une estimation du nombre de membres du segment ce jour-là, et qu'ils devraient également fluctuer d'un jour à l'autre parce qu'un échantillon différent d'utilisateurs peut être interrogé pour cette estimation chaque jour.

{% alert note %}
Toutes les estimations peuvent être supérieures ou inférieures à la valeur indiquée d'environ 1 % de la population totale de votre espace de travail. Les espaces de travail plus vastes et comptant un plus grand nombre d'utilisateurs sont plus susceptibles d'avoir des estimations qui peuvent différer des calculs exacts par un montant numérique plus élevé, même si la différence est toujours de 1 % de la population d'utilisateurs de l'espace de travail. Cela signifie que l'on peut s'attendre à des différences plus importantes entre les estimations et les comptages exacts dans les grands espaces de travail.
{% endalert %}

### Raisons des changements importants

Le nombre de membres peut changer de manière significative pour un certain nombre de raisons, telles que celles mentionnées dans ce tableau.

| Raison | Exemple |
| --- | --- |
| Comportement normal de l'utilisateur | Les utilisateurs s'abonnent après une campagne particulièrement réussie. |
| Les utilisateurs sont importés par CSV | L'importation d'un fichier CSV d'utilisateurs a permis d'augmenter de manière significative le nombre de membres de la segmentation. |
| Modification des critères de segmentation de l'audience | Les règles d'audience d'un segment existant (telles que les filtres) ont été modifiées, ce qui a entraîné des changements importants dans la composition du segment. |
| Les utilisateurs sont supprimés | Un nombre important d'utilisateurs a été supprimé. |
| Une intégration des partenaires synchronisée avec Braze | Un tiers a envoyé à Braze des données qui ont influencé de manière significative l'appartenance à un segment. |
| Les utilisateurs dormants sont archivés. | Un nombre important de profils inactifs ont été archivés. Par exemple, un grand nombre d'utilisateurs importés au format CSV n'enregistrent jamais d'activité et sont archivés en même temps. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

[1]: {% image_buster /assets/img_archive/historical_membership2.png %}
[2]: {% image_buster /assets/img_archive/segment_filter_stats.png %}
[3]: {% image_buster /assets/img_archive/segmenter_reachable_users.png %}