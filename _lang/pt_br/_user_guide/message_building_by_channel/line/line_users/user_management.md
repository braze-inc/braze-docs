---
nav_title: Gerenciamento de usuários
article_title: Gerenciamento de usuários do LINE
page_order: 0
description: "Este artigo aborda o ID de usuário do LINE e como defini-lo."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# Gerenciamento de usuários do LINE

> A ID do usuário do LINE é armazenada no atributo do perfil do usuário chamado `native_line_id`, que é usado para enviar mensagens a um usuário no canal LINE. Este artigo aborda como definir e localizar o atributo `native_line_id`.

Os dados de usuário do cliente são representados em um [perfil de usuário Braze]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/). Um perfil de usuário armazena informações e atributos sobre os usuários de uma empresa, como nomes próprios e endereços de e-mail. 

Quando você envia mensagens LINE pelo Braze, o Braze usa o atributo `native_line_id` para identificar quais usuários devem enviar a mensagem. Quando o LINE envia eventos de webhook do Braze, como quando um usuário segue um canal ou responde a uma mensagem, o endereço `native_line_id` é usado para procurar o perfil de usuário correspondente.

{% alert note %}
As IDs de usuário do LINE são distintas por provedor do LINE. Um usuário específico terá IDs de usuário LINE diferentes para cada provedor que seguir. É improvável que os usuários saibam sua ID do LINE (ao contrário de seu e-mail ou número de telefone), pois elas mudam para cada marca que seguem.
{% endalert %}

## Configuração do atributo `native_line_id` 

Há vários cenários em que o `native_line_id` é definido no perfil do usuário, que são descritos abaixo.

| Cenário | Se o perfil do usuário existe com `native_line_id` | Resultado |
| --- | --- | --- |
|Um usuário segue um canal LINE | Não| Um perfil de usuário anônimo é criado (será necessário mesclar):<br> - `native_line_id` é definido como a LINE ID do usuário <br>- `line_id` O alias do usuário é definido como o ID da LINHA do usuário<br>\- O usuário está inscrito no grupo de assinaturas do Braze do canal |
|Um usuário segue um canal LINE| Sim | Todos os perfis de usuário com o endereço `native_line_id`:<br>\- Estão inscritos no grupo de assinaturas do Braze do canal|
|A empresa usa o upload de CSV do usuário com uma coluna`ative_line_id` | Não| Se não houver perfil de usuário para o `external_id` ou alias de usuário especificado:<br>- `native_line_id` é definido com o valor especificado<br> \- Todos os outros atributos especificados no CSV são definidos no perfil do usuário|
|A empresa usa o upload de CSV do usuário com uma coluna `native_line_id`  | Sim | Se houver um perfil de usuário para o `external_id` ou alias de usuário especificado:<br>- `native_line_id` é definido com o valor especificado<br>\- Todos os outros atributos especificados no CSV são definidos no perfil do usuário<br>\- Vários perfis têm a mesma `native_line_id` |
| A empresa usa o ponto de extremidade `/users/track` e especifica o atributo `native_line_id`  | Não | Se não houver perfil de usuário para o usuário especificado[(especificado por `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>- `native_line_id` é definido com o valor especificado<br>\- Todos os outros atributos especificados na solicitação são definidos no perfil do usuário |
| A empresa usa o ponto de extremidade `/users/track` e especifica o atributo `native_line_id`  | Sim | Se existir um perfil de usuário para o usuário especificado[(especificado por `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>- `native_line_id` é definido com o valor especificado<br>\- Todos os outros atributos especificados na solicitação são definidos no perfil do usuário<br>\- Vários perfis têm a mesma `native_line_id` |
| A empresa solicita que o Braze execute o sincronizador de status da assinatura | Não | Se um ID de usuário LINE for retornado do LINE e não tiver um perfil de usuário correspondente no Braze, será criado um perfil de usuário anônimo:<br>- `native_line_id` é definido como a LINE ID do usuário<br>- `line_id` O alias do usuário é definido como o ID da LINHA do usuário<br>\- O usuário está inscrito no grupo de assinaturas do Braze do canal<br><br>Observe que, se um usuário com o mesmo ID LINE for criado posteriormente, haverá usuários duplicados, mas ambos terão o status de assinatura LINE correto. A fusão de usuários pode limpar sua base de usuários nesses casos. |
| A empresa solicita que o Braze execute o sincronizador de status da assinatura | Sim | Se uma ID de linha de usuário for retornada do LINE e tiver um perfil de usuário correspondente no Braze:<br>\- O usuário está inscrito no grupo de assinaturas do Braze do canal |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Encontrando o `native_line_id`

Ao visualizar o perfil de um usuário no painel do Braze, você pode ver se ele tem o atributo `native_line_id` definido, acessando a guia **Engajamento** > seção **Configurações de contato** > seção **LINE**.

Se o endereço `native_line_id` tiver sido definido, ele será mostrado em **LINE User ID (ID do usuário da linha**). Caso contrário, ele não aparecerá.

Configurações de contato de linha na guia Engajamento.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}

