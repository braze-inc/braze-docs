---
nav_title: "Objet de destinataire"
article_title: Objet de destinataire de l’API
page_order: 9
page_type: référence
description: "Cet article explique les différents composants de l’objet de destinataire Braze."

---

# Spécification de l’objet de destinataire

L’objet de destinataire vous permet de demander ou d’écrire des informations dans nos endpoints.

`external_user_id` ou `user_alias` est requis dans cet objet. **Les demandes ne doivent en spécifier qu’un seul des deux.**

L’objet de destinataire vous permet de combiner l’[objet alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/), l’[objet propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), et l’[objet propriétés d’entrées de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/).

## Corps de l’objet

```json
[{
  "user_alias": (optional, User Alias Object) Alias d’utilisateur de l’utilisateur qui doit recevoir le message,
  "external_user_id": (optional, string) voir ID utilisateur externe.,
  "trigger_properties": (optional, object) paires clé-valeur de personnalisation pour cet utilisateur lors de l’envoi d’une campagne ou d’un message ; voir propriétés du déclencheur,
  "canvas_entry_properties": (optional, object) paires clé-valeur de personnalisation pour cet utilisateur lors du déclenchement d’un Canvas ; voir propriétés de l’entrée Canvas
}]
```

## Déduplication d’objet de destinataire

Lorsque vous effectuez un appel d’API avec l’objet de destinataire, **s’il existe un destinataire dupliqué ciblant la même adresse (par ex. e-mail, notification push), l’utilisateur sera dédupliqué**, ce qui signifie que les utilisateurs identiques seront supprimés. Il n’en restera qu’un. 

Par exemple, si le même `external_user_id` est utilisé, alors un seul message sera reçu. Envisagez de passer plusieurs appels d’API si vous avez besoin d’une solution de contournement pour ce comportement.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```