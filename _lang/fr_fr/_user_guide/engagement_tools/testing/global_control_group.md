---
nav_title: Groupe de contrôle global
article_title: Groupe de contrôle global
alias: /global_control_group/
page_order: 0

description: "Cet article explique comment configurer et utiliser correctement le groupe de contrôle global. Il explique également comment consulter les mesures et les rapports liés à l’utilisation de ces groupes."
page_type: reference
tool: Reports
search_rank: 1

---

# Groupe de contrôle global

> Utilisez le groupe de contrôle global pour indiquer un pourcentage de tous les utilisateurs qui ne devraient pas recevoir de campagnes ou de Canvas, ce qui vous permet d’analyser l’impact global de vos efforts de communication au fil du temps. 

En comparant les comportements des utilisateurs qui reçoivent des messages à ceux qui n’en reçoivent pas, vous pouvez mieux comprendre comment vos Canvas et campagnes marketing entraînent une augmentation du nombre de sessions et d’événements personnalisés.

## Fonctionnement du groupe de contrôle global

Avec le groupe de contrôle global, vous pouvez définir un pourcentage de tous les utilisateurs comme groupe de contrôle. Lorsqu'il est enregistré, les utilisateurs du groupe ne recevront aucune campagne ni aucun canevas. 

{% alert important %}
Votre groupe de contrôle global s'applique à tous les canaux, campagnes et canevas, à l'exception des [campagnes API.]({{site.baseurl}}/api/api_campaigns) Cela signifie que les utilisateurs de votre groupe de contrôle recevront toujours des campagnes API. Toutefois, cette exception ne s'applique pas aux cartes de contenu. Si vous utilisez une campagne de cartes de contenu déclenchée par l'API, les utilisateurs de votre groupe de contrôle ne les recevront pas.
{% endalert %}

### Assigner des utilisateurs au groupe de contrôle global de manière aléatoire

Braze sélectionne de manière aléatoire plusieurs plages de [numéros de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) et inclut les utilisateurs de ces compartiments sélectionnés. Si vous utilisez actuellement des numéros de compartiment aléatoire à d'autres fins, consultez la rubrique [Choses à surveiller.](#things-to-watch-for) 

Lorsque votre groupe de contrôle global est généré, tous les utilisateurs ayant un numéro de compartiment aléatoire font partie du groupe. En outre, les nouveaux utilisateurs qui s'inscrivent après cette date (ceux qui ont été recrutés après la création du groupe de contrôle global) et qui possèdent ces numéros de compartiment aléatoires seront également ajoutés au groupe de contrôle global. De même, si de nombreux utilisateurs sont supprimés, vous pouvez vous attendre à ce que la taille de votre groupe de contrôle global diminue, car un pourcentage de ces utilisateurs supprimés sera tombé dans ce groupe. Cela permet de maintenir la taille de votre groupe à un pourcentage constant par rapport à l'ensemble de votre base d'utilisateurs.

### Affecter les utilisateurs de manière aléatoire au groupe de traitement pour l'établissement de rapports

Pour vous permettre de rendre compte de l'élévation, Braze crée également un groupe de traitement. Le groupe de traitement est un groupe d'utilisateurs sélectionnés de manière aléatoire qui ne fait pas partie de votre groupe de contrôle global et qui est généré à l'aide de la même méthode de numéro compartiment aléatoire que le groupe de contrôle global. 

Votre groupe de traitement sera de taille similaire à votre groupe de contrôle global, mais il est peu probable qu'il soit exactement de la même taille. Pour les [rapports](#reporting), Braze mesure les comportements des utilisateurs de votre groupe de contrôle et des utilisateurs de votre échantillon de traitement. Chaque espace de travail comporte au maximum un groupe de contrôle global et un groupe d'échantillons de traitement. Le groupe de l'échantillon de traitement est le même groupe d'utilisateurs, quelle que soit la manière dont vous configurez votre rapport de contrôle global.

### Exclure les utilisateurs des drapeaux de fonctionnalité

Vous ne pouvez pas activer les [drapeaux de fonctionnalité]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) pour les utilisateurs de votre groupe de contrôle global. Cela signifie que les utilisateurs de votre groupe de contrôle global ne peuvent pas non plus participer aux expériences de marquage des fonctionnalités.

## Créer un groupe de contrôle global

### Étape 1 : Accédez aux paramètres du groupe de contrôle global

Dans le tableau de bord, sélectionnez **Audience** > **Groupe de contrôle global**.

### Étape 2 : Attribuez un pourcentage de tous les utilisateurs à ce groupe de contrôle

Saisissez un pourcentage pour votre groupe de contrôle et sélectionnez **Enregistrer.** Une fois le pourcentage saisi, Braze vous montre une estimation du nombre d’utilisateurs qui seront ajoutés à votre groupe de contrôle global, votre groupe de traitement et votre échantillon de traitement. Gardez à l'esprit que plus vous avez d'utilisateurs dans votre espace de travail, plus cette estimation sera précise. 

Le nombre d'utilisateurs de votre groupe de contrôle global est automatiquement mis à jour après sa configuration initiale pour rester proportionnel à ce pourcentage lorsque des utilisateurs sont ajoutés à votre espace de travail. En outre, les utilisateurs qui ont rejoint le groupe après la création du groupe de contrôle global et qui ont des numéros de compartiment aléatoires seront également ajoutés au groupe de contrôle global. Si de nombreux utilisateurs sont ajoutés, la taille de votre groupe de contrôle global augmentera afin de maintenir un pourcentage constant par rapport à l'ensemble de votre base d'utilisation. Lorsque la taille de votre groupe de contrôle global augmente, les utilisateurs qui en faisaient partie auparavant restent dans le groupe (à moins que vous ne modifiiez votre groupe en le désactivant et en en créant un nouveau).

Pour connaître les pourcentages, reportez-vous aux [meilleures pratiques en matière de tests.](#percentage-guidelines)

![Les paramètres du groupe de contrôle global avec les paramètres d'audience réglés sur "Attribuer cinq pour cent de tous les utilisateurs au groupe de contrôle global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Étape 3 : Attribuer des paramètres d’exclusion

Vous pouvez utiliser des balises pour ajouter des paramètres d’exclusion à votre groupe de contrôle global. Les campagnes ou les Canvas qui utilisent les balises incluses dans les paramètres d’exclusion n’utiliseront pas votre groupe de contrôle global. Ces campagnes et Canvas continueront d’être envoyés à chaque utilisateur de l’audience cible, y compris ceux de votre groupe de contrôle global.

{% alert tip %}
Vous souhaiterez peut-être ajouter des paramètres d’exclusion si vous devez envoyer des messages transactionnels à chaque utilisateur.
{% endalert %}

![Section permettant d'ajouter ou de modifier les paramètres d'exclusion pour votre groupe de contrôle global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Étape 4 : Enregistrer votre groupe de contrôle

À ce stade, Braze génère un groupe d’utilisateurs sélectionnés de manière aléatoire pour inclure le pourcentage sélectionné de l’ensemble de votre base d’utilisateurs. Lorsque vous l'enregistrez, toutes les campagnes et tous les canevas actifs et futurs n'envoient plus d'informations aux utilisateurs de ce groupe, à l'exception des campagnes ou des canevas qui contiennent l'une des étiquettes définies dans vos paramètres d'exclusion.

## Modifier votre groupe de contrôle global

Vous ne pouvez modifier votre groupe de contrôle global qu'en le désactivant et en en créant un nouveau. Par exemple, si vous créez un groupe de contrôle global représentant 10 % de votre audience et que vous souhaitez réduire sa taille à 5 %, vous devez désactiver votre groupe de contrôle global actuel et réactiver un nouveau groupe de contrôle global. 

Vous pouvez désactiver votre groupe de contrôle global à tout moment à partir de l'onglet **Paramètres du groupe de contrôle global**, mais gardez à l'esprit que les utilisateurs de ce groupe deviendront immédiatement éligibles pour les campagnes et les toiles.

Avant de désactiver votre groupe de contrôle, nous vous recommandons d'[exporter](#export-group-members) un fichier CSV des utilisateurs de ce groupe au cas où vous auriez besoin d'y faire référence ultérieurement. Lorsque vous désactivez un groupe de contrôle, il n'y a aucun moyen pour Braze de restaurer le groupe ou d'identifier les utilisateurs qui faisaient partie de ce groupe.

Vous pouvez enregistrer un nouveau groupe après avoir désactivé votre groupe de contrôle. Lorsque vous entrez un pourcentage et que vous l'enregistrez, Braze génère un nouveau groupe d'utilisateurs sélectionnés de manière aléatoire. Si vous saisissez le même pourcentage qu’auparavant, Braze génèrera toujours un nouveau groupe d’utilisateurs pour vos groupes de contrôle et de traitement.

![Une boîte de dialogue intitulée "Vous êtes en train de modifier les paramètres généraux des messages" avec un texte avertissant qu'une fois votre groupe de contrôle global désactivé, il ne sera plus exclu des campagnes ou des canevas nouveaux ou actifs.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exporter vos membres de groupe de contrôle {#export-group-members}

Si vous souhaitez voir quels utilisateurs font partie de votre groupe de contrôle global, vous pouvez exporter les membres de votre groupe par CSV ou API. 

Pour lancer une exportation CSV, accédez à l'onglet **Paramètres du groupe de contrôle global** et cliquez sur <i class="fas fa-download"></i> **Export.** Pour exporter par API, utilisez l'[endpoint`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Les groupes de contrôle historiques ne sont pas conservés, vous pouvez donc uniquement exporter les membres de votre groupe actuel. Assurez-vous d’exporter toutes les informations nécessaires avant de désactiver un groupe de contrôle.
{% endalert %}

## Vérifier si un utilisateur fait partie d'un groupe de contrôle global

Vous pouvez consulter l'appartenance à un groupe de contrôle global en allant dans la section **Divers de** l'onglet **Engagement** du profil d'un utilisateur individuel.

![Une section "Divers" indique que l'utilisateur a un numéro de compartiment aléatoire de 6356 et qu'il ne fait pas partie du groupe de contrôle global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Reporting

Pour plus d'informations sur les indicateurs des rapports, reportez-vous à la section [Rapports des groupes de contrôle globaux]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/).

## Résolution des problèmes

Vous trouverez ci-dessous quelques erreurs que vous pourriez rencontrer au moment de configurer vos groupes de contrôle globaux et de consulter vos rapports :

| Problème | Résolution des problèmes |
| --- | --- |
| Impossible d’enregistrer le pourcentage saisi au moment de désigner un groupe de contrôle global. | Ce problème survient si vous entrez un nombre entier ou non entier qui n’est pas compris entre 1 et 15 inclus. |
| Erreur « Braze ne peut pas mettre à jour votre groupe de contrôle global » sur la page Paramètres de contrôle global. | Cela indique généralement que certains composants de cette page ont été modifiés, probablement par un autre utilisateur de votre compte Braze. Dans ce cas, actualisez la page et réessayez. |
| Le rapport du groupe de contrôle global ne contient aucune donnée. | Si vous consultez le rapport du groupe de contrôle global sans avoir enregistré de groupe de contrôle global, vous ne verrez aucune donnée dans le rapport. Créez et enregistrez un groupe de contrôle global, puis réessayez. |
| Mon taux de conversion est de 0 % ou le graphique ne s’affiche pas, même s’il y a plus de zéro événement. | Si le nombre de conversions est très faible et que vos groupes de contrôle ou de traitement sont très importants, il se peut que le taux de conversion soit arrondi à 0 % et qu’il ne soit pas pris en compte dans le graphique. Vous pouvez vérifier cela en cochant la mesure Total Number of Events (Nombre total d’événements). Vous pouvez comparer l’efficacité de vos deux groupes à l’aide de la mesure du pourcentage d’augmentation progressive.  |
| Mon taux de conversion (ou d’autres mesures) change considérablement en fonction de la période pendant laquelle je consulte les données. | Si vous visualisez des données sur de courtes périodes, il se peut que vos mesures fluctuent de jour en jour ou de semaine en semaine. Nous vous recommandons d’afficher les indicateurs sur une période d’au moins un mois. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Choses à garder à l’esprit {#things-to-watch-for}

#### Chevauchement des numéros de compartiment aléatoires

Votre groupe de contrôle global est créé à l’aide de numéros de compartiment aléatoires. Si vous exécutez d’autres tests à l’aide des filtres de segments de numéros de compartiment aléatoires, gardez donc à l’esprit qu’il pourrait y avoir un chevauchement entre les segments que vous créez et les utilisateurs de votre groupe de contrôle global.

#### Adresses e-mail en double

Si deux utilisateurs ayant des ID d’utilisateur externe différents ont la même adresse e-mail, et que l’un des deux utilisateurs se trouve dans le groupe de contrôle, un e-mail sera toujours envoyé à cette adresse e-mail chaque fois que l’utilisateur du groupe non contrôlé est éligible à recevoir un e-mail. Lorsque cela se produit, nous désignerons les deux profils utilisateur comme ayant reçu la campagne ou le Canvas contenant cet e-mail.

#### Groupe de contrôle global et groupes de contrôle spécifiques aux communications

Vous pouvez avoir un groupe de contrôle global tout en utilisant un groupe de contrôle spécifique aux campagnes ou aux Canvas. Avoir un groupe de contrôle spécifique pour vos campagnes ou Canvas vous permet de mesurer l’impact d’un message donné.

Les utilisateurs de votre groupe de contrôle global recevront uniquement des messages qui comportent des exceptions de balise, et si vous ajoutez un groupe de contrôle à une campagne ou à un Canvas, Braze bloquera l’envoi de cette campagne ou de ce Canvas pour une partie de votre groupe de traitement global. Cela signifie que si un membre du groupe de contrôle global n’est pas éligible pour recevoir une campagne ou un Canvas donné, ils ne seront pas non plus présents dans le groupe de contrôle correspondant à cette campagne ou ce Canvas.

> En bref, les utilisateurs du groupe de contrôle global sont exclus de l’audience de la campagne ou du Canvas. Un pourcentage des utilisateurs inclus dans la campagne ou le Canvas est ensuite affecté à la variante de contrôle.

#### Segments du groupe de contrôle global sur la console de développement

Vous pouvez voir plusieurs segments de **contrôle global** dans la section **Identifiants d'API supplémentaires** de la page [Clés d'API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). En effet, un nouveau groupe de contrôle global est créé chaque fois que le groupe de contrôle global est activé ou désactivé. Cela conduit donc à la création de plusieurs segments portant la mention « Global Control Group (Groupe de contrôle global) ».

Un seul de ces segments est actif et peut être interrogé à l'aide de l'[endpoint`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/), ou exporté à partir du tableau de bord. L’exportation depuis le tableau de bord indique spécifiquement quels sous-segments composent ce groupe de contrôle global.

## Mettre les meilleures pratiques à l’épreuve

### Taille optimale du groupe de contrôle {#percentage-guidelines}

Les deux principales règles à garder à l'esprit sont\*\* :
1. Votre groupe de contrôle ne doit pas comporter moins de 1 000 utilisateurs.
2. Votre groupe de contrôle ne doit pas dépasser 10 % de l’ensemble de votre audience.

Si vous avez une audience totale inférieure à 10 000 utilisateurs, vous devez augmenter votre pourcentage pour créer un groupe de plus de 1 000 utilisateurs ; dans ce cas, vous ne devez pas augmenter votre pourcentage au-delà du seuil des 15 %. Gardez à l'esprit que plus votre espace de travail est petit, plus il sera difficile d'effectuer un test statistiquement rigoureux.

- Notez qu’il existe certains compromis à prendre en compte lorsque vous réfléchissez à la taille de votre groupe de contrôle. Par exemple, votre groupe de contrôle doit comporter un grand nombre de clients afin de garantir la fiabilité de vos analyses comportementales. Cependant, plus votre groupe de contrôle est important, plus le nombre de clients qui reçoivent vos campagnes sera réduit, ce qui est un inconvénient si vous utilisez vos campagnes pour stimuler l’engagement et augmenter les conversions.
- Le pourcentage idéal de votre audience globale dépendra donc de la taille de votre audience globale. Plus votre audience globale est importante, plus votre pourcentage sera réduit. Cependant, si votre audience est de petite taille, vous aurez besoin d’un pourcentage plus important pour votre groupe de contrôle.

### Durée de l’expérience 

#### Choisir une durée idéale {#reshuffle}

Le temps nécessaire pour mener votre expérience avant de pouvoir remanier les utilisateurs de votre groupe de contrôle dépend de ce que vous testez et des comportements de référence de vos utilisateurs. Si vous n’êtes pas sûr, vous pouvez commencer par une durée d’un trimestre (trois mois), mais pas moins d’un mois.

Pour déterminer la durée appropriée pour votre expérience, réfléchissez aux questions auxquelles vous espérez trouver une réponse. Par exemple, cherchez-vous à voir s’il y a une différence entre les sessions ? Si oui, pensez à la fréquence à laquelle vos utilisateurs ont naturellement des sessions. Les marques dont les utilisateurs ont des sessions chaque jour peuvent mener des expériences plus courtes que les marques dont les utilisateurs ont des sessions seulement deux fois par mois. 

Vous pouvez également vous intéresser à un événement personnalisé, et votre expérience devra alors durer plus longtemps qu'une expérience où vous examinez des sessions, s'il est probable que vos utilisateurs déclenchent cet événement personnalisé moins fréquemment.

{% alert tip %}
Plus vous maintenez le même groupe de contrôle en place, plus il divergera du groupe de traitement, ce qui peut compromettre l’impartialité des résultats. Le fait de réinitialiser le groupe de contrôle global rééquilibrera la population.
{% endalert %}

#### Évitez d’arrêter une expérience prématurément

Avant de commencer, décidez de la durée sur laquelle vous allez conduire votre expérience, puis laissez votre expérience se dérouler jusqu’à la fin de la durée choisie avant de recueillir les résultats finaux. Mettre fin à votre expérience trop tôt, ou lorsque vous voyez des données prometteuses, aura pour effet de compromettre les résultats.

#### Pensez à des mesures utiles

Pensez aux comportements de référence pour les mesures qui vous intéressent le plus. Êtes-vous intéressé(e) par les tarifs des abonnements qui sont renouvelés uniquement tous les ans ? Ou voulez-vous savoir si vos clients ont une habitude hebdomadaire pour l’événement que vous souhaitez mesurer ? Pensez au temps qu’il faut pour que les utilisateurs changent potentiellement leurs comportements suite à votre message. Une fois que vous avez décidé de la durée de votre expérience, veillez à ne pas la terminer ou à ne pas enregistrer les résultats finaux trop tôt, car vos conclusions risqueraient d'être faussées.

