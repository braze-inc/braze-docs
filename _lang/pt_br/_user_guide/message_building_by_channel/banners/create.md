---
nav_title: Criar um banner
article_title: Criar um banner
page_order: 1
description: "Este artigo de referência aborda como criar, criar, configurar e enviar Banners usando campanhas e Canvas do Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Criar um banner

> Saiba como criar Banners ao criar campanhas e telas no Braze. Para saber mais sobre informações gerais, consulte [Sobre banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

{% alert important %}
A criação de uma mensagem de banner no Canvas está em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

## Pré-requisitos

Antes de lançar seu banner, sua equipe de desenvolvimento deve [configurar posicionamentos em seu app ou site]({{site.baseurl}}/developer_guide/banners/creating_placements/). Enquanto isso, você ainda pode elaborar sua campanha de banner, mas não poderá lançá-la até que os canais estejam configurados.

## Criar uma mensagem de banner

{% multi_lang_include banners/creating_placements.md section="user" %}

### Etapa 2: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? As campanhas são melhores para campanhas de mensagens únicas e direcionadas, enquanto as canvas são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **o banner**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [times]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário. As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o Report Builder, você pode filtrar pelas tags relevantes.
5. Selecione o posicionamento que você criou anteriormente para associá-lo à sua campanha.
6. Adicione variantes conforme necessário. Você pode escolher um tipo de mensagem e um layout diferentes para cada uma delas. Para saber mais sobre variantes, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
7. Escolha uma data e hora de início para sua campanha de banner. Por padrão, os Banners duram indefinidamente. Você pode alterar isso selecionando **End Time** e especificando uma data e hora de término.

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Você pode então selecionar **Copiar da Variante** no menu suspenso **Adicionar Variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Após configurar seu canva, adicione uma etapa de Mensagem no construtor de canva. Dê um nome claro e significativo à sua etapa.
3. Selecione **Banner** como seu canal de envio de mensagens.
4. Selecione um local para o banner.
5. Definir a prioridade do banner. [A prioridade do banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) determina a ordem em que os banners são exibidos se eles compartilharem o mesmo posicionamento.
6. Defina uma expiração para o Banner. Isso pode ser feito após um período de tempo depois que a etapa estiver disponível ou em uma data e hora específicas.

{% endtab %}
{% endtabs %}

### Etapa 3: Crie um banner {#compose-a-banner}

Para criar seu banner, você pode optar por:

- Comece com um modelo em branco
- Usar um modelo de banner do Braze
- Selecione um modelo de banner salvo

![Opção para escolher um Banner em branco ou um modelo.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Etapa 3.1: Estilo do banner

Você pode arrastar e soltar blocos e linhas na área da tela para começar a criar sua mensagem.

Para personalizar as propriedades do plano de fundo da mensagem, as configurações de borda e muito mais, selecione **Styles (Estilos**). Se você quiser personalizar apenas o estilo de um bloco ou linha específica, selecione-o para fazer alterações.

![Painel de estilo do criador do banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Etapa 3.2: Definir o comportamento ao clicar (opcional)

Quando um usuário clica em um link no Banner, você pode optar por navegar mais profundamente em seu app ou redirecioná-lo para outra página da Web. Além disso, é possível optar pelo [registro de um atributo personalizado ou evento]({{site.baseurl}}/developer_guide/analytics/), que atualiza o perfil do usuário com dados personalizados quando ele clica no banner.

{% alert important %}
{::nomarkdown}
O comportamento ao clicar pode ser substituído se um elemento específico (como um botão, link ou imagem do Banner) tiver seu próprio comportamento ao clicar. Por exemplo, considerando os seguintes comportamentos ao clicar:<br><ul><li>Um banner tem um comportamento ao clicar que redireciona para a página inicial de um site.</li><li>Uma imagem no banner tem um comportamento ao clicar que redireciona para a página de produto de um site.</li></ul>Se um usuário clicar na imagem, ele será redirecionado para a página do produto. No entanto, ao clicar na área ao redor do banner, o usuário é redirecionado para a página inicial.
{:/}
{% endalert %}

#### Etapa 3.3: Adicionar propriedades personalizadas (opcional) {#custom-properties}

Você pode adicionar propriedades personalizadas a um Banner para anexar metadados estruturados, como strings ou objetos JSON. Essas propriedades não afetam a forma como o Banner é exibido, mas podem ser [acessadas por meio do SDK do Braze]({{site.baseurl}}/developer_guide/banners/placements/) para modificar o comportamento ou a aparência do seu app. Por exemplo, você poderia:

- Envie metadados para suas análises de dados ou integrações de terceiros.
- Use metadados, como um objeto `timestamp` ou JSON, para disparar a lógica condicional.
- Controle o comportamento de um banner com base nos metadados incluídos, como `ratio` ou `format`.

Para adicionar uma propriedade personalizada, selecione **Configurações** > **Propriedades** > **Adicionar propriedade**.

![A página de propriedades mostra a opção de adicionar a primeira propriedade personalizada a uma campanha de banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propriedade que você gostaria de adicionar, preencha o seguinte:

| Campo | Descrição | Exemplo |
|-------|-------------|---------|
| Tipo de propriedade | O tipo de dados da propriedade. Os tipos suportados incluem string, booleano, número, registro de data e hora, URL de imagem e objeto JSON. | String |
| Chave de propriedade | O identificador exclusivo da propriedade. Essa chave é usada no SDK para acessar a propriedade. | `color` |
| Valor | O valor atribuído à propriedade. Deve corresponder ao tipo de propriedade selecionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Quando terminar, selecione **Concluído**.

![A página de propriedades com uma propriedade string com uma chave de cor e um valor de #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Etapa 4: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campaign %}

#### Definir a prioridade do banner (opcional)

[A prioridade do banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) determina a ordem em que os banners são exibidos se eles compartilharem o mesmo posicionamento. Para definir manualmente a prioridade:

1. Selecione **Definir prioridade exata**.
2. Arraste e solte as campanhas para ordená-las com a prioridade correta.
3. Selecione **Aplicar classificação**.

{% alert tip %}
Se você tiver várias campanhas de banner usando o mesmo ID de posicionamento, recomendamos usar o classificador de prioridade de arrastar e soltar para definir a prioridade exata.
{% endalert %}

#### Escolha seu público

1. Em **Target Audiences (Públicos-alvo**), escolha segmentos ou filtros para restringir seu público. Você recebe automaticamente uma prévia da população aproximada do segmento. A associação exata ao segmento de mensagens é calculada antes do envio da mensagem.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. Em **Atribuir conversões**, rastreie a frequência com que os usuários realizam ações específicas após receberem uma campanha, definindo eventos de conversão com uma janela de até 30 dias para contar a ação como uma conversão.

{% multi_lang_include target_audiences.md %}

#### Selecionar eventos de conversão

O Braze permite rastrear [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), a frequência com que os usuários realizam ações específicas após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão é contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canva. Para mais detalhes sobre como construir o restante do seu canva, implemente [testes multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), e mais, consulte a [Etapa de Construção do seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do canva.

{% endtab %}
{% endtabs %}

### Etapa 5: Teste sua mensagem (opcional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Etapa 6: Revisão e implementação

Depois de terminar de criar sua campanha ou Canva, revise os detalhes, [teste-o]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) e envie-o quando estiver pronto.
