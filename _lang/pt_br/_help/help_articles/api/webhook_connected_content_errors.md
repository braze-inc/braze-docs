---
nav_title: Solução de problemas de solicitações de webhook e Conteúdo conectado
article_title: Solução de problemas de solicitações de webhook e Conteúdo conectado
page_order: 3
channel:
  - webhooks
description: "Este artigo aborda como solucionar problemas de códigos de erro do webhook e do Conteúdo conectado, incluindo quais são os erros e as etapas para resolvê-los."
---

# Solução de problemas de solicitações de webhook e Conteúdo conectado

> Este artigo aborda como solucionar problemas de códigos de erro comuns para webhooks e Conteúdo conectado e fornece explicações adicionais sobre como esses erros podem ocorrer em suas solicitações.

## Erros 4XX

Os erros `4XX` indicam que há um problema com a solicitação enviada ao endpoint. Esses erros geralmente são causados por solicitações errôneas, incluindo parâmetros malformados, cabeçalhos de autenticação ausentes ou URLs incorretos. Observe que esses erros também se aplicam ao [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder).

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
      <th>O que significa</th>
      <th>Etapas para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>Há uma sintaxe inválida na solicitação.</td>
      <td>
        <ul>
          <li>Verifique se há erros de sintaxe na carga útil da solicitação.</li>
          <li>Confirme se todos os campos obrigatórios foram incluídos e formatados corretamente.</li>
          <li>Se estiver enviando uma carga útil JSON, valide a estrutura JSON.</li>
          <li>Se estiver usando Liquid para incluir tags de personalização na solicitação de webhook, verifique se o Liquid não resolve para um valor em branco ou produz caracteres que quebram o JSON (como aspas sem escape). Visualize a mensagem para um usuário teste para confirmar que a saída renderizada é válida.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>A solicitação requer autenticação do usuário.</td>
      <td>
        <ul>
          <li>Verifique se as credenciais de autenticação corretas (como chaves de API ou tokens) estão incluídas nos cabeçalhos da solicitação.</li>
          <li>Confirme que você tem as permissões de usuário para acessar o endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>O endpoint entende a solicitação, mas se recusa a autorizá-la.</td>
      <td>
        <ul>
          <li>Verifique se a chave de API ou o token tem as permissões necessárias.</li>
          <li>Confirme que você tem as permissões de usuário para acessar o endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>O endpoint não consegue encontrar o recurso solicitado.</td>
      <td>
        <ul>
          <li>Verifique se há erros de digitação ou caminhos incorretos no URL do endpoint.</li>
          <li>Confirme se o recurso que está tentando acessar existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>O método de solicitação é conhecido pelo endpoint, mas não é compatível com o recurso de destino.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme se o endpoint é compatível com o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>O endpoint atingiu o tempo limite de processamento da solicitação.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme se o endpoint é compatível com o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>A solicitação está incompleta devido a um conflito com o estado atual do recurso.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme se o endpoint é compatível com o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>Há um número excessivo de solicitações enviadas em um determinado período de tempo.</td>
      <td>
        <ul>
          <li>Reduza o limite de taxa na sua campanha ou etapa do canva.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Erros 5XX

Os erros `5XX` indicam que há um problema com o endpoint. Esses erros geralmente são causados por problemas no lado do servidor.

| Código de erro                    | O que significa                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | O endpoint encontrou uma condição inesperada que o impediu de concluir a solicitação.                                                       |
| **502 Bad Gateway**           | O endpoint recebeu uma resposta inválida do servidor upstream.                                                                                   |
| **503 Service Unavailable**   | O endpoint não está conseguindo processar a solicitação devido a uma sobrecarga temporária ou manutenção.                                                    |
| **504 Gateway Timeout**       | O endpoint não recebeu uma resposta oportuna do servidor upstream.                                                                               |
| **529 Host Overloaded**       | O host do endpoint está sobrecarregado e não pôde responder. |
| **598 Host Unhealthy**        | A Braze simulou a resposta porque o host do endpoint está temporariamente marcado como não íntegro. Consulte [Detecção de host não íntegro](#unhealthy-host-detection) para saber mais. |
| **599 Connection Error**      | A Braze apresentou um erro de tempo limite de conexão de rede ao tentar estabelecer uma conexão com o endpoint, o que significa que o endpoint pode estar instável ou fora do ar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Resolução de erros 5XX

Aqui estão algumas dicas para solucionar erros comuns `5XX`:

- Revise a mensagem de erro para obter detalhes específicos disponíveis no **Registro de atividades de mensagens**. Para webhooks, acesse a seção **Performance ao longo do tempo** na página inicial da Braze e selecione as estatísticas para webhooks. Lá, você pode encontrar o registro de data e hora que indica quando os erros ocorreram.
- Certifique-se de que não esteja enviando muitas solicitações que sobrecarreguem o endpoint. Você pode enviar em lotes ou ajustar o limite de taxa para verificar se isso reduz os erros.

## Detecção de host não íntegro

Os webhooks da Braze e o Conteúdo conectado empregam um mecanismo de detecção de host não íntegro para identificar quando o host de destino apresenta uma alta taxa de lentidão significativa ou sobrecarga, resultando em tempos limite, excesso de solicitações ou outros resultados que impedem a Braze de se comunicar com sucesso com o endpoint de destino. Ele atua como uma salvaguarda para reduzir a carga desnecessária que pode estar causando dificuldades ao host de destino. Também serve para estabilizar a infraestrutura da Braze e manter velocidades rápidas de envio de mensagens.

Os limites de detecção diferem entre webhooks e Conteúdo conectado:
- **Para webhooks**: Se o número de **falhas exceder 3.000 em qualquer janela de tempo móvel de um minuto** (por combinação exclusiva de nome de host e grupo de app&#8212;**não** por caminho de endpoint), a Braze interromperá temporariamente as solicitações ao host de destino por um minuto.
- **Para Conteúdo conectado**: Se o número de **falhas exceder 3.000 E a taxa de erro exceder 90% em qualquer janela de tempo móvel de um minuto** (por combinação exclusiva de nome de host e grupo de app&#8212;**não** por caminho de endpoint), a Braze interromperá temporariamente as solicitações ao host de destino por um minuto.

Quando as solicitações são interrompidas, a Braze simula respostas com um código de erro `598` para indicar a integridade ruim. Após um minuto, a Braze retomará as solicitações em velocidade máxima se o host for considerado íntegro. Se o host ainda não estiver íntegro, a Braze aguardará mais um minuto antes de tentar novamente.

Os códigos de erro a seguir contribuem para a contagem de falhas do detector de host não íntegro: `408`, `429`, `502`, `503`, `504`, `529`.

Para webhooks, a Braze repetirá automaticamente as solicitações HTTP que foram interrompidas pelo detector de host não íntegro. Essa nova tentativa automática usa backoff exponencial e tentará apenas algumas vezes antes de falhar. Para saber mais sobre erros de webhook, consulte [Erros, lógica de repetição e tempos limite]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#errors-retry-logic-and-timeouts).

Para o Conteúdo conectado, se as solicitações ao host de destino forem interrompidas pelo detector de host não íntegro, a Braze continuará a renderizar mensagens e a seguir sua lógica Liquid como se tivesse recebido um código de resposta de erro. Se você quiser garantir que essas solicitações de Conteúdo conectado sejam repetidas quando forem interrompidas pelo detector de host não íntegro, use a opção `:retry`. Para saber mais sobre a opção `:retry`, consulte [Novas tentativas de Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Se achar que a detecção de host não íntegro pode estar causando problemas, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact/).

## E-mails automatizados e entradas do registro de atividade de mensagens

### Configuração de e-mails automatizados

Se ocorrerem mais de 100.000 erros de webhook ou de endpoint de Conteúdo conectado (incluindo novas tentativas) em um espaço de trabalho em um período de 24 horas, você receberá um e-mail com as seguintes informações sobre como resolver os erros.

- Nome do espaço de trabalho
- Um link para o canva ou a campanha
- URL do endpoint
- Código de erro
- Hora em que o erro foi observado pela última vez
- Links para o registro de atividades de mensagens e documentação relacionada

{% alert note %}
Você pode configurar o limite de erro por espaço de trabalho. Para ajustar esse limite, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact/).
{% endalert %}

Os erros do endpoint são:

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

Esses e-mails são enviados apenas uma vez por dia no nível do espaço de trabalho. Se nenhum usuário se inscrever para receber esses e-mails, todos os administradores da empresa serão notificados.

Para se inscrever para receber esses e-mails, faça o seguinte:

1. Acesse **Configurações** > **Configurações administrativas** > **Preferências de notificação**.
2. Selecione **Erros de Conteúdo conectado** e **Erros de webhook** na seção **Canvas & Campaigns**.

### Entradas do registro de atividade de mensagens

Se ocorrer uma falha, haverá pelo menos uma entrada no [Registro de atividades de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) relacionada a ela. Se a solicitação for repetida e eventualmente bem-sucedida, esses detalhes estarão disponíveis no Currents e no Snowflake Data Share. Observe que, mesmo que uma solicitação eventualmente seja bem-sucedida após uma nova tentativa, os erros ainda podem disparar o e-mail automatizado.

### Insights adicionais sobre falhas no Braze Currents

Para aumentar a transparência dos problemas relacionados a webhooks, a Braze envia dados detalhados de eventos de falha de webhook para o Currents e o Snowflake Data Sharing. Esses eventos incluem solicitações de webhook com falha (como respostas HTTP `4xx` ou `5xx`), proporcionando mais observabilidade sobre como os problemas de webhook podem afetar a entrega de mensagens. Observe que os eventos de falha incluem erros terminais, bem como erros que estão sendo tentados novamente.

{% alert note %}
As solicitações de Conteúdo conectado não estão incluídas nesses eventos de falha do webhook.
{% endalert %}

Para saber mais, consulte o [glossário de eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).