---
nav_title: "Empfänger Objekt"
article_title: API-Empfänger Objekt
page_order: 9
page_type: reference
description: "Dieser Referenzartikel erklärt die verschiedenen Komponenten des Objekts Braze."

---

# Objekt Empfänger

> Mit dem Empfängerobjekt können Sie Informationen in unseren Endpunkten anfordern oder schreiben.

Entweder `external_user_id`, `user_alias` oder `email` ist in diesem Objekt erforderlich. **In der Anfrage darf nur eine Option angegeben werden.**

{% alert important %}
Die Angabe eines Empfängers über die E-Mail-Adresse ist derzeit in einer frühen Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an diesem frühen Zugang interessiert sind.
{% endalert %}

Mit dem Empfänger-Objekt können Sie das [Benutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/), das [Objekt mit den Auslösereigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) und das [Objekt mit den Eigenschaften des Canvas-Eintrags]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) kombinieren.

## Objektkörper

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}]
```

- [Benutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [Externe Benutzer-ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Prioritätensetzung]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)

## Deduplizierung von Empfängerobjekten

Wenn bei einem API-Aufruf mit dem Empfängerobjekt **ein doppelter Empfänger existiert, der auf dieselbe Adresse abzielt (d.h. E-Mail, Push), wird der Benutzer dedupliziert**, d.h. identische Benutzer werden entfernt, so dass einer übrig bleibt. 

Wenn zum Beispiel dieselbe `external_user_id` verwendet wird, wird nur eine Nachricht empfangen. Ziehen Sie mehrere API-Aufrufe in Betracht, wenn Sie eine Abhilfe für dieses Verhalten benötigen.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```