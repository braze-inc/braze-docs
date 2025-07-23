---
nav_title: Mensagens Comuns de Erro de Push
article_title: Envio de mensagens de erro comuns do push
page_order: 22
page_type: reference
description: "Este artigo aborda as mensagens de erro comuns relacionadas ao push para iOS e Android e o orienta quanto às possíveis soluções."
channel: push
platform:
- iOS
- Android
---

# Mensagens comuns de erro de push

> Esta página aborda mensagens de erro comuns para envio de mensagens.

{% tabs %}
{% tab Android %} 
### Push devolvido: MismatchSenderId
`MismatchSenderId` indica uma falha de autenticação. Firebase Cloud Messaging (FCM) autentica com alguns dados principais: senderID e chave de API do FCM.  Estes devem ser validados quanto à precisão. Para saber mais veja a [documentação do Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) sobre este problema.

Falhas comuns podem incluir:
- Remetente [senderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) ruim
- Registro múltiplo se eles se registrarem com outro push service com um senderID diferente

### Push devolvido: InvalidRegistration
`InvalidRegistration` pode acontecer quando um token por push está malformado. Falhas comuns podem incluir quando:
- As pessoas estão passando tokens de registro Braze manualmente, mas não chamam `getToken()`. Por exemplo, eles podem passar a ID da instância inteira. O token na mensagem de erro parece `&#124;ID&#124;1&#124;:[regular token]`.  
- As pessoas estão se registrando em vários serviços. Atualmente, esperamos que as intenções de registro de push cheguem no estilo antigo, então, se as pessoas estiverem se registrando em vários lugares e capturarmos intenções de outros serviços, podemos obter tokens de push malformados.

### Push devolvido: NãoRegistrado
`NotRegistered` geralmente significa que o app foi excluído do dispositivo (como nosso sinal para Desinstalar). Isso também pode ocorrer se houver vários registros e um segundo registro estiver invalidando o token por push que a Braze recebe.

{% endtab %}
{% tab iOS %}

### Push devolvido: BadToken

O erro `BadToken` pode ocorrer por vários motivos:
- O token por push não está sendo enviado para nós corretamente em `[[Appboy sharedInstance] registerPushToken:]`
	- Verifique o token no [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Em geral, deve se parecer com uma longa string de letras e números (como `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Se isso não acontecer, verifique o código envolvido no envio de erros de token por push do Braze.<br><br>
- Ambiente de provisionamento incompatível:
	- Se você se registrar com um certificado de desenvolvimento e tentar enviar com um de produção, poderá ver este erro.  
	- Braze só suporta certificados universais para ambientes de produção. Testar push em ambientes de desenvolvimento com um certificado universal não funcionará. 
	- Este relatório envia saltos na produção, mas não no desenvolvimento.<br><br>
- Perfil de provisionamento incompatível:
	- Isso pode acontecer se o seu certificado não corresponder ao que foi usado para obter o token. Se isso for suspeito, os próximos passos incluem:
		- Garantir que o push certificado que está sendo usado para enviar push do dashboard da Braze e o perfil de provisionamento estejam configurados corretamente.
		- Recriando a certificação APNS e depois recriando o perfil de provisionamento após o certificado APNS ser configurado para o `app_id`. Isso pode às vezes resolver alguns problemas mais visíveis.

### Push devolvido: Serviço de feedback APNS removido

Isso geralmente acontece quando alguém desinstala. Braze consulta o Serviço de Feedback APNS todas as noites para obter uma lista de tokens inválidos. Para saber mais, consulte a [Comunicação com APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) da Apple.

{% endtab %}
{% endtabs %}
