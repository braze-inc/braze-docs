---
nav_title: Criação de campanhas
article_title: Criação de campanhas de cartões de banner
alias: "/create_banner_card/"
description: "Este artigo de referência aborda como criar e enviar cartões de banner usando campanhas do Braze."
page_type: reference
---

# Criação de campanhas de cartões de banner

> Saiba como criar cartões de banner ao criar uma campanha no Braze. Para saber mais sobre informações gerais, consulte [Sobre cartões de banner]({{site.baseurl}}/developer_guide/banners/).

{% alert important %}
Os cartões de banner estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Pré-requisitos {#prerequisite-determine-placement}

Essas são as versões mínimas do SDK para começar a usar os cartões de banner:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Criação de uma campanha de cartão de banner

{% multi_lang_include banners/creating_placements.md %}

### Etapa 2: Criar uma campanha

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **Cartão de bandeira**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione equipes e tags conforme necessário. As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o Report Builder, você pode filtrar pelas tags relevantes.
5. Selecione o posicionamento que você criou anteriormente para associá-lo à sua campanha.
6. Adicione variantes conforme necessário. Você pode escolher um tipo de mensagem e um layout diferentes para cada uma delas. Para saber mais sobre variantes, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

### Etapa 2: Criador de mensagem

Para criar seu Banner Card, selecione **Editar mensagem**. Aqui, você pode estilizar o cartão e definir o comportamento ao clicar.

#### Etapa 2.1: Estilo do cartão {#styles}

Você pode arrastar e soltar blocos e linhas na área da tela para começar a criar sua mensagem. Para personalizar as propriedades do plano de fundo da mensagem, as configurações de borda e muito mais, selecione **Styles (Estilos**). Se você quiser personalizar apenas o estilo de um bloco ou linha específica, selecione-o para fazer alterações.

![Painel de estilo do criador do cartão de banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Etapa 2.2: Definir o comportamento ao clicar

Quando um cliente clica em um link no cartão de banner, você pode optar por navegar mais profundamente em seu app ou redirecioná-lo para outra página da Web. Além disso, é possível optar por [registrar um atributo ou evento personalizado]({{site.baseurl}}/developer_guide/analytics/), que atualizará o perfil do cliente com dados personalizados quando ele clicar no cartão de banner.

### Etapa 3: Definir a prioridade do cartão {#set-card-priority}

Quando várias campanhas fazem referência à mesma ID de colocação, os cartões são exibidos em ordem de nível de prioridade. Por padrão, os cartões de banner recém-criados são definidos como médios, mas você pode definir manualmente a prioridade como alta, média ou baixa. Se vários cartões tiverem o mesmo nível de prioridade, o cartão mais novo será exibido primeiro.

Para definir a prioridade do cartão para um cartão:

1. Selecione **Priority sorter (Classificador** de **prioridade**).
2. Arraste e solte as campanhas para ordená-las com a prioridade correta.
3. Selecione **Aplicar classificação**.

### Etapa 3: Concluir a criação da campanha

Conclua a criação de sua campanha completando o seguinte:

| Opção                    | Descrição |
|---------------------------|-------------|
| **Duração da campanha** | Escolha uma data e hora de início para sua campanha de cartão de banner. Por padrão, os cartões de banner duram indefinidamente. Você pode alterar isso selecionando **End Time** e especificando uma data e hora de término. |
| **Usuários-alvo** | Direcione os usuários escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente um instantâneo da população aproximada do segmento. A associação exata ao segmento é calculada imediatamente antes do envio da mensagem. |
| **Eventos de conversão** | Rastreie a frequência com que os usuários realizam ações específicas após receberem uma campanha. Você pode definir eventos de conversão com uma janela de até 30 dias para contar a ação como uma conversão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Etapa 4: Teste e lançamento

Depois de criar sua campanha, teste-a e revise-a para garantir que ela funcione conforme o esperado. Quando estiver pronto, lance sua campanha de cartão de banner!
