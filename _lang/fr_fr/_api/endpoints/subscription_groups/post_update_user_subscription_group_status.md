---
nav_title: "POST : Mise à jour du statut du groupe d'abonnement des utilisateurs"
article_title: "POST : Mettre à jour le statut du groupe d'abonnement de l'utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Mettre à jour le statut du groupe d'abonnement de l'utilisateur."
---
{% api %}
# Mettre à jour le statut du groupe d'abonnement de l'utilisateur
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour en masse le statut d'abonnement de jusqu'à 50 utilisateurs sur le tableau de bord de Braze.

Vous pouvez accéder au `subscription_group_id` d'un groupe d'abonnement en vous rendant sur la page **Groupe d'abonnement**.

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement e-mail** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement SMS et RCS** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `subscription.status.set`.

{% alert note %}
Si vous souhaitez utiliser cet endpoint avec les [groupes d'abonnement LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/), contactez votre Customer Success Manager.
{% endalert %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Corps de la demande

{% tabs %}
{% tab SMS and RCS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   "use_double_opt_in_logic": (optional, boolean) defaults to `false`; when `subscription_state` is "subscribed", set to `true` to enter the user into the SMS double opt-in workflow,
   // SMS and RCS subscription group - you must include one of external_id or phone
 }
```
\* Groupes d'abonnement SMS et RCS : Braze n'accepte que `external_id` ou `phone`.

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - you must include one of external_id or email
   // Note that sending an email address that is linked to multiple profiles updates all relevant profiles
 }
```
\* Groupes d'abonnement e-mail : Vous devez inclure soit `email`, soit `external_id`.
{% endtab %}
{% endtabs %}

Cette propriété ne doit pas être utilisée pour mettre à jour les informations de profil d'un utilisateur. Utilisez plutôt la propriété [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

{% alert tip %}
**Ajouter des utilisateurs existants à un groupe d'abonnement :** Cet endpoint est la méthode recommandée pour remplir rétroactivement ou mettre à jour en masse l'appartenance à un groupe d'abonnement pour les utilisateurs existants. Vous pouvez transmettre jusqu'à 50 `external_id`, adresses e-mail ou numéros de téléphone par requête. Les utilisateurs peuvent également mettre à jour leur propre statut d'abonnement via un lien de [centre de préférences e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

**Créer de nouveaux utilisateurs avec un groupe d'abonnement :** Lorsque vous créez de nouveaux utilisateurs à l'aide de l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), vous pouvez définir des groupes d'abonnement dans l'objet des attributs de l'utilisateur, ce qui vous permet de créer un utilisateur et de définir l'état du groupe d'abonnement en un seul appel API.
{% endalert %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Requis | Chaîne de caractères | L'`id` de votre groupe d'abonnement. |
| `subscription_state` | Requis | Chaîne de caractères | Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d'abonnement) ou `subscribed` (dans le groupe d'abonnement). |
| `external_id` | Requis* | Tableau de chaînes de caractères | L'`external_id` de l'utilisateur ou des utilisateurs (50 `id`s max). |
| `email` | Requis* | Chaîne de caractères ou tableau de chaînes de caractères | L'adresse e-mail de l'utilisateur, qui peut être transmise sous forme de tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (maximum 50). <br><br>Si plusieurs utilisateurs (`external_id`) du même espace de travail partagent la même adresse e-mail, Braze met à jour tous les utilisateurs partageant cette adresse e-mail avec les modifications du groupe d'abonnement. |
| `phone` | Requis* | Chaîne de caractères au format [E.164](https://en.wikipedia.org/wiki/E.164) | Le numéro de téléphone de l'utilisateur, qui peut être transmis sous forme de tableau de chaînes de caractères. Doit inclure au moins un numéro de téléphone (jusqu'à 50). <br><br>Si plusieurs utilisateurs (`external_id`) du même espace de travail partagent le même numéro de téléphone, Braze met à jour tous les utilisateurs partageant ce numéro de téléphone avec les mêmes modifications du groupe d'abonnement. |
| `use_double_opt_in_logic` | Facultatif | Valeur booléenne | S'applique uniquement aux groupes d'abonnement SMS ; ignoré pour les e-mails et les autres types de groupes d'abonnement. La valeur par défaut est `false` si omis. Pour les groupes d'abonnement SMS, définissez sur `true` pour faire entrer l'utilisateur dans le workflow de [double abonnement SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) lorsque son statut d'abonnement est défini sur `subscribed`. Si ce paramètre est omis ou défini sur `false`, les utilisateurs sont abonnés sans passer par le workflow de double abonnement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemples de requêtes

### E-mail

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

### SMS et RCS

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## Exemple de réponse réussie

Le code de statut `201` peut renvoyer le corps de réponse suivant.

```json
{
    "message": "success"
}
```

{% alert important %}
L'endpoint n'accepte que la valeur `email` ou `phone`, pas les deux. Si vous fournissez les deux, vous recevrez cette réponse : `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}