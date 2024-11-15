---
nav_title: Criando um Cartão de Banner
article_title: Criando um Cartão de Banner
permalink: "/create_banner_card/"
description: "Este artigo de referência aborda como criar e enviar Cartões de Banner usando campanhas Braze."
page_type: reference
---

# Criando um Cartão de Banner

> Este artigo aborda como criar um Cartão de Banner no Braze ao construir campanhas.

Semelhante aos [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), os Banner Cards estão incorporados diretamente no seu app ou site para que você possa envolver os usuários com uma experiência que parece natural. Eles são uma solução rápida e sem costura para criar mensagens personalizadas para seus usuários, enquanto ampliam o alcance de outros canais (como e-mail ou notificações por push). 

Os cartões de banner são ótimos para:

- Destacando conteúdo em destaque
- Notificando usuários sobre eventos futuros
- Compartilhando atualizações sobre programas de fidelidade

Porque os Cartões de Banner personalizam cada vez que um usuário inicia uma nova sessão e podem ser configurados para nunca expirar, eles são uma ferramenta útil para adicionar à sua estratégia de engajamento.

{% alert important %}
Os Cartões de Banner estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Pré-requisito: Determinar colocação

Antes de criar um Cartão de Banner, você deve designar áreas em seu app onde deseja exibir o Cartão de Banner. Isso também é referido como a colocação. Depois de criar uma colocação, você pode selecioná-la ao criar sua campanha de Cartão de Banner. Se você já tem uma colocação, pule para [etapa 1](#step-1-create-your-campaign).

Para criar uma colocação:

1. Acessar **Configurações** > **Colocações de Cartão de Banner**.
2. Dê um nome para a colocação do seu cartão de banner.
3. (Opcional) Adicione uma descrição para explicar onde este Cartão Banner deve ser colocado.
4. Insira um ID de colocação exclusivo. Trabalhe com sua equipe de desenvolvedores para definir este ID, porque eles precisarão usá-lo durante a integração. Evite editar seu ID de colocação após o lançamento, pois isso pode quebrar a integração com seu app ou site.
5. Selecione **Salvar**.

Cada colocação pode ser usada em até 10 campanhas. 

{% alert important %}
Os IDs de colocação são únicos por espaço de trabalho.
{% endalert %}

## Etapa 1: Crie sua campanha

Depois de determinar a colocação do seu cartão de banner, é hora de construir sua campanha.

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **Cartão Banner**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione equipes e tags conforme necessário. As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o Construtor de Relatórios, você pode filtrar pelas tags relevantes.
5. Selecione um [placement](#prerequisite-determine-placement) para associar à sua campanha. Este é o local onde o Cartão Banner aparecerá em seu app ou site.
6. Adicione e nomeie quantas variantes desejar para sua campanha. Você pode escolher diferentes tipos de mensagem e layouts para cada variante adicionada. Para saber mais sobre variantes, consulte [multivariante e Testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

## Etapa 2: Compor um cartão de banner

Para editar os detalhes do conteúdo da sua mensagem:

1. Selecione **Editar mensagem**. O criador irá abrir.
2. Escolha um estilo de linha que se encaixe na sua mensagem. Arraste e solte uma linha na área do canva.
3. Arraste e solte blocos na linha para construir sua mensagem.
4. Defina o [estilo](#styles) da sua mensagem.

### Estilos

Selecione **Estilo** para ajustar as configurações a serem aplicadas a todos os blocos na mensagem.

![Painel de estilo do compositor do cartão de banner.]({% image_buster /assets/img/banner_cards/banner_card_styles.png %})

Aqui, você pode fornecer estilos personalizados, como propriedades de fundo, configurações de borda e padrões para seus Cartões de Banner. Os estilos aplicados aqui podem ser substituídos para um bloco ou linha específica. Para substituir estilos, selecione o bloco ou a linha específica para visualizar suas propriedades e fazer alterações.

### Comportamento ao clicar

Quando seu cliente clica em um link no Cartão de Banner, você pode navegar mais fundo em seu app ou redirecioná-los para outra página da web.

Você também pode escolher registrar um atributo personalizado ou evento personalizado. Isso atualizará o perfil do seu cliente com dados personalizados quando eles clicarem no Cartão Banner.

## Etapa 3: Construa o restante da sua campanha

Em seguida, crie o restante de sua campanha. Consulte as próximas seções para mais detalhes sobre como usar melhor nossas ferramentas para criar Cartões de Banner.

### Escolha uma duração de campanha

Selecione a data e hora de início para a campanha do cartão Banner. 

Por padrão, os Cartões de Banner duram indefinidamente. Se desejado, selecione **End Time** para especificar uma data e hora de término.

### Escolha os usuários a serem direcionados

Em seguida, direcione os usuários escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente uma visão geral de como é a população aproximada desse segmento neste momento. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

### Selecionar eventos de conversão

Braze permite que você acompanhe com que frequência os usuários realizam ações específicas e eventos de conversão, após receber uma campanha. É possível permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

## Etapa 4: Testar e implantar

Após construir sua campanha, teste e revise-a para garantir que sua campanha funcione como esperado. Então, você está pronto para lançar sua campanha de Cartão de Banner!

## Coisas para saber

### Expiração dos Cartões de Banner

Por padrão, os Cartões Banner não têm uma data de expiração, mas você pode adicionar uma data de término opcional.

### Gestão de colocação

As colocações são únicas por espaço de trabalho, e cada colocação pode ser usada em até 10 campanhas.

Os IDs de colocação devem ser exclusivos para um espaço de trabalho e não devem ser editados após o lançamento. Trabalhe com sua equipe de desenvolvedores para definir este ID, porque eles precisarão usá-lo durante a integração. 

### Análise de dados

A tabela a seguir define as principais métricas do Cartão Banner.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href='https://braze.com/docs/user_guide/data_and_analytics/report_metrics#total-impressions'>Total de impressões</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-impressions'>Impressões únicas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#total-clicks'>Total de cliques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-clicks'>Cliques únicos projetados</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event'>Conversões primárias</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}<ul><li>{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</li><li>{% multi_lang_include metrics.md metric='Conversion Rate' %}</li></ul></td>
        </tr>
    </tbody>
</table>

Para uma lista completa de métricas, definições e cálculos, consulte nosso [Glossário de Métricas do Relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).