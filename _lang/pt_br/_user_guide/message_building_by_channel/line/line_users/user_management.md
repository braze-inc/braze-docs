---
nav_title: Gerenciamento de Usuários
article_title: LINE Gerenciamento de Usuários
page_order: 0
description: "Este artigo cobre o ID de usuário LINE e como configurá-lo."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# GERENCIAMENTO DE USUÁRIOS

> O ID do usuário do LINE é armazenado no atributo do perfil do usuário chamado `native_line_id`, que é usado para enviar mensagens a um usuário no canal LINE. Este artigo aborda como definir e encontrar o atributo `native_line_id`.

Os dados de usuários do cliente são representados em um [Braze user profile]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/). Um perfil de usuário armazena informações e atributos sobre os usuários de uma empresa, como nomes e e-mails. 

Quando você envia mensagens LINE através do Braze, o Braze usa o `native_line_id` atributo para identificar quais usuários enviar a mensagem. Quando a LINE envia eventos de webhook do Braze, como quando um usuário segue um canal ou responde a uma mensagem, o `native_line_id` é usado para procurar o perfil de usuário correspondente.

{% alert note %}
Os IDs de usuário do LINE são distintos por provedor do LINE. Um usuário específico terá diferentes LINE IDs de usuário para cada provedor que eles seguem. Os usuários provavelmente não saberão seu ID do LINE (diferente de seu e-mail ou número de telefone), pois eles mudam para cada marca que seguem.
{% endalert %}

## Definindo o atributo `native_line_id`

Existem vários cenários onde `native_line_id` está definido no perfil do usuário, que estão descritos abaixo.

| Cenário | Se o perfil do usuário existe com `native_line_id` | Resultado |
| --- | --- | --- |
|Um usuário segue um canal LINE | Não| Um perfil de usuário anônimo é criado (a fusão será necessária):<br> `native_line_id` é definido como o ID de LINE do usuário <br>`line_id` o alias do usuário é definido como o ID do LINE do usuário<br>O usuário está inscrito no grupo de inscrições Braze do canal. |
|Um usuário segue um canal LINE| Sim | Todos os perfis de usuário com o `native_line_id`:<br>Estão inscritos no grupo de inscrições do canal Braze|
|A empresa usa o upload de CSV do usuário com uma coluna n `ative_line_id`| Não| Se nenhum perfil de usuário existir para o `external_id` especificado ou alias de usuário:<br>`native_line_id` é definido para o valor especificado<br> Todos os outros atributos especificados no CSV são definidos no perfil do usuário.|
|A empresa utiliza o upload de CSV do usuário com uma `native_line_id` coluna | Sim | Se um perfil de usuário existir para o `external_id` especificado ou alias de usuário:<br>`native_line_id` é definido para o valor especificado<br>Todos os outros atributos especificados no CSV são definidos no perfil do usuário.<br>Vários perfis têm o mesmo `native_line_id` |
| A empresa usa `/users/track` ponto de extremidade e especifica `native_line_id` atributo | Não | Se nenhum perfil de usuário existir para o usuário especificado ([especificado por `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>`native_line_id` é definido para o valor especificado<br>Todos os outros atributos especificados na solicitação estão definidos no perfil do usuário. |
| A empresa usa `/users/track` ponto de extremidade e especifica `native_line_id` atributo | Sim | Se um perfil de usuário existir para o usuário especificado ([especificado por `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>`native_line_id` é definido para o valor especificado<br>Todos os outros atributos especificados na solicitação estão definidos no perfil do usuário.<br>Vários perfis têm o mesmo `native_line_id` |
| A empresa solicita que o Braze execute a sincronização do status da inscrição | Não | Se um ID de usuário LINE for retornado do LINE que não tem um perfil de usuário correspondente no Braze, então um perfil de usuário anônimo é criado:<br>`native_line_id` é definido como o ID de LINE do usuário<br>`line_id` o alias do usuário é definido como o ID do LINE do usuário<br>O usuário está inscrito no grupo de inscrições Braze do canal.<br><br>Nota que se um usuário com o mesmo ID de LINE for criado posteriormente, haverá usuários duplicados, mas ambos terão o status de inscrição de LINE correto. A fusão de usuários pode limpar sua base de usuários nesses casos. |
| A empresa solicita que o Braze execute a sincronização do status da inscrição | Sim | Se um ID de usuário LINE for retornado do LINE que tenha um perfil de usuário correspondente no Braze:<br>O usuário está inscrito no grupo de inscrições Braze do canal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Encontrando o `native_line_id`

Ao visualizar um perfil de usuário no dashboard do Braze, você pode ver se ele tem o atributo `native_line_id` definido indo para a guia **Engajamento** > seção **Configurações de Contato** > seção **LINE**.

Se o `native_line_id` foi definido, estará sob **LINE User ID**. Caso contrário, não aparecerá.

![Configurações de Contato de Linha na guia de Engajamento.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}

