---
nav_title: "Empfänger:innen Objekt"
article_title: "API Empfänger:innen Objekt"
page_order: 9
page_type: reference
description: "Dieser referenzierte Artikel erläutert die verschiedenen Komponenten des Objekts Empfänger:innen von Braze."

---

# Empfänger:innen Objekt

> Das Empfänger:innen-Objekt erlaubt es Ihnen, Informationen in unseren Endpunkten anzufragen oder zu schreiben.

Entweder `external_user_id`, `user_alias`, `braze_id` oder `email` ist in diesem Objekt erforderlich. **In der Anfrage darf nur eine Angabe gemacht werden.**

Mit dem Empfänger:innen-Objekt können Sie das [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/), das [Objekt für die triggernden Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) und das [Objekt für die Eingangs-Eigenschaften von Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) kombinieren.

## Objektkörper

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "braze_id": (optional, string) see Braze ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}]
```

Wenn `send_to_existing_only` auf `true` steht, sendet Braze die Nachricht nur an bestehende Nutzer:innen. Dieses Flag kann jedoch nicht mit Nutzer:innen verwendet werden. Wenn `send_to_existing_only` `false` ist, muss ein Attribut angegeben werden. Braze erstellt einen Nutzer:innen mit der `id` und den Attributen, bevor die Nachricht gesendet wird.

- [Braze-ID]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [Nutzer-Aliasse]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [Externe Nutzer:innen ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Prioritätensetzung]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)

## Deduplizierung von Empfänger:in-Objekten

Wenn bei einem API-Aufruf mit dem Empfänger-Objekt **ein doppelter Empfänger:in existiert, der auf dieselbe Adresse targetiert (d.h. E-Mail, Push), wird der Nutzer:in dedupliziert**, d.h. identische Nutzer:in werden entfernt, so dass einer übrig bleibt. 

Wenn zum Beispiel dieselbe `external_user_id` verwendet wird, wird nur eine Nachricht empfangen. Ziehen Sie mehrere API-Aufrufe in Betracht, wenn Sie eine Abhilfe für dieses Verhalten benötigen.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```
