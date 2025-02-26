---
nav_title: "Números de telefone do usuário"
article_title: Números de telefone do usuário de SMS
page_order: 1
description: "Este artigo de referência aborda a formatação de números de telefone SMS, como importar números de telefone e como adicionar usuários a grupos de inscrições de SMS."
page_type: reference
channel: 
  - SMS
  
---

# Números de telefone do usuário

> Este artigo discutirá diferentes tópicos relacionados aos números de telefone dos seus usuários ou clientes. Se estiver procurando informações sobre seus próprios números, acesse nosso artigo sobre o [envio de números de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).

Os números de telefone são mostrados no perfil do usuário como uma string de dígitos. Se você importar um número que contenha não dígitos (como `,`, `-`, `(` ou outros), os não dígitos serão removidos. Por exemplo, a importação de `+1 (724) 123-4567` será exibida como `17241234567`.

## Importação de números telefônicos

É possível importar números de telefone fazendo upload de um [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) ou via [API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) para criar um usuário.

### Formatação

Como prática recomendada, a melhor maneira de importar um número de telefone é no formato [`E.164`](https://en.wikipedia.org/wiki/e.164). No entanto, o Braze tentará interpretar ou converter qualquer número do U.S. da melhor forma possível.

Todos os números de U.S. devem ser números de telefone válidos, com 10 dígitos e um código de área válido. Eles podem ser inseridos sem o código `+` e o código do país, pois o Braze assumirá e mapeará todos os números telefônicos válidos de 10 dígitos como números U.S.

Todos os números internacionais devem começar com `+`, seguido do código do país e do número de telefone. (e.g `+442071838750`)

![][picture]{: style="max-width:50%;border: 0;"}

No entanto, para garantir a precisão caso esteja enviando para várias regiões com diferentes códigos de país ou de área, é recomendável usar o formato `E.164`, mesmo para números de telefone baseados em U.S.

Você pode ver as diferenças entre a formatação de números na localização e a formatação universal em `E.164` na tabela a seguir:

| País | Local | Código do país | `E.164` |
|---|---|---|---|
| EUA | `4155552671` | 1 | `+14155552671` |
| REINO UNIDO | `2071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Adição de usuários a grupos de inscrições de SMS

Para que um cliente receba uma mensagem SMS, ele deve ter um número de telefone válido e ser aceito em um grupo de inscrições. Os grupos de inscrições estão vinculados ao programa de SMS que você está executando (certifique-se de seguir os [requisitos legais para SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) e de ter registrado o consentimento de cada cliente). Para saber mais, consulte os [grupos de inscrição de SMS][1]. 

### Tratamento de números de telefone inválidos

Quando um número de telefone for considerado inválido, a Braze marcará o número de telefone do usuário como inválido e não tentará enviar mais comunicações para esse número de telefone. Um número de telefone inválido é marcado na **guia Engajamento** de um perfil de usuário.

![][picture2]{: style="max-width:50%;border: 0;"}

Um número de telefone é considerado inválido pelos seguintes motivos:
- **Erro do provedor**: foi recebido um erro permanente do provedor de SMS. Isso indica que o número de telefone fornecido está formatado incorretamente ou permanentemente incapaz de receber mensagens SMS.
- **Desativado**: o número de telefone foi desativado porque um assinante móvel encerrou seu serviço e liberou seu número da operadora (e pode eventualmente ser reciclado e atribuído a um novo usuário).

Esses números de telefone inválidos podem ser gerenciados usando [pontos de extremidade de SMS]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
Se vários perfis de usuário tiverem o mesmo número de telefone e esse número de telefone for marcado como inválido, todos os perfis de usuário existentes com esse número serão exibidos como inválidos. Os perfis de usuário recém-criados nunca serão inicialmente marcados como inválidos.
{% endalert %}

Você também pode incluir ou excluir qualquer usuário com números de telefone inválidos ao [criar um segmento][2]. 

### Fornecimento e verificação por terceiros

A Braze depende de ferramentas de terceiros para obter números inválidos. A Braze não se responsabiliza por quaisquer interrupções ou informações errôneas sobre esses serviços. Portanto, não se deve confiar nessa ferramenta como seu único método de conformidade para verificar números inválidos.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[picture]: {% image_buster /assets/img/sms/e164.png %}
[picture2]: {% image_buster /assets/img/sms/invalid_banner.png %}
