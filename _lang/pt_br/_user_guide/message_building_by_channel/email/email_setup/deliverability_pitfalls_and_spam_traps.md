---
nav_title: Armadilhas de entregabilidade e armadilhas de spam
article_title: Armadilhas de entregabilidade e armadilhas de spam
page_order: 7
page_type: reference
description: "Este artigo de referência aborda as possíveis armadilhas da capacidade de entrega de e-mail, as armadilhas de spam e como evitá-las."
channel: email

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"} Armadilhas da entregabilidade e armadilhas de spam

A capacidade de entrega de seu e-mail pode ser afetada por qualquer uma das seguintes armadilhas de spam:

| Tipo de armadilha | Descrição |
|---|---|
| Armadilhas imaculadas | Endereços de e-mail e domínios que nunca foram usados. |
| Armadilhas recicladas | Endereços de e-mail que originalmente eram usuários reais, mas que agora estão inativos. |
| Armadilhas de erro de digitação | Endereços de e-mail que contêm erros de digitação comuns. |
| Reclamações de spam | Quando seu e-mail é marcado como spam por um cliente. |
| Alta taxa de rejeição | Quando seu e-mail falha constantemente na entrega porque o endereço do destinatário é inválido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Como evitar armadilhas de spam

Essas armadilhas podem ser evitadas se você configurar um processo de opt-in confirmado. Ao enviar um e-mail inicial de opt-in e pedir aos clientes que confirmem que desejam receber suas mensagens, você garante que os destinatários queiram receber notícias suas e que você esteja enviando para endereços reais e válidos. Aqui estão outras maneiras de evitar armadilhas de spam:

1. Envie um e-mail de opt-in duplo. Esse é um e-mail que solicitará que os usuários confirmem suas opções de assinatura clicando em um link.
2. Como prática recomendada, implemente uma [política de expiração]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).
3. **Nunca compre listas de e-mail.** 

{% alert tip %}
As equipes de Sucesso do Cliente e de Capacidade de Entrega da Braze podem ajudar a garantir que você esteja seguindo as práticas recomendadas para maximizar a capacidade de entrega em todo o mundo.
{% endalert %}

## Remoção de um endereço de e-mail de sua lista de devoluções ou de spam

Você pode remover e-mails devolvidos e e-mails da sua lista de spam do Braze com os seguintes pontos de extremidade:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)