---
nav_title: Alertas de uso da API
article_title: Alertas de uso da API
description: "Este artigo fornece uma visão geral dos alertas de uso da API, que permitem detectar proativamente o tráfego inesperado."
page_order: 3.6
---

# Alertas de uso da API

> Os alertas de uso da API fornecem visibilidade crítica do uso da API, permitindo que você detecte proativamente o tráfego inesperado. Ao configurar esses alertas para rastrear os principais volumes de solicitações de API, você pode receber notificações em tempo real e resolver os problemas antes que eles afetem suas campanhas de marketing.

## Sobre os alertas de uso da API

Você pode usar os alertas de uso da API para monitorar os volumes de solicitação das seguintes categorias:

| Categoria API | Detalhes |
|--------------|---------|
| Pontos de extremidade da API REST | Rastreia o uso de todas as chamadas de API REST feitas para o back-end do Braze, como o envio de mensagens, a criação de campanhas ou a exportação de usuários. |
| Solicitações de API do SDK | Rastreia solicitações de API feitas a partir de SDKs do Braze em aplicativos clientes, como o acionamento de mensagens no aplicativo ou a sincronização de dados do usuário.<br><br>_\*Disponível apenas para clientes que adquiriram o Monthly Active Users - CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Criação de um alerta de uso da API

Para criar um alerta de uso da API:

1. Vá para **Configurações** > **APIs e identificadores** > **Alertas de uso de API** e crie um novo alerta.
2. Insira um nome para o alerta e escolha os pontos de extremidade da API REST e as chaves de API para os quais você gostaria de ser alertado.
3. Defina seus critérios de alerta escolhendo um ou mais códigos de resposta e especificando os [limites de alerta](#api-usage-alert-thresholds).
4. Quando terminar, ative a opção **Alerta**.
    \![Um exemplo de alerta de uso de API que envia notificações quando o ponto de extremidade Rastrear usuários aumenta em 100% em uma hora.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Limites de alerta {#api-usage-alert-thresholds}

Ao definir seus critérios de alerta, você pode ajustar os seguintes limites:

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
        Define as condições que levam ao volume limite sobre o qual você gostaria de ser alertado. Há suporte para os seguintes itens:<br><br>
        <ul>
          <li><strong>Aumentado por</strong> ou <strong>Diminuído por</strong>: Compara as solicitações com a janela de tempo anterior.</li>
          <li><strong>Aumentado em porcentagem</strong> ou <strong>Diminuído em porcentagem</strong>: Compara a variação percentual das solicitações com a janela de tempo anterior.</li>
          <li><strong>Maior que ou igual</strong>, ou <strong>menor que ou igual</strong>: Contabiliza as solicitações em uma janela de tempo.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volume limite</td>
      <td>Usado em conjunto com a condição de limite.</td>
    </tr>
    <tr>
      <td>Dentro de</td>
      <td>A janela de tempo para avaliação do alerta.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuração de notificações de alerta

Você pode configurar um alerta de e-mail, um alerta de webhook ou ambos. Os alertas de webhook podem ser muito úteis para casos de uso, como o envio de um alerta para plataformas externas, como um canal do Slack. Para obter um exemplo, consulte nossa [documentação](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) sobre a integração de alertas com o Slack para ver nossas preferências de notificação.

Um e-mail será enviado para o e-mail selecionado quando os critérios do alerta forem atingidos.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Amostra de carga útil {#payload}

A seguir, um exemplo de carga útil para o corpo de um webhook de alerta de uso de API.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": [
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition: "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    	],
    "timeframe_start": 2025-03-20T15:35:00Z,
    "timeframe_end": 2025-03-20T16:35:00Z,
    "volume": 1500,
    "previous_timeframe_start": 2025-03-20T14:35:00Z,
    "previous_timeframe_end": 2025-03-20T15:35:00Z,
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Exemplo de alertas

Aqui estão algumas maneiras de definir suas configurações de alerta de uso da API para serem notificadas nos seguintes cenários.

{% tabs local %}
{% tab api health %}
Você pode configurar alertas para monitorar a integridade geral da sua API. Por exemplo, você pode configurar esses alertas quando os erros de API aumentarem drasticamente, como 20% em relação à hora anterior.

| Ponto final | Chave da API | Código de resposta | Condição de limite | Volume limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| Todos os endpoints | Todas as chaves de API | `4XX` e `5XX` | Aumento de 10% | 10 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Receba um alerta quando seu espaço de trabalho atingir o limite de taxa para o endpoint `/users/track`. Você também pode aplicar essa configuração a outros endpoints do Braze.

| Ponto final | Chave da API | Código de resposta | Condição de limite | Volume limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Todas as chaves de API | `429` | Maior ou igual a | 100 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
Essa configuração de alerta o notifica quando ocorrem erros nas campanhas e Canvases acionados pela API, alguns dos quais podem ser de alta prioridade.

| Ponto final | Chave da API | Código de resposta | Condição de limite | Volume limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Todas as chaves de API | `4XX` e `5XX` | Maior que ou igual a | 1 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Use a seguinte configuração de alerta para ser alertado quando uma integração de parceiro parar de enviar dados para o Braze.

| Ponto final | Chave da API | Código de resposta | Condição de limite | Volume limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| Todos os endpoints | A chave de API usada para a integração de seu parceiro | Todos os códigos de resposta | Menor ou igual a | 0 | 1 dia |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Considerações

- Cada alerta ativo só enviará uma notificação por e-mail ou webhook uma vez a cada 8 horas. Isso serve para evitar o excesso de notificações de um único alerta. Se o seu alerta estiver notificando-o prematuramente, considere editar os critérios de alerta para que correspondam melhor ao seu caso de uso.
- Você pode ter até 10 alertas por espaço de trabalho.
