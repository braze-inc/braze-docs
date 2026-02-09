---
nav_title: "Objet Destinataire"
article_title: Objet Destinataire de l’API
page_order: 9
page_type: reference
description: "Cet article de référence explique les différents composants de l’objet Destinataire Braze."

---

# Objet Destinataire

> L’objet Destinataire vous permet de demander ou d’écrire des informations dans nos endpoints.

Vous devez inclure l'un des objets suivants : `external_user_id`, `user_alias`, `braze_id`, ou `email` dans cet objet. **Les demandes ne doivent en spécifier qu’un seul des deux.**

L'objet destinataire vous permet de combiner l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/), l'[objet propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), l'[objet propriétés de l'entrée Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) et l'[objet attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

## Corps de l’objet

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "braze_id": (optional, string) see Braze ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties,
  "send_to_existing_only": (optional, boolean) defaults to true; cannot be used with user aliases,
  "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
}]
```

Lorsque `send_to_existing_only` est `true`, Braze n'envoie le message qu'aux utilisateurs existants. Toutefois, vous ne pouvez pas utiliser ce drapeau avec les aliasing de l'utilisateur. Lorsque `send_to_existing_only` est `false`, vous devez inclure un attribut. Braze crée un utilisateur avec le site `id` et les attributs avant d'envoyer le message.

- [ID Braze]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [Alias utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [ID utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Détermination de l’ordre de priorité]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [Objet Attributs d’utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## Déduplication d’objet Destinataire

Lors d'un appel API avec l'objet destinataire, **s'il existe un destinataire dupliqué ciblant la même adresse (c'est-à-dire e-mail, push),** Braze **dédouble l'utilisateur**, ce qui signifie que Braze supprime les utilisateurs identiques, pour n'en laisser qu'un seul.

Par exemple, si vous utilisez le même `external_user_id`, l'utilisateur ne reçoit qu'un seul message. Envisagez de faire plusieurs appels à l'API si vous avez besoin d'une solution de contournement pour ce comportement.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
