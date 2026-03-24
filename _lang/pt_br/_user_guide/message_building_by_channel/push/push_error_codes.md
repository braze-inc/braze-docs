---
nav_title: Mensagens comuns de erro de push
article_title: Mensagens comuns de erro de push
page_order: 22
page_type: reference
description: "Este artigo cobre mensagens de erro comuns relacionadas a push para iOS e Android, e orienta você sobre soluções potenciais."
channel: push
platform:
- iOS
- Android
---

# Mensagens comuns de erro de push

> Esta página cobre mensagens de erro comuns para envio de mensagens por push.

{% tabs %}
{% tab Android %} 
### Push com bounce: MismatchSenderId
`MismatchSenderId` indica uma falha de autenticação. O Firebase Cloud Messaging (FCM) autentica com alguns dados principais: senderID e chave de API do FCM.  Ambos devem ser validados quanto à precisão. Para saber mais, veja a [documentação do Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) sobre este problema.

Falhas comuns podem incluir:
- [senderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) incorreto
- Registro múltiplo caso se registrem com outro serviço de push com um senderID diferente

### Push com bounce: InvalidRegistration
`InvalidRegistration` pode acontecer quando um token por push está malformado. Falhas comuns podem incluir quando:
- As pessoas estão passando tokens de registro da Braze manualmente, mas não chamam `getToken()`. Por exemplo, elas podem passar o ID da instância inteira. O token na mensagem de erro se parece com `&#124;ID&#124;1&#124;:[regular token]`.  
- As pessoas estão se registrando em vários serviços. Atualmente, esperamos que as intenções de registro de push cheguem no estilo antigo, então, se as pessoas estiverem se registrando em vários lugares e capturarmos intenções de outros serviços, podemos obter tokens de push malformados.

### Push com bounce: NotRegistered {#notregistered}
`NotRegistered` geralmente significa que o app foi excluído do dispositivo (como nosso sinal para desinstalação). Isso também pode ocorrer se houver vários registros e um segundo registro estiver invalidando o token por push que a Braze recebe.

### DEVICE_UNREGISTERED {#device-unregistered}

Este erro aparece no Registro de Atividade de Mensagens como:

`Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

Isso geralmente ocorre por um dos seguintes motivos:

- O usuário desinstalou o app. Esta é a causa mais comum. Quando o app é removido de um dispositivo, o token por push se torna inválido.
- As credenciais de push foram atualizadas no app. Se sua equipe alterou as credenciais ou certificados do FCM incluídos no app, os usuários que se registraram com as credenciais anteriores terão tokens inválidos até que o app os registre novamente.
- Uma lógica personalizada está cancelando o registro de usuários do push. Isso é raro, mas é tecnicamente possível cancelar programaticamente o registro de um dispositivo do push usando o SDK do Firebase/Android.

{% alert note %}
Este erro não significa que o usuário está com push desativado — apenas que um token específico foi removido do perfil dele. Isso é comum para usuários que estão testando funcionalidades e frequentemente instalando e desinstalando o app. Para verificar se o usuário ainda possui tokens válidos, acesse **Pesquisa de Usuário** e revise a seção **Configurações de Contato** na guia **Engajamento**.
{% endalert %}

{% endtab %}
{% tab iOS %}

### Erro ao enviar push porque a carga útil era inválida

Esta mensagem pode aparecer na guia **Engajamento** do perfil do usuário em **Configurações de Contato** > **Changelog de Push** quando o serviço de Notificações por Push da Apple (APNs) rejeita a solicitação de push devido a uma carga útil inválida.

Na Braze, esta mensagem no dashboard pode corresponder a uma das seguintes razões de erro do APNs:

- `PayloadEmpty`: A carga útil estava sem o conteúdo necessário para o tipo de push sendo enviado.
- `PayloadTooLarge`: A carga útil excedeu o tamanho máximo de carga útil do APNs.

Causas comuns incluem:

- Chaves personalizadas (e seus valores) tornando a carga útil muito grande (isso pode incluir valores renderizados em Liquid inesperadamente grandes).
- Um alerta ou corpo vazio ou ausente onde necessário (ou uma carga útil `aps` malformada).

Próximos passos:

- Reduza o tamanho da carga útil cortando chaves personalizadas e encurtando valores dinâmicos grandes.
- Se você enviar pela API, valide a carga útil JSON final (incluindo o tamanho) antes de enviar.

### Push com bounce: BadToken

O erro `BadToken` pode ocorrer por várias razões:
- O token por push não está sendo enviado para a Braze corretamente (por exemplo, em `registerDeviceToken:` ou o equivalente da sua plataforma).
	- Verifique o token no [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Ele deve geralmente parecer uma longa sequência de letras e números (como `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Se não parecer, verifique o código envolvido no envio do token por push para a Braze.<br><br>
- Ambiente de provisionamento incompatível:
	- Se você se registrar com um certificado de desenvolvimento e tentar enviar com um de produção, poderá ver este erro.  
	- A Braze só suporta certificados universais para ambientes de produção. Testar push em ambientes de desenvolvimento com um certificado universal não funcionará. 
	- Este relatório envia bounces na produção, mas não no desenvolvimento.<br><br>
- Perfil de provisionamento incompatível:
	- Isso pode acontecer se o seu certificado não corresponder ao que foi usado para obter o token. Se isso for suspeito, os próximos passos incluem:
		- Garantir que o certificado de push sendo usado para enviar push pelo dashboard da Braze e o perfil de provisionamento estejam configurados corretamente.
		- Recriar a certificação APNS e depois recriar o perfil de provisionamento após o certificado APNS ser configurado para o `app_id`. Isso pode às vezes resolver alguns problemas mais visíveis.

### Bundle ID não permitido

O erro `TopicDisallowed` significa que o APNs rejeitou o push porque o tópico (bundle ID) na solicitação não é permitido para as credenciais de autenticação sendo usadas. Para resolver isso:

1. **Verifique o bundle ID.** Confirme que o bundle ID configurado nas configurações do seu app na Braze corresponde exatamente ao bundle ID do seu app. Isso inclui quaisquer variações de sufixo (por exemplo, `.debug`, `.staging`).
2. **Verifique sua configuração de autenticação APNs.** Confirme que seu app está configurado com a chave `.p8` correta do APNs e que a chave está associada ao mesmo Apple Developer Team do app para o qual você está enviando.
3. **Confirme o ambiente do app.** Se você tem App IDs separados na Braze para builds de desenvolvimento e produção, verifique se cada um está configurado com as credenciais de push e o ambiente corretos.

### Unregistered {#ios-unregistered}

Este erro aparece no Registro de Atividade de Mensagens como:

`Received 'Unregistered' sending to '[Token String]'`

Este é o equivalente iOS do erro [DEVICE_UNREGISTERED](#device-unregistered) do Android. Geralmente ocorre por um dos seguintes motivos:

- O usuário desinstalou o app. Esta é a causa mais comum.
- Os certificados de push foram atualizados. Se sua equipe alterou ou renovou os certificados APNs, os usuários que se registraram com os certificados anteriores podem ter tokens inválidos até que o app os registre novamente.
- Uma lógica personalizada está cancelando o registro de usuários do push. Isso é raro, mas é tecnicamente possível cancelar programaticamente o registro de notificações remotas usando o SDK do iOS.

{% alert note %}
Este erro não significa que o usuário está com push desativado — apenas que um token específico foi removido do perfil dele. Para verificar se o usuário ainda possui tokens válidos, acesse **Pesquisa de Usuário** e revise a seção **Configurações de Contato** na guia **Engajamento**.
{% endalert %}

### InvalidProviderToken

O erro `InvalidProviderToken` significa que o APNs rejeitou a solicitação porque o token de autenticação (de uma chave `.p8`) ou o certificado de push (`.p12`) não corresponde ao bundle ID ou Team ID do app. Para resolver isso:

1. **Verifique seu Team ID e Key ID:** Se você está usando uma chave de autenticação `.p8`, confirme que o **Team ID** e o **Key ID** configurados no dashboard da Braze (**Configurações** > **Configurações do App** > selecione seu app iOS) correspondem aos valores na sua conta Apple Developer.
2. **Verifique o bundle ID:** Certifique-se de que o bundle ID registrado na Braze corresponde ao bundle ID do seu app. Uma incompatibilidade, como uma diferença de capitalização ou um sufixo `.debug`, causa este erro.
3. **Reenvie a chave ou certificado:** Se a chave `.p8` ou o certificado `.p12` foi recentemente regenerado ou revogado, faça upload da nova chave para a Braze e remova a antiga.
4. **Confirme o ambiente APNs:** Se você está usando um certificado `.p12`, verifique se selecionou o ambiente correto (desenvolvimento versus produção) ao fazer o upload. Para chaves `.p8`, isso é tratado automaticamente.

### Push com bounce: serviço de feedback APNS removido

Isso geralmente acontece quando alguém desinstala o app. A Braze consulta o serviço de feedback do APNS todas as noites para obter uma lista de tokens inválidos. Para saber mais, consulte a documentação da Apple sobre [Comunicação com APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}