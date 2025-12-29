---
nav_title: Painel de uso da API
article_title: Painel de uso da API
alias: "/api_usage/"
page_order: 3.5
description: "Este artigo fornece uma visão geral do painel de uso da API."
---

# Painel de uso da API

> O painel de uso da API permite que você monitore o tráfego de entrada da API REST no Braze para entender as tendências de uso de nossas APIs REST e solucionar possíveis problemas.

## Sobre o painel de uso da API

Para visualizar o painel de uso da API, vá para **Configurações** > **APIs e identificadores** e selecione **Painel**.

O painel padrão é uma exibição de todas as solicitações de entrada da API REST para seu espaço de trabalho no último dia (24 horas). Dependendo do seu caso de uso, você pode ajustar os controles do painel para filtrar ou agrupar o tráfego e também configurar o intervalo de tempo do painel.

Painel de uso da API com 130 solicitações no total, com uma taxa de sucesso de 70% e uma taxa de falha de 30%.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Métricas disponíveis

O painel de uso da API inclui as seguintes estatísticas:

| Métrico         | Descrição |
|----------------|-------------|
| Total de solicitações | O número total de solicitações enviadas ao Braze para o seu espaço de trabalho atual, considerando os filtros e controles aplicados ao painel. |
| Taxa de sucesso   | A porcentagem do total de solicitações em que o Braze emitiu uma resposta de sucesso `2XX`. |
| Taxa de erro     | A porcentagem do total de solicitações em que o Braze emitiu uma resposta de erro `4XX` ou `5XX`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Usando o painel de controle

\![Filtros a serem aplicados ao painel, incluindo: Chave de API, ponto de extremidade, códigos de resposta, dados de grupo e data.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtros

Selecione **Filtros** para aplicar filtros e restringir a visualização do tráfego da API REST para seu espaço de trabalho, incluindo:

- Chave da API
- Ponto final
- Código de resposta

### Dados do grupo

Você pode agrupar dados em várias séries de dados para explorar diferentes padrões em seu uso, inclusive:

- Códigos de resposta (padrão)
- Ponto de extremidade da API
- Chave da API
- Somente sucesso e fracasso

### Data

Ajuste o filtro de data para mostrar um intervalo de tempo maior ou menor, conforme necessário. Isso inclui:

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
As opções **Last 3 Hours (Últimas 3 horas** ) e **Last 6 Hours (Últimas 6 horas** ) mostrarão o tráfego por minutos. Períodos de tempo maiores mostrarão o tráfego a cada cinco minutos, hora ou dia.
{% endalert %}

## Considerações

O painel de uso da API inclui todas as solicitações da API REST que o Braze recebeu e para as quais retornou uma resposta `2XX`, `4XX` ou `5XX`. Isso inclui saídas de transformação de dados e sincronizações de ingestão de dados na nuvem. As etapas de tráfego do SDK e de atualização do usuário não estão incluídas nesse painel.

Os dados mostrados no painel podem ter um pequeno atraso na exibição do tráfego recente. Durante períodos de alta utilização, você pode atualizar o painel até 4 vezes por minuto. Talvez seja necessário aguardar alguns minutos antes de atualizar o painel novamente.
