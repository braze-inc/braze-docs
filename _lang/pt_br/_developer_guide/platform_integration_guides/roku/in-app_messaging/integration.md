---
nav_title: Integração
article_title: Guia de Integração de mensagem no app para Roku
platform: Roku
page_order: 2
description: "Este guia de referência cobre como integrar mensagens no app para Roku e considerações relevantes de código"
channel:
  - in-app messages
---

# Integração de mensagem no app

> Este guia de implementação cobre considerações de código de mensagem no app e trechos de código acompanhantes. Embora forneçamos código de integração de amostra, você precisará adicionar lógica para lidar e exibir mensagens acionadas na sua interface de usuário desejada. 

Como seu código será exclusivo para seu app, você não precisa lidar com todas as situações listadas se não forem relevantes para seu caso de uso. Por exemplo, se você não usar a exibição atrasada de mensagens no app, não precisará implementar essa lógica e casos extremos.

## Requisitos do SDK {#supported-sdk-versions}

Mensagens no app serão enviadas apenas para dispositivos Roku executando a versão mínima suportada do SDK:

{% sdk_min_versions roku:0.1.2 %}

## Configuração de mensagem no app

Para processar mensagens no app, você pode adicionar um observador em `BrazeTask.BrazeInAppMessage`:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Então, dentro do seu manipulador, você tem acesso à mensagem no app mais alta que suas campanhas dispararam:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## campos de mensagem no app

A seguir estão listados os campos que você precisará para gerenciar suas mensagens no app:

| Campos | Descrição |
| ------ | ----------- |
| `buttons` | Lista de botões (pode ser uma lista vazia). |
| `click_action` | `"URI"` ou `"NONE"`. Use este campo para indicar se a mensagem no app deve abrir um link URI ou fechar a mensagem quando clicado. Quando não houver botões, isso deve acontecer quando o usuário clicar em "OK" quando a mensagem no app for exibida. |
| `dismiss_type` | `"AUTO_DISMISS"` ou `"SWIPE"`. Use este campo para indicar se sua mensagem no app será automaticamente descartada ou se exigirá um deslize para ser descartada. |
| `display_delay` | Quanto tempo (segundos) esperar até exibir a mensagem no app. |
| `duration` | Por quanto tempo (milissegundos) a mensagem deve ser exibida quando `dismiss_type` é configurado para `"AUTO_DISMISS"`. |
| `extras` | Pares chave-valor. |
| `header` | O texto do cabeçalho. |
| `id` | O ID usado para registrar impressões ou cliques. |
| `image_url` | URL da imagem da mensagem no app. |
| `message` | Texto do corpo da mensagem. |
| `uri` | Seus usuários de URI serão enviados com base no seu `click_action`. Este campo deve ser incluído quando `click_action` é `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Para mensagens no app contendo botões, a mensagem `click_action` também será incluída na carga útil final se a ação de clique for adicionada antes de adicionar o texto do botão.
{% endalert %}

### Campos de Estilo
Existem também vários campos de estilo que você pode escolher usar no dashboard:

| Campos | Descrição |
| ------ | ----------- |
| `bg_color` | Cor de fundo. |
| `close_button_color` | Cor do botão de fechar. |
| `frame_color` | A cor da sobreposição da tela de fundo. |
| `header_text_color` | Cor do texto do cabeçalho. |
| `message_text_color` | Cor do texto da mensagem. |
| `text_align` | "INÍCIO", "CENTRO" ou "FIM". Seu alinhamento de texto selecionado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Alternativamente, você poderia implementar a mensagem no app e estilizar dentro do seu aplicativo Roku usando uma paleta padrão:

### Campos de botão

| Campos | Descrição |
| ------ | ----------- |
| `click_action` | `"URI"` ou `"NONE"`. Use este campo para indicar se a mensagem no app deve abrir um link URI ou fechar a mensagem quando clicado. |
| `id` | O valor de ID do próprio botão. |
| `text` | O texto a ser exibido no botão. |
| `uri` | Seus usuários de URI serão enviados com base no seu `click_action`. Este campo deve ser incluído quando `click_action` é `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Lidando com interações

Você precisará garantir que certas funções sejam chamadas para lidar com a análise de dados da sua campanha.

##### Quando uma mensagem é exibida

Quando uma mensagem é exibida ou vista, registre uma impressão:
```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

##### Quando um usuário clica em uma mensagem
Depois que um usuário clica na mensagem, registre um clique e então processe `in_app_message.click_action`:
```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

##### Quando um usuário clica em um botão
Se o usuário clicar em um botão, registre o clique do botão e depois processe `inappmessage.buttons[selected].click_action`:

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

##### Após processar uma mensagem no app
Depois de processar uma mensagem no app, você deve limpar o campo:
```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
