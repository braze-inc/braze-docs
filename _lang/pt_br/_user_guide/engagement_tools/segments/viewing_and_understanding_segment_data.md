---
nav_title: Dados do segmento
article_title: Visualização e compreensão dos dados do segmento
page_order: 4
page_type: reference
description: "Esta página explica a seção de segmentos do painel de controle do Braze e inclui um resumo das estatísticas fornecidas."
alias: /viewing_and_understanding_segment_data/
tool: 
  - Segments
  - Reports
  
---
# Dados do segmento

> Esta página explica a seção de segmentos do painel de controle do Braze e inclui um resumo das estatísticas fornecidas.

## Acesso a dados sobre seus segmentos e associação

A página **Segmentos** de seu painel do Braze contém um resumo de todos os seus segmentos e permite que você examine os dados detalhados de cada um deles. Nessa página, pesquise e selecione o nome de um segmento para editar e visualizar seus dados. Para saber como criar um segmento, consulte [Criação de um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment).

\![Página de segmentos]({% image_buster /assets/img_archive/segments.png %})

Depois de selecionar o nome de um segmento, você pode visualizar as estatísticas e os filtros do segmento e editar o segmento adicionando ou excluindo filtros. Não se esqueça de salvar todas as alterações!

Quando você ativa [o rastreamento analítico para um segmento]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/), pode visualizar sessões, eventos personalizados e receita ao longo do tempo para esse segmento.

\![Alternância de rastreamento do Analytics para um segmento]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Estatísticas do segmento

Você pode visualizar as seguintes estatísticas de segmento, que são atualizadas em tempo real à medida que você adiciona ou exclui filtros:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Estatísticas</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total de usuários</td>
            <td class="no-split">Quantos usuários seu aplicativo tem no total.</td>
        </tr>
        <tr>
            <td class="no-split">Usuários selecionados</td>
            <td class="no-split">Quantos usuários estão no seu segmento e qual é a porcentagem da sua base total de usuários.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (usuários pagantes)</td>
            <td class="no-split">O valor vitalício por usuário (LTV) nesse segmento e o valor vitalício por usuário pagante nesse segmento. O LTV é calculado dividindo sua receita vitalícia pelos usuários vitalícios.</td>
        </tr>
        <tr>
            <td class="no-split">Emails (opt-in)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} Devido às <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">regulamentações sobre spam</a>, é uma boa ideia pedir aos seus usuários que aceitem explicitamente, implementando uma política de aceitação dupla em que os usuários devem clicar em um link em um e-mail de confirmação inicial. Para incentivar mais usuários a optarem por participar, você pode direcionar uma mensagem para <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">aqueles que não optaram por participar nem por sair</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push ativado (ativado)</td>
            <td class="no-split">O push ativado refere-se ao número de usuários com pelo menos um token push. Alguns usuários podem ter vários tokens push (por exemplo, se tiverem um iPhone e um iPad), portanto, o número de notificações push enviadas a esse segmento pode ser maior do que o número de usuários "habilitados para push". "Opted In" refere-se ao número de usuários que optaram explicitamente por receber notificações por push. Os usuários devem sempre aceitar explicitamente o envio de pushes.</td>
        </tr>
    </tbody>
</table>

### Informações sobre o segmento

Você pode ver o desempenho de um segmento em comparação com outro em um conjunto de KPIs pré-selecionados visitando a página [Segment Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) do seu painel.

### Uso de mensagens
A seção **Uso de mensagens** mostra quais segmentos, campanhas atualmente ativadas e telas atualmente ativadas estão direcionando seu segmento.

### Histórico de filiação

A seção **Membership Historical** mostra como o tamanho do seu segmento mudou ao longo do tempo. Use o menu suspenso para filtrar a associação ao segmento por intervalo de datas.

Para saber mais sobre como monitorar a associação e o tamanho do seu segmento, consulte [Medição do tamanho do segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

### Visualização do usuário

Para visualizar informações detalhadas e específicas do usuário sobre seus segmentos, clique em **User Data (Dados do usuário** ) e selecione **User Preview (Visualização do usuário**).

Nessa página, é possível visualizar vários atributos específicos do usuário, como sexo, idade, número de sessões e se ele optou por receber push e e-mail.

Observe que, nos casos em que o segmento é muito pequeno em relação ao tamanho do espaço de trabalho, é possível que a Visualização do usuário retorne zero usuários. Isso não significa necessariamente que não há nenhum usuário no seu segmento; execute [Calculate Exact Stats (Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/#statistics-for-segment-size) ) para determinar o tamanho exato do seu segmento.

\![Visualização do usuário]({% image_buster /assets/img_archive/user_preview.png %})

## Visualização de dados de desempenho por segmento

Use [os modelos de relatório do Query Builder]({{site.baseurl}}/user_guide/analytics/reporting/data_by_segments/) para detalhar as métricas de desempenho de campanhas, Canvas, variantes e etapas por segmentos.

## Criação de um relatório de detalhamento de segmento usando o Query Builder

Para criar um relatório a partir de um modelo [do Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/), acesse o **Query Builder** e faça o seguinte:

1. Selecione **Criar consulta SQL** > **Modelo de consulta**.
2. Filtre os modelos para aqueles que têm métricas que incluem "detalhamentos de segmentos".
3. Selecione o modelo que você deseja usar.
4. Preencha as variáveis em seu modelo SQL na guia [Variables (Variáveis](#variables) ).
5. (Opcional) Edite diretamente o SQL no modelo.
6. Selecione **Run Query (Executar consulta**). Seus resultados serão exibidos em uma tabela.

## Variáveis {#variables}

Antes de gerar seu relatório, vá para a guia **Variables (Variáveis** ) para fornecer informações para o modelo do Report Builder, incluindo as variáveis necessárias que variam de acordo com o relatório. 

As variáveis incluem:

- **Campanha ou Canvas:** Você pode incluir uma ou várias campanhas ou Canvases (não há limite máximo para o número de campanhas ou Canvases que você pode especificar). Se você não especificar nenhuma campanha ou Canvase, o relatório incluirá todas as campanhas ou Canvases do período de tempo escolhido.
- **Variante:** Se estiver usando um modelo que ofereça detalhamentos em nível de variante, depois de selecionar uma campanha ou tela, você poderá selecionar variantes dentro dessa campanha ou tela. Se você selecionar várias variantes, seus resultados serão agrupados por variante.
- **Etapa:** Se você selecionar uma variante do Canvas, poderá selecionar uma etapa do Canvas. Não é possível selecionar uma etapa sem antes selecionar uma variante do Canvas. 
- **Intervalo de tempo:** Identifique o período de tempo do qual você deseja extrair os dados. Se nenhum intervalo de tempo for especificado, o intervalo de tempo será padronizado para os últimos 30 dias.
- **Nome do produto:** Se estiver executando um relatório de dados de compra, você poderá identificar um produto específico para o qual extrair dados.
- **Janela de conversão:** Sempre necessário para relatórios com dados de receita e compra. O número de dias após o recebimento do e-mail ou clique ao qual o Braze deve atribuir compras ou receita.
- **Segmentos:** Identificar os segmentos pelos quais os dados serão divididos. Se não for especificado, o relatório será executado para todos os segmentos que tenham o rastreamento analítico ativado.
- **Tags:** Especifique as tags em **Variables** para executar seu relatório para todas as campanhas ou Canvases com determinadas tags. Você pode incluir várias tags. Se você adicionar tags e campanhas ou Canvases específicos a um relatório, o relatório incluirá dados de suas tags e das campanhas ou Canvases especificados. 

## Disponibilidade de dados

Os dados estão disponíveis para períodos de tempo em que essas duas condições são atendidas:

1. [O rastreamento da análise de]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) segmentos está ativado para os segmentos para os quais você deseja ver os dados.
2. O recurso de dados de desempenho por segmento está ativado.

Não é possível acessar dados de períodos de tempo anteriores à ativação desse recurso para sua empresa. Por exemplo, se o rastreamento analítico for ativado para o Segmento A em 1º de outubro e esse recurso for ativado para sua empresa em 2 de outubro, você só poderá visualizar os dados do Segmento A para as campanhas e Canvases que registraram métricas após 2 de outubro. 

Se a sua empresa ativou esse recurso em 2 de outubro e ativou o rastreamento analítico para o Segmento B em 3 de outubro, você só poderá ver os dados do Segmento B para as campanhas e Canvases que registraram métricas após 3 de outubro.


