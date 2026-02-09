---
nav_title: "Objeto destinatários"
article_title: Objeto de destinatários da API
page_order: 9
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de receptores Braze."

---

# Objeto destinatários

> O objeto recipients permite que você solicite ou grave informações em nossos endpoints.

Você deve incluir um dos `external_user_id`, `user_alias`, `braze_id` ou `email` neste objeto. **As solicitações devem especificar apenas uma.**

O objeto de destinatários permite combinar o [objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/), o [objeto de propriedades de disparo]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), o [objeto de propriedades de canva]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) e o [objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

## Corpo do objeto

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

Quando `send_to_existing_only` é `true`, a Braze envia a mensagem apenas para usuários existentes. No entanto, você não pode usar essa flag com aliases de usuário. Quando `send_to_existing_only` é `false`, você deve incluir um atributo. A Braze cria um usuário com o `id` e atributos antes de enviar a mensagem.

- [ID da Braze]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [Alias do usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [ID de usuário externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Priorização]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [Objeto de atribuições do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## Eliminação de objetos do destinatário

Ao fazer uma chamada de API com o objeto de destinatário, **se existir um destinatário duplicado direcionando para o mesmo endereço (ou seja, e-mail, push), a Braze remove duplicatas do usuário**, o que significa que a Braze remove usuários idênticos, deixando apenas um.

Por exemplo, se você usar o mesmo `external_user_id`, o usuário receberá apenas uma mensagem. Considere fazer várias chamadas à API se precisar de uma solução alternativa para esse comportamento.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
