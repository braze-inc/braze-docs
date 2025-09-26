---
nav_title: Cancelamento de inscrição impreciso
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

![Bate-papo de mensagens do iOS que mostra mensagens de aceitação de saída em resposta à aceitação difusa de entrada "Please stopppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Os usuários que enviam SMS, MMS e RCS com o Braze devem aderir às leis, aos regulamentos e aos padrões do setor aplicáveis que forem definidos. Para cancelar, as leis determinam que quando um usuário envia uma mensagem de texto com a palavra "STOP", todas as mensagens subsequentes relacionadas a esse programa de envio de mensagens serão interrompidas. Braze processa automaticamente essas mensagens e cancela a inscrição do usuário.<br><br>O cancelamento de inscrição impreciso em SMS tenta reconhecer quando uma mensagem SMS de entrada não corresponde [a uma palavra-chave de cancelamento de inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), mas indica a intenção de cancelamento. Se a capacitação de fuzzy opt-out estiver ativada e uma resposta de palavra-chave de entrada for considerada "fuzzy", o Braze responderá automaticamente com uma mensagem de resposta que instrui os usuários a fazer a aceitação.

Atualmente, apenas palavras-chave de exclusão criadas usando o inglês como [idioma local]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) são suportadas.

## O que é considerado impreciso?

Os critérios para que uma resposta de entrada seja considerada "imprecisa" são os seguintes:
- Se trocar uma letra pela letra à esquerda ou à direita dela em um teclado QWERTY resultar em uma palavra-chave de exclusão correspondente.
- Uma substring da mensagem corresponde a uma palavra-chave de exclusão.

Por exemplo, "Stpo" ou "Por favor, pareee" serão considerados imprecisos, e uma resposta de exclusão imprecisa será enviada. Se o usuário responder com uma palavra-chave de aceitação, um evento de gatilho de cancelamento de inscrição será disparado.

## Configurar exclusão fuzzy

Para configurar a exclusão aproximada, navegue até a página de gerenciamento de palavras-chave do grupo de inscrições.

1. Acesse **Público** > **Inscrições** e selecione um **SMS/MMS/RCS** grupo de inscrições.

{:start="2"}
2\. Em **Global Keywords**, encontre a categoria de **aceitação** e selecione o ícone de lápis.
3\. Ativar **Cancelamento de inscrição impreciso** no botão.
4\. Modifique a resposta conforme desejar. 

![]({% image_buster /assets/img/sms/fuzzy2.png %}){: style="max-width:70%;"}


