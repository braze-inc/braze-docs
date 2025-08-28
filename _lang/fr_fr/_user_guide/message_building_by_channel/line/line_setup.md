---
nav_title: Configuration de la LIGNE
article_title: Configuration de la LIGNE
description: "Cet article explique comment configurer le canal LINE de Braze, y compris les conditions préalables et les prochaines étapes suggérées."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# Configuration de la ligne

> Cet article explique comment configurer le canal LINE dans Braze, notamment comment configurer des utilisateurs, rapprocher les ID utilisateurs et créer des utilisateurs test LINE dans Braze.

## Conditions préalables

Vous aurez besoin des éléments suivants pour intégrer LINE avec Braze :

- [Compte professionnel LINE](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Statut du compte Premium ou vérifié (nécessaire pour synchroniser les followers existants)
   - Voir [Directives de comptes de LINE](https://terms2.line.me/official_account_guideline_oth)
- [Compte développeurs LINE](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [Canal de l’API d’envoi de messages LINE](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

L'envoi de messages LINE à partir de Braze est prélevé sur les crédits de messages de votre compte.

## Types de comptes LINE

| Type de compte | Description |
| --- | --- |
| Compte non vérifié | Un compte non vérifié qui peut être obtenu par n'importe qui (individu ou entreprise). Ce compte est représenté par un badge gris et n'apparaîtra pas dans les résultats de recherche dans l'application LINE. |
| Compte vérifié | Un compte qui a passé le contrôle de LINE Yahoo. Ce compte est représenté par un badge bleu et apparaîtra dans les résultats de recherche dans l'application LINE.<br><br>Ce compte n'est disponible que pour les comptes basés au Japon, à Taïwan, en Thaïlande et en Indonésie.  |
| Compte premium | Un compte qui a passé le contrôle de LINE Yahoo. Ce compte est représenté par un badge vert et apparaîtra dans les résultats de recherche de l'application LINE. Ce type de compte est automatiquement accordé lors du filtrage à la discrétion de LINE. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Type de compte requis

Pour synchroniser les abonnés dans Braze, votre compte LINE doit être vérifié ou premium. Lorsque vous créez un compte, son statut par défaut sera non vérifié. Vous devrez demander une vérification de compte.

### Demander un compte LINE vérifié

{% alert important %}
Les comptes vérifiés ne sont disponibles que pour les comptes basés au Japon, à Taïwan, en Thaïlande et en Indonésie.
{% endalert %}

1. Sur la page **Compte Officiel** LINE, sélectionnez **Paramètres**.
2. Sous **Statut de vérification de la divulgation d'informations**, sélectionnez **Demander la vérification du compte**.
3. Entrez les informations requises.
4. Attendez une notification avec les résultats de la vérification.

## Intégration de LINE

Pour mettre en place des mises à jour cohérentes pour les utilisateurs, reprenez les ID LINE des utilisateurs existants et synchronisez-les tous avec les états d'abonnement de LINE :

1. [Importation d'utilisateurs connus ou mise à jour de ceux-ci](#step-1-import-or-update-existing-line-users)
2. [Intégrer le canal LINE](#step-2-integrate-line-channel)
3. [Rapprocher les ID des utilisateurs](#step-3-reconcile-user-ids)
4. [Modifier les méthodes de mise à jour des utilisateurs](#step-4-change-your-user-update-methods)
5. [(Facultatif) Fusionner les profils utilisateurs](#step-5-merge-profiles-optional)

## Étape 1 : Importation ou mise à jour des utilisateurs LINE existants

Cette étape est nécessaire si vous avez un utilisateur LINE existant et identifié, car Braze récupérera ensuite automatiquement l'état de son abonnement et mettra à jour le profil utilisateur correct. Si vous n'avez pas encore rapproché les utilisateurs avec leur ID LINE, sautez cette étape. 

Vous pouvez importer ou mettre à jour des utilisateurs à l'aide de n'importe laquelle des méthodes prises en charge par Braze, y compris le [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) l'endpoint, l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou l'[ingestion de données dans le nuage]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

Quelle que soit la méthode utilisée, mettez à jour le site `native_line_id` pour fournir l'ID de ligne de l'utilisateur. Pour en savoir plus sur le site `native_line_id`, voir [Configuration de l'utilisateur](#user-setup).

{% alert note %}
L'état du groupe d'abonnement ne doit pas être spécifié et sera ignoré. LINE est la source de vérité pour l'état de l'abonnement des utilisateurs, qui sera synchronisé avec Braze soit par l'outil de synchronisation des abonnements, soit par des mises à jour d'événements.
{% endalert %}

## Étape 2 : Intégration du canal LINE

Une fois que le processus d'intégration est terminé, Braze intègre automatiquement les followers LINE de ce canal dans Braze. Pour tous les LINE ID qui sont déjà associés à un profil d'utilisateur Braze, chaque profil sera mis à jour avec le statut "abonné", et tous les LINE ID restants généreront des utilisateurs anonymes. En outre, les nouveaux adeptes de votre chaîne LINE verront des profils utilisateurs non identifiés créés lorsqu'ils suivront la chaîne.

### Étape 2.1 : Modifier les paramètres du webhook

1. Dans LINE, allez dans l'onglet **API de messagerie** et modifiez vos **paramètres de Webhook**:
   - Définissez l'URL du **Webhook** sur `https://anna.braze.com/line/events`.
      - Braze changera automatiquement cela en une URL différente lors de l'intégration, en fonction de votre cluster de tableau de bord.
   - Activez **Utiliser le webhook** et **Rélivraison du webhook**. <br><br> ![Page des paramètres du webhook permettant de vérifier ou de modifier l'URL du webhook, de basculer sur ou hors "Utiliser le webhook", "Redélivrance du webhook" et "Agrégation des statistiques d'erreur".]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Prenez note des informations suivantes dans l'onglet **Fournisseurs** :

| Type d'information | Localisation |
| --- | --- |
| ID du fournisseur | Sélectionnez votre fournisseur, puis sélectionnez **Paramètres** > **Information de base** |
| ID du canal | Sélectionnez votre fournisseur, puis sélectionnez **Canaux** > votre canal > **Paramètres de base** |
| Secret de chaîne | Sélectionnez votre fournisseur et allez dans **Chaînes** > votre chaîne > **Paramètres de base**. |
| Jeton d’accès au canal | Sélectionnez votre fournisseur, puis sélectionnez **Canaux** > votre canal > **API d’envoi de messages**. S'il n'y a pas de jeton d'accès au canal, sélectionnez **Problème**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3\. Accédez à votre **Paramètres** page > **Paramètres de réponse** et faites ce qui suit :
   - Désactivez le **message de salutation**. Ceci peut être géré dans Braze via un déclencheur lors du suivi.
   - Désactivez les **messages de réponse automatique**. Tous les messages déclenchés doivent passer par Braze. Cela ne vous empêchera pas d'envoyer directement depuis la console LINE.
   - Activez les **Webhooks**.

![Page des paramètres de réponse avec des bascules pour la façon dont votre compte traitera les chats.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Étape 2.2 : Générer des groupes d'abonnement LINE dans Braze

1. Accédez à la page Partenaires technologiques de Braze pour LINE et saisissez les informations que vous avez notées dans votre onglet **Fournisseurs** :
   - ID du fournisseur
   - ID du canal
   - Secret de chaîne
   - Jeton d’accès au canal

Si vous souhaitez ajouter une liste blanche d'adresses IP à votre compte LINE, ajoutez à votre liste d'autorisations toutes les adresses IP répertoriées pour votre cluster dans la [liste d'autorisations IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting).

{% alert important %}
Lors de l'intégration, veillez à vérifier que votre secret de canal est correct. S'il est incorrect, il peut y avoir des incohérences dans l'état de l'abonnement.
{% endalert %}

![Page d'intégration des messages LINE avec section d'intégration LINE.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Après la connexion, Braze générera automatiquement un groupe d'abonnement Braze pour chaque intégration LINE ajoutée avec succès à votre espace de travail. <br><br> Toute modification de votre liste d’abonnés (tels que de nouveaux abonnés ou des désabonnés) sera automatiquement transmise à Braze.

![LINE subscription groups section affichant un groupe d'abonnement pour le canal "LINE".]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Étape 3 : Rapprocher les ID des utilisateurs

Combinez les LINE ID de vos utilisateurs avec leurs profils utilisateurs Braze existants en suivant les étapes de la rubrique [Rapprochement des ID utilisateur.](#user-id-reconciliation)

## Étape 4 : Modifiez vos méthodes de mise à jour des utilisateurs 

Si vous disposez déjà d'une méthode pour fournir des mises à jour d'utilisateurs à Braze, vous devrez la mettre à jour pour inclure le nouveau champ `native_line_id` afin que les mises à jour d'utilisateurs envoyées ultérieurement à Braze incluent ce champ.

Il peut exister dans Braze des profils utilisateurs non identifiés avec une adresse `native_line_id` qui ont été créés dans le cadre du processus de synchronisation de l'état de l'abonnement, ou lorsqu'un nouveau follower a suivi votre chaîne. 

Lorsqu'un utilisateur LINE est identifié dans votre application par le biais de la [réconciliation des utilisateurs](#user-id-reconciliation) ou par d'autres moyens, vous pouvez cibler un profil utilisateur potentiel non identifié dans Braze à l'aide du point de terminaison [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint. Chaque profil utilisateur non identifié avec un `native_line_id` possède également un alias d'utilisateur `line_id` qui peut être utilisé pour cibler le profil utilisateur à identifier.

Voici un exemple de charge utile à `/users/identify` qui cible un profil utilisateur non identifié par l'alias d'utilisateur `line_id`: 

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

Si aucun profil utilisateur n'existe pour votre adresse `external_id`, celle-ci sera ajoutée au profil utilisateur non identifié, ce qui la rendra identifiée. S'il existe un profil utilisateur pour le site `external_id`, tous les attributs qui figurent exclusivement dans le profil utilisateur non identifié seront copiés dans le profil utilisateur connu, y compris `native_line_id` et l'état de l'abonnement de l'utilisateur.

Vous pouvez mettre à jour les utilisateurs de LINE qui sont connus dans votre application par l'intermédiaire du point de terminaison [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) en transmettant leurs identifiants externes et `native_line_id`. Si un profil utilisateur non identifié existe déjà pour un utilisateur et que le même `native_line_id` est ajouté à un profil utilisateur différent par le biais de `/users/track`, il héritera de tous les états d'abonnement du profil utilisateur non identifié. Cependant, des profils utilisateurs doubles existeront avec la même adresse `native_line_id`. Toute mise à jour ultérieure de l'abonnement à la suite d'un événement mettra à jour tous les profils en conséquence. 

Voici un exemple de charge utile à `/users/track` qui met à jour un profil utilisateur par l'ID externe pour ajouter un `native_line_id`: 

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Étape 5 : Fusionner les profils (facultatif)

Comme décrit ci-dessus, il est possible que plusieurs profils utilisateurs existent avec la même adresse `native_line_id`. Si vos méthodes de mise à jour créent des profils utilisateurs en double, vous pouvez fusionner les profils utilisateurs non identifiés en profils utilisateurs identifiés avec l'endpoint `/user/merge`. 

Voici un exemple de charge utile à `/users/merge` qui cible un profil utilisateur non identifié par l'alias d'utilisateur `line_id`:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Pour en savoir plus sur la gestion des utilisateurs en double dans Braze, consultez la section [Utilisateurs en double]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).
{% endalert %}

## Configuration de l'utilisateur

LINE est la source de vérité pour les états d'abonnement des utilisateurs. Même si vous disposez de l'ID LINE d'un utilisateur (`native_line_id`), si cet utilisateur n'a pas suivi le canal LINE à partir duquel vous envoyez des messages, LINE ne lui enverra pas de messages.

Pour vous aider à gérer cela, Braze propose des outils et une logique qui prennent en charge une base d'utilisateurs bien intégrée, notamment la synchronisation des abonnements et les mises à jour d'événements pour les suivis et les désuivis de LINE.

### Synchronisation des abonnements et logique des événements

1. **Outil de synchronisation des abonnements :** Cet outil est automatiquement déployé après une intégration réussie du canal LINE. Utilisez-le pour mettre à jour les profils existants et en créer de nouveaux.<br><br>Tous les profils utilisateurs de Braze dont le site `native_line_id` suit le canal LINE seront mis à jour et auront un statut du groupe d'abonnement de `subscribed`. Tous les adeptes de la chaîne LINE qui n'ont pas de profil utilisateur Braze avec le site `native_line_id` en auront un :<br><br>\- Un profil utilisateur anonyme créé avec `native_line_id` réglé sur l'ID LIGNE de l'utilisateur suivant le canal <br>\- Un alias d'utilisateur `line_id` défini sur l'ID de ligne de l'utilisateur suivant le canal <br>\- Un statut du groupe d'abonnement de `subscribed`

{: start="2"}
2\. **Mise à jour de l'événement :** Ils sont utilisés pour mettre à jour l'état de l'abonnement d'un utilisateur. Lorsque Braze reçoit des mises à jour d'événements utilisateur pour le canal LINE intégré et que l'événement est un suivi, le profil utilisateur aura un statut du groupe d'abonnement de `subscribed`. Si l'événement est un unfollow, le profil utilisateur aura un statut du groupe d'abonnement de `unsubscribed`.<br><br>\- Tous les profils utilisateurs de Braze ayant un `native_line_id` correspondant seront automatiquement mis à jour. <br>\- S'il n'existe pas de profil utilisateur correspondant à un événement, Braze [créera un utilisateur anonyme]({{site.baseurl}}/line/user_management/).

## Cas d’utilisation

Il s'agit de cas d'utilisation de la manière dont les utilisateurs peuvent être mis à jour après avoir suivi les étapes de configuration ci-dessus.

##### Le profil utilisateur de Braze suit déjà le canal LINE

1. Le profil utilisateur de Braze est mis à jour avec un attribut `native_line_id`. Son statut d'abonnement par défaut est `unsubscribed`.
2. L'outil de synchronisation des abonnements est exécuté, constate que l'utilisateur suit la chaîne LINE, puis met à jour le profil utilisateur avec l'état de l'abonnement `subscribed`.
3. Si l'état de l'abonnement change (par exemple, si l'utilisateur bloque la chaîne, la désamorce ou la suit à nouveau), Braze reçoit la mise à jour de LINE et actualise le profil de l'utilisateur à l'adresse `native_line_id` en conséquence.

##### Le profil utilisateur existant a bloqué le canal LINE, l'a exclu de ses amis ou l'a supprimé. 

1. Le profil utilisateur de Braze est mis à jour avec un attribut `native_line_id`. Son statut d'abonnement par défaut est `unsubscribed`.
2. L'outil de synchronisation des abonnements ne trouve pas que l'utilisateur suit la chaîne LINE et le statut de l'abonnement de l'utilisateur reste `unsubscribed`.
3. Si l'utilisateur suit ensuite la chaîne, Braze reçoit la mise à jour de LINE et met à jour le profil utilisateur avec l'état de l'abonnement `subscribed`.

##### La création du profil utilisateur intervient après le suivi de la LIGNE

1. La chaîne reçoit un nouveau follower LINE.
2. Braze crée un profil utilisateur anonyme dont l'attribut `native_line_id` correspond à l'ID LINE du suiveur et dont l'alias d'utilisateur `line_id` correspond à l'ID LINE du suiveur. Le profil a un statut d'abonnement de `subscribed`.
3. L'utilisateur est identifié comme ayant l'ID LINE par le biais de la [réconciliation des utilisateurs](#user-id-reconciliation).
  - Le profil utilisateur anonyme peut être identifié à l'aide du point de terminaison [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint. Les mises à jour ultérieures (via le [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou l'[ingestion de données dans le nuage]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) à ce profil utilisateur peuvent cibler l'utilisateur par cette importation d'utilisateurs connue `external_id`.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - Un nouveau profil utilisateur peut être créé (via le point de terminaison [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de l'endpoint, de l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou de l'[ingestion de données dans le nuage]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) en définissant l'adresse `native_line_id`. Ce nouveau profil héritera de l'état de l'abonnement du profil de l'utilisateur anonyme existant. Notez que plusieurs profils partageront le même site `native_line_id`. Ceux-ci peuvent être fusionnés à tout moment à l'aide de l'endpoint `/users/merge` selon la procédure décrite à l'[étape 5.](#step-5-merge-profiles-optional)

##### La création du profil utilisateur intervient avant le suivi de la LIGNE

1. Vous acquérez un nouvel utilisateur et envoyez l'information à Braze. Un nouveau profil utilisateur est créé (profil 1).
2. L'utilisateur suit votre compte LINE.
3. Braze reçoit un événement de suivi et crée un profil utilisateur anonyme (profil 2).
4. L'utilisateur est identifié comme ayant l'ID LINE par le biais de la [réconciliation des utilisateurs](#user-id-reconciliation).
5. Vous mettez à jour le profil 1 pour définir l'attribut `native_line_id`. Ce profil hérite de l'état de l'abonnement du profil 2.
  - Il y a maintenant deux profils utilisateurs avec le même `native_line_id`. Ceux-ci peuvent être fusionnés à tout moment à l'aide de l'endpoint `/users/merge` selon la procédure décrite à l'[étape 5.](#step-5-merge-profiles-optional)

## Rapprochement de l'ID de l'utilisateur 

Les LINE ID sont automatiquement reçus par Braze lorsqu'un utilisateur suit votre chaîne, ou lorsque vous utilisez le flux de travail unique "sync followers". Les LINE ID sont également spécifiques à la chaîne que les utilisateurs suivent, il est donc peu probable que les utilisateurs puissent fournir leurs LINE ID.

Il existe deux façons de combiner un LINE ID avec un profil utilisateur Braze existant :

- [LINE identifiant](#line-login)
- [Liaison des comptes d'utilisateurs](#user-account-linking)

### LINE Identifiant

Cette méthode utilise les identifiants des réseaux sociaux pour le rapprochement. Lorsqu'un utilisateur se connecte à votre application, il a la possibilité d'utiliser [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) pour créer un compte utilisateur ou se connecter.

{% alert note %}
Pour obtenir l'ID LINE correct pour chaque utilisateur, configurez l'identifiant LINE sous le même fournisseur que votre compte ou canal officiel LINE intégré à Braze.
{% endalert %}

1. Accédez à la LINE Developer Console et [demandez l'autorisation d'obtenir les adresses e-mail des utilisateurs](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) qui se connectent à votre appli par l'intermédiaire de LINE Login.

2. Suivez les étapes appropriées fournies par LINE pour mettre en œuvre l'identifiant LINE :<br><br>
  - [Instructions pour l'application web](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Orientations de l'application native](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Veillez à inclure `email` dans le [champ d'application défini](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) pour les demandes de vérification. 

{: start="3"}
3\. Utilisez le [jeton Verify ID](https://developers.line.biz/en/reference/line-login/#verify-id-token) pour obtenir l'e-mail de l'utilisateur. 

4. Enregistrez l'ID de ligne de l'utilisateur (`native_line_id`) dans le profil de l'utilisateur avec un e-mail correspondant dans votre base de données, ou créez un nouveau profil d'utilisateur avec l'e-mail et l'ID de ligne de l'utilisateur.

5. Envoyez les données nouvelles ou actualisées de l'utilisateur à Braze à l'aide de l'[endpoint`/user/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), de l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou de l'[ingestion de données dans le nuage]({{site.baseurl}}/user_guide/data/cloud_ingestion/).

#### Flux de travail

##### L'adepte actuel utilise l'identifiant LINE

**Scénario :** Un utilisateur anonyme a été créé lors de la synchronisation initiale des abonnés ou après l'intégration par le biais d'un événement "suivre".

1. L'utilisateur se connecte à votre application en utilisant LINE Login.
2. LINE vous fournit l'e-mail de l'utilisateur.
3. Vous envoyez à Braze l'utilisateur mis à jour (le profil de l'utilisateur existant avec cet e-mail pour ajouter l'ID LINE) ou vous mettez à jour l'utilisateur anonyme avec l'e-mail.

##### Un nouvel adepte utilise l'identifiant LINE

**Scénario :** Aucun profil utilisateur n'existe dans Braze avec l'ID LINE de l'utilisateur.

1. L'utilisateur se connecte à votre application en utilisant LINE Login.
2. LINE vous fournit l'e-mail de l'utilisateur.
3. Soit vous :
  - Mettez à jour un profil utilisateur existant avec cet e-mail pour qu'il contienne également l'ID de ligne de l'utilisateur.
  - Créez un nouveau profil utilisateur avec l'e-mail et l'ID LIGNE.
4. Lorsque l'utilisateur suit votre compte officiel LINE, Braze reçoit un événement de suivi et met à jour le statut d'abonnement de l'utilisateur à `subscribed`.

### Liaison des comptes d'utilisateurs 

Cette méthode permet aux utilisateurs de lier leur compte LINE au compte utilisateur de votre application. Vous pouvez ensuite utiliser Liquid dans Braze, comme {% raw %}`{{line_id}}`{% endraw %}, pour créer une URL personnalisée pour l'utilisateur qui transmet son LINE ID à votre site Web ou à votre application, qui peut alors être associée à un utilisateur connu.

1. Créez un Canvas basé sur une action qui repose sur un changement d'état de l'abonnement et qui se déclenche lorsqu'un utilisateur s'abonne à votre canal LINE.<br>![Canvas qui se déclenche lorsqu'un utilisateur s'abonne au canal LINE.]({% image_buster /assets/img/line/account_link_1.png %})
2. Créez un message incitant les utilisateurs à se connecter à votre site web ou à votre app, en transmettant l'ID LINE de l'utilisateur en tant que paramètre de requête (via Liquid), comme par exemple :

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3\. Créez un message de suivi qui transmet le code du coupon.
4\. (Facultatif) Créez une campagne basée sur une action ou un canvas qui se déclenche lorsque l'utilisateur LINE est identifié pour lui envoyer son code de coupon. <br>![Campagne basée sur des actions qui se déclenche lorsque l'utilisateur de LINE est identifié.]({% image_buster /assets/img/line/account_link_2.png %})

#### Fonctionnement

Une fois que l'utilisateur s'est connecté, une modification est apportée sur votre site web ou votre app afin que l'ID de l'utilisateur soit renvoyé à Braze pour l'associer à l'ID LINE qui a été transmis dans le cadre de l'URL, avec un exemple de code tel que :

```json
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Flux de travail

##### Un utilisateur existant suit votre canal LINE

**Scénario :** Un utilisateur existant à Braze suit votre chaîne sur LINE.

1. LINE envoie à Braze un événement de suivi.
2. Braze crée un profil utilisateur anonyme avec l'ID LINE, l'alias utilisateur `line_id` et le statut du subscription group d'`subscribed`.
3. L'utilisateur reçoit un message LINE avec un lien vers votre site web et votre app et se connecte. Leur profil utilisateur est désormais connu.
4. Le profil d'utilisateur anonyme qui a été créé est identifié et est fusionné, via l'[endpoint /users/identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/), avec le profil d'utilisateur connu de l'utilisateur. Le profil utilisateur connu contient désormais l'ID LINE et l'état de l'abonnement est `subscribed`.
5. (Facultatif) L'utilisateur reçoit un message LINE avec le code du coupon et Braze enregistre l'envoi dans le profil utilisateur Braze.

## Création d'utilisateurs test LINE dans Braze

Vous pouvez tester votre canal LINE avant d'implémenter [la réconciliation des utilisateurs](#user-id-reconciliation) en créant un canevas ou une campagne "Qui suis-je".

1. Configurer un Canvas qui renvoie l'ID utilisateur Braze d'un utilisateur sur un mot déclencheur spécifique. <br><br>Déclencheur d'exemple <br><br>![Déclencheur pour envoyer la campagne aux utilisateurs qui ont envoyé une LIGNE entrante à un groupe d'abonnement spécifique.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Message d'exemple<br><br>![Message LINE indiquant l'ID de l'utilisateur de Braze.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Dans Braze, vous pouvez utiliser l'ID Braze pour rechercher des utilisateurs spécifiques et les modifier selon vos besoins.

{% alert important %}
Assurez-vous que le Canvas n'a pas de contrôle global ou de groupes de contrôle empêchant les envois.
{% endalert %}


