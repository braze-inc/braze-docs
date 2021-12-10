---
nav_title: "Objet Destinataires"
article_title: Objet Destinataires de l'API
page_order: 9
page_type: Référence
description: "Cet article explique les différentes composantes de l'objet Braze Recipients."
---

# Spécification de l'objet destinataire

L'objet Destinataires vous permet de demander ou d'écrire des informations dans nos terminaux.

Soit `external_user_id` ou `user_alias` est requis dans cet objet. __Les demandes ne doivent préciser qu'une seule.__

L'objet Destinataires vous permet de combiner l'objet [Alias Utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/), l'objet [Propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), et l'objet [Propriétés de l'entrée du canevas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/).

## Corps de l'objet

```json
[{
  "user_alias": (optionnel, objet User Alias) Alias de l'utilisateur pour recevoir le message,
  "external_user_id": (optionnel, string) voir "Id utilisateur externe",
  "trigger_properties": (optionnel, objet) paires clé-valeur de personnalisation pour cet utilisateur lors de l'envoi d'une campagne ou d'un message ; voir Propriétés du déclencheur,
  "canvas_entry_properties": (optionnel, objet) paires clé-valeur pour cet utilisateur lors du déclenchement d'un Canvas ; voir Propriétés de l'entrée de Canvas
}]
```

## Délai de l'objet destinataire

Lors d'un appel API avec l'objet destinataire, __s'il existe un destinataire dupliqué ciblant la même adresse (par exemple, e-mail, e-mail) push), l'utilisateur sera déduit__, ce qui signifie que les utilisateurs identiques seront supprimés, en laissant un.

Par exemple, si le même `external_user_id` est utilisé, alors un seul message sera reçu. Envisagez de faire plusieurs appels API si vous avez besoin d'un contournement pour ce comportement.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```