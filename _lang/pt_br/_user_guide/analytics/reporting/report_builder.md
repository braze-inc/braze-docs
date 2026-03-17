---
nav_title: Criador de relatórios
article_title: Criador de relatórios
alias: /report_builder/
page_type: reference
description: "Este artigo de referência descreve o recurso Criador de Relatórios."
tool:
    - Reports
page_order: 6.2
---

# Criador de relatórios

> Esta página aborda como usar o Criador de Relatórios para criar e visualizar relatórios granulares usando dados do Braze, e como adicionar relatórios aos painéis.

## Usando um modelo de relatório

1. Acessar **análise de dados** > **Criador de Relatórios (Novo)**.
2. Selecione a seta **Mais opções** ao lado do botão **Criar Novo Relatório**, e depois selecione **Usar um modelo de relatório**.<br><br>![Menu suspenso do botão "Criar Novo Relatório" com opções para criar um relatório personalizado ou usar um modelo.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Selecione um dos modelos de relatório da biblioteca de modelos do Braze.
    - Use o menu suspenso **Itens de linha** e **Tags** para encontrar relatórios relevantes para seus casos de uso.<br><br>![Janela "modelos de relatório do Braze" com lista de modelos do Braze para selecionar.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Siga o passo 3 e em diante em [Criando um relatório](#creating-a-report) para personalizar ainda mais o relatório para se adequar ao seu caso de uso.

## Criando um relatório

1. Acessar **análise de dados** > **Criador de Relatórios (Novo)**.
2. Selecione **Criar Novo Relatório**.
3. No menu suspenso **Linhas**, selecione sobre o que você gostaria de relatar:
    - Campanhas
    - Canvas
    - Campanhas e canvas
    - Canais
    - Tags

    Observe que sua seleção de **Linhas** impactará [as métricas que você pode visualizar](#metrics-availability). Por exemplo, você pode visualizar métricas multivariantes apenas se relatar sobre **Canvases**, ou **Campanhas** com um **Variant** detalhamento. Você não pode visualizar essas métricas ao relatar sobre **Campanhas e Canvases**, mesmo que essas campanhas e Canvases tenham testes multivariantes. 

![A seção "Linhas e colunas" com campos para selecionar as linhas e agrupamentos para seu relatório.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4\. (Opcional) Selecione **Adicionar detalhamento** para dividir seus dados em visualizações mais granulares:
    \- Canais
    \- Data
        \- Use isso para dividir seus dados em intervalos de tempo menores. Por exemplo, se você está interessado em como suas campanhas se saíram por dia, selecione a seguinte configuração:
            - **Linhas**: Campanhas
            - **Agrupamento:** Data
            - **Intervalo:** dias
    \- Variantes
    \- Campanhas e Canvases

{% alert tip %}
Experimente diferentes configurações de opções de detalhamento para explorar as [muitas maneiras de dividir seus dados](#metrics-availability).
{% endalert %}

{: start="5"}
5\. Na seção **Colunas**, selecione **Personalizar Métricas**.

![A seção "Personalizar Métricas" com opções para selecionar várias métricas.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6\. Navegue pelas métricas por categoria e selecione a caixa de seleção correspondente para adicionar uma métrica ao seu relatório.
    \- Reordene as métricas e colunas arrastando o ícone pontilhado para cima ou para baixo.
7\. Em **Conteúdo do relatório**, configure o intervalo de datas para o qual você gostaria de incluir dados em seu relatório.
8\. Então, dependendo de suas seleções na etapa 3, escolha adicionar campanhas, Canvases ou ambos manualmente ou automaticamente ao seu relatório.
    - **Adicionar manualmente:** Escolha cada campanha ou Canvas para incluir no relatório usando os filtros para datas e tags ou canais de **Último Enviado**, ou pesquisando o nome da campanha ou Canvas.<br><br>![A seção "Adicionar campanhas e canvases manualmente" com uma lista de campanhas para selecionar.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Adicionar automaticamente:** Defina regras para quais campanhas ou Canvases incluir no relatório. Você só precisa selecionar um campo nesta página.
        \- Note que, à medida que campanhas ou Canvases adicionais atendem às condições que você definiu nesta tela, elas serão automaticamente adicionadas às execuções futuras do seu relatório.<br><br>![A seção "Adicionar campanhas e canvases automaticamente" com campos para definir regras sobre quais campanhas e Canvases devem ser adicionadas ao relatório.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9\. Execute o relatório selecionando **Salvar & Executar**.

{% alert note %}
O relatório pode levar até alguns minutos para ser gerado, dependendo do intervalo de datas e do número de campanhas ou Canvases que você selecionou na etapa de configuração.
{% endalert %}

## Disponibilidade de métricas

Sua seleção para **Linhas** afeta as métricas que você pode selecionar.

{% alert tip %}
Se você quiser relatar sobre variantes ou etapas do Canvas, selecione **Canvases** para linhas e deixe o campo vazio ou selecione **Data** como a detalhamento. Isso cria um dropdown de **Visualização do Canvas** para visualizar métricas apenas para o Canvas, ou agrupar métricas por variante, etapa ou mensagem. 

![O dropdown "Visualização do Canvas" aberto.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Métrico | Descrição |
| --- | --- |
| Métricas de conversão | Disponível para Campanhas, Canvases, Campanhas e Canvases. |
| Entradas | Disponível para Campanhas, Canvases, Campanhas e Canvases, Tags. |
| Última Data Enviada | Disponível para Campanhas, Canvases, Campanhas e Canvases. Exibe apenas para campanhas agendadas—não é preenchido para campanhas baseadas em ação ou acionadas por API. |
| Envios | Disponível para cada canal relevante. |
| Mensagens enviadas | Disponível para Campanhas, Canvases, Campanhas e Canvases, Tags. |
| Linha de assunto | Disponível para campanhas de e-mail com detalhamento de **Variante**, Canvases e Canvases com detalhamento de **Variante**. |
| Total de receitas | Disponível para Campanhas, Canvases, Campanhas e Canvases, Tags. Indisponível com detalhamento de **Canais**. |
| Impressões únicas | Disponível para Campanhas, Canvases, Campanhas e Canvases, Tags. |
| Destinatários únicos | Disponível para Campanhas, Canvases, Campanhas e Canvases, Tags. Indisponível com detalhamento de **Canais**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Variantes de mensagens excluídas

Estatísticas para variantes de mensagens excluídas não são exibidas quando você detalha seu relatório por campanhas ou Canvases. No entanto, os totais a nível de canal incluem todas as estatísticas, independentemente de o variante ter sido excluído. Por exemplo, _Sends_ para e-mail incluem todos os envios de e-mail, mas se você detalhar essas estatísticas por campanha, os números podem ser menores porque os envios de variantes de mensagens excluídas são filtrados.

## Visualização de um relatório

Após executar seu relatório, você pode visualizar seus resultados em formato de tabela na página do relatório. 

![Uma tabela dos dados do relatório para as métricas de cada campanha.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Criando um gráfico de relatório

Na parte inferior da página, você pode criar um gráfico dos seus dados selecionando um **Tipo de gráfico** e configurando as métricas do gráfico. Por padrão, você verá a primeira métrica.

![Um gráfico dos dados do relatório com opções para configurar o eixo x do gráfico, o eixo y, o tipo de gráfico e mais.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Para criar um gráfico de linha, selecione **Data** como uma opção de detalhamento ao configurar o relatório. Isso exibirá tendências ao longo do tempo.
{% endalert %}

#### Baixando um gráfico de relatório

Para baixar uma imagem do gráfico do relatório, selecione o ícone pontilhado e escolha uma opção de download.

![Um menu com opções de download para diferentes formatos de arquivo.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Compartilhando um relatório

Você pode compartilhar um link do dashboard para o relatório selecionando **Compartilhar** e uma dessas opções:
- **Compartilhar um link:** Copie e compartilhe o link.

![Dropdown "Compartilhar um link" com um link para o relatório.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **Enviar ou agendar um e-mail:** Envie um e-mail imediatamente ou em um horário designado que contenha um link de download que expira após uma hora. Você pode selecionar destinatários entre os usuários da empresa listados no dropdown **Destinatários de E-mail** ou inserir qualquer outro endereço de e-mail.

!["Agendar um e-mail" janela com campos para escolher como o relatório é formatado, quem deve recebê-lo e quando deve ser enviado.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Baixar CSV:** Baixe um CSV do relatório.

## Adicionando um relatório a um dashboard

1. Selecione o ícone pontilhado no topo da tabela do relatório.
2. Selecione **Adicionar ao dashboard**.
3. Selecione se deseja criar um novo dashboard ou adicionar a um dashboard existente.<br><br>![Janela com opções para selecionar se deseja adicionar o relatório a um dashboard novo ou existente.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Siga os passos em [Construtor de Dashboard]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) para saber mais sobre como construir um dashboard.

