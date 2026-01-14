---
nav_title: Criação de campanhas
article_title: Criação de campanhas de banner no Braze
page_order: 1
description: "Este artigo de referência aborda como criar, compor, configurar e enviar Banners usando campanhas do Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Criação de campanhas de banner

> Saiba como criar Banners quando você cria uma campanha no Braze. Para obter mais informações gerais, consulte [Sobre banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Pré-requisitos

Antes de lançar sua campanha de banner, sua equipe de desenvolvimento precisará [configurar os posicionamentos em seu aplicativo ou site]({{site.baseurl}}/developer_guide/banners/creating_placements/). Você ainda pode elaborar sua campanha de banner nesse meio tempo, mas não poderá lançar a campanha.

## Criação de uma campanha de banner

{% multi_lang_include banners/creating_placements.md section="user" %}

### Etapa 2: Criar uma campanha

1. Vá para **Messaging** > **Campaigns** ( **Mensagens** > **Campanhas** ) e selecione **Create Campaign (Criar campanha**).
2. Selecione **o banner**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione equipes e tags conforme necessário. As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o Report Builder, você pode filtrar pelas tags relevantes.
5. Selecione o posicionamento que você criou anteriormente para associá-lo à sua campanha.
6. Adicione variantes conforme necessário. Você pode escolher um tipo de mensagem e um layout diferentes para cada uma delas. Para obter mais informações sobre variantes, consulte [Testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).

### Etapa 3: Composição de um banner {#compose-a-banner}

Para compor seu banner, você pode optar por:

- Comece com um modelo em branco
- Use um modelo de banner do Braze
- Selecione um modelo de banner salvo

Opção para escolher um banner em branco ou um modelo.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Etapa 3.1: Estilo do banner

Você pode arrastar e soltar blocos e linhas na área da tela para começar a criar sua mensagem.

Para personalizar as propriedades do plano de fundo da mensagem, as configurações de borda e muito mais, selecione **Styles (Estilos**). Se você quiser personalizar apenas o estilo de um bloco ou linha específica, selecione-o para fazer alterações.

\![Painel de estilo do compositor de banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Etapa 3.2: Definir o comportamento ao clicar (opcional)

Quando um usuário clica em um link no Banner, você pode optar por navegar mais profundamente em seu aplicativo ou redirecioná-lo para outra página da Web. Além disso, você pode optar por [registrar um atributo ou evento personalizado]({{site.baseurl}}/developer_guide/analytics/), que atualizará o perfil do usuário com dados personalizados quando ele clicar no banner.

{% alert important %}
{::nomarkdown}
O comportamento ao clicar pode ser substituído se um elemento específico (como um botão, link ou imagem do banner) tiver seu próprio comportamento ao clicar. Por exemplo, considerando os seguintes comportamentos ao clicar:<br><ul><li>Um banner tem um comportamento de clique que redireciona para a página inicial de um site.</li><li>Uma imagem no banner tem um comportamento de clique que redireciona para a página de produto de um site.</li></ul>Se um usuário clicar na imagem, ele será redirecionado para a página do produto. No entanto, ao clicar na área ao redor do banner, o usuário será redirecionado para a página inicial.
{:/}
{% endalert %}

#### Etapa 3.3: Adicionar propriedades personalizadas (opcional) {#custom-properties}

Você pode adicionar propriedades personalizadas a um Banner para anexar metadados estruturados, como strings ou objetos JSON. Essas propriedades não afetam a forma como o Banner é exibido, mas podem ser [acessadas por meio do Braze SDK]({{site.baseurl}}/developer_guide/banners/placements/) para modificar o comportamento ou a aparência do seu aplicativo. Por exemplo, você poderia:

- Envie metadados para suas análises ou integrações de terceiros.
- Use metadados, como um objeto `timestamp` ou JSON, para acionar a lógica condicional.
- Controle o comportamento de um banner com base nos metadados incluídos, como `ratio` ou `format`.

Para adicionar uma propriedade personalizada, selecione **Configurações** > **Propriedades** > **Adicionar propriedade**.

A página de propriedades mostra a opção de adicionar a primeira propriedade personalizada a uma campanha de banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propriedade que você gostaria de adicionar, preencha o seguinte:

| Campo | Descrição | Exemplo |
|-------|-------------|---------|
| Tipo de propriedade | O tipo de dados da propriedade. Os tipos compatíveis incluem string, booleano, número, registro de data e hora, URL de imagem e objeto JSON. | Cordas |
| Chave de propriedade | O identificador exclusivo da propriedade. Essa chave é usada no SDK para acessar a propriedade. | `color` |
| Valor | O valor atribuído à propriedade. Deve corresponder ao tipo de propriedade selecionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Quando terminar, selecione **Concluído**.

\![A página de propriedades com uma propriedade de cadeia de caracteres com uma chave de cor e valor de #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

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

1. Em **Target Audiences (Públicos-alvo**), escolha segmentos ou filtros para restringir seu público. Você receberá automaticamente uma prévia da população aproximada do segmento. A associação exata ao segmento é calculada imediatamente antes de a mensagem ser enviada.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. Em **Assign Conversions (Atribuir conversões**), acompanhe a frequência com que os usuários realizam ações específicas após receberem uma campanha, definindo eventos de conversão com uma janela de até 30 dias para contar a ação como uma conversão.

### Etapa 8: Lance sua campanha

Quando terminar de criar e testar sua campanha de banner, você estará pronto para lançá-la!
