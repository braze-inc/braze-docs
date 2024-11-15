---
nav_title: Criador de dashboard
article_title: Criador de dashboard
permalink: "/dashboard_builder/"
description: "Este artigo de referência aborda como usar o Criador de dashboard para criar dashboards e visualizações usando relatórios criados no Criador de consultas."
page_type: reference
hidden: true
---

# Criador de dashboard

> Use o Criador de dashboard para criar dashboards e visualizações usando relatórios criados no Criador de consultas. Você pode começar com os modelos de consultas de SQL pré-criados no Query Builder ou escrever suas próprias consultas de SQL personalizadas para obter ainda mais insights.

A Braze oferece modelos de dashboards pré-criados para casos de uso frequente, como análise de receita usando a atribuição do último ponto de contato. Note que a capacidade de editar um dashboard de modelo ainda não está disponível.

{% alert note %}
O Dashboard Builder está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

## Execução de um modelo de dashboard

1. Acesse **Análise de dados** > **Criador de dashboard**. A página inicial lista todos os dashboards existentes em seu espaço de trabalho, com modelos criados pelo Braze na parte superior. Eles são indicados com "(Braze)" no título.
2. Selecione o dashboard de seu interesse.
3. Selecione **Run Dashboard (Executar painel)** para gerar um dashboard usando esse modelo.

### Modelos de dashboard disponíveis

#### Receita – atribuição de último ponto de contato

O modelo **Receita - Atribuição do último ponto de contato** fornece uma análise da receita em campanhas, telas e canais. Todos os dados de receita são atribuídos à última mensagem tocada durante a janela de atribuição.

Os toques incluem `Email Click`, `Content Card Click`, `In-App Message Click`, `SMS Delivery`, `WhatsApp Read`, e `Webhook Send`.

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

## Criação de um dashboard personalizado

1. Selecione **Create Dashboard (Criar painel**) ou um dashboard existente e **Edit (Editar**). Em seguida, selecione **\+ Add Tile**.
2. Selecione **Selecione consulta existente** e escolha uma consulta que você tenha executado no Criador de consultas.
3. Para editar como os resultados da consulta são exibidos no bloco, selecione o ícone de lápis para alterar o título e o tipo de gráfico.<br><br>![Visualização do editor de blocos com opções para alterar o título e o tipo de gráfico.][2]{: style="max-width:60%;"}<br><br>
    - Se estiver selecionando um tipo de gráfico de **coluna**, **barra** ou **LINE**:
        - Selecione um campo da consulta para usar em seu eixo X.
        - Desmarque as colunas que não lhe interessam.<br><br>![Menu suspenso com os tipos de gráfico.][1]{: style="max-width:40%;"}

{: start="4"}        
4\. Certifique-se de salvar suas alterações. Se quiser excluir o bloco, selecione o ícone da lixeira. Os blocos excluídos não podem ser revertidos e devem ser recriados.
5\. Ajuste o tamanho do bloco arrastando o canto inferior direito e a posição do bloco no dashboard arrastando a alça no canto superior direito.<br><br>![Ladrilho sendo arrastado pela alça.][3]<br><br>
6\. Adicione mais blocos até que seu dashboard esteja completo.
7\. Selecione **View Dashboard (Exibir painel)** e, em seguida, selecione **Run Dashboard (Executar painel)**. Seu dashboard pode levar alguns minutos para terminar de gerar relatórios.

## Compartilhe seus comentários conosco

Sinta-se à vontade para compartilhar seus comentários conosco entrando em contato com o gerente de sucesso do cliente ou respondendo ao e-mail de capacitação que recebeu.

[1]: {% image_buster /assets/img/chart_type.png %}
[2]: {% image_buster /assets/img/sample_tile.png %}
[3]: {% image_buster /assets/img/drag_tile.png %}
