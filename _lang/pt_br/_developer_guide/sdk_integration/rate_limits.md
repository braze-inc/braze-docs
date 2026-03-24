---
page_order: 2.0
nav_title: Limites de taxa
article_title: Limites de taxa do SDK da Braze
description: "Saiba mais sobre a limitação de taxa inteligente e do lado do cliente do SDK da Braze que otimiza a vida útil da bateria, reduz o uso de largura de banda e garante a entrega confiável de dados."
---

# Limites de taxa do SDK da Braze

> Saiba mais sobre a limitação de taxa inteligente e do lado do cliente do SDK da Braze que otimiza a vida útil da bateria, reduz o uso de largura de banda e garante a entrega confiável de dados.

## Entendendo os limites de taxa do SDK

A limitação de taxa do SDK da Braze utiliza os seguintes recursos para otimizar a performance, minimizar o consumo de bateria, reduzir o uso de dados e garantir a entrega confiável de dados:

### Processamento assíncrono

O SDK da Braze usa um algoritmo de token bucket para limitação de taxa. Essa abordagem permite picos de atividade enquanto mantém o controle de taxa a longo prazo. Em vez de processar solicitações em uma fila rígida, o token bucket opera de forma assíncrona:

- **Geração de tokens**: Os tokens são reabastecidos a uma taxa constante no bucket.
- **Tratamento de solicitações**: Qualquer chamada do SDK que chega quando um token está disponível prossegue imediatamente, independentemente de quando outras chamadas chegaram.
- **Sem ordenação rígida**: As solicitações não esperam na fila; várias chamadas podem competir pelo próximo token disponível.
- **Tratamento de picos**: Picos curtos de atividade são permitidos se houver tokens suficientes disponíveis no momento das solicitações.
- **Controle de taxa**: A taxa de transferência a longo prazo é limitada pela taxa constante de reabastecimento de tokens.

Esse fluxo assíncrono ajuda o SDK a responder rapidamente à capacidade de rede disponível enquanto mantém níveis de tráfego geral previsíveis.

### Limitação de taxa adaptativa

O SDK da Braze pode ajustar os limites de taxa em tempo real para proteger a infraestrutura da rede e manter uma performance ideal. Essa abordagem:

- **Previne sobrecarga**: Ajusta limites para evitar congestionamento na rede.
- **Otimiza a performance**: Mantém a operação suave do SDK sob condições variadas.
- **Responde às condições**: Adapta-se com base nos padrões atuais de rede e uso.

{% alert note %}
Como os limites se adaptam em tempo real, tamanhos exatos de buckets e valores estáticos não são fornecidos. Eles podem mudar dependendo das condições da rede e do uso.
{% endalert %}

### Otimizações de rede

O SDK da Braze inclui vários comportamentos integrados para melhorar a eficiência, reduzir o uso da bateria e lidar com condições de rede variadas:

- **Agrupamento automático**: Coloca eventos em fila e os envia em lotes eficientes.
- **Comportamento ciente da rede**: Ajusta as taxas de envio com base na qualidade da conectividade.
- **Otimização da bateria**: Minimiza ativações do rádio e chamadas de rede.
- **Degradação suave**: Mantém a funcionalidade durante condições de rede ruins.
- **Consciência de segundo plano/primeiro plano**: Otimiza o comportamento à medida que o ciclo de vida do app muda.

## Melhores práticas

Siga estas melhores práticas para ajudar a evitar problemas de limite de taxa:

| Faça isso | Não faça isso |
| --- | --- |
| Rastreie ações e marcos significativos do usuário | Rastreie cada interação menor ou evento de UI |
| Atualize o conteúdo apenas quando necessário | Atualize o conteúdo em cada ação do usuário (como eventos de rolagem) |
| Deixe o SDK lidar com o agrupamento automaticamente | Force a transmissão imediata de dados (a menos que absolutamente necessário) |
| Concentre-se em eventos que agregam valor à análise de dados | Chame métodos do SDK em rápida sucessão sem considerar a frequência |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Obtendo ajuda

Se você está enfrentando problemas de limite de taxa do SDK, revise os seguintes métodos de rede:

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Ao entrar em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support), inclua os seguintes detalhes para cada um dos métodos de rede do SDK que você usa:

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
