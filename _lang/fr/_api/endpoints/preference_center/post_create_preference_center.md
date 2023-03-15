---
nav_title: "POST : Créer un centre de préférences"
article_title: "POST : Créer un centre de préférences"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article précise des détails concernant l’endpoint de Braze Créer un centre de préférences."

---
{% api %}
# Créer un centre de préférences
{% apimethod post %}
/preference_center/v1
{% endapimethod %}

Utilisez cet endpoint pour créer un centre de préférences pour permettre aux utilisateurs de gérer leurs préférences de notification pour les campagnes par e-mail. Consultez [Créer un centre de préférences par API]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/) pour obtenir des détails sur la manière de l’inclure dans vos campagnes par e-mail.

## Limites de débit

Cet endpoint a une limitation du débit de 10 demandes par minute, par groupe d’apps.

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "name": "string",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "state": (optional) Choose `active` or `draft`. Defaults to `active` if not specified
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`name`| Requis | String | Le nom du centre de préférences qui se conforme aux exigences suivantes : <br>- Comprend uniquement des lettres, des chiffres, des traits d’union et des traits de soulignement <br>- N’a pas d’espaces |
|`preference_center_title`| Facultatif | String | Le titre des pages du centre de préférences et de confirmation. Si aucun titre n’est précisé le titre des pages passera par défaut à « Centre de préférences ». |
|`preference_center_page_html`| Requis | String | L’HTML de la page du centre de préférences. |
|`confirmation_page_html`| Requis | String | L’HTML de la page de confirmation. |
|`state` | Facultatif | String | Choisir `active` ou `draft`. Défini par défaut sur `active` si cela n’est pas spécifié. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
Le nom du centre de préférences ne peut pas être édité une fois qu’il a été créé.
{% endalert %}

### Balises Liquid

Référez-vous aux balises Liquid suivantes qui peuvent être intégrées à votre HTML pour générer un état d’abonnement de l’utilisateur sur la page du centre de préférences.

{% raw %}

#### État d’abonnement utilisateur

| Liquid | Description |
| --------- | ---------|
|`{{subscribed_state.${email_global}}}`| Obtenir l’état global d’abonnement aux e-mails de l’utilisateur (« opted_in », « abonné » ou « désabonné »). |
|`{{subscribed_state.${<subscription_group_id>}}}`| Obtenir l’état global d’abonnement du groupe d'abonnement donné pour l’utilisateur (« abonné » ou « désabonné »). |
{: .reset-td-br-1 .reset-td-br-2}

#### Saisies de formulaire et action

| Liquid | Description |
| --------- | ---------|
|`{% form_field_name :email_global_state %}`| Indique qu’un élément de saisie de formulaire particulier correspond à l’état global d’abonnement aux e-mails de l’utilisateur. L’état de sélection de l’utilisateur devrait être « opted_in », « abonné » ou « désabonné » lorsque le formulaire est soumis avec des données de sélection pour l’état global d’abonnement aux e-mails. S’il s’agit d’une case à cocher, l’utilisateur sera « opted_in » ou « désabonné ». Pour un input caché, l’état « abonné » sera aussi valide. |
|`{% form_field_name :subscription_group <external_id> %}`| Indique qu’un élément de saisie de formulaire particulier correspond à un groupe d'abonnement particulier. L’état de sélection de l’utilisateur devrait être « abonné » ou « désabonné » lorsque le formulaire est soumis avec des données de sélection pour un groupe d'abonnement particulier. |
|`{{preference_center_submit_url}}`| Produit une URL pour la soumission du formulaire. |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

## Exemple de réponse
{% raw %}
```
{
  "preference_center_api_id": "preference_center_api_id_example",
  "liquid_tag": "{{preference_center.${MyPreferenceCenter2022-09-22}}}",
  "created_at": "2022-09-22T18:28:07+00:00",
  "message": "success"
}
```
{% endraw %}

{% endapi %}
