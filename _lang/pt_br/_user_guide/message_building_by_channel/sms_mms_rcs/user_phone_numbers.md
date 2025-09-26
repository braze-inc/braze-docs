---
nav_title: "Números de telefone do usuário"
article_title: Números de telefone do usuário de SMS
page_order: 7
description: "Este artigo de referência aborda a formatação de números de telefone SMS, como importar números de telefone e como adicionar usuários a grupos de inscrições de SMS."
page_type: reference
alias: /user_phone_numbers/
channel: 
  - SMS
  - MMS
  - RCS
---

# Números de telefone do usuário

> Este artigo discutirá diferentes tópicos relacionados aos números de telefone dos seus usuários ou clientes. Se estiver procurando informações sobre seus próprios números, acesse nosso artigo sobre o [envio de números de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Formato recomendado

Recomendamos a importação de números telefônicos no formato [`E.164`](https://en.wikipedia.org/wiki/e.164) para garantir a precisão, caso esteja enviando para várias regiões com diferentes códigos de país ou de área, mesmo para números de telefone baseados em U.S.

- **U.S. números:** Todos os números de U.S. devem ser números de telefone válidos, com 10 dígitos e um código de área válido. Se qualquer número telefônico de 10 dígitos não tiver o código `+` e o código do país, o Braze o mapeará como números U.S.
- **Números internacionais:** Todos os números internacionais devem começar com `+`, seguido do código do país e do número do telefone. Por exemplo, `+442071838750`.

![Exemplo de um número de telefone internacional e164 válido.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Veja a seguir alguns exemplos que mostram as diferenças entre a formatação local e a formatação do site `E.164`:

| País | Local | Código do país | `E.164` |
|---|---|---|---|
| EUA | `4155552671` | 1 | `+14155552671` |
| REINO UNIDO | `2071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

## Importação de números telefônicos

Ao importar números de telefone, é importante que você siga o [formato recomendado](#recommended-format). Para importar números de telefone, use um dos métodos a seguir:

- [Fazendo upload de um CSV para o Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)
- [Usando o ponto de extremidade `/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Os números de telefone do usuário são exibidos no Braze como uma string de dígitos. Se você importar um número que contenha quaisquer não dígitos (como `,`, `-`, `(`, ou outros), os não dígitos serão removidos quando renderizados no Braze. Por exemplo, a importação de `+1 (724) 123-4567` será exibida como `17241234567`.
{% endalert %}

## Tratamento de números de telefone inválidos

Quando um número de telefone for considerado inválido, a Braze marcará o número de telefone do usuário como inválido e não tentará enviar mais comunicações para esse número de telefone. Um número de telefone inválido é marcado na **guia Engajamento** de um perfil de usuário.

![Exemplo de mensagem de erro para números de telefone inválidos no Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Um número de telefone é considerado inválido pelos seguintes motivos:

- **Erro do provedor**: foi recebido um erro permanente do provedor de SMS e RCS. Isso indica que o número de telefone fornecido está formatado incorretamente ou permanentemente incapaz de receber mensagens SMS ou RCS.
- **Desativado**: o número de telefone foi desativado porque um assinante móvel encerrou seu serviço e liberou seu número da operadora (e pode eventualmente ser reciclado e atribuído a um novo usuário).

Esses números de telefone inválidos podem ser gerenciados usando [endpoints de SMS e RCS]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
Se vários perfis de usuário tiverem o mesmo número de telefone e esse número de telefone for marcado como inválido, todos os perfis de usuário existentes com esse número serão exibidos como inválidos. Os perfis de usuário recém-criados nunca serão inicialmente marcados como inválidos.
{% endalert %}

Você também pode incluir ou excluir qualquer usuário com números de telefone inválidos ao [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

## Adição de usuários a grupos de inscrições de SMS e RCS

Para que um usuário receba uma mensagem SMS ou RCS, ele deve ter um número de telefone válido e ser aceito em um grupo de inscrições. Os grupos de inscrições estão vinculados ao programa de SMS ou RCS que você está executando (certifique-se de seguir os [requisitos legais para SMS, MMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) e de ter registrado o consentimento de cada cliente). Para saber mais, consulte [Grupos de inscrições de SMS e RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

## Fornecimento e verificação por terceiros

A Braze depende de ferramentas de terceiros para obter números inválidos. A Braze não se responsabiliza por quaisquer interrupções ou informações errôneas sobre esses serviços. Portanto, não se deve confiar nessa ferramenta como seu único método de conformidade para verificar números inválidos.
