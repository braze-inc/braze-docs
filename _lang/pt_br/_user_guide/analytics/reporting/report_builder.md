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

> Esta página aborda como usar o Report Builder para criar e visualizar relatórios granulares usando dados do Braze e como adicionar relatórios a painéis.

## Uso de um modelo de relatório

1. Vá para **Analytics** > **Report Builder (New)**.
2. Selecione a seta **Mais opções** ao lado do botão **Criar novo relatório** e, em seguida, selecione **Usar um modelo de relatório**.<br><br>Botão suspenso "Criar novo relatório" com opções para criar um relatório personalizado ou usar um modelo.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Selecione um dos modelos de relatório da biblioteca de modelos do Braze.
    - Use os **itens de linha** e o menu suspenso **Tags** para encontrar relatórios relevantes para seus casos de uso.<br><br>Janela "Modelos de relatório Braze" com uma lista de modelos Braze para seleção.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Siga a etapa 3 e as seguintes em [Criar um relatório](#creating-a-report) para personalizar ainda mais o relatório de acordo com seu caso de uso.

## Criação de um relatório

1. Vá para **Analytics** > **Report Builder (New)**.
2. Selecione **Criar novo relatório**.
3. No menu suspenso **Rows (Linhas** ), selecione o que você gostaria de relatar:
    - Campanhas
    - Telas
    - Campanhas e telas
    - Canais
    - Tags

    Observe que sua seleção de **linhas** afetará [as métricas que você pode visualizar](#metrics-availability). Por exemplo, você pode visualizar métricas multivariadas somente se fizer relatórios sobre **Canvases** ou **Campaigns** com um detalhamento **de Variant**. Você não pode visualizar essas métricas ao gerar relatórios sobre **campanhas e telas**, mesmo que essas campanhas e telas tenham testes multivariados. 

\![A seção "Rows and columns" (Linhas e colunas) com campos para selecionar as linhas e os agrupamentos do seu relatório.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4\. (Opcional) Selecione **Adicionar detalhamento** para dividir seus dados em exibições mais granulares:
    \- Canais
    \- Data
        \- Use isso para dividir seus dados em intervalos de tempo menores. Por exemplo, se você estiver interessado em saber o desempenho de suas campanhas por dia, selecione a seguinte configuração:
            - **Fileiras**: Campanhas
            - **Agrupamento:** Data
            - **Intervalo:** Dias
    \- Variantes
    \- Campanhas e telas

{% alert tip %}
Experimente diferentes configurações de opções de drilldown para explorar as [várias maneiras de detalhar seus dados](#metrics-availability).
{% endalert %}

{: start="5"}
5\. Na seção **Colunas**, selecione **Personalizar métricas**.

\![A seção "Customize Metrics" (Personalizar métricas) com opções para selecionar várias métricas.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6\. Procure métricas por categoria e marque a caixa de seleção correspondente para adicionar uma métrica ao seu relatório.
    \- Reorganize as métricas e colunas arrastando o ícone pontilhado para cima ou para baixo.
7\. Em **Conteúdo do relatório**, configure o intervalo de datas para o qual você gostaria de incluir dados em seu relatório.
8\. Em seguida, dependendo de suas seleções na etapa 3, opte por adicionar manual ou automaticamente campanhas, Canvases ou ambos ao seu relatório.
    - **Adicionar manualmente:** Escolha cada campanha ou Canvas a ser incluído no relatório usando os filtros para datas e tags ou canais de **Último envio** ou pesquisando o nome da campanha ou do Canvas.<br><br>\![A seção "Manually add campaigns and canvases" (Adicionar campanhas e telas manualmente) com uma lista de campanhas a serem selecionadas.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Adicionar automaticamente:** Defina regras para quais campanhas ou Canvases devem ser incluídas no relatório. Você só precisa selecionar um campo nesta página.
        \- Observe que, à medida que campanhas ou Canvases adicionais satisfizerem as condições definidas nessa tela, eles serão automaticamente adicionados a execuções futuras do seu relatório.<br><br>A seção "Adicionar campanhas e telas automaticamente" com campos para definir regras para quais campanhas e telas devem ser adicionadas ao relatório.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9\. Execute o relatório selecionando **Salvar & Run**.

{% alert note %}
O relatório pode levar alguns minutos para ser executado, dependendo do intervalo de datas e do número de campanhas ou Canvases que você selecionou na etapa de configuração.
{% endalert %}

## Disponibilidade de métricas

Sua seleção para **Linhas** afeta as métricas que você pode selecionar.

{% alert tip %}
Se você quiser fazer um relatório sobre as variantes ou etapas do Canvas, selecione **Canvases** for rows **(telas** para linhas) e deixe o campo em branco ou selecione **Date (data** ) como a pesquisa. Isso cria um menu suspenso de **visualização do Canvas** para exibir métricas somente para o Canvas ou agrupar métricas por variante, etapa ou mensagem. 

\![O menu suspenso "Canvas View" aberto.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Métrico | Descrição |
| --- | --- |
| Métricas de conversão | Disponível para campanhas, telas, campanhas e telas. |
| Entradas | Disponível para Campanhas, Telas, Campanhas e Telas, Tags. |
| Data do último envio | Disponível para campanhas, telas, campanhas e telas. Só é exibido para campanhas programadas - não é preenchido para campanhas baseadas em ações ou acionadas por API. |
| Envia | Disponível para cada canal relevante. |
| Mensagens enviadas | Disponível para Campanhas, Telas, Campanhas e Telas, Tags. |
| Linha de assunto | Disponível para campanhas de e-mail com drilldown **de variantes**, Canvases e Canvases com drilldown **de variantes**. |
| Receita total | Disponível para Campanhas, Telas, Campanhas e Telas, Tags. Indisponível com a pesquisa de **canais**. |
| Impressões exclusivas | Disponível para Campanhas, Telas, Campanhas e Telas, Tags. |
| Destinatários exclusivos | Disponível para Campanhas, Telas, Campanhas e Telas, Tags. Indisponível com a pesquisa de **canais**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Visualização de um relatório

Depois de executar o relatório, você pode visualizar os resultados em formato de tabela na página do relatório. 

\![Uma tabela dos dados do relatório para cada métrica da campanha.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Criação de um gráfico de relatório

Na parte inferior da página, você pode criar um gráfico dos seus dados selecionando um **tipo de gráfico** e configurando as métricas do gráfico. Por padrão, você verá a primeira métrica.

\![Um gráfico dos dados do relatório com opções para configurar o eixo x, o eixo y, o tipo de gráfico e muito mais.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Para criar um gráfico de linhas, selecione **Data** como uma opção de pesquisa ao configurar o relatório. Isso exibirá as tendências ao longo do tempo.
{% endalert %}

#### Download de um gráfico de relatório

Para fazer download de uma imagem do gráfico do relatório, selecione o ícone pontilhado e escolha uma opção de download.

\![Um menu com opções de download para diferentes formatos de arquivo.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Compartilhamento de um relatório

Você pode compartilhar um link do painel para o relatório selecionando **Compartilhar** e uma destas opções:
- **Compartilhe um link:** Copie e compartilhe o link.

\!["Compartilhar um link" com um link para o relatório.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **Enviar ou agendar um e-mail:** Envie um e-mail imediatamente ou em um horário determinado que contenha um link de download que expira após uma hora. Você pode selecionar destinatários entre os usuários do painel listados no menu suspenso **Email Recipients (Destinatários de e-mail** ) ou inserir qualquer outro endereço de e-mail.

Janela "Agendar um e-mail" com campos para escolher como o relatório será formatado, quem deverá recebê-lo e quando deverá ser enviado.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Baixar CSV:** Faça o download de um arquivo CSV do relatório.

## Adição de um relatório a um painel

1. Selecione o ícone pontilhado na parte superior da tabela de relatórios.
2. Selecione **Adicionar ao painel**.
3. Selecione se deseja criar um novo painel ou adicionar a um painel existente.<br><br>Janela com opções para selecionar se você deseja adicionar o relatório a um painel novo ou existente.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Siga as etapas do [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) para saber mais sobre como criar um painel.

