---
nav_title: alertas de uso da API
article_title: Alertas de uso da API
description: "Este artigo fornece uma visão geral dos alertas de uso da API, que permitem detectar proativamente tráfego inesperado."
page_order: 3.6
---

# alertas de uso da API

> Os alertas de uso da API fornecem visibilidade crítica sobre o uso da sua API, permitindo que você detecte proativamente tráfego inesperado. Ao configurar esses alertas para monitorar volumes de solicitações da API, você pode receber notificações em tempo real e resolver problemas antes que eles impactem suas campanhas de marketing.

## Sobre os alertas de uso da API

Você pode usar alertas de uso da API para monitorar volumes de solicitações para as seguintes categorias:

| Categoria da API | Informações |
|--------------|---------|
| Endpoints da API REST | Monitora o uso de todas as chamadas da API REST feitas para o backend da Braze, como enviar mensagens, criar campanhas ou exportar usuários. |
| Solicitações da API SDK | Monitora as solicitações da API feitas a partir dos SDKs da Braze em aplicativos clientes, como acionar mensagens no aplicativo ou sincronizar dados de usuários.<br><br>_\*Disponível apenas para clientes que adquiriram Usuários Ativos Mensais – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Criando um alerta de uso da API

Para criar um alerta de uso da API:

1. Acesse **Configurações** > **APIs e Identificadores** > **Alertas de Uso da API**, e então crie um novo alerta.
2. Digite um nome para o seu alerta e escolha os endpoints da API REST e as chaves da API para as quais você gostaria de ser alertado.
3. Defina os critérios do seu alerta escolhendo um ou mais códigos de resposta e especificando os [limites de alerta](#api-usage-alert-thresholds).
4. Quando terminar, ative **Alerta habilitado**.
    ![Um exemplo de um alerta de uso da API que envia notificações quando o endpoint de Rastrear usuários aumenta em 100 por cento dentro de uma hora.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Limites de alerta {#api-usage-alert-thresholds}

Quando você define seus critérios de alerta, pode ajustar os seguintes limites:

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Condição de limite</td>
      <td>
        Define as condições que levam ao volume de limite que você gostaria de ser alertado. Os seguintes são suportados:<br><br>
        <ul>
          <li><strong>Aumentado em</strong> ou <strong>Diminuído em</strong>: Compara solicitações em relação à janela de tempo anterior.</li>
          <li><strong>Aumentado em porcentagem</strong> ou <strong>Diminuído em porcentagem</strong>: Compara a mudança percentual nas solicitações em relação à janela de tempo anterior.</li>
          <li><strong>Maior ou igual a</strong>, ou <strong>menor ou igual a</strong>: Conta solicitações em uma janela de tempo.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volume de limite</td>
      <td>Usado em conjunto com a condição de limite.</td>
    </tr>
    <tr>
      <td>Entre</td>
      <td>A janela de tempo para avaliação de alerta.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configurando notificações de alerta

Você pode configurar um alerta de e-mail, um alerta de webhook ou ambos. Alertas de Webhook podem ser muito úteis para casos de uso, como enviar um alerta para plataformas externas, como um canal do Slack. Para um exemplo, veja nossa [documentação](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) sobre como integrar alertas com o Slack para nossas preferências de notificação.

![Um e-mail será enviado para o e-mail selecionado quando os critérios para o alerta forem atingidos.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Carga útil de exemplo {#payload}

O seguinte é uma carga útil de exemplo para o corpo de um alerta de uso da API via webhook.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Exemplos de alertas

Aqui estão algumas maneiras de configurar suas configurações de alerta de uso da API para ser notificado nas seguintes situações.

{% tabs local %}
{% tab api health %}
Você pode configurar alertas para monitorar a integridade geral da sua API. Por exemplo, você pode configurar esses alertas quando os erros da API aumentarem drasticamente, como 20% em relação à hora anterior.

| Endpoint | Chave de API | Código da resposta | Condição de limite | Volume de limite | Entre |
| --- | --- | --- | --- | --- | --- |
| Todos os endpoints | Todas as chaves de API | `4XX` e `5XX` | Aumentado em 10% | 10 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Fique alerta quando seu espaço de trabalho atingir seu limite de frequência para o endpoint `/users/track`. Você também pode aplicar essa configuração para outros endpoints do Braze.

| Endpoint | Chave de API | Código da resposta | Condição de limite | Volume de limite | Entre |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Todas as chaves de API | `429` | Maior ou igual a | 100 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
Essa configuração de alerta notifica você quando ocorrem erros em campanhas acionadas pela API e canvases, algumas das quais podem ser de alta prioridade.

| Endpoint | Chave de API | Código da resposta | Condição de limite | Volume de limite | Entre |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Todas as chaves de API | `4XX` e `5XX` | Maior ou igual a | 1 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Use a seguinte configuração de alerta para ser notificado quando uma integração com parceiros parar de enviar dados para o Braze.

| Endpoint | Chave de API | Código da resposta | Condição de limite | Volume de limite | Entre |
| --- | --- | --- | --- | --- | --- |
| Todos os endpoints | A chave de API usada para sua integração com parceiros | Todos os códigos de resposta | Menor ou igual a | 0 | 1 dia |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Considerações

- Cada alerta ativo enviará apenas um e-mail ou notificação de webhook uma vez a cada 8 horas. Isso é para evitar muitas notificações de um único alerta. Se seu alerta estiver notificando você prematuramente, considere editar os critérios do alerta para melhor corresponder ao seu caso de uso.
- Você pode ter até 10 alertas por espaço de trabalho.
