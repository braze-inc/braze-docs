---
nav_title: Groupe de contrôle global
article_title: Groupe de contrôle global
alias: /global_control_group/
page_order: 0

description: "Cet article explique comment configurer et utiliser correctement le groupe de contrôle global. Il explique également comment consulter les rapports et les indicateurs résultant de l'utilisation de ces groupes."
page_type: reference
tool: Reports
search_rank: 1

---

# Groupe de contrôle global

> Utilisez le groupe de contrôle global pour spécifier un pourcentage de tous les utilisateurs qui ne devraient pas recevoir de campagnes ou de canevas, ce qui vous permet d'analyser l'impact global de vos envois de messages au fil du temps. 

En comparant les comportements des utilisateurs qui reçoivent des messages à ceux qui n'en reçoivent pas, vous pouvez mieux comprendre comment vos campagnes de communication et vos Canvas se traduisent par une augmentation des sessions et des événements personnalisés.

## Fonctionnement du groupe de contrôle global

Avec le groupe de contrôle global, vous pouvez définir un pourcentage de tous les utilisateurs comme groupe de contrôle. Lorsqu'il est enregistré, les utilisateurs du groupe ne recevront aucune campagne ni aucun canevas. 

{% alert important %}
Votre groupe de contrôle global s'applique à tous les canaux, campagnes et canevas, à l'exception des [campagnes API.]({{site.baseurl}}/api/api_campaigns) Cela signifie que les utilisateurs de votre groupe de contrôle recevront toujours des campagnes API. Toutefois, cette exception ne s'applique pas aux cartes de contenu. Si vous utilisez une campagne de cartes de contenu déclenchée par l'API, les utilisateurs de votre groupe de contrôle ne les recevront pas.
{% endalert %}

### Affecter des utilisateurs de manière aléatoire au groupe de contrôle global

Braze sélectionne de manière aléatoire plusieurs plages de [numéros de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) et inclut les utilisateurs de ces compartiments sélectionnés. Si vous utilisez actuellement des numéros de compartiment aléatoire à d'autres fins, consultez la rubrique [Choses à surveiller.](#things-to-watch-for) 

Lorsque votre groupe de contrôle global est généré, tous les utilisateurs ayant un numéro de compartiment aléatoire font partie du groupe. En outre, les nouveaux utilisateurs qui s'inscrivent après cette date (ceux qui ont été recrutés après la création du groupe de contrôle global) et qui possèdent ces numéros de compartiment aléatoires seront également ajoutés au groupe de contrôle global. De même, si de nombreux utilisateurs sont supprimés, vous pouvez vous attendre à ce que la taille de votre groupe de contrôle global diminue, car un pourcentage de ces utilisateurs supprimés sera tombé dans ce groupe. Cela permet de maintenir la taille de votre groupe à un pourcentage constant par rapport à l'ensemble de votre base d'utilisateurs.

### Affecter les utilisateurs de manière aléatoire au groupe de traitement pour l'établissement de rapports

Pour vous permettre de rendre compte de l'élévation, Braze crée également un groupe de traitement. Le groupe de traitement est un groupe d'utilisateurs sélectionnés de manière aléatoire qui ne fait pas partie de votre groupe de contrôle global et qui est généré à l'aide de la même méthode de numéro compartiment aléatoire que le groupe de contrôle global. 

Votre groupe de traitement sera de taille similaire à votre groupe de contrôle global, mais il est peu probable qu'il soit exactement de la même taille. Pour les [rapports](#reporting), Braze mesure les comportements des utilisateurs de votre groupe de contrôle et des utilisateurs de votre échantillon de traitement. Chaque espace de travail comporte au maximum un groupe de contrôle global et un groupe d'échantillons de traitement. Le groupe de l'échantillon de traitement est le même groupe d'utilisateurs, quelle que soit la manière dont vous configurez votre rapport de contrôle global.

### Exclure les utilisateurs des drapeaux de fonctionnalité

Vous ne pouvez pas activer les [drapeaux de fonctionnalité]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) pour les utilisateurs de votre groupe de contrôle global. Cela signifie que les utilisateurs de votre groupe de contrôle global ne peuvent pas non plus participer aux expériences de marquage des fonctionnalités.

### Exclure les utilisateurs du groupe de contrôle global

Vous ne pouvez pas supprimer des utilisateurs spécifiques du groupe de contrôle global, mais vous pouvez ajouter des [paramètres d'exclusion]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings) afin que les campagnes et les toiles avec des étiquettes spécifiques n **'utilisent pas le groupe de contrôle global.**  Vous pouvez également désactiver et réactiver votre groupe de contrôle global pour mélanger les membres. La durée idéale du brassage des utilisateurs varie en fonction du type de test que vous effectuez, mais nous vous encourageons à ne pas le faire plus d'une fois par mois.

## Créer un groupe de contrôle global

### Étape 1 : Naviguez jusqu'au groupe de contrôle global Paramètres

Dans le tableau de bord, allez dans **Audience** > **Groupe de** contrôle global.

### Étape 2 : Assigner un pourcentage de tous les utilisateurs à ce groupe de contrôle

Saisissez un pourcentage pour votre groupe de contrôle et sélectionnez **Enregistrer.** Une fois saisi, Braze vous indique une estimation du nombre d'utilisateurs qui entreront dans votre échantillon de contrôle global, de traitement et de traitement. Gardez à l'esprit que plus vous avez d'utilisateurs dans votre espace de travail, plus cette estimation sera précise. 

Le nombre d'utilisateurs de votre groupe de contrôle global est automatiquement mis à jour après sa configuration initiale pour rester proportionnel à ce pourcentage lorsque des utilisateurs sont ajoutés à votre espace de travail. En outre, les utilisateurs qui ont rejoint le groupe après la création du groupe de contrôle global et qui ont des numéros de compartiment aléatoires seront également ajoutés au groupe de contrôle global. Si de nombreux utilisateurs sont ajoutés, la taille de votre groupe de contrôle global augmentera afin de maintenir un pourcentage constant par rapport à l'ensemble de votre base d'utilisation. Lorsque la taille de votre groupe de contrôle global augmente, les utilisateurs qui en faisaient partie auparavant restent dans le groupe (à moins que vous ne modifiiez votre groupe en le désactivant et en en créant un nouveau).

Pour connaître les pourcentages, reportez-vous aux [meilleures pratiques en matière de tests.](#percentage-guidelines)

Les paramètres du groupe de contrôle global avec les paramètres d'audience réglés sur "Assigner cinq pour cent de tous les utilisateurs au groupe de contrôle global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Étape 3 : Attribuer des paramètres d'exclusion

Utilisez les tags pour ajouter des paramètres d'exclusion à votre groupe de contrôle global. Les campagnes ou les toiles qui utilisent les étiquettes incluses dans les paramètres d'exclusion n'utilisent pas votre groupe de contrôle global. Ces campagnes et Canevas continuent d'être envoyés à chaque utilisateur de l'audience cible, y compris ceux de votre groupe de contrôle global.

{% alert tip %}
Vous pouvez ajouter des paramètres d'exclusion si vous avez des messages transactionnels qui doivent être envoyés à chaque utilisateur.
{% endalert %}

Cette section permet d'ajouter ou de modifier les paramètres d'exclusion de votre groupe de contrôle global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Étape 4 : Enregistrez votre groupe de contrôle

À ce stade, Braze génère un groupe d'utilisateurs sélectionnés de manière aléatoire pour constituer le pourcentage choisi de votre base totale d'utilisateurs. Lorsque vous l'enregistrez, toutes les campagnes et tous les canevas actifs et futurs n'envoient plus d'informations aux utilisateurs de ce groupe, à l'exception des campagnes ou des canevas qui contiennent l'une des étiquettes définies dans vos paramètres d'exclusion.

## Modifier votre groupe de contrôle global

Vous ne pouvez modifier votre groupe de contrôle global qu'en le désactivant et en en créant un nouveau. Par exemple, si vous créez un groupe de contrôle global représentant 10 % de votre audience et que vous souhaitez réduire sa taille à 5 %, vous devez désactiver votre groupe de contrôle global actuel et réactiver un nouveau groupe de contrôle global. 

Vous pouvez désactiver votre groupe de contrôle global à tout moment à partir de l'onglet **Paramètres du groupe de contrôle global**, mais gardez à l'esprit que les utilisateurs de ce groupe deviendront immédiatement éligibles pour les campagnes et les toiles.

Avant de désactiver votre groupe de contrôle, nous vous recommandons d'[exporter](#export-group-members) un fichier CSV des utilisateurs de ce groupe au cas où vous auriez besoin d'y faire référence ultérieurement. Lorsque vous désactivez un groupe de contrôle, il n'y a aucun moyen pour Braze de restaurer le groupe ou d'identifier les utilisateurs qui faisaient partie de ce groupe.

Après avoir désactivé votre groupe de contrôle, vous pouvez en enregistrer un nouveau. Lorsque vous entrez un pourcentage et que vous l'enregistrez, Braze génère un nouveau groupe d'utilisateurs sélectionnés de manière aléatoire. Si vous introduisez le même pourcentage que précédemment, Braze génère toujours un nouveau groupe d'utilisateurs pour vos groupes de contrôle et de traitement.

Une boîte de dialogue intitulée "Vous modifiez les paramètres généraux des messages" contenant un texte avertissant qu'une fois votre groupe de contrôle global désactivé, il ne sera plus exclu des campagnes ou des canevas nouveaux ou actifs.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exporter les membres de votre groupe de contrôle {#export-group-members}

Si vous souhaitez voir quels utilisateurs font partie de votre groupe de contrôle global, vous pouvez exporter les membres de votre groupe par CSV ou API. 

Pour lancer une exportation CSV, accédez à l'onglet **Paramètres du groupe de contrôle global** et cliquez sur <i class="fas fa-download"></i> **Export.** Pour exporter par API, utilisez l'[endpoint`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Les groupes de contrôle historiques ne sont pas conservés. Vous ne pouvez donc exporter que les membres de votre groupe actuel. Veillez à exporter toutes les informations nécessaires avant de désactiver un groupe de contrôle.
{% endalert %}

## Vérifier si un utilisateur fait partie d'un groupe de contrôle global

Vous pouvez consulter l'appartenance à un groupe de contrôle global en allant dans la section **Divers de** l'onglet **Engagement** du profil d'un utilisateur individuel.

Une section "Divers" indique que l'utilisateur a un numéro de compartiment aléatoire de 6356 et qu'il ne fait pas partie du groupe de contrôle global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Rapports

Pour plus d'informations sur les indicateurs des rapports, reportez-vous à la section [Rapports des groupes de contrôle globaux]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/).

## Résolution des problèmes

Lorsque vous configurez vos groupes de contrôle global et que vous visualisez les rapports, voici les erreurs que vous pouvez rencontrer :

| Enjeu | Résolution des problèmes |
| --- | --- |
| Impossible d'enregistrer le pourcentage saisi lors de la désignation d'un groupe de contrôle global. | Ce problème survient si vous entrez un nombre non entier ou un nombre entier qui n'est pas compris entre 1 et 15 (inclus). |
| Erreur "Braze n'est pas en mesure de mettre à jour votre groupe de contrôle global" sur la page des paramètres du contrôle global. | Cela indique généralement qu'un élément de cette page a été modifié, probablement en raison d'actions entreprises par un autre utilisateur sur votre compte Braze. Dans ce cas, actualisez la page et réessayez. |
| Le rapport du groupe de contrôle global ne contient aucune donnée. | Si vous accédez au rapport sur les groupes de contrôle global sans avoir enregistré un groupe de contrôle global, vous ne verrez aucune donnée dans le rapport. Créez et enregistrez un groupe de contrôle global et réessayez. |
| Mon taux de conversion est de 0 % ou je ne vois pas le graphique s'afficher, bien qu'il y ait plus de zéro événement. | Si le nombre de conversions est très faible et que vos groupes de contrôle ou de traitement sont très importants, le taux de conversion peut être arrondi à 0 % et ne pas apparaître dans le graphique. Vous pouvez le vérifier en consultant les indicateurs du nombre total d'événements. Vous pourriez comparer l'efficacité de vos deux groupes en utilisant l'indicateur du pourcentage d'augmentation incrémentielle.  |
| Mon taux de conversion (ou d'autres indicateurs) change radicalement en fonction de la période pour laquelle je consulte les données. | Si vous consultez des données sur de courtes périodes, il est possible que vos indicateurs fluctuent d'un jour à l'autre ou d'une semaine à l'autre. Nous vous recommandons de consulter les indicateurs sur une période d'au moins un mois. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Les points à surveiller {#things-to-watch-for}

#### Nombre de compartiments aléatoires se chevauchant

Votre groupe de contrôle global est constitué à l'aide de numéros de compartiment aléatoire. Par conséquent, si vous effectuez d'autres tests à l'aide de filtres de segment aléatoire, gardez à l'esprit qu'il peut y avoir un chevauchement entre les segments que vous créez et les utilisateurs de votre groupe de contrôle global.

#### Adresses e-mail en double

Si deux utilisateurs ayant des ID externes différents ont la même adresse e-mail, et que l'un de ces utilisateurs fait partie du groupe de contrôle et l'autre non, un e-mail sera quand même envoyé à cette adresse e-mail chaque fois que l'utilisateur ne faisant pas partie du groupe de contrôle est éligible pour recevoir un e-mail. Dans ce cas, nous marquerons les deux profils utilisateurs comme ayant reçu la campagne ou le canvas contenant cet e-mail.

#### Groupe de contrôle global et groupes de contrôle spécifiques aux messages

Il est possible d'avoir à la fois un groupe de contrôle global et d'utiliser un groupe de contrôle spécifique à une campagne ou à un Canvas. Le fait de disposer d'un groupe de contrôle spécifique à la campagne ou au Canvas vous permet de mesurer l'impact d'un message particulier.

Les utilisateurs de votre groupe de contrôle global sont empêchés de recevoir tout message autre que ceux comportant des exceptions d'étiquette, et si vous ajoutez un contrôle à une campagne ou à un Canvas, Braze empêche une partie de votre groupe de traitement global de recevoir cette campagne ou ce Canvas en particulier. Cela signifie que si un membre du groupe de contrôle global n'est pas éligible pour recevoir une campagne ou un Canvas particulier, il ne sera pas non plus présent dans le groupe de contrôle pour cette campagne ou ce Canvas particulier.

> En bref, les utilisateurs du groupe de contrôle global sont filtrés de la campagne ou de l'audience de Canvas avant leur entrée. Parmi les utilisateurs qui entrent dans la campagne ou le Canvas, un pourcentage d'entre eux est ensuite affecté à la variante de contrôle.

#### Segments du groupe de contrôle global dans la console de développement

Vous pouvez voir plusieurs segments de **contrôle global** dans la section **Identifiants d'API supplémentaires** de la page [Clés d'API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). En effet, chaque fois que le groupe de contrôle global est activé ou désactivé, un nouveau groupe de contrôle global est formé. Cela conduit à plusieurs segments intitulés "groupe de contrôle global".

Un seul de ces segments est actif et peut être interrogé à l'aide de l'[endpoint`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/), ou exporté à partir du tableau de bord. L'exportation du tableau de bord indique spécifiquement les sous-segments qui composent ce groupe de contrôle global.

## Meilleures pratiques en matière d'essais

### Taille optimale du groupe de contrôle {#percentage-guidelines}

Les deux principales règles à garder à l'esprit sont\** :
1. Votre groupe de contrôle ne doit pas être inférieur à 1000 utilisateurs.
2. Votre groupe de contrôle ne doit pas représenter plus de 10 % de l'ensemble de votre audience.

Si votre audience totale est inférieure à 10 000 personnes, vous devez augmenter votre pourcentage pour créer un groupe de plus de 1 000 utilisateurs ; dans ce cas, vous ne devez pas augmenter votre pourcentage au-delà de 15 %. Gardez à l'esprit que plus votre espace de travail est petit, plus il sera difficile d'effectuer un test statistiquement rigoureux.

- Certains compromis sont à prendre en compte lorsque vous réfléchissez à la taille de votre groupe de contrôle : vous devez disposer d'un nombre significativement élevé de clients dans votre groupe de contrôle pour que toute analyse de comportement créée soit fiable. Cependant, plus votre groupe de contrôle est important, moins il y a de clients qui reçoivent vos campagnes, ce qui est un inconvénient si vous utilisez vos campagnes pour stimuler l'engagement et les conversions.
- Le pourcentage idéal dépendra de la taille de votre audience totale. Plus votre audience totale est importante, plus votre pourcentage peut être faible. En revanche, si votre audience est restreinte, vous aurez besoin d'un pourcentage plus élevé pour votre groupe de contrôle.

### Durée de l'expérience 

#### Choisissez une durée idéale {#reshuffle}

La durée de l'expérience avant de modifier la composition du groupe de contrôle dépend de ce que vous testez et des comportements de base de vos utilisateurs. Si vous n'êtes pas sûr, commencez par un trimestre (trois mois), mais ne descendez pas en dessous d'un mois.

Pour déterminer la durée appropriée de votre expérience, réfléchissez aux questions auxquelles vous souhaitez répondre. Par exemple, cherchez-vous à voir s'il y a une différence entre les sessions ? Si c'est le cas, réfléchissez à la fréquence des sessions organiques de vos utilisateurs. Les marques dont les utilisateurs se connectent tous les jours peuvent mener des expériences plus courtes que celles dont les utilisateurs ne se connectent que quelques fois par mois. 

Vous pouvez également vous intéresser à un événement personnalisé, et votre expérience devra alors durer plus longtemps qu'une expérience où vous examinez des sessions, s'il est probable que vos utilisateurs déclenchent cet événement personnalisé moins fréquemment.

{% alert tip %}
Plus vous gardez longtemps le même groupe de contrôle, plus il diverge du groupe de traitement, ce qui peut créer un biais. La réinitialisation du groupe de contrôle global rééquilibre la population.
{% endalert %}

#### Essayez de ne pas mettre fin prématurément aux expériences

Vous devez décider de la durée de votre expérience avant de la commencer, et vous ne devez terminer votre expérience et rassembler les résultats finaux qu'après avoir atteint ce point prédéterminé. Mettre fin à votre expérience prématurément, ou dès que vous obtenez des données prometteuses, introduira un biais.

#### Pensez à des indicateurs utiles

Tenez compte des comportements de référence pour les indicateurs qui vous intéressent le plus. Êtes-vous intéressé par les tarifs d'achat pour les plans d'abonnement qui sont renouvelés uniquement sur une base annuelle ? Ou bien les clients ont-ils une habitude hebdomadaire pour l'événement que vous aimeriez mesurer ? Pensez au temps qu'il faut aux utilisateurs pour modifier potentiellement leur comportement à la suite de votre envoi de messages. Une fois que vous avez décidé de la durée de votre expérience, veillez à ne pas la terminer ou à ne pas enregistrer les résultats finaux trop tôt, car vos conclusions risqueraient d'être faussées.

