---
nav_title: Synchronisation de l’audience avec Pinterest
article_title: Synchronisation de l’audience Canvas avec Pinterest
description: "Cet article de référence couvre la façon d’utiliser la synchronisation d’audience de Braze vers Pinterest pour fournir des publicités basées sur des déclencheurs comportementaux, des segmentations, etc."
page_order: 4
alias: "/audience_sync_pinterest/"
hidden: true

Outil :
  - Canvas

---

## Synchronisation de l’audience avec Pinterest

En utilisant la synchronisation de l’audience Braze vers Pinterest, les marques peuvent choisir d’ajouter les données utilisateurs à partir de leur intégration Braze aux audiences Pinterest afin de proposer des publicités basées sur des déclencheurs comportementaux, des segmentations, etc. Les critères que vous utilisez généralement pour déclencher un message (notification push, e-mail, SMS, webhook, etc.) dans un Canvas Braze en fonction de vos données utilisateur peuvent maintenant être utilisés pour déclencher une publicité pour cet utilisateur dans vos audiences TikTok.

**Les cas d’utilisation courants pour synchroniser les audiences comprennent** :

- Cibler des utilisateurs à forte valeur à travers plusieurs canaux pour stimuler les achats ou l’engagement
- Recibler des utilisateurs qui sont moins réactifs aux autres canaux marketing
- Supprimer des audiences pour empêcher les utilisateurs de recevoir des publicités lorsqu’ils sont déjà de fidèles clients de votre marque
- Créer des audiences agissant de manière similaire pour acquérir de nouveaux utilisateurs plus efficacement

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Pinterest. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager avec vos données first-party sont considérées avec le plus grand sérieux. Consultez notre [Politique de confidentialité](https://www.braze.com/privacy) pour plus d’informations.

{% alert important %}
La synchronisation de l’audience avec Pinterest est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la bêta.
{% endalert %}

## Conditions préalables 
Vous devrez vous assurer que les éléments suivants ont été créés et/ou terminés avant de configurer votre synchronisation d’audience dans Pinterest.

| Condition | Origine | Description |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Un outil centralisé pour gérer les actifs Pinterest de votre marque (p. ex., comptes publicitaires, pages, applications). |
| Compte publicitaire Pinterest | [Pinterest](https://ads.pinterest.com/) | Un compte publicitaire Pinterest actif lié au Pinterest Business Hub de votre marque.<br><br>Assurez-vous que l’administrateur du gestionnaire Pinterest Business Hub vous a donné les autorisations d’administrateur aux comptes publicitaires Pinterest que vous prévoyez d’utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration 

### Étape 1 : Se connecter à Pinterest

Dans le tableau de bord de Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Pinterest**. Dans la rubrique Exportation d’audience Pinterest, cliquez sur **Connect Pinterest (Connecter Pinterest)**.

![La page des technologies Pinterest dans Braze qui comprend un module Overview et un module d’exportation de l’audience Pinterest avec le bouton Connected Pinterest.][1]{: style="max-width:80%;"}

Vous serez alors redirigé vers la page Pinterest OAuth afin d’autoriser Braze à gérer le compte publicitaire et l’audience.

Après avoir sélectionné Confirmer, vous serez redirigé vers Braze afin de choisir les comptes publicitaires Pinterest à synchroniser. 

![Une liste des comptes publicitaires disponibles que vous pouvez connecter à Pinterest.][2]{: style="max-width:80%;"}

Une fois connecté avec succès, vous serez ramené à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Version mise à jour de la page de partenaire technologique de Pinterest montrant les comptes publicitaires connectés avec succès.][3]{: style="max-width:80%;"}

Votre connexion à Pinterest sera appliquée au niveau du groupe d’apps dans Braze. Si votre administrateur Pinterest vous retire de votre Pinterest Business Hub ou vous retire l’accès aux comptes Pinterest connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvas actifs utilisant des composants d’audience Pinterest afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Ajouter une étape de synchronisation de l’audience avec Pinterest

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync (Synchronisation d’audience)**.

![Flux de travail des étapes précédentes pour ajouter un composant Pinterest Audience dans Canvas Flow.][4]{: style="max-width:50%;"}

![Flux de travail des étapes précédentes pour ajouter un composant Pinterest Audience dans Canvas Flow.][5]{: style="max-width:50%;"}

### Étape 3 : Configurer une synchronisation

Cliquez sur le bouton **Custom Audience (Audience personnalisée)** pour ouvrir l’éditeur de composant. Sélectionnez Pinterest comme partenaire de synchronisation d’audience souhaité. 

Sélectionnez ensuite votre compte publicitaire Pinterest souhaité. Sous le **menu déroulant Choose a New or Existing Audience (Choisir une nouvelle audience ou une audience existante)**, saisissez le nom d’une nouvelle audience ou d’une audience existante.

{% tabs %}
{% tab Create a New Audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience personnalisée, sélectionnez **Add Users to Audience (Ajouter les utilisateurs à l’audience)** et sélectionnez les champs que vous souhaitez synchroniser avec Pinterest. Ensuite, enregistrez votre audience en cliquant sur le bouton **Créer une audience** en bas de l’éditeur d’étapes.

![Vue agrandie de l’étape Audience Canvas personnalisée. Le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée ici.]({% image_buster /assets/img/pinterest/pinterest8.png %})

Les utilisateurs seront avertis en haut de l’éditeur d’étapes si l’audience a été créée avec succès ou si des erreurs sont survenues au cours du processus. Les utilisateurs peuvent également revenir à cette audience pour supprimer des utilisateurs plus tard dans le parcours Canvas, car l’audience a été créée en mode ébauche.

![Une alerte qui apparaît lorsqu’une nouvelle audience a été créée dans le composant Canvas.]({% image_buster /assets/img/pinterest/pinterest9.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs en temps quasi réel lorsqu’ils entrent dans l’étape Audience Sync.
{% endtab %}
{% tab Sync with an Existing Audience %}
**Synchroniser une audience existante**<br>
Braze permet également d’ajouter des utilisateurs à des audiences de Pinterest pour s’assurer que ces audiences sont à jour. Pour synchroniser une audience existante, saisissez le nom de l’audience dans le menu déroulant et choisissez Add to the Audience (Ajouter à l’audience). Ensuite, Braze ajoutera des utilisateurs en temps quasi réel lorsqu’ils passeront à l’étape de synchronisation d’audience.

![Vue agrandie de l’étape Audience Canvas personnalisée. Le compte publicitaire souhaité et l’audience existante sont sélectionnés ici.]({% image_buster /assets/img/pinterest/pinterest10.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer Canvas

Après avoir configuré votre synchronisation d’audience avec Pinterest, lancez le Canvas ! La nouvelle audience sera créée, et les utilisateurs qui passent par le composant de synchronisation d’audience seront transférés dans cette audience personnalisée sur Pinterest. Si votre Canvas contient des composants subséquents, vos utilisateurs passeront ensuite à l’étape suivante de leur parcours utilisateur.

Vous pouvez afficher l’audience dans Pinterest en accédant à votre compte de gestionnaire des publicités, puis sélectionner Audiences dans le menu déroulant Ads (Publicités). Sur la page Audience, vous pouvez voir la taille de chaque audience après avoir atteint environ 100 personnes.

![Détails d’audience pour une audience Pinterest donnée qui comprennent le nom d’audience, l’ID de l’audience, le type d’audience, la taille de l’audience.][11]

## Considérations relatives à la synchronisation des utilisateurs et aux limites de débit

À mesure que les utilisateurs atteignent l’étape de synchronisation de l’audience, Braze synchronisera ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l’API marketing de Pinterest. Concrètement, Braze essaiera de classer et de traiter autant d’utilisateurs que possible toutes les cinq secondes avant d’envoyer ces utilisateurs vers Pinterest.

La limitation du débit de l’API segment de Pinterest ne doit pas dépasser sept requêtes par seconde par utilisateur et 1 900 utilisateurs par demande. Si un client Braze atteint ces limites de débit, le Canvas Braze tentera à nouveau d’effectuer la synchronisation pendant un délai d’environ 13 heures maximum. Si la synchronisation n’est pas possible, ces utilisateurs sont répertoriés dans l’indicateur Utilisateurs en erreur.

## Comprendre les analyses

Le tableau suivant contient des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation de l’audience.

| Indicateur | Description |
| --- | --- |
| Saisie | Nombre d'utilisateurs qui ont entré ce composant à synchroniser avec Pinterest. |
| Poursuivre vers l’étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un ? Tous les utilisateurs avanceront automatiquement s’il s’agit de la dernière étape de la branche Canvas. |
| Utilisateurs synchronisés | Nombre d’utilisateurs ayant réussi à se synchroniser avec Pinterest. |
| Utilisateurs non synchronisés | Nombre d’utilisateurs qui n’ont pas été synchronisés en raison de champs manquants à faire correspondre. |
| Utilisateurs en attente | Nombre d’utilisateurs en cours de traitement par Braze et en attente de synchronisation sur Pinterest. |
| Utilisateurs en erreur | Nombre d’utilisateurs qui n’ont pas été synchronisés avec Pinterest en raison d’une erreur d’API après 13 heures de tentatives infructueuses. Les causes d’erreurs potentielles peuvent inclure un jeton Pinterest non valide ou le fait que l’audience personnalisée ait été supprimée de Pinterest. |
| Sortis de Canvas | Nombre d’utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d’un Canvas est un composant de synchronisation d’audience. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Rappelez-vous que les indicateurs sur les utilisateurs synchronisés et les utilisateurs en erreur seront signalées en retard en raison du vidage en vrac et des nouvelles tentatives sur une période de 13 heures, respectivement.
{% endalert %}   

## Résolution des problèmes
{% details Que dois-je faire ensuite si je reçois une erreur de jeton non valide ? %}
Vous pouvez simplement déconnecter et reconnecter votre compte Pinterest sur la page Partenaire de Pinterest. Assurez-vous que votre administrateur Pinterest Business Hub dispose des autorisations appropriées sur le compte publicitaire que vous souhaitez synchroniser.
{% enddetails %}

{% details Pourquoi mon Canvas n’est-il pas autorisé à être lancé ? %}
Assurez-vous que votre compte Pinterest se connecte avec succès à Braze sur la page partenaire de Pinterest.
Assurez-vous que vous avez sélectionné un compte publicitaire, saisi le nom de la nouvelle audience et que les champs sélectionnés correspondent.
{% enddetails %}

{% details Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transféré à Pinterest ? %}
Pinterest ne fournit pas cette information pour ses propres politiques de confidentialité des données.
{% enddetails %}

{% details Combien de temps faudra-t-il à mes audiences pour se remplir dans Pinterest ? %}
La taille de l’audience sera mise à jour dans les 24 à 48 heures sur la page Audiences dans le gestionnaire d’annonces de Pinterest.
{% enddetails %}

[1]: {% image_buster /assets/img/pinterest/pinterest1.png %}
[2]: {% image_buster /assets/img/pinterest/pinterest2.png %}
[3]: {% image_buster /assets/img/pinterest/pinterest3.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[6]: {% image_buster /assets/img/pinterest/pinterest6.png %}
[7]: {% image_buster /assets/img/pinterest/pinterest7.png %}
[8]: {% image_buster /assets/img/pinterest/pinterest8.png %}
[9]: {% image_buster /assets/img/pinterest/pinterest9.png %}
[10]: {% image_buster /assets/img/pinterest/pinterest10.png %}
[11]: {% image_buster /assets/img/pinterest/pinterest11.png %}
