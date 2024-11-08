---
nav_title: Solução de problemas
article_title: Solução de problemas de push para FireOS
platform: FireOS
page_order: 20
page_type: solution
description: "Este artigo de referência fornece cenários de solução de problemas do FireOS para possíveis problemas que você possa ter com as notificações por push."
channel: push

---

# Solução de problemas

> Este artigo apresenta vários cenários de solução de problemas do FireOS.

## Utilização dos registros de erros do push

O Braze fornece notificações por push de erros no registro de atividades de mensagens. Esse registro de erros fornece uma variedade de avisos que podem ser muito úteis para identificar por que suas campanhas não estão funcionando como esperado. Ao clicar em uma mensagem de erro, o sistema redirecionará você para a documentação relevante que ajudará a solucionar um incidente específico.

![]({% image_buster /assets/img_archive/message_activity_log.png %})

## Cenários de solução de problemas

### Nenhum usuário "push registrado" é exibido no dashboard da Braze (antes do envio de mensagens)

- Certifique-se de que seu app esteja configurado corretamente para permitir notificações por push.
- Certifique-se de que o ID do cliente e o segredo do cliente configurados em seu dashboard do Braze estejam corretos.

### As notificações por push não são exibidas nos dispositivos dos usuários

Há alguns motivos pelos quais isso pode estar ocorrendo:

- Se você forçar o encerramento do aplicativo, as notificações por push não serão exibidas enquanto o app não estiver em execução.
- Certifique-se de que a configuração [Notification Priority]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/fireos/customization/advanced_settings/#notification-display-priority) esteja definida como `HIGH` em sua campanha.
- A chave de API do ADM em seu site `api_key.txt` está incorreta ou contém caracteres inválidos.
- O `BrazeAmazonDeviceMessagingReceiver` não está registrado corretamente em `AndroidManifest.xml` com filtros de intenção para `<action android:name="com.amazon.device.messaging.intent.RECEIVE" />` e `<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />`.

### Os usuários "Push registrados" não são mais ativados após o envio de mensagens

Isso geralmente ocorre quando os usuários desinstalam o aplicativo, fazendo com que a ID de registro do ADM se torne inválida.

