---
nav_title: "PUBLICAR: Crear un centro de preferencias"
article_title: "PUBLICAR: Crear Centro de Preferencias"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Crear un centro de preferencias de Braze."

---
{% api %}
# Crear un centro de preferencias
{% apimethod post %}
/preference_center/v1
{% endapimethod %}

> Utiliza este punto final para crear un centro de preferencias que permita a los usuarios gestionar sus preferencias de notificación para tus campañas de correo electrónico. Consulta [Crear un centro de preferencias con API]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/#creating-a-preference-center-with-api) para saber cómo crear un centro de preferencias generado por API.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e15d7065-2cbc-4eb3-ae16-32efe43357a6 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `preference_center.update`.

## Límite de velocidad

Este punto final tiene un límite de velocidad de 10 solicitudes por minuto, por espacio de trabajo.

## Cuerpo de la solicitud

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

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`name`| Obligatoria | Cadena | El nombre del centro de preferencia que cumpla los siguientes requisitos: <br>\- Sólo contiene letras, números, guiones y guiones bajos <br>\- No tiene espacios |
|`preference_center_title`| Opcional | Cadena | El título para el centro de preferencias y las páginas de confirmación. Si no se especifica un título, el título de las páginas será predeterminado "Centro de preferencias". |
|`preference_center_page_html`| Obligatoria | Cadena | El HTML de la página del centro de preferencias. |
|`confirmation_page_html`| Obligatoria | Cadena | El HTML de la página de confirmación. |
|`state` | Opcional | Cadena | Elige `active` o `draft`. Predetermina `active` si no se especifica. |
|`options` | Opcional | Objeto | Atributos: <br>`meta-viewport-content`: Cuando esté presente, se añadirá una metaetiqueta `viewport` a la página con `content= <value of attribute>`.<br><br> `link-tags`: Establece un favicon para la página. Cuando se establece, se añade a la página una etiqueta `<link>` con un atributo rel.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
El nombre del centro de preferencias no se puede editar una vez creado.
{% endalert %}

### Etiquetas de Liquid

Consulta las siguientes etiquetas de Liquid que puedes incluir en tu HTML para generar el estado de suscripción de un usuario en la página del centro de preferencias.

{% raw %}

#### Estado de suscripción del usuario

| Liquid | Descripción |
| --------- | ---------|
|`{{subscribed_state.${email_global}}}`| Obtiene el estado global de suscripción al correo electrónico del usuario (como "opted_in", "suscrito", o "cancelado". |
|`{{subscribed_state.${<subscription_group_id>}}}`| Obtiene el estado de suscripción del grupo de suscripción especificado para el usuario (como "suscrito" o "cancelado"). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Entradas y acción del formulario

| Liquid | Descripción |
| --------- | ---------|
|`{% form_field_name :email_global_state %}`| Indica que un elemento de entrada de formulario específico corresponde al estado de suscripción global al correo electrónico del usuario. El estado de selección del usuario debe ser "opted_in", "suscrito", o "dado de baja" cuando se envía el formulario con datos de selección para el estado global suscrito al correo electrónico. Si es una casilla de verificación, el usuario se "opted_in" o "cancelará suscripción". Para una entrada oculta, también será válido el estado "suscrito". |
|`{% form_field_name :subscription_group <subscription_group_id> %}`| Indica que un elemento de entrada de formulario concreto corresponde a un grupo de suscripción determinado. El estado de selección del usuario debe ser "suscrito" o "cancelado" cuando el formulario se envía con datos de selección de un grupo de suscripción concreto. |
|`{{preference_center_submit_url}}`| Genera la URL para el envío del formulario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

## Ejemplos de respuestas

### Crear un centro de preferencias

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

### HTML con entradas de formulario

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
