---
nav_title: Mensagens de lembrete selecionadas pelo usuário
article_title: Mensagens de lembrete selecionadas pelo usuário
page_order: 5
page_type: reference
description: "Este artigo de referência explica como usar landing pages, atributos personalizados e campanhas da Braze para permitir que os usuários se inscrevam para receber mensagens de lembrete personalizadas sobre eventos ou compromissos futuros."
---

# Mensagens de lembrete selecionadas pelo usuário

> Use [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/), atributos personalizados e campanhas da Braze para permitir que os usuários escolham quando desejam receber mensagens de lembrete sobre eventos ou compromissos futuros. Essa abordagem permite que usuários não técnicos da Braze criem e editem o conteúdo das páginas de inscrição para lembretes, enquanto as preferências selecionadas pelos usuários podem orientar a segmentação, o direcionamento e a personalização em todo o envio de mensagens da Braze.

Com essa abordagem, você pode:

- Permitir que os usuários selecionem a data da mensagem de lembrete em relação a um evento futuro.
- Capturar preferências diretamente dos usuários usando uma landing page da Braze e gravá-las nos perfis de usuário — sem necessidade de backend adicional.
- Enviar mensagens nas datas escolhidas pelos usuários, para que o envio de mensagens permaneça relevante e baseado em permissão.
- Expandir o caso de uso com recursos adicionais da Braze, como postergação de mensagens, redirecionamento de acompanhamento e Testes A/B.

## Pré-requisitos

Para concluir este guia, você precisa de:

| Requisito | Descrição |
| --- | --- |
| Acesso a landing pages | Acesso e permissões para criar [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) na Braze. |
| Conhecimento de HTML e JavaScript | Familiaridade básica com HTML e JavaScript para personalizar sua landing page. Necessário apenas para a [Opção B](#option-b-personal-dates-custom-code-block). |
| Conhecimento de Liquid | Familiaridade básica com [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para criar templates de variáveis personalizadas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 1: Criar uma landing page e vinculá-la a uma mensagem

Primeiro, [crie uma landing page da Braze]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/). Em seguida, crie uma mensagem (como um e-mail) que direcione os usuários para a landing page.

{% raw %}
Para associar automaticamente a atividade da landing page ao perfil de usuário do destinatário, use a Liquid tag `{% landing_page_url %}` ao vincular à página a partir de uma mensagem da Braze. Por exemplo:

```html
<a href="{% landing_page_url your-page-url-handle %}">Sign up for reminders</a>
```
{% endraw %}

Quando um usuário clica nesse link, a Braze o identifica automaticamente, de modo que quaisquer preferências enviadas são gravadas no perfil existente — sem necessidade de parâmetros de URL manuais. Para um passo a passo completo, consulte [Rastrear usuários por meio de um formulário]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/).

## Etapa 2: Capturar preferências na landing page

A forma como você captura as preferências dos usuários depende de estar coletando datas compartilhadas ou datas pessoais. Escolha a opção que se encaixa no seu caso de uso.

### Opção A: Datas compartilhadas (blocos de formulário de arrastar e soltar)

Para eventos em que muitos usuários compartilham a mesma data (como feriados ou eventos esportivos), use os [blocos de formulário **Checkbox**]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks) integrados do editor de arrastar e soltar para capturar preferências. Cada checkbox define nativamente um atributo personalizado booleano (`true` ou `false`) no perfil do usuário quando o formulário é enviado — sem necessidade de código personalizado.

Por exemplo, adicione um checkbox com o rótulo "Lembrete do Super Bowl 2026" que mapeia para o atributo personalizado `super_bowl_2026_reminder`. Quando um usuário marca a caixa e envia o formulário, a Braze define:

```
super_bowl_2026_reminder = true
```

Esses atributos booleanos podem então ser usados diretamente em [filtros de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) para construir seu público-alvo.

### Opção B: Datas pessoais (bloco de código personalizado)

Para datas únicas de cada usuário (como aniversários), use um [bloco de **Código Personalizado**]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#basic-blocks) na sua landing page para capturar a data e gravá-la na Braze usando a API `lpBridge`. Essa abordagem oferece uma entrada de data (ou seletor) e permite armazenar preferências em um [array de objetos de atributo personalizado aninhado]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/array_of_objects/), que os blocos de formulário de arrastar e soltar não suportam.

Quando os usuários chegam por meio da Liquid tag {% raw %}`{% landing_page_url %}`{% endraw %}, a Braze já sabe quem eles são, então seu script só precisa:

1. Escutar o clique no botão de envio do formulário.
2. Ler o valor da data da sua entrada personalizada.
3. Usar a API `lpBridge` para definir atributos personalizados aninhados e enviar os dados para a Braze.

Armazene essas preferências usando um array de objetos de atributo personalizado aninhado. Essa estrutura permite armazenar múltiplos lembretes por usuário e adicionar campos derivados posteriormente, como `next_reminder_name` ou `last_reminder_date`.

#### Exemplo de script

O exemplo de script a seguir desabilita o comportamento padrão do botão e executa métodos personalizados ao clicar no botão. Substitua os IDs dos elementos e os valores dos atributos pelos seus próprios.

```html
<script async="true">
  // Set IDs (as found by inspecting your landing page preview) and success message
  const registerButtonId = "YOUR_BUTTON_ID";
  const messageDivId = "YOUR_MESSAGE_DIV_ID";
  const successMessage = "You're all set! We'll send your reminder.";

  // Wait for page content to load
  document.addEventListener("DOMContentLoaded", () => {
    // Remove the default redirect event from the Braze Message Handler Script
    props[registerButtonId].onclickContract[0].brazeEvents =
      props[registerButtonId].onclickContract[0].brazeEvents.filter(
        (event) => event.eventType !== "REDIRECT"
      );

    const registerButton = document.getElementById(registerButtonId);
    if (registerButton) {
      registerButton.addEventListener("click", async (event) => {
        event.preventDefault();

        // Set the custom attribute (replace with your actual key/value)
        await window.lpBridge.setCustomUserAttribute("key", "value");

        // Flush data to Braze
        await window.lpBridge.requestImmediateDataFlush();

        // Remove the button and update the message
        registerButton.remove();
        const messageDiv = document.getElementById(messageDivId);
        if (messageDiv) {
          messageDiv.innerHTML = successMessage;
        }
      });
    }
  });
</script>
```

Para encontrar os IDs dos elementos dos componentes da sua landing page, visualize a prévia da página, clique com o botão direito e selecione **Inspecionar** no seu navegador. Localize os IDs do botão e dos componentes de mensagem no HTML.

## Etapa 3: Configurar e disparar mensagens de lembrete

Após coletar atributos personalizados por meio da landing page, crie campanhas para enviar mensagens aos usuários sobre eventos futuros.

### Opção A: Datas compartilhadas {#step-3-option-a-shared-dates}

Se você usou atributos personalizados booleanos (Opção A na [Etapa 2](#option-a-shared-dates-dnd-form-blocks)), use esse atributo como filtro de segmento para construir o público da sua mensagem de lembrete. Em seguida, crie uma nova campanha, agendada antes do evento, para direcionar esse grupo com o conteúdo escolhido.

### Opção B: Datas pessoais {#step-3-option-b-personal-dates}

Se você usou atributos personalizados aninhados (Opção B na [Etapa 2](#option-b-personal-dates-custom-code-block)), use o filtro de público **Atributo Personalizado Aninhado** para selecionar todos os usuários que têm uma data de lembrete em um período específico — por exemplo, daqui a dois dias.

Para enviar lembretes de forma contínua, configure uma campanha recorrente diária para que, a cada dia, os usuários com lembretes futuros dentro do seu período recebam suas mensagens.

## Etapa 4: Verificar sua integração

Após concluir a configuração, verifique sua integração:

1. Envie para si mesmo um link para a landing page e preencha o formulário.
2. Navegue até o seu perfil de usuário no dashboard da Braze e confirme que o atributo personalizado aparece.
3. Envie uma mensagem de lembrete de teste para o seu perfil e verifique se os detalhes personalizados são renderizados corretamente.
4. Monitore os resultados de perto ao lançar sua campanha.

## Considerações

- Para um exemplo detalhado de como enviar mensagens com base em atributos personalizados baseados em data, consulte o caso de uso de e-mail no [guia de envio de mensagens da API REST]({{site.baseurl}}/developer_guide/rest_api/messaging/).
- Se você duplicar uma landing page ou substituir quaisquer campos, os IDs dos componentes mudam. Atualize seu bloco de código personalizado para refletir os novos IDs.
- Atributos personalizados aninhados consomem [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) para cada chave no array de objetos. Atualizar um objeto de atributo personalizado para null também consome um ponto de dados.
- O código apresentado neste guia é um exemplo ilustrativo. Teste completamente todo o código e os componentes no seu ambiente antes de implantar em produção.