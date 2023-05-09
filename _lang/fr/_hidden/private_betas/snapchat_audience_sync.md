---
nav_title: Synchronisation de l’audience avec Snapchat
article_title: Synchronisation de l’audience Canvas avec Snapchat
description: "Cet article de référence couvre la façon d’utiliser la synchronisation d’audience de Braze vers Snapchat pour fournir des publicités basées sur des déclencheurs comportementaux, des segmentations, etc."
page_order: 4
alias: "/audience_sync_snapchat/"

Outil :
  - Canvas
hidden: true
layout: dev_guide
---

# Synchronisation de l’audience avec Snapchat

En utilisant la synchronisation de l’audience Braze vers Snapchat, les marques peuvent choisir d’ajouter les données utilisateurs à partir de leur intégration Braze aux listes client Snapchat afin de proposer des publicités basées sur des déclencheurs comportementaux, des segmentations, etc. Les critères que vous utilisez généralement pour déclencher un message (notification push, e-mail, SMS, webhook, etc.) dans un Canvas Braze en fonction de vos données utilisateur peuvent maintenant être utilisés pour déclencher une publicité pour cet utilisateur dans vos listes client Snapchat.

**Les cas d’utilisation courants pour synchroniser les audiences comprennent** :

- Cibler des utilisateurs à forte valeur à travers plusieurs canaux pour stimuler les achats ou l’engagement
- Recibler des utilisateurs qui sont moins réactifs aux autres canaux marketing
- Supprimer des audiences pour empêcher les utilisateurs de recevoir des publicités lorsqu’ils sont déjà de fidèles clients de votre marque
- Créer des audiences similaires pour acquérir de nouveaux utilisateurs plus efficacement

Cette fonctionnalité permet aux utilisateurs de contrôler quelles données first-party spécifiques sont partagées avec Snapchat. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont considérées avec le plus grand sérieux. Consultez notre [Politique de confidentialité](https://www.braze.com/privacy) pour plus d’informations.

{% alert important %}
La synchronisation de l’audience avec Snapchat est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la bêta.
{% endalert %}

## Conditions préalables 

Vous devrez vous assurer que les éléments suivants ont été créés et/ou terminés avant de configurer votre synchronisation d’audience dans Snapchat.

| Condition | Origine | Description |
| --- | --- | --- |
| Gestionnaire commercial Snapchat | Snapchat | Un outil centralisé pour gérer les actifs Snapchat de votre marque (p. ex., comptes publicitaires, pages, applications). |
| Compte publicitaire Snapchat | Snapchat | Un compte publicitaire Snapchat actif lié au gestionnaire commercial de votre marque.<br><br>Assurez-vous que l’administrateur du gestionnaire commercial Snapchat vous a donné les autorisations d’administrateur aux comptes publicitaires Snapchat que vous prévoyez d’utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration 

### Étape 1 : Se connecter à Snapchat

Dans le tableau de bord de Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Snapchat**. Dans le module Exportation de l’audience Snapchat, cliquez sur **Connect Snapchat (Connecter Snapchat)**.

![La page des technologies Snapchat dans Braze qui comprend un module Overview et un module d’exportation de l’audience Snapchat avec le bouton Connected Snapchat.][1]{: style="max-width:80%;"}

Vous serez ensuite redirigé vers la page OAuth de Snapchat pour autoriser Braze à obtenir les autorisations liées à votre intégration de synchronisation d’audience.

Après avoir sélectionné Confirmer, vous serez redirigé vers Braze afin de choisir les comptes publicitaires Snapchat à synchroniser. 

![Une liste des comptes publicitaires disponibles que vous pouvez connecter à Snapchat.][2]{: style="max-width:80%;"}

Une fois connecté avec succès, vous serez ramené à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Version mise à jour de la page des partenaires de technologie de Snapchat montrant les comptes publicitaires connectés avec succès.][3]{: style="max-width:80%;"}

Votre connexion à Snapchat sera appliquée au niveau du groupe d’apps dans Braze. Si votre administrateur Snapchat vous retire de votre gestionnaire Snapchat Business ou vous retire l’accès aux comptes publicitaires Snapchat connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvas actifs utilisant Snapchat afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Configurer vos critères d’entrée Canvas

Lorsque vous créez des audiences pour le Suivi des publicités, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent mettre en œuvre les filtres pertinents pour l’éligibilité des utilisateurs dans leurs critères d’entrée Canvas. Nous énumérons quelques options ci-dessous. 

Si vous avez collecté l’[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre **Ads Tracking Enabled (Suivi des publicités activé)**. Sélectionnez la valeur `true` pour envoyer uniquement les utilisateurs vers les destinations de synchronisation d’audience auxquelles ils sont abonnés. 
![][16]{: style="max-width:75%;"}

Si vous recueillez des « abonnements », des « désabonnements », des « Ne pas vendre ou partager » ou tout autre attribut personnalisé pertinent, vous devez les inclure dans vos critères d’entrée Canvas comme filtre :

![Un Canvas avec une audience d’entrée de « opted_in_marketing » correspond à « true ».][13]{: style="max-width:75%;"}

### Étape 3 : Ajouter une étape de synchronisation de l’audience avec Snapchat

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync (Synchronisation d’audience)**.

![Flux de travail des étapes précédentes pour ajouter un composant Snapchat Audience dans Canvas Flow.][4]{: style="max-width:60%;"}

![Flux de travail des étapes précédentes pour ajouter un composant Snapchat Audience dans Canvas Flow.][5]{: style="max-width:60%;"}

### Étape 4 : Configurer une synchronisation

Cliquez sur le bouton **Custom Audience (Audience personnalisée)** pour ouvrir l’éditeur de composant. Sélectionnez Snapchat comme partenaire de synchronisation d’audience souhaité. 

Sélectionnez ensuite votre compte publicitaire Snapchat souhaité. Sous le **menu déroulant Choose a New or Existing Audience (Choisir une nouvelle audience ou une audience existante)**, saisissez le nom d’une nouvelle audience ou d’une audience existante.

{% tabs %}
{% tab Create a New Audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience personnalisée, sélectionnez **Add Users to Audience (Ajouter les utilisateurs à l’audience)** et sélectionnez les champs que vous souhaitez synchroniser avec Snapchat. Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience (Créer une audience)** en bas de l’éditeur d’étapes.

![Vue agrandie de l’étape Canvas d’audience personnalisée. Le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée ici.]({% image_buster /assets/img/snapchat/snapchat4.png %})

Les utilisateurs seront avertis en haut de l’éditeur d’étapes si l’audience a été créée avec succès ou si des erreurs sont survenues au cours du processus. Les utilisateurs peuvent également revenir à cette audience pour supprimer des utilisateurs plus tard dans le parcours Canvas, car l’audience a été créée en mode ébauche.

![Une alerte qui apparaît lorsqu’une nouvelle audience a été créée dans le composant Canvas.]({% image_buster /assets/img/snapchat/snapchat5.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs en temps quasi réel lorsqu’ils entrent dans le composant Audience Sync.

{% endtab %}
{% tab Sync with an Existing Audience %}
**Synchroniser une audience existante**<br>
Braze permet également d’ajouter des utilisateurs à des audiences de Snapchat pour s’assurer que ces audiences sont à jour. Pour synchroniser une audience existante, saisissez le nom de l’audience dans le menu déroulant et choisissez **Add to the Audience (Ajouter à l’audience)**. Ensuite, Braze ajoutera des utilisateurs en temps quasi réel lorsqu’ils passeront au composant de synchronisation d’audience.

![Vue agrandie de l’étape Canvas d’audience personnalisée. Le compte publicitaire souhaité et l’audience existante sont sélectionnés ici.]({% image_buster /assets/img/snapchat/snapchat6.png %})

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer Canvas

Après avoir configuré votre synchronisation d’audience avec Snapchat, lancez simplement le Canvas ! Une nouvelle audience sera créée, et les utilisateurs qui passent par le composant de synchronisation d’audience seront transférés dans cette audience personnalisée sur Snapchat. Si votre Canvas contient des composants subséquents, vos utilisateurs passeront à l’étape suivante de leur parcours utilisateur.

Vous pouvez afficher l’audience dans Snapchat en accédant à votre compte de gestionnaire des publicités, puis en sélectionnant **Audiences** dans le menu déroulant Assets (Actifs). Sur la page **Audience**, vous pouvez voir la taille de chaque audience après avoir atteint environ 1 000 personnes.

![Détails d’audience pour une audience Snapchat donnée qui comprennent le nom d’audience, le type d’audience, la taille de l’audience et la rétention d’audience en jours.][9]

## Considérations relatives à la synchronisation des utilisateurs et aux limites de débit

À mesure que les utilisateurs atteignent l’étape de synchronisation de l’audience, Braze synchronisera ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l’API de Snapchat. Concrètement, Braze essaiera de classer et de traiter autant d’utilisateurs que possible toutes les cinq secondes avant d’envoyer ces utilisateurs vers Snapchat.

La limitation du débit de l’API de Snapchat ne doit pas dépasser dix requêtes par seconde et 100 000 utilisateurs par demande. Si un client Braze atteint ces limites de débit, le Canvas Braze tentera à nouveau d’effectuer la synchronisation pendant un délai d’environ 13 heures maximum. Si la synchronisation n’est pas possible, ces utilisateurs sont répertoriés dans l’indicateur Utilisateurs en erreur.

### Comprendre les analyses

Le tableau suivant contient des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation de l’audience.

| Indicateur | Description |
| --- | --- |
| Saisie | Nombre d’utilisateurs qui ont entré ce composant à synchroniser avec Snapchat. |
| Poursuivre vers l’étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un ? Tous les utilisateurs avanceront automatiquement s’il s’agit de la dernière étape de la branche Canvas. |
| Utilisateurs synchronisés | Nombre d’utilisateurs ayant réussi à se synchroniser avec Snapchat. |
| Utilisateurs non synchronisés | Nombre d’utilisateurs qui n’ont pas été synchronisés en raison de champs manquants à faire correspondre. |
| Utilisateurs en attente | Nombre d’utilisateurs en cours de traitement par Braze et en attente de synchronisation sur Snapchat. |
| Utilisateurs en erreur | Nombre d’utilisateurs qui n’ont pas été synchronisés avec Snapchat en raison d’une erreur d’API après 13 heures de tentatives infructueuses. Les causes d’erreurs potentielles peuvent inclure un jeton Snapchat non valide ou le fait que l’audience personnalisée ait été supprimée de Snapchat. |
| Sortis de Canvas | Nombre d’utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d’un Canvas est un composant de synchronisation d’audience. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Rappelez-vous que les indicateurs sur les utilisateurs synchronisés et les utilisateurs en erreur seront signalées en retard en raison du vidage en vrac et des nouvelles tentatives sur une période de 13 heures, respectivement.
{% endalert %}   

## Résolution des problèmes

{% details Que dois-je faire ensuite si je reçois une erreur de jeton non valide ? %}
Vous pouvez déconnecter et reconnecter votre compte Snapchat sur la page Partenaire de Snapchat. Assurez-vous que votre administrateur du gestionnaire commercial Snapchat dispose des autorisations appropriées sur le compte publicitaire que vous souhaitez synchroniser.
{% enddetails %}

{% details Pourquoi mon Canvas n’est-il pas autorisé à être lancé ? %}
Assurez-vous que votre compte publicitaire Snapchat se connecte avec succès à Braze sur la page partenaire de Snapchat. Assurez-vous que vous avez sélectionné un compte publicitaire, saisi le nom de la nouvelle audience et que les champs sélectionnés correspondent
{% enddetails %}

{% details Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transféré à Snapchat ? %}
Snapchat ne fournit pas cette information de ses politiques de confidentialité des données.
{% enddetails %}

{% details Combien d’audiences Snapchat peut-il prendre en charge ? %}
Pour le moment, vous ne pouvez avoir que 1 000 audiences sur votre compte Snapchat. 
Si vous ne respectez pas cette limite, Braze vous informera que nous ne pouvons pas créer de nouvelles audiences. 
Vous devrez accéder à votre compte de publicités Snapchat et supprimer les audiences que vous n’utilisez plus. 
{% enddetails %}

[1]: {% image_buster /assets/img/snapchat/snapchat1.png %}
[2]: {% image_buster /assets/img/snapchat/snapchat2.png %}
[3]: {% image_buster /assets/img/snapchat/snapchat3.png %}
[6]: {% image_buster /assets/img/snapchat/snapchat4.png %}
[7]: {% image_buster /assets/img/snapchat/snapchat5.png %}
[8]: {% image_buster /assets/img/snapchat/snapchat6.png %}
[9]: {% image_buster /assets/img/snapchat/snapchat7.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
