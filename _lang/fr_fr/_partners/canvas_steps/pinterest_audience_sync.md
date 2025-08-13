---
nav_title: Pinterest
article_title: Synchronisation des audiences Canvas avec Pinterest
description: "Cet article de référence explique comment utiliser la synchronisation d'audience Braze vers Pinterest, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 5
alias: "/audience_sync_pinterest/"

Tool:
  - Canvas

---

# Synchronisation d’audiences avec Pinterest

En utilisant la synchronisation de l'audience Braze vers Pinterest, les marques peuvent choisir d'ajouter des données utilisateur de leur propre intégration Braze aux audiences Pinterest pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tout critère que vous utiliseriez normalement pour déclencher un message (push, e-mail, SMS, webhook, etc.) dans un canvas Braze basé sur vos données utilisateur peut désormais être utilisé pour déclencher une annonce à cet utilisateur dans vos audiences Pinterest.

**Les cas d'utilisation courants pour la synchronisation de l'audience incluent :**

- Ciblage des utilisateurs de grande valeur via plusieurs canaux pour stimuler les achats ou l'engagement
- Reciblage des utilisateurs qui réagissent moins aux autres canaux de marketing.
- Création d'audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque.
- Créer des audiences similaires pour acquérir de nouveaux utilisateurs plus efficacement

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Pinterest. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont prises en compte avec la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation des audiences Braze avec Pinterest est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Prérequis 
Vous devez vous assurer que les éléments suivants sont créés, complétés et/ou acceptés avant de configurer votre étape d'audience Pinterest dans le canvas.

| Exigence | Origine | Descriptif |
| --- | --- | --- |
| Centre d'affaires Pinterest | [Pinterest](https://www.pinterest.com/business/hub/) | Un outil centralisé pour gérer les actifs Pinterest de votre marque (tels que les comptes publicitaires, les pages, les applications). |
| Compte publicitaire Pinterest | [Pinterest](https://ads.pinterest.com/) | Un compte publicitaire Pinterest actif lié au Centre d’affaires Pinterest de votre marque.<br><br>Assurez-vous que l’administrateur du Centre d'affaires Pinterest vous a accordé les autorisations d'administrateur pour les comptes publicitaires Pinterest que vous prévoyez d'utiliser avec Braze. |
| Conditions et politiques de Pinterest | Pinterest | Acceptez de vous conformer à toutes les conditions, politiques, directives et documentations requises par Pinterest relatives à votre utilisation de la synchronisation d'audience Pinterest, y compris toutes les conditions, politiques, directives et documentations incorporées par référence, qui peuvent inclure : les Conditions de service, les Conditions de service pour les entreprises, la Politique de confidentialité, les Conditions de service pour les développeurs et les API, les Conditions relatives aux données publicitaires, les Directives publicitaires, l'Accord de services publicitaires, les Directives communautaires et les Directives de la marque. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration 

### Étape 1 : Se connecter à Pinterest

Dans le tableau de bord de Braze, allez à **Intégrations de partenaires** > **Partenaires technologiques** et sélectionnez **Pinterest**. Sous la rubrique Synchronisation de l'audience Pinterest, sélectionnez **Connecter Pinterest.**

![Page technologique Pinterest dans Braze qui comprend une section Aperçu et une section Pinterest Audience Sync avec le bouton Pinterest connecté.][1]{: style="max-width:80%;"}

Vous serez ensuite redirigé vers la page OAuth de Pinterest pour autoriser Braze à gérer les comptes publicitaires et les audiences.

Après avoir sélectionné **Confirmer**, vous serez redirigé vers Braze pour sélectionner les comptes publicitaires Pinterest que vous souhaitez synchroniser. 

![Une liste de comptes publicitaires disponibles que vous pouvez connecter à Pinterest.][2]{: style="max-width:80%;"}

Une fois la connexion établie, vous retournerez à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Une version mise à jour de la page des partenaires technologiques de Pinterest montrant les comptes publicitaires connectés avec succès.][3]{: style="max-width:80%;"}

Votre connexion Pinterest sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur Pinterest supprime votre accès au Centre d’affaires Pinterest ou aux comptes Pinterest connectés, Braze détectera un jeton non valide. En conséquence, vos canvas actifs utilisant des composants d’audience Pinterest afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Ajouter une étape de synchronisation d'audience avec Pinterest

Ajoutez un composant dans votre canvas et sélectionnez **Synchroniser l’audience**.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation

Cliquez sur le bouton **Audience personnalisé** pour ouvrir l'éditeur de composants.

Sélectionnez **Pinterest** comme partenaire de synchronisation d'audience souhaité.

![][19]{: style="max-width:80%;"}

Ensuite, sélectionnez le compte publicitaire Pinterest souhaité. Sous le **menu déroulant Choisir une audience nouvelle ou existante**, tapez le nom d'un nouveau ou d'un public existant.

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Entrez un nom pour la nouvelle audience, sélectionnez **Ajouter des utilisateurs à l'audience**, et sélectionnez les champs que vous souhaitez synchroniser avec Pinterest. Ensuite, enregistrez votre audience en cliquant sur le bouton **Créer une audience** en bas de l'éditeur d'étape.

![Vue élargie de l'étape du canvas d’audience personnalisée. Ici, le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Les utilisateurs seront avertis en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent également référencer cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas car l'audience a été créée en mode brouillon.

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant canvas.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Lorsque vous lancez un canvas avec une nouvelle audience, Braze synchronise les utilisateurs en quasi temps réel lorsqu'ils entrent dans l'étape de synchronisation de l'audience.
{% endtab %}
{% tab Synchronisation avec une audience existante %}
**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs aux audiences Pinterest existantes pour s'assurer que ces audiences sont à jour. Pour synchroniser avec une audience existante, tapez le nom de l'audience existante dans le menu déroulant et ajoutez-le à l'audience. Braze ajoutera ensuite des utilisateurs en quasi-temps réel lorsqu'ils entreront dans l'étape de synchronisation de l'audience.

![Vue élargie de l'étape du canvas d’audience personnalisé. Ici, le compte publicitaire souhaité et l'audience existante sont sélectionnés.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer canvas

Une fois que vous avez configuré la synchronisation d'audience avec Pinterest, lancez le canvas ! La nouvelle audience sera créée et les utilisateurs qui passeront par l'étape Synchronisation de l’audience seront transférés vers cette audience sur Pinterest. Si votre canvas contient des composants ultérieurs, vos utilisateurs passeront à l'étape suivante de leur parcours utilisateur.

Vous pouvez voir l'audience sur Pinterest en entrant dans votre compte gestionnaire de publicités et en sélectionnant Audiences dans le menu déroulant des publicités. Depuis la page Audience, vous pouvez voir la taille de chaque audience une fois qu'elles ont atteint environ 100.

![Détails d’une audience Pinterest donnée, notamment le nom, l'ID, le type et la taille de l'audience.][11]

## Considérations sur la synchronisation des utilisateurs et la limite de débit

Au fur et à mesure que les utilisateurs atteignent l'étape de synchronisation de l'audience, Braze synchronisera ces utilisateurs en quasi-temps réel tout en respectant les limites de taux de l'API Marketing de Pinterest. En pratique, Braze essaiera de regrouper et de traiter autant d'utilisateurs que possible toutes les 5 secondes avant d'envoyer ces utilisateurs à Pinterest.

Selon la limite de débit de l'API Segment de Pinterest, il ne peut pas y avoir plus de sept requêtes par seconde par utilisateur et 1 900 utilisateurs par requête. Si un client Braze atteint cette limite de débit, le canvas Braze tentera de synchroniser pendant environ 13 heures maximum. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés sous les indicateurs Users Errored.

## Comprendre les analyses

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation des audiences.

| Indicateurs | Description |
| --- | --- |
| Entré | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés avec Pinterest. |
| Procédé à l'étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un ? Tous les utilisateurs avanceront automatiquement si c'est la dernière étape de la branche canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès sur Pinterest. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour se synchroniser avec Pinterest. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Pinterest en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Pinterest non valide ou la suppression de l'audience Pinterest. |
| Sorti de canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un canvas est un composant de synchronisation d'audience. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans la génération du rapport des utilisateurs synchronisés et des indicateurs d’erreurs en raison du vidage en masse et de la période de 13 heures de nouvelles tentatives, respectivement.
{% endalert %}   

## Foire aux questions

### Combien de temps faudra-t-il à mes audiences pour se remplir dans Pinterest ?

La taille de l'audience sera mise à jour dans les 24 à 48 heures sur la page **Audiences** du gestionnaire de publicités de Pinterest.

### Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transféré à Pinterest ?

Pinterest ne fournit pas ces informations pour ses propres politiques de confidentialité des données.

### Que dois-je faire ensuite si je reçois une erreur de jeton non valide ?

Confirmez auprès de votre administrateur Pinterest Business Hub que vous disposez des autorisations appropriées pour le compte publicitaire que vous souhaitez synchroniser. Vous pouvez également déconnecter et reconnecter votre compte Pinterest sur la page partenaire de Pinterest. 

### Pourquoi mon Canvas n’est-il pas autorisé à être lancé ?

Assurez-vous que votre compte Pinterest se connecte avec succès à Braze sur la page partenaire Pinterest. Assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.

### Pourquoi ne puis-je pas sélectionner mon compte publicitaire pour mon étape de synchronisation de l'audience ?

Vérifiez que votre jeton a été généré avec les autorisations de compte correctes. Notez que si vous avez trop d'audiences dans votre compte publicitaire Pinterest, le menu déroulant permettant de sélectionner votre compte publicitaire peut dépasser le temps imparti. Dans ce cas, nous vous recommandons de réduire le nombre d'audiences dans votre compte publicitaire.

[1]: {% image_buster /assets/img/pinterest/pinterest1.png %}
[2]: {% image_buster /assets/img/pinterest/pinterest2.png %}
[3]: {% image_buster /assets/img/pinterest/pinterest3.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[6]: {% image_buster /assets/img/pinterest/pinterest6.png %}
[7]: {% image_buster /assets/img/pinterest/pinterest7.png %}
[8]: {% image_buster /assets/img/pinterest/pinterest8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[9]: {% image_buster /assets/img/pinterest/pinterest9.png %}
[10]: {% image_buster /assets/img/pinterest/pinterest10.png %}
[11]: {% image_buster /assets/img/pinterest/pinterest11.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}