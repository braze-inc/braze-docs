---
nav_title: Testes
article_title: Teste de mensagens no app
page_order: 4.5
description: "Este artigo de referência explica o valor de testar suas mensagens no app, como testá-las, bem como uma lista de verificação de itens a serem considerados antes do envio."
channel:
  - in-app messages
  
---

# Teste de mensagens no app

> É extremamente importante sempre testar suas mensagens no app antes de enviar suas campanhas. Nossos recursos de prévia e teste oferecem duas maneiras de dar uma olhada nas suas mensagens no app. É possível fazer uma prévia da mensagem, para ajudá-lo a visualizar enquanto a cria, bem como enviar uma mensagem de teste para o seu dispositivo ou para o de um usuário específico. Recomendamos que você tire proveito de ambos.

## Prévia

Você pode fazer uma prévia da sua mensagem no app enquanto a cria. Isso deve ajudá-lo a visualizar como será a mensagem final do ponto de vista do usuário.

{% alert warning %}
Na **Prévia**, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Sempre recomendamos o envio de uma mensagem de teste para um dispositivo para garantir que a mídia, o texto, a personalização e os atributos personalizados sejam gerados corretamente.
{% endalert %}

### Prévia da geração de mensagens no app

Faça uma prévia de como sua mensagem será exibida para um usuário aleatório, um usuário específico ou um usuário personalizado - os dois últimos são especialmente úteis se sua mensagem contiver personalização ou vários idiomas. Também é possível fazer uma prévia das mensagens em dispositivos móveis ou tablets para ter uma ideia melhor da experiência dos usuários.

![Guia "Criar" ao criar uma mensagem no app mostrando a prévia de como será a mensagem. Um usuário não é selecionado, portanto, o Liquid adicionado na seção do corpo é exibido como está.]({%image_buster /assets/img/in-app-message-preview.png %})

O Braze tem três gerações de mensagens no app disponíveis. Você pode ajustar para quais dispositivos suas mensagens devem ser enviadas, com base na geração que eles suportam.

![Alternância entre gerações ao visualizar uma mensagem no app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## Testar

{% alert warning %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve ser ativado nos dispositivos de teste antes do envio. <br><br>Por exemplo, é necessário ter o push ativado em seu dispositivo iOS para tocar na notificação antes da exibição da mensagem de teste.
{% endalert %}

### Ver prévia de mensagem como usuário

Também é possível fazer a prévia das mensagens na guia **Teste**, como se fosse um usuário. Você pode selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado.

![Guia Teste ao criar uma mensagem no app. "Preview message as user" (Visualizar mensagem como usuário) está definido como "Custom User" (Usuário personalizado), com os campos de perfil disponíveis aparecendo como opções configuráveis.]({% image_buster /assets/img/iam-user-preview.png %})

### Lista de verificação de teste

- As imagens e a mídia aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atribuição padrão]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) no caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus botões direcionam o usuário para onde ele deve acessar?

## Scanner de acessibilidade

Para dar suporte às práticas recomendadas de acessibilidade, o Braze verifica automaticamente o conteúdo das mensagens no app criadas usando o editor de HTML tradicional em relação aos padrões de acessibilidade. Esse scanner ajuda a identificar o conteúdo que pode não atender aos padrões[das WCAG (](https://www.w3.org/WAI/standards-guidelines/wcag/)Web Content Accessibility Guidelines). As WCAG são um conjunto de padrões técnicos reconhecidos internacionalmente e desenvolvidos pelo World Wide Web Consortium (W3C) para tornar o conteúdo da Web mais acessível a pessoas com deficiências.

![Resultados da varredura de acessibilidade]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
O scanner de acessibilidade de mensagens no app só funciona em mensagens criadas com HTML personalizado.
{% endalert %}

### Como funciona?

O scanner é executado automaticamente em mensagens HTML personalizadas e avalia toda a sua mensagem HTML em relação ao [conjunto](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) completo [de regras WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada problema sinalizado, ele mostra:

- O elemento HTML específico envolvido
- Uma descrição do problema de acessibilidade
- Um link para contexto adicional ou orientação de correção

### Compreensão dos testes automatizados de acessibilidade

{% multi_lang_include accessibility/automated_testing.md %}





