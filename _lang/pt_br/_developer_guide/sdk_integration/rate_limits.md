---
page_order: 2.0
nav_title: Limites de taxa
article_title: Limites de frequência do Braze SDK
description: "Saiba mais sobre o limite de frequência inteligente no lado do cliente do Braze SDK, que otimiza a vida útil da bateria, reduz o uso da largura de banda e garante o fornecimento confiável de dados."
---

# Limites de frequência do Braze SDK

> Saiba mais sobre o limite de frequência inteligente no lado do cliente do Braze SDK, que otimiza a vida útil da bateria, reduz o uso da largura de banda e garante o fornecimento confiável de dados.

## Compreensão dos limites de frequência do SDK

O limite de frequência do Braze SDK usa os seguintes recursos para otimizar a performance, minimizar o consumo de bateria, reduzir o uso de dados e garantir o fornecimento confiável de dados:

### Processamento assíncrono

O SDK do Braze usa um algoritmo de token bucket para limite de frequência. Essa abordagem permite explosões de atividade e, ao mesmo tempo, mantém o controle da taxa de longo prazo. Em vez de processar solicitações em uma fila rígida, o token bucket opera de forma assíncrona:

- **Geração de tokens**: As fichas são reabastecidas em um ritmo constante no balde.
- **Tratamento de solicitações**: Qualquer chamada do SDK que chegue quando um token estiver disponível prossegue imediatamente, independentemente de quando outras chamadas chegaram.
- **Não há pedidos rigorosos**: As solicitações não aguardam na fila; várias chamadas podem competir pelo próximo token disponível.
- **Manuseio de explosões**: Pequenas explosões de atividade são permitidas se houver tokens suficientes disponíveis no momento das solicitações.
- **Controle de taxa**: A taxa de transferência de longo prazo é limitada pela taxa de reposição constante de tokens.

Esse fluxo assíncrono ajuda o SDK a responder rapidamente à capacidade de rede disponível, mantendo níveis gerais de tráfego com previsão.

### Limite de frequência adaptável

O SDK do Braze pode ajustar os limites de frequência em tempo real para proteger a infraestrutura de rede e manter o desempenho ideal. Essa abordagem:

- **Evita a sobrecarga**: Ajusta os limites para evitar o congestionamento da rede.
- **Otimiza a performance**: Mantém a operação tranquila do SDK em condições variáveis.
- **Responde às condições**: Adapta-se com base na rede atual e nos padrões de uso.

{% alert note %}
Como os limites se adaptam em tempo real, não são fornecidos tamanhos exatos de baldes e valores estáticos. Elas podem mudar dependendo das condições e do uso da rede.
{% endalert %}

### Otimizações de rede

O SDK do Braze inclui vários comportamentos incorporados para melhorar a eficiência, reduzir o uso da bateria e lidar com condições de rede variáveis:

- **Dosagem automática**: Enfileira eventos e os envia em lotes eficientes.
- **Comportamento consciente da rede**: Ajusta as taxas de descarga com base na qualidade da conectividade.
- **Otimização da bateria**: Minimiza o despertar do rádio e as chamadas de rede.
- **Degradação graciosa**: Mantém a funcionalidade durante condições de rede ruins.
- **Consciência do plano de fundo/plano de fundo**: Otimiza o comportamento à medida que o ciclo de vida do app muda.

## Melhores práticas

Siga estas práticas recomendadas para ajudar a evitar problemas de limite de frequência:

| Faça isso | Não é isso |
| --- | --- |
| Rastreamento de ações e marcos significativos do usuário | Rastreamento de cada interação menor ou evento da interface do usuário |
| Atualizar o conteúdo somente quando necessário | Atualizar o conteúdo em cada ação do usuário (como eventos de rolagem) |
| Permita que o SDK lide com a formação de lotes automaticamente | Forçar a transmissão imediata de dados (a menos que seja absolutamente necessário) |
| Concentre-se em eventos que agreguem valor à análise de dados | Chamar métodos SDK em rápida sucessão sem considerar a frequência |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Obter ajuda

Se estiver tendo problemas com o limite de frequência do SDK, examine os seguintes métodos de rede:

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Ao entrar em contato com [support@braze.com](mailto:support@braze.com), inclua os seguintes detalhes para cada um dos métodos do SDK de rede que você usa:

```plaintext
Method name:

Frequency:
[Describe how often this is called, e.g., at every app launch, once per session]

Trigger/context:
[Describe what causes it to be called, e.g., button click, scroll event]

Code snippet:  
[Paste the exact code where this method is called, one snippet for each time it is called]

Patterns in user flow that may cause bursts or excessive calls:
[Describe here]
```
