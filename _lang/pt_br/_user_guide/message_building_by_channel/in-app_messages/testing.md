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

![Guia "Criar" ao criar uma mensagem no app mostrando a prévia de como será a mensagem. Um usuário não é selecionado, portanto, o Liquid adicionado na seção do corpo é exibido como está.][1]

O Braze tem três gerações de mensagens no app disponíveis. Você pode ajustar para quais dispositivos suas mensagens devem ser enviadas, com base na geração que eles suportam.

![Alternância entre gerações ao visualizar uma mensagem no app.][2]{: height="50%" width="50%"}

## Testar

{% alert warning %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve ser ativado nos dispositivos de teste antes do envio. <br><br>Por exemplo, é necessário ter o push ativado em seu dispositivo iOS para tocar na notificação antes da exibição da mensagem de teste.
{% endalert %}

### Ver prévia de mensagem como usuário

Também é possível fazer a prévia das mensagens na guia **Teste**, como se fosse um usuário. Você pode selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado.

![Guia Teste ao criar uma mensagem no app. A opção "Pré-visualizar mensagem como usuário" está definida como "Usuário personalizado", com os campos de perfil disponíveis aparecendo como opções configuráveis.][3]

### Lista de verificação de teste

- As imagens e a mídia aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atribuição padrão]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) no caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus botões direcionam o usuário para onde ele deve acessar?

[1]: {%image_buster /assets/img/in-app-message-preview.png %}
[2]: {% image_buster /assets/img/iam-generations.gif %}
[3]: {% image_buster /assets/img/iam-user-preview.png %}
