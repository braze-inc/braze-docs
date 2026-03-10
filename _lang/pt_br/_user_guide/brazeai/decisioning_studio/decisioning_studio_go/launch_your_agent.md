---
nav_title: Lance seu agente
article_title: Lance seu agente
page_order: 4
description: "Aprenda como lançar seu agente BrazeAI Decisioning Studio Go e configurar relatórios de Business as Usual (BAU) para comparação de performance."
---

# Lance seu agente

> Depois de conectar suas fontes de dados, configurar a orquestração e projetar seu agente, você está pronto para lançar. Este artigo aborda a ativação do seu agente e a configuração de relatórios BAU opcionais.

## Lançando seu agente

Após concluir todas as etapas de configuração no portal Decisioning Studio Go:

1. Revise a configuração do seu agente para garantir que todas as configurações estejam corretas.
2. Verifique se sua integração CEP está ativa e se a orquestração está pronta.
3. Selecione **Lançar** (ou ação equivalente) no portal Decisioning Studio Go para ativar seu agente.

Uma vez lançado, seu agente irá:
- Começar a receber dados do público do seu CEP
- Começar a fazer recomendações personalizadas para cada cliente
- A orquestração envia através do seu CEP configurado
- Coletar dados de engajamento para aprender e melhorar ao longo do tempo

## Configurando relatórios BAU

Por padrão, os relatórios do portal Decisioning Studio Go comparam o grupo do Decisioning Studio Go com o grupo de Controle Aleatório. Se você tiver uma campanha Business as Usual (BAU) existente que gostaria de comparar, pode configurar relatórios BAU para visualizar os três grupos em um só lugar.

### Benefícios dos relatórios BAU

O principal benefício de configurar relatórios BAU é a aplicação da filtragem de cliques inválidos do Decisioning Studio Go. Quando aplicada a todos os três grupos de experimento, isso permite a comparação de performance de cliques mais precisa e justa ("maçãs com maçãs") ao remover ruídos de:
- Cliques suspeitos de máquina
- Cliques no link de cancelamento de inscrição

### Requisitos para relatórios BAU

Antes de configurar os relatórios BAU, certifique-se de uma comparação justa entre o grupo de tratamento BAU, o grupo Decisioning Studio Go e o grupo de Controle Aleatório:

- **Sem sobreposição**: Nenhum destinatário pode pertencer a mais de um grupo durante toda a duração do experimento
- **Atribuição aleatória**: Os destinatários são atribuídos aleatoriamente aos grupos sem viés
- **Opções iguais**: Quaisquer opções disponíveis para o grupo BAU (criativo, frequência, tempo, incentivo ou oferta) estão disponíveis para os grupos Decisioning Studio Go e Controle Aleatório

{% alert warning %}
Sem um design de experimento "justo", os relatórios BAU podem ser confusos ou enganosos.
{% endalert %}

### Informações necessárias

Após validar o design do seu experimento, reúna os seguintes detalhes para configurar os relatórios BAU:

**IDs de campanha do seu CEP:**

| CEP | Tipos aceitos |
|-----|---------------|
| **Braze** | Campanhas e canvas |
| **Salesforce Marketing Cloud** | Apenas jornadas |
| **Klaviyo** | Apenas fluxos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

**ID do público do seu CEP:**

| CEP | Tipos aceitos |
|-----|---------------|
| **Braze** | Segmentos apenas |
| **Salesforce Marketing Cloud** | Extensões de Dados apenas |
| **Klaviyo** | Segmentos apenas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Se você não tiver um público existente que rastreie seu público BAU, deve criar um.

### Considerações

- **Clique apenas em KPIs**: Semelhante ao Decisioning Studio Go de forma mais geral, a reportagem BAU cobre apenas KPIs de cliques, não KPIs de conversão.
- **Limitações do Canvas**: Atualmente, não suportamos filtragem para IDs de etapas específicas do Canvas. Eventos de todas as etapas do Canvas serão incluídos nos dados BAU. Isso pode invalidar comparações contra BAU se apenas certas etapas do Canvas devem ser incluídas.

### Configurando relatórios BAU

Siga as instruções em seu portal do Decisioning Studio Go. Você deve ter:
- Um ou mais IDs de campanha onde todas as comunicações são comunicações BAU
- Um ID de público que rastreia os destinatários no público BAU a cada dia

## Monitorando seu agente

Após o lançamento, monitore o desempenho do seu agente no portal do Decisioning Studio Go:

- **Métricas de engajamento**: Rastreie as taxas de cliques entre grupos de experimentos
- **Progresso de aprendizado**: Observe como as recomendações do agente evoluem ao longo do tempo
- **Comparações de grupos**: Compare o desempenho do Decisioning Studio Go com o Controle Aleatório e o BAU (se configurado)

{% alert tip %}
Permita pelo menos 2-4 semanas de coleta de dados antes de tirar conclusões sobre o desempenho. O agente precisa de interações suficientes para aprender e otimizar efetivamente.
{% endalert %}

## Solução de problemas

Se o seu agente não estiver se saindo como esperado:

1. **Verifique a orquestração**: Confirme que sua integração CEP está ativa, campanhas e jornadas estão em execução, e que não há limites globais ou regras semelhantes interferindo na orquestração.
2. **Verifique o fluxo de dados**: Confirme que os dados do público e os dados de engajamento estão sendo capturados corretamente.
3. **Revise os grupos de experimento**: Garanta a atribuição aleatória adequada e que não haja sobreposição entre os grupos.
4. **Entre em contato com o suporte**: Entre em contato com o suporte da Braze para mais assistência.
