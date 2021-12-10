---
nav_title: Créer une prédiction d'achat
article_title: Créer une prédiction d'achat
page_order: 1
description: "Cet article explique comment créer une prédiction d'achat dans le tableau de bord de Braze."
---

# Créer une prédiction d'achat

Sur la barre de navigation gauche du tableau de bord Braze, choisissez la page __Prédictions__. Une prédiction est une instance d'un modèle d'apprentissage automatique formé et de tous les paramètres et données qu'il utilise. Sur cette page, vous verrez une liste des prédictions actives actuelles et des informations de base à leur sujet. Ici vous pouvez renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores des utilisateurs.

Pour créer une nouvelle prédiction, choisissez __Créer une prédiction__ dans le coin supérieur droit et sélectionnez un nouveau __Achat prédiction__.

{% alert note %}
Il y a une limite de 3 prédictions d'achat actives simultanément. Avant d'acheter des achats prévisionnels, la limite est une prédiction d'achat d'aperçu active. Une prévision d'achat d'aperçu ne mettra pas régulièrement à jour les scores ou les utilisateurs ciblés en fonction de la sortie de la prédiction. Contactez votre responsable de compte pour plus de détails.
{% endalert %}

## Étape 1 : Créer une nouvelle prédiction

!\[Acheter 1\]\[1\]

Sur la première page, donnez à votre nouvelle prédiction un nom unique. Vous pouvez également fournir une description pour enregistrer les notes pertinentes.

Cliquez sur __Avancer__ pour passer à l'étape suivante. En option, vous pouvez cliquer sur __Build Now__ pour utiliser tous les paramètres par défaut et passer à la dernière étape de la création. Vous aurez une chance de vérifier les paramètres avant de commencer le processus de construction. De plus, vous pouvez revenir à n'importe quelle étape plus tard en cliquant dessus dans la barre supérieure.

## Étape 2 : Spécifiez le suivi des achats

Sur cette page, spécifiez si les achats de vos utilisateurs sont stockés dans Braze comme des [événements d'achat standard](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/purchase_events/) ou [événements personnalisés](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events/).

Ici, vous verrez si la méthode d'achat sélectionnée fournit suffisamment de données pour que Braze puisse créer un modèle d'apprentissage automatique. Si la condition n'est pas remplie, essayez de sélectionner l'autre méthode de journalisation si elle est également utilisée par votre application. Malheureusement, si ce n'est pas le cas, Braze n'est pas en mesure de créer une prédiction avec la quantité de données disponibles. Si vous pensez que vous ne voyez pas correctement cette erreur, veuillez contacter votre CSM.

### Étape 3 : Filtrer votre audience de prédiction (facultatif) {#audience}

Votre audience de prédiction est le groupe d'utilisateurs dont vous aimeriez prédire la probabilité d'achat. Achat anticipé vous permet d'exécuter une prédiction sur toute votre population d'utilisateurs. Pour ce faire, laissez l'option par défaut __Tous les utilisateurs__ sélectionnée.

Le modèle sera probablement plus performant si vous filtrez les utilisateurs que vous voulez évaluer à l'aide de certains critères. Pour ce faire, sélectionnez __Définir mon propre public de prédiction__ et choisissez vos filtres d'audience. Par exemple, vous pouvez vous concentrer sur les utilisateurs qui utilisent votre application depuis au moins 30 jours en sélectionnant le filtre "première application utilisée" à 30 jours.

La définition de l’Audience prédictive est également utilisée pour interroger les données historiques afin de permettre au modèle d’apprentissage automatique d’apprendre du passé. Simulaire à la page précédente, la quantité de données fournies par ces filtres est affichée avec la demande. Si vous spécifiez votre audience désirée et que vous ne remplissez pas le minimum, essayez de spécifier un filtre plus large ou utilisez l'option __Tous les utilisateurs__.

{% alert note %}
L'audience de prédiction ne peut excéder 100 millions d'utilisateurs.
{% endalert %}

Pour les filtres qui commencent par "Last... comme "Dernière application utilisée" et "Dernier achat effectué", la fenêtre de temps pour regarder en arrière pour ces filtres __ne peut pas excéder 16 jours__.

### Étape 4 : Choisissez la fréquence de mise à jour

Le modèle d'apprentissage automatique créé lorsque vous complétez cette page sera utilisé sur un horaire que vous sélectionnez ici, pour générer de nouveaux scores de probabilité d'achat des utilisateurs. Veuillez sélectionner la __fréquence maximale de mises à jour__ que vous trouverez utile. Par exemple, si vous allez envoyer une promotion hebdomadaire pour empêcher les utilisateurs d’acheter, réglez la fréquence de mise à jour sur __Hebdomadaire__ le jour et l'heure de votre choix.

{% alert note %}
Les prédictions de prévisualisation et de démonstration ne mettront jamais à jour les probabilités d'achat des utilisateurs.
{% endalert %}

### Étape 5 : Construire la prédiction

Vérifiez que les détails que vous avez fournis sont corrects, et choisissez __Build Prediction__. Vous pouvez également enregistrer vos modifications dans le formulaire brouillon en sélectionnant __Enregistrer comme brouillon__ pour revenir à cette page et construire le modèle plus tard. Une fois que vous cliquez sur __Build Prediction__, le processus qui génère le modèle va commencer. Cela peut prendre entre 30 minutes et quelques heures, selon les volumes de données. Pour cette prédiction, vous verrez une page expliquant que la formation est en cours pour la durée du processus de construction du modèle.

Une fois terminée, la page passera automatiquement à la vue analytique, et vous recevrez également un courriel vous informant que la Prédiction et les résultats sont prêts. En cas d'erreur, la page retournera au mode d'édition avec une explication de ce qui s'est mal passé.

La prédiction sera reconstruite ("reformée") toutes les __deux semaines automatiquement__ pour la tenir à jour sur les données les plus récentes disponibles. Notez que ce processus est séparé du moment où les points de probabilité d'achat des utilisateurs, la sortie de la prédiction, sont produits. Cette dernière est déterminée par la fréquence de mise à jour que vous avez choisie à l'étape 4.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction archivée qui est désarchivée continuera à mettre à jour les scores des utilisateurs selon son calendrier prédéterminé. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.
[1]: {% image_buster /assets/img/purchasePrediction/purchases_step1.png %}

