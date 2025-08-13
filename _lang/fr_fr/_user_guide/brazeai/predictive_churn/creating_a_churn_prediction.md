---
nav_title: Créer une prédiction d’attrition
article_title: Créer une prédiction d’attrition
description: "Cet article explique comment créer une prédiction du taux de désabonnement dans le tableau de bord de Braze."
page_order: 1.1

---

# Créer une prédiction du taux d'attrition

> Découvrez comment créer une prédiction du taux de désabonnement dans le tableau de bord de Braze.

## Étape 1 : Créer une nouvelle prédiction

Dans Braze, sélectionnez **Analyse** > **Prédiction du taux d'attrition**.

Une prédiction est une instance d'un modèle d'apprentissage automatique formé et de tous les paramètres et données qu'il utilise. Sur cette page, vous trouverez une liste des prédictions actives actuelles ainsi que quelques informations de base à leur sujet. Vous pouvez y renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores utilisateur. 

Pour créer une nouvelle prédiction, choisissez **Créer une prédiction** et sélectionnez une nouvelle **prédiction du taux d'attrition**.

{% alert note %}
Le nombre de prédictions du taux d'attrition actives simultanément est limité à cinq. Si vous n’avez pas acheté la prédiction du taux d'attrition, la limite est d’un seul aperçu de prédiction d'attrition actif. Une prédiction du taux d'attrition ne met pas régulièrement à jour les scores et ne vous permet pas de cibler les utilisateurs sur la base des résultats de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

Sur la page de **base**, donnez un nom unique à votre nouvelle prédiction. Vous pouvez également fournir une description facultative pour prendre des notes sur cette prédiction particulière.

Cliquez sur **Suivant** pour passer à l'étape suivante. En option, vous pouvez cliquer sur **Créer maintenant** pour utiliser tous les paramètres par défaut et passer à la dernière étape de la création. Vous aurez la possibilité d’examiner les paramètres avant de commencer le processus de création. Vous pouvez revenir à n’importe quelle étape ultérieurement en la sélectionnant dans le traceur de progression au-dessus.

## Étape 2 : Définir l’attrition

Dans le panneau **Définition du désabonnement**, utilisez les filtres fournis pour spécifier la manière dont vous définissez le désabonnement des utilisateurs pour votre entreprise. En d’autres termes, qu’est-ce qu’un utilisateur doit faire et dans quel délai pour que vous considériez qu’il a abandonné ?

N’oubliez pas que vous n’avez pas besoin d’expliquer les comportements qui peuvent précéder l’abandon, seulement ce qui transforme un utilisateur en utilisateur ayant abandonné. Pensez à cela en termes de ce qu’un utilisateur fait une fois (`do`) ou arrête de faire (`do not`) qui constituerait l’attrition. Par exemple, vous pouvez considérer les utilisateurs qui n’ont pas ouvert votre application en 7 jours comme ayant abandonné. Vous pourriez envisager que désinstaller, ou des événements personnalisés comme se désabonner, désactiver un compte ou autres, indiquent l’abandon de l’utilisateur. 

#### Fenêtre d’attrition

La fenêtre d’attrition est le cadre temporel au cours duquel un utilisateur effectue le comportement spécifié constituant l’attrition. Elle peut être réglée sur 60 jours. Cette fenêtre permet d'interroger les données historiques pour l'apprentissage des prédictions. De plus, une fois que la prédiction est créée et que les utilisateurs reçoivent des scores, le _score du risque d’attrition_ indique la probabilité qu’un utilisateur abandonne durant le nombre de jours spécifiés par la fenêtre d’attrition. 

Voici un exemple de définition simple basée sur l’inactivité des sessions au cours des 7 derniers jours.

![Définition du désabonnement : un utilisateur est considéré comme désabonné s'il ne démarre pas de session dans les 7 jours]({% image_buster /assets/img/churn/churn1.png %})

Dans ce cas, nous sélectionnons `do not` et `start a session`. Vous pouvez combiner d’autres filtres avec `AND` et `OR` comme vous le désirez pour créer la définition dont vous avez besoin. Vous êtes intéressé par certaines définitions d’attrition à envisager ? Vous pouvez trouver votre inspiration dans la section suivante sur les [exemples de définition de l’attrition](#sample-definitions).

{% alert note %}
Pour `do`, nous supposons que les utilisateurs actifs n’ont pas effectué l’action que vous spécifiez pour cette ligne avant d’être considérés comme ayant abandonné. Effectuer l’action entraîne leur considération comme ayant abandonné. <br><br>Pour `do not`, nous considérons que les utilisateurs actifs sont ceux qui ont effectué cette action dans les jours qui précèdent, puis arrêtent.
{% endalert %}

Sous la définition, vous verrez les estimations du nombre d’utilisateurs disponibles (qui ont abandonné ou pas par le passé selon votre définition). Vous verrez également les valeurs minimales requises. Braze doit disposer de ce nombre minimum d'utilisateurs dans les données historiques afin que la prédiction dispose de suffisamment de données pour apprendre.

## Étape 3 : Filtrer votre audience de prédiction

Votre audience de prédiction est le groupe d'utilisateurs pour lesquels vous souhaitez prédire le risque de désabonnement. Par défaut, ce paramètre est défini sur **Tous les utilisateurs**, ce qui signifie que cette prédiction créera des scores de risque de désabonnement pour tous vos utilisateurs actifs. En général, le modèle fonctionnera probablement mieux si vous limitez et filtrez le groupe d’utilisateurs que vous souhaitez empêcher d’abandonner selon certains critères. Pensez aux utilisateurs spécifiques qui signifient le plus pour vous et que vous souhaitez conserver et définissez-les ici. Par exemple, vous souhaitez peut-être fidéliser les utilisateurs qui ont utilisé l’application il y a plus d’un mois ou qui ont déjà effectué un achat.

{% alert note %}
L'audience des prédictions ne peut dépasser 100 millions d'utilisateurs.
{% endalert %}

Lorsque la fenêtre de prédiction est de 14 jours ou moins, la fenêtre temporelle pour les filtres qui commencent par « Dernier… », tels que « Dernière utilisation de l’application » et « Dernier achat effectué » **ne peuvent pas dépasser la fenêtre d’attrition indiquée** dans la définition de l’attrition. Par exemple, si votre définition de l’attrition dispose d’une fenêtre de 14 jours, la fenêtre temporelle du filtre « Dernier… » ne peut pas dépasser 14 jours.

#### Mode de filtrage complet

Afin de créer immédiatement une nouvelle prédiction, seul un sous-ensemble de filtres de segmentation de Braze est pris en charge. Le mode filtrage complet vous permet d'utiliser tous les filtres de Braze mais nécessite une fenêtre de désabonnement pour créer la prédiction. Par exemple, si la fenêtre d’attrition est définie sur 15 jours, il faudra 15 jours pour collecter les données de l'utilisateur et créer la prédiction lors de l'utilisation de filtres uniquement pris en charge en mode de filtrage complet. En outre, certaines estimations concernant la taille des audiences ne seront pas disponibles en mode filtrage complet.

Pour obtenir une liste d'exemples de définitions d’audience de prédiction, consultez nos exemples de définitions dans la section suivante sur les [exemples de définitions de l'attrition](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Tout comme la page précédente, le panneau inférieur vous indique le nombre estimé d'utilisateurs désabonnés résultant de votre définition du désabonnement et de la définition de l'audience de prédiction. Ces estimations doivent répondre aux exigences minimales indiquées afin de créer une prédiction.

## Étape 4 : Choisissez la fréquence de mise à jour pour la prédiction du taux d'attrition.

Le modèle de machine learning créé lorsque vous remplissez cette page sera utilisé selon une planification que vous sélectionnez ici pour générer de nouveaux scores de risque de désabonnement. Sélectionnez la **fréquence maximale des mises à jour** que vous jugerez utile. Par exemple, si vous comptez envoyer une promotion hebdomadaire pour empêcher les utilisateurs de se désabonner, définissez la fréquence de mise à jour sur **Hebdomadaire** au jour et à l'heure de votre choix. 

![La planification de la mise à jour des prédictions est fixée quotidiennement à 17 heures.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
La prédiction d'un aperçu ou d'une démo ne mettra jamais à jour le risque de désabonnement des utilisateurs. En outre, les mises à jour quotidiennes des prédictions nécessitent un achat supplémentaire par rapport aux mises à jour hebdomadaires ou mensuelles avec le taux d'attrition prédictif. Pour acheter cette fonctionnalité, contactez votre gestionnaire de compte.
{% endalert %}

## Étape 5 : Créer la prédiction

Vérifiez que les informations que vous avez fournies sont correctes, puis choisissez **Créer la prédiction**. Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Enregistrer comme brouillon** pour revenir à cette page et créer le modèle ultérieurement. Une fois que vous avez cliqué sur **Créer une prédiction**, le processus qui génère le modèle commence. Cela peut prendre entre 30 minutes et quelques heures en fonction du volume de données. Pour cette prédiction, vous verrez une page expliquant que la formation est en cours pour la durée du processus de création du modèle.

Une fois que c'est fait, la page basculera automatiquement vers l'analyse/analytique (et vous recevrez également un e-mail vous informant que les prédictions et les résultats sont prêts). En cas d’erreur, la page revient en mode Édition avec une explication de ce qui s’est mal passé.

La prédiction sera reconstruite ("réentraînée") **automatiquement toutes les deux semaines** afin de la maintenir à jour sur la base des données les plus récentes disponibles. Notez qu'il s'agit d'un processus distinct de la production des _scores de risque de désabonnement_ des utilisateurs, qui sont le résultat de la prédiction. Ces derniers sont déterminés par la fréquence de mise à jour que vous avez choisie à l’étape 4.

## Exemples de définitions d’attrition et de l’audience de prédiction {#sample-definitions}

**Exemples de définitions de l’attrition**<br>
- « Dans les 7 jours, effectue l’événement personnalisé "Annulation d’abonnement". »<br>
- « Dans les 30 jours, effectue l’événement personnalisé "Essai expiré". »<br>
- « Dans un délai d’un jour, effectue une désinstallation. » <br>
- « Dans les 14 jours, ne réalise pas d’achat. » <br>

Pour les définitions du désabonnement que nous avons présentées, il pourrait y avoir des définitions correspondantes de l'audience de prédiction :<br>
- **A commencé l'abonnement il y a plus de 2 semaines OU A commencé l'abonnement il y a moins de 2 semaines**<br>Vous pourriez désirer créer 2 prédictions dans ce cas, puis contacter les nouveaux utilisateurs abonnés différemment que les anciens. Vous pouvez également définir cela comme « Premier achat réalisé il y a plus de 30 jours ».<br>
- **Désinstallateurs**<br>Vous pourriez vous concentrer sur les clients qui ont acheté quelque chose il y a peu ou utilisé l’application très récemment.<br>
- **Les personnes « à risque de ne pas acheter » en tant que définition de l’attrition**<br>Vous pourriez désirer vous concentrer sur les clients qui ont parcouru, recherché ou se sont engagés avec votre application plus récemment. Peut-être que l’apparition d’une remise appropriée empêchera ce groupe plus engagé d’abandonner.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction non archivée continuera à mettre à jour les scores des utilisateurs selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.


