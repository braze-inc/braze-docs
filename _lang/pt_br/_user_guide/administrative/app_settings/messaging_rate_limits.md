---
nav_title: Limites de taxa de envio de mensagens do espaço de trabalho
article_title: Limites de taxa de envio de mensagens do espaço de trabalho
alias: /workspace_messaging_rate_limits/
page_type: reference
description: "Este artigo de referência descreve os limites de taxa de envio de mensagens do espaço de trabalho e como eles funcionam com suas mensagens."
page_order: 10
---

# Limites de taxa de envio de mensagens do espaço de trabalho

> Use os limites de taxa de envio de mensagens do espaço de trabalho para regular a taxa de entrega das mensagens enviadas pela sua plataforma, garantindo que seus usuários recebam as mensagens de que precisam.

{% alert important %}
Os limites de taxa de envio de mensagens do espaço de trabalho estão sendo disponibilizados gradualmente. Talvez você ainda não veja essas configurações no seu dashboard.
{% endalert %}

## Como funciona

Os limites de taxa de envio de mensagens do espaço de trabalho se aplicam ao total de mensagens enviadas no seu espaço de trabalho. Ao definir e otimizar um limite de taxa no nível do espaço de trabalho, você pode controlar melhor o tráfego de saída das suas mensagens da Braze, evitando possíveis picos de demanda que possam afetar a performance do servidor.
{% alert note %}
Lembre-se de que as mensagens enviadas usando endpoints de API de envio de mensagens como `/messages/send` e `/messages/schedule/create` também são contabilizadas e impactadas pelos limites de taxa de envio de mensagens do espaço de trabalho.
{% endalert %}
O total de mensagens enviadas por minuto não excede os limites de taxa configurados para o espaço de trabalho. Não há uma ordem específica de quais campanhas são despachadas nos primeiros minutos em comparação com os minutos posteriores.

Por exemplo, digamos que você tenha um limite de taxa de envio de mensagens do espaço de trabalho de 100.000 mensagens por minuto, e as seguintes mensagens estejam todas sendo processadas às 12h:

| Campanha   | Número de mensagens | Horário de envio |
|------------|--------------------|-----------|
| Campanha 1 | 100.000            | 12h       |
| Campanha 2 | 100.000            | 12h       |
| Campanha 3 | 100.000            | 12h       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

As mensagens são despachadas ao longo de um intervalo de 3 minutos.

As mensagens são processadas em paralelo. Quando processadas, as mensagens são programadas para respeitar o limite de taxa de envio de mensagens do espaço de trabalho por ordem de chegada. Isso significa que, no exemplo acima, as mensagens enviadas a cada minuto são uma combinação variada das Campanhas 1, 2 e 3 que totalizam 100.000.

![Exemplo de como as mensagens são despachadas para as três campanhas.]({% image_buster /assets/img/workspace_messaging_rate_limits2.png %})

Considere o próximo exemplo com um limite de taxa de envio de mensagens do espaço de trabalho de 100.000 mensagens por minuto, com as seguintes mensagens configuradas:

| Campanha   | Número de mensagens | Horário de envio |
|------------|--------------------|-----------|
| Campanha 1 | 1.000.000          | 9h        |
| Campanha 2 | 1.000.000          | 9h05      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

A seguir está o cronograma de despacho esperado e as mensagens enviadas por minuto:

- A Campanha 1 seria programada das 9h às 9h10, com 100.000 mensagens enviadas por minuto.
- A Campanha 2 seria programada para despacho 5 minutos após o horário de despacho original, das 9h10 às 9h20, com 100.000 mensagens enviadas por minuto.

![Exemplo de como as mensagens são despachadas por minuto para as duas campanhas.]({% image_buster /assets/img/workspace_messaging_rate_limits1.png %})

{% alert note %}
Depois de definir o limite de taxa de envio de mensagens do espaço de trabalho, você pode aumentá-lo. No entanto, todas as mensagens já processadas antes do aumento usam o limite definido anteriormente.
{% endalert %}

## Definindo o limite de taxa de envio de mensagens do espaço de trabalho

1. No dashboard da Braze, acesse **Configurações** > **Configurações do espaço de trabalho** > **Limites de taxa de envio de mensagens do espaço de trabalho**.
2. Selecione **+ Adicionar limite de taxa** e, em seguida, selecione um canal de envio de mensagens.
3. Em **Mensagens por minuto**, insira o limite de taxa.
4. Selecione **Salvar**.

## Informações importantes

O limite de taxa é aplicado ao despacho, ou seja, ao início da tentativa de envio da mensagem. Quando há flutuações no tempo necessário para concluir o envio, o número de envios concluídos pode exceder ligeiramente o limite de taxa em alguns minutos. Com o tempo, o número de envios por minuto se equilibra para não ultrapassar o limite de taxa.

Quando uma campanha ou Canvas tem seu próprio limite de taxa definido e um limite de taxa no nível do espaço de trabalho também se aplica, ambos são respeitados. Por exemplo, se uma campanha tem um limite de taxa de 500.000, mas, devido aos limites de taxa do espaço de trabalho, ela só pode enviar 100.000 mensagens por minuto neste momento, então o limite de taxa do espaço de trabalho entra em vigor.

A Braze tenta distribuir uniformemente os despachos de mensagens ao longo do minuto, mas não pode garantir isso. Por exemplo, se você tem uma campanha com um limite de taxa de 500.000 mensagens por minuto, tentaremos distribuir as 500.000 mensagens uniformemente ao longo do minuto (cerca de 8.400 mensagens por segundo), mas pode haver alguma variação na taxa por segundo.

Observe que você ainda pode definir limites de taxa individuais nas suas campanhas e Canvas. Eles são aplicados independentemente dos limites de taxa de envio de mensagens do espaço de trabalho.

### Mensagens não incluídas nos limites de taxa de envio de mensagens do espaço de trabalho

- Mensagens enviadas usando [campanhas de e-mail de transação]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) não são incluídas nos limites de taxa de envio de mensagens do espaço de trabalho. Isso significa que elas têm limite de taxa próprio e não são contabilizadas nos limites de taxa de envio de mensagens do espaço de trabalho definidos.
- Mensagens para [grupos de teste]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab#seed-groups) e [envios de teste]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages) não são incluídas nos limites de taxa de envio de mensagens do espaço de trabalho. Isso significa que elas não têm limite de taxa e não são contabilizadas nos limites de taxa de envio de mensagens do espaço de trabalho definidos.
- Respostas automáticas de SMS não são incluídas nos limites de taxa de envio de mensagens do espaço de trabalho. Isso significa que elas não têm limite de taxa e não são contabilizadas nos limites de taxa de envio de mensagens do espaço de trabalho definidos.