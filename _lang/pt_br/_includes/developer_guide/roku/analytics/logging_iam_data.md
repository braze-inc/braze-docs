{% multi_lang_include developer_guide/prerequisites/android.md %}

## Envio de mensagens de registro de dados

Você precisará garantir que certas funções sejam chamadas para lidar com a análise de dados da sua campanha.

### Envio de mensagens

Quando uma mensagem é exibida ou vista, registre uma impressão:

```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

### Envio de mensagens clicadas

Depois que um usuário clica na mensagem, registre um clique e então processe `in_app_message.click_action`:

```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

### Botões clicados

Se o usuário clicar em um botão, registre o clique do botão e depois processe `inappmessage.buttons[selected].click_action`:

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

### Após o processamento de uma mensagem

Depois de processar uma mensagem no app, você deve limpar o campo:

```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
