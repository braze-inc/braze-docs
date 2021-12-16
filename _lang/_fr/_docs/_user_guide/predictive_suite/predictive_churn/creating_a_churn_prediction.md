---
nav_title: Créer une prédiction de la nature
article_title: Créer une prédiction de la nature
description: "Cet article couvre la façon de créer une prédiction de Churchn dans le tableau de bord de Braze"
page_order: 1
---

# Créer une prédiction de la nature

## Étape 1 : Créer une nouvelle prédiction

Sur la barre de navigation gauche du tableau de bord Braze, choisissez la page __Prédictions__. Une prédiction est une instance d'un modèle d'apprentissage automatique formé et de tous les paramètres et données qu'il utilise. Sur cette page, vous verrez une liste des prédictions actives actuelles ainsi que quelques informations de base à leur sujet. Ici vous pouvez renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores des utilisateurs.

Pour créer une nouvelle prédiction, choisissez __Créer une prédiction__ dans le coin supérieur droit et sélectionnez une nouvelle __prédiction de la coque__.

{% alert note %}
Il y a une limite de 3 Églises prédictions simultanément actives. Avant d'acheter une Église prédictive, la limite est une Prévisualisation active de la prédiction. Un aperçu de la prévision ne mettra pas régulièrement à jour les scores ou ne vous permettra pas de cibler les utilisateurs en fonction de la sortie de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

Sur la page **Basics** , donnez à votre nouvelle prédiction un nom unique. Vous pouvez également fournir une description facultative pour prendre des notes sur cette prédiction.

Cliquez sur __Avancer__ pour passer à l'étape suivante. En option, vous pouvez cliquer sur __Build Now__ pour utiliser tous les paramètres par défaut et passer à la dernière étape de la création. Vous aurez une chance de vérifier les paramètres avant de commencer le processus de construction. Vous pouvez revenir à n'importe quelle étape plus tard en la sélectionnant dans le tracker de progression en haut.

## Étape 2 : Définir le churn

Dans le panneau __Définition de la Churn__ , utilisez les filtres fournis pour spécifier comment vous définissez la propriété de l'utilisateur pour votre entreprise. En d'autres termes, qu'est-ce qu'un utilisateur a à faire dans quel délai pour que vous les considériez foulés ?

Rappelez-vous que vous n’avez pas besoin d’expliquer quels comportements pourraient précéder l’église — seulement ce qui fait de l’utilisateur un utilisateur désagréé. Pensez à cela en termes de quelque chose qu'un utilisateur fait une fois (`do`) ou arrête de faire (`do not`) qui constitue un semblant. Par exemple, vous pouvez considérer que les utilisateurs qui n'ont pas ouvert votre application depuis 7 jours doivent être abonnés. Vous pourriez envisager la désinstallation ou des événements personnalisés tels que la désinscription, la désactivation d'un compte ou d'autres pour faire qu'un utilisateur devienne apparié.

Voici un exemple de définition simple basée sur les sessions de lapsing au cours des 7 derniers jours.

!\[Définition de Churn \]\[1\]

Dans ce cas, nous sélectionnons `ne pas` et `démarre une session`. Vous pouvez combiner d'autres filtres avec `ET` et `OU` comme bon vous semble pour créer la définition dont vous avez besoin. Intéressé par certaines définitions potentielles de churn à prendre en considération? Vous pouvez trouver de l'inspiration dans la section sur [Exemples de définitions de churn](#sample-definitions) ci-dessous.

{% alert note %}
Pour `faire`, nous supposons que les utilisateurs actifs n'ont pas fait l'action que vous spécifiez pour cette ligne avant de devenir appariés. Faire cette action les fait mourir. <br><br>Car `ne le font pas`, nous considérons que les utilisateurs actifs sont ceux qui ont fait cette action dans les jours précédents, puis arrêtés.
{% endalert %}

Sous la définition, vous verrez des estimations sur le nombre d'utilisateurs (dans le passé qui ont croulé et qui n'ont pas croulé selon votre définition) sont disponibles. Vous verrez également les valeurs minimales requises. Braze doit avoir ce nombre minimum d'utilisateurs disponibles dans les données historiques afin que la prédiction dispose de suffisamment de données pour apprendre.

## Étape 3 : Filtrer votre audience de prédiction

Votre Audience de Prédiction est le groupe d'utilisateurs pour lequel vous voulez prédire le risque de mouton. Par défaut, cela sera réglé sur __Tous les utilisateurs__, ce qui signifie que cette prédiction créera des notes de risque pour tous vos utilisateurs actifs. Habituellement, le modèle sera probablement plus performant si vous affinez et filtrez le groupe d'utilisateurs que vous voulez éviter de retourner avec certains critères. Pensez aux utilisateurs spécifiques qui veulent le plus pour vous que vous souhaitez conserver et définir ici. Par exemple, vous pourriez vouloir conserver les utilisateurs qui ont utilisé l'application pour la première fois il y a plus d'un mois ou qui ont déjà fait un achat.

{% alert note %}
L'audience de prédiction ne peut excéder 100 millions d'utilisateurs.
{% endalert %}

Pour les filtres qui commencent par « ... comme Dernier App Utilisé et Dernier Achat, la fenêtre de temps pour regarder en arrière pour ces filtres __ne peut pas excéder 30 jours moins le nombre de jours de la fenêtre spécifiée__ dans la définition de la Churn. Par exemple, si votre définition de Churn a une fenêtre de 14 jours, la fenêtre de temps pour le « Dast ». .” les filtres ne doivent pas excéder 30 - 14 = 16 jours.

Pour un exemple de liste de définitions d'audience de prédiction, consultez nos exemples de définitions dans la section sur [Les exemples de définitions de churn](#sample-definitions) ci-dessous.

!\[Audience de la prédiction\]\[3\]

Tout comme la page précédente, le panneau du bas vous montrera le nombre estimé d'utilisateurs historiques qui résultent de votre définition de Churn et de la définition de l'audience de prévision. Ces estimations doivent répondre aux exigences minimales indiquées pour créer une prédiction.

## Étape 4 : Choisissez la fréquence de mise à jour pour les prédictions de type Churn

Le modèle d'apprentissage automatique créé lorsque vous complétez cette page sera utilisé selon un horaire que vous sélectionnez ici pour générer de nouveaux scores de risque de cohabitation. Veuillez sélectionner la __fréquence maximale de mises à jour__ que vous trouverez utile. Par exemple, si vous allez envoyer une promotion hebdomadaire pour empêcher les utilisateurs de s'absenter, réglez la fréquence de mise à jour sur __Hebdomadaire__ le jour et l'heure de votre choix.

!\[Calendrier de mise à jour de la prédiction\]\[2\]

{% alert note %}
Les prédictions d'aperçu et de démo ne mettront jamais à jour le risque d'apparition des utilisateurs. En outre, les mises à jour quotidiennes des prédictions nécessitent un achat supplémentaire au-delà des mises à jour hebdomadaires ou mensuelles auprès de l’Église prédictive. Pour acheter cette fonctionnalité, contactez votre responsable de compte.
{% endalert %}

## Étape 5 : Construire la prédiction

Vérifiez que les détails que vous avez fournis sont corrects et choisissez __Prédiction de construction__. Vous pouvez également enregistrer vos modifications dans le formulaire brouillon en sélectionnant __Enregistrer comme brouillon__ pour revenir à cette page et construire le modèle plus tard. Une fois que vous cliquez sur __Build Prediction__, le processus qui génère le modèle va commencer. Cela peut prendre entre 30 minutes et quelques heures selon les volumes de données. Pour cette prédiction, vous verrez une page expliquant que la formation est en cours pour la durée du processus de construction du modèle.

Une fois terminée, la page passera à la vue Analytics automatiquement, et vous recevrez également un courriel vous informant que la Prédiction et les résultats sont prêts. En cas d'erreur, la page retournera au mode Édition avec une explication de ce qui s'est mal passé.

La prédiction sera reconstruite ("reformée") toutes les __deux semaines automatiquement__ pour la tenir à jour sur les données les plus récentes disponibles. Notez que ce processus est séparé du moment où les résultats de la prédiction sont produits par les utilisateurs. Cette dernière est déterminée par la fréquence de mise à jour que vous avez choisie à l'étape 4.

## Exemple de définitions d'orthographe et d'audience de prédiction {#sample-definitions}

__Échantillons de définitions__<br>
- « Dans les 7 jours, faire un événement personnalisé « Annulation d'abonnement»»<br>
- « Dans les 14 jours, faire un événement personnalisé « Épreuve expirée»<br>
- « Dans un délai d'un jour, ne désinstallez pas. » <br>
- « Dans les 14 jours ne font pas d’achat. » <br>

Pour les définitions des Églises que nous avons décrites ci-dessus, il peut y avoir des définitions correspondantes d'Audience de Prédiction :<br>
- __Un abonnement démarré il y a plus de 2 semaines OU un abonnement démarré il y a moins de deux semaines__<br>Vous pouvez créer 2 prédictions dans ce cas, puis envoyer un message aux nouveaux abonnés différemment des abonnés à plus long terme. Vous pourriez également définir ceci comme « premier achat fait il y a plus de 30 jours ».<br>
- __Uninstallers__<br>Vous pouvez vous concentrer sur les clients qui ont acheté quelque chose dans le passé récent ou utilisé l'application très récemment.<br>
- __Ceux qui risquent de ne pas acheter en tant que définition de Churn__<br>Vous pouvez vous concentrer sur les clients qui ont navigué ou recherché ou engagé plus récemment avec votre application. Peut-être que la bonne intervention de réduction empêchera ce groupe plus engagé de s'effondrer.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction archivée qui est désarchivée continuera à mettre à jour les scores des utilisateurs selon son calendrier prédéterminé. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.
[1]: {% image_buster /assets/img/churn/churn1.png %} [2]: {% image_buster /assets/img/churn/churn2.png %} [3]: {% image_buster /assets/img/churn/churn5.png %}

