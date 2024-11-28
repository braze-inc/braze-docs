---
nav_title: TikTok
article_title: "Synchronisation de l'audience de Canvas sur TikTok"
alias: /tiktok_audience_sync/
description: "Cet article de référence abordera la manière d'utiliser Braze Audience Sync sur TikTok pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
Tool:
  - Canvas
page_order: 7

---

# Synchronisation de l'audience sur TikTok

Grâce à Braze Audience Sync to TikTok, les marques peuvent choisir d'ajouter les données utilisateurs de leur propre intégration de Braze à TikTok Audiences pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tout critère que vous utiliseriez normalement pour déclencher un message (push, e-mail, SMS, webhook, etc.) dans un Braze Canvas. 

**Les cas d'utilisation courants de la synchronisation de l'audience sont les suivants :**

- Ciblage des utilisateurs à forte valeur ajoutée via plusieurs canaux pour favoriser les achats ou l'engagement.
- Reciblage des utilisateurs qui réagissent moins aux autres canaux de marketing.
- Création d'audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque.
- Créer des audiences Actalike pour acquérir de nouveaux utilisateurs plus efficacement.

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec TikTok. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation d’audiences Braze avec TikTok est une intégration d'Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Conditions préalables

Vous devez vous assurer que les éléments suivants sont créés, complétés et/ou acceptés avant de configurer votre étape de l'audience TikTok dans Canvas.

| Exigence | Origine | Description |
| ----------- | ------ | ----------- |
| Compte TikTok pour Business Center | [TikTok](https://business.tiktok.com/) | Un outil centralisé pour gérer les ressources TikTok de votre marque (comme les comptes publicitaires, les pages, les apps). |
| Compte publicitaire TikTok | [TikTok](https://ads.tiktok.com/) | Un compte publicitaire TikTok actif lié au compte Business Center de votre marque.<br><br>Assurez-vous que votre gestionnaire du centre d'affaires TikTok vous a accordé des droits d'administrateur sur les comptes publicitaires TikTok que vous prévoyez d'utiliser avec Braze. |
| Conditions d'utilisation de TikToK | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Accepter de se conformer à tous les termes, politiques, directives et documents requis de TikTok liés à votre utilisation de Pinterest Audience Sync, y compris tous les termes, politiques, directives et documents qui y sont incorporés par référence, qui peuvent inclure : les Conditions commerciales de service, les Conditions de publicité, la Politique de confidentialité, les Conditions d'audience personnalisée, les Conditions de service du développeur, l'Accord de partage des données du développeur, les Politiques publicitaires, les Lignes directrices de la marque et les Lignes directrices de la communauté. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration 

### Étape 1 : Se connecter à TikTok

Dans le tableau de bord de Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **TikTok.** Sous Synchronisation de l'audience TikTok, sélectionnez **Connecter TikTok**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **partenaires technologiques** sous la rubrique **Intégrations.**
{% endalert %}

![La page de la technologie TikTok dans Braze comprend une section Aperçu et une section Synchronisation de l'audience TikTok avec le bouton TikTok connecté.][1]{: style="max-width:75%;"}

Vous serez ensuite redirigé vers la page OAuth de TikTok afin d'autoriser Braze pour la gestion des comptes publicitaires et la gestion de l'audience. Après avoir sélectionné **Confirmer**, vous serez redirigé dans Braze pour sélectionner les comptes publicitaires TikTok avec lesquels vous souhaitez vous synchroniser. 

![][2]{: style="max-width:75%;"}

Une fois la connexion établie, vous reviendrez à la page partenaire. Ici, vous pouvez voir quels comptes sont connectés et déconnecter les comptes existants.

![][3]{: style="max-width:75%;"}

Votre connexion TikTok sera appliquée au niveau du groupe d'applications Braze. Si votre administrateur TikTok vous retire de votre Centre d'affaires TikTok ou de l'accès aux comptes TikTok connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvas actives utilisant des composants TikTok Audience afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Ajouter un composant TikTok Audience dans Canvas Flow

Ajoutez un composant dans votre canvas et sélectionnez **Synchronisation de l’audience**. 

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation

Cliquez sur le bouton **Audience personnalisée** pour ouvrir l'éditeur de composants.

Sélectionnez **TikTok** comme partenaire de synchronisation d'audience.

![][19]{: style="max-width:80%;"}

Sélectionnez ensuite le compte publicitaire TikTok souhaité. Dans la liste déroulante **Choisir une audience nouvelle ou existante**, saisissez le nom d'une audience nouvelle ou existante.

![][11]

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Ajouter des utilisateurs à l'audience** et sélectionnez les champs que vous souhaitez synchroniser avec TikTok. Ensuite, enregistrez votre audience en cliquant sur le bouton **Créer une audience** en bas de l'éditeur d'étape.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Les utilisateurs seront avertis en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent également faire référence à cette audience pour la supprimer plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Lorsque vous lancez un canvas avec une nouvelle audience, Braze synchronise les utilisateurs quasiment en temps réel lorsqu'ils entrent dans l'étape du canvas.

{% endtab %}
{% tab Synchronisation avec une audience existante %}

**Synchronisation avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs aux audiences TikTok existantes afin de s'assurer que ces audiences sont à jour. Pour effectuer une synchronisation avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant et sélectionnez **Ajouter à l'audience**. Braze ajoutera ensuite des utilisateurs en temps quasi réel lorsqu'ils entreront dans l'étape TikTok Audience.

![Vue élargie de l'étape du canvas de l'audience personnalisée. Ici, le compte publicitaire souhaité et l'audience existante sont sélectionnés.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le canvas
Une fois que vous avez configuré votre composant TikTok Audience, il vous suffit de lancer Canvas ! Une nouvelle audience sera créée, et les utilisateurs qui passent par le composant TikTok Audience seront transférés dans cette audience sur TikTok. Si votre Canvas contient d’autres composants, vos utilisateurs passeront à l'étape suivante de leur parcours.

Vous pouvez afficher l'audience dans TikTok en entrant dans votre **compte Gestionnaire de publicités** et en sélectionnant **Audiences** dans le menu déroulant **Actifs.**  Sur la page **Audience**, vous pouvez voir la taille de chaque audience une fois qu'elle a atteint ~1 000.

![Page TikTok listant les indicateurs suivants pour l'audience donnée.][5]

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit

Lorsque les utilisateurs atteignent l'étape de synchronisation de l'audience, Braze synchronise ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l'API marketing de TikTok. Cela signifie que Braze va essayer de mettre en lot et de traiter autant d'utilisateurs toutes les 5 secondes avant d'envoyer ces utilisateurs sur TikTok.

La limite de débit de l'API Segment de TikTok stipule qu'il ne faut pas dépasser 50 requêtes par seconde et 10k utilisateurs par requête. Si un client de Braze atteint cette limite de débit, le canvas tentera à nouveau la synchronisation pendant environ 13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés sous les indicateurs Users Errored.

## Comprendre les analyses

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation des audiences.

| Indicateurs | Description |
| ------ | ----------- |
| Entré | Nombre d'utilisateurs ayant saisi ce composant à synchroniser avec TikTok. |
| Passage à l'étape suivante | Nombre d'utilisateurs qui ont avancé au composant suivant s'il en existe un. Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape du canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès sur TikTok. Notez que cela n'équivaut pas aux utilisateurs appariés sur TikTok. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour être synchronisés avec TikTok. |
| Utilisateurs erronés | Nombre d'utilisateurs qui n'ont pas été synchronisés sur TikTok en raison d'une erreur de l'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton TikTok invalide ou si l'audience a été supprimée sur TikTok. |
| Utilisateurs sortis du canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un canvas est un composant de synchronisation de l'audience. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
N'oubliez pas que les indicateurs relatifs aux utilisateurs synchronisés et aux utilisateurs en erreur sont retardés en raison de la vidange en masse et de la relance après 13 heures, respectivement.
{% endalert %}

## Résolution des problèmes

{% details Que dois-je faire si je reçois une erreur de jeton non valide ? %}
Vous pouvez déconnecter et reconnecter votre compte TikTok sur la page partenaire de TikTok. Assurez-vous auprès de votre administrateur du Centre d'affaires TikTok que vous disposez des autorisations appropriées pour le compte publicitaire que vous souhaitez synchroniser.
{% enddetails %}

{% details Pourquoi mon Canvas n'est-il pas autorisé à se lancer ? %}
Assurez-vous que votre compte TikTok se connecte avec succès à Braze sur la page partenaire de TikTok.
Assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.
{% enddetails %}

{% details Comment puis-je savoir si des utilisateurs ont été appariés après avoir transféré des utilisateurs à TikTok ? %}
TikTok ne fournit pas cette information pour leurs politiques de confidentialité des données.
{% enddetails %}

{% details Combien de temps faudra-t-il pour que mes audiences s'affichent sur TikTok ? %}
La taille de l'audience sera mise à jour dans les 24 à 48 heures sur la page Audiences du gestionnaire de publicités de TikTok.
{% enddetails %}

{% details Quel est le nombre maximum d'audiences que je peux avoir dans mon compte TikTok ads ? %}
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
[11]: {% image_buster /assets/img/tiktok/tiktok11.png %}
[12]: {% image_buster /assets/img/tiktok/tiktok12.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[14]: {% image_buster /assets/img/tiktok/tiktok14.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok15.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
