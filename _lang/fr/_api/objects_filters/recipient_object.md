---
nav_title: "Objet Destinataire"
article_title: Objet Destinataire de l’API
page_order: 9
page_type: reference
description: "Cet article explique les différents composants de l’objet Destinataire Braze."

---

# Spécification de l’objet Destinataire

L’objet Destinataire vous permet de demander ou d’écrire des informations dans nos endpoints.

`external_user_id` ou `user_alias` est requis dans cet objet. **Les demandes ne doivent en spécifier qu’un seul des deux.**

L’objet Destinataire vous permet de combiner l’[objet Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/), l’[objet Propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), et l’[objet Propriétés d’entrées de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/).

## Corps de l’objet

```json
[{
  "user_alias": (optional, User Alias Object) User Alias of user to receive message,
  "external_user_id": (optional, string) see External User Id,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a Campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}]
```

- [Alias utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [ID utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)

## Déduplication d’objet Destinataire

Lorsque vous effectuez un appel d’API avec l’objet Destinataire, **s’il existe un destinataire dupliqué ciblant la même adresse (par ex. e-mail, notification push), l’utilisateur sera dédupliqué**, ce qui signifie que les utilisateurs identiques seront supprimés. Il n’en restera qu’un. 

Par exemple, si le même `external_user_id` est utilisé, alors un seul message sera reçu. Envisagez de passer plusieurs appels d’API si vous avez besoin d’une solution de contournement pour ce comportement.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```