---
nav_title: Créer une prédiction d’attrition
article_title: Créer une prédiction d’attrition
description: "Le présent article explique comment créer une prédiction d’attrition dans le tableau de bord de Braze"
page_order: 1

---

# Créer une prédiction d’attrition

## Étape 1 : Créer une nouvelle prédiction

Depuis la barre de navigation de gauche sur le tableau de bord de Braze, choisissez la page **Predictions**. Une prédiction est une instance d’un modèle de machine learning entraîné et de tous les paramètres et données qu’il utilise. Sur cette page, vous verrez une liste des prédictions actuellement actives ainsi que des informations de base à leur sujet. Ici, vous pouvez renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores utilisateur. 

Pour créer une nouvelle prédiction, choisissez **Create Prediction (Créer une prédiction)** et sélectionnez une nouvelle **Churn Prediction (Prédiction de l’attrition)**.

{% alert note %}
Il y existe une limite de cinq prédictions d’attrition actives simultanément. Si vous n’avez pas acheté la Prédiction du taux d'attrition, la limite est d’un seul aperçu de prédiction d'attrition actif. Un aperçu de prédiction d’attrition n’actualisera pas régulièrement les scores ni ne vous permettra de cibler les utilisateurs sur la base des résultats de la prévision. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

Sur la page **Basics (Bases)**, donnez un nom unique à votre nouvelle prédiction. Vous pouvez également fournir une description facultative pour prendre des notes sur cette prédiction particulière.

Cliquez sur **Forward (Avancer)** pour passer à l’étape suivante. Facultativement, vous pouvez cliquer sur **Build Now (Construire maintenant)** pour utiliser tous les paramètres par défaut et passer à la dernière étape de création. Vous aurez la possibilité d’examiner les paramètres avant de commencer le processus de construction. Vous pouvez revenir à n’importe quelle étape ultérieurement en la sélectionnant dans le traceur de progression au-dessus.

## Étape 2 : Définir l’attrition

Dans le panneau **Churn Definition (Définition de l’attrition)** utilisez les filtres fournis pour spécifier la manière dont vous définissez l’attrition utilisateur pour votre société. En d’autres termes, qu’est-ce qu’un utilisateur doit faire et dans quel délai pour que vous considériez qu’il a abandonné ?

N’oubliez pas que vous n’avez pas besoin d’expliquer les comportements qui peuvent précéder l’abandon, seulement ce qui transforme un utilisateur en utilisateur ayant abandonné. Pensez à cela en termes de ce qu’un utilisateur fait une fois (`do`) ou arrête de faire (`do not`) qui constituerait l’attrition. Par exemple, vous pouvez considérer les utilisateurs qui n’ont pas ouvert votre application en 7 jours comme ayant abandonné. Vous pourriez envisager que désinstaller, ou des événements personnalisés comme se désabonner, désactiver un compte ou autres, indiquent l’abandon de l’utilisateur. 

#### Fenêtre d’attrition

La fenêtre d’attrition est le cadre temporel au cours duquel un utilisateur exécute le comportement spécifié constituant l’attrition. Elle peut être réglée sur 60 jours. Cette fenêtre permet de rechercher des données historiques pour entraîner la prédiction. De plus, une fois que la prédiction est créée et que les utilisateurs reçoivent des scores, le « Churn Risk Score » (Score de risque d’attrition) indique la probabilité qu’un utilisateur abandonne durant le nombre de jours spécifiés par la fenêtre d’attrition. 

Voici un exemple de définition simple basée sur l’inactivité des sessions au cours des 7 derniers jours.

![Définition de l’attrition dans laquelle un utilisateur est considéré comme ayant abandonné s’il ne démarre pas une session pendant 7 jours][1]

Dans ce cas, nous sélectionnons `do not` et `start a session`. Vous pouvez combiner d’autres filtres avec `AND` et `OR` comme vous le désirez pour créer la définition dont vous avez besoin. Vous êtes intéressé par certaines définitions d’attrition à envisager ? Vous pouvez trouver de l’inspiration dans la section suivante : [Exemples de définition de l’attrition](#sample-definitions).

{% alert note %}
Pour `do`, nous supposons que les utilisateurs actifs n’ont pas effectué l’action que vous spécifiez pour cette ligne avant d’être considérés comme ayant abandonné. Effectuer l’action entraîne leur considération comme ayant abandonné. <br><br>Pour `do not`, nous considérons que les utilisateurs actifs sont ceux qui ont effectué cette action dans les jours qui précèdent, puis arrêtent.
{% endalert %}

Sous la définition, vous verrez les estimations du nombre d’utilisateurs disponibles (qui ont abandonné ou pas par le passé selon votre définition). Vous verrez également les valeurs minimales requises. Braze doit avoir ce nombre minimum d’utilisateurs disponibles dans les données historiques afin que la prédiction dispose de suffisamment de données pour apprendre.

## Étape 3 : Filtrer votre audience de prédiction

Votre audience de prédiction est le groupe d’utilisateurs pour lequel vous souhaitez prédire le risque d’attrition. Par défaut, il sera défini sur **Tous les utilisateurs**, ce qui signifie que cette prédiction créera des scores de risque d’attrition pour tous vos utilisateurs actifs. En général, le modèle fonctionnera probablement mieux si vous limitez et filtrez le groupe d’utilisateurs que vous souhaitez empêcher d’abandonner selon certains critères. Pensez aux utilisateurs spécifiques qui signifient le plus pour vous et que vous souhaitez conserver et définissez-les ici. Par exemple, vous souhaitez peut-être fidéliser les utilisateurs qui ont utilisé l’application il y a plus d’un mois ou qui ont déjà effectué un achat.

{% alert note %}
L’audience de prédiction ne peut pas dépasser 100 millions d’utilisateurs.
{% endalert %}

Lorsque la fenêtre de prédiction est de 14 jours ou moins, la fenêtre temporelle pour les filtres qui commencent par « Dernière… » tels que « Dernière utilisation de l’application » et « Dernier achat effectué » **ne peuvent pas dépasser la fenêtre d’attrition définie** dans la définition de l’attrition. Par exemple, si votre définition de l’attrition dispose d’une fenêtre de 14 jours, la fenêtre temporelle du filtre « Dernier… » ne peut pas dépasser 14 jours.

#### Mode de filtrage complet

Afin de créer une nouvelle prédiction immédiatement, seul un sous-ensemble de filtres de segmentation Braze est pris en charge. Le Mode de filtrage complet vous permet d’utiliser tous les filtres Braze, mais nécessite une «Churn Window » (Fenêtre d’attrition) pour créer la prédiction. Par exemple, si la «Churn Window » (Fenêtre d’attrition) est définie sur 15 jours, il faudra 15 jours pour collecter les données utilisateur et construire la prédiction lorsque vous utilisez des filtres uniquement pris en charge en Mode de filtrage complet. En outre, certaines estimations sur les tailles d’audience ne seront pas disponibles en Mode de filtrage complet.

Pour obtenir un exemple de liste des définitions d’audience de prédiction, consultez nos exemples de définitions dans la section suivante : [Exemples de définition de l’attrition](#sample-definitions).

![][3]

Tout comme pour la page précédente, le panneau inférieur vous indiquera le nombre estimé d’utilisateurs historiques qui résultent de vos définitions d’attrition et d’audience de prédiction. Ces estimations doivent satisfaire aux exigences minimales indiquées afin de créer une prédiction.

## Étape 4 : Choisir la fréquence de mise à jour pour les prédictions d’attrition

Le modèle de machine learning créé lorsque vous remplissez cette page sera utilisé selon une planification que vous sélectionnez ici pour générer de nouveaux scores de risque d’attrition. Sélectionnez la **fréquence maximale des mises à jour** que vous trouvez utile. Par exemple, si vous allez envoyer une promotion hebdomadaire pour empêcher les utilisateurs d’abandonner, définissez la fréquence de mise à jour sur **Hebdomadaire** au jour et à l’heure de votre choix. 

![Planification de mise à jour de prédiction définie quotidiennement à 17 h.][2]

{% alert note %}
Les prévisualisations et les démonstrations de prédictions ne mettront jamais à jour le risque d’attrition des utilisateurs. De plus, les mises à jour quotidiennes des prédictions nécessitent un achat supplémentaire en plus des mises à jour hebdomadaires ou mensuelles pour la Prédiction du taux d'attrition. Pour acheter cette fonctionnalité, contactez votre gestionnaire de compte. 
{% endalert %}

## Étape 5 : Construire la prédiction

Vérifiez que les détails que vous avez fournis sont corrects et choisissez **Build Prediction** (Construire la prédiction). Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Save As Draft (Enregistrer en tant que brouillon)** pour revenir à cette page et créer le modèle ultérieurement. Une fois que vous cliquez sur **Construire la prédiction**, le processus qui génère le modèle commence. Cela peut prendre entre 30 minutes et quelques heures en fonction du volume de données. Pour cette prédiction, vous verrez une page expliquant que l’entraînement est en cours pendant la durée du processus de construction du modèle.

Une fois qu’il est terminé, la page passera automatiquement à l’affichage de l’analytique et vous recevrez également un e-mail vous informant que la prédiction et les résultats sont prêts. En cas d’erreur, la page revient en mode Édition avec une explication de ce qui s’est mal passé.

La prédiction sera reconstruite (« entraînée ») à nouveau toutes les **deux semaines automatiquement** pour la maintenir à jour sur les données les plus récentes disponibles. Prenez en compte qu’il s’agit d’un processus distinct de celui où les scores de risque d’attrition des utilisateurs, le résultat de la prédiction, sont produits. Ces derniers sont déterminés par la fréquence de mise à jour que vous avez choisie à l’étape 4.

## Exemples de définitions d’attrition et de l’audience de prédiction {#sample-definitions}

**Exemples de définition de l’attrition**<br>
- « Dans les 7 jours, effectue l’événement personnalisé "Annulation d’abonnement". »"<br>
- « Dans les 30 jours, effectue l’événement personnalisé "Essai expiré". »"<br>
- « Dans un délai d’un jour, effectue une désinstallation. » <br>
- « Dans les 14 jours, ne réalise pas d’achat. » <br>

Pour les définitions d’attrition que nous avons définies, il peut y avoir des définitions d’audience de prédiction correspondantes :<br>
- **Abonnement démarré il y a plus de 2 semaines OU Abonnement démarré il y a moins de 2 semaines**<br>Vous pourriez désirer créer 2 prédictions dans ce cas, puis contacter les nouveaux utilisateurs abonnés différemment que les anciens. Vous pouvez également définir cela comme « Premier achat réalisé il y a plus de 30 jours »."<br>
- **Utilisateurs qui désinstallent**<br>Vous pourriez vous concentrer sur les clients qui ont acheté quelque chose il y a peu ou utilisé l’application très récemment.<br>
- **Les personnes « à risque de ne pas acheter » en tant que définition de l’attrition**<br>Vous pourriez désirer vous concentrer sur les clients qui ont parcouru, recherché ou se sont engagés avec votre application plus récemment. Peut-être que l’apparition d’une remise appropriée empêchera ce groupe plus engagé d’abandonner.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores utilisateur. Toute prédiction archivée qui est désarchivée continuera à mettre à jour les scores utilisateur selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.

[1]: {% image_buster /assets/img/churn/churn1.png %}
[2]: {% image_buster /assets/img/churn/churn2.png %}
[3]: {% image_buster /assets/img/churn/churn5.png %}

