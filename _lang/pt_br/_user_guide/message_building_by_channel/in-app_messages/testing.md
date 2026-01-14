---
nav_title: Testes
article_title: Teste de mensagens no aplicativo
page_order: 4.5
description: "Este artigo de referência explica o valor de testar suas mensagens in-app, como testá-las, bem como uma lista de verificação de itens a serem considerados antes do envio."
channel:
  - in-app messages
  
---

# Teste de mensagens in-app

> É extremamente importante sempre testar suas mensagens in-app antes de enviar suas campanhas. Nossos recursos de visualização e teste oferecem duas maneiras de dar uma olhada nas suas mensagens in-app. Você pode pré-visualizar sua mensagem, para ajudá-lo a visualizar enquanto a compõe, bem como enviar uma mensagem de teste para o seu dispositivo ou para o de um usuário específico. Recomendamos que você tire proveito de ambos.

## Prévia

Você pode visualizar sua mensagem no aplicativo enquanto a escreve. Isso deve ajudá-lo a visualizar como será a mensagem final do ponto de vista do usuário.

{% alert warning %}
No **Preview**, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Sempre recomendamos o envio de uma mensagem de teste a um dispositivo para garantir que a mídia, o texto, a personalização e os atributos personalizados sejam gerados corretamente.
{% endalert %}

### Visualização da geração de mensagens no aplicativo

Visualize a aparência da sua mensagem para um usuário aleatório, um usuário específico ou um usuário personalizado - os dois últimos são especialmente úteis se a sua mensagem contiver personalização ou vários idiomas. Também é possível visualizar as mensagens em dispositivos móveis ou tablets para ter uma ideia melhor da experiência dos usuários.

A guia Compor ao criar uma mensagem no aplicativo mostra a visualização de como será a mensagem. Um usuário não é selecionado, portanto, o Liquid adicionado na seção do corpo é exibido como is.]({%image_buster /assets/img/in-app-message-preview.png %})

O Braze tem três gerações de mensagens no aplicativo disponíveis. Você pode ajustar para quais dispositivos suas mensagens devem ser enviadas, com base na geração que eles suportam.

\![Alternando entre gerações ao visualizar uma mensagem no aplicativo.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## Teste

{% alert warning %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve estar ativado nos dispositivos de teste antes do envio. <br><br>Por exemplo, você deve ter o push ativado em seu dispositivo iOS para poder tocar na notificação antes da exibição da mensagem de teste.
{% endalert %}

### Visualizar mensagem como usuário

Você também pode visualizar mensagens na guia **Teste**, como se fosse um usuário. É possível selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado.

\![Guia Teste ao criar uma mensagem no aplicativo. "Preview message as user" (Visualizar mensagem como usuário) está definido como "Custom User" (Usuário personalizado), com os campos de perfil disponíveis aparecendo como opções configuráveis.]({% image_buster /assets/img/iam-user-preview.png %})

{% alert important %}
Os envios de teste podem resultar no envio de mais de uma mensagem in-app para cada destinatário.
{% endalert %}

### Lista de verificação de teste

- As imagens e a mídia aparecem e funcionam como esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atributo padrão]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) para o caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus botões direcionam o usuário para onde ele deve ir?

## Scanner de acessibilidade

Para dar suporte às práticas recomendadas de acessibilidade, o Braze verifica automaticamente o conteúdo das mensagens no aplicativo criadas usando o editor HTML tradicional em relação aos padrões de acessibilidade. Esse scanner ajuda a identificar o conteúdo que pode não atender aos padrões[das WCAG (](https://www.w3.org/WAI/standards-guidelines/wcag/)Web Content Accessibility Guidelines). As WCAG são um conjunto de padrões técnicos reconhecidos internacionalmente e desenvolvidos pelo World Wide Web Consortium (W3C) para tornar o conteúdo da Web mais acessível a pessoas com deficiências.

\![Resultados da verificação de acessibilidade]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
O verificador de acessibilidade de mensagens no aplicativo só funciona em mensagens criadas com HTML personalizado.
{% endalert %}

### Como funciona

O scanner é executado automaticamente em mensagens HTML personalizadas e avalia toda a sua mensagem HTML em relação ao [conjunto](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) completo [de regras WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada problema sinalizado, ele mostra:

- O elemento HTML específico envolvido
- Uma descrição do problema de acessibilidade
- Um link para contexto adicional ou orientação de correção

### Compreensão dos testes automatizados de acessibilidade

{% multi_lang_include accessibility/automated_testing.md %}





