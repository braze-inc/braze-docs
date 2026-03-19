---
nav_title: Preparando suas fontes de dados
article_title: Preparando suas fontes de dados
page_order: 2
page_type: reference
description: "Este artigo de referência cobre os ativos de dados de feedback críticos necessários para fechar o ciclo de decisão da IA e ativar seu agente para aprender e melhorar continuamente."
---

# Preparando suas fontes de dados

> Este artigo de referência cobre os ativos de dados de feedback críticos necessários para fechar o ciclo de decisão da IA e ativar seu agente para aprender e melhorar continuamente.

## Fechando o ciclo de decisão da IA

Embora todos os dados de cliente sejam importantes para o agente (veja [Conectar fontes de dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), os ativos de dados mais importantes são aqueles que informam ao agente o que aconteceu após as decisões de engajamento com o cliente serem enviadas.

Esses ativos criam o ciclo de feedback que permite ao agente aprender.

{% alert note %}
Se o agente estiver integrado nativamente com a plataforma de engajamento com clientes (como Braze, SFMC ou Klaviyo), pode não haver etapas de configuração adicionais necessárias para os dados de feedback, uma vez que esses podem ser enviados automaticamente com os dados de cliente.
{% endalert %}

## Ativos de dados de feedback críticos

Existem três ativos críticos para criar o ciclo de feedback:

1. Dados de conversões
2. Dados de engajamento
3. Dados de ativações

### Dados de conversões

O ativo de conversão descreve o que aconteceu com o cliente após a orquestração. Por exemplo, supondo que um agente esteja otimizando o Valor Presente Líquido (VPL) para clientes que recebem campanhas otimizadas, o ativo de conversão pode incluir uma atualização diária das mudanças no VPL.

| Requisito | Motivo |
|-------------|------|
| Cada registro contém um identificador único de cliente que é consistente com todos os ativos de dados | O Decisioning Studio precisa rastrear a jornada individual do cliente desde a recomendação, passando pela ativação, até a conversão. |
| Cada registro tem um timestamp associado | Entender o tempo entre a comunicação e a sequência de ações do cliente é extremamente importante para o treinamento do agente e o cálculo de métricas. |
| Se estiver usando uma métrica alvo não binária (como, convertido versus não convertido), o valor da métrica alvo é fornecido com cada evento de conversão | O Decisioning Studio usa o valor da métrica alvo para gerar experiências de treinamento para recompensar/penalizar adequadamente o agente com base nos resultados das ações recomendadas. |
| Se as conversões puderem ser atribuídas de forma única às comunicações (e.g., resgate de cupons), os campos necessários para corresponder conversões a ativações são fornecidos. | Se um evento de conversão puder ser vinculado a uma comunicação específica, isso permite uma atribuição limpa e precisa. A atribuição direta fornece o sinal mais claro para o agente, mas se não for possível (como muitas vezes acontece), a atribuição baseada em proximidade será utilizada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Dados de engajamento

O ativo de engajamento descreve as interações dos clientes, incluindo cliques, aberturas e outras impressões. Os dados de engajamento podem ser incluídos nos dados de conversão ou podem ser separados. Ele desempenha um papel semelhante aos dados de conversão—informando ao agente o que aconteceu após o engajamento do cliente.

| Requisito | Motivo |
|-------------|------|
| Cada registro contém um identificador único de cliente que é consistente com todos os ativos de dados | O Decisioning Studio precisa rastrear eventos de engajamento para cada cliente individual. |
| Cada registro tem um timestamp associado | Entender o tempo entre a comunicação e a sequência de ações do cliente é extremamente importante para o treinamento do agente e o cálculo de métricas. |
| Se cliques, aberturas ou outros dados de engajamento puderem ser atribuídos de forma única às comunicações, os campos necessários para combinar engajamento com ativações são fornecidos. | Assim como com os dados de conversão, se o engajamento puder ser vinculado a uma comunicação específica, isso permite uma atribuição limpa e precisa. A atribuição direta fornece o sinal mais claro para o agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Dados de ativações

O ativo de ativações informa ao agente quais comunicações foram enviadas. Isso é frequentemente necessário dependendo de como a orquestração é configurada. Se o agente orquestra por meio de uma integração direta com Braze, SFMC ou Klaviyo, então o agente pode ser capaz de puxar dados de ativação diretamente.

{% alert note %}
Os dados de engajamento e os dados de ativações são muito comumente encontrados no mesmo ativo de dados.
{% endalert %}

| Requisito | Motivo |
|-------------|------|
| Cada registro contém um identificador único de cliente que é consistente com todos os ativos de dados | O Decisioning Studio precisa rastrear a jornada individual do cliente desde a recomendação, passando pela ativação, até a conversão. |
| Cada registro tem um timestamp associado | Entender o tempo entre a comunicação e a sequência de ações do cliente é extremamente importante para o treinamento do agente e o cálculo de métricas. |
| Os campos necessários para combinar o conteúdo da comunicação com os eventos de ativação são fornecidos (como `event_id`) | Combinar corretamente as características da comunicação com os envios é necessário para a atribuição e treinamento do agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

