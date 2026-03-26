---
nav_title: Configuration de LINE
article_title: Configuration de LINE
description: "Cet article explique comment configurer le canal LINE de Braze, y compris les conditions préalables et les prochaines étapes suggérées."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# Configuration de LINE

> Cet article explique comment configurer le canal LINE dans Braze, notamment comment configurer des utilisateurs, rapprocher les ID utilisateurs et créer des utilisateurs test LINE dans Braze.

## Conditions préalables

Vous aurez besoin des éléments suivants pour intégrer LINE avec Braze :

- [Compte professionnel LINE](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Statut de compte Premium ou vérifié (nécessaire pour synchroniser les followers existants)
   - Voir les [directives de comptes LINE](https://terms2.line.me/official_account_guideline_oth)
- [Compte développeurs LINE](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [Canal de l'API de messagerie LINE](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

L'envoi de messages LINE depuis Braze est déduit des crédits de messagerie de votre compte.

{% alert note %}
**Définir `native_line_id`** : Vous pouvez définir `native_line_id` en envoyant des mises à jour utilisateur à Braze (par exemple, avec l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/)). Si votre SDK côté client ne dispose pas d'un champ dédié pour `native_line_id`, envoyez-le dans les mises à jour utilisateur côté serveur en utilisant l'une de ces méthodes.
{% endalert %}

## Types de comptes LINE

| Type de compte | Description |
| --- | --- |
| Compte non vérifié | Un compte non examiné qui peut être obtenu par n'importe qui (individu ou entreprise). Ce compte est représenté par un badge gris et n'apparaît pas dans les résultats de recherche de l'application LINE. |
| Compte vérifié | Un compte ayant passé le contrôle de LINE Yahoo. Ce compte est représenté par un badge bleu et apparaît dans les résultats de recherche de l'application LINE.<br><br>Ce compte n'est disponible que pour les comptes basés au Japon, à Taïwan, en Thaïlande et en Indonésie.  |
| Compte premium | Un compte ayant passé le contrôle de LINE Yahoo. Ce compte est représenté par un badge vert et apparaît dans les résultats de recherche de l'application LINE. Ce type de compte est automatiquement accordé lors du contrôle, à la discrétion de LINE. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Type de compte requis

Pour synchroniser les followers dans Braze, votre compte LINE doit être vérifié ou premium. Lorsque vous créez un compte, son statut par défaut est non vérifié. Vous devrez demander une vérification de compte.

### Demander un compte LINE vérifié

{% alert important %}
Les comptes vérifiés ne sont disponibles que pour les comptes basés au Japon, à Taïwan, en Thaïlande et en Indonésie.
{% endalert %}

1. Sur la page **Compte officiel** LINE, sélectionnez **Paramètres**.
2. Sous **Statut de vérification de la divulgation d'informations**, sélectionnez **Demander la vérification du compte**.
3. Saisissez les informations requises.
4. Attendez une notification avec les résultats de la vérification.

## Intégration de LINE

Pour mettre en place des mises à jour utilisateur cohérentes, récupérer les ID LINE des utilisateurs existants et les synchroniser avec les états d'abonnement LINE :

1. [Importer ou mettre à jour les utilisateurs connus existants](#step-1-import-or-update-existing-line-users)
2. [Intégrer le canal LINE](#step-2-integrate-line-channel)
3. [Rapprocher les ID utilisateurs](#step-3-reconcile-user-ids)
4. [Modifier les méthodes de mise à jour des utilisateurs](#step-4-change-your-user-update-methods)
5. [(Facultatif) Fusionner les profils utilisateurs](#step-5-merge-profiles-optional)

{% alert note %}
Vous ne pouvez avoir qu'un seul compte LINE par espace de travail. Si vous disposez de plusieurs comptes LINE, nous vous recommandons d'utiliser chacun d'entre eux dans un espace de travail distinct.
{% endalert %}

## Étape 1 : Importer ou mettre à jour les utilisateurs LINE existants

Cette étape est nécessaire si vous avez un utilisateur LINE existant et identifié, car Braze récupérera ensuite automatiquement son état d'abonnement et mettra à jour le profil utilisateur correspondant. Si vous n'avez pas encore rapproché les utilisateurs avec leur ID LINE, passez cette étape. 

Vous pouvez importer ou mettre à jour des utilisateurs à l'aide de n'importe quelle méthode prise en charge par Braze, y compris l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

Quelle que soit la méthode utilisée, mettez à jour `native_line_id` pour fournir l'ID LINE de l'utilisateur. Pour en savoir plus sur `native_line_id`, consultez [Configuration de l'utilisateur](#user-setup).

{% alert note %}
L'état du groupe d'abonnement ne doit pas être spécifié et sera ignoré. LINE est la source de vérité pour l'état d'abonnement des utilisateurs, qui sera synchronisé avec Braze soit par l'outil de synchronisation des abonnements, soit par des mises à jour d'événements.
{% endalert %}

## Étape 2 : Intégrer le canal LINE

Une fois le processus d'intégration terminé, Braze récupérera automatiquement les followers LINE de ce canal. Pour tous les ID LINE déjà associés à un profil utilisateur Braze, chaque profil sera mis à jour avec le statut « abonné », et tous les ID LINE restants généreront des utilisateurs anonymes. De plus, les nouveaux followers de votre canal LINE verront des profils utilisateurs non identifiés créés lorsqu'ils suivront le canal.

### Étape 2.1 : Modifier les paramètres du webhook

1. Dans LINE, accédez à l'onglet **API de messagerie** et modifiez vos **paramètres de webhook** :
   - Définissez l'**URL du webhook** sur `https://anna.braze.com/line/events`.
      - Braze changera automatiquement cette URL lors de l'intégration, en fonction de votre cluster de tableau de bord.
   - Activez **Utiliser le webhook** et **Redistribution du webhook**. <br><br> ![Page des paramètres du webhook pour vérifier ou modifier l'URL du webhook, activer ou désactiver « Utiliser le webhook », « Redistribution du webhook » et « Agrégation des statistiques d'erreurs ».]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Prenez note des informations suivantes dans l'onglet **Fournisseurs** :

| Type d'information | Emplacement |
| --- | --- |
| ID du fournisseur | Sélectionnez votre fournisseur, puis accédez à ***Paramètres** > **Informations de base** |
| ID du canal | Sélectionnez votre fournisseur, puis accédez à **Canaux** > votre canal > **Paramètres de base** |
| Secret du canal | Sélectionnez votre fournisseur, puis accédez à **Canaux** > votre canal > **Paramètres de base** |
| Jeton d'accès au canal | Sélectionnez votre fournisseur, puis accédez à **Canaux** > votre canal > **API de messagerie**. S'il n'y a pas de jeton d'accès au canal, sélectionnez **Émettre**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3. Accédez à votre page **Paramètres** > **Paramètres de réponse** et procédez comme suit :
   - Désactivez le **message de bienvenue**. Celui-ci peut être géré dans Braze via un déclencheur lors du suivi.
   - Désactivez les **messages de réponse automatique**. Tous les messages déclenchés doivent passer par Braze. Cela ne vous empêchera pas d'envoyer directement depuis la console LINE.
   - Activez les **webhooks**.

![Page des paramètres de réponse avec des commutateurs pour la gestion des discussions par votre compte.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Étape 2.2 : Générer des groupes d'abonnement LINE dans Braze

1. Accédez à la page Partenaires technologiques de Braze pour LINE et saisissez les informations que vous avez notées dans l'onglet **Fournisseurs** de LINE :
   - ID du fournisseur
   - ID du canal
   - Secret du canal
   - Jeton d'accès au canal

Si vous souhaitez ajouter une liste blanche d'adresses IP à votre compte LINE, ajoutez toutes les adresses IP répertoriées pour votre cluster dans la [liste d'autorisation IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting) à votre liste d'autorisation.

{% alert important %}
Lors de l'intégration, veillez à vérifier que votre secret de canal est correct. S'il est incorrect, il peut y avoir des incohérences dans l'état de l'abonnement.
{% endalert %}

![Page d'intégration de messagerie LINE avec la section d'intégration LINE.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. Après la connexion, Braze générera automatiquement un groupe d'abonnement Braze pour chaque intégration LINE ajoutée avec succès à votre espace de travail. <br><br> Toute modification de votre liste de followers (nouveaux followers ou désabonnements) sera automatiquement transmise à Braze.

![Section des groupes d'abonnement LINE affichant un groupe d'abonnement pour le canal « LINE ».]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Étape 3 : Rapprocher les ID utilisateurs

Combinez les ID LINE de vos utilisateurs avec leurs profils utilisateurs Braze existants en suivant les étapes de la section [Rapprochement des ID utilisateurs](#user-id-reconciliation).

## Étape 4 : Modifier vos méthodes de mise à jour des utilisateurs 

Si vous disposez déjà d'une méthode pour fournir des mises à jour utilisateur à Braze, vous devrez la mettre à jour pour inclure le nouveau champ `native_line_id` afin que les mises à jour utilisateur envoyées ultérieurement à Braze incluent ce champ.

Il peut exister dans Braze des profils utilisateurs non identifiés avec un `native_line_id` qui ont été créés dans le cadre du processus de synchronisation de l'état d'abonnement, ou lorsqu'un nouveau follower a suivi votre canal. 

Lorsqu'un utilisateur LINE est identifié dans votre application par le biais de la [réconciliation des utilisateurs](#user-id-reconciliation) ou par d'autres moyens, vous pouvez cibler un profil utilisateur potentiellement non identifié dans Braze à l'aide de l'endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). Chaque profil utilisateur non identifié avec un `native_line_id` possède également un alias d'utilisateur `line_id` qui peut être utilisé pour cibler le profil utilisateur à identifier.

Voici un exemple de PAYLOAD pour `/users/identify` qui cible un profil utilisateur non identifié par l'alias d'utilisateur `line_id` : 

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

Si aucun profil utilisateur n'existe pour l'`external_id` fourni, celui-ci sera ajouté au profil utilisateur non identifié, le rendant ainsi identifié. Si un profil utilisateur existe pour l'`external_id`, tous les attributs présents exclusivement sur le profil utilisateur non identifié seront copiés vers le profil utilisateur connu, y compris `native_line_id` et l'état d'abonnement de l'utilisateur.

Vous pouvez mettre à jour les utilisateurs LINE connus dans votre application via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) en transmettant leurs identifiants externes et `native_line_id`. Si un profil utilisateur non identifié existe déjà pour un utilisateur et que le même `native_line_id` est ajouté à un profil utilisateur différent via `/users/track`, il héritera de tous les états d'abonnement du profil utilisateur non identifié. Cependant, des profils utilisateurs en double existeront avec le même `native_line_id`. Toute mise à jour ultérieure de l'abonnement à la suite d'événements mettra à jour tous les profils en conséquence. 

{% alert note %}
Les états d'abonnement LINE sont suivis par `native_line_id`, et non par `external_id`. Par exemple, si le profil de l'utilisateur B est créé avec le même `native_line_id` que l'utilisateur A, mais pas le même `external_id`, l'utilisateur B héritera de l'état d'abonnement LINE de l'utilisateur A.
{% endalert %}

Voici un exemple de PAYLOAD pour `/users/track` qui met à jour un profil utilisateur par l'ID externe pour ajouter un `native_line_id` : 

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

## Étape 5 : Fusionner les profils (facultatif)

Comme décrit ci-dessus, il est possible que plusieurs profils utilisateurs existent avec le même `native_line_id`. Si vos méthodes de mise à jour créent des profils utilisateurs en double, vous pouvez fusionner les profils utilisateurs non identifiés avec les profils utilisateurs identifiés à l'aide de l'endpoint `/user/merge`. 

Voici un exemple de PAYLOAD pour `/users/merge` qui cible un profil utilisateur non identifié par l'alias d'utilisateur `line_id` :

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

LINE est la source de vérité pour les états d'abonnement des utilisateurs. Même si vous disposez de l'ID LINE d'un utilisateur (`native_line_id`), si cet utilisateur n'a pas suivi le canal LINE depuis lequel vous envoyez des messages, LINE ne lui délivrera pas de messages.

Pour vous aider à gérer cela, Braze propose des outils et une logique qui prennent en charge une base d'utilisateurs bien intégrée, notamment la synchronisation des abonnements et les mises à jour d'événements pour les suivis et désabonnements LINE.

### Synchronisation des abonnements et logique des événements

1. **Outil de synchronisation des abonnements :** Cet outil est automatiquement déployé après une intégration réussie du canal LINE. Utilisez-le pour mettre à jour les profils existants et en créer de nouveaux.<br><br>Tous les profils utilisateurs Braze dont le `native_line_id` suit le canal LINE seront mis à jour avec un statut de groupe d'abonnement `subscribed`. Tout follower du canal LINE qui n'a pas de profil utilisateur Braze avec le `native_line_id` aura :<br><br>- Un profil utilisateur anonyme créé avec `native_line_id` défini sur l'ID LINE de l'utilisateur suivant le canal <br>- Un alias d'utilisateur `line_id` défini sur l'ID LINE de l'utilisateur suivant le canal <br>- Un statut de groupe d'abonnement `subscribed`

{: start="2"}
2. **Mises à jour d'événements :** Elles servent à mettre à jour l'état d'abonnement d'un utilisateur. Lorsque Braze reçoit des mises à jour d'événements utilisateur pour le canal LINE intégré et que l'événement est un suivi, le profil utilisateur aura un statut de groupe d'abonnement `subscribed`. Si l'événement est un désabonnement, le profil utilisateur aura un statut de groupe d'abonnement `unsubscribed`.<br><br>- Tous les profils utilisateurs Braze ayant un `native_line_id` correspondant seront automatiquement mis à jour. <br>- S'il n'existe pas de profil utilisateur correspondant pour un événement, Braze [créera un utilisateur anonyme]({{site.baseurl}}/line/user_management/).

## Cas d'utilisation

Voici des cas d'utilisation montrant comment les utilisateurs peuvent être mis à jour après avoir suivi les étapes de configuration ci-dessus.

##### Un profil utilisateur Braze existant suit déjà le canal LINE

1. Le profil utilisateur Braze est mis à jour avec un attribut `native_line_id`. Son statut d'abonnement par défaut est `unsubscribed`.
2. L'outil de synchronisation des abonnements est exécuté, constate que l'utilisateur suit le canal LINE, puis met à jour le profil utilisateur avec le statut d'abonnement `subscribed`.
3. Si l'état d'abonnement change (par exemple, si l'utilisateur bloque le canal, le supprime de ses amis ou le suit à nouveau), Braze reçoit la mise à jour de LINE et met à jour le profil utilisateur avec le `native_line_id` en conséquence.

##### Un profil utilisateur existant a bloqué, supprimé ou ne suit plus le canal LINE 

1. Le profil utilisateur Braze est mis à jour avec un attribut `native_line_id`. Son statut d'abonnement par défaut est `unsubscribed`.
2. L'outil de synchronisation des abonnements ne constate pas que l'utilisateur suit le canal LINE et le statut d'abonnement de l'utilisateur reste `unsubscribed`.
3. Si l'utilisateur suit ensuite le canal, Braze reçoit la mise à jour de LINE et met à jour le profil utilisateur avec le statut d'abonnement `subscribed`.

##### La création du profil utilisateur intervient après le suivi LINE

1. Le canal reçoit un nouveau follower LINE.
2. Braze crée un profil utilisateur anonyme dont l'attribut `native_line_id` correspond à l'ID LINE du follower et dont l'alias d'utilisateur `line_id` correspond à l'ID LINE du follower. Le profil a un statut d'abonnement `subscribed`.
3. L'utilisateur est identifié comme ayant l'ID LINE par le biais de la [réconciliation des utilisateurs](#user-id-reconciliation).
  - Le profil utilisateur anonyme peut être identifié à l'aide de l'endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). Les mises à jour ultérieures (via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) de ce profil utilisateur peuvent cibler l'utilisateur par cet `external_id` connu.

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

  - Un nouveau profil utilisateur peut être créé (via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) en définissant le `native_line_id`. Ce nouveau profil héritera de l'état d'abonnement du profil utilisateur anonyme existant. Notez que cela entraînera l'existence de plusieurs profils partageant le même `native_line_id`. Ceux-ci peuvent être fusionnés à tout moment à l'aide de l'endpoint `/users/merge` selon la procédure décrite à l'[étape 5](#step-5-merge-profiles-optional).

##### La création du profil utilisateur intervient avant le suivi LINE

1. Vous acquérez un nouvel utilisateur et envoyez l'information à Braze. Un nouveau profil utilisateur est créé (profil 1).
2. L'utilisateur suit votre compte LINE.
3. Braze reçoit un événement de suivi et crée un profil utilisateur anonyme (profil 2).
4. L'utilisateur est identifié comme ayant l'ID LINE par le biais de la [réconciliation des utilisateurs](#user-id-reconciliation).
5. Vous mettez à jour le profil 1 pour définir l'attribut `native_line_id`. Ce profil hérite de l'état d'abonnement du profil 2.
  - Il y a maintenant deux profils utilisateurs avec le même `native_line_id`. Ceux-ci peuvent être fusionnés à tout moment à l'aide de l'endpoint `/users/merge` selon la procédure décrite à l'[étape 5](#step-5-merge-profiles-optional).

## Rapprochement des ID utilisateurs 

Les ID LINE sont automatiquement reçus par Braze lorsqu'un utilisateur suit votre canal, ou lorsque vous utilisez le flux de travail ponctuel « synchroniser les followers ». Les ID LINE sont également spécifiques au canal que les utilisateurs suivent, il est donc peu probable que les utilisateurs puissent fournir leurs ID LINE.

Il existe deux façons de combiner un ID LINE avec un profil utilisateur Braze existant :

- [LINE Login](#line-login)
- [Liaison des comptes utilisateurs](#user-account-linking)

### LINE Login

Cette méthode utilise les identifiants de réseaux sociaux pour le rapprochement. Lorsqu'un utilisateur se connecte à votre application, il a la possibilité d'utiliser [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) pour créer un compte utilisateur ou se connecter.

{% alert note %}
Pour obtenir l'ID LINE correct pour chaque utilisateur, configurez LINE Login sous le même fournisseur que votre compte ou canal officiel LINE intégré à Braze.
{% endalert %}

1. Accédez à la console développeurs LINE et [demandez l'autorisation d'obtenir les adresses e-mail des utilisateurs](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) qui se connectent à votre application via LINE Login.

2. Suivez les étapes appropriées fournies par LINE pour implémenter LINE Login :<br><br>
  - [Instructions pour l'application web](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Instructions pour l'application native](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Veillez à inclure `email` dans la [configuration du scope](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) pour les demandes de vérification. 

{: start="3"}
3. Utilisez l'[appel de vérification du jeton d'ID](https://developers.line.biz/en/reference/line-login/#verify-id-token) pour obtenir l'e-mail de l'utilisateur. 

4. Enregistrez l'ID LINE de l'utilisateur (`native_line_id`) dans le profil de l'utilisateur avec un e-mail correspondant dans votre base de données, ou créez un nouveau profil utilisateur avec l'e-mail et l'ID LINE de l'utilisateur.

5. Envoyez les informations utilisateur nouvelles ou mises à jour à Braze à l'aide de l'[endpoint `/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), de l'[importation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou de l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/).

#### Flux de travail

##### Un follower existant utilise LINE Login

**Scénario :** Un utilisateur anonyme a été créé lors de la synchronisation initiale des abonnés ou après l'intégration via un événement « suivre ».

1. L'utilisateur se connecte à votre application en utilisant LINE Login.
2. LINE vous fournit l'e-mail de l'utilisateur.
3. Vous envoyez à Braze l'utilisateur mis à jour (le profil utilisateur existant avec cet e-mail pour ajouter l'ID LINE) ou vous mettez à jour l'utilisateur anonyme avec l'e-mail.

##### Un nouveau follower utilise LINE Login

**Scénario :** Aucun profil utilisateur n'existe dans Braze avec l'ID LINE de l'utilisateur.

1. L'utilisateur se connecte à votre application en utilisant LINE Login.
2. LINE vous fournit l'e-mail de l'utilisateur.
3. Soit vous :
  - Mettez à jour un profil utilisateur existant avec cet e-mail pour qu'il contienne également l'ID LINE de l'utilisateur.
  - Créez un nouveau profil utilisateur avec l'e-mail et l'ID LINE.
4. Lorsque l'utilisateur suit votre compte officiel LINE, Braze reçoit un événement de suivi et met à jour le statut d'abonnement de l'utilisateur à `subscribed`.

### Liaison des comptes utilisateurs 

Cette méthode permet aux utilisateurs de lier leur compte LINE au compte utilisateur de votre application. Vous pouvez ensuite utiliser Liquid dans Braze, comme {% raw %}`{{line_id}}`{% endraw %}, pour créer une URL personnalisée pour l'utilisateur qui transmet son ID LINE à votre site web ou à votre application, où il peut alors être associé à un utilisateur connu.

1. Créez un Canvas basé sur une action qui repose sur un changement d'état d'abonnement et qui se déclenche lorsqu'un utilisateur s'abonne à votre canal LINE.<br>![Canvas qui se déclenche lorsqu'un utilisateur s'abonne au canal LINE.]({% image_buster /assets/img/line/account_link_1.png %})
2. Créez un message incitant les utilisateurs à se connecter à votre site web ou à votre application, en transmettant l'ID LINE de l'utilisateur en tant que paramètre de requête (via Liquid), par exemple :

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. Créez un message de suivi qui transmet le code de coupon.
4. (Facultatif) Créez une campagne basée sur une action ou un Canvas qui se déclenche lorsque l'utilisateur LINE est identifié pour lui envoyer son code de coupon. <br>![Campagne basée sur une action qui se déclenche lorsque l'utilisateur LINE est identifié.]({% image_buster /assets/img/line/account_link_2.png %})

#### Fonctionnement

Une fois que l'utilisateur s'est connecté, une modification est apportée sur votre site web ou votre application afin que l'ID utilisateur soit renvoyé à Braze pour l'associer à l'ID LINE transmis dans l'URL, avec un exemple de code tel que :

```javascript
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

**Scénario :** Un utilisateur existant dans Braze suit votre canal sur LINE.

1. LINE envoie à Braze un événement de suivi.
2. Braze crée un profil utilisateur anonyme avec l'ID LINE, l'alias d'utilisateur `line_id` et le statut de groupe d'abonnement LINE `subscribed`.
3. L'utilisateur reçoit un message LINE avec un lien vers votre site web et votre application et se connecte. Son profil utilisateur est désormais connu.
4. Le profil utilisateur anonyme créé est identifié et fusionné via l'[endpoint /users/identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) avec le profil utilisateur connu. Le profil utilisateur connu contient désormais l'ID LINE et a un statut d'abonnement `subscribed`.
5. (Facultatif) L'utilisateur reçoit un message LINE avec le code de coupon et Braze enregistre l'envoi dans le profil utilisateur Braze.

## Création d'utilisateurs test LINE dans Braze

Vous pouvez tester votre canal LINE avant de configurer la [réconciliation des utilisateurs](#user-id-reconciliation) en créant un Canvas ou une campagne « Qui suis-je ».

1. Configurez un Canvas qui renvoie l'ID utilisateur Braze d'un utilisateur sur un mot déclencheur spécifique. <br><br>Exemple de déclencheur <br><br>![Déclencheur pour envoyer la campagne aux utilisateurs qui ont envoyé un message LINE entrant à un groupe d'abonnement spécifique.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Exemple de message<br><br>![Message LINE indiquant l'ID utilisateur Braze.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Dans Braze, vous pouvez utiliser l'ID Braze pour rechercher des utilisateurs spécifiques et les modifier selon vos besoins.

{% alert important %}
Assurez-vous que le Canvas n'a pas de contrôle global ou de groupes de contrôle empêchant les envois.
{% endalert %}