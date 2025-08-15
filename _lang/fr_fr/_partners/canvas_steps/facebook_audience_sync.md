---
nav_title: Facebook
article_title: "Synchronisation de l'audience de Canvas avec Facebook"
description: "Cet article de référence expliquera comment utiliser la synchronisation des audiences Braze avec Facebook, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Synchronisation de l'audience avec Facebook

> Grâce à la synchronisation de l'audience Braze avec Facebook, vous pouvez choisir d'ajouter les données de vos propres utilisateurs issues de votre intégration Braze aux audiences personnalisées de Facebook afin de diffuser des publicités basées sur des déclencheurs comportementaux, une segmentation, etc.

Tous les critères que vous utiliseriez habituellement pour déclencher un message (push, e-mail, SMS ou webhook) dans un Braze Canvas sur la base de vos données utilisateur peuvent désormais être utilisés pour déclencher une publicité auprès de cet utilisateur dans Facebook à l'aide d'audiences personnalisées. Par exemple, lorsque vous configurez une synchronisation d'audience avec Facebook, vous pourrez utiliser une grande variété de champs first-party comme l'e-mail, le téléphone, le prénom et le nom de famille.

**Les cas d'utilisation courants pour la synchronisation des audiences personnalisées sont les suivants :**

- Le ciblage des utilisateurs à forte valeur ajoutée avec plusieurs canaux pour favoriser les achats ou l'engagement.
- Reciblez les utilisateurs qui réagissent moins aux autres canaux de marketing.
- Créer des audiences de suppression pour empêcher les utilisateurs de recevoir des publicités lorsqu'ils sont déjà des consommateurs fidèles de votre marque.
- Créer des audiences lookalike pour acquérir de nouveaux utilisateurs plus efficacement.

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Facebook. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

## Considérations sur la synchronisation des utilisateurs et la limite de débit
 
Lorsque les utilisateurs atteignent l'étape de synchronisation de l'audience, Braze synchronise ces utilisateurs quasiment en temps réel tout en respectant les limites de débit de l'API marketing de Facebook. Ce que cela signifie en pratique, c'est que Braze essaiera de regrouper et de traiter autant d'utilisateurs que possible toutes les 5 secondes avant d'envoyer ces utilisateurs à Facebook. 

La limite de débit de l'API marketing de Facebook stipule qu'il ne faut pas dépasser ~190 000 requêtes API pour chaque compte publicitaire sur une période d'une heure. Si un client Braze atteint cette limite de débit, le canvas Braze retentera la synchronisation pendant environ 13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés dans la métrique Utilisateurs erronés.

## Conditions préalables

Vous devrez confirmer que vous avez créé et complété les éléments suivants avant de configurer votre étape de l'audience Facebook dans Canvas. 

| Exigence | Origine | Description |
| ----------- | ------ | ----------- |
| Facebook gestionnaire d'entreprise | [Facebook][1] | Un outil centralisé pour gérer les ressources Facebook de votre marque (par exemple, les comptes publicitaires, les pages et les applications). |
| Compte publicitaire Facebook | [Facebook][2] | Un compte publicitaire Facebook actif lié au gestionnaire d'entreprise de votre marque.<br><br>Assurez-vous que l'administrateur de votre gestionnaire Facebook vous a accordé les autorisations " Gérer les campagnes " ou " Gérer les comptes publicitaires " pour les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze. Assurez-vous également que vous avez accepté les conditions générales de votre compte publicitaire. |
| Conditions des audiences personnalisées de Facebook | [Facebook][3] | Acceptez les conditions des audiences personnalisées de Facebook pour vos comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

### Étape 1 : Connectez-vous à Facebook

Dans le tableau de bord de Braze, allez à **Intégrations de partenaires** > **Partenaires technologiques** et sélectionnez **Facebook**. Sous Exportation de l'audience Facebook, sélectionnez **Connecter Facebook**.

![Page technologique Facebook dans Braze qui comprend une section Aperçu et une section Exportation de l'audience Facebook avec le bouton Facebook connecté.][4]{: style="max-width:85%;"}

Une fenêtre de dialogue oAuth Facebook apparaîtra pour autoriser Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook.

![La première boîte de dialogue Facebook demandant de "Se connecter en tant que X", où X est votre nom d'utilisateur Facebook.][6]{: style="max-width:30%;"}  ![La deuxième boîte de dialogue Facebook demandant l'autorisation de gérer les publicités pour vos comptes publicitaires.][5]{: style="max-width:40%;"}

Une fois que vous avez lié Braze à votre compte Facebook, vous pourrez alors sélectionner les comptes publicitaires que vous souhaitez synchroniser dans votre espace de travail Braze. 

![Une liste de comptes publicitaires disponibles que vous pouvez connecter à Facebook.][7]{: style="max-width:70%;"}

Après avoir réussi à vous connecter, vous serez ramené à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Une version mise à jour de la page des partenaires technologiques de Facebook montrant les comptes publicitaires connectés avec succès.][8]{: style="max-width:85%;"}

Votre connexion Facebook est appliquée au niveau de l'espace de travail Braze. Si votre administrateur Facebook vous supprime de votre gestionnaire d'entreprise Facebook ou de l'accès aux comptes Facebook connectés, Braze détectera un jeton invalide. En conséquence, vos Canvases actifs utilisant des composants Facebook audience afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs. 

{% alert important %}
Pour les clients qui ont déjà suivi le processus de révision de l'application Facebook pour [Gestion des publicités](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Accès standard à la gestion des publicités](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d'utilisateur système sera toujours valide pour le composant audience de Facebook. Vous ne pourrez pas modifier ou révoquer le jeton d'utilisateur du système Facebook via la page partenaire Facebook. Au lieu de cela, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d'utilisateur système Facebook dans votre espace de travail Braze. 

<br><br>La configuration de Facebook oAuth s'appliquera également aux [exportations Facebook utilisant des segmentations]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Étape 2 : Accepter les conditions de service des audiences personnalisées

Avant de créer votre Canvas, vous devez accepter les conditions d'utilisation de Facebook en cliquant sur les liens suivants :

- **Liste de clients Audiences personnalisées Conditions d'utilisation de votre compte personnel :** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Outils Facebook Business Conditions d'utilisation de votre compte professionnel :** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Un exemple des conditions à accepter pour les audiences personnalisées des listes de clients.][24]{: style="max-width:85%;"}
![Un exemple des conditions à accepter pour les outils professionnels de Facebook.][25]{: style="max-width:85%;"}

Consultez la [section FAQ](#terms) pour plus de détails sur la vérification de votre compte Facebook lors de l'intégration.

### Étape 3 : Ajoutez un composant audience Facebook dans Canvas Flow

Ajoutez un composant dans votre canvas et sélectionnez **Facebook audience**.

![Une liste de composants à ajouter au Canvas.][18]{: style="max-width:35%;"} ![Le composant Audience Sync.][20]{: style="max-width:28%;"}

### Étape 4 : Configuration de la synchronisation

Cliquez sur le bouton **Audience personnalisée** pour ouvrir l'éditeur de composants. Ensuite, sélectionnez **Facebook** comme partenaire de synchronisation de l'audience.

!["Configurer Audience Sync" avec des options pour le choix d'un partenaire.][19]{: style="max-width:80%;"}

Sélectionnez le compte publicitaire Facebook souhaité. Sous le menu déroulant **Choisir une audience nouvelle ou existante**, tapez le nom d'une audience nouvelle ou existante. 

{% tabs %}
{% tab Créer une nouvelle audience %}

1. Saisissez un nom pour la nouvelle audience personnalisée.
2. Sélectionnez **Ajouter des utilisateurs à l'audience**, puis choisissez les champs que vous souhaitez synchroniser avec Facebook. 
3. Ensuite, sélectionnez **Créer une audience** pour enregistrer votre audience.

![Configuration de la synchronisation de l'audience "abandon de panier" avec l'e-mail, le téléphone, le prénom et le nom de famille.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Vous serez informé en haut de l'éditeur d'étape si l'audience est créée avec succès ou si une erreur se produit au cours de ce processus. Vous pouvez également faire référence à cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Un message de succès indiquant que l'audience "abandoned_cart" a été créée.]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze crée la nouvelle audience personnalisée dès le lancement du Canvas et synchronise ensuite les utilisateurs quasiment en temps réel lorsqu'ils entrent dans l'étape de synchronisation de l'audience.

{% endtab %}
{% tab Synchronisation avec une audience existante %}

Braze offre la possibilité d'ajouter ou de supprimer des utilisateurs des audiences personnalisées Facebook existantes afin de confirmer que ces audiences sont à jour. Pour synchroniser avec une audience existante, procédez comme suit :

1. Saisissez le nom de l'audience existante dans le menu déroulant.
2. Choisissez si vous voulez **ajouter à l'audience** ou **retirer de l'audience**. 
3. Braze ajoutera ou supprimera des utilisateurs en temps quasi réel lorsqu'ils entreront dans l'étape de l'audience Facebook. 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook interdit de supprimer des utilisateurs des audiences personnalisées lorsque la taille des audiences est trop faible (généralement moins de 1 000 utilisateurs). Par conséquent, Braze ne pourra pas synchroniser les utilisateurs pour une suppression de l'étape Synchronisation de l'audience jusqu'à ce que l'audience atteigne la taille d'audience appropriée.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer canvas

Après avoir configuré votre composant Facebook Audience, il est temps de lancer le Canvas ! La nouvelle audience personnalisée sera créée, et les utilisateurs qui passent par l’étape d’audience Facebook seront transférés dans cette audience personnalisée sur Facebook. Si votre Canvas contient des étapes ultérieures, vos utilisateurs passeront ensuite à l’étape suivante de leur parcours utilisateur.

L'onglet **Historique** de l'audience personnalisée dans le gestionnaire d'audience Facebook reflétera le nombre d'utilisateurs envoyés à l'audience depuis Braze. Si un utilisateur revient à l'étape, il sera renvoyé sur Facebook.

![Détails de l'audience et l'onglet Historique pour une audience Facebook donnée qui comprend un tableau Historique de l'audience avec des colonnes pour l'activité, les détails de l'activité, les éléments modifiés, la date et l'heure.][9]{: style="max-width:80%;"}

## Comprendre les analyses

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation des audiences.

| Indicateurs | Description |
| --- | --- |
| Entré | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés avec Facebook. |
| Procédé à l'étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un. Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès à Facebook. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour se synchroniser avec Facebook. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Facebook en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Facebook non valide ou la suppression de l'audience personnalisée sur Facebook. |
| Sorti de canvas | Nombre d'utilisateurs qui ont quitté le canvas. Cela se produit lorsque la dernière étape dans un canvas est une étape Facebook. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Il y aura un retard dans les indicateurs pour les utilisateurs synchronisés et les utilisateurs en erreur en raison d'un traitement interne.
{% endalert %}

## Foire aux questions

### Combien de temps faut-il pour que mes audiences soient générées dans le tableau de bord de mon partenaire de synchronisation d’audiences ?

Le temps nécessaire pour générer une audience dépend du partenaire spécifique. Tous les réseaux traiteront les requêtes de Braze et tenteront de faire correspondre les utilisateurs. La mise à jour des audiences personnalisées peut prendre jusqu'à 24 heures.

### Que dois-je faire ensuite si je reçois une erreur de jeton non valide ?

Vous pouvez simplement déconnecter et reconnecter votre compte Facebook sur la page partenaire Facebook. Confirmez auprès de votre gestionnaire de compte Facebook que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez effectuer la synchronisation.

### Pourquoi mon Canvas n’est-il pas autorisé à être lancé ?

- Assurez-vous que votre jeton utilisateur du système est authentifié et qu'il a accès aux comptes publicitaires souhaités dans Facebook Business Manager.
- Assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience personnalisée et sélectionné les champs à faire correspondre.
- Vous avez peut-être atteint la limite de 500 audiences personnalisées sur Facebook. Rendez-vous dans le gestionnaire d'audiences de Facebook pour en supprimer certaines inutiles avant de créer de nouvelles audiences personnalisées à l'aide de Canvas.

### Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transféré à Facebook ?

Facebook ne fournit pas cette information pour des raisons de confidentialité.

### Braze prend-il en charge les audiences personnalisées basées sur la valeur ?

Pour l'instant, les audiences personnalisées basées sur la valeur ne sont pas prises en charge par Braze. Si vous souhaitez synchroniser ces types d'audiences personnalisées, soumettez vos [commentaires sur le produit.]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)

### Braze procède-t-il au hachage des données avant de les envoyer aux partenaires d'Audience Sync ?

Une fois les données des e-mails normalisées, Braze procède à un hachage avec SHA256.

**IDFA/AAID/phone:** Braze effectue des hachages avec SHA256. Les types d'audience auxquels nous nous adressons sont toujours l'un des suivants :

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256\.

En termes de fréquence, Braze ne hachera les informations personnelles identifiables (IPI) des utilisateurs que lorsque ceux-ci entreront dans l'étape Audience Sync du parcours de l'utilisateur, en préparation de la synchronisation.

### Comment résoudre un problème lié à la synchronisation d'une audience personnalisée lookalike basée sur la valeur ?

Pour le moment, les audiences personnalisées similaires basées sur la valeur ne sont pas prises en charge par Braze. Si vous tentez de synchroniser avec cette audience, cela peut provoquer des erreurs au niveau de l’étape de synchronisation d'audience. Pour résoudre cela, suivez ces étapes :

1. Accédez à votre tableau de bord du gestionnaire de publicités Facebook et sélectionnez **Audiences**.
2. Sélectionnez **Créer une audience** > **Audience personnalisée**.
3. Sélectionnez **liste des clients**.
4. Téléchargez votre CSV ou liste sans la colonne **Value**. Sélectionnez **Non, continuer avec une liste de clients qui n'inclut pas la valeur du client**.
5. Terminez la création de votre audience personnalisée.
6. Dans Braze, mettez à jour l'étape de synchronisation de l'audience Facebook avec l'audience personnalisée que vous avez créée.

### J'ai reçu un e-mail relatif aux conditions de service de l'audience personnalisée de Facebook. Que dois-je faire pour résoudre ce problème ?

Pour utiliser Audience Sync to Facebook, vous devez accepter les présentes conditions de service. 

- Si votre compte publicitaire est directement associé à votre compte Facebook personnel, vous pouvez accepter les conditions de service à partir de votre compte personnel ici : `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Si votre compte publicitaire est lié au compte gestionnaire de votre entreprise, vous devez accepter les conditions de service dans votre compte Facebook Business Manager ici : `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Après avoir accepté les conditions de service de votre audience personnalisée Facebook, procédez comme suit :

1. Actualisez votre jeton d'accès Facebook avec Braze en déconnectant et reconnectant votre compte Facebook.
2. Réactivez votre étape de synchronisation d'audience Facebook en modifiant et en mettant à jour votre canvas.

Ensuite, Braze peut synchroniser les utilisateurs dès qu'ils atteignent l'étape de synchronisation de l'audience Facebook.

## Résolution des problèmes

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Erreur</th>
      <th>Description</th>
      <th>Marche à suivre pour résoudre le problème</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Jeton non valide</b></td>
      <td>Les causes typiques sont le changement de mot de passe de l'utilisateur qui a connecté l'intégration, l'expiration des informations d'identification, etc.</td>
      <td>Allez dans <b>Intégrations partenaires</b> > <b>Facebook</b> et déconnectez puis reconnectez votre compte. Consultez <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette section de résolution des problèmes</a> cette section de résolution des problèmes pour connaître les étapes supplémentaires à suivre pour auditer votre compte Facebook.</td>
    </tr>
    <tr>
      <td><b>Taille de l'audience trop petite</b></td>
      <td>Cette erreur peut se produire si vous avez créé une étape de synchronisation d'audience qui supprime des utilisateurs de vos audiences. Si la taille de votre audience est proche de zéro, le réseau peut signaler que la taille de l'audience est trop petite pour être diffusée.</td>
      <td> Utilisez une stratégie de synchronisation de l'audience qui ajoute et supprime régulièrement des utilisateurs lorsque cela n'épuise pas complètement la taille de l'audience.</td>
    </tr>
    <tr>
      <td><b>L’audience n'existe pas</b></td>
      <td>L'étape de synchronisation de l'audience utilise une audience qui n'existe pas ou qui a été supprimée. Cela peut également être déclenché si vous n'avez plus les autorisations nécessaires pour accéder à l'audience.</td>
      <td>Faites vérifier par un administrateur sur la plateforme partenaire si l'audience existe toujours. <br><br>S'il existe, confirmez que l'utilisateur qui a connecté l'intégration a l'autorisation d'accéder à l'audience. Si ce n'est pas le cas, l'utilisateur doit se voir accorder l'accès à cette audience. <br><br>Si l'audience a été supprimée intentionnellement, ajoutez une audience active et créez une nouvelle audience sur l'étape.</td>
    </tr>
    <tr>
      <td><b>Tentative d'accès au compte publicitaire</b></td>
      <td>Vous ne disposez pas d'autorisations pour le compte publicitaire ou l'audience que vous avez sélectionné.</td>
      <td>Travaillez avec les administrateurs de votre compte publicitaire pour obtenir l'accès et les autorisations nécessaires.</td>
    </tr>
    <tr>
      <td><b>Conditions de service non acceptées</b></td>
      <td>Pour certaines destinations d'Audience Sync, comme Facebook, le réseau publicitaire exige que vous acceptiez des conditions de service spécifiques pour utiliser la fonctionnalité Audience Sync. Cette erreur se déclenche si vous n'avez pas accepté les conditions appropriées. Par conséquent, il se peut que vous ayez également reçu un e-mail de Braze à ce sujet : "Vos identifiants d'autorisation pour Facebook ne sont pas valides".</td>
      <td>Vérifiez que vous avez accepté les conditions requises par Facebook.</td>
    </tr>
    <tr>
      <td><b>Tous les utilisateurs se trompent</b></td>
      <td>Si tous les utilisateurs obtiennent un résultat erroné lors d'une étape alors qu'il a été confirmé que ces utilisateurs ont des valeurs pour les champs sélectionnés de l'étape, cela peut indiquer un problème avec votre compte Facebook.</td>
      <td>Suivez les étapes de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette résolution des problèmes</a> pour vérifier que votre compte ne présente aucun problème.
      </td>
    </tr>
    <tr>
      <td><b>Échec de la création d'une audience</b></td>
      <td>Sur la page Facebook Technology Partner, vous voyez "Connected", mais il y a une erreur à l'étape Facebook Audience Sync lors de la synchronisation d'une audience, "Failed to create audience "audience name"". L'autorisation de votre compte Facebook a échoué. Veuillez consulter la page des partenaires technologiques pour reconnecter votre compte.</td>
      <td>Suivez les étapes de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette résolution des problèmes</a> pour vérifier que votre compte ne présente aucun problème.
      </td>
    </tr>
  </tbody>
</table>

### Contrôlez votre compte Facebook

Si vous rencontrez d'autres problèmes avec votre intégration, reportez-vous aux sections et étapes suivantes pour auditer votre compte Facebook. 

#### Réviser les autorisations du compte

1. Consultez la [documentation de Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sur la manière de gérer ces autorisations dans leur plateforme. Pour Facebook Business Manager, vous devez au moins avoir un rôle d'**administrateur** ou d'**employé** Business Manager et avoir accès aux comptes publicitaires nécessaires.
2. En tant qu'**employé**, confirmez que l'administrateur vous accorde toutes les autorisations de **gestion du compte publicitaire** pour chaque compte publicitaire afin de créer une audience ou de synchroniser des utilisateurs avec l'audience. 
3. Une fois cette autorisation accordée, vous devez déconnecter et reconnecter votre compte.

#### Accepter les conditions de service {#terms}

Accepter toutes les conditions de service (CGS) en cours d'élaboration par Facebook. Facebook vous demandera périodiquement, à vous (l'utilisateur) et au gestionnaire de l'entreprise, de réapprouver ses conditions de service.

1. L'utilisateur connecté doit accepter toutes les conditions de service pour chacun de ses comptes publicitaires :
- CGU de l'audience personnalisée pour votre compte Facebook personnel :
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- TOS de l'audience personnalisée basée sur la valeur :
  - Si votre compte publicitaire est lié au compte gestionnaire de votre entreprise, vous devez accepter les CGU dans votre compte gestionnaire ici : `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.
  - Si votre compte publicitaire est lié à votre compte personnel (non associé à une entreprise), vous devez accepter les CGU ici : `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>`

![Un compte disposant de toutes les autorisations nécessaires pour gérer un compte publicitaire.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Pour trouver votre ID de compte et d'entreprise, procédez comme suit :

1. Accédez à votre [gestionnaire de compte Facebook Ads Manager](https://adsmanager.facebook.com/).
2. Confirmez que vous utilisez le bon compte publicitaire en le vérifiant dans le menu déroulant.
3. Dans l'URL, trouvez l'ID du compte après `act=` et l'ID de l'entreprise après `business_id=`

![L'URL avec l'ID du compte et l'ID de l'entreprise en surbrillance.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lisez et sélectionnez **Accepter** pour les conditions de l'audience personnalisée. Nous vous recommandons de confirmer pour quel compte les conditions de service sont signées en utilisant le menu déroulant en haut des conditions.

![La liste déroulante qui indique le compte qui signe les conditions de service.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5\. Vous devez sélectionner **Accepter** pour les conditions de service. Ensuite, vous verrez apparaître ce message : "Vous avez accepté ces conditions de service au nom de Braze".
6\. Actualisez votre jeton d'accès Facebook avec Braze en déconnectant et reconnectant votre compte Facebook.
7\. Réactivez votre étape de synchronisation d'audience Facebook en modifiant et en mettant à jour votre canvas. Braze pourra alors synchroniser les utilisateurs dès qu'ils atteindront l'étape de l'audience Facebook.
8\. Si le problème persiste, essayez d'utiliser un autre utilisateur disposant d'autorisations d'administration pour accepter manuellement les conditions via le gestionnaire de publicités.

#### Achever les tâches en suspens 

Vérifiez si vous avez des tâches en cours avec Facebook qui pourraient vous empêcher d'utiliser les services Facebook Ads :

1. [Connectez-vous au Gestionnaire de publicités Facebook](https://adsmanager.facebook.com/).
2. Sélectionnez le compte publicitaire avec lequel vous rencontrez des problèmes.
3. Dans la navigation, sélectionnez l'**aperçu de** votre **compte.** <br> ![La navigation avec l'aperçu des comptes sélectionné.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Vérifiez s'il y a des alertes qui doivent être traitées. <br> ![Un compte avec une carte de crédit expirée.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Vérifiez s'il y a des tâches de configuration à effectuer. <br> ![Un compte dont la configuration est partiellement terminée.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Se connecter avec un autre utilisateur

Dans le cadre d'une autre résolution des problèmes, nous recommandons qu'un autre utilisateur administrateur essaie de connecter son compte en procédant comme suit :

1. Déconnectez l'intégration currents.
2. Un utilisateur distinct disposant de droits d'administration connecte son compte d'utilisateur Facebook.

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
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
[24]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}
[25]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}