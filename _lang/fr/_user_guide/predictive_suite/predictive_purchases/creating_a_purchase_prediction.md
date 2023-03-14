---
nav_title: Créer une prédiction d’achat
article_title: Créer une prédiction d’achat
page_order: 1
description: "Le présent article explique comment créer une prédiction d’achat dans le tableau de bord de Braze."

---

# Créer une prédiction d’achat

Depuis la barre de navigation de gauche sur le tableau de bord de Braze, choisissez la page **Predictions (Prédictions)**. Une prédiction est une instance d’un modèle de machine learning entraîné et de tous les paramètres et données qu’il utilise. Sur cette page, vous verrez une liste des prédictions actuellement actives et des informations de base à leur sujet. Vous pouvez renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores utilisateur. 

Pour créer une nouvelle prédiction, choisissez **Create Prediction (Créer une prédiction)** et sélectionnez une nouvelle **Purchase Prediction (Prédiction d’achat)**.

{% alert note %}
Il y existe une limite de cinq prédictions d’achat actives simultanément. Avant d’acquérir les Achats prédictifs, la limite est d’une unique prévisualisation de prédiction d’achat active. Un aperçu de prédiction d’achat n’actualisera pas régulièrement les scores ni ne vous permettra de cibler les utilisateurs sur la base des résultats de la prévision. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

## Étape 1 : Créer une nouvelle prédiction

![][1]

Sur la première page, donnez un nom unique à votre nouvelle prédiction. Vous pouvez également fournir une description pour enregistrer des remarques pertinentes.

Cliquez sur **Forward (Avancer)** pour passer à l’étape suivante. Facultativement, vous pouvez cliquer sur **Build Now (Construire maintenant)** pour utiliser tous les paramètres par défaut et passer à la dernière étape de création. Vous aurez la possibilité d’examiner les paramètres avant de commencer le processus de construction. Vous pouvez également revenir plus tard à n’importe quelle étape en cliquant dessus dans la barre supérieure. 

## Étape 2 : Spécifier le suivi des achats

Sur cette page, spécifiez si les achats de vos utilisateurs sont enregistrés dans Braze en tant qu’[événements d’achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) standard ou en tant qu’[événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/).

Ici, vous verrez si la méthode d’achat sélectionnée fournit suffisamment de données pour que Braze crée un modèle de machine learning. Si l’exigence n’est pas satisfaite, essayez de sélectionner l’autre méthode d’enregistrement si elle est également utilisée par votre application. Malheureusement, si ce n’est pas le cas, Braze n’est pas en mesure de créer une prédiction avec la quantité de données disponibles. Si vous pensez que vous n’auriez pas dû voir cette erreur, contactez votre CSM.

#### Fenêtre de prédiction

La fenêtre de prédiction est la période durant laquelle vous souhaitez prévoir si un utilisateur va effectuer un achat. Elle peut être réglée sur 60 jours. Cette fenêtre permet de rechercher des données historiques pour entraîner la prédiction. De plus, une fois que la prédiction est créée et que les utilisateurs reçoivent des scores, le « Purchase Likelihood Score » (Score de probabilité d’achat) indique la probabilité qu’un utilisateur achète durant le nombre de jours spécifiés par la fenêtre de prédiction.

### Étape 3 : Filtrer votre audience de prédiction (facultatif) {#audience}

Votre audience de prédiction est le groupe d’utilisateurs dont vous souhaitez prédire la probabilité d’achat. La prédiction d’achat vous permet d’exécuter une prédiction sur toute la population d’utilisateurs. Pour ce faire, gardez sélectionnée l’option par défaut **All Users (Tous les utilisateurs)**.

Le modèle fonctionnera probablement mieux si vous filtrez les utilisateurs que vous souhaitez évaluer avec certains critères. Pour ce faire, sélectionnez **Define my own prediction audience (Définir ma propre audience de prédiction)** et choisissez vos filtres d'audience. Par exemple, vous souhaiterez peut-être vous concentrer sur les utilisateurs qui utilisent votre application depuis au moins 30 jours en réglant le filtre « A utilisé l’app pour la première fois » sur 30 jours. 

La définition de l’audience de prédiction est également utilisée pour interroger les données historiques afin de permettre au modèle de machine learning d’apprendre du passé. Comme à la page précédente, la quantité de données fournies par ces filtres est affichée ainsi que l’exigence. Si vous spécifiez l’audience souhaitée et n’atteignez pas le minimum, essayez de spécifier un filtre plus large ou utilisez l’option **Tous les utilisateurs**.

{% alert note %}
L’audience de prédiction ne peut pas dépasser 100 millions d’utilisateurs.
{% endalert %}

Lorsque la fenêtre de prédiction est de 14 jours ou moins, la fenêtre temporelle pour les filtres qui commencent par « Dernière… » tels que « Dernière utilisation de l’application » et « Dernier achat effectué » **ne peuvent pas dépasser la fenêtre de prédiction définie dans le suivi de l’événement d’achat**. Par exemple, si la fenêtre de prédiction est définie sur 14 jours, la fenêtre temporelle pour les filtres « Dernier… » ne peut pas dépasser 14 jours.

#### Mode de filtrage complet

Afin de créer une nouvelle prédiction immédiatement, seul un sous-ensemble de filtres de segmentation Braze est pris en charge. Le Mode de filtrage complet vous permet d’utiliser tous les filtres Braze, mais nécessite une « Prediction Window » (Fenêtre d’achat) pour créer la prédiction. Par exemple, si la « Fenêtre d’achat » est définie sur 14 jours, il faudra 14 jours pour collecter les données utilisateur et construire la prédiction lorsque vous utilisez des filtres uniquement pris en charge en Mode de filtrage complet. En outre, certaines estimations sur les tailles d’audience ne seront pas disponibles en Mode de filtrage complet.

### Étape 4 : Choisir la fréquence de mise à jour

Le modèle de machine learning créé lorsque vous remplissez cette page sera utilisé selon une planification que vous sélectionnez ici pour générer de nouveaux scores de probabilité d’achat de vos utilisateurs. Sélectionnez la **fréquence maximale des mises à jour** que vous trouvez utile. Par exemple, si vous allez envoyer une promotion hebdomadaire pour inciter les utilisateurs à acheter, définissez la fréquence de mise à jour sur **Hebdomadaire** au jour et à l’heure de votre choix. 

{% alert note %}
Les prévisualisations et les démonstrations de prédictions ne mettront jamais à jour la probabilité d’achat des utilisateurs. 
{% endalert %}

### Étape 5 : Construire la prédiction

Vérifiez que les détails que vous avez fournis sont corrects et choisissez **Build Prediction (Construire la prédiction)**. Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Save As Draft (Enregistrer en tant que brouillon)** pour revenir à cette page et créer le modèle ultérieurement. Une fois que vous cliquez sur **Build Prediction (Construire la prédiction)**, le processus qui génère le modèle commence. Cela peut prendre entre 30 minutes et quelques heures en fonction du volume de données. Pour cette prédiction, vous verrez une page expliquant que l’entraînement est en cours pendant la durée du processus de construction du modèle.

Une fois qu’il est terminé, la page passera automatiquement à l’affichage de l’analytique et vous recevrez également un e-mail vous informant que la prédiction et les résultats sont prêts. En cas d’erreur, la page revient en mode Édition avec une explication de ce qui s’est mal passé.

La prédiction sera reconstruite (« entraînée ») à nouveau toutes les **deux semaines automatiquement** pour la maintenir à jour sur les données les plus récentes disponibles. Prenez en compte qu’il s’agit d’un processus distinct de celui où les scores de probabilité d’achat des utilisateurs, le résultat de la prédiction, sont produits. Ces derniers sont déterminés par la fréquence de mise à jour que vous avez choisie à l’étape 4.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores utilisateur. Toute prédiction archivée qui est désarchivée continuera à mettre à jour les scores utilisateur selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.

[1]: {% image_buster /assets/img/purchasePrediction/purchases_step1.png %}

