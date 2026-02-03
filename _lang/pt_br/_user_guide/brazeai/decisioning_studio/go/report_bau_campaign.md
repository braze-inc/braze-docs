---
nav_title: Relatório sobre a campanha BAU
article_title: Relatando sobre a campanha BAU
page_order: 10
description: "Este artigo fornece respostas para perguntas frequentes sobre relatórios de uma campanha Business as Usual (BAU) no portal BrazeAI Decisioning Studio Go."
---

# Relatando sobre a campanha Business as Usual

> Este artigo fornece respostas para perguntas frequentes sobre relatórios de uma campanha Business as Usual (BAU) no portal BrazeAI Decisioning Studio™ Go.

## Sobre relatórios da campanha BAU

Por padrão, o relatório do portal BrazeAI Decisioning Studio™ Go comparará o BrazeAI Decisioning Studio™ Go e grupos de controle aleatórios. Além de comparar esses dois grupos, você pode ter um grupo Business as Usual (também conhecido como BAU) que gostaria de comparar o desempenho do BrazeAI Decisioning Studio™ Go. Ao configurar relatórios BAU, você pode visualizar o desempenho de todos os três grupos em um único lugar no portal BrazeAI Decisioning Studio™ Go.

O principal benefício de configurar relatórios BAU é a aplicação da filtragem de cliques inválidos do BrazeAI Decisioning Studio™ Go, que, quando aplicada a todos os três grupos de experimento, permite a comparação de desempenho de cliques mais precisa e justa (ou "maçãs com maçãs") removendo qualquer ruído adicional de cliques suspeitos de máquina e cliques no link de cancelamento de inscrição.

## Solicitações

Antes de configurar relatórios BAU, primeiro certifique-se de que há uma comparação de maçã com maçã entre o grupo de tratamento BAU, o BrazeAI Decisioning Studio™ Go e o grupo de controle aleatório. Isso inclui verificar que:

- Nenhum destinatário pode pertencer a mais de um grupo (durante toda a duração do experimento).
- Os destinatários são atribuídos aleatoriamente aos grupos, sem viés nas atribuições de grupo.
- Quaisquer opções disponíveis para o grupo BAU (criativo, frequência, tempo, incentivo ou oferta) estão disponíveis para o BrazeAI Decisioning Studio™ Go e o grupo de controle aleatório.

Sem um design de experimento "maçã com maçã", os relatórios BAU podem ser confusos ou enganosos.

Depois de validar o design do seu experimento, os seguintes detalhes são necessários para configurar relatórios BAU:
- Um ou mais IDs de campanha da sua plataforma de ativação integrada (Braze, Salesforce Marketing Cloud ou Klaviyo) onde todas as comunicações na campanha são comunicações BAU.
    - Para Braze, campanhas e Canvases são aceitos.
    - Para Salesforce Marketing Cloud, apenas Journeys são aceitos.
    - Para Klaviyo, apenas Fluxos são aceitos
- Um ID de público da sua plataforma de ativação integrada que rastreia os destinatários que estão no público BAU a cada dia
    - Para Braze, apenas segmentos são aceitos
    - Para Salesforce Marketing Cloud, apenas extensões de dados são aceitas
    - Para Klaviyo, apenas segmentos são aceitos

Se você não tiver um público existente que rastreie seu público BAU, deve criar um.

{% alert note %}
**Para clientes da Braze apenas:** Certifique-se de que sua exportação atual da Braze para o BrazeAI Decisioning Studio™ Go inclua dados de suas campanhas BAU.
{% endalert %}

## Considerações

Semelhante ao BrazeAI Decisioning Studio™ Go de forma mais geral, a reportagem BAU cobre apenas KPIs de cliques, não KPIs de conversão.

Neste momento, não suportamos filtragem para IDs de etapas específicas do Canvas. Eventos de todas as etapas do Canvas serão incluídos nos dados BAU. Observe que isso pode invalidar comparações contra BAU se apenas certas etapas do Canvas devem ser incluídas.

## Configurando uma campanha BAU 

Siga as instruções no seu portal do BrazeAI Decisioning Studio™ Go. Você deve ter um ou mais [IDs de campanha e um ID de público](#what-are-the-requirements-to-use-in-portal-bau-reporting).