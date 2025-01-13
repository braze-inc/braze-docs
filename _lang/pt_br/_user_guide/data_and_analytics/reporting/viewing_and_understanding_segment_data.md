---
nav_title: Dados do segmento
article_title: Visualização e compreensão dos dados do segmento
page_order: 2
page_type: reference
description: "Este artigo de referência explica a seção de segmentos do seu dashboard do Braze e inclui um resumo das estatísticas fornecidas."
tool: 
  - Segments
  - Reports
  
---
# Dados do segmento

> Este artigo de referência explica a seção de segmentos do seu dashboard do Braze e inclui um resumo das estatísticas fornecidas.

## Acesso a dados sobre seus segmentos e associação

A página **Segments (Segmentos** ) de seu dashboard do Braze contém um resumo de todos os seus segmentos e permite que você examine os dados detalhados de cada um deles. Nessa página, pesquise e clique no nome de um segmento para editar e visualizar seus dados. Para saber como criar um segmento, consulte [Como criar um segmento][3].

![Página de segmentos][1]

Depois de clicar no nome de um segmento, você poderá visualizar as estatísticas e os filtros do segmento. Você pode editar seu segmento adicionando ou excluindo filtros. Não se esqueça de salvar todas as alterações!

![Dados do segmento][2]

Quando você ativar o [rastreamento de análise de dados para um segmento][9], o Braze permitirá que você visualize sessões, eventos personalizados e receita ao longo do tempo por esse segmento.

### Estatísticas do segmento

Você verá as seguintes estatísticas de segmento, que são atualizadas em tempo real à medida que você adiciona ou exclui filtros:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Estatística</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total de usuários</td>
            <td class="no-split">Quantos usuários seu app tem no total.</td>
        </tr>
        <tr>
            <td class="no-split">Usuários selecionados</td>
            <td class="no-split">Quantos usuários estão no seu segmento e qual é a porcentagem da sua base total de usuários.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (usuários pagantes)</td>
            <td class="no-split">O valor do tempo de vida por usuário (LTV) nesse segmento e o valor do tempo de vida por usuário pagante nesse segmento. O LTV é calculado dividindo sua receita vitalícia pelos usuários vitalícios.</td>
        </tr>
        <tr>
            <td class="no-split">Emailable (Optou por receber)</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Emailable' %} Devido às <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">regulamentações de spam</a>, muitas vezes é uma boa ideia pedir aos seus usuários que aceitem explicitamente, implementando uma política de dupla aceitação, onde os usuários devem clicar em um link em um e-mail de confirmação inicial. Para incentivar mais usuários a aceitação, você pode direcionar uma mensagem para <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">aqueles que não optaram nem por aceitar nem por sair</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push Habilitado (Optado)</td>
            <td class="no-split">A capacitação por push refere-se ao número de usuários com pelo menos um token por push. Alguns usuários podem ter vários tokens por push (por exemplo, se tiverem um iPhone e um iPad), portanto, o número de notificações por push enviadas a esse segmento pode ser maior do que o número de usuários "ativados por push". "Aceito" refere-se ao número de usuários que aceitaram explicitamente as notificações por push. Os usuários devem sempre fazer a aceitação explícita para que você envie pushs a eles.</td>
        </tr>
    </tbody>
</table>

### Insights de segmento

É possível ver a performance de um segmento em comparação com outro em um conjunto de KPIs pré-selecionados visitando a página [Segment Insights (Insights de segmento)]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) do seu dashboard.

### envio de mensagens uso
A seção **Envio de Mensagens Use** mostra quais segmentos, campanhas atualmente habilitadas e canvases atualmente habilitados estão direcionando seu segmento.

![Em Uso de mensagens, veja as campanhas em que seu segmento está sendo usado.][4]

### Membro histórico
A seção **Histórico de Membros** mostra como o tamanho do seu segmento mudou ao longo do tempo. Use o menu suspenso para filtrar a associação ao segmento por intervalo de datas. 

A contagem histórica de membros do segmento é uma estimativa, da mesma forma que o tamanho do segmento é uma estimativa antes de você clicar em **Calculate Exact Statistics (Calcular estatísticas exatas**). A Braze estima a contagem de membros consultando os usuários em um intervalo aleatório. Isso significa que, em um dia, a contagem de associação pode se basear em usuários com um número de bloco aleatório de 111 a 120 e, em outro dia, em usuários com um número de bloco aleatório de 8.452 a 8.455. Portanto, o gráfico pode mostrar ligeiras flutuações em cada data devido a diferentes quantidades de usuários que chegam dentro dos intervalos aleatórios de buckets.

![Use o menu suspenso Associação histórica para filtrar a associação do segmento por intervalo de datas.][10]

### Prévia do usuário

Para visualizar informações detalhadas e específicas do usuário sobre seus segmentos, clique em **User Data (Dados do usuário** ) e selecione **User Preview (Prévia do usuário**).

![Informações específicas do usuário][7]

Nessa página, é possível visualizar várias atribuições específicas do usuário, como sexo, idade, número de sessões e se houve aceitação de envio de push e e-mail.

![Prévia do usuário][8]

## Dados de performance por segmento

Use [os modelos de relatório do Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/data_by_segments/) para detalhar as métricas de performance de campanhas, Canvas, variantes e etapas de segmentos.

## Criação de um relatório de detalhamento de segmentos usando o Criador de consultas

Para criar um relatório a partir de um modelo [do Criador de consultas]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/), acesse o **Criador de consultas** e faça o seguinte:

1. Selecione **Criar consulta de SQL** > Modelo de consulta **.**
2. Filtre os modelos para aqueles que têm métricas que incluem "detalhamento de segmentos".
3. Selecione o modelo que deseja usar.
4. Preencha as variáveis em seu modelo SQL na guia [Variables (Variáveis](#variables) ).
5. (opcional) Edite diretamente o SQL no modelo.
6. Clique em **Run Query (Executar consulta**). Seus resultados serão exibidos em uma tabela.

## Variáveis {#variables}

Antes de gerar seu relatório, acesse a guia **Variables (Variáveis** ) para fornecer informações para o modelo do Report Builder, incluindo as variáveis necessárias que variam de acordo com o relatório. 

![][11]

As variáveis incluem:

- **Campanha ou canvas:** Você pode incluir uma ou várias campanhas ou Canvases (não há limite máximo para o número de campanhas ou Canvases que você pode especificar). Se você não especificar nenhuma campanha ou Canvas, o relatório incluirá todas as campanhas ou Canvases do período escolhido.
- **Variante:** Se estiver usando um modelo que ofereça detalhamentos em nível de variante, depois de selecionar uma campanha ou Canvas, você poderá selecionar variantes dentro dessa campanha ou Canvas. Se você selecionar várias variantes, seus resultados serão agrupados por variante.
- **Etapa:** Se você selecionar uma variante do canvas, poderá selecionar uma etapa do canva. Não é possível selecionar uma etapa do canva sem antes selecionar uma variante do Canvas. 
- **Intervalo de tempo:** Identifique o período de tempo do qual você deseja extrair os dados. Se nenhum intervalo de tempo for especificado, o intervalo de tempo será padronizado para os últimos 30 dias.
- **Nome do produto:** Se estiver executando um relatório de dados de compra, você poderá identificar um produto específico para o qual extrair dados.
- **Janela de conversão:** Sempre necessário para relatórios com dados de receita e compra. O número de dias após o recebimento do e-mail ou do clique ao qual o Braze deve atribuir compras ou receita.
- **Segmentos:** Identificar os segmentos pelos quais os dados serão divididos. Se não for especificado, o relatório será executado para todos os segmentos que tenham o rastreamento de dados ativado.
- **Tags:** Especifique tags em **Variáveis** para executar seu relatório para todas as campanhas ou Canvas com determinadas tags. Você pode incluir várias tags. Se você adicionar tags e campanhas ou Canvas específicos a um relatório, o relatório incluirá dados de suas tags e das campanhas ou Canvas especificados. 

## Disponibilidade de dados

Os dados estão disponíveis para períodos de tempo em que essas duas condições são atendidas:

1. [O rastreamento da análise de dados do segmento]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/) está ativado para os segmentos para os quais você deseja ver os dados.
2. O recurso de dados de performance por segmento está ativado. Durante a fase de acesso antecipado, implementaremos gradualmente esse recurso para os clientes. 

Não será possível acessar dados de períodos de tempo anteriores à ativação desse recurso para a sua empresa. Por exemplo, se o rastreamento de análises for ativado para o Segmento A em 1º de outubro e esse recurso for ativado para sua empresa em 2 de outubro, só será possível ver os dados do Segmento A para as campanhas e Canvas que registraram métricas após 2 de outubro. 

Se a sua empresa ativou esse recurso em 2 de outubro e ativou o rastreamento de análises para o Segmento B em 3 de outubro, só será possível ver os dados do Segmento B para as campanhas e Canvas que registraram métricas após 3 de outubro.


[1]: {% image_buster /assets/img_archive/segments.png %}
[2]: {% image_buster /assets/img_archive/A_Tracking.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[4]: {% image_buster /assets/img_archive/historical_membership1.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions
[6]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[7]: {% image_buster /assets/img_archive/preview_users.png %}
[8]: {% image_buster /assets/img_archive/user_preview.png %}
[9]: {{site.baseurl}}/user_guide/data_e_analytics/tracking/segment_analytics_tracking/
[10]: {% image_buster /assets/img_archive/historical_membership2.png %}
[11]:{% image_buster /assets/img_archive/variables_panel.png %}