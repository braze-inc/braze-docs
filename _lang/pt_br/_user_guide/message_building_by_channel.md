---
nav_title: Criação de mensagens por canal
article_title: Criação de mensagens por canal
page_order: 5
layout: dev_guide

guide_top_header: "Criação de mensagens por canal"
guide_top_text: "Os canais de mensagens são maneiras de se comunicar virtualmente com seus clientes por meio de notificações push no telefone ou no navegador da Web, e-mail, mensagens no aplicativo e muito mais! Se quiser saber mais sobre esses canais e como utilizá-los com o Braze, consulte as seções listadas a seguir. Ou confira nossos cursos do Braze Learning sobre <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>canais de mensagens</a>!<br><br>Você pode usar o Braze para criar campanhas de mensagens acessíveis em cada canal. Trabalhe com seus engenheiros para garantir que você atenda aos padrões de acessibilidade em sua implementação."
description: "Esta página de destino abrange os canais de mensagens da Braze. Os canais de mensagens são maneiras de se comunicar virtualmente com seus clientes por meio de notificações push no telefone ou no navegador da Web, e-mail, mensagens no aplicativo e muito mais!"

guide_featured_title: "Canais disponíveis"
guide_featured_list:
- name: Banners
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Cartões de conteúdo
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: Mensagens de e-mail
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "Mensagens no aplicativo"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: Mensagens push
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: "SMS, MMS e RCS"
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## Recursos de acessibilidade

Você pode usar o Braze para criar campanhas de mensagens acessíveis em cada canal. Trabalhe com seus engenheiros para garantir que você atenda aos padrões de acessibilidade em sua implementação. Se você quiser obter orientação adicional, recomendamos:

- [Fundamentos de mensagens acessíveis](https://learning.braze.com/accessible-messaging-foundations): Aprenda os princípios fundamentais de acessibilidade que se aplicam às comunicações da marca neste curso do Braze Learning.
- [Criando mensagens acessíveis]({{site.baseurl}}/help/accessibility/): Saiba como adicionar texto alternativo e estruturar seu conteúdo para tecnologias assistivas diretamente no Braze.

{% multi_lang_include accessibility/feedback.md %}

## Escolha de um canal de mensagem

Ao determinar qual canal de mensagem é melhor para suas campanhas e Canvases, sempre pense no conteúdo e na urgência da mensagem:

- **O conteúdo** é o grau de envolvimento visual de sua mensagem. Você pode adicionar multimídia e outros ativos à sua cópia para tornar o conteúdo mais rico.
- **A urgência** é uma medida da rapidez com que uma mensagem é capaz de notificar o usuário e atrair sua atenção. As notificações que o usuário pode visualizar imediatamente têm uma alta urgência, enquanto as mensagens que exigem que o usuário faça login no aplicativo têm uma baixa urgência.

A matriz a seguir ilustra os pontos fortes e fracos dos principais canais de mensagens em termos de conteúdo e urgência. Pense sempre em quão urgente e rica em conteúdo deve ser sua mensagem e, em seguida, escolha o canal certo para sua campanha.

\![Mobile/web push são de conteúdo simples, de alta urgência; e-mails são de conteúdo rico, de alta urgência; mensagens no aplicativo/navegador são de conteúdo simples, de baixa urgência; cartões de conteúdo são de baixa urgência, de conteúdo rico]({% image_buster /assets/img_archive/messaging_matrix.png %})

Para saber mais sobre como você pode aproveitar essa matriz, confira nosso curso do Braze Learning sobre [como entender a matriz de mensagens](https://learning.braze.com/understand-the-messaging-matrix).

<br><br>
