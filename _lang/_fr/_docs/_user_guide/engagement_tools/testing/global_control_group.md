---
nav_title: Groupe de contrôle global
article_title: Groupe de contrôle global
alias: /fr/global_control_group/
page_order: 0
description: "Cet article traite de la manière de mettre en place et d'utiliser correctement le Groupe Global Control. Il couvre également la façon de voir les rapports et les paramètres fournis par l'utilisation de ces groupes."
page_type: Référence
tool: Rapports
---

# Groupe de contrôle global

> Cet article traite de la manière de mettre en place et d'utiliser correctement le Groupe Global Control. Il couvre également la façon de voir les rapports et les paramètres fournis par l'utilisation de ces groupes.

Utilisez le Groupe de Contrôle Global pour spécifier un pourcentage de tous les utilisateurs qui ne devraient recevoir aucune campagne ou Canvases, vous permettant d'analyser l'impact global de vos efforts de messagerie au fil du temps. En comparant les comportements des utilisateurs qui reçoivent des messages à ceux qui ne le font pas, vous pouvez mieux comprendre comment vos campagnes de marketing et Canvases se traduisent par une augmentation des sessions et des événements personnalisés.

## Comment fonctionne le Groupe de Contrôle Mondial

Avec le Global Control Group, vous pouvez définir un pourcentage de tous les utilisateurs comme un groupe de contrôle. Une fois enregistrés, les utilisateurs du groupe ne recevront aucune campagne ou Canvases.

Votre groupe de contrôle global est appliqué à tous les canaux, campagnes et canvases, à l’exception des Fil d’actualités – les utilisateurs de votre groupe de contrôle recevront toujours les Fil d’Actualité. Cette exception ne s'applique pas aux cartes de contenu — si vous utilisez des cartes de contenu, les utilisateurs de votre groupe de contrôle ne les recevront pas.

__Assigner des utilisateurs aléatoirement au groupe de contrôle global :__<br> Braze sélectionne aléatoirement plusieurs plages de [nombres de seaux aléatoires]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) et inclut les utilisateurs de ces compartiments sélectionnés. Si vous utilisez actuellement des nombres aléatoires à d'autres fins, veuillez lire la section [choses à faire attention à](#things-to-watch-for) ci-dessous. <br><br> __Suivi des données pour signaler :__<br>Braze mesure les comportements des utilisateurs de votre groupe de contrôle et des utilisateurs dans votre échantillon de traitement. Votre échantillon de traitement est une sélection aléatoire d'utilisateurs qui ne font pas partie de votre groupe de contrôle, générée en utilisant la même méthode Random Bucket Number mentionnée ci-dessus.

## Créer un groupe de contrôle global

### Étape 1 : Accédez aux paramètres du groupe de contrôle global.

À partir du tableau de bord, allez dans **Paramètres globaux des messages** sous **Engagement**, et sélectionnez l'onglet **Paramètres des groupes de contrôle globaux**.

### Étape 2 : Assigner un pourcentage de tous les utilisateurs à ce groupe de contrôle

Entrez un pourcentage pour votre groupe de contrôle et cliquez sur __Enregistrer__. Une fois saisi, Braze vous montre une estimation du nombre d'utilisateurs qui vont tomber dans votre échantillon de contrôle global, de traitement et de traitement. Gardez à l'esprit que plus vous avez d'utilisateurs dans votre groupe d'applications, plus cette estimation sera précise.

Le nombre d'utilisateurs dans votre groupe de contrôle global est automatiquement mis à jour après sa configuration initiale pour rester proportionné à ce pourcentage d'audience lorsque plus d'utilisateurs sont ajoutés à votre groupe d'applications. Pour des lignes directrices en pourcentage, reportez-vous à la section [des meilleures pratiques](#percentage-guidelines) ci-dessous.

!\[Groupe de contrôle global\]\[4\]

### Étape 3 : Assigner les paramètres d'exclusion

Utilisez des balises pour ajouter des paramètres d'exclusion à votre groupe de contrôle global. Les campagnes ou Canvases qui utilisent les balises incluses dans les paramètres d'exclusion n'utilisent pas votre Groupe de Contrôle Global. Ces campagnes et Canvases continuent à être envoyées à tous les utilisateurs du public cible, y compris ceux de votre groupe de contrôle global.

{% alert tip %}
Vous pouvez ajouter des paramètres d'exclusion si vous avez des messages transactionnels qui doivent être envoyés à chaque utilisateur.
{% endalert %}

!\[Groupe de contrôle global\]\[5\]

### Étape 4 : Enregistrez votre groupe de contrôle

À ce stade, Braze génère un groupe d’utilisateurs sélectionné au hasard pour représenter le pourcentage sélectionné de votre base d’utilisateurs. Une fois enregistrés, toutes les campagnes actuelles et futures et les Canvases ne sont plus envoyées aux utilisateurs de ce groupe, à l'exception des campagnes ou des Canvases qui contiennent l'une des balises dans vos paramètres d'exclusion.

## Désactiver votre groupe de contrôle global

Vous pouvez désactiver votre groupe de contrôle global à tout moment à partir de l’onglet **Paramètres du groupe de contrôle global** , mais gardez à l'esprit que cela entraînera que les utilisateurs de ce groupe seront immédiatement éligibles pour les campagnes et les Canvases.

__Avant de désactiver votre Groupe de Contrôle__ nous vous recommandons [d'exporter](#export-group-members) un CSV d'utilisateurs dans ce groupe au cas où vous auriez besoin de le référencer à un point ultérieur. Une fois que vous désactivez un groupe de contrôle, il n'y a aucun moyen pour Braze de restaurer le groupe ou d'identifier quels utilisateurs étaient dans ce groupe.

__Après avoir désactivé votre Groupe de Contrôle__ vous pouvez en enregistrer un nouveau. Une fois que vous entrez un pourcentage et sauvegardez-le, Braze génère un nouveau groupe d'utilisateurs aléatoirement sélectionnés. Si vous entrez le même pourcentage qu'avant, Braze génère toujours un nouveau groupe d'utilisateurs pour vos groupes de contrôle et de traitement.

!\[Global Control Group\]\[2\]{: style="max-width:50%" }

## Exporter les membres de votre groupe de contrôle {#export-group-members}

Si vous souhaitez voir quels sont les utilisateurs de votre groupe de contrôle global, vous pouvez exporter les membres de votre groupe via CSV ou API.

Pour exécuter une exportation CSV, accédez à l'onglet **Paramètres du groupe de contrôle global** et cliquez sur <i class="fas fa-download"></i>&nbsp;**Exporter**. Pour exporter via API, utilisez le point de terminaison de l'API [Utilisateurs par Groupe de Contrôle Global]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Les groupes de contrôle historique ne sont pas préservés, vous ne pouvez donc exporter que les membres de votre groupe actuel. Assurez-vous d'exporter toutes les informations nécessaires avant de désactiver un groupe de contrôle.
{% endalert %}

## Voir le rapport

Pour afficher un rapport pour votre groupe de contrôle global à partir du tableau de bord, accédez à __Groupe de contrôle global__ sous __Données__. Ensuite, sélectionnez le paramètre avec lequel vous souhaitez exécuter votre rapport (sessions ou événements personnalisés particuliers) et cliquez sur __Exécuter le rapport__.

!\[Groupe de contrôle global\]\[6\]

### À propos de votre rapport

Le rapport Global Control Group vous permet de comparer votre groupe à un échantillon de traitement. Votre échantillon de traitement est une sélection aléatoire d'utilisateurs non contrôlés, environ le même nombre d'utilisateurs que votre contrôle, généré en utilisant la méthode Random Bucket Num.

Lors de la génération de votre rapport, choisissez un événement, soit une session, soit un événement personnalisé, pour comparer vos groupes de traitement et de contrôle. Choisissez ensuite une période de temps pour laquelle afficher les données. Gardez à l'esprit que si vous avez sauvegardé plusieurs expériences de groupe de contrôle à différentes périodes de temps, vous devriez éviter d'inclure des données provenant de plus d'une expérience dans votre rapport.

Enfin, comme pour plusieurs autres rapports sur notre plate-forme, ce rapport affiche un pourcentage de [confiance]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#understanding-confidence) pour votre changement de métrique de contrôle. Notez que dans les cas où le taux de conversion entre votre contrôle et le traitement est identique, une confiance de 0 % est à prévoir ; cela indique qu'il y a 0 % de chances qu'il y ait une différence de performance entre les deux groupes.

### Signaler les métriques

| Métrique                             | Définition                                                                                                                                                                                                                                                                          | Calcul                                                                                                                                                |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Changer depuis le contrôle           | Cela calcule la hausse entre le taux de conversion de vos groupes de traitement et de contrôle.                                                                                                                                                                                     | (Taux de conversion de traitement – contrôle du taux de conversion) (taux de conversion de contrôle) * 100                                            |
| Incrémentiel                         | La différence dans les événements totaux entre votre traitement et les groupes de contrôle. Cette métrique cherche à répondre à la question de « Combien d’autres événements de conversion ont-ils été réalisés par le groupe de traitement ? ».                                    | Total des événements pour le traitement - total des événements pour le contrôle                                                                       |
| Pourcentage d'élévation incrémentale | Le pourcentage des événements totaux de votre traitement qui peuvent être attribués à votre traitement (contre le comportement naturel de l'utilisateur). Ceci est calculé en divisant la hausse incrémentale (nombre) par le nombre total d’événements pour votre groupe de soins. | Augmentation incrémentale (nombre) ÷ Événements totaux pour le groupe de traitement                                                                   |
| Taux de conversion                   | En moyenne, le pourcentage d'utilisateurs de votre groupe de contrôle/traitement qui terminent l'événement sélectionné chaque jour au cours de la période choisie.                                                                                                                  | Moyenne (moyenne) du pourcentage d'utilisateurs qui effectuent votre événement sélectionné chaque jour au cours de la période choisie.                |
| Taille estimée du groupe             | Le nombre estimé d'utilisateurs dans vos groupes de contrôle et de traitement au cours de la période sélectionnée.                                                                                                                                                                  | La taille maximale de votre adhésion à vos groupes de contrôle et de traitement atteint au cours de la période que vous avez choisie pour le rapport. |
| Nombre total d'événements            | Le nombre total de fois où l'événement sélectionné s'est produit au cours de la période choisie. Ce n'est pas unique (c'est à dire si un utilisateur effectue un événement deux fois pendant la période de temps, l'événement est incrémenté deux fois).                            | La somme du nombre de fois de l'événement a eu lieu chaque jour pendant la période choisie.                                                           |
| Événements par utilisateur           | Le nombre moyen estimé de fois que les utilisateurs de chaque groupe ont terminé vos événements de conversion pendant la période sélectionnée.                                                                                                                                      | Total des événements (taille estimée au nombre de groupes).                                                                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Dépannage

Au fur et à mesure que vous configurez vos groupes de contrôle globaux et que vous affichez les rapports, voici les erreurs dans lesquelles vous pouvez exécuter :

| Problème                                                                                                                             | Dépannage                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Impossible d'enregistrer le pourcentage saisi lors de la désignation d'un groupe de contrôle global.                                 | Ce problème se produit si vous entrez un entier non entier ou un entier qui n'est pas compris entre 1 et 15 (inclus).                                                                                                     |
| L'erreur "Braze n'est pas en mesure de mettre à jour votre groupe de contrôle global" sur la page des paramètres de contrôle global. | Ceci indique généralement que certains composants de cette page ont changé, probablement en raison des actions prises par un autre utilisateur sur votre compte Braze. Dans ce cas, rafraîchissez la page et réessayez.   |
| Le rapport Global Control Group ne contient aucune donnée.                                                                           | Si vous accédez au rapport de groupe de contrôle global sans avoir enregistré un groupe de contrôle global, vous ne verrez aucune donnée dans le rapport. Créez et enregistrez un groupe de contrôle global et réessayez. |
{: .reset-td-br-1 .reset-td-br-2}

### Les choses à surveiller {#things-to-watch-for}

#### Recouvrement des nombres de Seau Aléatoire

Votre groupe de contrôle global est formé à l'aide de numéros de Bucket aléatoires, et donc si vous exécutez d'autres tests en utilisant des filtres de segments de Bucket Numbers aléatoires, Gardez à l'esprit qu'il pourrait y avoir un chevauchement entre ces segments que vous créez, et les utilisateurs de votre Groupe de Contrôle Global.

#### Dupliquer les adresses e-mail

Si deux utilisateurs ayant des identifiants d'utilisateurs externes différents ont la même adresse e-mail, et l'un de ces utilisateurs est dans le groupe de contrôle et l'autre ne l'est pas, alors un courriel sera toujours envoyé à cette adresse dès que l'utilisateur du groupe non contrôlé aura droit à un courriel. Lorsque cela se produit, nous marquerons les deux profils d'utilisateurs comme ayant reçu la campagne ou Canvas contenant ce courriel.

#### Groupe de contrôle global et groupes de contrôle spécifiques aux messages

Il est possible d'avoir à la fois un groupe de contrôle global et un groupe de contrôle spécifique à une campagne ou à un groupe de contrôle spécifique à Canvas. Avoir un groupe de contrôle spécifique à une campagne ou spécifique à Canvas vous permet de mesurer l’impact d’un message particulier.

Les utilisateurs de votre groupe de contrôle global ne peuvent pas recevoir de messages autres que ceux ayant des exceptions de tags, et si vous ajoutez un contrôle à une campagne ou à Canvas, Braze empêche une partie de votre groupe de traitement mondial de recevoir cette campagne ou Canva en particulier. Cela signifie que si un membre du Groupe de Contrôle Mondial n'est pas éligible pour recevoir une campagne particulière ou Canvas, ils ne seront pas non plus présents dans le groupe de contrôle pour cette campagne particulière ou Canvas.

> En bref, les utilisateurs du Groupe de contrôle mondial sont filtrés hors de la campagne ou du public de Canvas avant l'inscription. Parmi les utilisateurs qui entrent dans la campagne ou Canvas, un pourcentage de ces derniers sont ensuite affectés à la variante de contrôle.

#### Segments du groupe de contrôle global dans la console de développement

Vous pouvez voir plusieurs segments **Contrôle global** dans la section **Identifiants d'API supplémentaires** de la **console développeur**. Ceci est dû au fait que chaque fois que le Groupe de contrôle global est activé ou désactivé, un nouveau Groupe de contrôle global est formé. Ceci mène à plusieurs segments marqués "Groupe de contrôle global".

Un seul de ces segments est actif et peut être interrogé en utilisant le point de terminaison de l'API [Utilisateurs par Groupe de Contrôle Global,]({{site.baseurl}}api/endpoints/export/user_data/post_users_global_control_group/) ou exporté depuis le tableau de bord. L'exportation depuis le tableau de bord indique spécifiquement quels sous-segments composent ce Groupe de Contrôle Global.

## Tester les meilleures pratiques

### Contrôle optimal de la taille du groupe {#percentage-guidelines}

<br>__Deux règles principales à garder à l'esprit sont__:<br>- Votre groupe de contrôle ne devrait pas être inférieur à 1000 utilisateurs.<br>- Votre groupe de contrôle ne doit pas dépasser 10 % de l'ensemble de votre audience.

Si vous avez un public total inférieur à 10 000 personnes, vous devriez augmenter votre pourcentage pour créer un groupe de plus de 1000 utilisateurs ; dans ce cas, vous ne devriez pas augmenter votre pourcentage de plus de 15%. Gardez à l'esprit que la taille globale de votre groupe d'applications est plus petite, plus il sera difficile de faire un test statistiquement rigoureux.
- Certains compromis à considérer lorsque vous pensez à la taille de votre groupe de contrôle sont que vous avez besoin d'un nombre important de clients dans votre groupe de contrôle afin que toute analyse de comportement créée soit digne de confiance. Cependant, plus votre groupe de contrôle est grand, moins de clients reçoivent de vos campagnes, qui est un inconvénient si vous utilisez vos campagnes pour stimuler l'engagement et les conversions.
- Le pourcentage idéal de votre auditoire total dépendra de la taille de votre auditoire. Plus votre audience est grande, plus votre pourcentage peut être petit. Toutefois, si vous avez un petit public, vous aurez besoin d'un pourcentage plus important pour votre groupe de contrôle.

### Durée de l'expérience

#### Choisissez une durée idéale {#reshuffle}

La durée de votre expérience avant de remanier la composition du groupe de contrôle dépend de ce que vous testez et des comportements de base de vos utilisateurs. Si vous n'êtes pas sûr, un bon endroit pour commencer est un quart (3 mois), et vous ne devriez pas aller plus court que 1 mois.

Pour déterminer la durée appropriée de votre expérience, examinez les questions auxquelles vous comptez répondre. Par exemple, êtes-vous à la recherche de voir s’il y a une différence dans les sessions ? Si c'est le cas, pensez à la fréquence à laquelle vos utilisateurs ont des sessions organiques. Les marques dont les utilisateurs ont des sessions chaque jour peuvent faire des expériences plus courtes que les marques dont les utilisateurs n'ont des sessions que deux fois par mois.

Ou peut-être que vous êtes intéressé par des comportements d’achat. Alors votre expérience devrait probablement être exécutée plus longtemps qu'une expérience où vous examinez des sessions, car il est probable que vos utilisateurs fassent des achats moins fréquemment.

{% alert tip %}
Plus vous détenez le même groupe de contrôle, plus ils se différencient du groupe de traitement, ce qui peut créer des partis. La réinitialisation du Groupe de contrôle mondial rééquilibre la population.
{% endalert %}

#### Essayez de limiter prématurément les expériences de fin de vie

Vous devez décider de la durée de votre expérience avant de la lancer, puis vous ne devriez terminer votre expérience et récolter les résultats finaux qu'une fois que vous avez atteint ce point prédéterminé. Mettre fin à votre expérience tôt ou chaque fois que vous voyez des données prometteuses, introduira un parti pris.

#### Pensez à des indicateurs de valeur

Considérez tout comportement de base pour les paramètres qui vous intéressent le plus. Êtes-vous intéressé par les tarifs d’achat pour les abonnements renouvelés uniquement sur une base annuelle? Ou les clients ont-ils une habitude hebdomadaire pour l’événement que vous souhaitez mesurer ? Pensez au temps qu'il faut aux utilisateurs pour modifier leurs comportements en raison de votre messagerie. Une fois que vous décidez combien de temps votre expérience doit courir, Assurez-vous de ne pas mettre fin à votre expérience ou de ne pas enregistrer les résultats finaux tôt ou vos conclusions peuvent être partiales.
[2]: {% image_buster /assets/img/control_group/control_group2.png %} [4]: {% image_buster /assets/img/control_group/control_group4. ng %} [5]: {% image_buster /assets/img/control_group/control_group5.png %} [6]: {% image_buster /assets/img/control_group/control_group6.png %}
