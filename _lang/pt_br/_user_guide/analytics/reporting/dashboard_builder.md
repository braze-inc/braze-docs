---
nav_title: Criador de painel
article_title: Criador de painel
alias: "/dashboard_builder/"
description: "Este artigo de referência aborda como usar o Dashboard Builder para criar painéis e visualizações usando relatórios criados no Query Builder."
page_type: reference
tool:
    - Reports
page_order: 6.1
---

# Criador de painel

> Use o Dashboard Builder para criar dashboards e visualizações usando relatórios criados no Report Builder ou no Query Builder.

O Dashboard Builder permite que você componha e visualize painéis analíticos personalizados a partir do zero e de painéis fornecidos pela Braze. Você pode usar uma fonte de dados sem código (Report Builder) ou uma fonte de dados SQL (Query Builder) para alimentar seu painel ou começar com um dos vários painéis fornecidos pela Braze.

## Criação de um painel personalizado

1. Vá para **Analytics** > **Dashboard Builder**.
2. Selecione **Create Dashboard (Criar painel**).
3. Selecione a fonte de dados que alimentará seus relatórios:
- **Relatórios** criados no Report Builder
- **Consultas personalizadas** que foram criadas no Query Builder<br><br>Janela para selecionar a fonte de dados para o painel.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Agora, siga as respectivas etapas para sua fonte de dados:

{% tabs %}
{% tab Reports %}

{: start="4"}
4\. Selecione **\+ Add Tile** e, em seguida, escolha um dos relatórios que você criou no [Report Builder (New)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).
5\. Selecione o ícone de lápis para alterar a forma como o título e o tipo de gráfico são exibidos no bloco.
    \- Você pode alternar entre diferentes tipos de gráficos abaixo da visualização padrão. As opções atuais incluem gráficos de barras (horizontais ou verticais) e gráficos de linhas (disponíveis somente se você tiver selecionado **Data** como uma opção de pesquisa na configuração do Report Builder).<br><br>Alterna para diferentes tipos de gráficos.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Use o menu suspenso de métricas para selecionar as métricas a serem incluídas em sua visualização. Por padrão, a primeira coluna do relatório será a métrica padrão exibida.
6\. Selecione **Save (Salvar)** depois de alterar a visualização de acordo com suas preferências.
7\. Adicione um nome, uma descrição e uma tag para facilitar a localização de seu painel mais tarde.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4\. Selecione **\+ Add Tile** e escolha uma consulta que você executou no Query Builder.
5\. Para editar como os resultados da consulta são exibidos no bloco, selecione o ícone de lápis para alterar o título e o tipo de gráfico.
    \- Você pode alternar entre diferentes tipos de gráficos abaixo da visualização padrão. As opções atuais incluem tabelas, gráficos de barras (horizontais ou verticais) e gráficos de linhas.<br><br>Alterna para diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Se você escolher uma das opções de gráfico, use o menu suspenso **Eixo X** para selecionar uma única coluna dos resultados da consulta para usar como eixo x.
        \- Use o menu suspenso **do eixo Y** para selecionar quais métricas serão incluídas em sua visualização. Por padrão, todas as colunas dos resultados da consulta serão exibidas, portanto, desmarque as colunas que você não tem interesse em visualizar.<br><br>Alterna para diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        \- (Opcional) Você pode usar o menu suspenso **Agrupamento** para agrupar os resultados da consulta. Por exemplo, se você tiver o ID da campanha como resultado de uma coluna e quiser somar todas as linhas com esse valor, use o menu suspenso **Agrupamento**.  
        \- (Opcional) Para editar os dados que estão sendo exibidos, selecione a consulta que está anexada ao visual e faça suas edições no [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/).
6\. Selecione **Save (Salvar)** depois de alterar a visualização de acordo com suas preferências.
7\. Adicione um nome, uma descrição e uma tag para facilitar a localização de seu painel mais tarde.
{% endtab %}
{% endtabs %}

{: start="8"}
8\. Repita as etapas 4 a 7 para seu respectivo método até criar o painel desejado.
9\. Selecione **View Dashboard (Exibir painel)** > selecione **Run Dashboard (Executar painel)**. 

Seu painel pode levar alguns minutos para concluir a geração de relatórios.

{% alert note %}
Você pode adicionar até 10 blocos a um painel.
{% endalert %}

## Gerenciamento de blocos do painel

### Excluir blocos

Exclua um bloco do painel selecionando **Excluir bloco** na parte inferior do bloco. **Essa ação não pode ser revertida.**

### Ladrilhos duplicados

Faça uma cópia de seu bloco selecionando **Duplicate Tile (Duplicar bloco** ) na parte inferior do bloco.

### Ajuste o tamanho e a posição do ladrilho

Ajuste o tamanho do bloco arrastando o canto inferior direito do bloco e ajuste a posição do bloco no painel arrastando a alça no canto superior direito do bloco.

## Execução de um painel

1. Vá para **Analytics** > **Dashboard Builder**. A página inicial lista todos os painéis existentes em seu espaço de trabalho, com os painéis criados pelo Braze na parte superior. Eles são indicados com "(Braze)" no título.
2. Selecione o painel em que você está interessado.
3. Selecione **Run Dashboard (Executar painel)** para carregar o respectivo painel usando esse painel.

### Painéis disponíveis

O Braze fornece painéis pré-criados para casos de uso frequente, como análise de receita usando a atribuição de último toque. Observe que a capacidade de editar um painel ainda não está disponível. Entre em contato com o gerente de sucesso do cliente se quiser ver determinado painel no futuro.

#### Receita - Atribuição do último toque

O painel **Atribuição de receita - Último toque** fornece uma análise da receita em campanhas, Canvases e canais. Todos os dados de receita são atribuídos à última mensagem tocada durante a janela de atribuição.

Os toques incluem _clique em e-mail_ (clique em link), _clique em cartão de conteúdo_, _clique em mensagem no aplicativo_ (excluindo botões de fechar), _abertura de push_, _clique em link curto de SMS_, _leitura de WhatsApp_ e _envio de webhook_.

| Métrico | Definição |
| --- | --- |
| Receita total do Last Touch | Uma soma de todos os eventos de receita da campanha e do Canvas com um evento de último toque dentro do intervalo de datas e da janela de atribuição selecionados. |
| Total de conversões de compras | Uma contagem de todos os eventos de receita da campanha e do Canvas com um evento de último toque qualificado. |
| Média de dias para conversão | O tempo médio entre todos os eventos de compra da campanha e do Canvas com um evento de último toque qualificado. |
| Receita por beneficiário | Soma da receita de eventos de receita qualificada dividida pelo número de usuários únicos que receberam uma mensagem dentro do intervalo de datas. |
| Compradores exclusivos | Contagem de usuários únicos com um evento de receita qualificado. |
| Receita por país | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último toque, agrupados por país. |
| Receita por campanha | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último toque qualificado, agrupados por campanha. |
| Receita por variante de campanha | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último toque qualificado, agrupados por variante de campanha. |
| Receita por tela | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último toque qualificado, agrupados por Canvas. |
| Receita por variante de tela | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último toque qualificado, agrupados por variante do Canvas. |
| Compras por produto | Uma contagem de todas as compras agrupadas por produto. |
| Receita por canal | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último toque qualificado, agrupados por canal. | 
| Série temporal de receitas | Soma de todos os eventos de receita da campanha e do Canvas com um evento de último toque qualificado, agrupados por dia em UTC. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Dispositivos e operadoras

| Métrico | Definição |
| --- | --- |
| Portadores de dispositivos | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por operadora de dispositivo. |
| Modelo do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por modelo de dispositivo. |
| Sistema operacional do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por sistema operacional do dispositivo. |
| Tamanho da tela do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados pela resolução (tamanho) da tela do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Informações sobre o segmento - E-mail

| Métrico  | Definição  |
|---|---|
| Métricas semanais de e-mail (taxas) | Taxas de engajamento de e-mail (taxas de entrega, rejeição, abertura, clique, cancelamento de assinatura) agrupadas por segmento e exibidas como séries temporais semanais.|
| Métricas semanais de e-mail (contagens) | Contagens de engajamento de e-mail (enviado, entregue, devoluções, aberturas, cliques, cancelamentos de assinatura) agrupadas por segmento e exibidas como séries temporais semanais.|
| Métricas de compras semanais (taxas) | Taxas de conversão de compras (receita por destinatário) de aberturas e cliques em e-mails, agrupadas por segmento e exibidas como uma série temporal semanal.|
| Métricas de compras semanais (contagens) | Contagens de compras e totais de receita de aberturas e cliques em e-mails, agrupados por segmento e exibidos como uma série temporal semanal.|
| Engajamento de e-mail por segmento | Tabela de resumo mostrando o total de métricas de envolvimento de e-mail (enviadas, entregues, devoluções, aberturas, cliques, cancelamentos de assinatura e suas taxas) agregadas por segmento.|
| Compras & Receita por segmento | Tabela de resumo mostrando o total de métricas de compra (compras, receita e receita por destinatário) de aberturas e cliques em e-mails, agregados por segmento.|
| As 10 principais campanhas para métricas de engajamento | Lista classificada de campanhas com as métricas de envolvimento de e-mail mais altas (métrica configurável para classificação).|
| As 10 campanhas mais baixas para métricas de engajamento | Lista classificada de campanhas com as métricas de engajamento de e-mail mais baixas (métrica configurável para classificação).|
| As 10 principais telas para métricas de engajamento | Lista classificada de Canvases com as métricas de envolvimento de e-mail mais altas (métrica configurável para classificação).|
| As 10 telas mais baixas para métricas de engajamento | Lista classificada de Canvases com as métricas de engajamento de e-mail mais baixas (métrica configurável para classificação).|
| As 10 principais campanhas para métricas de compras | Lista classificada de campanhas com as métricas de conversão de compra mais altas do envolvimento de e-mail (métrica configurável para classificação).|
| As 10 campanhas mais baixas para métricas de compra | Lista classificada de campanhas com as métricas de conversão de compra mais baixas do envolvimento de e-mail (métrica configurável para classificação).|
| As 10 principais telas para métricas de compras | Lista classificada de Canvases com as métricas de conversão de compra mais altas do envolvimento de e-mail (métrica configurável para classificação).|
| As 10 telas mais baixas para métricas de compra | Lista classificada de Canvases com as métricas de conversão de compra mais baixas do envolvimento de e-mail (métrica configurável para classificação).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Análise de sessão

| Métrico | Definição  |
|---|---|
| \# Número de sessões por dia (série temporal) | Contagem de sessões exclusivas agrupadas por dia no intervalo de datas selecionado, exibidas como uma série temporal.|
| Número médio de sessões por usuário | Número médio de sessões por usuário, calculado como o total de sessões dividido por usuários únicos dentro do intervalo de datas selecionado.|
| As campanhas são convertidas em sessões | Contagem de sessões exclusivas que ocorreram ao mesmo tempo que as conversões da campanha, agrupadas por ID da campanha e classificadas por contagem de sessões.|
| As telas são convertidas em sessões | Contagem de sessões exclusivas que ocorreram ao mesmo tempo que as conversões do Canvas, agrupadas por ID do Canvas e classificadas por contagem de sessões.|
| Número total de sessões por usuário | Lista dos 1.000 principais usuários por sua contagem total de sessões dentro do intervalo de datas selecionado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Compartilhe seus comentários conosco

Selecione o botão **Enviar feedback** ou entre em contato com o gerente de sucesso do cliente para compartilhar seu feedback conosco.

