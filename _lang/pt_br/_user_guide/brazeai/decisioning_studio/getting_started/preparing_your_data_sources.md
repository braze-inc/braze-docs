---
nav_title: Preparação de suas fontes de dados
article_title: Preparação de suas fontes de dados
page_order: 2
page_type: reference
description: "Este artigo de referência aborda os ativos de dados de feedback críticos necessários para fechar o ciclo de decisão de IA e ativar seu agente para aprender e melhorar continuamente."
---

# Preparação de suas fontes de dados

> Este artigo de referência aborda os ativos de dados de feedback críticos necessários para fechar o ciclo de decisão de IA e ativar seu agente para aprender e melhorar continuamente.

## Fechando o ciclo de decisões de IA

Embora todos os dados de clientes sejam importantes para o agente (consulte [Conectar fontes de dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), os ativos de dados mais importantes são aqueles que informam ao agente o que aconteceu depois que as decisões de engajamento do cliente foram enviadas.

Esses ativos criam o ciclo de feedback que permite que o agente aprenda.

{% alert note %}
Se o agente estiver integrado de forma nativa à plataforma de engajamento com clientes (como Braze, SFMC ou Klaviyo), talvez não sejam necessárias etapas adicionais de configuração para os dados de feedback, pois eles podem ser enviados automaticamente com os dados do cliente.
{% endalert %}

## Ativos de dados de feedback críticos

Há três ativos críticos para a criação do ciclo de feedback:

1. Dados de conversões
2. Dados de engajamento
3. Dados de ativação

### Dados de conversões

O ativo de conversão descreve o que aconteceu com o cliente após a orquestração. Por exemplo, supondo que um agente esteja otimizando o Valor Presente Líquido (VPL) para clientes que recebem campanhas otimizadas, o ativo de conversão pode incluir uma atualização diária das alterações no VPL.

| Requisito | Motivo |
|-------------|------|
| Cada registro contém um identificador exclusivo de cliente que é consistente com todos os dados de ativos | O Decisioning Studio precisa rastrear a jornada individual do cliente, desde a recomendação, passando pela ativação, até a conversão. |
| Cada registro tem um registro de data e hora associado | Compreender o tempo entre a comunicação e a sequência de ações do cliente é extremamente importante para o treinamento de agentes e o cálculo de métricas. |
| Se estiver usando uma métrica de destino não binária (por exemplo, convertida versus não convertida), o valor da métrica de destino será fornecido com cada evento de conversão | O Decisioning Studio usa o valor da métrica de direcionamento para gerar experiências de treinamento para recompensar/penalizar adequadamente o agente com base nos resultados das ações recomendadas. |
| Se as conversões puderem ser atribuídas exclusivamente a comunicações (e.g., resgate de cupom), serão fornecidos os campos necessários para fazer a correspondência entre conversões e ativações | Se um evento de conversão puder ser vinculado a uma comunicação específica, isso permitirá uma atribuição limpa e precisa. A atribuição direta fornece o sinal mais claro para o agente, mas, se não for possível (como é frequentemente o caso), será usada a atribuição baseada em proximidade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Dados de engajamento

O ativo de engajamento descreve as interações com o cliente, incluindo cliques, aberturas e outras impressões. Os dados de engajamento podem ser incluídos nos dados de conversão ou podem ser separados. Eles desempenham um papel semelhante ao dos dados de conversões - informando ao agente o que aconteceu após o engajamento do cliente.

| Requisito | Motivo |
|-------------|------|
| Cada registro contém um identificador exclusivo de cliente que é consistente com todos os dados de ativos | O Decisioning Studio precisa rastrear os eventos de engajamento de cada cliente individual. |
| Cada registro tem um registro de data e hora associado | Compreender o tempo entre a comunicação e a sequência de ações do cliente é extremamente importante para o treinamento de agentes e o cálculo de métricas. |
| Se os dados de cliques, aberturas ou outros dados de engajamento puderem ser atribuídos exclusivamente às comunicações, serão fornecidos os campos necessários para associar o engajamento às ativações. | Assim como ocorre com os dados de conversão, se o engajamento puder ser vinculado a uma comunicação específica, isso permitirá uma atribuição limpa e precisa. A atribuição direta fornece o sinal mais claro para o agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Dados de ativação

O ativo de ativações informa ao agente quais comunicações foram enviadas. Isso geralmente é necessário, dependendo de como a orquestração está configurada. Se o agente orquestrar por meio de uma integração direta com Braze, SFMC ou Klaviyo, ele poderá extrair dados de ativação diretamente.

{% alert note %}
Os dados de engajamento e os dados de ativação são muito comumente encontrados no mesmo ativo de dados.
{% endalert %}

| Requisito | Motivo |
|-------------|------|
| Cada registro contém um identificador exclusivo de cliente que é consistente com todos os dados de ativos | O Decisioning Studio precisa rastrear a jornada individual do cliente, desde a recomendação, passando pela ativação, até a conversão. |
| Cada registro tem um registro de data e hora associado | Compreender o tempo entre a comunicação e a sequência de ações do cliente é extremamente importante para o treinamento de agentes e o cálculo de métricas. |
| São fornecidos os campos necessários para corresponder o conteúdo da comunicação aos eventos de ativação (como `event_id`) | A correspondência correta entre as características de comunicação e os envios é necessária para a atribuição e o treinamento do agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

