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

> Use o Dashboard Builder para criar dashboards e visualizações usando relatórios criados no Report Builder ou no Query Builder.

O Dashboard Builder permite que você crie e visualize dashboards analíticos personalizados a partir do zero e de modelos fornecidos pela Braze. Você pode usar uma fonte de dados sem código (Report Builder) ou uma fonte de dados SQL (Query Builder) para alimentar seu dashboard ou começar com um dos muitos modelos do Braze.

## Criação de um dashboard personalizado

1. Acesse **Análise de dados** > **Criador de dashboard**.
2. Selecione **Create Dashboard**.
3. Selecione a fonte de dados que alimentará seus relatórios:
- **Relatórios** criados no Report Builder
- **Consultas personalizadas** que foram criadas no Query Builder<br><br>![Janela para selecionar a fonte de dados para seu dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Agora, siga as respectivas etapas para sua fonte de dados:

{% tabs %}
{% tab Relatórios %}

{: start="4"}
4\. Selecione **\+ Add Tile** e, em seguida, escolha um dos relatórios que você criou no [Report Builder (New)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).
5\. Selecione o ícone de lápis para alterar a forma como o título e o tipo de gráfico são exibidos no bloco.
    \- Você pode alternar entre diferentes tipos de gráficos abaixo da visualização padrão. As opções atuais incluem gráficos de barras (horizontais ou verticais) e gráficos de linhas (disponíveis somente se você tiver selecionado **Data** como uma opção de pesquisa na configuração do Report Builder).<br><br>![Alterna para diferentes tipos de gráficos.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Use o menu suspenso de métricas para selecionar as métricas a serem incluídas em sua visualização. Por padrão, a primeira coluna do relatório será a métrica padrão exibida.
6\. Selecione **Save (Salvar)** depois de alterar a visualização de acordo com suas preferências.
7\. Adicione um nome, uma descrição e uma tag para facilitar a localização de seu dashboard mais tarde.
{% endtab %}
{% tab Consultas personalizadas %}
{: start="4"}
4\. Selecione **\+ Add Tile** e escolha uma consulta que você tenha executado no Query Builder.
5\. Para editar como os resultados da consulta são exibidos no bloco, selecione o ícone de lápis para alterar o título e o tipo de gráfico.
    \- Você pode alternar entre diferentes tipos de gráficos abaixo da visualização padrão. As opções atuais incluem tabelas, gráficos de barras (horizontais ou verticais) e gráficos de linhas.<br><br>![Alterna para diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Se você escolher uma das opções de gráfico, use o menu suspenso **do eixo X** para selecionar uma única coluna dos resultados da consulta a ser usada como eixo x.
        \- Use o menu suspenso **do eixo Y** para selecionar quais métricas serão incluídas em sua visualização. Por padrão, todas as colunas dos resultados da consulta serão exibidas, portanto, desmarque as colunas que não lhe interessam.<br><br>![Alterna para diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        \- (Opcional) Você pode usar o menu suspenso **Agrupamento** para agrupar os resultados da consulta. Por exemplo, se você tiver o ID da campanha como resultado de uma coluna e quiser somar todas as linhas com esse valor, use o menu suspenso **Agrupamento**.  
        \- (Opcional) Para editar os dados que estão sendo exibidos, selecione a consulta que está anexada ao visual e faça suas edições no [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/).
6\. Selecione **Save (Salvar)** depois de alterar a visualização de acordo com suas preferências.
7\. Adicione um nome, uma descrição e uma tag para facilitar a localização de seu dashboard mais tarde.
{% endtab %}
{% endtabs %}

{: start="8"}
8\. Repita as etapas 4 a 7 para seu respectivo método até criar o dashboard desejado.
9\. Selecione **View Dashboard (Exibir painel)** > selecione **Run Dashboard (Executar painel)**. 

Seu dashboard pode levar alguns minutos para terminar de gerar relatórios.

{% alert note %}
Você pode adicionar até 10 blocos a um dashboard.
{% endalert %}

## Gerenciando blocos do dashboard

### Excluir blocos

Exclua um bloco do dashboard selecionando **Excluir bloco** na parte inferior do bloco. **Essa ação não pode ser revertida.**

### Ladrilhos duplicados

Faça uma cópia de seu bloco selecionando **Duplicate Tile (Duplicar bloco** ) na parte inferior do bloco.

### Ajuste o tamanho e a posição do ladrilho

Ajuste o tamanho do bloco arrastando o canto inferior direito do bloco e ajuste a posição do bloco no dashboard arrastando a alça no canto superior direito do bloco.

## Execução de um modelo de dashboard

1. Acesse **Análise de dados** > **Criador de dashboard**. A página inicial lista todos os dashboards existentes em seu espaço de trabalho, com modelos criados pelo Braze na parte superior. Eles são indicados com "(Braze)" no título.
2. Selecione o dashboard de seu interesse.
3. Selecione **Run Dashboard (Executar painel)** para carregar o respectivo dashboard usando esse modelo.

### Modelos de dashboard disponíveis

A Braze oferece modelos de dashboards pré-criados para casos de uso frequente, como análise de receita usando a atribuição do último ponto de contato. Note que a capacidade de editar um dashboard de modelo ainda não está disponível. Entre em contato com seu gerente de sucesso do cliente se quiser ver determinados modelos de dashboard em futuras versões de modelos.

#### Receita – atribuição de último ponto de contato

O modelo **Receita - Atribuição do último ponto de contato** fornece uma análise da receita em campanhas, telas e canais. Todos os dados de receita são atribuídos à última mensagem tocada durante a janela de atribuição.

Os toques incluem _clique em e-mail_, _clique em cartão de conteúdo_, _clique em mensagem no app_, _clique em link curto de SMS_, _leitura de WhatsApp_ e _envio de webhook_.

| Métricas | Definição |
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

| Métricas | Definição |
| --- | --- |
| Operadoras de dispositivos | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por operadora de dispositivo. |
| Modelo do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por modelo de dispositivo. |
| Sistema operacional dos dispositivos | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por sistema operacional do dispositivo. |
| Tamanho da tela do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados pela resolução (tamanho) da tela do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Compartilhe seus comentários conosco

Selecione o botão **Enviar feedback** ou entre em contato com o gerente de sucesso do cliente para compartilhar seu feedback conosco.

