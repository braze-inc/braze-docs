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

Recomendamos importar números de telefone no formato [`E.164`](https://en.wikipedia.org/wiki/e.164) para garantir precisão no caso de você estar enviando para várias regiões com diferentes códigos de país ou de área—mesmo para números de telefone baseados em U.S.

- **Exemplos de números:** Todos os números de U.S. devem ser números de telefone válidos, com 10 dígitos e um código de área válido. Se algum número de telefone de 10 dígitos estiver faltando um `+` e o código do país, a Braze o mapeará como U.S. números.
- **Números internacionais:** Todos os números internacionais devem começar com um `+`, seguido pelo código do país e, em seguida, o número de telefone. Por exemplo, `+442071838750`.

![Exemplo de um número de telefone internacional e164 válido.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Aqui estão alguns exemplos mostrando as diferenças entre o formato local e `E.164`:

| País | Local | Código do país | `E.164` |
|---|---|---|---|
| EUA | `4155552671` | 1 | `+14155552671` |
| REINO UNIDO | `2071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

## Importação de números telefônicos

Ao importar números de telefone, é importante que você siga o [formato recomendado](#recommended-format). Para importar números de telefone, use um dos seguintes métodos:

- [Carregando um CSV para a Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)
- [Usando o endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Os números de telefone dos usuários são exibidos na Braze como uma sequência de dígitos. Se você importar um número que contenha qualquer não-dígito (como `,`, `-`, `(` ou outros), os não-dígitos serão removidos quando renderizados na Braze. Por exemplo, a importação de `+1 (724) 123-4567` será exibida como `17241234567`.
{% endalert %}

## Tratamento de números de telefone inválidos

Quando um número de telefone for considerado inválido, a Braze marcará o número de telefone do usuário como inválido e não tentará enviar mais comunicações para esse número de telefone. Um número de telefone inválido é marcado na **guia Engajamento** de um perfil de usuário.

![Exemplo de mensagem de erro para números de telefone inválidos na Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Um número de telefone é considerado inválido pelos seguintes motivos:

- **Erro do Provedor**: um erro permanente foi recebido do provedor de SMS e RCS. Isso indica que o número de telefone fornecido está formatado incorretamente ou permanentemente incapaz de receber mensagens SMS ou RCS.
- **Desativado**: o número de telefone foi desativado porque um assinante móvel encerrou seu serviço e liberou seu número da operadora (e pode eventualmente ser reciclado e atribuído a um novo usuário).

Esses números de telefone inválidos podem ser gerenciados usando [endpoints de SMS e RCS]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
Se vários perfis de usuário tiverem o mesmo número de telefone e esse número de telefone for marcado como inválido, todos os perfis de usuário existentes com esse número serão exibidos como inválidos. Os perfis de usuário recém-criados nunca serão inicialmente marcados como inválidos.
{% endalert %}

Você também pode incluir ou excluir qualquer usuário com números de telefone inválidos ao [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

## Adicionando usuários a grupos de inscrição de SMS e RCS

Para que um usuário receba uma mensagem SMS ou RCS, ele deve ter um número de telefone válido e estar inscrito em um grupo de inscrição. Os grupos de inscrição estão vinculados ao programa SMS ou RCS que você está executando (certifique-se de seguir os [requisitos legais para SMS, MMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) e ter o consentimento registrado de cada cliente). Para saber mais, consulte [grupos de inscrição SMS e RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

## Fornecimento e verificação por terceiros

A Braze depende de ferramentas de terceiros para obter números inválidos. A Braze não se responsabiliza por quaisquer interrupções ou informações errôneas sobre esses serviços. Portanto, não se deve confiar nessa ferramenta como seu único método de conformidade para verificar números inválidos.
