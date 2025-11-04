---
nav_title: Cancelamento difuso
article_title: Opção de exclusão difusa
description: "Este artigo de referência aborda como configurar o opt-out difuso, uma configuração que tenta reconhecer quando uma mensagem de entrada não corresponde a uma palavra-chave de opt-out."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 1

---

# Cancelamento difuso

\![bate-papo de mensagem do iOS que mostra mensagens de opt-out de saída em resposta ao opt-out difuso de entrada "Please stopppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Os usuários que enviam SMS, MMS e RCS com o Braze devem aderir às leis, aos regulamentos e aos padrões do setor aplicáveis que forem definidos. Para a exclusão, as leis determinam que, quando um usuário envia a mensagem "STOP", todas as mensagens subsequentes relacionadas a esse programa de mensagens serão interrompidas. A Braze processa automaticamente essas mensagens e cancela a inscrição do usuário.<br><br>O opt-out difuso tenta reconhecer quando uma mensagem de entrada não corresponde a uma [palavra-chave de opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), mas indica a intenção de opt-out. Se o opt-out difuso estiver ativado e uma resposta de palavra-chave de entrada for considerada "difusa", o Braze responderá automaticamente com uma mensagem de resposta que instrui os usuários a optarem pelo opt-out.

Atualmente, somente as palavras-chave de exclusão criadas usando o inglês como [idioma local]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) são suportadas.

## O que é considerado difuso?

Os critérios para que uma resposta de entrada seja considerada "difusa" são os seguintes:
- Se a troca de uma letra com a letra um à esquerda ou à direita dela em uma palavra-chave QWERTY gerar uma palavra-chave opt-out correspondente.
- Uma substring da mensagem corresponde a uma palavra-chave de exclusão.

Por exemplo, "Stpo" ou "Please stopppp" serão considerados difusos, e uma resposta difusa de recusa será enviada. Se o usuário responder com uma palavra-chave de cancelamento, um evento de cancelamento de assinatura será acionado.

## Configurar o opt-out difuso

Para configurar o opt-out difuso, navegue até a página de gerenciamento de palavras-chave do grupo de assinaturas.

1. Vá para **Audience** > **Subscription Group Management (** **Público** > **Gerenciamento de grupos de** assinatura) e selecione um grupo de assinatura de **SMS/MMS/RCS**.
2. Em **Global Keywords**, localize a categoria **opt-out** e selecione o ícone de lápis.
3. Habilite **o Fuzzy Opt-Out** ativando-o.
4. Modifique a resposta fuzzy opt-out conforme desejado. 

\![Seção para editar palavras-chave de exclusão.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Práticas recomendadas para mensagens de opt-out difusas

Para garantir uma experiência clara, compatível e positiva para seus assinantes, é fundamental configurar cuidadosamente sua mensagem de opt-out difusa. O principal objetivo da mensagem de opt-out difusa é **orientar os usuários que enviam uma mensagem semelhante, mas não exatamente, à sua palavra-chave de opt-out designada**. A mensagem solicita que os usuários saibam como cancelar a assinatura com êxito.

### Considerações críticas

{% alert warning %}
**NÃO** configure sua mensagem de opt-out difusa para confirmar o cancelamento da assinatura. Sua mensagem de opt-out difusa não deve conter linguagem que implique que o usuário já cancelou a assinatura com sucesso. Por exemplo, **não** use "Sua inscrição foi cancelada", "Você não receberá mais mensagens deste número" ou "Você está excluído".
{% endalert %}

A mensagem fuzzy opt-out é enviada antes que o usuário tenha feito o opt-out com sucesso. O uso da linguagem de confirmação induz o assinante a acreditar que cancelou a assinatura quando não o fez, levando à continuidade de mensagens indesejadas, à frustração do assinante e a riscos significativos de conformidade.

{% alert warning %}
**NÃO** configure sua mensagem de opt-out difusa para ser idêntica ou semelhante à sua palavra-chave exata de opt-out.
{% endalert %}

Se a sua mensagem difusa for igual ou muito próxima da palavra-chave exata de cancelamento (por exemplo, se "STOP" for a palavra-chave exata e a mensagem difusa for "Text STOP to unsubscribe"), isso pode gerar confusão sobre se a mensagem inicial do usuário realmente resultou em um cancelamento de assinatura ou se ele precisa realizar outra ação. A mensagem difusa deve sempre esclarecer a ação que o usuário precisa realizar.

### Exemplos de mensagens de opt-out difusas

Concentre-se em orientar os usuários. Por exemplo, se sua palavra-chave de opt-out for "STOP", esses são exemplos bons e ruins de mensagens de opt-out difusas que você poderia criar:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Exemplos ruins <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Para cancelar a assinatura de todas as mensagens, responda com a palavra STOP."</td>
      <td>"Sua inscrição foi cancelada com sucesso. Você não receberá mais mensagens desse número. Reply START to resubscribe." (Essa é uma confirmação direta do cancelamento da assinatura, o que é enganoso em um cenário de opt-out difuso).</td>
    </tr>
    <tr>
      <td>"Recebemos sua mensagem. Se você quiser parar de receber mensagens de texto, envie uma mensagem de texto para STOP."</td>
      <td>"STOP." (Essa é apenas a palavra-chave exata em si, que não orienta o usuário).</td>
    </tr>
    <tr>
      <td>"Você queria cancelar a assinatura? Responda STOP para cancelar o recebimento de todas as mensagens futuras."</td>
      <td>"(Se "STOP" também for sua palavra-chave exata, isso é redundante e não esclarece a ação se a mensagem inicial for confusa).</td>
    </tr>
  </tbody>
</table>
