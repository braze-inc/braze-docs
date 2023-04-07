---
nav_title: Synchronisation de l’audience vers Facebook
article_title: Synchronisation de l’audience Canvas vers Facebook
description: "Cet article de référence couvre la façon d’utiliser la synchronisation d’audience de Braze vers Facebook pour fournir des publicités basées sur des déclencheurs comportementaux, des segmentations, etc."
page_order: 4
alias: "/audience_sync_facebook/"

Outil :
  - Canvas

---

# Synchronisation de l’audience vers Facebook

En utilisant la synchronisation de l’audience Braze vers Facebook, les marques peuvent choisir d’ajouter les données de leurs propres utilisateurs à partir de leur intégration Braze aux audiences personnalisées de Facebook Custom afin de proposer des publicités basées sur des déclencheurs comportementaux, des segmentations, etc. Les critères que vous utilisez généralement pour déclencher un message (notification push, e-mail, SMS, Webhook, etc.) dans un Canvas Braze en fonction de vos données utilisateur peuvent maintenant être utilisés pour envoyer une publicité à cet utilisateur dans Facebook via les audiences personnalisées.

**Les cas d’utilisation courants pour synchroniser les audiences personnalisées comprennent** :

- Cibler des utilisateurs à forte valeur à travers plusieurs canaux pour stimuler les achats ou l’engagement.
- Recibler des utilisateurs qui sont moins réactifs aux autres canaux marketing.
- Supprimer des audiences pour empêcher les utilisateurs de recevoir des publicités lorsqu’ils sont déjà de fidèles clients de votre marque.
- Créer des audiences similaires pour acquérir de nouveaux utilisateurs plus efficacement.

Cette fonctionnalité permet aux marques de contrôler les données first-party partagées avec Facebook. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont considérées avec le plus grand sérieux. Consultez notre [Politique de confidentialité](https://www.braze.com/privacy) pour plus d’informations.

## Conditions préalables

Vous devrez vous assurer que les éléments suivants ont été créés et terminés avant de configurer votre audience Facebook dans Canvas. 

| Condition | Origine | Description |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | Un outil centralisé pour gérer les actifs Facebook de votre marque (p. ex., comptes publicitaires, pages, applications). |
| Compte publicitaire Facebook | [Facebook][2] | Un compte publicitaire Facebook actif lié au directeur commercial de votre marque.<br><br>Assurez-vous que votre administrateur commercial Facebook a accordé vos autorisations d’administrateur aux comptes publicitaires Facebook que vous prévoyez d’utiliser avec Braze, et que vous avez accepté les conditions générales de votre compte. |
| Conditions générales des audiences personnalisées de Facebook | [Facebook][3] | Acceptez les Conditions générales des audiences personnalisées de Facebook pour vos comptes publicitaires Facebook que vous prévoyez d’utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

### Étape 1 : Connectez-vous à Facebook

Dans le tableau de bord de Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Facebook**. Dans le module Facebook Audience Export, cliquez sur **Connect Facebook (Connecter Facebook)**.

![La page des technologies Facebook dans Braze qui comprend un module Overview et un module Facebook Audience Export avec le bouton Connected Facebook.][4]{: style="max-width:70%;"}

Une boîte de dialogue de Facebook oAuth apparaît pour autoriser Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook.

![La première boîte de dialogue Facebook invitant à se « Connecter comme X », où X est votre nom d’utilisateur Facebook.][6]{: style="max-width:30%;"}  ![La deuxième boîte de dialogue de Facebook vous demandant l’autorisation de gérer les publicités pour vos comptes publicitaires.][5]{: style="max-width:40%;"}

Une fois que vous avez lié Braze à votre compte Facebook, vous pourrez sélectionner les comptes publicitaires que vous souhaitez synchroniser au sein de votre groupe d’apps Braze. 

![Une liste des comptes publicitaires disponibles que vous pouvez connecter à Facebook.][7]{: style="max-width:70%;"}

Une fois que vous vous êtes connecté avec succès, vous serez ramené à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Version mise à jour de la page des partenaires de technologies de Facebook montrant les comptes publicitaires connectés avec succès.][8]{: style="max-width:70%;"}

Votre connexion à Facebook sera appliquée au niveau du groupe d’apps dans Braze. Si votre administrateur Facebook vous retire de votre Facebook Business Manager ou vous retire l’accès aux comptes Facebook connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvas actifs utilisant des composants d’audience Facebook afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs. 

{% alert important %}
Pour les clients qui ont déjà passé le processus d’examen de l’application Facebook pour [Ads Management (Gestion des annonces)](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Ads Management Standard Access (Accès standard à la gestion des annonces)](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d’utilisateur système sera toujours valable pour le composant de l’audience Facebook. Vous ne pourrez pas modifier ou révoquer le jeton d’utilisateur du système Facebook via la page partenaire de Facebook. Au lieu de cela, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d’utilisateur du système Facebook dans votre groupe d’apps de Braze. 

<br><br>La configuration de Facebook oAuth s’appliquera également aux [exportations de Facebook via les segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites). 
{% endalert %}

### Étape 2 : Accepter les conditions d'utilisation des audiences personnalisées

Avant de créer votre Canvas, vous devez d'abord accepter les conditions d'utilisation des audiences personnalisées de Facebook. Vos conditions d'utilisation se trouvent au lien suivant :
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### Étape 3 : Configurer vos critères d’entrée Canvas

Lorsque vous créez des audiences pour le Suivi des publicités, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent mettre en œuvre les filtres pertinents pour l’éligibilité des utilisateurs dans leurs critères d’entrée Canvas. Nous énumérons quelques options ci-dessous. 

Si vous avez collecté l’[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre **Ads Tracking Enabled (Suivi des publicités activé)**. Sélectionnez la valeur `true` pour envoyer uniquement les utilisateurs vers les destinations de synchronisation d’audience auxquelles ils sont abonnés. 

![][16]{: style="max-width:75%;"}

Si vous recueillez des « abonnements », des « désabonnements », des « Ne pas vendre ou partager » ou tout autre attribut personnalisé pertinent, vous devez les inclure dans vos critères d’entrée Canvas comme filtre :

![Un Canvas avec une audience d’entrée de « opted_in_marketing » correspond à « true ».][15]{: style="max-width:75%;"}

### Étape 4 : Ajouter un composant Facebook Audience dans Canvas Flow

Ajoutez un composant dans votre Canvas et sélectionnez **Facebook Audience (Audience Facebook)**.

![Flux de travail des étapes précédentes pour ajouter un composant Facebook Audience dans Canvas.][11]

### Étape 5 : Configurer une synchronisation

Cliquez sur le bouton **Custom Audience (Audience personnalisée)** pour ouvrir l’éditeur de composant.

Sélectionnez le compte publicitaire Facebook souhaité. Sous le **menu déroulant Choose a New or Existing Audience (Choisir une nouvelle audience ou une audience existante)**, saisissez le nom d’une nouvelle audience ou d’une audience existante. 

{% tabs %}
{% tab Create a New Audience %}
**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience personnalisée, sélectionnez **Add Users to Audience (Ajouter les utilisateurs à l’audience)** et sélectionnez les champs que vous souhaitez synchroniser avec Facebook. Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience (Créer une audience)** en bas de l’éditeur d’étapes.

![Vue agrandie de l’étape Canvas d’audience personnalisée. Le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée ici.]({% image_buster /assets/img/fb_audience_sync/create_audience.png %})

Les utilisateurs seront avertis en haut de l’éditeur d’étapes si l’audience a été créée avec succès ou si des erreurs sont survenues au cours du processus. Les utilisateurs peuvent également revenir à cette audience pour supprimer des utilisateurs plus tard dans le parcours Canvas, car l’audience a été créée en mode ébauche. 

![Une alerte qui apparaît lorsqu’une nouvelle audience a été créée dans le composant Canvas.]({% image_buster /assets/img/fb_audience_sync/new_audience.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze crée la nouvelle audience personnalisée lors du lancement de Canvas et synchronise ensuite les utilisateurs en temps quasi réel lorsqu’ils passent à l’étape d’audience Facebook. 

{% endtab %}
{% tab Sync with an Existing Audience %}
**Synchroniser une audience existante**<br>
Braze permet également d’ajouter ou de supprimer des utilisateurs dans des audiences personnalisées de Facebook pour s’assurer que ces audiences sont à jour. Pour synchroniser une audience existante, saisissez le nom de l’audience dans le menu déroulant et choisissez **Add to the Audience (Ajouter à l’audience)** ou **Remove from the Audience (Supprimer de l’audience)**. Ensuite, Braze ajoutera ou supprimera des utilisateurs en temps quasi réel lorsqu’ils passeront à l’étape d’audience Facebook. 

![Vue agrandie de l’étape Canvas d’audience personnalisée. Le compte publicitaire souhaité et l’audience existante sont sélectionnés ici.]({% image_buster /assets/img/fb_audience_sync/add_audience.png %})

Il est important de noter que Facebook interdit de supprimer des utilisateurs si la taille de l’audience personnalisée est trop petite (généralement moins de 1 000 utilisateurs). Par conséquent, Braze ne peut pas synchroniser d’utilisateurs pour procéder à une étape Remove from Audience (Supprimer de l’audience) jusqu’à ce que l’audience atteigne la taille appropriée.

{% endtab %}
{% endtabs %}

### Étape 6 : Lancer Canvas

Après avoir configuré votre composant d’audience Facebook, lancez simplement Canvas ! La nouvelle audience personnalisée sera créée, et les utilisateurs qui passent par le composant d’audience Facebook seront transférés dans cette audience personnalisée sur Facebook. Si votre Canvas contient des composants subséquents, vos utilisateurs passeront ensuite à l’étape suivante de leur parcours utilisateur.

L’onglet **History (Historique)** de l’audience personnalisée dans Facebook Audience Manager reflètera le nombre d’utilisateurs transférés dans l’audience depuis Braze. Si un utilisateur entre à nouveau dans l’étape, il sera envoyé vers Facebook.

![Les détails de l’audience et l’onglet Historique d’une audience Facebook donnée qui inclut un tableau Historique de l’audience avec des colonnes pour l’activité, les détails de l’activité, les éléments modifiés et la date et l’heure.][9]{: style="max-width:80%;"}

## Considérations relatives à la synchronisation des utilisateurs et aux limites de débit
 
À mesure que les utilisateurs atteignent l’étape de synchronisation de l’audience, Braze synchronisera ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l’API marketing de Facebook. Ce que cela signifie concrètement que Braze essaiera de classer et de traiter autant d’utilisateurs que possible toutes les cinq secondes avant d’envoyer ces utilisateurs vers Facebook. 

Les limites de débit de l’API marketing de Facebook n’indiquent pas plus de &#126;190 000 requêtes d’API pour chaque compte publicitaire par période d’une heure. Si un client Braze atteint ces limites de débit, le Canvas Braze tentera à nouveau d’effectuer la synchronisation pendant un délai de &#126;13 heures maximum. Si la synchronisation n’est pas possible, ces utilisateurs sont répertoriés dans l’indicateur Utilisateurs en erreur.

## Comprendre les analyses

Le tableau suivant contient des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation de l’audience.

| Indicateur | Description |
| --- | --- |
| Saisie | Nombre d'utilisateurs qui ont entré ce composant à synchroniser avec Facebook. |
| Poursuivre vers l’étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un. Tous les utilisateurs avanceront automatiquement s’il s’agit de la dernière étape de la branche Canvas. |
| Utilisateurs synchronisés | Nombre d’utilisateurs ayant été synchronisés avec Facebook. |
| Utilisateurs non synchronisés | Nombre d’utilisateurs qui n’ont pas été synchronisés en raison de champs manquants à faire correspondre. |
| Utilisateurs en attente | Nombre d’utilisateurs en cours de traitement par Braze et en attente de synchronisation sur Facebook. |
| Utilisateurs en erreur | Nombre d’utilisateurs qui n’ont pas été synchronisés avec Facebook en raison d’une erreur d’API après 13 heures de tentatives infructueuses. Les causes d’erreurs potentielles peuvent inclure un jeton Facebook non valide ou le fait que l’audience personnalisée ait été supprimée de Facebook. |
| Sortis de Canvas | Nombre d’utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d’un Canvas est une étape Facebook. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Rappelez-vous que les indicateurs sur les utilisateurs synchronisés et les utilisateurs en erreur seront signalées en retard en raison du vidage en vrac et des nouvelles tentatives sur une période de 13 heures, respectivement.
{% endalert %}   

## Résolution des problèmes

{% details Que dois-je faire ensuite si je reçois une erreur de jeton non valide ? %}
Vous pouvez simplement déconnecter et reconnecter votre compte Facebook sur la page Partenaire de Facebook. Assurez-vous que votre administrateur Facebook Business Manager dispose des autorisations appropriées sur le compte publicitaire que vous souhaitez synchroniser.
{% enddetails %}

{% details Pourquoi mon Canvas n’est-il pas autorisé à être lancé ? %}
- Assurez-vous que votre jeton d’utilisateur du système est authentifié et que vous avez accès aux comptes publicitaires souhaités dans Facebook Business Manager
- Assurez-vous que vous avez sélectionné un compte publicitaire, saisi le nom de la nouvelle audience personnalisée et que les champs sélectionnés correspondent
- Vous avez peut-être atteint la limite de 500 audiences personnalisées sur Facebook. Accédez au Facebook Audience Manager pour supprimer certaines audiences non nécessaires avant de créer une nouvelle audience personnalisée à l’aide de Canvas.
{% enddetails %}

{% details Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transféré à Facebook ? %}
Facebook ne fournit pas ces informations pour des raisons de confidentialité.
{% enddetails %}

{% details Braze prend-il en charge les audiences personnalisées basées sur la valeur ? %}
À l’heure actuelle, les audiences personnalisées basées sur la valeur ne sont pas prises en charge par Braze. Si vous souhaitez synchroniser ces types d’audiences personnalisées, contactez votre gestionnaire du succès des clients ou contactez le support technique.
{% enddetails %}

[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
