---
nav_title: Snapchat
article_title: "Synchronisation de l'audience de Canvas sur Snapchat"
description: "Cet article de référence vous explique comment synchroniser l’audience Braze avec Snapchat, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 6
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas

---

# Synchronisation de l'audience avec Snapchat

Grâce à la synchronisation de l'audience Braze avec Snapchat, les marques peuvent ajouter les données utilisateurs de leur intégration Braze aux listes de clients Snapchat pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tous les critères que vous utiliseriez normalement pour déclencher un message (push, e-mail, SMS, webhook, etc.) dans un Braze Canvas sur la base de vos données utilisateur peuvent désormais être utilisés pour déclencher une publicité à destination de cet utilisateur dans vos listes de clients Snapchat.

**Les cas d'utilisation courants pour la synchronisation de l'audience incluent :**

- Ciblage des utilisateurs de grande valeur via plusieurs canaux pour stimuler les achats ou l'engagement
- Reciblage des utilisateurs qui réagissent moins aux autres canaux de marketing.
- Créer des audiences de suppression pour empêcher les utilisateurs de recevoir des publicités lorsqu'ils sont déjà des consommateurs fidèles de votre marque
- Créer des audiences de type "lookalike" pour acquérir de nouveaux utilisateurs plus efficacement.

Cette fonctionnalité permet aux utilisateurs de contrôler quelles données first-party spécifiques sont partagées avec Snapchat. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont prises en compte avec la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
L’intégration de l’audience Braze avec Snapchat est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Prérequis 

Vous devez vous assurer que les éléments suivants sont créés, complétés et/ou acceptés avant de configurer votre étape de l'audience Snapchat dans Canvas.

| Exigence | Origine | Descriptif |
| --- | --- | --- |
| Gestionnaire d’affaires Snapchat | Snapchat | Un outil centralisé pour gérer les ressources Snapchat de votre marque (comme les comptes publicitaires, les pages, les apps). |
| Compte publicitaire Snapchat | Snapchat | Un compte publicitaire Snapchat actif lié au gestionnaire de compte Snapchat de votre marque.<br><br>Assurez-vous que votre gestionnaire de compte Snapchat vous a accordé des droits d'administrateur sur les comptes publicitaires Snapchat que vous prévoyez d'utiliser avec Braze. |
| Conditions d'utilisation de Snapchat | [Snapchat](https://www.snap.com/en-US/policies) | Acceptez de vous conformer à tous les termes, politiques, directives et documents requis de Snapchat liés à votre utilisation de Snapchat Audience Sync, y compris tous les termes, politiques, directives et documents qui y sont incorporés par référence, qui peuvent inclure : les conditions de service, les conditions de service commerciales, les conditions des développeurs, Audience Match, les politiques publicitaires, la politique de contenu commercial, les lignes directrices de la communauté et la responsabilité des fournisseurs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration 

### Étape 1 : Se connecter à Snapchat

Dans le tableau de bord de Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Snapchat**. Sous Synchronisation de l'audience Snapchat, sélectionnez **Connecter Snapchat**.

![Page technologique de Snapchat dans Braze qui comprend une section Aperçu et une section Synchronisation de l'audience de Snapchat avec le bouton Snapchat connecté.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

Vous serez ensuite redirigé vers la page OAuth de Snapchat pour autoriser Braze à obtenir les permissions liées à votre intégration de synchronisation d’audience.

Une fois que vous aurez sélectionné confirmer, vous serez redirigé vers Braze pour sélectionner les comptes publicitaires Snapchat que vous souhaitez synchroniser. 

![Liste des comptes publicitaires disponibles que vous pouvez connecter à Snapchat.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

Une fois connecté avec succès, vous serez renvoyé à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Une version mise à jour de la page des partenaires technologiques de Snapchat montrant que les comptes publicitaires se sont connectés avec succès.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Votre connexion Snapchat sera appliquée au niveau de l'espace de travail de Braze. Si votre administrateur Snapchat vous retire de votre gestionnaire de compte Snapchat ou de l'accès aux comptes publicitaires Snapchat connectés, Braze détectera un jeton invalide. Par conséquent, vos canvas actives utilisant Snapchat afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Ajouter une étape de synchronisation de l'audience avec Snapchat

Ajoutez un composant dans votre canvas et sélectionnez **Synchronisation de l’audience**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation

Cliquez sur le bouton **Audience personnalisée** pour ouvrir l'éditeur de composants.

Sélectionnez **TikTok** comme partenaire de synchronisation d'audience.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Sélectionnez ensuite le compte publicitaire Snapchat de votre choix. Dans la liste déroulante **Choisir une audience nouvelle ou existante**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Ajouter des utilisateurs à l'audience** et sélectionnez les champs que vous souhaitez synchroniser avec Snapchat. Ensuite, enregistrez votre audience en cliquant sur le bouton **Créer une audience** en bas de l'éditeur d'étape.

![Vue élargie de l'étape du canvas d’audience personnalisée. Ici, le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Les utilisateurs seront avertis en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent également référencer cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas car l'audience a été créée en mode brouillon.

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant canvas.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Lorsque vous lancez un canvas avec une nouvelle audience, Braze synchronise les utilisateurs quasiment en temps réel lorsqu'ils entrent dans le composant de synchronisation de l’audience.

{% endtab %}
{% tab Synchronisation avec une audience existante %}
**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs aux audiences Snapchat existantes afin de s'assurer que ces audiences sont à jour. Pour effectuer une synchronisation avec une audience existante, saisissez le nom de l'audience dans le menu déroulant et sélectionnez **Ajouter à l'audience**. Braze ajoutera ensuite des utilisateurs en temps quasi réel au fur et à mesure qu'ils entreront dans le composant Audience Sync.

![Vue élargie de l'étape du canvas d’audience personnalisé. Ici, le compte publicitaire souhaité et l'audience existante sont sélectionnés.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer canvas

Une fois que vous avez configuré la synchronisation de votre audience avec Snapchat, lancez le canvas ! Une nouvelle audience sera créée, et les utilisateurs qui passent par l'étape de synchronisation de l'audience seront passés dans cette audience sur Snapchat. Si votre canvas contient des composants ultérieurs, vos utilisateurs passeront à l'étape suivante de leur parcours utilisateur.

Vous pouvez afficher l'audience dans Snapchat en entrant dans votre compte gestionnaire de publicités et en sélectionnant **Audiences** dans la section Actifs de la navigation. Sur la page **Audiences**, vous pouvez voir la taille des audiences dès qu'elles atteignent environ 1 000.

![Détails de l'audience pour une audience Snapchat donnée qui comprend le nom de l'audience, le type d'audience, la taille de l'audience et la rétention de l'audience en jours.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit

Lorsque les utilisateurs atteignent l'étape de synchronisation de l'audience, Braze synchronise ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l'API de Snapchat. En pratique, Braze va essayer de mettre en lot et de traiter autant d'utilisateurs toutes les 5 secondes avant d'envoyer ces utilisateurs à Snapchat.

La limite de débit de l'API de Snapchat stipule qu'il ne faut pas dépasser dix requêtes par seconde et 100 000 utilisateurs par requête. Si un client Braze atteint cette limite de débit, le canvas Braze tentera de synchroniser pendant environ 13 heures maximum. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés sous les indicateurs Users Errored.

### Comprendre les analyses

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation des audiences.

| Indicateurs | Description |
| --- | --- |
| Entré | Nombre d'utilisateurs qui ont saisi ce composant pour être synchronisés avec Snapchat. |
| Procédé à l'étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un ? Tous les utilisateurs avanceront automatiquement si c'est la dernière étape de la branche canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès sur Snapchat. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze en vue d'une synchronisation avec Snapchat. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Snapchat en raison d'une erreur de l'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Snapchat non valide ou la suppression de l’audience sur Snapchat. |
| Sorti de canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un canvas est un composant de synchronisation d'audience. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans la génération du rapport des utilisateurs synchronisés et des indicateurs d’erreurs en raison du vidage en masse et de la période de 13 heures de nouvelles tentatives, respectivement.
{% endalert %}   

## Foire aux questions

### Combien d'audiences Snapchat peut-il prendre en charge ?

Pour l'instant, vous ne pouvez avoir que 1 000 audiences au sein de votre compte Snapchat. 

Si vous dépassez cette limite, Braze vous informera que nous ne pouvons pas créer de nouvelles audiences. Vous devrez supprimer les audiences que vous n'utilisez plus dans votre compte publicitaire Snapchat.

### Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transféré à Snapchat ?

Snapchat ne fournit pas cette information pour ses politiques de confidentialité des données.

### Que dois-je faire ensuite si je reçois une erreur de jeton non valide ?

Vous pouvez déconnecter et reconnecter votre compte Snapchat sur la page partenaire de Snapchat. Confirmez auprès de votre gestionnaire de compte Snapchat que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez vous synchroniser.

### Pourquoi mon Canvas n’est-il pas autorisé à être lancé ?

Assurez-vous que votre compte publicitaire Snapchat se connecte avec succès à Braze sur la page partenaire de Snapchat. Vérifiez que vous avez sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.


