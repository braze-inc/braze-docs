---
nav_title: Synchronisation de l'audience vers Facebook
article_title: Synchronisation de l'audience sur Facebook
description: "Cet article de référence couvrira comment utiliser Braze Audience Sync à Facebook, pour livrer des publicités basées sur des déclencheurs de comportement, segmentation, et plus encore."
page_order: 4
alias: "/audience_sync_facebook/"
Tool:
  - Toile
---

# Synchronisation de l'audience vers Facebook

Utilisation de la synchronisation de Braze Audience avec Facebook, les marques peuvent choisir d'ajouter les données de leurs propres utilisateurs à partir de leur propre intégration Braze à Facebook Custom Audiences pour livrer des publicités basées sur des déclencheurs de comportement, la segmentation, et plus encore. Tous les critères que vous utilisez généralement pour déclencher un message (Push, Email, SMS, Webhook, etc.). dans une toile Braze basée sur vos données utilisateur peut maintenant être utilisée pour déclencher une publicité pour cet utilisateur sur Facebook via des publics personnalisés.

__Les cas d'utilisation courants pour la synchronisation des audiences personnalisées comprennent__:

- Cibler les utilisateurs de grande valeur via plusieurs canaux pour générer des achats ou des engagements.
- Recibler les utilisateurs qui sont moins réceptifs aux autres canaux de marketing.
- Créer des publics de suppression pour empêcher les utilisateurs de recevoir des publicités alors qu'ils sont déjà des consommateurs loyaux de votre marque.
- Créer des audiences Lookalike pour acquérir de nouveaux utilisateurs plus efficacement.

Cette fonctionnalité permet aux marques de contrôler quelles données spécifiques sont partagées avec Facebook. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager les données de votre première partie sont prises en considération avec la plus grande attention. Pour plus d'informations, reportez-vous à notre [politique de confidentialité](https://www.braze.com/privacy).

## Intégration

### Exigences d'intégration

Vous devrez vous assurer que vous avez créé et/ou complété les éléments suivants avant de configurer votre Étape de l'Audience Facebook sur Canvas.

| Exigences                                                      | Origine       | Libellé                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gestionnaire d'entreprise Facebook                             | [Facebook][1] | Un outil centralisé pour gérer les actifs Facebook de votre marque (par exemple, comptes publicitaires, pages, applications).                                                                                                                                                                                                                                                            |
| Compte publicitaire Facebook                                   | [Facebook][2] | Un compte d'annonce Facebook actif est lié au Business Manager de votre marque.<br><br>Veuillez vous assurer que votre administrateur Facebook Business Manager vous a accordé des autorisations d'administration aux comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze et que vous avez accepté les conditions générales de votre compte publicitaire. |
| Conditions d'utilisation des audiences personnalisées Facebook | [Facebook][3] | Acceptez les conditions d'utilisation des audiences personnalisées de Facebook pour vos comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze.                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

### Étape 1 : Connectez-vous à Facebook

Dans le tableau de bord de Braze, allez dans __Partenaires Technologiques__ et sélectionnez __Facebook__. Dans le module d'exportation public Facebook, cliquez sur __Connecter Facebook__.

!\[Activer Facebook\]\[4\]{: style="max-width:70%;"}

Une fenêtre de dialogue oAuth Facebook apparaîtra pour autoriser Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook.

!\[Facebook Dialog\]\[6\]{: style="max-width:30%;"} !\[Facebook Dialog\]\[5\]{: style="max-width:40%;"}

Une fois que vous avez lié Braze à votre compte Facebook, vous serez alors en mesure de sélectionner les comptes de pub que vous souhaitez synchroniser au sein de votre groupe d'application Braze.

!\[Facebook Dialog\]\[7\]{: style="max-width:70%;"}

Une fois que vous serez connecté avec succès, vous serez ramené à la page du partenaire, où vous pouvez voir quels comptes sont connectés et déconnecter les comptes existants.

!\[Facebook Connected\]\[8\]{: style="max-width:70%;"}

Votre connexion Facebook sera appliquée au niveau du groupe d'applications Braze. Si votre administrateur Facebook vous supprime de votre Business Manager Facebook ou accède aux comptes Facebook connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvases actifs en utilisant Facebook Audience Steps montreront des erreurs, et Braze ne sera pas en mesure de synchroniser les utilisateurs.

{% alert important %}
Pour les clients qui ont précédemment subi le processus de révision de l'application Facebook pour la [Gestion de la publicité](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Accès Standard de la gestion des publicités](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d'utilisateur système sera toujours valide pour l'étape d'audience Facebook. Vous ne serez pas en mesure de modifier ou de révoquer le jeton d'utilisateur du système Facebook via la page partenaire de Facebook. Au lieu de cela, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d'utilisateur système Facebook dans votre groupe d'application Braze.

<br><br>La configuration de Facebook oAuth s'appliquera également aux [exportations Facebook via Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Étape 2 : Ajouter une étape sur Facebook dans Canvas

Ajoutez une étape dans votre Canvas, sélectionnez le menu déroulant en haut de l'étape et sélectionnez __Étape Facebook__.

!\[Add Audience Sync\]\[11\]{:style="max-width:70%"}

### Étape 3 : Configuration de la synchronisation

Cliquez sur le bouton __Audience personnalisée__ pour ouvrir l'éditeur d'étape.

Sélectionnez le compte d'annonce Facebook désiré. Sous la liste déroulante __Choisir une nouvelle audience ou une audience existante__ , tapez le nom d'un public nouveau ou existant.

{% tabs %}
{% tab Create a New Audience %}
__Créer une nouvelle audience__<br> Entrez un nom pour le nouveau public personnalisé, sélectionnez __Ajouter des utilisateurs à l'audience__ et sélectionnez les champs que vous souhaitez synchroniser avec Facebook. Ensuite, enregistrez votre audience en cliquant sur le bouton __Créer un public__ en bas de l'éditeur d'étape.

![Synchronisation de Facebook]({% image_buster /assets/img/fb_audience_sync/create_audience.png %})

Les utilisateurs seront avertis en haut de l'éditeur d'étapes si le public est créé avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent également référencer ce public pour le retrait des utilisateurs plus tard dans le voyage de Canvas parce que le public a été créé en mode brouillon.

![Synchronisation de Facebook]({% image_buster /assets/img/fb_audience_sync/new_audience.png %})

Lorsque vous lancez une toile avec un nouveau public, Braze créera le nouveau public personnalisé en lançant Canvas et ensuite en synchronisant les utilisateurs presque en temps réel au moment où ils entreront dans l'étape de l'audience Facebook.

{% endtab %}
{% tab Sync with an Existing Audience %}
__Synchroniser avec une Audience Existante__<br> Braze offre également la possibilité d'ajouter ou de supprimer des utilisateurs des audiences personnalisées Facebook existantes pour s'assurer que ces audiences sont à jour. Pour synchroniser avec un public existant, tapez le nom du public existant dans la liste déroulante et choisissez si vous voulez __Ajouter à l'auditoire__ ou __Retirer de l'auditoire__. Braze va alors soit ajouter ou supprimer des utilisateurs en temps quasi réel alors qu'ils entrent dans l'étape de l'Audience Facebook.

![Synchronisation de Facebook]({% image_buster /assets/img/fb_audience_sync/add_audience.png %})

Il est important de noter que Facebook interdit de supprimer les utilisateurs des publics personnalisés où les audiences sont trop faibles (généralement moins de 1 000). En conséquence, Braze ne pourra pas synchroniser les utilisateurs pour une étape de retrait de l'audience jusqu'à ce que le public atteigne la taille du public appropriée.

{% endtab %}
{% endtabs %}

### Étape 4 : Lancez Canvas

Une fois que vous avez configuré votre Étape de l'Audience Facebook, lancez simplement le Canvas! Le nouveau public personnalisé sera créé, et les utilisateurs qui passent par l'étape de l'Audience Facebook seront passés à ce public personnalisé sur Facebook. Si votre Canvas contient des étapes suivantes, vos utilisateurs passeront alors à l'étape suivante de leur voyage utilisateur.

L'onglet __Historique__ du public personnalisé dans le Gestionnaire d'Audience Facebook reflétera le nombre d'utilisateurs envoyés au public du Brésil. Si un utilisateur rentre à l’étape, il sera de nouveau envoyé à Facebook.

!\[Historique du public\]\[9\]{: style="max-width:80%;"}

## Synchronisation des utilisateurs et limites de taux

Au fur et à mesure que les utilisateurs atteignent l'étape de Synchronisation Audience, Braze synchronisera ces utilisateurs en temps quasi réel tout en respectant les limites de taux de l'API Marketing de Facebook. Cela signifie en pratique que Braze va essayer de traiter autant d'utilisateurs toutes les 5 secondes avant d'envoyer ces utilisateurs sur Facebook.

La limite de taux de l'API marketing de Facebook n'indique pas plus de &#126;190k de demandes API pour chaque compte publicitaire sur une période d'une heure. Si un client Braze atteint cette limite de taux, Braze le Canvas recommencera la synchronisation pendant jusqu'à &#126;13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés sous la métrique Utilisateurs erronés.

## Comprendre les analyses

Le tableau suivant contient des métriques et des descriptions pour vous aider à mieux comprendre les analyses à partir de l'étape de synchronisation de votre audience.

| Métrique                      | Libellé                                                                                                                                                                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entré                         | Nombre d'utilisateurs qui ont entré cette étape à synchroniser avec Facebook.                                                                                                                                                                                                     |
| Procédé à l'étape suivante    | Combien d'utilisateurs ont avancé à l'étape suivante s'il y en a une. Tous les utilisateurs avanceront automatiquement si c'est la dernière étape de la branche Canvas .                                                                                                          |
| Utilisateurs synchronisés     | Nombre d'utilisateurs qui ont été synchronisés avec succès sur Facebook.                                                                                                                                                                                                          |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants à correspondre.                                                                                                                                                                                |
| Utilisateurs en attente       | Nombre d'utilisateurs actuellement en cours de traitement par Braze pour se synchroniser avec Facebook.                                                                                                                                                                           |
| Utilisateurs erronés          | Nombre d'utilisateurs qui n'ont pas été synchronisés sur Facebook en raison d'une erreur de l'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Facebook non valide ou si le public personnalisé a été supprimé sur Facebook. |
| Toile Sortie                  | Nombre d'utilisateurs qui ont quitté le Canvas. Cela se produit lorsque la dernière étape dans un Canvas est une étape Facebook.                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2}

!\[Audience Sync Metrics Exemple\]\[10\]{: style="max-width:25%;"}

{% alert important %}
Rappelez-vous qu'il y aura un délai dans les rapports pour les utilisateurs synchronisés et les utilisateurs erronnés en raison de la vidange en vrac et de la reprise de 13 heures respectivement.
{% endalert %}

## Dépannage

{% de détails Que dois-je faire ensuite si je reçois une erreur de jeton invalide ? %}
Vous pouvez simplement vous déconnecter et reconnecter votre compte Facebook sur la page partenaire Facebook. Veuillez vous assurer avec l'administrateur de Facebook Business Manager que vous avez les autorisations appropriées pour le compte d'annonce avec lequel vous souhaitez synchroniser.
{% enddetails %}

{% détails Pourquoi mon Canvas n'est-il pas autorisé à se lancer? %}
- Assurez-vous que votre jeton d'utilisateur système est authentifié et a accès aux comptes publicitaires désirés dans Facebook Business Manager
- Assurez-vous que vous avez sélectionné un compte publicitaire, entrez un nom pour le nouveau public personnalisé, et les champs sélectionnés pour correspondre
- Vous avez peut-être atteint la limite de 500 audiences personnalisées sur Facebook. Allez dans le Gestionnaire d'Audience Facebook pour supprimer certains publics inutiles avant de créer de nouveaux publics personnalisés à l'aide de Canvas.
{% enddetails %}

{% de détails Comment savoir si les utilisateurs ont des correspondances après avoir passé des utilisateurs à Facebook? %}
Facebook ne fournit pas ces informations pour des raisons de confidentialité.
{% enddetails %}

{% de détails Braze supporte-t-il les audiences personnalisées basées sur la valeur ? %}
En ce moment, les audiences personnalisées basées sur la valeur ne sont pas soutenues par Braze. Si vous êtes intéressé à synchroniser ce type d'audiences personnalisées, veuillez contacter votre Responsable du service clientèle ou contacter le support.
{% enddetails %}
[4]: {% image_buster /assets/img/fb/afb_1.png %} [5]: {% image_buster /assets/img/fb/afb_2.png %} [6]: {% image_buster /assets/img/fb/afb_3. ng %} [7]: {% image_buster /assets/img/fb/afb_4.png %} [8]: {% image_buster /assets/img/fb/afb_5.png %} [9]: {% image_buster /assets/img/fb_audience_sync/audience_history. ng %} [10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %} [11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %} [12]: {% image_buster /assets/img/fb_audience_sync/add_audience. ng %} [13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %} [14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}

[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
