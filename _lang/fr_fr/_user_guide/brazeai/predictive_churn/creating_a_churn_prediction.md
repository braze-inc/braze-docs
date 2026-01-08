---
nav_title: "Créer une prédiction du taux d'attrition"
article_title: "Créer une prédiction du taux d'attrition"
description: "Cet article explique comment créer une prédiction du taux de désabonnement dans le tableau de bord de Braze."
page_order: 1.1

---

# Créer une prédiction du taux d'attrition

> Découvrez comment créer une prédiction du taux de désabonnement dans le tableau de bord de Braze.

## Étape 1 : Créer une nouvelle prédiction

Dans Braze, allez dans **Analyses/analytiques** > Seabonner prédictivement (si vous utilisez une **analyse** prédictive du taux d'attrition).

Une prédiction est une instance d'un modèle d'apprentissage automatique formé et de tous les paramètres et données qu'il utilise. Sur cette page, vous trouverez une liste des prédictions actives actuelles ainsi que quelques informations de base à leur sujet. Vous pouvez y renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores des utilisateurs. 

Pour créer une nouvelle prédiction, choisissez **Créer une prédiction** et sélectionnez une nouvelle **prédiction du taux d'attrition**.

{% alert note %}
Le nombre de prédictions du taux d'attrition actives simultanément est limité à cinq. Avant l'achat de Prediction du taux d'attrition, la limite est d'une prédiction active du taux d'attrition. Une prédiction du taux d'attrition ne met pas régulièrement à jour les scores et ne vous permet pas de cibler les utilisateurs sur la base des résultats de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

Sur la page de **base**, donnez un nom unique à votre nouvelle prédiction. Vous pouvez également fournir une description facultative pour prendre des notes sur cette prédiction particulière.

Sélectionnez **Avancer** pour passer à l'étape suivante. En option, vous pouvez sélectionner **Créer maintenant** pour utiliser tous les paramètres par défaut et passer à la dernière étape de la création. Vous aurez la possibilité de revoir les paramètres avant de lancer le processus de création. Vous pouvez revenir à n'importe quelle étape ultérieurement en la sélectionnant dans le suivi de la progression.

## Étape 2 : Définir le désabonnement

Dans le panneau **Définition du désabonnement**, utilisez les filtres fournis pour spécifier la manière dont vous définissez le désabonnement des utilisateurs pour votre entreprise. En d'autres termes, que doit faire un utilisateur dans quel laps de temps pour que vous le considériez comme désabonné ?

Rappelez-vous que vous n'avez pas besoin d'expliquer les comportements qui peuvent précéder le désabonnement, mais seulement ce qui fait qu'un utilisateur est désabonné. Pensez-y en termes de quelque chose qu'un utilisateur fait une fois (`do`) ou arrête de faire (`do not`) et qui constitue un désabonnement. Par exemple, vous pouvez considérer que les utilisateurs qui n'ont pas ouvert votre application depuis 7 jours sont désabonnés. Vous pouvez envisager la désinstallation ou des événements personnalisés tels que le désabonnement, la désactivation d'un compte, ou d'autres pour faire en sorte qu'un utilisateur devienne désabonné. 

#### Fenêtre de désabonnement

La fenêtre de désabonnement est la période pendant laquelle l'activité d'un utilisateur répond aux critères de désabonnement. Vous pouvez la définir pour une durée allant jusqu'à 60 jours, en fonction des données disponibles. Cette fenêtre est utilisée pour extraire des données historiques afin d'entraîner vos prédictions. Une fois la prédiction créée, vous verrez s'il y avait suffisamment de données pour obtenir des résultats précis.

Une fois que la prédiction s'est créée et que les utilisateurs ont reçu des scores, le _score de risque de_ désabonnement indique la probabilité qu'un utilisateur désabonne dans le délai que vous avez défini dans la fenêtre de désabonnement. 

Voici un exemple de définition simple basée sur les sessions de péremption des 7 derniers jours.

Définition du désabonnement : un utilisateur est considéré comme désabonné s'il ne démarre pas de session dans les 7 jours.]({% image_buster /assets/img/churn/churn1.png %})

Dans ce cas, nous sélectionnons `do not` et `start a session`. Vous pouvez combiner d'autres filtres avec `AND` et `OR` comme bon vous semble pour créer la définition dont vous avez besoin. Vous souhaitez connaître quelques définitions potentielles du désabonnement à prendre en compte ? Vous pouvez trouver une certaine inspiration dans la section suivante sur les [définitions d'échantillons de désabonnement](#sample-definitions).

{% alert note %}
Pour `do`, nous supposons que les utilisateurs actifs n'ont pas entrepris l'action que vous indiquez pour cette ligne avant d'être désabonnés. L'action les amène à se désabonner. <br><br>Pour `do not`, nous considérons que les utilisateurs actifs sont ceux qui ont effectué cette action dans les jours précédents, puis se sont arrêtés. <br><br>**Exemple :** Si le désabonnement est défini comme "n'a pas acheté au cours des 60 derniers jours", nous considérons que les utilisateurs actifs sont ceux qui ont acheté au cours des 60 derniers jours. Par conséquent, toute personne qui n'a pas effectué d'achat au cours des 60 derniers jours n'est pas considérée comme un utilisateur actif. Cela signifie qu'une audience désabonnée créée à partir de cette définition du désabonnement ne comprendrait que les utilisateurs qui ont acheté au cours des 60 derniers jours. L'audience prédictive du taux d'attrition obtenue peut alors sembler nettement inférieure à la population d'origine. En effet, la plupart des utilisateurs d'un espace de travail peuvent déjà correspondre à la définition du taux désabonné et ne pas être pris en compte dans la prédiction du taux d'attrition.
{% endalert %}

Sous la définition, vous verrez des estimations du nombre d'utilisateurs désabonnés et non désabonnés selon votre définition. Vous verrez également les valeurs minimales requises. Braze doit disposer de ce nombre minimum d'utilisateurs dans les données historiques afin que la prédiction dispose de suffisamment de données pour apprendre.

## Étape 3 : Filtrez votre audience de prédictions

Votre audience de prédiction est le groupe d'utilisateurs pour lesquels vous souhaitez prédire le risque de désabonnement. L'audience de prédiction définit le groupe d'utilisateurs que le modèle de machine learning examine pour tirer des enseignements du passé. Par défaut, ce paramètre est défini sur **Tous les utilisateurs**, ce qui signifie que cette prédiction créera des scores de risque de désabonnement pour tous vos utilisateurs actifs (reportez-vous à la note précédente pour savoir qui est considéré comme actif pour un modèle de désabonnement).

En fonction de votre cas d'utilisation, vous pouvez utiliser des filtres pour spécifier les utilisateurs que vous souhaitez évaluer pour le modèle. Pour ce faire, sélectionnez **Définir ma propre audience de prédictions** et choisissez vos filtres d'audience. Par exemple, si vous êtes une application de covoiturage avec des conducteurs et des usagers dans votre base d'utilisateurs, et que vous créez un modèle de désabonnement pour les usagers, vous voudrez filtrer votre audience de prédiction aux seuls usagers. Gardez à l'esprit que de nombreux cas d'utilisation ne nécessitent pas que vous sélectionniez une audience de prédictions spécifique. Par exemple, si votre cas d'utilisation consiste à cibler les utilisateurs de la région UE qui sont les plus susceptibles de se désabonner, vous pouvez exécuter votre modèle sur tous les utilisateurs, puis simplement inclure un filtre pour la région UE dans le segment de la campagne.

Braze vous indiquera la taille estimée de votre audience de prédictions. Si vous spécifiez l'audience souhaitée et que vous n'atteignez pas le minimum requis pour exécuter le modèle, essayez de spécifier un filtre plus large ou utilisez l'option **Tous les utilisateurs.**  Notez que la taille de votre groupe "tous les utilisateurs" n'est pas statique et varie d'un modèle à l'autre, car elle tient compte de votre définition du désabonnement. Dans ce cas, Braze exécute le modèle sur les utilisateurs qui **ont** acheté au cours des 30 derniers jours (et prédit la probabilité qu'ils **n'** achètent **pas** au cours des 30 prochains jours), et ce sont donc ces utilisateurs qui sont pris en compte dans l'indicateur "tous les utilisateurs".

{% alert note %}
L'audience des prédictions ne peut dépasser 100 millions d'utilisateurs.
{% endalert %}

Lorsque la fenêtre de prédiction est de 14 jours ou moins, la fenêtre temporelle pour les filtres qui commencent par "Dernier..." comme "Dernière utilisation d'une application" et "Dernier achat effectué" **ne peut pas dépasser la fenêtre de désabonnement spécifiée** dans la définition du taux d'attrition. Par exemple, si votre définition du désabonnement a une fenêtre de 14 jours, la fenêtre temporelle pour les filtres "Dernier..." ne peut pas dépasser 14 jours.

#### Mode filtrage complet

Afin de créer immédiatement une nouvelle prédiction, seul un sous-ensemble de filtres de segmentation de Braze est pris en charge. Le mode filtrage complet vous permet d'utiliser tous les filtres de Braze, mais il vous faudra une fenêtre de désabonnement pour créer la prédiction. Par exemple, si la fenêtre de désabonnement est définie sur 15 jours, il faudra 15 jours pour collecter les données de l'utilisateur et créer la prédiction lors de l'utilisation de filtres uniquement pris en charge en mode filtrage complet. En outre, certaines estimations concernant la taille des audiences ne seront pas disponibles en mode filtrage complet.

Pour obtenir une liste d'exemples de définitions de prédiction du [taux d'attrition](#sample-definitions), consultez nos exemples de définitions dans la section suivante sur [les exemples de définitions du taux d'attrition](#sample-definitions).

\![]({% image_buster /assets/img/churn/churn5.png %})

Comme sur la page précédente, le panneau inférieur vous indique le nombre estimé d'utilisateurs désabonnés résultant de votre définition du désabonnement et de la définition de l'audience de prédiction. Ces estimations doivent répondre aux exigences minimales indiquées afin de créer une prédiction.

## Étape 4 : Choisissez la fréquence de mise à jour de la prédiction du taux d'attrition.

Le modèle d'apprentissage automatique générera des scores de probabilité d'événement pour les utilisateurs, et ces scores seront mis à jour en fonction de la planification que vous sélectionnez ici. Vous pourrez cibler les utilisateurs en fonction de leur score de probabilité d'événement. 

Sélectionnez la **fréquence maximale des mises à jour** que vous jugerez utile. Par exemple, si vous comptez envoyer une promotion hebdomadaire pour empêcher les utilisateurs de se désabonner, définissez la fréquence de mise à jour sur **Hebdomadaire** au jour et à l'heure de votre choix. 

!La planification de la mise à jour des prédictions est fixée à tous les jours à 17 heures.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
La prédiction de l'aperçu et de la démo ne mettra jamais à jour le risque de désabonnement des utilisateurs. En outre, les mises à jour quotidiennes des prédictions nécessitent un achat supplémentaire par rapport aux mises à jour hebdomadaires ou mensuelles avec le taux d'attrition prédictif. Pour acheter cette fonctionnalité, contactez votre gestionnaire de compte.
{% endalert %}

## Étape 5 : Créer des prédictions

Vérifiez que les informations que vous avez fournies sont correctes, puis choisissez **Créer une prédiction**. Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Enregistrer comme brouillon** pour revenir à cette page et créer le modèle ultérieurement. Une fois que vous avez sélectionné **Créer une prédiction**, le processus qui génère le modèle commence. Cette opération peut prendre de 30 minutes à quelques heures en fonction du volume des données. Pour cette prédiction, vous verrez une page expliquant que la formation est en cours pour la durée du processus de création du modèle. Le modèle de Braze prend en compte les événements personnalisés, les événements d'achat, les événements d'interaction avec la campagne et les données de session.

Une fois que c'est fait, la page basculera automatiquement vers l'analyse/analytique (et vous recevrez également un e-mail vous informant que les prédictions et les résultats sont prêts). En cas d'erreur, la page revient au mode édition avec une explication de ce qui s'est passé.

La prédiction sera reconstruite ("réentraînée") **automatiquement toutes les deux semaines** afin de la maintenir à jour sur la base des données les plus récentes disponibles. Notez qu'il s'agit d'un processus distinct de la production des _scores de risque de désabonnement_ des utilisateurs, qui sont le résultat de la prédiction. Cette dernière est déterminée par la fréquence de mise à jour que vous avez choisie à l'étape 4.

## Exemples de définitions d'audiences de désabonnement et de prédiction {#sample-definitions}

**Exemples de définitions du désabonnement**<br>
- "Dans les 7 jours, faire l'événement personnalisé 'Annulation de l'abonnement'".<br>
- "Dans les 30 jours, faites l'événement personnalisé 'Essai expiré'".<br>
- "Dans un délai d'un jour, désinstallez. <br>
- "Dans les 14 jours, n'effectuez pas d'achat. <br>

Pour les définitions du désabonnement que nous avons présentées, il pourrait y avoir des définitions correspondantes de l'audience de prédiction :<br>
- **A commencé l'abonnement il y a plus de 2 semaines OU A commencé l'abonnement il y a moins de 2 semaines**<br>Dans ce cas, vous pouvez créer deux prédictions et envoyer des messages différents aux nouveaux abonnés et aux abonnés de longue date. Vous pouvez également définir cette notion comme "premier achat effectué il y a plus de 30 jours".<br>
- **Désinstallateurs**<br>Vous pourriez vous concentrer sur les clients qui ont acheté quelque chose dans un passé récent ou qui ont utilisé l'appli très récemment.<br>
- **Ceux qui risquent de ne pas acheter en raison du désabonnement.**<br>Vous pouvez vous concentrer sur les clients qui ont navigué ou effectué des recherches ou se sont engagés avec votre application plus récemment. Peut-être qu'un rabais approprié empêchera ce groupe plus engagé de se désabonner.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction non archivée continuera à mettre à jour les scores des utilisateurs selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.


