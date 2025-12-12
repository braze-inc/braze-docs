---
nav_title: Erros e respostas
article_title: Erros e respostas da API
description: "Este artigo de referência aborda os vários erros e respostas do servidor que podem surgir ao usar a API do Braze e como solucioná-los." 
page_type: reference
page_order: 2.3

---
# Erros e respostas da API

> Este artigo de referência aborda os vários erros e respostas do servidor que podem surgir ao usar a API do Braze e como solucioná-los. 

{% raw %}

## Respostas do servidor

Se sua carga útil POST foi aceita por nossos servidores, as mensagens bem-sucedidas receberão a seguinte resposta:

```json
{
  "message" : "success"
}
```

Note que o sucesso significa apenas que a carga útil da API RESTful foi formada corretamente e passada para nossa notificação por push, e-mail ou outros serviços de envio de mensagens. Isso não significa que as mensagens foram realmente entregues, pois fatores adicionais podem impedir que a mensagem seja entregue (por exemplo, um dispositivo pode estar off-line, o token por push pode ser rejeitado pelos servidores da Apple, você pode ter fornecido um ID de usuário desconhecido).

Se sua mensagem for bem-sucedida, mas tiver erros não fatais, você receberá a seguinte resposta:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

Em caso de sucesso, todas as mensagens que não foram afetadas por um erro na matriz `errors` ainda serão entregues. Se sua mensagem tiver um erro fatal, você receberá a seguinte resposta:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Respostas para IDs de envio rastreadas

A análise de dados está sempre disponível para campanhas. Além disso, a análise de dados está disponível para uma instância específica de envio de campanha quando a campanha é enviada como uma transmissão. Quando o rastreamento estiver disponível para uma instância específica de envio de campanha, você receberá a seguinte resposta:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

O ID de envio fornecido pode ser usado como um parâmetro para o endpoint `/send/data_series` para extrair análises específicas de dados de envio.

## Erros

O elemento de código de status de uma resposta do servidor é um número de três dígitos em que o primeiro dígito do código define a classe da resposta.

- A **classe 2XX** do código de status (não fatal) indica que **sua solicitação** foi recebida, compreendida e aceita com êxito.
- A **classe 4XX** do código de status (fatal) indica um **erro do cliente**. Consulte a tabela de erros fatais para obter uma lista completa dos códigos de erro 4XX e suas descrições.
- A **classe 5XX** do código de status (fatal) indica um **erro do servidor**. Há várias causas possíveis, por exemplo, o servidor que você está tentando acessar não consegue executar a solicitação, o servidor está passando por manutenção, o que o impede de executar a solicitação, ou o servidor está com altos níveis de tráfego. Quando isso acontecer, recomendamos que você tente novamente sua solicitação com backoff exponencial. No caso de um incidente ou interrupção, a Braze não poderá reproduzir nenhuma chamada à API REST que tenha falhado durante a janela do incidente. Você precisará tentar novamente todas as chamadas que falharam durante a janela do incidente.
  - Um **erro 502** é uma falha antes de chegar ao servidor de destino.
  - Um **erro 503** significa que a solicitação chegou ao servidor de destino, mas não foi possível concluí-la porque não há capacidade suficiente, ou há um problema de rede, ou algo semelhante.
  - Um **erro 504** indica que um servidor não recebeu uma resposta de outro servidor upstream.

### Erros fatais

Os códigos de status a seguir e as mensagens de erro associadas serão retornados se sua solicitação encontrar um erro fatal.

{% endraw %}
{% alert warning %}
Todos os códigos de erro a seguir indicam que nenhuma mensagem será enviada.
{% endalert %}
{% raw %}

| Código de erro | Descrição |
|---|---|
| `5XX Internal Server Error` | Repetir sua solicitação com backoff exponencial.|
| `400 Bad Request` | Sintaxe ruim.|
| `400 No Recipients` | Não há IDs externas ou IDs de segmento, nem tokens por push na solicitação.|
| `400 Invalid Campaign ID` | Nenhuma campanha de mensagens API foi encontrada para o ID de campanha fornecido.|
| `400 Message Variant Unspecified` | Você fornece um ID de campanha, mas não um ID de variação de mensagem.|
| `400 Invalid Message Variant` | Você forneceu um ID de campanha válido, mas o ID de variação da mensagem não corresponde a nenhuma das mensagens dessa campanha.|
| `400 Mismatched Message Type` | Você forneceu uma variação de mensagem do tipo errado para pelo menos uma de suas mensagens.|
| `400 Invalid Extra Push Payload` | Você fornece a chave `extra` para `apple_push` ou `android_push`, mas ela não é um dicionário.|
| `400 Max Input Length Exceeded` | Causada pela chamada de mais de 75 IDs externas ao acessar o ponto de extremidade `/users/track`.|
| `400 The max number of external_ids and aliases per request was exceeded` | Causado por chamadas para mais de 50 IDs externas.|
| `400 The max number of ids per request was exceeded` | Causado por chamadas para mais de 50 IDs externas.|
| `400 No message to send` | Nenhuma carga útil é especificada para a mensagem.|
| `400 Slideup Message Length Exceeded` | A mensagem do slideup contém mais de 140 caracteres.|
| `400 Apple Push Length Exceeded` | A carga útil do JSON é superior a 1.912 bytes.|
| `400 Android Push Length Exceeded` | A carga útil do JSON tem mais de 4.000 bytes.|
| `400 Bad Request` | Não é possível analisar `send_at` datetime.|
| `400 Bad Request` | Em sua solicitação, `in_local_time` é verdadeiro, mas `time` já passou no fuso horário de sua empresa.|
| `401 Unauthorized` | Chave de API inválida. Esse erro também pode ocorrer se:<br><br> \- Você está enviando a solicitação para a [instância]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) incorreta. Por exemplo, se sua conta estiver em nossa instância da UE (`https://dashboard-01.braze.eu`), a solicitação deverá ser enviada para `https://rest.fra-01.braze.eu`.<br>\- A sintaxe da chave da API usa aspas simples ou duplas. A sintaxe correta é `Authorization: Bearer {YOUR-API-KEY}`. |
| `403 Forbidden` | O plano tarifário não é compatível ou a conta foi desativada de outra forma.|
| `403 Access Denied` | A chave da API REST que está usando não tem permissões suficientes; verifique as permissões da chave da API na página **Configurações**.|
| `404 Not Found` | URL inválido. |
| `429 Rate Limited` | Over rate limit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}
