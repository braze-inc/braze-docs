---
nav_title: Criador de relatórios
article_title: Criador de relatórios
alias: /report_builder/
page_type: reference
description: "Este artigo de referência descreve o recurso Report Builder."
tool:
    - Reports
page_order: 6.2
---

# Criador de relatórios

> Esta página aborda como usar o Report Builder para criar e visualizar relatórios granulares usando dados do Braze e como adicionar relatórios aos dashboards.

## Uso de um modelo de relatório

1. Acesse **Análise de dados** > **Criador de relatórios (novo)**.
2. Selecione a seta **Mais opções** ao lado do botão **Criar novo relatório** e, em seguida, selecione **Usar um modelo de relatório**.<br><br><br><br>
3. Selecione um dos modelos de relatório da biblioteca de modelos do Braze.
    - Use os **itens de linha** e o menu suspenso **Tags** para encontrar relatórios relevantes para seus casos de uso.<br><br><br><br>
4. Siga a etapa 3 e seguintes em [Criar um relatório](#creating-a-report) para personalizar ainda mais o relatório de acordo com seu caso de uso.

## Criação de um relatório

1. Acesse **Análise de dados** > **Criador de relatórios (novo)**.
2. Selecione **Criar novo relatório**.
3. No menu suspenso **Linhas**, selecione uma das seguintes opções para criar um relatório:
    - Campanhas
    - Canvas
    - Campanhas e canvas
    - Canais
    - Tags



{: start="4"}
4\. (Opcional) Selecione **Adicionar detalhamento** para dividir seus dados em exibições mais granulares:
    \- Canais
    \- Data
        \- Use isso para dividir seus dados em intervalos de tempo menores. Por exemplo, se estiver interessado em saber como foi a performance de suas campanhas por dia, selecione a seguinte configuração:
            - **Fileiras**: Campanhas
            - **Agrupamento:** Data
            - **Intervalo:** dias
    \- Variantes
    \- Campanhas e telas

{% alert tip %}

{% endalert %}

{: start="5"}
5\. Na seção **Colunas**, selecione **Personalizar métricas**.



{: start="6"}
6\. Procure métricas por categoria e marque a caixa de seleção correspondente para adicionar uma métrica ao seu relatório.
    \- Reorganize as métricas e colunas arrastando o ícone pontilhado para cima ou para baixo.
7\. Em **Conteúdo do relatório**, configure o intervalo de datas para o qual você gostaria de incluir dados em seu relatório.
8\. Em seguida, dependendo de suas seleções na etapa 3, escolha adicionar manual ou automaticamente campanhas, Canvas ou ambos ao seu relatório.
    - **Adicionar manualmente:** Escolha cada campanha ou Canvas a ser incluído no relatório usando os filtros para datas e tags ou canais de **Último envio** ou pesquisando o nome da campanha ou do Canvas.<br><br><br><br>
    - **Adicionar automaticamente:** Defina regras para quais campanhas ou telas devem ser incluídas no relatório. Você só precisa selecionar um campo nesta página.
        \- Note que, à medida que campanhas ou Canvas adicionais satisfizerem as condições definidas nessa tela, elas serão automaticamente adicionadas a futuras execuções do relatório.<br><br><br><br>
9\. Execute o relatório selecionando **Save & Run**.

{% alert note %}
O relatório pode levar alguns minutos para ser executado, dependendo do intervalo de datas e do número de campanhas ou Canvas que você selecionou na fase de configuração.
{% endalert %}

## 



|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |   |
|  |  |
|  |   |


## Visualização de um relatório

Depois de executar o relatório, você pode visualizar os resultados em formato de tabela na página do relatório. 



### Criação de um gráfico de relatório

Na parte inferior da página, você pode criar um gráfico de seus dados selecionando um **tipo de gráfico** e configurando as métricas do gráfico. Por padrão, você verá a primeira métrica.



{% alert note %}
Para criar um gráfico de linhas, selecione **Date (Data** ) como uma opção de pesquisa ao configurar o relatório. Isso exibirá as tendências ao longo do tempo.
{% endalert %}

#### Baixando um gráfico de relatório

Para baixar uma imagem do gráfico do relatório, selecione o ícone pontilhado e escolha uma opção de download.



## Adição de um relatório a um dashboard

1. Selecione o ícone pontilhado na parte superior da tabela de relatórios.
2. Selecione **Adicionar ao dashboard**.
3. Selecione se deseja criar um novo dashboard ou adicionar a um dashboard existente.<br><br><br><br>
4. Siga as etapas do [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) para saber mais sobre a criação de um dashboard.

