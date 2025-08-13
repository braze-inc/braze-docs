---
nav_title: Google
article_title: "Synchronisation de l'audience de Canvas avec Google"
alias: /google_audience_sync/
description: "Cet article de référence vous explique comment synchroniser l’audience Braze avec Google pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
Tool:
  - Canvas
page_order: 3

---

# Synchronisation de l'audience avec Google

{% alert important %}
Google met à jour ses [règles de consentement des utilisateurs de l'Union européenne](https://www.google.com/about/company/user-consent-policy/) en réponse aux changements apportés à la [loi sur les marchés numériques (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), en vigueur à partir du 6 mars 2024. Ce nouveau changement oblige les annonceurs à divulguer certaines informations à leurs utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse, ainsi qu'à obtenir d'eux le consentement nécessaire. Consultez la documentation suivante pour en savoir plus.
{% endalert %}

L'intégration de la synchronisation de l’audience Braze avec Google permet aux marques d'étendre la portée de leurs parcours clients cross-canal à Google Search, Google Shopping, Gmail, YouTube et Google Display. Grâce à vos données clients first-party, vous pouvez diffuser en toute sécurité des publicités basées sur des déclencheurs comportementaux dynamiques, la segmentation, etc. Tous les critères que vous utilisez habituellement pour déclencher un message (par exemple, push, e-mail ou SMS) dans le cadre d'un Canvas Braze peuvent être utilisés pour déclencher une publicité à l'intention de cet utilisateur via [Google Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en).

{% alert important %}
À partir du 1er mai 2023, Google Ads ne générera plus d'audiences similaires, également appelées "lookalike audiences", à des fins de ciblage et de reporting. Pour en savoir plus, consultez la [documentation de Google Ads](https://support.google.com/google-ads/answer/12463119?).
{% endalert %}

**Les cas d'utilisation courants pour la synchronisation des audiences personnalisées sont les suivants :**
- Le ciblage des utilisateurs à forte valeur ajoutée via plusieurs canaux pour stimuler les achats ou l'engagement.
- Reciblez les utilisateurs qui réagissent moins aux autres canaux de marketing.
- Créer des audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque.

{% alert note %}
Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Google. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. Pour en savoir plus sur notre politique de confidentialité des données de Braze, cliquez [ici.](https://www.braze.com/privacy)
{% endalert %}

## Conditions préalables

Assurez-vous que les éléments suivants sont créés et complétés avant de configurer votre étape Google Audience dans Canvas.

| Exigence | Origine | Description |
| ----------- | ------ | ----------- |
| Compte Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Un compte Google Ads actif pour votre marque.<br><br>Si vous souhaitez partager une audience entre plusieurs comptes gérés, vous pouvez télécharger vos audiences dans votre [compte gestionnaire](https://support.google.com/google-ads/answer/6139186). |
| Conditions d'utilisation des annonces Google et règles d'utilisation des annonces Google | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Vous devez accepter et vous assurer de respecter les [Conditions d’utilisation des annonces](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) de Google et les [Règles des annonces de Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), qui incluent la [Politique de consentement de l'utilisateur de l'UE](https://www.google.com/about/company/user-consent-policy/), selon ce qui vous est applicable, dans le cadre de votre utilisation de la synchronisation d’audiences Braze.<br><br>Consultez votre équipe juridique sur les nouvelles règles de Google en matière de consentement des utilisateurs de l'UE afin de vous assurer que vous recueillez le consentement approprié pour utiliser les services Google Ads pour vos utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Le service Customer Match n'est pas disponible pour tous les annonceurs.<br><br>**Pour utiliser le service Customer Match, votre compte doit être doté des éléments suivants**<br>\- Des antécédents satisfaisants en matière de respect des politiques<br>\- De bons antécédents de paiement<br>\- Au moins 90 jours d'expérience dans Google Ads<br>\- Plus de 50 000 USD de dépenses totales au cours de la vie. Pour les annonceurs dont les comptes sont gérés dans des devises autres que l'USD, le montant de vos dépenses sera converti en USD en utilisant le taux de conversion mensuel moyen pour cette devise.<br><br>Si votre compte ne répond pas à ces critères, il n'est pas éligible au programme Customer Match.<br><br>Contactez votre conseiller Google Ads pour plus d'informations sur la disponibilité de Customer Match pour votre compte. |
| Signaux de consentement de Google | [Google](https://support.google.com/google-ads/answer/14310715) |  Si vous souhaitez diffuser des annonces auprès des utilisateurs finaux de l'EEE en utilisant le service Customer Match de Google, vous devez transmettre à Braze les attributs personnalisés suivants (booléens) dans le cadre de la politique de consentement des utilisateurs de l'UE de Google. Vous trouverez plus de détails à la rubrique [Collecte du consentement pour les utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsque vous utilisez les SDK de Braze pour collecter des signaux de consentement, assurez-vous de respecter les versions minimales suivantes :

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Collecte du consentement des utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse

Les règles de Google en matière de consentement des utilisateurs de l'UE exigent que les annonceurs divulguent les éléments suivants à leurs utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse, et qu'ils obtiennent leur consentement à cet égard :

* l'utilisation de cookies ou d'autres moyens de stockage local lorsque la loi l'exige ; et
* La collecte, le partage et l'utilisation de leurs données personnelles pour la personnalisation des publicités.

Cela n'affecte pas les utilisateurs finaux américains ou tout autre utilisateur final situé en dehors de l'EEE, du Royaume-Uni ou de la Suisse. Consultez votre équipe juridique sur les nouvelles règles de Google en matière de consentement des utilisateurs de l'UE afin de vous assurer que vous recueillez le consentement approprié pour utiliser les services de Google Ads pour vos utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse.

En vertu des exigences de la loi sur les marchés numériques (DMA) en vigueur à partir du 6 mars 2024, les annonceurs doivent passer le consentement des utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse lorsqu'ils partagent des données avec Google. Dans le cadre de ce changement, vous pouvez collecter les deux signaux de consentement dans Braze sous la forme des attributs personnalisés booléens suivants :

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze synchronisera les données de ces attributs personnalisés avec les [champs de consentement appropriés dans Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Gestion des consentements révoqués

Pour maintenir vos listes d'audience à jour dans le cas où un utilisateur final de l'EEE a été ajouté à la liste d'audience, puis s'est ensuite rétracté de l'un des deux consentements (`$google_ad_user_data` ou `$google_ad_personalization`), vous devez configurer un canvas pour supprimer les utilisateurs des listes d'audience existantes à l'aide d'une étape de synchronisation d'audience.

{% alert note %}
Si un EEE a précédemment donné son consentement pour les deux signaux, ces données continueront d'être utilisées pour le Customer Match de Google jusqu'à ce que cette liste expire, ou que cet état de consentement soit explicitement mis à jour via la synchronisation de l’audience Google ou les deux.
{% endalert %}

#### Conseils

* Envoyez la valeur en tant que valeur booléenne, et non de chaîne de caractères.
* Le nom de l'attribut est précédé du signe du dollar ($). Braze utilise un signe de dollar au début du nom d'un attribut pour indiquer qu'il s'agit d'une clé spéciale et réservée.
* Saisissez le nom de l'attribut en minuscules.
* Bien que vous ne puissiez pas explicitement définir un utilisateur comme non spécifié, si vous envoyez une valeur `null` ou `nil` ou toute autre valeur qui n'est pas `true` ou `false`, Braze transmettra cet utilisateur à Google en tant que `UNSPECIFIED`.
* Les nouveaux utilisateurs ajoutés ou mis à jour sans spécifier l'un ou l'autre des attributs de consentement seront synchronisés avec Google avec ces attributs de consentement marqués comme non spécifiés.

Si vous tentez de synchroniser un utilisateur de l'EEE sans les champs de consentement nécessaires et le statut accordé, Google rejettera cette tentative et ne diffusera pas d'annonces à cet utilisateur. En outre, si une publicité est diffusée à un utilisateur de l'EEE sans son consentement explicite, vous pouvez en être tenu responsable et encourir un risque financier. Pour éviter cela, nous vous suggérons d'envoyer des campagnes avec des filtres de segmentation qui n'incluent que les utilisateurs de l'EEE, du Royaume-Uni et de la Suisse ayant des attributs de consentement Google `true`. Pour plus de détails concernant la politique de consentement des utilisateurs de l'UE pour les partenaires de chargement de Customer Match, consultez les [FAQ](https://support.google.com/google-ads/answer/14310715) de Google.

### Configurer votre Canvas

Après votre synchronisation avec Braze, les attributs de consentement suivants seront disponibles sur vos profils utilisateurs et pour la segmentation :

- `$google_ad_user_data`
- `$google_ad_personalization`

Dans tous les Canvas où vous ciblez des utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse en utilisant Google Audience Sync pour ajouter des utilisateurs à une audience, vous devez exclure ces utilisateurs lorsque les deux attributs de consentement ont une valeur qui n'est pas `true`. Cela peut être réalisé en segmentant ces utilisateurs lorsque les valeurs de consentement sont fixées à `true`. Cela permet également de synchroniser les analyses/analytiques les plus précises des utilisateurs, puisque nous savons que Google rejettera ces utilisateurs des audiences. Notez que si vous utilisez Google Audience Sync pour supprimer des utilisateurs d'une audience, les attributs de consentement ne sont pas nécessaires.

## Intégration

### Étape 1 : Connectez votre compte Google

Pour commencer, allez dans **Intégrations partenaires** > **Partenaires technologiques** > **Google Ads** et sélectionnez **Connecter Google Ads**. Une fenêtre modale/boîte de dialogue vous invite à sélectionner l'e-mail associé à votre compte Google Ads, puis à accorder à Braze l'accès à votre compte Google Ads.

Une fois que vous avez réussi à connecter votre compte Google Ads, vous êtes renvoyé vers votre page partenaire Google Ads. Vous serez ensuite invité à sélectionner les comptes publicitaires auxquels vous souhaitez accéder dans l'espace de travail de Braze.

![Un GIF qui montre le déroulement d'une connexion réussie d'un compte Google Ads à Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exporter les ID d'IDFA ou de Google Advertising pour iOS

Si vous prévoyez d'exporter des ID IDFA iOS ou Google Advertising dans votre synchronisation d'audience, Google a besoin de votre ID d'application iOS et de votre ID d'application Android au sein des requêtes. Sous Google Audience Sync, sélectionnez **Ajouter des ID de publicité mobile**, saisissez l'ID de votre application iOS et l'ID de votre application Android (nom du package de l'application), puis enregistrez chacun d'entre eux.

<br><br>
![La page technologique Google Ads mise à jour affiche les comptes publicitaires connectés, ce qui vous permet de resynchroniser les comptes et d'ajouter des ID de publicité mobile.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Si vous avez plusieurs applications dans un même espace de travail, vous pouvez saisir n'importe lequel de vos ID d'application dans la configuration, car les ID de publicité mobile pour vos utilisateurs seront les mêmes dans plusieurs applications. En effet, le GAID Android et l'IDFA iOS sont des identifiants publicitaires universels sur l'appareil et ne sont pas spécifiques à une application. Pour synchroniser les ID des publicités mobiles pour les utilisateurs d'une application spécifique, vous pouvez utiliser des filtres de segmentation (" Dernière utilisation d'une application spécifique " ou " Version la plus récente de l'application ") pour cibler ces utilisateurs.

### Étape 2 : Ajouter une étape Google Audience dans Canvas Flow

Ajoutez un composant dans votre canvas, puis sélectionnez **Audience Sync.**

![Menu permettant de sélectionner un composant Canvas dans l'éditeur.][18]{: style="max-width:35%;"} ![L'étape de synchronisation de l'audience a été ajoutée au parcours de l'utilisateur.][20]{: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation

1. Sélectionnez **Audience personnalisée** pour ouvrir l'éditeur de composants.
2. Sélectionnez **Google** comme partenaire de la synchronisation de l'audience.

![Les paramètres de l'étape de synchronisation de l'audience avec l'option de sélectionner un partenaire pour commencer la synchronisation.][19]{: style="max-width:80%;"}

{: start="3"}
3\. Sélectionnez le compte Google ad souhaité.
4\. Dans la liste déroulante **Choisir une audience nouvelle** ou existante, saisissez le nom d'une audience nouvelle ou existante. 

{% tabs %}
{% tab Créer une nouvelle audience %}

1. Saisissez un nom pour la nouvelle audience personnalisée.
2. Sélectionnez **Ajouter des utilisateurs à l'audience**.
3. Sélectionnez les données first-party des champs d'utilisateurs à envoyer à votre audience. Vous pouvez choisir l'un des deux champs suivants :

- **Coordonnées du client** : Contient l'e-mail ou le numéro de téléphone de vos utilisateurs, ou les deux s'ils existent dans Braze. Google exige qu'il s'agisse d'un seul champ à synchroniser et non d'identifiants distincts. Vous pouvez toujours utiliser ce champ unique si vous n'avez qu'un seul des identifiants.
- **ID de l’annonceur mobile** : Sélectionnez soit IDFA pour iOS, soit GAID pour Android. En raison des exigences de Google en matière de correspondance des clients, vous ne pouvez pas avoir les deux ID d'annonceurs mobiles dans les mêmes listes de clients.

{: start="4"}
4\. Ensuite, enregistrez votre audience en sélectionnant le bouton **Créer une audience** en bas de l'éditeur d'étape.

![Vue élargie du composant d’audience personnalisée. Ici, le compte publicitaire souhaité est sélectionné, une nouvelle audience est créée et la case "Coordonnées du client" est cochée.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Les utilisateurs seront avertis en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent faire référence à cette audience pour la supprimer plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon. 

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant Canvas.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze crée une nouvelle audience personnalisée dès le lancement du Canvas et synchronise ensuite les utilisateurs quasiment en temps réel lorsqu'ils entrent dans l'étape du canvas. 

{% alert important %}
Compte tenu des exigences de Google en matière de correspondance des clients, vous ne pouvez pas avoir les coordonnées des clients et les ID des annonceurs mobiles dans les mêmes listes de clients. Google Customer Match utilisera ensuite ces informations pour déterminer quels utilisateurs de Google Search, Google Display, YouTube et Gmail peuvent être ciblés. Pour plus de détails sur les exigences de Google Customer Match, consultez leur [documentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Synchronisation avec une audience existante %}

Braze offre également la possibilité d'ajouter ou de supprimer des utilisateurs des listes de clients Google existantes afin de s'assurer que ces audiences sont à jour. Pour se synchroniser avec une audience existante :

1. Sélectionnez une audience personnalisée existante à synchroniser.
2. Choisissez si vous voulez **ajouter à l'audience** ou **retirer de l'audience**.
3. Braze ajoutera ou supprimera des utilisateurs en temps quasi réel lorsqu'ils entreront dans l'étape Google Audience. 
4. Après avoir configuré votre étape Google Audience, sélectionnez **Terminé**. Votre étape d’audience Google contiendra des détails sur la nouvelle audience.

![Vue élargie du composant d’audience personnalisée. Ici, le compte publicitaire souhaité et l'audience existante sont sélectionnés, ainsi que le bouton radio "Ajouter l'utilisateur à l'audience".]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le canvas

Complétez le reste de votre parcours utilisateur dans Canvas, puis déployez le canvas ! Si vous avez opté pour la création d'une nouvelle audience, Braze créera l'audience dans Google et ajoutera ensuite des utilisateurs au fur et à mesure qu'ils atteignent cette étape du canvas. Si vous avez choisi d'ajouter ou de supprimer des utilisateurs d'une audience existante, Braze ajoutera ou supprimera des utilisateurs lorsqu'ils atteindront cette étape de leur parcours utilisateur.

Les utilisateurs passent alors à l'élément suivant du canvas, s'il y en a un, ou quittent le canvas s'il s'agit de la dernière étape du parcours de l'utilisateur. 

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit

Lorsque les utilisateurs atteignent le composant de synchronisation de l’audience, Braze synchronise ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l'API Google Ads. Ce que cela signifie en pratique, c'est que Braze essaiera de mettre en lot et de traiter autant d'utilisateurs que possible toutes les 5 secondes avant d'envoyer ces utilisateurs à Google. 

Lorsqu'un client est sur le point d'atteindre la limite de débit de l'API Google Ads, Google transmet à Braze des recommandations pour les nouvelles tentatives. Si un client de Braze atteint sa limite de débit, Braze the Canvas tentera à nouveau la synchronisation pendant environ 13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés sous les indicateurs Users Errored.

## Présentation des analyses 

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses réalisées au cours de l’étape de synchronisation de l’audience.

| Indicateurs | Description |
| ------ | ----------- |
| *Entré* | Nombre d'utilisateurs qui ont franchi cette étape pour être synchronisés avec Google. |
| *Passage à l'étape suivante* | Combien d'utilisateurs ont avancé au composant suivant, s'il y en a un. Tous les utilisateurs avanceront automatiquement. S'il s'agit de la dernière étape de la branche du canvas, cet indicateur sera égal à 0. |
| *Utilisateurs synchronisés* | Nombre d'utilisateurs dont la synchronisation avec Google a réussi. |
| *Utilisateur non synchronisé* | Nombre d'utilisateurs qui n'ont pas été synchronisés parce qu'il manquait des champs à faire correspondre ou parce que l'attribut de consentement était défini sur `false`. |
| *Utilisateurs erronés* | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Google en raison d'une erreur, après environ 13 heures de tentatives. En cas d'erreurs spécifiques, telles que les interruptions de service de l'API Google Ads, Canvas tentera de synchroniser pendant environ 13 heures. Si la synchronisation n'est toujours pas possible à ce stade, le champ *Utilisateur non synchronisé* sera rempli. |
| *Utilisateurs en attente* | Nombre d'utilisateurs dont la synchronisation avec Google est en cours de traitement par Braze. |
| *Utilisateurs ayant quitté le canvas* | Nombre d'utilisateurs ayant quitté le Canvas. Un utilisateur quitte le canvas lorsque la dernière étape d'un canvas est une étape Google. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

### Pourquoi ne puis-je pas sélectionner plusieurs champs à faire correspondre dans ma configuration de Google Audience Step ?

Google Customer Match a des exigences strictes en ce qui concerne le formatage de ces audiences et les informations sur les clients qui y figurent. Plus précisément, les ID des annonceurs mobiles doivent être chargés séparément des informations de contact des clients (telles que l'e-mail et le numéro de téléphone). Pour plus de détails, consultez la [documentation de Google Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### Combien de temps faudra-t-il pour que mes audiences se synchronisent dans Google ?

Il faut compter entre 6 et 12 heures pour qu'une audience soit synchronisée dans Google. 

### J'ai synchronisé une audience, alors pourquoi la taille de l'audience est-elle nulle dans Google ?

Pour des raisons de confidentialité, la taille de la liste d'utilisateurs affichera zéro jusqu'à ce que la liste compte au moins 1 000 membres. Ensuite, la taille sera arrondie aux deux chiffres les plus significatifs.

### J’ai synchronisé une audience sur Google, mais mes publicités ne sont pas diffusées.

Vérifiez que vos audiences contiennent au moins 5 000 utilisateurs pour que les publicités puissent commencer à être diffusées.

### Comment résoudre l'erreur "ID de l'application mobile supprimés" ?

Si vous synchronisez des audiences avec Google, cette erreur se déclenche si vous avez choisi de synchroniser les identifiants mobiles dans le cadre de vos synchronisations, mais que vous avez supprimé les ID de vos applications mobiles depuis la page partenaire de Google. Pour résoudre ce problème, assurez-vous d'avoir ajouté les ID d'applications mobiles appropriés pour iOS et Android à la page partenaire de Google.


[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/g_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/g_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/g_sync3.png %}
