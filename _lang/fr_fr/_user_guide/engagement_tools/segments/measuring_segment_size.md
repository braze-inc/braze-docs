---
nav_title: Mesurer la taille des segments
article_title: Mesure de la taille des segments
page_order: 5
page_type: reference
tool: 
- Segments
description: "Cette page explique comment vous pouvez contrôler la composition et la taille de votre segmentation."
---

# Mesurer la taille des segments

> Cette page explique comment vous pouvez contrôler la composition et la taille de votre segmentation.

## Calcul de l'appartenance à un segmentation

Braze met à jour l'appartenance de l'utilisateur à un segment au fur et à mesure que les données sont renvoyées à nos serveurs et traitées, généralement de manière instantanée. L'appartenance d'un utilisateur à une segmentation ne changera pas tant que la session n'aura pas été traitée. Par exemple, un utilisateur qui se trouve dans un segment d'utilisateurs déchus au début de la session sera immédiatement déplacé hors du segment d'utilisateurs déchus lors du traitement de la session.

### Calcul du nombre total d'utilisateurs joignables

Chaque segmentation affiche le nombre total d'utilisateurs qui en font partie. Lorsque vous filtrez pour les **utilisateurs de toutes les applications**, il affiche également certains des canaux d'envoi de messages les plus fréquemment utilisés (tels que le push web ou l'e-mail) et le nombre d'utilisateurs joignables pour ces canaux spécifiques. 

Il est possible que le nombre d'utilisateurs totaux soit différent du nombre d'utilisateurs atteignables par chaque canal. En outre, tous les canaux ne sont pas répertoriés dans le tableau des utilisateurs joignables. Par exemple, les cartes de contenu, les webhooks et WhatsApp n'apparaissent pas dans la répartition. Cela signifie que le nombre total d'utilisateurs joignables peut être supérieur à la somme des utilisateurs de chaque canal affiché.

\![Un tableau affichant le nombre total d'utilisateurs joignables, réparti entre les utilisateurs joignables par e-mail, iOS push, Android push, web push et Kindle push.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Pour qu'un utilisateur soit répertorié comme joignable par un certain canal, il doit avoir les deux :
* Une adresse e-mail valide ou un jeton de poussée associé à leur profil ; et
* S'est abonné à votre application.

Un même utilisateur peut appartenir à différents groupes d'utilisateurs accessibles. Par exemple, un utilisateur peut avoir à la fois une adresse e-mail valide et un jeton push Android valide et être abonné aux deux, mais ne pas avoir de jeton push iOS associé. L'écart entre le nombre total d'utilisateurs joignables et la somme des différents canaux correspond au nombre d'utilisateurs qui se sont qualifiés pour le segment mais qui ne sont pas joignables par ces canaux de communication.

## Statistiques sur la taille des segments

Les statistiques estimées sont obtenues par échantillonnage d'une partie seulement de votre segmentation. Vous devez donc vous attendre à ce que les tailles estimées soient supérieures ou inférieures à la valeur réelle, les marges d'erreur étant potentiellement plus importantes pour les espaces de travail de grande taille. Pour obtenir un nombre précis d'utilisateurs dans votre segmentation, sélectionnez **Calculer les statistiques exactes**. L'appartenance exacte à un segment sera toujours calculée avant qu'un segment ne soit affecté par un message envoyé dans le cadre d'une campagne ou d'un Canvas. 

Braze fournit les statistiques suivantes sur la taille des segments. 

### Statistiques sur les filtres

Pour chaque groupe de filtres, vous pouvez afficher le nombre estimé d'utilisateurs joignables. Sélectionnez **Élargir les statistiques de l'entonnoir supplémentaire** pour voir la répartition entre les différents canaux.

\![Un groupe de filtrage avec un filtre pour les utilisateurs qui ont eu exactement un nombre de sessions.]({% image_buster /assets/img_archive/segment_filter_stats.png %}){: style="max-width:80%;"}

## Estimation du nombre d'utilisateurs joignables

Vous pouvez visualiser l'estimation des utilisateurs joignables d'un segment entier, y compris le nombre estimé d'utilisateurs pour chaque canal, dans le panneau latéral **Utilisateurs joignables**. Cette **estimation** vous donne une fourchette approximative de la taille de votre segmentation, ainsi qu'une estimation du pourcentage de votre base d'utilisateurs globale qui appartient à ce segment. Notez que les statistiques estimées sont mises en cache pendant 15 minutes, à moins que vous ne modifiiez votre segment, auquel cas les statistiques estimées seront automatiquement mises à jour. Vous pouvez également afficher le nombre exact d'utilisateurs joignables (pour l'ensemble du segment et par canal) en sélectionnant **Calculer les statistiques exactes**. 


Le panneau "Utilisateurs joignables" indique qu'il y a entre 2,3 et 2,4 millions d'utilisateurs estimés.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Considérations relatives au nombre d'estimations

Braze mesure le nombre d'utilisateurs estimés en interrogeant un sous-ensemble de vos utilisateurs, puis extrapole ces résultats à l'ensemble de votre audience. Étant donné que le sous-ensemble d'utilisateurs que Braze interroge peut différer à chaque fois que nous calculons cette estimation, celle-ci peut également changer dans les cas où la composition de votre audience aurait techniquement dû rester la même. Par exemple, si vous modifiez l'ordre de vos filtres ou si vous vérifiez à nouveau le même segment à un moment différent, il est possible que le nombre estimé change (même si **Calculer les statistiques exactes** donnerait les mêmes résultats si votre segment n'avait pas changé).

Si votre espace de travail compte un grand nombre d'utilisateurs, il se peut que vous constatiez une plus grande variation entre vos estimations et vos calculs exacts, en particulier lorsque votre segmentation ne représente qu'un très faible pourcentage de la population totale de votre espace de travail. En effet, Braze mesure l'estimation en interrogeant un sous-ensemble de vos utilisateurs et en extrapolant les résultats à l'ensemble de votre base d'utilisateurs. Pour des bases d'utilisateurs plus importantes, on peut s'attendre à des différences plus importantes entre les chiffres estimés et les chiffres exacts.

Les segments de très petite taille auront une fourchette d'estimation qui comprendra 0, ce qui signifie que le pourcentage du nombre total d'utilisateurs peut être arrondi à 0. Dans ces cas, **Calculer les statistiques exactes** vous aidera à obtenir un décompte précis de la taille de votre segmentation, qui peut ne pas être égale à 0.

\![Le panneau latéral "Utilisateurs joignables".]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Utilisateurs joignables par canal

Pour afficher le nombre d'utilisateurs joignables pour chaque canal de communication, sélectionnez **Afficher la répartition** dans le panneau **Utilisateurs joignables**. Elle affiche certains des canaux de communication les plus fréquemment utilisés (tels que le push web ou l'e-mail) et le nombre d'utilisateurs joignables pour ces canaux spécifiques. 

L'indicateur " _Total"_ représente les utilisateurs uniques. Par exemple, si un utilisateur a à la fois Android push et iOS push, il sera comptabilisé pour ces deux lignes, mais ne comptera que pour un seul utilisateur dans la ligne _Total._ 

Toutefois, il est possible que le nombre total d'utilisateurs soit différent de la somme des utilisateurs joignables par chaque canal, car un même utilisateur peut appartenir à différents groupes d'utilisateurs joignables. Par exemple, un utilisateur peut avoir à la fois une adresse e-mail valide et un jeton push Android valide et être abonné aux deux, mais ne pas avoir de jeton push iOS associé. 

Gardez à l'esprit que tous les canaux ne sont pas répertoriés dans le tableau des **utilisateurs joignables** (comme les cartes de contenu, les webhooks et WhatsApp). Par exemple, si vous avez des utilisateurs uniquement joignables par Whatsapp, ils apparaîtront dans le _Total_ mais pas dans les lignes spécifiques aux canaux. Cela signifie que le nombre total d'utilisateurs joignables peut être différent de la somme des utilisateurs pour chaque canal affiché.

Dans les cas où le _total_ est supérieur à la somme des canaux, l'écart représente le nombre d'utilisateurs qui se sont qualifiés pour le segment mais qui ne sont pas joignables par ces canaux de communication.

Pour qu'un utilisateur soit répertorié comme étant joignable via un certain canal, il doit avoir
- Une adresse e-mail valide ou un jeton de poussée associé à leur profil, et
- S'est abonné à votre application.

## Calculer des statistiques exactes 

Pour obtenir un décompte précis du nombre d'utilisateurs dans votre segmentation, sélectionnez **Calculer les statistiques exactes** dans le volet **Utilisateurs joignables**.

Pour actualiser les statistiques d'un calcul effectué précédemment, sélectionnez **Actualiser les statistiques exactes**. La date à laquelle ce calcul a été effectué pour la dernière fois sera automatiquement mise à jour.

Notez que la précision d'un calcul n'est que de 99,999 % ou plus. Ainsi, pour les grands segments, vous pouvez remarquer de légères variations - même en calculant des statistiques exactes - ce qui est un comportement normal. En outre, les résultats des statistiques exactes sont mis en cache pendant 24 heures, à moins que vous ne modifiiez votre segment, auquel cas vous pouvez recalculer les statistiques exactes.

Le panneau "Utilisateurs joignables" avec une option pour afficher la répartition.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Les statistiques au niveau de chaque filtre seront toujours estimées, même si vous calculez des statistiques exactes. **Calculer les statistiques exactes** ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres. Ce calcul peut prendre quelques minutes. Les grands espaces de travail, en particulier, peuvent nécessiter des périodes plus longues pour effectuer les calculs. Vous pouvez suivre vos progrès sur la barre de progression dans le panneau des **utilisateurs joignables**. Lorsqu'un calcul doit durer plus de cinq minutes, Braze vous envoie les résultats par e-mail. 

Braze donne la priorité à un calcul à la fois par espace de travail, de sorte que l'exécution de plusieurs calculs à la fois entraînera des retards. Vous pouvez sélectionner **Afficher la file d'attente des calculs** pour voir quels segments sont en avance sur le vôtre, leur état d'avancement et leur initiateur, et avoir une idée du moment où votre calcul pourrait être prioritaire.

\![Une file d'attente de calcul avec un calcul.]({% image_buster /assets/img_archive/calculation_queue.png %})

Vous pouvez annuler un calcul de statistiques exactes en sélectionnant **Annuler.** Cela peut être utile s'il y a plusieurs calculs dans la file d'attente et que vous souhaitez donner la priorité à un autre calcul. 

Un calcul actif avec possibilité d'annulation]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:25%"}

## Visualisation de l'historique du nombre de membres des segments

Pour tous les segments, vous pouvez consulter un graphique de l'historique des membres qui indique le nombre estimé de membres du segment pour chaque jour. Ce graphique montre comment la taille de votre segmentation a évolué dans le temps. Utilisez le menu déroulant pour filtrer l'appartenance à un segment par plage de dates.

Utilisez le menu déroulant Historique des adhésions pour filtrer les adhésions aux segments par plage de dates.]({% image_buster /assets/img_archive/historical_membership2.png %})

L'objectif de ce graphique étant de vous donner une idée de l'évolution globale du nombre de membres d'un segment, le nombre de jours est une estimation, de la même manière que la taille du segment est une estimation avant que vous ne sélectionniez **Calculer les statistiques exactes**. Et comme ce graphique présente des estimations, il est possible que la taille de votre segment apparaisse comme "0" dans ce graphique, même si sa taille réelle (qui peut être déterminée après avoir sélectionné **Calculer les statistiques exactes**) n'est pas "0". Il est particulièrement probable que le graphique affiche une estimation de "0" si votre segmentation est très petite par rapport à la taille de la population de votre espace de travail.

Par exemple, disons que votre espace de travail contient 100 millions d'utilisateurs et que votre segmentation compte environ 700 utilisateurs. Il est possible que certains jours, aucun utilisateur ne se trouve dans le segment et qu'aucun utilisateur n'entre dans la plage de compartiments aléatoires utilisée pour l'estimation historique du nombre de membres, ce qui se traduit par un nombre de membres égal à 0 pour un jour donné.

Braze estime le nombre de membres d'un segment en interrogeant un sous-ensemble de vos utilisateurs, puis en extrapolant ces résultats à l'ensemble de votre audience. Cela signifie que les résultats du graphique ne fournissent qu'une estimation du nombre de membres du segment ce jour-là, et qu'ils devraient également fluctuer d'un jour à l'autre parce qu'un échantillon différent d'utilisateurs peut être interrogé pour cette estimation chaque jour.

{% alert note %}
Toutes les estimations peuvent être supérieures ou inférieures à la valeur indiquée d'environ 1 % de la population totale de votre espace de travail. Les espaces de travail plus vastes et comptant un plus grand nombre d'utilisateurs sont plus susceptibles d'avoir des estimations qui peuvent différer des calculs exacts par un montant numérique plus élevé, même si la différence est toujours de 1 % de la population d'utilisateurs de l'espace de travail. Cela signifie que l'on peut s'attendre à des différences plus importantes entre les estimations et les chiffres exacts dans les grands espaces de travail.
{% endalert %}

### Raisons des changements importants

Le nombre de membres peut changer de manière significative pour un certain nombre de raisons, telles que celles mentionnées dans ce tableau.

| Raison | Exemple |
| --- | --- |
| Comportement normal de l'utilisateur | Les utilisateurs s'abonnent après une campagne particulièrement réussie. |
| Les utilisateurs sont importés par CSV | L'importation d'un fichier CSV d'utilisateurs a permis d'augmenter de manière significative le nombre de membres de la segmentation. |
| Les critères de segmentation de l'audience sont modifiés. | Les règles d'audience d'un segment existant (telles que les filtres) ont été modifiées, ce qui a entraîné des changements importants dans la composition du segment. |
| Les utilisateurs sont supprimés | Un nombre important d'utilisateurs a été supprimé. |
| Une intégration des partenaires synchronisée avec Braze | Un tiers a envoyé à Braze des données qui ont influencé de manière significative l'appartenance à un segment. |
| Les utilisateurs dormants sont archivés. | Un nombre important de profils inactifs ont été archivés. Par exemple, un grand nombre d'utilisateurs importés au format CSV n'enregistrent jamais d'activité et sont archivés en même temps. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
