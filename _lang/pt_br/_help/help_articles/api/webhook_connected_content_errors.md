---
nav_title: Solução de problemas de solicitações de Webhook e Connected Content
article_title: Solução de problemas de solicitações de Webhook e Connected Content
page_order: 3
channel:
  - webhooks
description: "Este artigo aborda como solucionar problemas de códigos de erro de webhook e Connected Content, incluindo o que são os erros e as etapas para resolvê-los."
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

`5XX` indicam que há um problema com o ponto de extremidade. Esses erros geralmente são causados por problemas no lado do servidor.

| Código de erro                    | O que isso significa                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Erro interno do servidor 500** | O endpoint encontrou uma condição inesperada que o impediu de concluir a solicitação.                                                       |
| **502 Gateway ruim**           | O ponto de extremidade recebeu uma resposta inválida do servidor upstream.                                                                                   |
| **503 Serviço indisponível**   | O endpoint não está conseguindo processar a solicitação devido a uma sobrecarga temporária ou manutenção.                                                    |
| **504 Tempo limite do gateway**       | O ponto de extremidade não recebeu uma resposta oportuna do servidor upstream.                                                                               |
| **599 Erro de conexão**      | O Braze apresentou um erro de tempo limite de conexão de rede ao tentar estabelecer uma conexão com o endpoint, o que significa que o endpoint pode estar instável ou inativo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Resolução de erros 5XX

Aqui estão algumas dicas para solucionar erros comuns do site `5XX`:

- Revise a mensagem de erro para obter detalhes específicos disponíveis no **registro de atividades de mensagens**. Para webhooks, acesse a seção **Performance ao longo do tempo** na página inicial do Braze e selecione as estatísticas para webhooks. Aqui, você pode encontrar o carimbo de data/hora que indica quando os erros ocorreram.
- Certifique-se de que não esteja enviando muitas solicitações que sobrecarreguem o endpoint. Você pode enviar em lotes ou ajustar o limite de frequência para verificar se isso reduz os erros.
