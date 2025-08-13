---
nav_title: "Création d'une prédiction d'événement"
article_title: "Création d'une prédiction d'événement"
page_order: 1.1
description: "Cet article explique comment créer une prédiction d'événement dans le tableau de bord de Braze."

---

# Création d'une prédiction d'événement

> Une prédiction est une instance d'un modèle d'apprentissage automatique formé et de tous les paramètres et données qu'il utilise. Pour en savoir plus sur les prédictions, consultez l'[aperçu des prédictions]({{site.baseurl}}/user_guide/brazeai//predictive_events/).

Dans Braze, sélectionnez **Analyse** > **Événements prévisionnels**.

Sur cette page, vous trouverez une liste des prédictions d'événements actifs actuels et quelques informations de base à leur sujet. Vous pouvez y renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores utilisateur.

## Étape 1 : Créer une nouvelle prédiction

1. Choisissez **Créer une prédiction** et sélectionnez une nouvelle **prédiction d'événement.**

{% alert note %}
Le nombre de prédictions actives simultanément est limité à cinq. Avant d'acheter les événements prédictifs, la limite est d'une unique prévisualisation de prédiction active. Une prédiction préalable n'actualisera pas régulièrement les scores ou ne ciblera pas les utilisateurs en fonction des résultats de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

{: start="2"}
2\. Donnez à vos prédictions un nom unique. Vous pouvez également fournir une description pour enregistrer des remarques pertinentes.

![]({% image_buster /assets/img/purchasePrediction/purchases_step1.png %})

{: start="3"}
3\. Cliquez sur **Suivant** pour passer à l'étape suivante. <br><br>En option, vous pouvez cliquer sur **Créer maintenant** pour utiliser tous les paramètres par défaut et passer à la dernière étape de la création. Vous aurez la possibilité d’examiner les paramètres avant de commencer le processus de création. Vous pouvez également revenir plus tard à n’importe quelle étape en cliquant dessus dans la barre supérieure.

## Étape 2 : Spécifier le suivi des événements {#event-tracking}

Indiquez si les événements de vos utilisateurs sont stockés dans Braze en tant qu' [événements d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) ou [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

Ici, vous verrez si la méthode sélectionnée fournit suffisamment de données pour que Braze puisse créer un modèle de machine learning. Si l’exigence n’est pas satisfaite, essayez de sélectionner l’autre méthode d’enregistrement si elle est également utilisée par votre application. Malheureusement, si ce n'est pas le cas, Braze n'est pas en mesure de créer une prédiction avec la quantité de données disponibles. Si vous pensez que cette erreur n’a pas lieu d’être, contactez votre gestionnaire de la satisfaction client.

#### Fenêtre d'événement

La fenêtre d'événement est le laps de temps dans lequel vous souhaitez prédire si un utilisateur effectuera l'événement. Elle peut être réglée sur 60 jours. Cette fenêtre permet d'interroger les données historiques pour l'apprentissage des prédictions. En outre, une fois que la prédiction est créée et que les utilisateurs reçoivent des scores, le score de probabilité indique dans quelle mesure un utilisateur est susceptible de réaliser l'événement dans le nombre de jours spécifié par la fenêtre d'événement.

### Étape 3 : Filtrez votre audience de prédictions (facultatif) {#audience}

Votre audience de prédictions est le groupe d'utilisateurs dont vous souhaitez prédire le score de probabilité. Si vous le souhaitez, vous pouvez effectuer une prédiction sur l'ensemble de votre population d'utilisateurs. Pour ce faire, laissez l'option par défaut **Tous les utilisateurs** sélectionnée.

Le modèle est généralement plus performant si vous filtrez les utilisateurs que vous souhaitez évaluer à l'aide de certains critères. Pour ce faire, sélectionnez **Définir ma propre audience de prédictions** et choisissez vos filtres d'audience. Par exemple, vous souhaiterez peut-être vous concentrer sur les utilisateurs qui utilisent votre application depuis au moins 30 jours en réglant le filtre « A utilisé l’app pour la première fois » sur 30 jours.

La définition de l'audience de prédictions est également utilisée pour interroger les données historiques afin de permettre au modèle de machine learning d'apprendre du passé. Comme à la page précédente, la quantité de données fournies par ces filtres est affichée ainsi que l’exigence. Si vous spécifiez l'audience souhaitée et n'atteignez pas le minimum requis, essayez de spécifier un filtre plus large ou utilisez l'option **Tous les utilisateurs**.

{% alert note %}
L'audience des prédictions ne peut dépasser 100 millions d'utilisateurs.
{% endalert %}

Lorsque la fenêtre de prédiction est de 14 jours ou moins, la fenêtre temporelle pour les filtres qui commencent par « Dernier… », tels que « Dernière utilisation de l’application » et « Dernier achat effectué », **ne peuvent pas dépasser la fenêtre de prédiction définie dans le [suivi des événements](#event-tracking)**. Par exemple, si la fenêtre d’événement est définie sur 14 jours, la fenêtre temporelle pour les filtres « Dernier… » ne peut pas dépasser 14 jours.

#### Mode de filtrage complet

Afin de créer immédiatement une nouvelle prédiction, seul un sous-ensemble de filtres de segmentation de Braze est pris en charge. Le mode filtrage complet vous permet d'utiliser tous les filtres Braze mais nécessite une fenêtre d'événement pour créer la prédiction. 

Par exemple, si la fenêtre d'événement est définie sur 14 jours, il faudra 14 jours pour collecter les données utilisateur et créer la prédiction lors de l'utilisation de filtres uniquement pris en charge en mode filtrage complet. En outre, certaines estimations concernant la taille des audiences ne seront pas disponibles en mode filtrage complet.

### Étape 4 : Choisissez la planification de la mise à jour

Le modèle de machine learning créé lorsque vous remplissez cette page sera utilisé selon une planification que vous sélectionnez ici, pour générer de nouveaux scores de probabilité des utilisateurs de réaliser l'événement (score de vraisemblance). Sélectionnez la **fréquence maximale des mises à jour** que vous jugerez utile. Par exemple, si vous prévoyez des prédictions d'achats et que vous envisagez d'envoyer une promotion hebdomadaire, réglez la fréquence de mise à jour sur **Hebdomadaire** au jour et à l'heure de votre choix.

{% alert note %}
Les prédictions de prévisualisation et de démonstration ne mettront jamais à jour les scores de vraisemblance des utilisateurs.
{% endalert %}

### Étape 5 : Créer la prédiction

Vérifiez que les informations que vous avez fournies sont correctes, puis choisissez **Créer la prédiction**. Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Enregistrer comme brouillon** pour revenir à cette page et créer le modèle ultérieurement. 

Une fois que vous avez cliqué sur **Créer une prédiction**, le processus qui génère le modèle commence. Cela peut prendre entre 30 minutes et quelques heures en fonction du volume de données. Pour cette prédiction, vous verrez une page expliquant que la formation est en cours pour la durée du processus de création du modèle.

Une fois terminé, la page basculera automatiquement vers la vue analyse/analytique et vous recevrez un e-mail vous informant que la prédiction et les résultats sont prêts. En cas d’erreur, la page revient en mode Édition avec une explication de ce qui s’est mal passé.

La prédiction sera automatiquement reconstruite ("réentraînée") toutes les **deux semaines** afin de la maintenir à jour sur la base des données les plus récentes disponibles. Notez qu'il s'agit d'un processus distinct de la production des scores de vraisemblance des utilisateurs, qui constituent le résultat de la prédiction. Ces derniers sont déterminés par la fréquence de mise à jour que vous avez choisie à l’étape 4.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction non archivée continuera à mettre à jour les scores des utilisateurs selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.


