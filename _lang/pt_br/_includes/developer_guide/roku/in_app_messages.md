{% multi_lang_include developer_guide/prerequisites/roku.md %} Além disso, as mensagens no app só serão enviadas para dispositivos Roku que estejam executando a versão mínima suportada do SDK:

{% sdk_min_versions roku:0.1.2 %}

## Tipos de mensagens

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Ativação de mensagens no app

### Etapa 1: Adicionar um observador

Para processar mensagens no app, você pode adicionar um observador em `BrazeTask.BrazeInAppMessage`:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### Etapa 2: Acesso a mensagens disparadas

Então, dentro do seu manipulador, você tem acesso à mensagem no app mais alta que suas campanhas dispararam:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Campos de mensagens

### Manuseio

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

### Estilo

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

### Botões

| Campos | Descrição |
| ------ | ----------- |
| `click_action` | `"URI"` ou `"NONE"`. Use este campo para indicar se a mensagem no app deve abrir um link URI ou fechar a mensagem quando clicado. |
| `id` | O valor de ID do próprio botão. |
| `text` | O texto a ser exibido no botão. |
| `uri` | Seus usuários de URI serão enviados com base no seu `click_action`. Este campo deve ser incluído quando `click_action` é `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
