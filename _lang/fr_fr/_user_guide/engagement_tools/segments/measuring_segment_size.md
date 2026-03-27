---
nav_title: Mesurer la taille du segment
article_title: Mesurer la taille du segment
page_order: 5
page_type: reference
tool: 
- Segments
description: "Cette page explique comment surveiller la composition et la taille de votre segment."
---

# Mesurer la taille du segment

> Cette page explique comment surveiller la composition et la taille de votre segment.

## Calcul de l'appartenance à un segment

Braze met à jour l'appartenance des utilisateurs à un segment au fur et à mesure que nos serveurs reçoivent et traitent les données, ce qui se produit généralement de manière instantanée. L'appartenance d'un utilisateur à un segment ne changera pas tant que sa session n'aura pas été traitée. Par exemple, un utilisateur faisant partie d'un segment d'utilisateurs inactifs au début d'une session sera immédiatement retiré de ce segment une fois la session traitée.

### Calcul du nombre total d'utilisateurs joignables

Chaque segment affiche le nombre total d'utilisateurs qui en sont membres. Lorsque vous filtrez par **Utilisateurs de toutes les applications**, les canaux de communication les plus fréquemment utilisés (tels que le push web ou l'e-mail) sont également affichés, ainsi que le nombre d'utilisateurs joignables pour ces canaux spécifiques. 

Il est possible que le nombre total d'utilisateurs diffère du nombre d'utilisateurs joignables par chaque canal. De plus, tous les canaux ne figurent pas dans le tableau des utilisateurs joignables. Par exemple, les cartes de contenu, les webhooks et WhatsApp n'apparaissent pas dans la répartition. Le nombre total d'utilisateurs joignables peut donc être supérieur à la somme des utilisateurs de chaque canal affiché.

![Tableau présentant le nombre total d'utilisateurs joignables, ventilé par utilisateurs joignables par e-mail, notifications push iOS, notifications push Android, notifications push web et notifications push Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Pour qu'un utilisateur soit considéré comme joignable via un canal donné, il doit remplir ces deux conditions :
* Disposer d'une adresse e-mail valide ou d'un jeton de notification push associé à son profil, et
* Être abonné à votre application.

Un même utilisateur peut appartenir à plusieurs groupes d'utilisateurs joignables. Par exemple, un utilisateur peut disposer d'une adresse e-mail valide et d'un jeton de notification push Android valide, être abonné aux deux, mais ne pas avoir de jeton de notification push iOS associé. L'écart entre le nombre total d'utilisateurs joignables et la somme des différents canaux correspond aux utilisateurs qualifiés pour le segment mais non joignables via ces canaux de communication.

## Statistiques sur la taille des segments

Les statistiques estimées sont calculées à partir d'un échantillon de votre segment uniquement. Les tailles estimées peuvent donc être supérieures ou inférieures à la valeur réelle, avec des marges d'erreur potentiellement plus importantes pour les grands espaces de travail. Pour obtenir un décompte précis des utilisateurs de votre segment, sélectionnez **Calculer les statistiques exactes**. L'appartenance exacte au segment est toujours calculée avant qu'un segment ne soit affecté par un message envoyé dans le cadre d'une campagne ou d'un Canvas. 

Braze fournit les statistiques suivantes sur la taille des segments. 

### Statistiques sur les filtres

Pour chaque groupe de filtres, vous pouvez afficher le nombre estimé d'utilisateurs joignables. Sélectionnez **Développer les statistiques d'entonnoir supplémentaires** pour voir la répartition par canal.

![Un groupe de filtres avec un filtre pour les utilisateurs ayant eu exactement une session.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Estimation du nombre d'utilisateurs joignables

Vous pouvez consulter l'estimation des utilisateurs joignables d'un segment entier, y compris le nombre estimé d'utilisateurs par canal, dans le panneau latéral **Utilisateurs joignables**. Cette **estimation** vous donne une fourchette approximative de la taille de votre segment, ainsi qu'une estimation du pourcentage de votre base d'utilisateurs globale qui en fait partie. Les statistiques estimées sont mises en cache pendant 15 minutes, sauf si vous modifiez votre segment, auquel cas elles seront automatiquement recalculées. Vous pouvez également afficher le nombre exact d'utilisateurs joignables (pour l'ensemble du segment et par canal) en sélectionnant **Calculer les statistiques exactes**. 


![Le panneau « Utilisateurs joignables » indique qu'il y a entre 2,3 et 2,4 millions d'utilisateurs estimés.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Considérations relatives aux estimations

Braze mesure le nombre d'utilisateurs estimés en interrogeant un sous-ensemble de vos utilisateurs, puis extrapole ces résultats à l'ensemble de votre audience. Le sous-ensemble interrogé pouvant varier d'un calcul à l'autre, l'estimation peut elle aussi changer même si la composition de votre audience n'a techniquement pas évolué. Par exemple, si vous modifiez l'ordre de vos filtres ou si vous consultez le même segment à un autre moment, le nombre estimé peut varier (même si **Calculer les statistiques exactes** donnerait les mêmes résultats si votre segment n'a pas changé).

Si votre espace de travail compte un grand nombre d'utilisateurs, vous constaterez peut-être une plus grande variation entre vos estimations et vos calculs exacts, en particulier lorsque votre segment ne représente qu'un très faible pourcentage de la population totale de votre espace de travail. Braze mesure en effet l'estimation en interrogeant un sous-ensemble de vos utilisateurs et en extrapolant les résultats à l'ensemble de votre base. Pour les bases d'utilisateurs plus importantes, des écarts plus marqués entre les chiffres estimés et les chiffres exacts sont donc attendus.

Les segments de très petite taille auront une fourchette d'estimation incluant 0, ce qui signifie que le pourcentage du nombre total d'utilisateurs peut être arrondi à 0. Dans ces cas, **Calculer les statistiques exactes** vous permettra d'obtenir un décompte précis de la taille de votre segment, qui peut ne pas être égale à 0.

![Le panneau latéral « Utilisateurs joignables » affiche un nombre exact de « 31 » utilisateurs.]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Utilisateurs joignables par canal

Pour afficher le nombre d'utilisateurs joignables par canal de communication, sélectionnez **Afficher la répartition** dans le panneau **Utilisateurs joignables**. Cette vue présente certains des canaux de communication les plus fréquemment utilisés (tels que le push web ou l'e-mail) et le nombre d'utilisateurs joignables pour chacun. 

L'indicateur _Total_ représente les utilisateurs uniques. Par exemple, si un utilisateur dispose à la fois de la notification push Android et de la notification push iOS, il sera comptabilisé dans ces deux lignes, mais ne comptera que pour un seul utilisateur dans la ligne _Total_.

Toutefois, le nombre total d'utilisateurs peut différer de la somme des utilisateurs joignables par chaque canal, car un même utilisateur peut appartenir à différents groupes d'utilisateurs joignables. Par exemple, un utilisateur peut disposer d'une adresse e-mail valide et d'un jeton de notification push Android valide, être abonné aux deux, mais ne pas avoir de jeton de notification push iOS associé. 

Gardez à l'esprit que tous les canaux ne figurent pas dans le tableau des **utilisateurs joignables** (comme les cartes de contenu, les webhooks et WhatsApp). Par exemple, si certains de vos utilisateurs ne sont joignables que par WhatsApp, ils apparaîtront dans le _Total_ mais pas dans les lignes spécifiques aux canaux. Le nombre total d'utilisateurs joignables peut donc différer de la somme des utilisateurs pour chaque canal affiché.

Lorsque le _Total_ est supérieur à la somme des canaux, l'écart représente les utilisateurs qualifiés pour le segment mais non joignables via ces canaux de communication.

Pour qu'un utilisateur soit répertorié comme joignable via un canal donné, il doit :
- Disposer d'une adresse e-mail valide ou d'un jeton de notification push associé à son profil, et
- Être abonné à votre application.

#### Filtres appliqués pour les utilisateurs joignables par canal

Les filtres suivants sont appliqués à chaque canal lors de la détermination des utilisateurs joignables.

| Canal | Filtre |
| --- | --- |
| E-mail | **Email Available** est vrai. |
| Notification push | **Foreground Push Enabled** est vrai. |
| SMS | **Subscription Group** correspond à n'importe quel groupe d'abonnement SMS. **Invalid Phone Number** est faux. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Calculer des statistiques exactes 

Pour obtenir un décompte précis du nombre d'utilisateurs dans votre segment, sélectionnez **Calculer les statistiques exactes** dans le volet **Utilisateurs joignables**.

Pour actualiser les statistiques d'un calcul effectué précédemment, sélectionnez **Actualiser les statistiques exactes**. La date du dernier calcul sera automatiquement mise à jour.

La précision d'un calcul est de 99,999 % ou plus. Pour les grands segments, vous pouvez donc remarquer de légères variations&#8212;même en calculant des statistiques exactes&#8212;ce qui est un comportement normal. De plus, les résultats des statistiques exactes sont mis en cache pendant 24 heures, sauf si vous modifiez votre segment, auquel cas vous pouvez recalculer les statistiques exactes.

{% alert note %}
Les segments répartis de manière égale par [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) ne seront pas nécessairement de taille identique. Par exemple, si vous créez un segment avec le filtre **Random Bucket # inférieur à 5000** et un segment avec le filtre **Random Bucket # supérieur ou égal à 5000**, il est possible et prévisible que la taille des segments varie de quelques points de pourcentage. Cela s'explique par des situations telles que la suppression d'utilisateurs inactifs ou l'inaccessibilité de certains utilisateurs.
{% endalert %}

![Capture d'écran du panneau « Utilisateurs joignables » affichant les statistiques exactes et un menu de répartition développé.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Les statistiques au niveau de chaque filtre restent toujours des estimations, même lorsque vous calculez des statistiques exactes. **Calculer les statistiques exactes** ne produit des résultats exacts qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres. Ce calcul peut prendre quelques minutes. Les grands espaces de travail, en particulier, peuvent nécessiter des délais plus longs. Vous pouvez suivre la progression sur la barre de progression dans le panneau **Utilisateurs joignables**. Lorsqu'un calcul doit durer plus de cinq minutes, Braze vous envoie les résultats par e-mail. 

Braze traite un seul calcul à la fois par espace de travail : lancer plusieurs calculs simultanément entraînera donc des retards. Vous pouvez sélectionner **Afficher la file d'attente des calculs** pour voir quels segments sont en attente avant le vôtre, leur état d'avancement et leur initiateur, et avoir une idée du moment où votre calcul sera traité.

![Une file d'attente de calcul contenant un seul calcul.]({% image_buster /assets/img_archive/calculation_queue.png %})

Vous pouvez annuler un calcul de statistiques exactes en sélectionnant **Annuler**. Cela peut être utile lorsque plusieurs calculs sont dans la file d'attente et que vous souhaitez en prioriser un autre. 

![Un calcul actif avec la possibilité d'annuler]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:35%"}

## Consulter l'historique du nombre de membres d'un segment

Pour tous les segments, vous pouvez consulter un graphique historique indiquant le nombre estimé de membres du segment pour chaque jour. Ce graphique montre l'évolution de la taille de votre segment au fil du temps. Utilisez la liste déroulante pour filtrer l'appartenance au segment par plage de dates.

![Utilisez la liste déroulante Historique des membres pour filtrer l'appartenance au segment par plage de dates.]({% image_buster /assets/img_archive/historical_membership2.png %})

L'objectif de ce graphique est de vous donner une vue d'ensemble des tendances d'appartenance au segment. Le décompte quotidien est donc une estimation, de la même manière que la taille du segment est une estimation avant que vous ne sélectionniez **Calculer les statistiques exactes**. Comme ce graphique présente des estimations, il est possible que la taille de votre segment apparaisse comme « 0 », même si sa taille réelle (déterminée après avoir sélectionné **Calculer les statistiques exactes**) n'est pas « 0 ». C'est particulièrement probable si votre segment est très petit par rapport à la population de votre espace de travail.

Par exemple, supposons que votre espace de travail compte 100 millions d'utilisateurs et que votre segment en compte environ 700. Il est possible que certains jours, aucun utilisateur ne se trouve dans le segment et qu'aucun utilisateur ne tombe dans la plage de compartiments aléatoires utilisée pour l'estimation historique, ce qui donne un nombre de membres journalier de 0.

Braze estime le nombre de membres d'un segment en interrogeant un sous-ensemble de vos utilisateurs, puis en extrapolant ces résultats à l'ensemble de votre audience. Les résultats du graphique ne fournissent donc qu'une estimation du nombre de membres du segment pour un jour donné, et des fluctuations d'un jour à l'autre sont attendues, car un échantillon différent d'utilisateurs peut être interrogé chaque jour.

{% alert note %}
Toutes les estimations peuvent être supérieures ou inférieures à la valeur indiquée d'environ 1 % de la population totale de votre espace de travail. Les espaces de travail plus vastes sont plus susceptibles de présenter des estimations qui diffèrent des calculs exacts d'un montant numérique plus élevé, même si la différence reste de l'ordre de 1 % de la population de l'espace de travail. Des écarts plus importants entre les estimations et les chiffres exacts sont donc attendus pour les grands espaces de travail.
{% endalert %}

### Raisons des changements importants

Le nombre de membres peut varier de manière significative pour plusieurs raisons, comme celles présentées dans ce tableau.

| Raison | Exemple |
| --- | --- |
| Comportement normal des utilisateurs | Les utilisateurs s'abonnent après une campagne particulièrement réussie. |
| Importation d'utilisateurs par fichier CSV | L'importation d'un fichier CSV d'utilisateurs a considérablement augmenté le nombre de membres du segment. |
| Modification des critères d'audience du segment | Les règles d'audience d'un segment existant (telles que les filtres) ont été modifiées, entraînant des changements importants dans la composition du segment. |
| Suppression d'utilisateurs | Un nombre important d'utilisateurs a été supprimé. |
| Synchronisation d'une intégration partenaire avec Braze | Un tiers a envoyé à Braze des données qui ont significativement influencé l'appartenance au segment. |
| Archivage des utilisateurs dormants | Un nombre important de profils inactifs ont été archivés. Par exemple, un grand nombre d'utilisateurs importés par fichier CSV n'enregistrent jamais d'activité et sont archivés en même temps. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}