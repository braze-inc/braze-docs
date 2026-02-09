---
nav_title: Envio de mensagens por canal
article_title: Envio de mensagens por canal
page_order: 5
layout: dev_guide

guide_top_header: "Envio de mensagens por canal"
guide_top_text: "Os canais de envio de mensagens são maneiras de se comunicar virtualmente com seus clientes por meio de notificações por push no telefone ou no navegador da Web, e-mail, mensagens no app e muito mais! Se quiser saber mais sobre esses canais e como utilizá-los com o Braze, consulte as seções listadas a seguir. Ou confira nossos cursos do Braze Learning sobre <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>canais de envio de mensagens</a>!<br><br>Você pode usar o Braze para criar campanhas de envio de mensagens acessíveis em cada canal. Trabalhe com seus engenheiros para garantir que você atenda aos padrões de acessibilidade em sua implementação."
description: "Esta landing page abrange os canais de envio de mensagens da Braze. Os canais de envio de mensagens são maneiras de se comunicar virtualmente com seus clientes por meio de notificações por push no telefone ou no navegador da Web, e-mail, mensagens no app e muito mais!"

guide_featured_title: "Canais disponíveis"
guide_featured_list:
- name: Banners
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Cartões de conteúdo
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: Envio de mensagens por e-mail
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "Mensagem no app"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: Mensagens por push
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

Você pode usar o Braze para criar campanhas de envio de mensagens acessíveis em cada canal. Trabalhe com seus engenheiros para garantir que você atenda aos padrões de acessibilidade em sua implementação. Se você quiser obter orientação adicional, recomendamos:

- [Fundamentos do envio de mensagens acessíveis](https://learning.braze.com/accessible-messaging-foundations): Aprenda os princípios fundamentais de acessibilidade que se aplicam às comunicações da marca neste curso do Braze Learning.
- [Criação de envios de mensagens acessíveis]({{site.baseurl}}/help/accessibility/): Saiba como adicionar texto alternativo e estruturar seu conteúdo para tecnologias assistivas diretamente no Braze.

{% multi_lang_include accessibility/feedback.md %}

## Escolha de um canal de envio de mensagens

Ao determinar qual canal de envio de mensagens é melhor para suas campanhas e Canvas, pense sempre no conteúdo e na urgência de sua mensagem:

- **O conteúdo** é o engajamento visual de sua mensagem. É possível adicionar multimídia e outros ativos ao seu texto para tornar seu conteúdo mais rico.
- **A urgência** é uma medida da rapidez com que uma mensagem é capaz de notificar o usuário e atrair sua atenção. As notificações que o usuário pode visualizar imediatamente têm uma alta urgência, enquanto as mensagens que precisam que o usuário registre no app têm uma baixa urgência.

A Matriz Braze de Envio de Mensagens simplifica a seleção de canais mapeando **a Complexidade do Conteúdo** em relação à **Urgência de Entrega**. Ao equilibrar esses dois fatores, você pode ajudar sua mensagem a repercutir em vez de interromper.

![Mensagens no mobile e na web são de conteúdo simples e de alta urgência; e-mails são de conteúdo rico e de alta urgência; mensagens no app e no navegador são de conteúdo simples e de baixa urgência; cartões de conteúdo são de baixa urgência e de conteúdo rico]({% image_buster /assets/img_archive/messaging_matrix.png %})

Embora a matriz destaque os canais principais, ela é adaptável: O SMS e o WhatsApp, por exemplo, são ferramentas de alta urgência que se transformam em conteúdo rico ao utilizar formatos multimídia. Para saber mais sobre como você pode aproveitar essa matriz, confira nosso curso do Braze Learning sobre [envio de mensagens entre canais](https://learning.braze.com/cross-channel-messaging).

<br><br>
