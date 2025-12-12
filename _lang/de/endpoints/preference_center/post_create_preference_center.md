---
nav_title: "POST: Präferenzzentrum erstellen"
article_title: "POST: Präferenz-Center erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Einstellungszentrum erstellen Braze."

---
{% api %}
# Präferenzzentrum erstellen
{% apimethod post %}
/preference_center/v1
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein Einstellungszentrum zu erstellen, mit dem Nutzer:innen ihre Benachrichtigungspräferenzen für Ihre E-Mail Kampagnen verwalten können. Unter [Erstellen eines Einstellungscenters mit API]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/#creating-a-preference-center-with-api) finden Sie Schritte, wie Sie ein API-generiertes Einstellungscenter erstellen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e15d7065-2cbc-4eb3-ae16-32efe43357a6 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `preference_center.update`.

## Rate-Limit

Für diesen Endpunkt gilt ein Rate-Limits von 10 Anfragen pro Minute und Workspace.

## Anfragetext

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

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`name`| Erforderlich | String | Der Name des Präferenzzentrums, das die folgenden Anforderungen erfüllt: <br>\- Enthält nur Buchstaben, Zahlen, Bindestriche und Unterstriche <br>\- Enthält keine Leerzeichen |
|`preference_center_title`| Optional | String | Der Titel für das Einstellungscenter und die Bestätigungsseiten. Wenn kein Titel angegeben wird, lautet der Titel der Seiten standardmäßig "Einstellungscenter". |
|`preference_center_page_html`| Erforderlich | String | Der HTML-Code für die Seite des Einstellungszentrums. |
|`confirmation_page_html`| Erforderlich | String | Der HTML-Code für die Bestätigungsseite. |
|`state` | Optional | String | Wählen Sie `active` oder `draft`. Der Standardwert ist `active`, wenn nichts angegeben wird. |
|`options` | Optional | Objekt | Attribute: <br>`meta-viewport-content`: Wenn vorhanden, wird der Seite ein `viewport` Meta-Tag mit `content= <value of attribute>` hinzugefügt.<br><br> `link-tags`: Legen Sie ein Favicon für die Seite fest. Wenn diese Option aktiviert ist, wird der Seite ein `<link>` Tag mit einem rel-Attribut hinzugefügt.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Der Name des Einstellungszentrums kann nach seiner Erstellung nicht mehr geändert werden.
{% endalert %}

### Liquid-Tags

Beachten Sie die folgenden Liquid-Tags, die Sie in Ihr HTML einfügen können, um den Status des Abos eines Nutzers:innen auf der Seite des Einstellungszentrums zu generieren.

{% raw %}

#### Status des Nutzer:in

| Liquid | Beschreibung |
| --------- | ---------|
|`{{subscribed_state.${email_global}}}`| Ermittelt den globalen Status des Nutzers:in Bezug auf die abonnierten E-Mails (z.B. "opted_in", "abonniert" oder "abgemeldet"). |
|`{{subscribed_state.${<subscription_group_id>}}}`| Ermittelt den Status des Abonnements der angegebenen Abo-Gruppe für den Nutzer:in (z.B. "abonniert" oder "abgemeldet"). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Formulareingaben und Aktionen

| Liquid | Beschreibung |
| --------- | ---------|
|`{% form_field_name :email_global_state %}`| Zeigt an, dass ein bestimmtes Formulareingabeelement dem globalen E-Mail-Abonnement des Nutzers:in entspricht. Der Auswahlstatus des Nutzers sollte "opted_in", "Abonnent:in" oder "abgemeldet" sein, wenn das Formular mit Auswahldaten für den globalen E-Mail-Abonnentenstatus übermittelt wird. Wenn es sich um ein Kontrollkästchen handelt, wird der Nutzer:in entweder "opted_in" oder "abgemeldet". Bei einer ausgeblendeten Eingabe gilt auch der Status "abonniert". |
|`{% form_field_name :subscription_group <subscription_group_id> %}`| Zeigt an, dass ein bestimmtes Formulareingabeelement einer bestimmten Abo-Gruppe entspricht. Der Auswahlstatus des Nutzers sollte entweder "abonniert" oder "abgemeldet" sein, wenn das Formular mit Auswahldaten für eine bestimmte Abo-Gruppe übermittelt wird. |
|`{{preference_center_submit_url}}`| Erzeugt die URL für die Formularübermittlung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

## Beispielhafte Antworten

### Präferenzzentrum erstellen

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

### HTML mit Formulareingaben

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
