---
nav_title: Migração de tokens por push
article_title: Migração de tokens por push
page_order: 0

page_type: solution
description: "Este artigo de ajuda aborda como migrar tokens por push para que você possa continuar enviando mensagens por push aos seus usuários depois de mudar para o Braze."
channel: push
---

# Migração de tokens por push

Um [token por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) é um identificador anônimo exclusivo que especifica para onde enviar as notificações de um app. A Braze se conecta a provedores de serviço por push, como o Firebase Cloud Messaging Service (FCMs) para Android e o Apple Push Notification Service (APNs) para iOS, e esses provedores enviam tokens de dispositivo exclusivos que identificam seu app. Se você estava enviando notificações por push antes de integrar o Braze, seja por conta própria ou por meio de outro provedor, a migração de token por push permite que você continue enviando notificações por push aos seus usuários com tokens por push registrados.

## Migração automática via SDK

O Braze SDK migrará automaticamente o token por push de um usuário que tenha aceitado anteriormente suas notificações por push na primeira vez em que ele fizer login em seu aplicativo ou site integrado ao Braze. Se você integrar os SDKs da Braze, não precisará migrar os tokens por push usando a API.

No entanto, como os tokens por push migram quando um usuário faz login pela primeira vez no seu app, note que o Braze não poderá enviar notificações por push para usuários que não tenham feito login após a integração do SDK. Talvez ainda queira migrar manualmente os tokens por push do Android e do iOS como uma forma de reengajamento com esses usuários.

{% alert note %}
Devido à natureza dos tokens por push da Web, a cada 60 dias o token expira e é redefinido. Qualquer pessoa que não tenha uma sessão dentro desse período de tempo não terá um token por push da Web ativo. O Braze não migrará tokens por push da Web expirados. Esses usuários precisarão ser engajados novamente por meio de [push primers]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages).
{% endalert %}

## Migração manual via API

A migração manual de token por push é o processo de importação dessas chaves criadas anteriormente para sua plataforma Braze por meio da API.

Migre programaticamente os tokens do iOS (APNs) e do Android (FCM) para sua plataforma usando o [endpoint`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). É possível migrar tanto usuários identificados (usuários com um ID externo associado) quanto usuários anônimos (usuários sem um ID externo).

Especifique o endereço `app_id` do seu aplicativo durante a migração do token por push para associar o token por push apropriado ao aplicativo apropriado. Cada app (iOS, Android, etc.) tem seu próprio `app_id`, que pode ser encontrado na seção **Identificação** da página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Confira se está usando a plataforma correta `app_id`.

{% alert important %}
Não é possível migrar tokens por push da web por meio da API. Isso ocorre porque os tokens por push da Web não estão em conformidade com o mesmo esquema de outras plataformas. 

<br>Se estiver tentando migrar tokens por push da Web de forma programática, poderá ver um erro como o seguinte: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Como alternativa à migração da API, recomendamos que você integre o SDK e permita que sua base de tokens seja preenchida naturalmente.
{% endalert %}

### Migração se a ID externa estiver presente
Para usuários identificados, defina o sinalizador `push_token_import` como `false` (ou omita o parâmetro) e especifique os valores `external_id`, `app_id` e `token` no objeto do usuário `attributes`. 

Por exemplo:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```

### Migração se a ID externa não estiver presente
Ao importar tokens por push de outros sistemas, um `external_id` nem sempre está disponível. Nessa circunstância, defina o sinalizador `push_token_import` como `true` e especifique os valores `app_id` e `token`. A Braze criará um perfil de usuário temporário e anônimo para cada token, a fim de ativar a possibilidade de continuar a enviar mensagens a essas pessoas. Se o token já existir na Braze, a solicitação será ignorada.

Por exemplo:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },
      
    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
      ]
    }
  ]
}'
```

Após a importação, quando o usuário anônimo iniciar a versão do seu app habilitada para o Braze, o Braze moverá automaticamente o token por push importado para o perfil de usuário do Braze e limpará o perfil temporário.

O Braze verificará uma vez por mês para encontrar qualquer perfil anônimo com o sinalizador `push_token_import` que não tenha um token por push. Se o perfil anônimo não tiver mais um token por push, nós o excluiremos. No entanto, se o perfil anônimo ainda tiver um token por push, o que sugere que o usuário real ainda não registrou o dispositivo com o referido token por push, não faremos nada.

## Importação de tokens por push do Android

{% alert important %}
As considerações a seguir só se aplicam a apps Android. Os apps iOS não precisarão dessas etapas porque essa plataforma tem apenas uma estrutura para exibir push, e as notificações por push serão renderizadas imediatamente, desde que o Braze tenha os tokens e certificados de push necessários.
{% endalert %}

Se for necessário enviar notificações por push do Android aos seus usuários antes que a integração do SDK do Braze seja concluída, use pares de valores-chave para validar as notificações por push. 

Você deve ter um receptor para manipular e exibir cargas úteis push. Para notificar o receptor da carga útil do push, adicione os pares de valores-chave necessários à campanha push. Os valores desses pares dependem do parceiro de push específico que você usou antes do Braze.

{% alert note %}
Para alguns provedores de notificações por push, o Braze precisará achatar os pares de valores-chave para que eles possam ser interpretados adequadamente. Para achatar pares de valores-chaves para um app Android específico, entre em contato com o gerente de integração ou de sucesso do cliente.
{% endalert %}

_Última atualização em 5 de dezembro de 2022_
