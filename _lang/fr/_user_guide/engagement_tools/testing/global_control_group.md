---
nav_title: Groupe de contrôle global
article_title: Groupe de contrôle global
alias: /global_control_group/
page_order: 0

description: "Cet article explique comment configurer et utiliser correctement le groupe de contrôle global. Il explique également comment consulter les mesures et les rapports liés à l’utilisation de ces groupes."
page_type: reference
tool: Rapports
search_rank: 1

---

# Groupe de contrôle global

> Cet article explique comment configurer et utiliser correctement le groupe de contrôle global. Il explique également comment consulter les mesures et les rapports liés à l’utilisation de ces groupes.

Utilisez le groupe de contrôle global pour indiquer un pourcentage de tous les utilisateurs qui ne devraient pas recevoir de campagnes ou de Canvas, ce qui vous permet d’analyser l’impact global de vos efforts de communication au fil du temps. En comparant les comportements des utilisateurs qui reçoivent des messages à ceux qui n’en reçoivent pas, vous pouvez mieux comprendre comment vos Canvas et campagnes marketing entraînent une augmentation du nombre de sessions et d’événements personnalisés.

## Fonctionnement du groupe de contrôle global

Avec le groupe de contrôle global, vous pouvez définir un pourcentage de tous les utilisateurs comme groupe de contrôle. Une fois enregistrés, les utilisateurs du groupe ne recevront aucune campagne ni aucun Canvas. 

Votre groupe de contrôle global est appliqué à tous les canaux, campagnes et Canvas à l’exception des [campagnes API]({{site.baseurl}}/api/api_campaigns#api-campaigns) et des cartes de fil d’actualité (obsolète) Les utilisateurs de votre groupe de contrôle vont quand même recevoir les campagnes API et les cartes de fil d’actualité. Notez que cette exception ne s’applique pas aux cartes de contenu. Si vous utilisez des cartes de contenu, les utilisateurs de votre groupe de contrôle ne les recevront pas.

### Assigner des utilisateurs au groupe de contrôle global de manière aléatoire

Braze sélectionne de manière aléatoire plusieurs plages de [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) et inclut les utilisateurs faisant partie des compartiments sélectionnés.  i vous utilisez actuellement des numéros de compartiment aléatoires à d’autres fins, consultez l’article [Points à surveiller](#things-to-watch-for). 

### Suivi des données pour les rapports

Braze mesure les comportements des utilisateurs de votre groupe de contrôle et des utilisateurs de votre échantillon de traitement. Votre échantillon expérimental est une sélection aléatoire d’utilisateurs qui ne font pas partie de votre groupe de contrôle, et qui est générée en suivant la même méthode des numéros de compartiment aléatoires.

## Créer un groupe de contrôle global

### Étape 1 : Accédez à Global Control Group Settings (Paramètres du groupe de contrôle global).

Dans le tableau de bord, accédez à **Global Message Settings (Paramètres généraux des messages)** dans **Engagement**, et cliquez sur l’onglet **Global Control Group Settings (Paramètres du groupe de contrôle global)**.

### Étape 2 : Attribuez un pourcentage de tous les utilisateurs à ce groupe de contrôle

Saisissez un pourcentage pour votre groupe de contrôle et cliquez sur **Save (Enregistrer)**. Une fois le pourcentage saisi, Braze vous montrera une estimation du nombre d’utilisateurs qui seront ajoutés à votre groupe de contrôle global, votre groupe de traitement et votre échantillon de traitement. N’oubliez pas que plus il y a d’utilisateurs dans votre groupe d’apps, plus cette estimation sera précise. 

Le nombre d’utilisateurs de votre groupe de contrôle global est automatiquement mis à jour après sa configuration initiale afin de rester proportionnel au pourcentage de l’audience lorsque d’autres utilisateurs sont ajoutés à votre groupe d’apps. Par exemple, si le nombre d’utilisateurs de votre groupe d’apps augmente, le nombre d’utilisateurs de votre groupe de contrôle global augmentera également afin que votre groupe de contrôle reste un pourcentage constant de l’audience de votre groupe d’apps. Pour connaître les directives sur les pourcentages, reportez-vous à la section suivante sur les [meilleures pratiques](#percentage-guidelines).

![Les paramètres du groupe de contrôle global avec les paramètres d’audience définis sur « Assign five percent of all users to the Global Control Group (Attribuer cinq pour cent de tous les utilisateurs au groupe de contrôle global) ».][4]

### Étape 3 : Attribuer des paramètres d’exclusion

Vous pouvez utiliser des balises pour ajouter des paramètres d’exclusion à votre groupe de contrôle global. Les campagnes ou les Canvas qui utilisent les balises incluses dans les paramètres d’exclusion n’utiliseront pas votre groupe de contrôle global. Ces campagnes et Canvas continueront d’être envoyés à chaque utilisateur de l’audience cible, y compris ceux de votre groupe de contrôle global.

{% alert tip %}
Vous souhaiterez peut-être ajouter des paramètres d’exclusion si vous devez envoyer des messages transactionnels à chaque utilisateur.
{% endalert %}

![L’option permettant d’ajouter des paramètres d’exclusion à votre groupe de contrôle global.][5]

### Étape 4 : Enregistrer votre groupe de contrôle

À ce stade, Braze génère un groupe d’utilisateurs sélectionnés de manière aléatoire pour inclure le pourcentage sélectionné de l’ensemble de votre base d’utilisateurs. Une fois le groupe enregistré, l’ensemble des campagnes et Canvas actifs et futurs ne seront plus envoyés aux utilisateurs de ce groupe, à l’exception des campagnes ou des Canvas qui contiennent l’une des balises de vos paramètres d’exclusion.

## Désactiver votre groupe de contrôle global

Vous pouvez désactiver votre groupe de contrôle global à tout moment en accédant à l’onglet **Global Control Group Settings (Paramètres du groupe de contrôle global)**, mais gardez à l’esprit qu’en faisant cela tous les utilisateurs de ce groupe deviendront immédiatement éligibles aux campagnes et Canvas.

Avant de désactiver votre groupe de contrôle, nous vous recommandons d’[exporter](#export-group-members) un fichier au format CSV regroupant tous les utilisateurs de ce groupe au cas où vous auriez besoin de le consulter ultérieurement. Lorsqu’un groupe de contrôle a été désactivé, Braze ne pourra plus restaurer le groupe ou identifier les utilisateurs de ce groupe.

Vous pouvez enregistrer un nouveau groupe après avoir désactivé votre groupe de contrôle. Une fois que vous avez saisi et enregistré un pourcentage, Braze génère un groupe d’utilisateurs sélectionnés de manière aléatoire. Si vous saisissez le même pourcentage qu’auparavant, Braze génèrera toujours un nouveau groupe d’utilisateurs pour vos groupes de contrôle et de traitement.

![Une boîte de dialogue intitulée « You are making changes to Global Messaging Settings (Vous apportez des modifications aux paramètres de messagerie globale) » avec le texte suivant : « Une fois votre groupe de contrôle global désactivé, celui-ci ne sera plus exclu des campagnes et Canvas, nouveaux ou actifs. Les utilisateurs de ce groupe seront immédiatement éligibles pour recevoir des messages. Êtes-vous sûr de vouloir continuer ? » avec deux boutons : Cancel (Annuler) et Proceed (Continuer).][2]{: style="max-width:50%" }

## Exporter vos membres de groupe de contrôle {#export-group-members}

Si vous souhaitez voir quels utilisateurs sont inclus dans votre groupe de contrôle global, vous pouvez exporter les membres de votre groupe dans un fichier CSV ou via une API. 

Pour exporter un fichier CSV, accédez à l’onglet **Global Control Group Settings (Paramètres du groupe de contrôle global)** et cliquez sur <i class="fas fa-download"></i>&nbsp;**Export (Exporter)**. Pour exporter un groupe via une API, utilisez l’endpoint API [Users by Global Control Group (Utilisateurs par groupe de contrôle global)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Les groupes de contrôle historiques ne sont pas conservés, vous pouvez donc uniquement exporter les membres de votre groupe actuel. Assurez-vous d’exporter toutes les informations nécessaires avant de désactiver un groupe de contrôle.
{% endalert %}

## Rapports

Consultez [Rapports sur le groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) pour des informations sur les indicateurs relatifs aux rapports.


## Résolution des problèmes

Vous trouverez ci-dessous quelques erreurs que vous pourriez rencontrer au moment de configurer vos groupes de contrôle globaux et de consulter vos rapports :

| Problème | Résolution des problèmes |
| --- | --- |
| Impossible d’enregistrer le pourcentage saisi au moment de désigner un groupe de contrôle global. | Ce problème survient si vous entrez un nombre entier ou non entier qui n’est pas compris entre 1 et 15 inclus. |
| Erreur « Braze is not able to update your Global Control Group (Braze n’est pas en mesure de mettre à jour votre groupe de contrôle global) » sur la page Global Control settings (Paramètres de contrôle global). | Cela indique généralement que certains composants de cette page ont été modifiés, probablement par un autre utilisateur de votre compte Braze. Dans ce cas, actualisez la page et réessayez. |
| Le rapport du groupe de contrôle global ne contient aucune donnée. | Si vous consultez le rapport du groupe de contrôle global sans avoir enregistré de groupe de contrôle global, vous ne verrez aucune donnée dans le rapport. Créez et enregistrez un groupe de contrôle global, puis réessayez. |
| Mon taux de conversion est de 0 % ou le graphique ne s’affiche pas, même s’il y a plus de zéro événement. | Si le nombre de conversions est très faible et que vos groupes de contrôle ou de traitement sont très importants, il se peut que le taux de conversion soit arrondi à 0 % et qu’il ne soit pas pris en compte dans le graphique. Vous pouvez vérifier cela en cochant la mesure Total Number of Events (Nombre total d’événements). Vous pouvez comparer l’efficacité de vos deux groupes à l’aide de la mesure du pourcentage d’augmentation progressive.  |
| Mon taux de conversion (ou d’autres mesures) change considérablement en fonction de la période pendant laquelle je consulte les données. | Si vous visualisez des données sur de courtes périodes, il se peut que vos mesures fluctuent de jour en jour ou de semaine en semaine. Nous vous recommandons d’afficher les métriques sur une période d’au moins un mois. |
{: .reset-td-br-1 .reset-td-br-2}

### Choses à garder à l’esprit {#things-to-watch-for}

#### Chevauchement des numéros de compartiment aléatoires

Votre groupe de contrôle global est créé à l’aide de numéros de compartiment aléatoires. Si vous exécutez d’autres tests à l’aide des filtres de segments de numéros de compartiment aléatoires, gardez donc à l’esprit qu’il pourrait y avoir un chevauchement entre les segments que vous créez et les utilisateurs de votre groupe de contrôle global.

#### Adresses e-mail en double

Si deux utilisateurs ayant des ID d’utilisateur externe différents ont la même adresse e-mail, et que l’un des deux utilisateurs se trouve dans le groupe de contrôle, un e-mail sera toujours envoyé à cette adresse e-mail chaque fois que l’utilisateur du groupe non contrôlé est éligible à recevoir un e-mail. Lorsque cela se produit, nous désignerons les deux profils utilisateur comme ayant reçu la campagne ou le Canvas contenant cet e-mail.

#### Groupe de contrôle global et groupes de contrôle spécifiques aux communications

Vous pouvez avoir un groupe de contrôle global tout en utilisant un groupe de contrôle spécifique aux campagnes ou aux Canvas. Avoir un groupe de contrôle spécifique pour vos campagnes ou Canvas vous permet de mesurer l’impact d’un message donné.

Les utilisateurs de votre groupe de contrôle global recevront uniquement des messages qui comportent des exceptions de balise, et si vous ajoutez un groupe de contrôle à une campagne ou à un Canvas, Braze bloquera l’envoi de cette campagne ou de ce Canvas pour une partie de votre groupe de traitement global. Cela signifie que si un membre du groupe de contrôle global n’est pas éligible pour recevoir une campagne ou un Canvas donné, ils ne seront pas non plus présents dans le groupe de contrôle correspondant à cette campagne ou ce Canvas.

> En bref, les utilisateurs du groupe de contrôle global sont exclus de l’audience de la campagne ou du Canvas. Un pourcentage des utilisateurs inclus dans la campagne ou le Canvas est ensuite affecté à la variante de contrôle.

#### Segments du groupe de contrôle global sur la Developer Console

Il se peut que plusieurs segments **Global Control** apparaissent dans la section **Additional API Identifiers (Identifiants API supplémentaires)** de la **Developer Console**. En effet, un nouveau groupe de contrôle global est créé chaque fois que le groupe de contrôle global est activé ou désactivé. Cela conduit donc à la création de plusieurs segments portant la mention « Global Control Group (Groupe de contrôle global) ».

Un seul de ces segments est actif et peut être interrogé à l’aide de l’endpoint API [Users by Global Control Group (Utilisateurs par groupe de contrôle global)]({{site.baseurl}}api/endpoints/export/user_data/post_users_global_control_group/), ou exporté depuis le tableau de bord. L’exportation depuis le tableau de bord indique spécifiquement quels sous-segments composent ce groupe de contrôle global.

## Mettre les meilleures pratiques à l’épreuve

### Taille optimale du groupe de contrôle {#percentage-guidelines}

Il y a deux règles principales à garder à l’esprit** :
1. Votre groupe de contrôle ne doit pas comporter moins de 1 000 utilisateurs.
2. Votre groupe de contrôle ne doit pas dépasser 10 % de l’ensemble de votre audience.

Si vous avez une audience totale inférieure à 10 000 utilisateurs, vous devez augmenter votre pourcentage pour créer un groupe de plus de 1 000 utilisateurs ; dans ce cas, vous ne devez pas augmenter votre pourcentage au-delà du seuil des 15 %. N’oubliez pas que plus votre groupe d’apps est petit, plus il vous sera difficile de conduire un test rigoureux sur le plan statistique.

- Notez qu’il existe certains compromis à prendre en compte lorsque vous réfléchissez à la taille de votre groupe de contrôle. Par exemple, votre groupe de contrôle doit comporter un grand nombre de clients afin de garantir la fiabilité de vos analyses comportementales. Cependant, plus votre groupe de contrôle est important, plus le nombre de clients qui reçoivent vos campagnes sera réduit, ce qui est un inconvénient si vous utilisez vos campagnes pour stimuler l’engagement et augmenter les conversions.
- Le pourcentage idéal de votre audience globale dépendra donc de la taille de votre audience globale. Plus votre audience globale est importante, plus votre pourcentage sera réduit. Cependant, si votre audience est de petite taille, vous aurez besoin d’un pourcentage plus important pour votre groupe de contrôle.

### Durée de l’expérience 

#### Choisir une durée idéale {#reshuffle}

Le temps nécessaire pour mener votre expérience avant de pouvoir remanier les utilisateurs de votre groupe de contrôle dépend de ce que vous testez et des comportements de référence de vos utilisateurs. Si vous n’êtes pas sûr, vous pouvez commencer par une durée d’un trimestre (trois mois), mais pas moins d’un mois.

Pour déterminer la durée appropriée pour votre expérience, réfléchissez aux questions auxquelles vous espérez trouver une réponse. Par exemple, cherchez-vous à voir s’il y a une différence entre les sessions ? Si oui, pensez à la fréquence à laquelle vos utilisateurs ont naturellement des sessions. Les marques dont les utilisateurs ont des sessions chaque jour peuvent mener des expériences plus courtes que les marques dont les utilisateurs ont des sessions seulement deux fois par mois. 

Ou, vous pourriez être intéressé par les comportements d’achat de vos utilisateurs, ce qui signifie que votre expérience devrait probablement se dérouler plus longtemps qu’une expérience dont le but est d’examiner les sessions uniquement, car il est probable que vos utilisateurs effectuent moins fréquemment des achats.

{% alert tip %}
Plus vous maintenez le même groupe de contrôle en place, plus il divergera du groupe de traitement, ce qui peut compromettre l’impartialité des résultats. Le fait de réinitialiser le groupe de contrôle global rééquilibrera la population.
{% endalert %}

#### Évitez d’arrêter une expérience prématurément

Avant de commencer, décidez de la durée sur laquelle vous allez conduire votre expérience, puis laissez votre expérience se dérouler jusqu’à la fin de la durée choisie avant de recueillir les résultats finaux. Mettre fin à votre expérience trop tôt, ou lorsque vous voyez des données prometteuses, aura pour effet de compromettre les résultats.

#### Pensez à des mesures utiles

Pensez aux comportements de référence pour les mesures qui vous intéressent le plus. Êtes-vous intéressé(e) par les tarifs des abonnements qui sont renouvelés uniquement tous les ans ? Ou voulez-vous savoir si vos clients ont une habitude hebdomadaire pour l’événement que vous souhaitez mesurer ? Pensez au temps qu’il faut pour que les utilisateurs changent potentiellement leurs comportements suite à votre message. Après avoir choisi la durée de votre expérience, assurez-vous de ne pas mettre fin à votre expérience ou d’enregistrer trop tôt les résultats finaux, faute de quoi vos résultats pourraient être biaisés.

[2]: {% image_buster /assets/img/control_group/control_group2.png %}
[4]: {% image_buster /assets/img/control_group/control_group4.png %}
[5]: {% image_buster /assets/img/control_group/control_group5.png %}
[6]: {% image_buster /assets/img/control_group/control_group6.png %}
