---
nav_title: Desativação imprecisa
article_title: Cancelamento de inscrição impreciso
description: "Este artigo de referência cobre como configurar a exclusão fuzzy, uma configuração que tenta reconhecer quando uma mensagem recebida não corresponde a uma palavra-chave de exclusão."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 1

---

# Desativação imprecisa

![chat de mensagens iOS que mostra mensagens de opt-out de saída em resposta à mensagem de opt-out difusa recebida "Por favor, pareee".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Os usuários que enviam SMS, MMS e RCS com Braze devem aderir às leis, regulamentos e padrões da indústria aplicáveis que estão definidos. Para cancelar, as leis determinam que quando um usuário envia uma mensagem de texto com a palavra "STOP", todas as mensagens subsequentes relacionadas a esse programa de envio de mensagens serão interrompidas. Braze processa automaticamente essas mensagens e cancela a inscrição do usuário.<br><br>O cancelamento de inscrição impreciso em SMS tenta reconhecer quando uma mensagem SMS de entrada não corresponde [a uma palavra-chave de cancelamento de inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), mas indica a intenção de cancelamento. Se o opt-out difuso estiver habilitado e uma resposta de palavra-chave recebida for considerada "difusa", o Braze responderá automaticamente com uma mensagem de resposta que instrui os usuários a optarem por sair.

Atualmente, apenas palavras-chave de exclusão criadas usando o inglês como [idioma local]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) são suportadas.

## O que é considerado impreciso?

Os critérios para que uma resposta de entrada seja considerada "imprecisa" são os seguintes:
- Se trocar uma letra pela letra à esquerda ou à direita dela em um teclado QWERTY resultar em uma palavra-chave de exclusão correspondente.
- Uma substring da mensagem corresponde a uma palavra-chave de exclusão.

Por exemplo, "Stpo" ou "Por favor, pareee" serão considerados imprecisos, e uma resposta de exclusão imprecisa será enviada. Se o usuário então responder com uma palavra-chave de opt-out, um evento de cancelamento de inscrição será disparado.

## Configurar exclusão fuzzy

Para configurar a exclusão aproximada, navegue até a página de gerenciamento de palavras-chave do grupo de inscrições.

1. Acesse **público** > **Gerenciamento de Grupo de Inscrições** e selecione um **grupo de inscrições SMS/MMS/RCS**.
2. Em **Palavras-chave Globais**, encontre a categoria **opt-out** e selecione o ícone de lápis.
3. Ativar **Cancelamento de inscrição impreciso** no botão.
4. Modifique a resposta conforme desejar. 

![Seção para editar palavras-chave de opt-out.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Melhores práticas para mensagens de opt-out difusas

Para garantir uma experiência clara, em conformidade e positiva para seus assinantes, é crucial configurar sua mensagem de opt-out difusa de forma cuidadosa. O principal objetivo da mensagem de opt-out difusa é **guiar os usuários que enviam uma mensagem semelhante, mas não exatamente, à sua palavra-chave de opt-out designada**. A mensagem orienta os usuários sobre como cancelar a inscrição com sucesso.

### Considerações críticas

{% alert warning %}
**NÃO** configure sua mensagem de opt-out difusa para confirmar um cancelamento de inscrição. Sua mensagem de opt-out difusa não deve conter linguagem que implique que um usuário já cancelou a inscrição com sucesso. Por exemplo, **não** use "Você foi cancelado", "Você não receberá mais mensagens deste número" ou "Você agora está optado por sair".
{% endalert %}

A mensagem de opt-out difusa é enviada antes que o usuário tenha cancelado a inscrição com sucesso. Usar linguagem de confirmação engana o assinante, fazendo-o acreditar que está cancelado quando não está, levando a mensagens indesejadas contínuas, frustração do assinante e riscos significativos de conformidade.

{% alert warning %}
**NÃO** configure sua mensagem de opt-out difusa para ser idêntica ou semelhante à sua palavra-chave de opt-out exata.
{% endalert %}

Se sua mensagem difusa for a mesma ou muito próxima da sua palavra-chave de opt-out exata (por exemplo, se "PARAR" for sua palavra-chave exata e sua mensagem difusa for "Envie PARAR para cancelar a inscrição"), isso pode criar confusão sobre se a mensagem inicial do usuário realmente resultou em um cancelamento de inscrição ou se eles precisam tomar outra ação. A mensagem difusa deve sempre esclarecer qual ação o usuário precisa tomar.

### Exemplos de mensagens de opt-out difusas

Concentre-se em guiar os usuários. Por exemplo, se sua palavra-chave de opt-out for "PARAR", estes são bons e maus exemplos de mensagens de opt-out difusas que você poderia criar:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Maus exemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Para cancelar a inscrição de todas as mensagens, por favor, responda com a palavra PARAR."</td>
      <td>"Você foi cancelado com sucesso." Você não receberá mais mensagens deste número. Responda INICIAR para se reinscrever." (Esta é uma confirmação direta de cancelamento, o que é enganoso em um cenário de opt-out difuso.)</td>
    </tr>
    <tr>
      <td>"Recebemos sua mensagem. Se você gostaria de parar de receber mensagens, por favor, envie PARAR."</td>
      <td>"PARAR." (Esta é apenas a palavra-chave exata, que não orienta o usuário.)</td>
    </tr>
    <tr>
      <td>"Você quis cancelar a inscrição? Responda PARAR para optar por não receber mais mensagens."</td>
      <td>"Envie PARAR para cancelar a inscrição." (Se "PARAR" também for sua palavra-chave exata, isso é redundante e não esclarece a ação se a mensagem inicial foi difusa.)</td>
    </tr>
  </tbody>
</table>
