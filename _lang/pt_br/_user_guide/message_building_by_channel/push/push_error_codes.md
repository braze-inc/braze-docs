---
nav_title: Mensagens de erro comuns do push
article_title: Mensagens de erro comuns do Push
page_order: 22
page_type: reference
description: "Este artigo aborda mensagens de erro comuns relacionadas a push para iOS e Android e orienta você sobre possíveis soluções."
channel: push
platform:
- iOS
- Android
---

# Mensagens de erro comuns do push

> Esta página aborda mensagens de erro comuns para mensagens push.

{% tabs %}
{% tab Android %} 
### O empurrão saltou: MismatchSenderId
`MismatchSenderId` indica uma falha de autenticação. O Firebase Cloud Messaging (FCM) se autentica com alguns dados importantes: senderID e FCM API key.  Ambos devem ser validados quanto à precisão. Para obter mais informações, consulte a [documentação do Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) sobre esse problema.

As falhas comuns podem incluir:
- [ID do remetente]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) ruim
- Registro múltiplo se eles se registrarem em outro serviço push com um senderID diferente

### O empurrão saltou: Registro inválido
`InvalidRegistration` pode ocorrer quando um token de envio é malformado. As falhas comuns podem incluir quando:
- As pessoas estão passando os tokens de registro do Braze manualmente, mas não ligam para `getToken()`. Por exemplo, eles podem passar o ID completo da instância. O token na mensagem de erro é semelhante a `&#124;ID&#124;1&#124;:[regular token]`.  
- As pessoas estão se registrando em vários serviços. Atualmente, esperamos que as intenções de registro por push cheguem no estilo antigo, portanto, se as pessoas estiverem se registrando em vários lugares e capturarmos intenções de outros serviços, poderemos obter tokens de push malformados.

### O empurrão saltou: Não registrado
`NotRegistered` geralmente significa que o aplicativo foi excluído do dispositivo (como o nosso sinal para Desinstalar). Isso também pode ocorrer se vários registros estiverem ocorrendo e um segundo registro estiver invalidando o token push que o Braze recebe.

{% endtab %}
{% tab iOS %}

### O empurrão saltou: BadToken

O erro `BadToken` pode ocorrer por vários motivos:
- O token de envio não está sendo enviado corretamente para nós em `[[Appboy sharedInstance] registerPushToken:]`
	- Verifique o token no [Registro de atividades de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Em geral, ele deve se parecer com uma longa sequência de letras e números (como `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Se isso não acontecer, verifique o código envolvido no envio de erros de token push do Braze.<br><br>
- Ambiente de provisionamento incompatível:
	- Se você se registrar com um certificado de desenvolvimento e tentar enviar com um certificado de produção, poderá ver este erro.  
	- O Braze só oferece suporte a certificados universais para ambientes de produção. Testar o push em ambientes de desenvolvimento com um certificado universal não funcionará. 
	- Esse relatório envia saltos na produção, mas não no desenvolvimento.<br><br>
- Perfil de provisionamento incompatível:
	- Isso pode acontecer se o seu certificado não corresponder ao que foi usado para obter o token. Se houver suspeita disso, as próximas etapas incluem:
		- Garantir que o certificado push que está sendo usado para enviar push do painel do Braze e o perfil de provisionamento estejam configurados corretamente.
		- Recriar a certificação APNS e, em seguida, recriar o perfil de provisionamento depois que o certificado APNS for configurado no site `app_id`. Às vezes, isso pode resolver alguns problemas mais visíveis.

### O empurrão saltou: Removido o serviço de feedback do APNS

Isso geralmente acontece quando alguém desinstala. O Braze consulta o APNS Feedback Service todas as noites para obter uma lista de tokens inválidos. Para obter mais informações, consulte a seção [Comunicação com APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) da Apple.

{% endtab %}
{% endtabs %}
