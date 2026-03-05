---
nav_title: Créer une prédiction du taux d'attrition
article_title: Créer une prédiction du taux d'attrition
description: "Cet article explique comment créer une prédiction du taux d'attrition dans le tableau de bord de Braze."
page_order: 1.1

---

# Créer une prédiction du taux d'attrition

> Découvrez comment créer une prédiction du taux d'attrition dans le tableau de bord de Braze.

## Étape 1 : Créer une nouvelle prédiction

Dans Braze, accédez à **Analytique** > **Predictive Churn**.

Une prédiction est une instance d'un modèle de machine learning entraîné, avec tous les paramètres et les données qu'il utilise. Sur cette page, vous verrez une liste des prédictions actives en cours ainsi que quelques informations de base les concernant. Ici, vous pouvez renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores des utilisateurs.

Pour créer une nouvelle prédiction, choisissez **Créer une prédiction** et sélectionnez une nouvelle **Prédiction du taux d'attrition**.

{% alert note %}
Il existe une limite de cinq prédictions du taux d'attrition actives simultanément. Avant l'achat de la fonctionnalité Predictive Churn, la limite est d'une prédiction du taux d'attrition en mode aperçu. Une prédiction du taux d'attrition en mode aperçu ne mettra pas régulièrement à jour les scores et ne vous permettra pas de cibler les utilisateurs en fonction des résultats de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

Sur la page **Bases**, donnez un nom unique à votre nouvelle prédiction. Vous pouvez également fournir une description facultative pour prendre des notes sur cette prédiction particulière.

Sélectionnez **Suivant** pour passer à l'étape suivante. Vous pouvez également sélectionner **Créer maintenant** pour utiliser tous les paramètres par défaut et passer directement à la dernière étape de création. Vous aurez la possibilité de vérifier les paramètres avant de lancer le processus de création. Vous pouvez revenir à n'importe quelle étape ultérieurement en la sélectionnant dans le suivi de progression.

## Étape 2 : Définir l'attrition

Dans le panneau **Définition de l'attrition**, utilisez les filtres fournis pour spécifier comment vous définissez l'attrition des utilisateurs pour votre entreprise. En d'autres termes, que doit faire un utilisateur et dans quel délai pour que vous le considériez comme désabonné ?

N'oubliez pas que vous n'avez pas besoin d'expliquer quels comportements pourraient précéder l'attrition, mais uniquement ce qui fait d'un utilisateur un utilisateur désabonné. Pensez-y en termes d'action qu'un utilisateur effectue une fois (`do`) ou cesse d'effectuer (`do not`) et qui constitue l'attrition. Par exemple, vous pourriez considérer que les utilisateurs qui n'ont pas ouvert votre application depuis 7 jours sont désabonnés. Vous pourriez considérer que la désinstallation, ou des événements personnalisés comme le désabonnement, la désactivation d'un compte ou d'autres actions provoquent l'attrition d'un utilisateur.

#### Fenêtre d'attrition

La fenêtre d'attrition est la période pendant laquelle l'activité d'un utilisateur répond aux critères d'attrition. Vous pouvez la définir jusqu'à 60 jours, en fonction des données disponibles. Cette fenêtre est utilisée pour extraire les données historiques afin d'entraîner votre prédiction. Une fois la prédiction créée, vous verrez s'il y avait suffisamment de données pour obtenir des résultats précis.

Une fois la prédiction créée et les scores attribués aux utilisateurs, le _Score de risque d'attrition_ indique la probabilité qu'un utilisateur se désabonne dans le délai que vous avez défini dans la fenêtre d'attrition.

Voici un exemple de définition simple basée sur l'absence de sessions au cours des 7 derniers jours.

![Définition de l'attrition où un utilisateur est considéré comme désabonné s'il ne démarre pas de session pendant 7 jours]({% image_buster /assets/img/churn/churn1.png %})

Dans ce cas, nous sélectionnons `do not` et `start a session`. Vous pouvez combiner d'autres filtres avec `AND` et `OR` comme bon vous semble pour créer la définition dont vous avez besoin. Vous souhaitez découvrir des définitions d'attrition potentielles ? Vous trouverez de l'inspiration dans la section suivante sur les [Exemples de définitions d'attrition](#sample-definitions).

{% alert note %}
Pour `do`, nous supposons que les utilisateurs actifs n'ont pas effectué l'action que vous spécifiez pour cette ligne avant de devenir désabonnés. L'exécution de l'action les fait devenir désabonnés. <br><br>Pour `do not`, nous considérons comme actifs les utilisateurs qui ont effectué cette action dans les jours précédents, puis ont cessé de le faire. <br><br>**Exemple :** Si l'attrition est définie comme « n'a pas effectué d'achat au cours des 60 derniers jours », nous considérons comme actifs les utilisateurs qui ont effectué un achat au cours des 60 derniers jours. Par conséquent, toute personne n'ayant pas effectué d'achat au cours des 60 derniers jours n'est pas considérée comme un utilisateur actif. Cela signifie qu'une audience d'attrition créée à partir de cette définition n'inclurait que les utilisateurs ayant effectué un achat au cours des 60 derniers jours. L'audience de prédiction du taux d'attrition résultante peut donc sembler nettement plus petite que la population d'origine — la plupart des utilisateurs d'un espace de travail pourraient déjà correspondre à la définition de désabonné et ne seraient donc pas actifs dans la prédiction du taux d'attrition.
{% endalert %}

Sous la définition, vous verrez des estimations du nombre d'utilisateurs (historiques ayant été désabonnés et n'ayant pas été désabonnés selon votre définition) disponibles. Vous verrez également les valeurs minimales requises. Braze doit disposer de ce nombre minimum d'utilisateurs dans les données historiques afin que la prédiction ait suffisamment de données pour apprendre.

## Étape 3 : Filtrer votre audience de prédiction

Votre audience de prédiction est le groupe d'utilisateurs pour lequel vous souhaitez prédire le risque d'attrition. L'audience de prédiction définit le groupe d'utilisateurs que le modèle de machine learning examine pour apprendre du passé. Par défaut, elle est définie sur **Tous les utilisateurs**, ce qui signifie que cette prédiction créera des scores de risque d'attrition pour tous vos utilisateurs actifs (reportez-vous à la note précédente pour savoir qui est considéré comme actif pour un modèle d'attrition).

Selon votre cas d'utilisation, vous pouvez utiliser des filtres pour spécifier les utilisateurs que vous souhaitez évaluer pour le modèle. Pour ce faire, sélectionnez **Définir ma propre audience de prédiction** et choisissez vos filtres d'audience. Par exemple, si vous êtes une application de covoiturage avec des chauffeurs et des passagers dans votre base d'utilisateurs, et que vous créez un modèle d'attrition pour les passagers, vous voudrez filtrer votre audience de prédiction pour ne garder que les passagers. Gardez à l'esprit que de nombreux cas d'utilisation ne nécessitent pas de sélectionner une audience de prédiction spécifique. Par exemple, si votre cas d'utilisation est de cibler les utilisateurs de la région UE les plus susceptibles de se désabonner, vous pouvez exécuter votre modèle sur tous les utilisateurs, puis simplement inclure un filtre pour la région UE dans le segment de la campagne.

Braze vous montrera la taille estimée de votre audience de prédiction. Si vous spécifiez l'audience souhaitée et ne remplissez pas les conditions minimales requises pour exécuter le modèle, essayez de spécifier un filtre plus large ou utilisez l'option **Tous les utilisateurs**. Notez que la taille de votre groupe « tous les utilisateurs » n'est pas statique et varie d'un modèle à l'autre, car elle prend en compte votre définition de l'attrition. Par exemple, si la définition de l'attrition est de **ne pas** effectuer d'achat pendant 30 jours, Braze exécute le modèle sur les utilisateurs qui **ont** effectué un achat au cours des 30 derniers jours (et prédit la probabilité qu'ils **n'effectuent pas** d'achat au cours des 30 prochains jours), ce sont donc ces utilisateurs qui sont reflétés dans l'indicateur « tous les utilisateurs ».

{% alert note %}
L'audience de prédiction ne peut pas dépasser 100 millions d'utilisateurs.
{% endalert %}

Lorsque la fenêtre de prédiction est de 14 jours ou moins, la fenêtre temporelle des filtres commençant par « Dernier... », comme « Dernière utilisation de l'application » et « Dernier achat effectué », **ne peut pas dépasser la fenêtre d'attrition spécifiée** dans la définition de l'attrition. Par exemple, si votre définition de l'attrition a une fenêtre de 14 jours, la fenêtre temporelle des filtres « Dernier... » ne peut pas dépasser 14 jours.

La fenêtre d'attrition est évaluée en remontant le nombre de jours à partir du jour où le modèle a été exécuté pour la dernière fois. Ainsi, si la fenêtre d'attrition est de 15 jours et que le modèle a été exécuté pour la dernière fois le 1er décembre, le modèle analyse la période du 16 au 30 novembre pour comprendre l'activité des utilisateurs en vue de l'éligibilité de l'audience et de l'entraînement.

#### Mode de filtrage complet

Afin de créer une nouvelle prédiction immédiatement, seul un sous-ensemble de filtres de segmentation Braze est pris en charge. Le mode de filtrage complet vous permet d'utiliser tous les filtres Braze, mais nécessitera une fenêtre d'attrition pour créer la prédiction. Par exemple, si la fenêtre d'attrition est définie sur 15 jours, il faudra 15 jours pour collecter les données utilisateur et créer la prédiction lors de l'utilisation de filtres uniquement pris en charge en mode de filtrage complet. De plus, certaines estimations concernant la taille des audiences ne seront pas disponibles en mode de filtrage complet.

Pour un exemple de liste de définitions d'audience de prédiction, consultez nos exemples de définitions dans la section suivante sur les [Exemples de définitions d'attrition](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Comme sur la page précédente, le panneau inférieur vous montrera le nombre estimé d'utilisateurs historiques résultant de votre définition de l'attrition et de votre définition d'audience de prédiction. Ces estimations doivent répondre aux exigences minimales indiquées pour pouvoir créer une prédiction.

## Étape 4 : Choisir la fréquence de mise à jour de la prédiction du taux d'attrition

Le modèle de machine learning générera des scores de probabilité d'événement pour les utilisateurs, et ces scores seront mis à jour selon la planification que vous sélectionnez ici. Vous pourrez cibler les utilisateurs en fonction de leur score de probabilité d'événement.

Sélectionnez la **fréquence maximale de mise à jour** que vous jugerez utile. Par exemple, si vous allez envoyer une promotion hebdomadaire pour empêcher les utilisateurs de se désabonner, définissez la fréquence de mise à jour sur **Hebdomadaire** au jour et à l'heure de votre choix.

![Planification de mise à jour de la prédiction définie sur quotidienne à 17 h.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
Les prédictions en mode aperçu et démo ne mettront jamais à jour le risque d'attrition des utilisateurs. De plus, les mises à jour quotidiennes des prédictions nécessitent un achat supplémentaire au-delà des mises à jour hebdomadaires ou mensuelles avec Predictive Churn. Pour acheter cette fonctionnalité, contactez votre gestionnaire de compte.
{% endalert %}

## Étape 5 : Créer la prédiction

Vérifiez que les détails que vous avez fournis sont corrects, puis choisissez **Créer la prédiction**. Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Enregistrer comme brouillon** pour revenir à cette page et créer le modèle ultérieurement. Après avoir sélectionné **Créer la prédiction**, le processus de génération du modèle commencera. Cela peut prendre entre 30 minutes et quelques heures, selon les volumes de données. Pour cette prédiction, vous verrez une page expliquant que l'entraînement est en cours pendant toute la durée du processus de création du modèle. Le modèle Braze prend en compte les événements personnalisés, les événements d'achat, les événements d'interaction avec les campagnes et les données de session.

Une fois terminé, la page basculera automatiquement vers la vue analytique, et vous recevrez également un e-mail vous informant que la prédiction et les résultats sont prêts. En cas d'erreur, la page reviendra au mode d'édition avec une explication de ce qui s'est mal passé.

La prédiction sera reconstruite (« réentraînée ») automatiquement toutes les **deux semaines** pour rester à jour avec les données les plus récentes disponibles. Notez qu'il s'agit d'un processus distinct de celui où les _Scores de risque d'attrition_ des utilisateurs, le résultat de la prédiction, sont produits. Ce dernier est déterminé par la fréquence de mise à jour que vous avez choisie à l'étape 4.

## Exemples de définitions d'attrition et d'audience de prédiction {#sample-definitions}

**Exemples de définitions d'attrition**<br>
- « Période de 7 jours, effectuer l'événement personnalisé 'Annulation d'abonnement' »<br>
- « Période de 30 jours, effectuer l'événement personnalisé 'Essai expiré' »<br>
- « Période de 1 jour, effectuer une désinstallation. »<br>
- « Période de 14 jours, ne pas effectuer d'achat. »<br>

Pour les définitions d'attrition que nous avons décrites, voici quelques définitions d'audience de prédiction correspondantes :<br>
- **A commencé un abonnement il y a plus de 2 semaines OU a commencé un abonnement il y a moins de deux semaines**<br>Vous pourriez vouloir créer 2 prédictions dans ce cas et envoyer des messages différents aux nouveaux abonnés par rapport aux abonnés de longue date. Vous pourriez également définir cela comme « Premier achat effectué il y a plus de 30 jours ».<br>
- **Désinstallateurs**<br>Vous pourriez vous concentrer sur les clients qui ont acheté quelque chose récemment ou qui ont utilisé l'application très récemment.<br>
- **Ceux à risque de ne pas acheter comme définition de l'attrition**<br>Vous pourriez vouloir vous concentrer sur les clients qui ont navigué, recherché ou interagi avec votre application plus récemment. Peut-être que la bonne intervention promotionnelle empêchera ce groupe plus engagé de se désabonner.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction archivée qui est désarchivée continuera à mettre à jour les scores des utilisateurs selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.