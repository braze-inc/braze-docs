---
nav_title: Criador de dashboard
article_title: Criador de dashboard
alias: "/dashboard_builder/"
description: "Este artigo de referência aborda como usar o Criador de dashboard para criar dashboards e visualizações usando relatórios criados no Criador de consultas."
page_type: reference
tool:
    - Reports
page_order: 6.1
---

# Criador de dashboard

> Use o Construtor de Dashboard para criar dashboards e visualizações usando relatórios criados no Construtor de Relatórios ou no Construtor de Consultas.

O Construtor de Dashboard permite que você componha e visualize dashboards analíticos personalizados do zero e a partir de dashboards fornecidos pelo Braze. Você pode usar uma fonte de dados sem código (Construtor de Relatórios) ou uma fonte de dados SQL (Construtor de Consultas) para alimentar seu dashboard, ou começar a partir de um dos muitos dashboards fornecidos pelo Braze.

## Criando um dashboard personalizado

1. Acesse **Análise de dados** > **Criador de dashboard**.
2. Selecione **Criar Dashboard**.
3. Selecione qual fonte de dados irá alimentar seus relatórios:
- **Relatórios** que foram construídos no Construtor de Relatórios
- **Consultas Personalizadas** que foram criadas no Construtor de Consultas<br><br>![Janela para selecionar sua fonte de dados para seu dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Agora, siga os passos respectivos para sua fonte de dados:

{% tabs %}
{% tab Reports %}

{: start="4"}
4\. Selecione **\+ Adicionar Bloco** e então escolha um dos relatórios que você criou em [Construtor de Relatórios (Novo)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).

{% alert important %}
Depois que um relatório do Construtor de Relatórios é adicionado a um bloco do Construtor de Dashboard, o bloco não está conectado ao relatório original. Se você editar o relatório original no Construtor de Relatórios, deve excluir o bloco de dashboard existente e criar um novo usando o relatório atualizado como fonte de dados.
{% endalert %}

{: start="5"}
5\. Selecione o ícone de lápis para mudar como o título e o tipo de gráfico são exibidos no bloco.
    \- Você pode alternar entre diferentes tipos de gráficos abaixo da visualização padrão. As opções atuais incluem gráficos de barras (horizontal ou vertical) e gráficos de linha (disponível apenas se você selecionou **Data** como uma opção de detalhamento na configuração do Construtor de Relatórios).<br><br>![Alternâncias para diferentes tipos de gráficos.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Use o menu suspenso de métricas para selecionar quais métricas incluir em sua visualização. Por padrão, a primeira coluna no relatório será a métrica exibida por padrão.
6\. Selecione **Salvar** após ter alterado a visualização para sua preferência.
7\. Adicione um nome, descrição e tag para facilitar a localização do seu dashboard mais tarde.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4\. Selecione **\+ Adicionar Tile** e depois escolha uma consulta que você executou no Construtor de Consultas.
5\. Para editar como os resultados da consulta são exibidos no bloco, selecione o ícone de lápis para alterar o título e o tipo de gráfico.
    \- Você pode alternar entre diferentes tipos de gráficos abaixo da visualização padrão. As opções atuais incluem tabelas, gráficos de barras (horizontal ou vertical) e gráficos de linha.<br><br>![Alternâncias para diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Se você escolher uma das opções de gráfico, use o menu suspenso **Eixo X** para selecionar uma única coluna dos resultados da sua consulta para usar como seu eixo x.
        \- Use o menu suspenso **Eixo Y** para selecionar quais métricas incluir na sua visualização. Por padrão, todas as colunas dos resultados da sua consulta serão exibidas, então desmarque as colunas que você não está interessado em visualizar.<br><br>![Alternâncias para diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        \- (Opcional) Você pode usar o menu suspenso **Agrupamento** para agrupar os resultados da sua consulta. Por exemplo, se você tiver o ID da campanha como um resultado de coluna e quiser somar todas as linhas com esse valor, use o menu suspenso **Agrupamento**.  
        \- (Opcional) Para editar os dados exibidos, selecione a consulta que está anexada à visualização e faça suas edições em [Construtor de Consultas]({{site.baseurl}}/user_guide/analytics/query_builder/).
6\. Selecione **Salvar** após ter alterado a visualização para o seu gosto.
7\. Adicione um nome, descrição e tag para facilitar a localização do seu dashboard mais tarde.
{% endtab %}
{% endtabs %}

{: start="8"}
8\. Repita os passos 4—7 para seu respectivo método até criar o dashboard desejado.
9\. Selecione **Ver Dashboard** > selecione **Executar Dashboard**. 

Seu dashboard pode levar até alguns minutos para terminar de gerar relatórios.

{% alert note %}
Você pode adicionar até 10 tiles a um dashboard.
{% endalert %}

## Gerenciando tiles do dashboard

### Excluir tiles

Exclua um tile do dashboard selecionando **Excluir Tile** na parte inferior do tile. **Esta ação não pode ser revertida.**

### Duplicar tiles

Faça uma cópia do seu tile selecionando **Duplicar Tile** na parte inferior do tile.

### Ajustar o tamanho e a posição do bloco

Ajuste o tamanho do bloco arrastando o canto inferior direito do bloco e ajuste a posição do bloco no dashboard arrastando a alça no canto superior direito do bloco.

## Executando um dashboard

1. Acesse **Análise de dados** > **Criador de dashboard**. A página inicial lista todos os dashboards existentes dentro do seu espaço de trabalho, com os dashboards criados pelo Braze no topo. Eles são indicados com "(Braze)" no título.
2. Selecione o dashboard de seu interesse.
3. Selecione **Executar Dashboard** para carregar o respectivo dashboard usando esse dashboard.

### Dashboards disponíveis

O Braze fornece dashboards pré-construídos para casos de uso frequentes, como análise de receita usando atribuição de último toque. Observe que a capacidade de editar um dashboard ainda não está disponível. Entre em contato com seu gerente de sucesso do cliente se você gostaria de ver certos dashboards no futuro.

#### Receita – atribuição de último ponto de contato

O dashboard **Receita - Atribuição de Último Toque** fornece uma revisão da receita em campanhas, Canvases e canais. Todos os dados de receita são atribuídos à última mensagem tocada durante a janela de atribuição.

Toques incluem _Clique em Email_ (clique no link), _Clique em Cartão de Conteúdo_, _Clique em Mensagem no App_ (excluindo botões de fechar), _Aberturas de Push_, _Clique em Link Curto de SMS_, _Leitura de WhatsApp_, e _Envio de Webhook_.

| Métrico | Definição |
| --- | --- |
| Receita total do último ponto de contato | Uma soma de todos os eventos de receita da campanha e do Canva com um evento de último ponto de contato dentro do intervalo de datas e da janela de atribuição selecionados. |
| Total de conversões de compras | Uma contagem de todos os eventos de receita da campanha e do Canva com um evento de último ponto de contato qualificado. |
| Média de dias para conversão | O tempo médio entre todos os eventos de compra da campanha e do Canva com um evento de último ponto de contato qualificado. |
| Receita por destinatário | Soma da receita de eventos de receita qualificada dividida pelo número de usuários únicos que receberam uma mensagem dentro do intervalo de datas. |
| Compradores exclusivos | Contagem de usuários únicos com um evento de receita qualificado. |
| Receita por país | Soma de todos os eventos de receita da campanha e do Canva com um evento de último ponto de contato, agrupados por país. |
| Receita por campanha | Soma de todos os eventos de receita da campanha e do Canva com um evento de último ponto de contato qualificado, agrupados por campanha. |
| Receita por variante de campanha | Soma de todos os eventos de receita da campanha e do Canva com um evento de último ponto de contato qualificado, agrupados por variante de campanha. |
| Receita por canva | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último ponto de contato qualificado, agrupados por Canvas. |
| Receita por variante de tela | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último ponto de contato qualificado, agrupados por variante do Canvas. |
| Compras por produto | Uma contagem de todas as compras agrupadas por produto. |
| Receita por canal | Soma de todos os eventos de receita da campanha e do Canva com um evento de último ponto de contato qualificado, agrupados por canal. | 
| Série temporal de receitas | Soma de todos os eventos de receita da campanha e do Canva com um evento de último ponto de contato qualificado, agrupados por dia em UTC. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Dispositivos e operadoras

| Métrico | Definição |
| --- | --- |
| Operadoras de dispositivos | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por operadora de dispositivo. |
| Modelo do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por modelo de dispositivo. |
| Sistema operacional dos dispositivos | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por sistema operacional do dispositivo. |
| Tamanho da tela do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados pela resolução (tamanho) da tela do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Insights de Segmento - Email

| Métrico  | Definição  |
|---|---|
| Métricas Semanais de Email (Taxas) | Taxas de engajamento de email (entrega, bounce, abertura, clique, taxas de cancelamento de inscrição) agrupadas por segmento e exibidas como séries temporais semanais.|
| Métricas Semanais de Email (Contagens) | Contagens de engajamento de email (enviados, entregues, bounces, aberturas, cliques, cancelamentos de inscrição) agrupadas por segmento e exibidas como séries temporais semanais.|
| Métricas Semanais de Compra (Taxas) | Taxas de conversão de compra (receita por destinatário) a partir de aberturas e cliques de email, agrupadas por segmento e exibidas como uma série temporal semanal.|
| Métricas Semanais de Compra (Contagens) | Contagens de compras e totais de receita a partir de aberturas e cliques de email, agrupadas por segmento e exibidas como uma série temporal semanal.|
| Engajamento de E-mail por Segmento | Tabela resumo mostrando as métricas totais de engajamento de e-mail (enviados, entregues, devoluções, aberturas, cliques, cancelamentos de inscrição e suas taxas) agregadas por segmento.|
| Compras & Receita por Segmento | Tabela resumo mostrando as métricas totais de compras (compras, receita e receita por destinatário) a partir de aberturas e cliques de e-mail, agregadas por segmento.|
| Top 10 Campanhas para Métricas de Engajamento | Lista classificada de campanhas com as maiores métricas de engajamento de e-mail (métrica configurável para classificação).|
| Bottom 10 Campanhas para Métricas de Engajamento | Lista classificada de campanhas com as menores métricas de engajamento de e-mail (métrica configurável para classificação).|
| Top 10 Canvases para Métricas de Engajamento | Lista classificada de Canvases com as maiores métricas de engajamento de e-mail (métrica configurável para classificação).|
| Bottom 10 Canvases para Métricas de Engajamento | Lista classificada de Canvases com as menores métricas de engajamento de e-mail (métrica configurável para classificação).|
| Top 10 Campanhas para Métricas de Compra | Lista classificada de campanhas com as maiores métricas de conversão de compras a partir do engajamento de e-mail (métrica configurável para classificação).|
| Bottom 10 Campanhas para Métricas de Compra | Lista classificada de campanhas com as menores métricas de conversão de compras a partir do engajamento de e-mail (métrica configurável para classificação).|
| Top 10 Canvases para Métricas de Compra | Lista classificada de Canvases com as maiores métricas de conversão de compras a partir do engajamento de e-mail (métrica configurável para classificação).|
| Bottom 10 Canvases para Métricas de Compra | Lista classificada de Canvases com as menores métricas de conversão de compras a partir do engajamento de e-mail (métrica configurável para classificação).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Análise de Sessões

| Métrico | Definição  |
|---|---|
| \# de sessões por dia (série temporal) | Contagem de sessões únicas agrupadas por dia dentro do intervalo de datas selecionado, exibida como uma série temporal.|
| Média # de sessões por usuário | Número médio de sessões por usuário calculado como total de sessões dividido por usuários únicos dentro do intervalo de datas selecionado.|
| Campanhas convertem em sessões | Contagem de sessões únicas que ocorreram ao mesmo tempo que conversões de campanhas, agrupadas por ID da campanha e classificadas por contagem de sessões.|
| Canvases convertem em sessões | Contagem de sessões únicas que ocorreram ao mesmo tempo que conversões de Canvas, agrupadas por ID do Canvas e classificadas por contagem de sessões.|
| Total # de sessões por usuário | Lista dos 1.000 principais usuários por sua contagem total de sessões dentro do intervalo de datas selecionado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Compartilhe seus comentários conosco

Selecione o **Enviar feedback** botão ou entre em contato com seu gerente de sucesso do cliente para compartilhar seu feedback conosco.

