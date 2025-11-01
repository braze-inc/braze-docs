---
nav_title: "Création d'une prédiction d'événement"
article_title: "Création d'une prédiction d'événement"
page_order: 1.1
description: "Cet article explique comment créer une prédiction d'événement dans le tableau de bord de Braze."

---

# Création d'une prédiction d'événement

> Une prédiction est une instance d'un modèle d'apprentissage automatique formé et de tous les paramètres et données qu'il utilise. Pour en savoir plus sur les prédictions, consultez l'[aperçu des prédictions]({{site.baseurl}}/user_guide/brazeai//predictive_events/).

Dans Braze, allez dans **Analyses/analytiques** > Prédictions (si vous utilisez une **analyse** prévisionnelle).

Sur cette page, vous trouverez une liste des prédictions d'événements actifs actuels et quelques informations de base à leur sujet. Vous pouvez y renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores des utilisateurs.

## Étape 1 : Créer une nouvelle prédiction

1. Choisissez **Créer une prédiction** et sélectionnez une nouvelle **prédiction d'événement.**

{% alert note %}
Le nombre de prédictions actives simultanément est limité à cinq. Avant d'acheter des événements prédictifs, la limite est d'une prédiction active. Une prédiction préalable n'actualisera pas régulièrement les scores ou ne ciblera pas les utilisateurs sur la base des résultats de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

{: start="2"}
2\. Donnez à vos prédictions un nom unique. Vous pouvez également fournir une description pour enregistrer toute note pertinente.

\![]({% image_buster /assets/img/purchasePrediction/purchases_step1.png %})

{: start="3"}
3\. Cliquez sur **Suivant** pour passer à l'étape suivante. <br><br>En option, vous pouvez cliquer sur **Créer maintenant** pour utiliser tous les paramètres par défaut et passer à la dernière étape de la création. Vous aurez la possibilité de revoir les paramètres avant de lancer le processus de création. Vous pouvez également revenir plus tard à n'importe quelle étape en cliquant sur celle-ci dans la barre supérieure.

## Étape 2 : Spécifier le suivi des événements {#event-tracking}

Indiquez si les événements de vos utilisateurs sont stockés dans Braze en tant qu' [événements d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) ou [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

Ici, vous verrez si la méthode sélectionnée fournit suffisamment de données pour que Braze puisse créer un modèle de machine learning. Si la condition n'est pas remplie, essayez de sélectionner l'autre méthode de journalisation si elle est également utilisée par votre application. Malheureusement, si ce n'est pas le cas, Braze n'est pas en mesure de créer une prédiction avec la quantité de données disponibles. Si vous pensez que cette erreur est erronée, contactez votre gestionnaire de satisfaction client.

#### Fenêtre d'événement

La fenêtre d'événement est le laps de temps dans lequel vous souhaitez prédire si un utilisateur effectuera l'événement. Il peut être fixé jusqu'à 60 jours. Cette fenêtre permet d'interroger les données historiques pour l'apprentissage des prédictions. En outre, une fois que la prédiction est créée et que les utilisateurs reçoivent des scores, le score de probabilité indique dans quelle mesure un utilisateur est susceptible de réaliser l'événement dans le nombre de jours spécifié par la fenêtre d'événement.

### Étape 3 : Filtrez votre audience de prédictions (facultatif) {#audience}

Votre audience de prédictions est le groupe d'utilisateurs dont vous souhaitez prédire le score de probabilité. Si vous le souhaitez, vous pouvez effectuer une prédiction sur l'ensemble de votre population d'utilisateurs. Pour ce faire, laissez l'option par défaut **Tous les utilisateurs** sélectionnée.

En fonction de votre cas d'utilisation, vous pouvez utiliser des filtres pour spécifier les utilisateurs que vous souhaitez évaluer pour le modèle. Pour ce faire, sélectionnez **Définir ma propre audience de prédictions** et choisissez vos filtres d'audience. Par exemple, vous pourriez vouloir vous concentrer sur les utilisateurs qui utilisent votre application depuis au moins 30 jours en sélectionnant le filtre "Première utilisation de l'application" réglé sur 30 jours. La configuration de cette audience indique à Braze que vous souhaitez que votre modèle apprenne spécifiquement des utilisateurs qui (au moment où le modèle s'exécute) ont utilisé l'application pendant au moins 30 jours.

L'audience de prédiction définit le groupe d'utilisateurs que le modèle de machine learning examine pour tirer des enseignements du passé. Braze vous indiquera la taille estimée de votre audience de prédictions. Si vous spécifiez l'audience souhaitée et que vous n'atteignez pas le minimum requis pour exécuter le modèle, essayez de spécifier un filtre plus large ou utilisez l'option **Tous les utilisateurs.**  Gardez à l'esprit que de nombreux cas d'utilisation ne nécessitent pas que vous sélectionniez une audience de prédictions spécifique. Par exemple, si votre cas d'utilisation consiste à cibler les utilisateurs de la région UE qui sont les plus susceptibles de se désabonner, vous pouvez exécuter votre modèle sur tous les utilisateurs, puis inclure un filtre pour la région UE dans le segment de la campagne.

{% alert note %}
L'audience des prédictions ne peut dépasser 100 millions d'utilisateurs.
{% endalert %}

Lorsque la fenêtre d'événement est de 14 jours ou moins, la fenêtre temporelle pour les filtres qui commencent par "Dernier..." comme "Dernière application utilisée" et "Dernier achat effectué" **ne peut pas dépasser la fenêtre d'événement spécifiée dans le [suivi des événements.](#event-tracking)** Par exemple, si la fenêtre d'événement est définie sur 14 jours, la fenêtre temporelle pour les filtres "Dernier..." ne peut pas dépasser 14 jours.

#### Mode filtrage complet

Afin de créer immédiatement une nouvelle prédiction, seul un sous-ensemble de filtres de segmentation de Braze est pris en charge. Le mode filtrage complet vous permet d'utiliser tous les filtres Braze mais nécessite une fenêtre d'événement pour créer la prédiction. 

Par exemple, si la fenêtre d'événement est définie sur 14 jours, il faudra 14 jours pour collecter les données utilisateur et créer la prédiction lors de l'utilisation de filtres uniquement pris en charge en mode filtrage complet. En outre, certaines estimations concernant la taille des audiences ne seront pas disponibles en mode filtrage complet.

### Étape 4 : Choisissez la planification de la mise à jour

Le modèle d'apprentissage automatique générera des scores de probabilité d'événement pour les utilisateurs, et ces scores seront mis à jour en fonction de la planification que vous sélectionnez ici. Vous pourrez cibler les utilisateurs en fonction de leur score de probabilité d'événement. 

Sélectionnez la **fréquence maximale des mises à jour** que vous jugerez utile. Par exemple, si vous prévoyez des prédictions d'achats et que vous envisagez d'envoyer une promotion hebdomadaire, réglez la fréquence de mise à jour sur **Hebdomadaire** au jour et à l'heure de votre choix.

{% alert note %}
Les prédictions de prévisualisation et de démonstration ne mettront jamais à jour les scores de vraisemblance des utilisateurs.
{% endalert %}

### Étape 5 : Créer des prédictions

Vérifiez que les informations que vous avez fournies sont correctes, puis choisissez **Créer une prédiction**. Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Enregistrer comme brouillon** pour revenir à cette page et créer le modèle ultérieurement. 

Une fois que vous avez cliqué sur **Créer une prédiction**, le processus qui génère le modèle commence. Cette opération peut prendre de 30 minutes à quelques heures, en fonction du volume des données. Pour cette prédiction, vous verrez une page expliquant que la formation est en cours pour la durée du processus de création du modèle. Le modèle de Braze prend en compte les événements personnalisés, les événements d'achat, les événements d'interaction avec la campagne et les données de session.

Une fois terminé, la page basculera automatiquement vers la vue analyse/analytique et vous recevrez un e-mail vous informant que la prédiction et les résultats sont prêts. En cas d'erreur, la page revient au mode modification avec une explication de ce qui s'est passé.

La prédiction sera automatiquement reconstruite ("réentraînée") toutes les **deux semaines** afin de la maintenir à jour sur la base des données les plus récentes disponibles. Notez qu'il s'agit d'un processus distinct de la production des scores de vraisemblance des utilisateurs, qui constituent le résultat de la prédiction. Cette dernière est déterminée par la fréquence de mise à jour que vous avez choisie à l'étape 4.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction non archivée continuera à mettre à jour les scores des utilisateurs selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.


