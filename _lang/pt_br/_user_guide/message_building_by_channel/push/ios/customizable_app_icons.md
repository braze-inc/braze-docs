---
nav_title: "Recurso de ícone de aplicativo personalizado (iOS)"
article_title: Recurso de ícone de aplicativo personalizado
page_order: 7
page_type: reference
description: "Este artigo de referência aborda a atualização do iOS 10.3 sobre o ícone personalizável do app."
platform: iOS
channel:
  - push

---

# Recurso de ícone de aplicativo personalizado (iOS 10.3) 

> Com o iOS 10.3, a Apple introduziu a capacidade de alterar o ícone da tela inicial de um aplicativo sem precisar atualizar o aplicativo na Apple App Store. O desenvolvedor agora pode permitir que o usuário altere o ícone da tela inicial dentro de seu app. A Apple exige que todas as imagens de ícones de aplicativos que o desenvolvedor deseja disponibilizar para o usuário sejam incluídas no binário enviado à Apple para revisão durante a publicação do app na Apple App Store.

Para notificar seus usuários sobre esse recurso, é possível enviar uma mensagem no app ou uma notificação por push por meio do Braze para o usuário, explicando essa funcionalidade ou perguntando se ele gostaria de alterar seu ícone. O desenvolvedor só precisaria criar um deep link no aplicativo, onde o prompt nativo do iOS pode ser mostrado para fazer a alteração do ícone. Isso é semelhante à mesma orientação que fornecemos hoje sobre a configuração de uma cartilha de notificações por push para APNs.

Além disso, esse envio de mensagens pode tirar o máximo proveito do segmento de mensagens para tornar o texto da mensagem altamente contextual para um usuário. Você também pode aproveitar os Testes A/B das mensagens para ver quais mensagens causam o maior impacto no resultado desejado.
