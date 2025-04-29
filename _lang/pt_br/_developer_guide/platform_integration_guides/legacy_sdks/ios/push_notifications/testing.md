---
nav_title: Testando
article_title: Testando notificação por push para iOS
platform: iOS
page_order: 29
description: "Este artigo de referência relata o teste de push na linha de comando para suas notificações por push no iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Testando {#push-testing}

Se você quiser testar notificações no app e notificações por push via a linha de comando, você pode enviar uma única notificação através do terminal via CURL e a [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/). Você precisará substituir os seguintes campos pelos valores corretos para o seu caso de teste:

Campos obrigatórios:

- `YOUR-API-KEY-HERE` - disponível em **Configurações** > **Chaves de API**. Confira se a chave está autorizada a enviar mensagens através do endpoint `/messages/send` da REST API. 
- `EXTERNAL_USER_ID` - disponível na página **Pesquisar Usuários**.
- `REST_API_ENDPOINT_URL` - listado nas [Instâncias]({{site.baseurl}}/api/basics/#endpoints. da Braze. Confira se o endpoint corresponde à instância da Braze em que seu espaço de trabalho está.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), essas páginas estão em um local diferente: <br>- **Chaves de API** está localizado em **Console de desenvolvedor** > **Configurações de API** <br>**Pesquisar Usuários** está localizado em **Usuários** > **Pesquisa de Usuários**
{% endalert %}

Campos opcionais:
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```
