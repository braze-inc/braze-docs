---
nav_title: Práticas recomendadas de coleta
article_title: Práticas recomendadas de coleta
page_order: 3.1
page_type: reference
description: "O artigo a seguir ajuda a esclarecer diferentes métodos e práticas recomendadas para a coleta de dados de usuários novos e existentes."

---

# Práticas recomendadas de coleta

> Saber quando e como coletar dados de usuários conhecidos e desconhecidos pode ser um desafio quando se imagina o ciclo de vida do perfil do usuário de seus clientes. Este artigo ajuda a esclarecer diferentes métodos e práticas recomendadas para a coleta de dados de usuários novos e existentes, orientando-o em um caso de uso.

O exemplo a seguir é um caso de uso de coleta de e-mail, mas a lógica se aplica a muitos cenários diferentes de coleta de dados. Neste exemplo, presumimos que você já tenha integrado um formulário de inscrição ou uma forma de coletar informações do usuário. 

Depois que um usuário fornecer informações para registro, recomendamos que você verifique se os dados já existem no seu banco de dados e, quando necessário, crie um perfil de alias de usuário ou atualize o perfil de usuário existente.

Se um usuário desconhecido visualizar seu site e, posteriormente, criar uma conta ou identificar-se por meio de envio de e-mail, a mesclagem de perfis deverá ser tratada com cuidado. Com base no método de mesclagem, as informações do usuário somente de alias ou os dados anônimos podem ser substituídos.

## Captura de dados de usuários por meio de um formulário da Web

### Etapa 1: Verificar se o usuário existe

Quando um usuário insere conteúdo por meio de um formulário da Web, verifique se já existe um usuário com esse e-mail em seu banco de dados. Isso pode ser feito de duas maneiras:

- **Verifique o banco de dados interno (recomendado):** Se houver um registro ou banco de dados externo contendo as informações de usuário fornecidas que exista fora do Braze, consulte-o no momento do envio do e-mail ou da criação da conta para confirmar que as informações ainda não foram capturadas.
- **[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/):** Use `email` como identificador, e um novo perfil de usuário será criado se o endereço de e-mail ainda não existir.

### Etapa 2: Registrar ou atualizar o usuário

- **Se existir um usuário:**
  - Não crie um novo perfil.
  - Registre um atributo personalizado (por exemplo, `newsletter_subscribed: true`) no perfil do usuário para indicar que o usuário enviou seu e-mail por meio de uma inscrição em boletim informativo. Se houver vários perfis de usuário Braze com o mesmo endereço de e-mail, todos os perfis serão exportados.<br><br>
- **Se um usuário não existir:**
  - Crie um perfil somente de alias por meio do [endpoint `/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Esse endpoint aceitará um [objeto `user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object/) e criará um perfil somente de alias quando `update_existing_only` estiver definido como `false`. Defina o e-mail do usuário como o alias do usuário para fazer referência a esse usuário no futuro (já que o usuário não terá um `external_id`).

![Diagrama que mostra o processo de atualização de um perfil de usuário somente de alias. Um usuário envia seu endereço de e-mail e um atributo personalizado, seu código postal, em uma landing page de marketing. Uma seta apontando da coleção da landing page para um perfil de usuário somente de alias mostra uma solicitação da Braze API para o endpoint Track user (Rastrear usuário), com o corpo da solicitação contendo o nome do alias do usuário, o rótulo do alias, o e-mail e o código postal. O perfil tem o rótulo "Alias Only user created in Braze" com as atribuições do corpo da solicitação para mostrar os dados que estão sendo refletidos no perfil recém-criado.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Capturar e-mails de usuários por meio de um formulário de captura de e-mail

Use um formulário de captura de e-mail para solicitar que os usuários enviem seu endereço de e-mail, que será adicionado ao perfil do usuário. Para saber mais sobre como configurar esse formulário, consulte [Formulário de captura de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/).
 
## Identificação de usuários somente de alias

Ao identificar usuários na criação da conta, os usuários somente de alias podem ser identificados e atribuídos a uma ID externa por meio do [endpoint`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/), mesclando o usuário somente de alias com o perfil conhecido. 

Para verificar se um usuário é somente de alias, [verifique se o usuário existe](#step-1-check-if-user-exists) em seu banco de dados. 
- Se houver um registro externo, é possível chamar o endpoint `/users/identify/`. 
- Se o [endpoint `/users/export/id`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) retornar um `external_id`, você poderá chamar o endpoint `/users/identify/`.
- Se o endpoint não retornar nada, não deverá ser feita uma chamada para `/users/identify/`.

## Captura de dados de usuários quando as informações de usuário somente de alias já estão presentes

Quando um usuário cria uma conta ou se identifica por meio do envio de e-mail, é possível mesclar os perfis. Para obter uma lista de campos que podem ser mesclados, consulte [Comportamento de mesclagem de atualizações]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).

### Mesclagem de perfis de usuário duplicados

À medida que os dados de seus usuários aumentam, é possível mesclar perfis de usuários duplicados a partir do dashboard do Braze. Esses perfis duplicados devem ser encontrados usando a mesma consulta de pesquisa. Para saber mais sobre como duplicar perfis de usuário, consulte [Mesclar perfis]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#merge-profiles).

Você também pode usar o [endpoint Merge users (Mesclar usuários)]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) para mesclar um perfil de usuário em outro. 

{% alert note %}
Depois que os perfis de usuário são mesclados, essa ação não pode ser desfeita.
{% endalert %}

## Recursos adicionais
- Consulte nosso artigo sobre o [ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) do Braze para obter mais contexto.<br>
- Veja nossa documentação sobre como definir IDs de usuário e chamar o método `changeUser()` para [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#suggested-user-id-naming-convention) e [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web).

