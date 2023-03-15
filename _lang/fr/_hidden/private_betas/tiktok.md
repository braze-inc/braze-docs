---
nav_title: Synchronisation de l’audience avec TikTok
article_title: Synchronisation de l’audience Canvas avec TikTok
alias: /tiktok_audience_sync/
description: "Cet article de référence couvre la façon d’utiliser la synchronisation d’audience de Braze vers TikTok pour fournir des publicités basées sur des déclencheurs comportementaux, des segmentations, etc."
Outil :
  - Canvas
hidden: true
---

# Synchronisation de l’audience avec TikTok

En utilisant la synchronisation de l’audience Braze vers TikTok, les marques peuvent choisir d’ajouter les données utilisateurs à partir de leur intégration Braze aux audiences TikTok afin de proposer des publicités basées sur des déclencheurs comportementaux, des segmentations, etc. Tous les critères que vous utiliseriez normalement pour déclencher un message (notification push, e-mail, SMS, webhook, etc.) dans un Canvas Braze. 

**Les cas d’utilisation courants pour synchroniser les audiences comprennent** :

- Cibler des utilisateurs à forte valeur à travers plusieurs canaux pour stimuler les achats ou l’engagement
- Recibler des utilisateurs qui sont moins réactifs aux autres canaux marketing
- Supprimer des audiences pour empêcher les utilisateurs de recevoir des publicités lorsqu’ils sont déjà de fidèles clients de votre marque
- Créer des audiences agissant de manière similaire pour acquérir de nouveaux utilisateurs plus efficacement

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec TikTok. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager avec vos données first-party sont considérées avec le plus grand sérieux. Consultez notre [Politique de confidentialité](https://www.braze.com/privacy) pour plus d’informations.

{% alert important %}
La synchronisation de l’audience avec TikTok est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la bêta.
{% endalert %}

## Conditions préalables

Vous devrez vous assurer que les éléments suivants ont été achevés avant de configurer votre synchronisation d’audience avec TikTok.

| Condition | Origine | Description |
| ----------- | ------ | ----------- |
| TikTok pour compte Business Center | [TikTok](https://business.tiktok.com/) | Un outil centralisé pour gérer les actifs TikTok de votre marque (p. ex., comptes publicitaires, pages, applications). |
| Compte publicitaire TikTok | [TikTok](https://ads.tiktok.com/) | Un compte publicitaire TikTok lié au compte Business Center de votre marque.<br><br>Assurez-vous que l’administrateur du gestionnaire TikTok Business Center vous a donné les autorisations d’administrateur aux comptes publicitaires TikTok que vous prévoyez d’utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration 

### Étape 1 : Se connecter à TikTok

Dans le tableau de bord de Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **TikTok**. Dans le module TikTok Audience Export, cliquez sur **Connect TikTok (Se connecter à TikTok)**.

![La page des technologies TikTok dans Braze comprend un module Overview et un module TikTok Audience Export avec le bouton Connected TikTok.][1]{: style="max-width:75%;"}

Vous serez alors redirigé vers la page TikTok OAuth afin d’autoriser Braze à gérer le compte publicitaire et l’audience. Après avoir sélectionné **Confirmer**, vous serez redirigé vers Braze afin de choisir les comptes publicitaires TikTok à synchroniser. 

![][2]{: style="max-width:75%;"}

Une fois connecté, vous retournerez à la page partenaire. Ici, vous pouvez voir quels comptes sont connectés et déconnecter des comptes existants.

![][3]{: style="max-width:75%;"}

Votre connexion à TikTok sera appliquée au niveau du groupe d’apps dans Braze. Si votre administrateur TikTok vous retire de votre TikTok Business Center ou vous retire l’accès aux comptes TikTok connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvas actifs utilisant des composants d’audience TikTok afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Configurer vos critères d’entrée Canvas

Lorsque vous créez des audiences pour le Suivi des publicités, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent mettre en œuvre les filtres pertinents pour l’éligibilité des utilisateurs dans leurs critères d’entrée Canvas. Nous énumérons quelques options ci-dessous. 

Si vous avez collecté l’[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre **Ads Tracking Enabled (Suivi des publicités activé)**. Sélectionnez la valeur `true` pour envoyer uniquement les utilisateurs vers les destinations de synchronisation d’audience auxquelles ils sont abonnés. 

![][16]{: style="max-width:75%;"}

Si vous recueillez les abonnements ou les désabonnements en tant qu’attributs personnalisés Braze, vous devez également les inclure dans vos critères d’entrée Canvas en tant que filtre :

![Un Canvas avec une audience d’entrée de « opted_in_marketing » correspond à « true ».][13]{: style="max-width:75%;"}

### Étape 3 : Ajouter un composant TikTok Audience dans Canvas Flow

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync (Synchronisation d’audience)**. Cliquez sur le bouton **Custom Audience (Audience personnalisée)** pour ouvrir l’éditeur de composant.

![][14]{: style="max-width:45%;"} ![][15]{: style="max-width:50%;"}

### Étape 4 : Configurer une synchronisation

Sélectionnez **TikTok** comme partenaire de synchronisation d’audience souhaité.

![][12]{: style="max-width:50%;"}

Sélectionnez alors le compte publicitaire TikTok souhaité. Sous le menu déroulant **Choose a New or Existing Audience (Choisir une nouvelle audience ou une audience existante)**, saisissez le nom d’une nouvelle audience ou d’une audience existante.

![][11]

{% tabs %}
{% tab Create a New Audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience personnalisée, sélectionnez **Add Users to Audience (Ajouter les utilisateurs à l’audience)** et sélectionnez les champs que vous souhaitez synchroniser avec TikTok. Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience (Créer une audience)** en bas de l’éditeur d’étapes.

![]({% image_buster /assets/img/tiktok/tiktok10.png %})

Les utilisateurs seront avertis en haut de l’éditeur d’étapes si l’audience a été créée avec succès ou si des erreurs sont survenues au cours du processus. Les utilisateurs peuvent également revenir à cette audience pour supprimer des utilisateurs plus tard dans le parcours Canvas, car l’audience a été créée en mode ébauche.

![]({% image_buster /assets/img/tiktok/tiktok9.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs en temps quasi réel lorsqu’ils entrent dans l’étape d’audience.

{% endtab %}
{% tab Sync with an Existing Audience %}

**Synchroniser une audience existante**<br>
Braze permet également d’ajouter des utilisateurs à des audiences de TikTok pour s’assurer que ces audiences sont à jour. Pour synchroniser une audience existante, saisissez le nom de l’audience dans le menu déroulant et choisissez **Add to the Audience (Ajouter à l’audience)**. Ensuite, Braze ajoutera des utilisateurs en temps quasi réel lorsqu’ils passeront à l’étape d’audience TikTok.

![Vue agrandie de l’étape Canvas d’audience personnalisée. Le compte publicitaire souhaité et l’audience existante sont sélectionnés ici.]({% image_buster /assets/img/tiktok/tiktok17.png %})

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer Canvas
Après avoir configuré votre composant d’audience TikTok, lancez simplement Canvas ! Une nouvelle audience sera créée, et les utilisateurs qui passent par le composant d’audience TikTok seront transférés dans cette audience personnalisée sur TikTok. Si votre Canvas contient des composants subséquents, vos utilisateurs passeront à l’étape suivante de leur parcours utilisateur.

Vous pouvez afficher l’audience dans TikTok en accédant à votre **compte de gestionnaire des publicités**, puis en sélectionnant **Audiences** dans le menu déroulant **Assets (Actifs)**. Sur la page **Audience**, vous pouvez voir la taille de chaque audience après avoir atteint &#126;1 000.

![Page TikTok énumérant les indicateurs suivants de l’audience concernée.][5]

## Considérations relatives à la synchronisation des utilisateurs et aux limites de débit

À mesure que les utilisateurs atteignent l’étape de synchronisation de l’audience, Braze synchronisera ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l’API marketing de TikTok. Cela signifie que Braze essaiera de classer et de traiter autant d’utilisateurs que possible toutes les cinq secondes avant d’envoyer ces utilisateurs vers TikTok.

La limitation du débit de l’API segment de TikTok ne doit pas dépasser 50 requêtes par seconde et 10 000 utilisateurs par demande. Si un client Braze atteint ces limites de débit, le Canvas tentera à nouveau d’effectuer la synchronisation pendant un délai de &#126;13 heures maximum. Si la synchronisation n’est pas possible, ces utilisateurs sont répertoriés dans l’indicateur Utilisateurs en erreur.

## Comprendre les analyses

Le tableau suivant contient des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation de l’audience.

| Indicateur | Description |
| ------ | ----------- |
| Saisie | Nombre d’utilisateurs qui ont entré ce composant à synchroniser avec TikTok. |
| Poursuivre vers l’étape suivante | Nombre d’utilisateurs qui sont passés au composant suivant s’il en existe un. Tous les utilisateurs avanceront automatiquement s’il s’agit de la dernière étape de la branche Canvas. |
| Utilisateurs synchronisés | Nombre d’utilisateurs ayant réussi à se synchroniser avec TikTok. Notez que cela ne correspond pas aux utilisateurs correspondant sur TikTok. |
| Utilisateurs non synchronisés | Nombre d’utilisateurs qui n’ont pas été synchronisés en raison de champs manquants à faire correspondre. |
| Utilisateurs en attente | Nombre d’utilisateurs en cours de traitement par Braze et en attente de synchronisation sur TikTok. |
| Utilisateurs en erreur | Nombre d’utilisateurs qui n’ont pas été synchronisés avec TikTok en raison d’une erreur d’API après 13 heures de tentatives infructueuses. Les causes d’erreurs potentielles peuvent inclure un jeton TikTok non valide ou le fait que l’audience personnalisée ait été supprimée de TikTok. |
| Sortis de Canvas | Nombre d’utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d’un Canvas est un composant de synchronisation d’audience. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Rappelez-vous que les indicateurs sur les utilisateurs synchronisés et les utilisateurs en erreur seront signalées en retard en raison du vidage en vrac et des nouvelles tentatives sur une période de 13 heures, respectivement.
{% endalert %}

## Résolution des problèmes

{% details Que dois-je faire ensuite si je reçois une erreur de jeton non valide ?
 %}
Vous pouvez déconnecter et reconnecter votre compte TikTok sur la page Partenaire de TikTok. Assurez-vous que votre administrateur TikTok Business Center dispose des autorisations appropriées sur le compte publicitaire que vous souhaitez synchroniser.
{% enddetails %}

{% details Pourquoi mon Canvas n’est-il pas autorisé à être lancé ? %}
Assurez-vous que votre compte TikTok se connecte avec succès à Braze sur la page partenaire de TikTok.
Assurez-vous que vous avez sélectionné un compte publicitaire, saisi le nom de la nouvelle audience et que les champs sélectionnés correspondent.
{% enddetails %}

{% details Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transféré à TikTok ? %}
TikTok ne fournit pas cette information de ses politiques de confidentialité des données.
{% enddetails %}

{% details Combien de temps faudra-t-il à mes audiences pour se remplir dans TikTok ? %}
La taille de l’audience sera mise à jour dans les 24 à 48 heures sur la page Audiences dans le gestionnaire publicitaire de TikTok.
{% enddetails %}

{% details Quel est le nombre maximum d’audiences que je peux avoir sur mon compte publicitaire TikTok ? %}
400
{% enddetails %}

[1]: {% image_buster /assets/img/tiktok/tiktok1.png %}
[2]: {% image_buster /assets/img/tiktok/tiktok2.png %}
[3]: {% image_buster /assets/img/tiktok/tiktok3.png %}
[4]: {% image_buster /assets/img/tiktok/tiktok4.png %}
[5]: {% image_buster /assets/img/tiktok/tiktok5.png %}
[6]: {% image_buster /assets/img/tiktok/tiktok6.png %}
[7]: {% image_buster /assets/img/tiktok/tiktok7.png %}
[8]: {% image_buster /assets/img/tiktok/tiktok8.png %}
[9]: {% image_buster /assets/img/tiktok/tiktok9.png %}
[10]: {% image_buster /assets/img/tiktok/tiktok10.png %}
[11]: {% image_buster /assets/img/tiktok/tiktok11.png %}
[12]: {% image_buster /assets/img/tiktok/tiktok12.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[14]: {% image_buster /assets/img/tiktok/tiktok14.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok15.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[17]: {% image_buster /assets/img/tiktok/tiktok17.png %}