---
nav_title: "POST : Créer un centre de préférences"
article_title: "POST : Créer un centre de préférences"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article détaille l'endpoint Braze Créer un centre de préférences."

---
{% api %}
# Créer un centre de préférences
{% apimethod post %}
/preference_center/v1
{% endapimethod %}

> Utilisez cet endpoint pour créer un centre de préférences permettant aux utilisateurs de gérer leurs préférences de notification pour vos campagnes d'e-mail. Consultez la section [Créer un centre de préférences avec l'API]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/#creating-a-preference-center-with-api) pour découvrir les étapes de création d'un centre de préférences généré par API.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e15d7065-2cbc-4eb3-ae16-32efe43357a6 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `preference_center.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='post or put preference center' %}

## Corps de la requête

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
  "state": (optional) Choose `active` or `draft`. Defaults to `active` if not specified,
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag,
    "links-tags": [
      {
        "rel": "string", (required) One of the following "icon", "shortcut icon", or "apple-touch-icon",
        "type": "string", (optional) Valid values include "image/png", "image/svg", "image/gif", "image/x-icon", "image/svg+xml", "mask-icon",
        "sizes": "string", (optional),
        "color": "string", (optional) Use when type="mask-icon",
        "href": "string", (required)
      }
    ]
  }
}
```

## Paramètres de la requête

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`name`| Requis | Chaîne de caractères | Le nom du centre de préférences, qui doit respecter les exigences suivantes : <br>- Contient uniquement des lettres, des chiffres, des tirets et des underscores <br>- Ne contient pas d'espaces |
|`preference_center_title`| Facultatif | Chaîne de caractères | Le titre des pages du centre de préférences et de confirmation. Si aucun titre n'est spécifié, le titre des pages sera par défaut « Preference Center ». |
|`preference_center_page_html`| Requis | Chaîne de caractères | Le code HTML de la page du centre de préférences. |
|`confirmation_page_html`| Requis | Chaîne de caractères | Le code HTML de la page de confirmation. |
|`state` | Facultatif | Chaîne de caractères | Choisissez `active` ou `draft`. Par défaut `active` si non spécifié. |
|`options` | Facultatif | Objet | Attributs : <br>`meta-viewport-content` : si présent, une balise méta `viewport` sera ajoutée à la page avec `content= <value of attribute>`.<br><br> `link-tags` : permet de définir un favicon pour la page. Lorsque cette option est définie, une balise `<link>` avec un attribut rel est ajoutée à la page.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Le nom du centre de préférences ne peut pas être modifié après sa création.
{% endalert %}

### Étiquettes Liquid

Voici les étiquettes Liquid que vous pouvez inclure dans votre HTML pour afficher l'état d'abonnement d'un utilisateur sur la page du centre de préférences.

{% raw %}

#### État d'abonnement de l'utilisateur

| Liquid | Description |
| --------- | ---------|
|`{{subscribed_state.${email_global}}}`| Récupère l'état d'abonnement global aux e-mails de l'utilisateur (par exemple « opted_in », « subscribed » ou « unsubscribed »). |
|`{{subscribed_state.${<subscription_group_id>}}}`| Récupère l'état d'abonnement de l'utilisateur pour le groupe d'abonnement spécifié (par exemple « subscribed » ou « unsubscribed »). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Champs de formulaire et action

| Liquid | Description |
| --------- | ---------|
|`{% form_field_name :email_global_state %}`| Indique qu'un champ de formulaire donné correspond à l'état d'abonnement global aux e-mails de l'utilisateur. L'état de sélection de l'utilisateur doit être « opted_in », « subscribed » ou « unsubscribed » lors de la soumission du formulaire avec les données de sélection pour l'état d'abonnement global aux e-mails. S'il s'agit d'une case à cocher, l'utilisateur sera soit « opted_in », soit « unsubscribed ». Pour un champ masqué, l'état « subscribed » est également valide. |
|`{% form_field_name :subscription_group <subscription_group_id> %}`| Indique qu'un champ de formulaire donné correspond à un groupe d'abonnement spécifique. L'état de sélection de l'utilisateur doit être « subscribed » ou « unsubscribed » lors de la soumission du formulaire avec les données de sélection pour un groupe d'abonnement donné. |
|`{{preference_center_submit_url}}`| Génère l'URL de soumission du formulaire. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

## Exemples de réponses

### Créer un centre de préférences

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

### HTML avec champs de formulaire

{% raw %}
```
<!doctype html>
<html lang="en">
  <head>
    <meta name="robots" content="noindex" />
    <title>Email Preferences</title>
    <script type="text/javascript">
      window.onload = () => {
        const globalUnsubscribed = '{{subscribed_state.${email_global}}}' == "unsubscribed";
        const globalSubscribedValue = '{{subscribed_state.${email_global}}}' == "opted_in" ? "opted_in" : "subscribed";
        const idStates = [
          // input format: [API_ID, '{{subscribed_state.${API_ID}}}' == "subscribed"][]
          ['3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec', '{{subscribed_state.${3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec}}}' == 'subscribed'],['7d89bdc3-4aa1-4592-8b8a-4c8b7161c875', '{{subscribed_state.${7d89bdc3-4aa1-4592-8b8a-4c8b7161c875}}}' == 'subscribed'],['5444d32e-2815-4258-964c-b9690d4ccb94', '{{subscribed_state.${5444d32e-2815-4258-964c-b9690d4ccb94}}}' == 'subscribed']
        ];

        const setState = (id, subscribed) => {
          document.querySelector(`#checkbox-${id}`).checked = subscribed;
          document.querySelector(`#value-${id}`).value = subscribed ? "subscribed" : "unsubscribed";
        };
        const setGlobal = (unsubscribed) => {
          document.querySelector(`#checkbox-global`).checked = unsubscribed;
          document.querySelector(`#value-global`).value = unsubscribed ? "unsubscribed" : globalSubscribedValue;
          idStates.forEach(([id]) => {
            document.querySelector(`#checkbox-${id}`).disabled = unsubscribed;
          });
        };

        idStates.forEach(([id, state]) => {
          setState(id, state);
          document.querySelector(`#checkbox-${id}`).onchange = ((e) => {
            setState(id, e.target.checked);
          });
        });
        setGlobal(globalUnsubscribed);
        document.querySelector(`#checkbox-global`).onchange = ((e) => {
          setGlobal(e.target.checked);
        });
      };
    </script>
    <style>
      body {
        background: #fff;
        margin: 0;
      }
      @media (max-width: 600px) {
        .main-container {
          margin-top: 0;
          width: 100%;
        }
        .main-container .content .email-input {
          width: 100%;
        }
      }
    </style>
  </head>
  <body class="vsc-initialized" style="margin: 0" bgcolor="#fff">
    <div
      class="main-container"
      style="
        background-color: #fff;
        color: #333335;
        font-family:
          Sailec W00 Medium,
          helvetica,
          arial,
          sans-serif;
        margin-left: auto;
        margin-right: auto;
        margin-top: 30px;
        width: 600px;
        padding: 15px 0 5px;
      "
    >
      <div class="content" style="margin-left: 20px; margin-right: 20px">

        <div>
          <h1
            style="color: #3accdd; font-size: 27px; font-weight: 400; margin-bottom: 40px; margin-top: 0"
            align="center"
          >
            Manage Email Preferences
          </h1>
          <p class="intro-text" style="font-size: 14px; margin-bottom: 20px" align="center">
            Select the emails that you want to receive.
          </p>
        </div>

        <form action="{{ preference_center_submit_url }}" method="post" accept-charset="UTF-8">
          <div>
            <h3 style="font-size: 15px; margin-bottom: 15px; margin-left: 5px; margin-top: 40px">
              Email Address: <span class="displayed-email" style="font-weight: 400">{{${email_address}}}</span>
            </h3>
          </div>
          <div class="subscription-groups-holder" style="margin-bottom: 20px"><div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
  <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
    <input type="checkbox" id="checkbox-3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec" class="sub_group" style="margin-right: 4px;">
    <input type="hidden" name="{% form_field_name :subscription_group 3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec %}" id="value-3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec" />
    Sub Group 1
  </label>
  <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">

  </p>
</div>
<div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
  <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
    <input type="checkbox" id="checkbox-7d89bdc3-4aa1-4592-8b8a-4c8b7161c875" class="sub_group" style="margin-right: 4px;">
    <input type="hidden" name="{% form_field_name :subscription_group 7d89bdc3-4aa1-4592-8b8a-4c8b7161c875 %}" id="value-7d89bdc3-4aa1-4592-8b8a-4c8b7161c875" />
    Sub Group 2
  </label>
  <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">

  </p>
</div>
<div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
  <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
    <input type="checkbox" id="checkbox-5444d32e-2815-4258-964c-b9690d4ccb94" class="sub_group" style="margin-right: 4px;">
    <input type="hidden" name="{% form_field_name :subscription_group 5444d32e-2815-4258-964c-b9690d4ccb94 %}" id="value-5444d32e-2815-4258-964c-b9690d4ccb94" />
    Sub Group 3
  </label>
  <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">

  </p>
</div>
</div>

          <div class="unsub-all" style="cursor: pointer; font-size: 13px; margin-bottom: 20px" align="center">
            <label>
              <input type="checkbox" id="checkbox-global" />
              <input
                type="hidden"
                id="value-global"
                name="{% form_field_name :email_global_state %}"
              />
              <i> Unsubscribe from all of the above types of emails </i>
            </label>
          </div>

          <div>
            <input
              class="save"
              type="submit"
              value="Save"
              style="
                background-color: rgb(71, 204, 163);
                color: #fff;
                cursor: pointer;
                display: block;
                font-size: 16px;
                text-align: center;
                text-decoration: none;
                width: 200px;
                margin: 0 auto 20px;
                padding: 12px;
                border-style: none;
              "
            />
          </div>
        </form>
      </div>
    </div>
  </body>
</html>
```
{% endraw %}

{% endapi %}