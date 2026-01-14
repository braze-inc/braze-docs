---
nav_title: Criteo
article_title: canvas audience Synchroniser avec Criteo
description: "Cet article de référence explique comment utiliser la synchronisation d'audience Braze avec Criteo, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 1
alias: /audience_sync_criteo/

Tool:
  - Canvas
---

# audience Synchroniser avec Criteo

Grâce à Braze Audience Sync to Criteo, les marques peuvent choisir d'ajouter les données utilisateurs de leur propre intégration Braze aux listes de clients Criteo afin de diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tous les critères que vous utiliseriez normalement pour déclencher un message (push, e-mail, SMS, webhook, etc.) dans un Braze Canvas sur la base de vos données utilisateur peuvent désormais être utilisés pour déclencher une publicité pour cet utilisateur dans vos listes de clients Criteo.

**Les cas d'utilisation courants pour la synchronisation de l'audience incluent :**

- Ciblage des utilisateurs de grande valeur via plusieurs canaux pour stimuler les achats ou l'engagement
- Recibler des utilisateurs qui sont moins réactifs aux autres canaux marketing
- Créer des audiences de suppression pour empêcher les utilisateurs de recevoir des publicités lorsqu'ils sont déjà des consommateurs fidèles de votre marque
- Créer des audiences similaires pour acquérir de nouveaux utilisateurs plus efficacement

Cette fonctionnalité donne aux marques la possibilité de contrôler quelles données first-party spécifiques sont partagées avec Criteo. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont prises en compte avec la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation des données Braze avec Criteo est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze. <br> 
{% endalert %}

## Conditions préalables 

Vous devrez vous assurer que les éléments suivants ont été créés avant de configurer votre synchronisation d'audience avec Criteo.

| Exigence | Origine | Description |
| --- | --- | --- |
| Compte publicitaire Criteo | [Criteo](https://marketing.criteo.com/) | Un compte publicitaire Criteo actif lié à votre marque.<br><br>Assurez-vous que votre administrateur Criteo vous a accordé les autorisations appropriées pour accéder aux audiences. |
| [Directives publicitaires de Criteo](https://www.criteo.com/advertising-guidelines/)<br>et<br>[Directives de sécurité de la marque Criteo](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | En tant que client actif de Criteo, vous devez vous assurer que vous pouvez respecter les directives de sécurité de la marque et de la publicité de Criteo avant de lancer toute campagne Criteo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration 

### Étape 1 : Connectez-vous à Criteo

Dans le tableau de bord de Braze, allez à **Intégrations de partenaires** > **Partenaires technologiques** et sélectionnez **Criteo**. Sous Exportation de l'audience Criteo, sélectionnez **Connecter Criteo**.

![Page de la technologie Criteo dans Braze qui comprend une section Aperçu et une section Criteo avec le bouton Connected Criteo.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Une page oAuth de Criteo apparaîtra pour autoriser Braze pour les autorisations liées à votre intégration de synchronisation d'audience.

Une fois que vous avez sélectionné confirmer, vous serez alors redirigé vers Braze pour sélectionner les comptes publicitaires Criteo que vous souhaitez synchroniser. 

![Une liste des comptes publicitaires disponibles que vous pouvez connecter à Criteo.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

Une fois que vous vous êtes connecté avec succès, vous serez redirigé vers la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Une version actualisée de la page de partenaires technologiques de Criteo montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Votre connexion Criteo sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur Criteo vous supprime de votre compte publicitaire Criteo, Braze détectera un jeton invalide. En conséquence, vos Canvases actifs utilisant Criteo afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Configurez vos critères d'entrée de canvas

Lors de la création d'audiences pour le suivi des publicités, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la confidentialité, telles que le droit de « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs devraient mettre en œuvre les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée de canvas. Ci-dessous, nous listons quelques options.

Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre Ads Tracking Enabled. Sélectionnez la valeur comme vraie pour n'envoyer les utilisateurs que dans les destinations de synchronisation d'audience où ils ont choisi de participer.

![]({% image_buster /assets/img/criteo/criteo11.png %})

Si vous collectez `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devez les inclure dans les critères d'entrée de votre Canvas en tant que filtre :

![]({% image_buster /assets/img/criteo/criteo12.png %})

Pour en savoir plus sur la manière de se conformer à ces lois sur la protection des données au sein de la plateforme Braze, consultez [Assistance technique à la protection des données]({{site.baseurl}}/dp-technical-assistance/).

### Étape 3 : Ajouter une étape de synchronisation d'audience avec Criteo

Ajoutez un composant dans votre canvas et sélectionnez **Synchronisation de l’audience**.

![Workflow des étapes précédentes pour ajouter un composant Criteo Audience dans Canvas Flow.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Workflow des étapes précédentes pour ajouter un composant Criteo Audience dans Canvas Flow.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### Étape 4 : Configuration de la synchronisation

Cliquez sur le bouton **Audience personnalisée** pour ouvrir l'éditeur de composants.

Sélectionnez **Criteo** comme le partenaire de synchronisation d'audience souhaité. 

![]({% image_buster /assets/img/criteo/criteo6.png %})

Sélectionnez ensuite le compte publicitaire Criteo souhaité. Dans la liste déroulante **Choisir une audience nouvelle ou existante**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}
**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Ajouter des utilisateurs à l'audience** et sélectionnez les champs que vous souhaitez synchroniser avec Criteo. Ensuite, enregistrez votre audience en cliquant sur le bouton **Créer une audience** en bas de l'éditeur d'étape.

![Vue élargie de l'étape du canvas d’audience personnalisée. Ici, le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée.]({% image_buster /assets/img/criteo/criteo3.png %})

Les utilisateurs seront avertis en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent également référencer cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas car l'audience a été créée en mode brouillon.

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant canvas.]({% image_buster /assets/img/criteo/criteo1.png %})

Lorsque vous lancez un canvas avec une nouvelle audience, Braze synchronise les utilisateurs quasiment en temps réel lorsqu'ils entrent dans le composant de synchronisation de l’audience.
{% endtab %}
{% tab Synchronisation avec une audience existante %}
**Synchronisation avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs aux audiences Criteo existantes afin de s'assurer que ces audiences sont à jour. Pour effectuer une synchronisation avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant et sélectionnez **Ajouter à l'audience**. Braze ajoutera ensuite des utilisateurs en temps quasi réel au fur et à mesure qu'ils entreront dans le composant Audience Sync.

![Vue élargie de l'étape du canvas d’audience personnalisé. Ici, le compte publicitaire souhaité et l'audience existante sont sélectionnés.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer le canvas

Une fois que vous avez configuré la synchronisation d’audience avec Criteo, lancez simplement le canvas ! La nouvelle audience sera créée, et les utilisateurs qui passeront par l'étape de synchronisation de l'audience seront passés dans cette audience sur Criteo. Si votre canvas contient des composants ultérieurs, vos utilisateurs passeront ensuite à l'étape suivante de leur parcours utilisateur.

Vous pouvez voir l'audience dans Criteo en accédant à votre compte gestionnaire de publicités, puis en sélectionnant Segments dans la **Bibliothèque d'audience** de la navigation. Sur la page **Segments**, vous pouvez voir la taille de chaque audience après qu'elle ait atteint ~1 000.

![La bibliothèque d'audience indique le segment, l'ID, la source, le type, la taille, l'utilisation actuelle et la dernière mise à jour.]({% image_buster /assets/img/criteo/criteo.png %})

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit

Au fur et à mesure que les utilisateurs atteignent l'étape de synchronisation de l'audience, Braze synchronisera ces utilisateurs en quasi-temps réel tout en respectant les limites de taux de l'API de Criteo. Ce que cela signifie en pratique, c'est que Braze essaiera de mettre en lot et de traiter autant d'utilisateurs que possible toutes les 5 secondes avant d'envoyer ces utilisateurs à Criteo.

La limite de débit de l'API de Criteo indique qu'il ne faut pas dépasser 250 demandes par minute. Si un client Braze atteint cette limite de débit, le canvas Braze retentera la synchronisation pendant environ 13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés sous les indicateurs Users Errored. 

## Comprendre les analyses

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation des audiences.

| Indicateurs | Description |
| --- | --- |
| Entré | Nombre d'utilisateurs ayant entré ce composant pour être synchronisé avec Criteo. |
| Passage à l'étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un. Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès à Criteo. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour être synchronisés dans Criteo. |
| Utilisateurs erronés | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Criteo en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Criteo non valide ou la suppression de l'audience dans Criteo. |
| Utilisateurs ayant quitté le canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un canvas est un composant de synchronisation d'audience. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
N'oubliez pas que les indicateurs relatifs aux utilisateurs synchronisés et aux utilisateurs en erreur sont retardés en raison de la vidange en masse et de la relance après 13 heures, respectivement.
{% endalert %}

## Foire aux questions

### Que dois-je faire ensuite si je reçois une erreur de jeton non valide ?
Vous pouvez simplement déconnecter et reconnecter votre compte Criteo sur la page partenaire Criteo. Assurez-vous avec votre administrateur Criteo que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez synchroniser.

### Pourquoi mon Canvas n’est-il pas autorisé à être lancé ?

Confirmez que votre compte publicitaire Criteo s'est bien connecté à Braze sur la page partenaire de Criteo. Ensuite, vérifiez que vous avez sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.

### Comment puis-je savoir si les utilisateurs ont été appariés après les avoir transmis à Criteo ?

Criteo ne fournit pas ces informations pour leurs propres politiques de confidentialité des données.

### Combien d'audiences Criteo peut-il prendre en charge ?

Pour l'instant, vous ne pouvez avoir que 1 000 audiences au sein de votre compte Criteo. Si vous dépassez cette limite, Braze vous informera de l'impossibilité de créer de nouvelles audiences. Vous devrez supprimer les audiences que vous n'utilisez plus dans votre compte publicitaire Criteo.


