---
nav_title: "Objekt Empfänger"
article_title: "API Empfänger:innen Objekt"
page_order: 9
page_type: reference
description: "Dieser referenzierte Artikel erläutert die verschiedenen Komponenten des Objekts Empfänger:innen von Braze."

---

# Empfänger:innen Objekt

> Das Empfänger:innen-Objekt erlaubt es Ihnen, Informationen in unseren Endpunkten anzufragen oder zu schreiben.

Bitte fügen Sie eines der `external_user_id`folgenden Elemente in dieses `email`Objekt ein: `user_alias`, `braze_id`, , oder . **In der Anfrage darf nur eine Angabe gemacht werden.**

Mit dem Empfängerobjekt können Sie das [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/), das [Triggereigenschafts-Objekt]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), das [Canvas-Objekt mit Eingangs-Eigenschaften]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) und das [Benutzer-Attribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/) kombinieren.

## Objektkörper

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "braze_id": (optional, string) see Braze ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "context": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas context object,
  "send_to_existing_only": (optional, boolean) defaults to true; cannot be used with user aliases,
  "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
}]
```

Wenn`send_to_existing_only`  ist`true`, sendet Braze die Nachricht nur an bestehende Nutzer:innen. Bitte beachten Sie, dass Sie dieses Flag nicht mit Benutzer-Aliasen verwenden können. Wenn`send_to_existing_only`  ist`false`, müssen Sie ein Attribut angeben. Braze erstellt einen Nutzer mit den `id`Attributen, bevor die Nachricht gesendet wird.

- [Braze-ID]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [Nutzer-Aliasse]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [Externe Nutzer:innen ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Prioritätensetzung]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [Nutzer:innen Attribute Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## Deduplizierung von Empfänger:in-Objekten

Wenn Sie einen API-Aufruf mit dem Empfängerobjekt durchführen und **ein doppelter Empfänger mit derselben Adresse (d. h. E-Mail, Push) vorhanden ist, führt Braze eine Deduplizierung der Nutzer:innen durch**, d. h. Braze entfernt identische Nutzer:innen und behält nur einen.

Wenn Sie beispielsweise dasselbe verwenden, erhält der Nutzer`external_user_id`:in nur eine Nachricht. Ziehen Sie mehrere API-Aufrufe in Betracht, wenn Sie eine Abhilfe für dieses Verhalten benötigen.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
