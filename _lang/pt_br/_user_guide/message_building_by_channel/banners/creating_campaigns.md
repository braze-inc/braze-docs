---
nav_title: Criação de campanhas
article_title: Criação de campanhas de banner no Braze
page_order: 1
description: "Este artigo de referência aborda como criar, criar, configurar e enviar Banners usando campanhas do Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Criação de campanhas de banner

> Saiba como criar Banners quando você cria uma campanha no Braze. Para saber mais sobre informações gerais, consulte [Sobre banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Pré-requisitos

Antes de lançar sua campanha de banner, sua equipe de desenvolvimento precisará [configurar os canais em seu app ou site]({{site.baseurl}}/developer_guide/banners/creating_placements/). Você ainda pode elaborar sua campanha de banner nesse meio tempo, mas não poderá lançar a campanha.

## Criação de uma campanha de banner

{% multi_lang_include banners/creating_placements.md section="user" %}

### Etapa 2: Criar uma campanha

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **o banner**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione equipes e tags conforme necessário. As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o Report Builder, você pode filtrar pelas tags relevantes.
5. Selecione o posicionamento que você criou anteriormente para associá-lo à sua campanha.
6. Adicione variantes conforme necessário. Você pode escolher um tipo de mensagem e um layout diferentes para cada uma delas. Para saber mais sobre variantes, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).

### Etapa 3: Crie um banner {#compose-a-banner}

Para criar seu banner, selecione **Editar mensagem**. Aqui, você pode criar o banner e definir o comportamento ao clicar. 

#### Etapa 3.1: Estilo do banner

Você pode arrastar e soltar blocos e linhas na área da tela para começar a criar sua mensagem.

Para personalizar as propriedades do plano de fundo da mensagem, as configurações de borda e muito mais, selecione **Styles (Estilos**). Se você quiser personalizar apenas o estilo de um bloco ou linha específica, selecione-o para fazer alterações.

![Painel de estilo do criador do banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Etapa 3.2: Definir o comportamento ao clicar

Quando um usuário clica em um link no Banner, você pode optar por navegar mais profundamente em seu app ou redirecioná-lo para outra página da Web. Além disso, é possível optar pelo [registro de um atributo personalizado ou evento]({{site.baseurl}}/developer_guide/analytics/), que atualizará o perfil do usuário com dados personalizados quando ele clicar no banner.

{% alert important %}
{::nomarkdown}
O comportamento ao clicar pode ser substituído se um elemento específico (como um botão, link ou imagem do Banner) tiver seu próprio comportamento ao clicar. Por exemplo, considerando os seguintes comportamentos ao clicar:<br><br><ul><li>Um banner tem um comportamento ao clicar que redireciona para a página inicial de um site.</li><li>Uma imagem no banner tem um comportamento ao clicar que redireciona para a página de produto de um site.</li></ul>Se um usuário clicar na imagem, ele será redirecionado para a página do produto. No entanto, ao clicar na área ao redor do banner, o usuário será redirecionado para a página inicial.
{:/}
{% endalert %}

### Etapa 4: Definir a duração da campanha

Escolha uma data e hora de início para sua campanha de banner. Por padrão, os Banners duram indefinidamente. Você pode alterar isso selecionando **End Time (Hora de término** ) e especificando uma data e hora de término.

### Etapa 5: Definir a prioridade do banner (opcional)

[A prioridade do banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) determina a ordem em que os banners são exibidos se eles compartilharem o mesmo posicionamento. Para definir manualmente a prioridade:

1. Selecione **Definir prioridade exata**.
2. Arraste e solte as campanhas para ordená-las com a prioridade correta.
3. Selecione **Aplicar classificação**.

{% alert tip %}
Se você tiver várias campanhas de banner usando o mesmo ID de posicionamento, recomendamos usar o classificador de prioridade de arrastar e soltar para definir a prioridade exata.
{% endalert %}

### Etapa 6: Teste sua mensagem (opcional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Etapa 7: Concluir a criação da campanha

Conclua a criação de sua campanha completando o seguinte:

| Opção | Descrição |
| --- | --- |
| **Usuários-alvo** | Direcione os usuários escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente um instantâneo da população aproximada do segmento. A associação exata ao segmento é calculada imediatamente antes do envio da mensagem. |
| **Eventos de conversão** | Rastreie a frequência com que os usuários realizam ações específicas após receberem uma campanha. Você pode definir eventos de conversão com uma janela de até 30 dias para contar a ação como uma conversão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 8: Lance sua campanha

Quando terminar de criar e testar sua campanha de banner, você estará pronto para lançá-la!
