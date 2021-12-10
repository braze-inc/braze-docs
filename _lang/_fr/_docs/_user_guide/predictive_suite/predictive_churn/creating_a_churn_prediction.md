---
nav_title: Créer une prédiction de la nature
article_title: Créer une prédiction de la nature
description: "Cet article couvre la façon de créer une prédiction de Churchn dans le tableau de bord de Braze"
page_order: 1
---

# Créer une prédiction de la nature

### Étape 1 : Créer une nouvelle prédiction

Sur la barre de navigation gauche du tableau de bord Braze, choisissez la page __Prédictions__. Une prédiction est une instance d'un modèle d'apprentissage automatique formé et de tous les paramètres et données qu'il utilise. Sur cette page, vous verrez une liste des prédictions actives actuelles ainsi que quelques informations de base à leur sujet. Ici vous pouvez renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores des utilisateurs.

Pour créer une nouvelle prédiction, choisissez __Créer une prédiction__ dans le coin supérieur droit et sélectionnez une nouvelle __prédiction de la coque__.

{% alert note %}
Il y a une limite de 3 Églises prédictions simultanément actives. Avant d'acheter une Église prédictive, la limite est une Prévisualisation active de la prédiction. Un aperçu de la prévision ne mettra pas régulièrement à jour les scores ou ne vous permettra pas de cibler les utilisateurs en fonction de la sortie de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

Sur la page Édition, donnez à votre nouvelle prédiction un nom unique.

### Étape 2 : Définir le churn

Dans le panneau __Définition de la coque__ , utilisez les filtres fournis pour définir ce que churn signifie pour votre entreprise. En d'autres termes, qu'est-ce qu'un utilisateur a à faire dans quel délai pour que vous les considériez foulés ? Rappelez-vous que vous n’avez pas besoin d’expliquer quels comportements pourraient précéder churn - seulement ce qui fait de l’utilisateur un utilisateur désagréé. Cela devrait aussi être une description du comportement qu'un utilisateur fait ou ne fait pas à churn par opposition à un attribut qu'il possède. Par exemple, vous pouvez considérer que les utilisateurs qui n'ont pas ouvert votre application depuis 7 jours doivent être abonnés.

Pour implémenter cet exemple, entrez 7 jours dans la fenêtre de temps en haut du panneau.

!\[Churn 1\]\[1\]

Ensuite, utilisez les filtres disponibles pour sélectionner quels comportements dans ce laps de temps constituent une apparition. Dans ce cas, sélectionnez « ne pas » et « démarrer une session ». Vous pouvez combiner d'autres filtres avec "et" et "ou" comme bon vous semble pour créer la définition dont vous avez besoin. Désinstaller, faire ou ne pas faire d’achats, ou exécuter ou ne pas exécuter d’événements personnalisés particuliers sont d’autres filtres qui peuvent être inclus.

Intéressé par certaines définitions potentielles de churn à prendre en considération? Vous trouverez de l'inspiration [ici](#sample-definitions).

### Étape 3 : Filtrer votre audience de prédiction

Votre Audience de Prédiction est le groupe d'utilisateurs que vous voulez cibler pour vous empêcher de tourner. Bien que vous puissiez essayer de prévenir la présence de churn comme défini ci-dessus dans toute votre population d'utilisateurs, le modèle sera probablement plus performant si vous affinez et filtrez le groupe d'utilisateurs que vous voulez éviter de retourner avec certains critères. Pensez aux utilisateurs spécifiques qui veulent le plus pour vous que vous souhaitez conserver et définir ici. Par exemple, vous pourriez vouloir conserver les utilisateurs qui ont utilisé l'application pour la première fois il y a plus d'un mois ou qui ont déjà fait un achat.

{% alert note %}
L'audience de la prédiction ne peut excéder 40 millions d'utilisateurs.
{% endalert %}

Pour les filtres qui commencent par « ... comme Dernier App Utilisé et Dernier Achat, la fenêtre de temps pour regarder en arrière pour ces filtres __ne peut pas excéder 30 jours moins le nombre de jours de la fenêtre spécifiée__ dans la définition de la Churn. Par exemple, si votre définition de Churn a une fenêtre de 14 jours, la fenêtre de temps pour le « Dast ». .” les filtres ne doivent pas excéder 30 - 14 = 16 jours.

Pour une liste d'exemples de définitions d'audience prévisionnelle, consultez nos exemples de définitions au [bas de cette page](#sample-definitions).

### Étape 4 : Choisissez la fréquence de mise à jour pour les prédictions de type Churn

Le modèle d’apprentissage automatique créé lorsque vous complétez cette page sera utilisé sur un calendrier que vous sélectionnez ici pour générer de nouveaux scores de probabilité des utilisateurs à l’effervescence. Veuillez sélectionner la __fréquence maximale de mises à jour__ que vous trouverez utile. Par exemple, si vous allez envoyer une promotion hebdomadaire pour empêcher les utilisateurs de s'absenter, réglez la fréquence de mise à jour sur __Hebdomadaire__ le jour et l'heure de votre choix.

!\[Churn 2\]\[2\]

{% alert note %}
Les prédictions d'aperçu et de démo ne mettront jamais à jour le risque d'apparition des utilisateurs. En outre, les mises à jour quotidiennes des prédictions nécessitent un achat supplémentaire au-delà des mises à jour hebdomadaires ou mensuelles auprès de l’Église prédictive. Pour acheter cette fonctionnalité, contactez votre responsable de compte.
{% endalert %}

### Étape 5 : Construire la prédiction

Vérifiez que les détails que vous avez fournis sont corrects et choisissez __Prédiction de construction__. Vous pouvez également enregistrer vos modifications dans le formulaire brouillon en sélectionnant __Enregistrer comme brouillon__ pour revenir à cette page et construire le modèle plus tard. Une fois que vous cliquez sur __Build Prediction__, le processus qui génère le modèle va commencer. Cela peut prendre entre 30 minutes et quelques heures selon les volumes de données. Pour cette prédiction, vous verrez une page expliquant que la formation est en cours pour la durée du processus de construction du modèle.

Une fois terminée, la page passera à la vue Analytics automatiquement, et vous recevrez également un courriel vous informant que la Prédiction et les résultats sont prêts. En cas d'erreur, la page retournera au mode Édition avec une explication de ce qui s'est mal passé.

La prédiction sera reconstruite ("reformée") toutes les __deux semaines automatiquement__ pour la tenir à jour sur les données les plus récentes disponibles. Notez que ce processus est séparé du moment où les résultats de la prédiction sont produits par les utilisateurs. Cette dernière est déterminée par la fréquence de mise à jour que vous avez choisie à l'étape 4.

## Exemple de définitions d'orthographe et d'audience de prédiction {#sample-definitions}

__Échantillons de définitions__<br>
- « En 7 jours, l'événement personnalisé « Annulation de l'abonnement »<br>
- « En 14 jours, l'événement personnalisé « Épreuve expirée »<br>
- « Dans un délai d'un jour il a été désinstallé. » <br>
- « En 14 jours, il n’y a pas eu d’achat. » <br>

Pour les définitions des Églises que nous avons décrites ci-dessus, il peut y avoir des définitions correspondantes d'Audience de Prédiction :<br>
- __Un abonnement démarré il y a plus de 2 semaines OU un abonnement démarré il y a moins de deux semaines__<br>Vous pouvez créer 2 prédictions dans ce cas, puis envoyer un message aux nouveaux abonnés différemment des abonnés à plus long terme. Vous pourriez également définir ceci comme « premier achat fait il y a plus de 30 jours ».<br>
- __Uninstallers__<br>Vous pouvez vous concentrer sur les clients qui ont acheté quelque chose dans le passé récent ou utilisé l'application très récemment.<br>
- __Ceux qui risquent de ne pas acheter en tant que définition de Churn__<br>Vous pouvez vous concentrer sur les clients qui ont navigué ou recherché ou engagé plus récemment avec votre application. Peut-être que la bonne intervention de réduction empêchera ce groupe plus engagé de s'effondrer.

## Prédictions archivées

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction archivée qui est désarchivée continuera à mettre à jour les scores des utilisateurs selon son calendrier prédéterminé. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.
[1]: {% image_buster /assets/img/churn/churn1.png %} [2]: {% image_buster /assets/img/churn/churn2.png %}

