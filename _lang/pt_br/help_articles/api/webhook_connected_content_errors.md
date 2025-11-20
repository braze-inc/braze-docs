---
nav_title: Solução de problemas de solicitações de webhook e Connected Content
article_title: Solução de problemas de solicitações de Webhook e Connected Content
page_order: 3
channel:
  - webhooks
description: "Este artigo aborda como solucionar problemas de códigos de erro do webhook e do Connected Content, incluindo quais são os erros e as etapas para resolvê-los."
---

# Solução de problemas de solicitações de webhook e Connected Content

> Este artigo aborda como solucionar problemas de códigos de erro comuns para webhooks e Connected Content e fornece explicações adicionais sobre como esses erros podem ocorrer em suas solicitações.

## Erros 4XX

`4XX` indicam que há um problema com a solicitação enviada ao endpoint. Esses erros geralmente são causados por solicitações errôneas, incluindo parâmetros malformados, cabeçalhos de autenticação ausentes ou URLs incorretos.

Consulte a tabela a seguir para obter detalhes sobre o código de erro e as etapas de resolução:

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Código de erro</th>
      <th>O que isso significa</th>
      <th>Etapas para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Solicitação incorreta</b></td>
      <td>Há uma sintaxe inválida na solicitação.</td>
      <td>
        <ul>
          <li>Verifique se há erros de sintaxe na carga útil da solicitação.</li>
          <li>Confirme se todos os campos obrigatórios foram incluídos e formatados corretamente.</li>
          <li>Se estiver enviando uma carga útil JSON, valide a estrutura JSON.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Não autorizado</b></td>
      <td>A solicitação requer autenticação do usuário.</td>
      <td>
        <ul>
          <li>Verifique se as credenciais de autenticação corretas (como chaves ou tokens de API) estão incluídas nos cabeçalhos da solicitação.</li>
          <li>Confirme que você tem as permissões de usuário para acessar o endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Proibido</b></td>
      <td>O ponto de extremidade entende a solicitação, mas se recusa a autorizá-la.</td>
      <td>
        <ul>
          <li>Verifique se a chave ou o token da API tem as permissões necessárias.</li>
          <li>Confirme que você tem as permissões de usuário para acessar o endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Não encontrado</b></td>
      <td>O ponto de extremidade não consegue encontrar o recurso solicitado.</td>
      <td>
        <ul>
          <li>Verifique se há erros de digitação ou jornadas incorretas no URL do endpoint.</li>
          <li>Confirme se o recurso que está tentando acessar existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Método não permitido</b></td>
      <td>O método de solicitação é conhecido pelo ponto de extremidade, mas não é compatível com o recurso de direcionamento.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme se o ponto de extremidade é compatível com o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Tempo limite da solicitação</b></td>
      <td>O ponto de extremidade atingiu o tempo limite de processamento da solicitação.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme se o ponto de extremidade é compatível com o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflito</b></td>
      <td>A solicitação está incompleta devido a um conflito com o estado atual do recurso.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme se o ponto de extremidade é compatível com o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Solicitações em excesso</b></td>
      <td>Há um número excessivo de solicitações enviadas em um determinado período de tempo.</td>
      <td>
        <ul>
          <li>Reduza o limite de frequência em sua campanha ou etapa do Canva.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Erros 5XX

`5XX` indicam que há um problema com o endpoint. Esses erros geralmente são causados por problemas no lado do servidor.

| Código de erro                    | O que isso significa                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Erro interno do servidor 500** | O endpoint encontrou uma condição inesperada que o impediu de concluir a solicitação.                                                       |
| **502 Gateway ruim**           | O ponto de extremidade recebeu uma resposta inválida do servidor upstream.                                                                                   |
| **503 Serviço indisponível**   | O ponto de extremidade não está conseguindo processar a solicitação devido a uma sobrecarga temporária ou manutenção.                                                    |
| **504 Tempo limite do gateway**       | O ponto de extremidade não recebeu uma resposta oportuna do servidor upstream.                                                                               |
| **529 Host sobrecarregado**       | O host do endpoint está sobrecarregado e não pôde responder. |
| **598 Host não saudável**        | O Braze simulou a resposta porque o host do endpoint está temporariamente marcado como não saudável. Consulte [Detecção de host não saudável](#unhealthy-host-detection) para saber mais. |
| **599 Erro de conexão**      | O Braze apresentou um erro de tempo limite de conexão de rede ao tentar estabelecer uma conexão com o endpoint, o que significa que o endpoint pode estar instável ou inativo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Resolução de erros 5XX

Aqui estão algumas dicas para solucionar erros comuns do site `5XX`:

- Revise a mensagem de erro para obter detalhes específicos disponíveis no **registro de atividades de mensagens**. Para webhooks, acesse a seção **Performance ao longo do tempo** na página inicial do Braze e selecione as estatísticas para webhooks. Aqui, você pode encontrar o registro de data e hora que indica quando os erros ocorreram.
- Certifique-se de que não esteja enviando muitas solicitações que sobrecarreguem o endpoint. Você pode enviar em lotes ou ajustar o limite de frequência para verificar se isso reduz os erros.

## Detecção de host não saudável

Os webhooks do Braze e o Connected Content empregam um mecanismo de detecção de host insalubre para detectar quando o host de destino apresenta uma alta taxa de lentidão significativa ou sobrecarga, resultando em tempos limite, excesso de solicitações ou outros resultados que impedem que o Braze se comunique com sucesso com o endpoint de destino. Ele atua como uma salvaguarda para reduzir a carga desnecessária que pode estar causando dificuldades ao host de destino. Ele também serve para estabilizar a infraestrutura do Braze e manter velocidades rápidas de envio de mensagens.

Os limites de detecção diferem entre webhooks e Connected Content:
- **Para webhooks**: Se o número de **falhas exceder 3.000 em qualquer janela de tempo móvel de um minuto** (por combinação exclusiva de nome de host e **grupo** de aplicativos - não por caminho de endpoint), o Braze interromperá temporariamente as solicitações ao host de destino por um minuto.
- **Para conteúdo conectado**: Se o número de **falhas exceder 3.000 E a taxa de erro exceder 90% em qualquer janela de tempo móvel de um minuto** (por combinação exclusiva de nome de host e **grupo** de aplicativos - não por caminho de endpoint), o Braze interromperá temporariamente as solicitações ao host de destino por um minuto.

Quando as solicitações são interrompidas, o Braze simula respostas com um código de erro `598` para indicar a saúde debilitada. Após um minuto, o Braze retomará as solicitações em velocidade máxima se o host for considerado saudável. Se o host ainda não estiver saudável, o Braze aguardará mais um minuto antes de tentar novamente.

Os códigos de erro a seguir contribuem para a contagem de falhas do detector de host não íntegro: `408`, `429`, `502`, `503`, `504`, `529`.

Para webhooks, o Braze repetirá automaticamente as solicitações HTTP que foram interrompidas pelo detector de host não saudável. Essa nova tentativa automática usa backoff exponencial e tentará apenas algumas vezes antes de falhar. Para saber mais sobre erros de webhook, consulte [Erros, lógica de repetição e tempos limite]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#errors-retry-logic-and-timeouts).

Para o Connected Content, se as solicitações ao host de destino forem interrompidas pelo detector de host não saudável, o Braze continuará a renderizar mensagens e a seguir sua lógica Liquid como se tivesse recebido um código de resposta de erro. Se você quiser garantir que essas solicitações de Connected Content sejam repetidas quando forem interrompidas pelo detector de host não saudável, use a opção `:retry`. Para saber mais sobre a opção `:retry`, consulte [Tentativas de Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Se achar que a detecção de host não saudável pode estar causando problemas, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact/).

## E-mails automatizados e entradas de registro de atividades de mensagens

### Configuração de e-mails automatizados

Se ocorrerem mais de 100.000 erros de webhook ou de endpoint Connected Content (incluindo novas tentativas) em um espaço de trabalho em um período de 24 horas, você receberá um e-mail com as seguintes informações sobre como resolver os erros. 

- Nome do espaço de trabalho.
- Um link para o Canvas ou a campanha
- URLs dos endpoints
- Código de erro
- Hora em que o erro foi observado pela última vez
- Links para o registro de atividades de mensagens e documentação relacionada

{% alert note %}
Você pode configurar o limite de erro por espaço de trabalho. Para ajustar esse limite, entre em contato com [o Suporte Braze]({{site.baseurl}}/support_contact/).
{% endalert %}

Os erros do ponto de extremidade são:

- **
- **

Esses e-mails são enviados apenas uma vez por dia no nível do espaço de trabalho. Se nenhum usuário se inscrever para receber esses e-mails, todos os administradores da empresa serão notificados.

Para se inscrever para receber esses e-mails, faça o seguinte:

1. Acesse **Configurações** > **Configurações administrativas** > **Preferências de notificação**.
2. Selecione **Connected Content Errors** e **Webhook Errors** na seção **Canvas & Campaigns**.

### Entradas do registro de atividades de mensagens

Haverá pelo menos uma entrada no [Registro de atividades de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) relacionada ao erro que acionou o e-mail automático.

### Insights adicionais sobre falhas no Braze Currents

Para aumentar a transparência dos problemas relacionados a webhooks, o Braze transmite eventos detalhados de falhas de webhooks para o Currents e o Snowflake Data Sharing. Esses eventos incluem solicitações de webhook com falha (como respostas HTTP `4xx` ou `5xx` ), proporcionando mais observabilidade sobre como os problemas de webhook podem afetar a entrega de mensagens. Observe que os eventos de falha incluem erros de terminal, bem como erros que estão sendo tentados novamente.

{% alert note %}
As solicitações de Connected Content não estão incluídas nesses eventos de falha do webhook.
{% endalert %}

Para obter mais informações, consulte o [glossário de eventos de engajamento de mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).
