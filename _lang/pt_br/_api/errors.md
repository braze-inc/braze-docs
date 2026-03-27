---
nav_title: Erros e respostas
article_title: Erros e respostas da API
description: "Este artigo de referência aborda os vários erros e respostas do servidor que podem surgir ao usar a API da Braze e como solucioná-los."
page_type: reference
page_order: 2.3

---
# Erros e respostas da API

> Este artigo de referência aborda os vários erros e respostas do servidor que podem surgir ao usar a API da Braze e como solucioná-los.

## Respostas do servidor

Se sua carga útil POST foi aceita por nossos servidores, as mensagens bem-sucedidas são acompanhadas pela seguinte resposta:

```json
{
  "message" : "success"
}
```

Observe que sucesso significa apenas que a carga útil da API RESTful foi corretamente formada e passada para nossos serviços de notificação por push, e-mail ou outros serviços de envio de mensagens. Isso não significa que as mensagens foram realmente entregues, pois fatores adicionais podem impedir a entrega da mensagem (por exemplo, um dispositivo pode estar offline, o token por push pode ser rejeitado pelos servidores da Apple, ou você pode ter fornecido um ID de usuário desconhecido).

Para endpoints como [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), que não enviam mensagens, uma mensagem de sucesso significa apenas que a Braze recebeu a solicitação para processamento. Se não houver correspondência para o alias após o processamento, a solicitação é interrompida.

Se sua mensagem for bem-sucedida, mas tiver erros não fatais, você receberá a seguinte resposta:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

No caso de sucesso, quaisquer mensagens que não foram afetadas por um erro no array `errors` ainda são entregues. Se sua mensagem tiver um erro fatal, você receberá a seguinte resposta:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Respostas para IDs de envio rastreados

A análise de dados está sempre disponível para campanhas. Além disso, a análise de dados está disponível para uma instância específica de envio de campanha quando a campanha é enviada como broadcast. Quando o rastreamento estiver disponível para uma instância de envio de campanha específica, você receberá a seguinte resposta:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

O ID de envio fornecido pode ser usado como parâmetro para o endpoint `/send/data_series` para obter análises de dados específicas do envio.

## Erros

O elemento de código de status de uma resposta do servidor é um número de três dígitos em que o primeiro dígito do código define a classe da resposta.

- A **classe 2XX** do código de status (não fatal) indica que **sua solicitação** foi recebida, compreendida e aceita com êxito.
- A **classe 4XX** do código de status (fatal) indica um **erro do cliente**. Consulte a tabela de erros fatais para obter uma lista completa dos códigos de erro 4XX e suas descrições.
- A **classe 5XX** do código de status (fatal) indica um **erro do servidor**. Há várias causas possíveis, por exemplo, o servidor que você está tentando acessar não consegue executar a solicitação, o servidor está passando por manutenção, o que o impede de executar a solicitação, ou o servidor está com altos níveis de tráfego. Quando isso acontecer, recomendamos que você tente novamente sua solicitação com backoff exponencial. No caso de um incidente ou interrupção, a Braze não poderá reproduzir nenhuma chamada à API REST que tenha falhado durante o período do incidente. Você deve tentar novamente quaisquer chamadas que falharam durante o período do incidente.
  - Um **erro 502** é uma falha antes de chegar ao servidor de destino.
  - Um **erro 503** significa que a solicitação chegou ao servidor de destino, mas não foi possível completá-la porque não há capacidade suficiente, ou há um problema de rede, ou similar.
  - Um **erro 504** indica que um servidor não recebeu uma resposta de outro servidor upstream.

### Erros fatais

Os seguintes códigos de status e mensagens de erro associadas são retornados se sua solicitação encontrar um erro fatal.

{% alert warning %}
Todos os seguintes códigos de erro indicam que nenhuma mensagem foi enviada.
{% endalert %}

| Código de erro | Descrição |
|---|---|
| `5XX Internal Server Error` | Tente novamente sua solicitação com backoff exponencial.|
| `400 Bad Request` | Sintaxe incorreta.|
| `400 No Recipients` | Não há IDs externos ou IDs de segmento, nem tokens por push na solicitação.|
| `400 Invalid Campaign ID` | Nenhuma campanha de API de envio de mensagens foi encontrada para o ID de campanha fornecido.|
| `400 Message Variant Unspecified` | Você forneceu um ID de campanha, mas não um ID de variação de mensagem.|
| `400 Invalid Message Variant` | Você forneceu um ID de campanha válido, mas o ID de variação da mensagem não corresponde a nenhuma das mensagens dessa campanha.|
| `400 Mismatched Message Type` | Você forneceu uma variação de mensagem do tipo errado para pelo menos uma de suas mensagens.|
| `400 Invalid Extra Push Payload` | Você forneceu a chave `extra` para `apple_push` ou `android_push`, mas ela não é um dicionário.|
| `400 Max Input Length Exceeded` | Para `/users/track`, esse erro é causado ao exceder o número máximo de objetos permitidos em uma única solicitação. O limite depende do modelo de limite de taxa: para a maioria dos clientes, cada solicitação suporta até 75 objetos no total combinados entre `attributes`, `events` e `purchases`. Para clientes com limites de taxa legados, cada array suporta até 75 objetos independentemente. Para saber mais, consulte [POST: Criar e atualizar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).|
| `400 The max number of external_ids and aliases per request was exceeded` | Causado por chamadas com mais de 50 IDs externos.|
| `400 The max number of ids per request was exceeded` | Causado por chamadas com mais de 50 IDs externos.|
| `400 No message to send` | Nenhuma carga útil foi especificada para a mensagem.|
| `400 Slideup Message Length Exceeded` | A mensagem do slideup contém mais de 140 caracteres.|
| `400 Apple Push Length Exceeded` | A carga útil do JSON é superior a 1.912 bytes.|
| `400 Android Push Length Exceeded` | A carga útil do JSON tem mais de 4.000 bytes.|
| `400 Bad Request` | Não é possível analisar o datetime de `send_at`.|
| `400 Bad Request` | Na sua solicitação, `in_local_time` é verdadeiro, mas `time` já passou no fuso horário da sua empresa.|
| `401 Unauthorized` | Chave de API inválida. Causas comuns incluem:<br><br>- **Cabeçalho de autorização ausente ou malformado.** O valor do cabeçalho deve ser `Bearer` seguido de um espaço e sua chave de API: `Authorization: Bearer YOUR-API-KEY`. Erros comuns incluem omitir `Bearer`, omitir a chave após `Bearer` ou envolver o valor entre aspas.<br>- **Endpoint REST incorreto.** Você está enviando a solicitação para a [instância]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) incorreta. Por exemplo, se sua conta estiver em nossa instância da UE (`https://dashboard-01.braze.eu`), a solicitação deve ser enviada para `https://rest.fra-01.braze.eu`.<br>- **Permissões insuficientes.** Cada chave de API está vinculada a um espaço de trabalho específico e a um conjunto de permissões. Verifique as permissões da chave em **Configurações** > **Chaves de API** no dashboard.<br>- **Chave de API incorreta.** As chaves de API são específicas do espaço de trabalho. Uma chave de um espaço de trabalho não pode ser usada para autenticar solicitações de outro espaço de trabalho. |
| `403 Forbidden` | O plano tarifário não é compatível ou a conta foi desativada.|
| `403 Access Denied` | A chave da API REST que você está usando não tem permissões suficientes. Causas comuns incluem: {::nomarkdown}<ul><li><strong>A chave de API é anterior ao recurso.</strong> Se a chave de API foi criada antes do lançamento de um recurso (como grupos de inscrições ou catálogos), a chave não herda automaticamente essas permissões. Crie uma nova chave de API com as permissões necessárias em <strong>Configurações</strong> &gt; <strong>Chaves de API</strong>.</li><li><strong>Permissão específica do endpoint ausente.</strong> Cada endpoint de API requer um escopo de permissão específico (por exemplo, <code>users.track</code> ou <code>email.status</code>). Verifique se as permissões da chave correspondem ao endpoint que você está chamando.</li><li><strong>Barra final ou erro de digitação na URL.</strong> Por exemplo, <code>/users/track/</code> (com barra final) em vez de <code>/users/track</code> pode produzir erros inesperados.</li></ul>{:/}|
| `404 Not Found` | URL inválida. |
| `415 Unsupported Media Type` | O cabeçalho de solicitação `Content-Type` está ausente ou incorreto. Na página **Configurações**, adicione `Content-Type` com o valor `application/json`. |
| `429 Rate Limited` | Limite de taxa excedido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }