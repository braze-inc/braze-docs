---
nav_title: Painel de uso da API
article_title: Painel de uso da API
permalink: "/api_usage/"
hidden: true
description: "Este artigo fornece uma visão geral do dashboard de uso da API."
---

# Painel de uso da API

> O dashboard de uso da API permite monitorar o tráfego de entrada da API REST na Braze para entender as tendências de uso de nossas APIs REST e solucionar possíveis problemas.

O dashboard padrão é uma visualização de todas as solicitações de entrada da API REST para seu espaço de trabalho no último dia (24 horas). Dependendo do seu caso de uso, é possível ajustar os controles do dashboard para filtrar ou agrupar o tráfego e também configurar o intervalo de tempo do dashboard.

![]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Estatísticas resumidas

- **Total de solicitações:** O número total de solicitações enviadas ao Braze para o seu espaço de trabalho atual, considerando os filtros e controles aplicados ao dashboard.
- **Taxa de sucesso:** A porcentagem do total de solicitações em que o Braze emitiu uma resposta de sucesso `2XX`.
- **Taxa de erro:** A porcentagem do total de solicitações em que o Braze emitiu uma resposta de erro `4XX` ou `5XX`.

## Controles do dashboard

![]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtros

Aplique filtros para restringir a visualização do tráfego da API REST em seu espaço de trabalho. Os filtros disponíveis incluem:

- Endpoint de API
- Chave de API
- Código da resposta

### Agrupar dados

Agrupe dados em várias séries de dados para explorar diferentes padrões em seu uso. As opções de agrupamento disponíveis são:

- Códigos de resposta (padrão)
- Endpoint de API
- Chave de API
- Somente sucesso e falha

### Data

Ajuste o filtro de data para mostrar um intervalo de tempo maior ou menor, conforme necessário. As opções de datas disponíveis incluem:

- Hoje (padrão)
- Personalizado
- Últimas 3 horas
- Últimas 6 horas
- Últimas 12 horas
- Últimas 24 horas
- Ontem
- Últimos 7 dias
- Últimos 14 dias
- Últimos 30 dias
- Último mês até a data

{% alert note %}
As opções **Last 3 Hours (Últimas 3 horas** ) e **Last 6 Hours (Últimas 6 horas** ) mostrarão o tráfego por minutos. Períodos de tempo maiores mostrarão o tráfego por horas ou dias.
{% endalert %}

## Considerações

O dashboard de uso da API inclui todas as solicitações da API REST que a Braze recebeu e para as quais retornou uma resposta `2XX`, `4XX` ou `5XX`. Isso inclui saídas de transformação de dados e sincronizações de ingestão de dados na nuvem. As etapas de tráfego do SDK e de atualização do usuário não estão incluídas nesse dashboard.

Os dados mostrados no dashboard podem ter uma postergação de até 15 minutos para mostrar o tráfego recente. Durante períodos de alta utilização, você pode atualizar o dashboard até 4 vezes por minuto. Talvez seja necessário aguardar alguns minutos antes de atualizar o dashboard novamente.
