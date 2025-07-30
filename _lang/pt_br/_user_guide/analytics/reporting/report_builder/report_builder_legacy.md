---
nav_title: Criador de relatórios (antigo)
article_title: Criador de relatórios (antigo)
alias: /report_builder_legacy/
page_order: 0
page_type: reference
description: "Esta página aborda como executar um relatório usando o criador de relatórios herdado, incluindo campanhas e canvas, criando relatórios de comparação e criando relatórios e gráficos."
tool: 
  - Reports

---

# Criador de relatórios (antigo)

> O Construtor de Relatórios permite que você compare os resultados de várias campanhas ou canvas em uma única visualização, para que você possa determinar facilmente quais estratégias de engajamento mais impactaram suas métricas principais. Tanto para campanhas quanto para Canvas, você pode exportar seus dados e salvar seu relatório para visualização futura.<br><br>Para obter uma lista descritiva das métricas que você encontrará em seus relatórios, consulte o [Glossário de métricas de relatórios]({{site.baseurl}}/user_guide/data/report_metrics/).

![Exemplo de comparação de campanhas]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Use esse relatório para responder às principais perguntas de engajamento, por exemplo:

- Quais foram as campanhas ou Canvas com melhor performance para uma tag ou canal específico?
- Quais variantes de campanhas multivariantes tiveram o maior aumento em relação ao controle?  
- Qual campanha de promoção sazonal levou a uma taxa de compra mais alta: a liquidação de verão, a liquidação de outono ou a liquidação de inverno?
- Quais notificações por push nesse Canva tiveram as taxas de abertura mais altas?
- Quais etapas desse grupo de telas tiveram o maior número de conversões?
- A versão 1 de um e-mail de boas-vindas ou a versão 2 de um e-mail de boas-vindas levou a um maior engajamento e conversão? As mudanças funcionaram?
- Como os diferentes métodos de entrega (por exemplo, 3 pushes programados, 3 pushes baseados em ação e 3 pushes disparados por API) afetam suas taxas de abertura, taxas de conversão ou taxas de compra?
- Os aprimoramentos contínuos no envio de mensagens de usuários com atraso tiveram um impacto positivo nos seus KPIs ao longo do tempo?

{% alert tip %}
Tente usar os mesmos eventos de conversão para a conversão A, B e assim por diante em todas as campanhas e canvas que deseja comparar, para que possa alinhar essas conversões nos relatórios do Report Builder.
{% endalert %}

## Execução de um relatório

### Etapa 1: Criar um novo relatório

No dashboard, acesse **Análise de dados**  > **Criador de relatórios**.

Selecione **Criar novo relatório** e selecione um relatório de comparação de campanhas ou um relatório de comparação do Canva.

Se você optar por executar um relatório sobre campanhas, poderá selecionar entre um relatório **manual** ou **automatizado**. Os relatórios podem conter campanhas ou canvas, mas não os dois juntos. Todas as campanhas e Canvas que tenham enviado mensagens pela última vez nos últimos 12 meses serão elegíveis para um relatório.

![Painel de controle da campanha]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

Veja a seguir as diferenças entre essas duas opções:

| **Ação** | **Manual** | **Automatizado** |
| ---- | ---------- | ------------- |
| **Geração de relatórios** | Você poderá restringir sua lista de campanhas usando filtros e, em seguida, marcar campanhas específicas. | Você criará seu relatório usando as opções de filtro para restringir sua lista de campanhas. |
| **Salvando e visualizando relatórios** | Você pode salvar seu relatório. Na próxima vez que a visualizar, você poderá ver a mesma campanha que adicionou anteriormente, pois essas campanhas ainda se enquadram no filtro "Last Sent" (último envio). | Você pode salvar seu relatório. Na próxima vez que você o visualizar, o relatório será atualizado automaticamente para incluir todas as campanhas que correspondem atualmente aos seus filtros. |
| **Edição de relatórios** | Você pode selecionar **Editar relatório** para adicionar ou excluir campanhas do seu relatório | Você pode editar seu relatório ajustando os critérios de filtragem. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Tanto os relatórios **manuais** quanto os **automatizados** podem incluir um máximo de 250 campanhas em um relatório.
{% endalert %}

Os relatórios do Canva funcionam de forma semelhante a um relatório de campanha manual, pois as seleções do Canvas e as atualizações de relatórios também devem ser feitas manualmente. Você pode incluir no máximo cinco Canvas em um relatório.

### Etapa 2: Escolha suas métricas

Depois de criar o relatório, você encontrará uma tabela em branco com campanhas em cada linha. A tabela será preenchida depois que você selecionar **Edit Columns (Editar colunas** ) e escolher as métricas que deseja adicionar.

![Opções de campanha]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Sua tabela será preenchida com as métricas que você escolher. Para obter as definições dessas métricas, consulte o [Glossário de métricas do relatório]({{site.baseurl}}/user_guide/data/report_metrics/). Algumas métricas estão disponíveis apenas para relatórios de comparação de campanhas.

Você também pode alternar os cálculos da **média** de qualquer taxa ou métrica numérica e do **total** de qualquer métrica numérica.

### Etapa 3: Escolha um período de tempo

Você pode selecionar um período de tempo específico para visualizar os dados do seu relatório. Se uma determinada campanha, tela, variante de tela ou componente de tela não tiver dados para o período de tempo selecionado, os resultados dessa linha ficarão em branco. 

![Métrica numérica da campanha]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Etapa 4: Dê um nome e salve seu relatório

Dê um nome ao seu relatório antes de salvá-lo. Se um relatório for salvo sem ser nomeado, o Braze aplicará um nome padrão de "Relatório de comparação de campanhas".

![Nota da campanha]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Quando estiver pronto, selecione **Salvar**. Os relatórios salvos podem ser visualizados posteriormente na página **do Report Builder**.

## Relatório de comparação de campanhas com campanhas multivariantes

Para quaisquer campanhas multivariantes, é possível visualizar essas métricas divididas por suas variantes e grupo de controle clicando na seta ao lado do nome da campanha. As linhas que contêm suas variantes incluirão resultados de performance para essa variante, e a linha que contém seu controle incluirá apenas os resultados dos seus eventos de conversão. 

![Nota da campanha]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

As métricas que preenchem a linha da sua campanha geral refletirão o desempenho de suas variantes, mas não incluirão o desempenho do controle. Por exemplo, o Evento de Conversão Primária A da sua campanha geral será a soma do Evento de Conversão Primária A das suas variantes, e isso não incluirá o Evento de Conversão Primária A do seu controle.

{% alert important %}
Se você excluir uma variante de uma campanha multivariante, os dados dessa variante não estarão disponíveis para uso em um relatório futuro.
{% endalert %}

## Detalhamento do relatório de comparação de telas

Em um relatório do Canvas, você pode visualizar seus Canvas divididos por variante, etapas ou mensagem.

### Variante

A seleção do **detalhamento por variante** permite visualizar as estatísticas de alto nível de suas Canvas gerais, bem como as estatísticas de cada variante, que podem ser expandidas selecionando a seta ao lado do nome da Canvas.

![Variantes]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Etapas 

A seleção do **detalhamento por etapas** permite visualizar as métricas em nível de etapa, com cada linha do relatório contendo a linha de uma etapa.

![Etapas]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Mensagem

Semelhante a um detalhamento em nível de etapa, a seleção do **detalhamento por mensagem** mostra o nome das etapas em cada linha. No entanto, nas **colunas de edição**, você terá acesso a métricas no nível da mensagem, como estatísticas específicas do canal, como cliques em e-mails e aberturas de push.

![Relatório]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Note que, no dashboard da Braze, é possível ver as primeiras 50 linhas do seu relatório do canva. Você pode acessar o relatório completo ao exportar um CSV.

## Acesso a relatórios salvos

Ao acessar um **Relatório manual** salvo, você pode visualizar as mesmas campanhas adicionadas anteriormente, já que essas campanhas ainda se enquadram no filtro "Last Sent" (Último envio).

Ao acessar um **Relatório automático** salvo, o relatório será atualizado automaticamente para incluir todas as campanhas que correspondem aos seus filtros no momento. Por exemplo, se o seu relatório filtrou campanhas com a tag "Promoção", cada vez que você visualizar esse relatório, poderá ver todas as campanhas com a tag "Promoção", mesmo que essas campanhas tenham sido criadas depois que você fez esse relatório.

## Edição de relatórios

Em um **relatório manual**, você pode editar um relatório selecionando **Editar**. A partir daí, você pode selecionar ou desmarcar campanhas para incluir em seu relatório.

Em um **relatório automático**, basta alternar seus filtros para restringir os resultados em seu relatório.

## Exportação de relatórios

Você também pode selecionar **Exportar** para baixar o relatório em CSV.

Se o relatório contiver campanhas multivariantes, sua exportação incluirá dois arquivos CSV: 

- Um arquivo contendo apenas as métricas de nível superior para cada campanha
- Um arquivo que contém métricas em nível de variante

O nome do arquivo que contém métricas de variantes começará com `variant_`. Na primeira vez que exportar um relatório automatizado, você receberá uma janela pop-up solicitando permissão para baixar vários arquivos - clique em **Permitir**.

![Baixar a campanha]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exportação de relatórios de comparação de telas

Sua exportação de CSV refletirá a visualização de detalhamento em que você estava quando selecionou **Exportar**. Por exemplo, se você estiver na exibição de detalhamento em nível de etapa, sua exportação conterá dados sobre as métricas da etapa. Para exportar dados de um detalhamento diferente, você precisará navegar primeiro para esse detalhamento e selecionar **Exportar** a partir daí.

Se baixar um relatório do Canva de detalhamento de variantes, você receberá dois arquivos CSV:

- Um arquivo contendo apenas métricas de nível superior para cada Canva
- Um arquivo que contém métricas em nível de variante

## Gráficos de construção 

Use gráficos para visualizar uma métrica selecionada em seu relatório. Os gráficos estão disponíveis para relatórios que apresentam campanhas e têm pelo menos uma métrica adicionada às suas colunas.

![Gráfico de performance da campanha com a métrica Mensagem enviada selecionada]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Por padrão, o gráfico em cada relatório exibirá a métrica na primeira coluna do relatório. Para selecionar uma métrica diferente para o gráfico, escolha sua métrica no menu suspenso. Qualquer métrica em sua tabela de relatório estará disponível para exibição em seu gráfico.

Você pode representar graficamente no máximo três métricas. As unidades de todas as métricas devem ser as mesmas - por exemplo, se você escolher uma taxa no primeiro menu suspenso, somente as taxas estarão disponíveis para seleção no segundo menu suspenso.

Se o seu gráfico contiver apenas uma métrica, ele exibirá até 30 campanhas em ordem decrescente com base na métrica que você selecionou. Por exemplo, se a métrica do seu gráfico for cliques em e-mails, ele exibirá as 30 campanhas de e-mail com mais cliques, ordenadas do maior para o menor número de cliques. Se seu relatório contiver mais de 30 campanhas, somente as 30 primeiras serão exibidas no gráfico. Se você selecionar mais de uma métrica, seu gráfico exibirá apenas as cinco principais campanhas com base na primeira métrica selecionada.

No momento, os gráficos não são salvos quando você salva o relatório.



