---
nav_title: TikTok
article_title: "Synchronisation de l'audience de Canvas sur TikTok"
alias: /tiktok_audience_sync/
description: "Cet article de référence explique comment utiliser Braze Audience Sync sur TikTok pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
Tool:
  - Canvas
page_order: 8

---

# Synchronisation de l'audience sur TikTok

Grâce à Braze Audience Sync to TikTok, les marques peuvent ajouter les données utilisateurs de leur propre intégration Braze à TikTok Audiences pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tout critère que vous utiliseriez normalement pour déclencher un message (push, e-mail, SMS, webhook, etc.) dans un Canvas Braze. 

**Les cas d'utilisation courants de la synchronisation de l'audience sont les suivants** :

- Cibler des utilisateurs à forte valeur ajoutée via plusieurs canaux pour favoriser les achats ou l'engagement
- Recibler des utilisateurs qui réagissent moins aux autres canaux marketing
- Créer des audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque
- Créer des audiences Actalike pour acquérir de nouveaux utilisateurs plus efficacement

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec TikTok. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation d'audiences Braze avec TikTok est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre Account Manager Braze.
{% endalert %}

## Conditions préalables

Vous devez vous assurer que les éléments suivants sont créés, complétés et/ou acceptés avant de configurer votre étape TikTok Audience dans Canvas.

| Exigence | Origine | Description |
| ----------- | ------ | ----------- |
| Compte TikTok for Business Center | [TikTok](https://business.tiktok.com/) | Un outil centralisé pour gérer les ressources TikTok de votre marque (comme les comptes publicitaires, les pages, les applications). |
| Compte publicitaire TikTok | [TikTok](https://ads.tiktok.com/) | Un compte publicitaire TikTok actif lié au compte Business Center de votre marque.<br><br>Assurez-vous que l'administrateur de votre TikTok Business Center vous a accordé des droits d'administrateur sur les comptes publicitaires TikTok que vous prévoyez d'utiliser avec Braze. |
| Conditions d'utilisation et politiques de TikTok | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Accepter de vous conformer à l'ensemble des conditions, politiques, directives et documents requis par TikTok en lien avec votre utilisation de Pinterest Audience Sync, y compris tous les termes, politiques, directives et documents qui y sont incorporés par référence, pouvant inclure : les Conditions commerciales de service, les Conditions de publicité, la Politique de confidentialité, les Conditions d'audience personnalisée, les Conditions de service du développeur, l'Accord de partage des données du développeur, les Politiques publicitaires, les Lignes directrices de la marque et les Lignes directrices de la communauté. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration 

### Étape 1 : Se connecter à TikTok

{% alert important %}
Vous devez disposer de l'[autorisation « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) pour connecter TikTok à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **TikTok**. Dans la section TikTok Audience Sync, sélectionnez **Connecter TikTok**.

![La page de la technologie TikTok dans Braze comprend une section Aperçu et une section TikTok Audience Sync avec le bouton Connecter TikTok.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Vous serez ensuite redirigé vers la page OAuth de TikTok afin d'autoriser Braze pour la gestion des comptes publicitaires et la gestion de l'audience. Après avoir sélectionné **Confirmer**, vous serez redirigé vers Braze pour sélectionner les comptes publicitaires TikTok que vous souhaitez synchroniser. 

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Une fois la connexion établie, vous reviendrez à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Votre connexion TikTok sera appliquée au niveau du groupe d'applications Braze. Si votre administrateur TikTok vous retire de votre TikTok Business Center ou révoque l'accès aux comptes TikTok connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvas actifs utilisant des composants TikTok Audience afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Ajouter un composant TikTok Audience dans Canvas

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync**. 

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation

Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composants.

Sélectionnez **TikTok** comme partenaire de synchronisation d'audience souhaité.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Sélectionnez ensuite le compte publicitaire TikTok souhaité. Dans la liste déroulante **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Create a New Audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience** et choisissez les champs que vous souhaitez synchroniser avec TikTok. Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Vous pourrez faire référence à cette audience pour supprimer des utilisateurs plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs quasiment en temps réel dès qu'ils atteignent l'étape de l'audience.

{% endtab %}
{% tab Sync with an Existing Audience %}

**Synchronisation avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs à des audiences TikTok existantes afin de les maintenir à jour. Pour effectuer une synchronisation avec une audience existante, saisissez le nom de l'audience dans le menu déroulant et sélectionnez **Add to the Audience**. Braze ajoutera ensuite les utilisateurs quasiment en temps réel dès qu'ils entreront dans l'étape TikTok Audience.

![Vue élargie de l'étape du Canvas Custom Audience. Le compte publicitaire souhaité et l'audience existante sont sélectionnés ici.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le Canvas
Une fois votre composant TikTok Audience configuré, il vous suffit de lancer le Canvas ! Une nouvelle audience sera créée, et les utilisateurs qui passent par le composant TikTok Audience seront transférés dans cette audience sur TikTok. Si votre Canvas contient d'autres composants, vos utilisateurs passeront à l'étape suivante de leur parcours.

Vous pouvez consulter l'audience dans TikTok en accédant à votre **compte Ads Manager** et en sélectionnant **Audiences** dans le menu déroulant **Assets**. Sur la page **Audience**, vous pouvez voir la taille de chaque audience une fois qu'elle a atteint &#126;1 000.

![Page TikTok listant les indicateurs suivants pour l'audience donnée.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit

Lorsque les utilisateurs atteignent l'étape Audience Sync, Braze les synchronise quasiment en temps réel tout en respectant les limites de débit de l'API Marketing de TikTok. Concrètement, Braze regroupe et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à TikTok.

La limite de débit de l'API Segment de TikTok n'autorise pas plus de 50 requêtes par seconde et 10 000 utilisateurs par requête. Si un client atteint cette limite, Braze retente la synchronisation pendant environ &#126;13 heures. Si la synchronisation reste impossible, ces utilisateurs sont répertoriés sous l'indicateur Users Errored.

## Comprendre les analyses

Le tableau suivant présente les indicateurs et leurs descriptions pour vous aider à mieux comprendre les analyses de votre composant Audience Sync.

| Indicateur | Description |
| ------ | ----------- |
| Entrés | Nombre d'utilisateurs ayant accédé à ce composant pour être synchronisés avec TikTok. |
| Passage à l'étape suivante | Nombre d'utilisateurs ayant avancé au composant suivant, s'il en existe un. Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche du Canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs synchronisés avec succès sur TikTok. Notez que cela ne correspond pas nécessairement aux utilisateurs appariés sur TikTok. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants pour l'appariement. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour être synchronisés avec TikTok. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés sur TikTok en raison d'une erreur de l'API après environ 13 heures de tentatives. Les causes potentielles incluent un jeton TikTok invalide ou la suppression de l'audience sur TikTok. |
| Sortis du Canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans le reporting des indicateurs d'utilisateurs synchronisés et d'utilisateurs en erreur, en raison respectivement du vidage en masse et de la période de relance de 13 heures.
{% endalert %}

## Foire aux questions

### Que dois-je faire si je reçois une erreur de jeton non valide ?

Vous pouvez déconnecter et reconnecter votre compte TikTok sur la page partenaire TikTok. Vérifiez auprès de l'administrateur de votre TikTok Business Center que vous disposez des autorisations appropriées pour le compte publicitaire que vous souhaitez synchroniser.

### Pourquoi mon Canvas ne peut-il pas être lancé ?

Vérifiez que votre compte TikTok est bien connecté à Braze sur la page partenaire TikTok. Assurez-vous ensuite d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.

### Comment savoir si les utilisateurs ont été appariés après leur transfert vers TikTok ?

TikTok ne fournit pas cette information en raison de ses politiques de confidentialité des données.

### Combien de temps faut-il pour que mes audiences se remplissent dans TikTok ?

La taille de l'audience sera mise à jour sous 24 à 48 heures sur la page Audiences du Ads Manager de TikTok.

### Quel est le nombre maximum d'audiences que je peux avoir dans mon compte publicitaire TikTok ?

Vous pouvez avoir jusqu'à 400 audiences par compte publicitaire TikTok.

### Pourquoi la taille de mon audience ou le taux de correspondance dans TikTok sont-ils plus élevés que le nombre d'utilisateurs synchronisés dans Braze avec Audience Sync ?

Dans TikTok, un même ID peut être associé à plusieurs utilisateurs TikTok. Cela se produit le plus souvent lorsque les clients utilisent des identifiants publicitaires mobiles (IDFA iOS et GAID Android), car un même appareil peut avoir plusieurs utilisateurs TikTok connectés. 

De plus, TikTok comptabilise également les utilisateurs de Pangle parmi les utilisateurs appariés, ce qui peut dans certains cas entraîner un taux d'appariement élevé. Cependant, lorsque vous utilisez l'audience pour la diffusion de publicités, la taille réelle de l'audience livrable peut être inférieure au nombre d'utilisateurs appariés, car elle dépend du placement et d'autres facteurs.

### Pourquoi est-ce que je reçois un e-mail dont l'objet est « Audience Does Not Exist For Canvas » ?

Cela peut se produire si l'audience que vous avez choisie pour la synchronisation n'est pas une audience en continu (par exemple, s'il s'agit d'une audience lookalike ou d'une audience basée sur un fichier d'utilisateurs). Essayez de créer une nouvelle audience via l'étape Braze Audience Sync dans votre Canvas.