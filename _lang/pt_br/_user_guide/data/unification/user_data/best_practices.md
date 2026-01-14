---
nav_title: Práticas recomendadas de coleta
article_title: Práticas Recomendadas de Coleta
page_order: 3.1
page_type: reference
description: "O seguinte artigo ajuda a esclarecer diferentes métodos e práticas recomendadas para coletar dados de usuários novos e existentes."

---

# Práticas recomendadas de coleta

> Saber quando e como coletar dados de usuários conhecidos e desconhecidos pode ser desafiador ao imaginar o ciclo de vida do perfil do usuário de seus clientes. Este artigo ajuda a esclarecer diferentes métodos e práticas recomendadas para coletar dados de usuários novos e existentes, guiando você por um caso de uso.

O seguinte exemplo é um caso de uso de coleta de e-mail, mas a lógica se aplica a muitos cenários diferentes de coleta de dados. Neste exemplo, assumimos que você já integrou um formulário de inscrição ou uma forma de coletar informações do usuário. 

Depois que um usuário fornece informações para você registrar, recomendamos que você verifique se os dados já existem em seu banco de dados e, quando necessário, crie um perfil de alias de usuário ou atualize o perfil de usuário existente.

Se um usuário desconhecido visualizar seu site e, em uma data posterior, criar uma conta ou se identificar por meio da inscrição por e-mail, a fusão de perfis deve ser tratada com cuidado. Com base no método pelo qual você mescla, as informações de usuário apenas de alias ou dados anônimos podem ser sobrescritos.

## Capturando dados do usuário através de um formulário da web

### Passo 1: Verifique se o usuário existe

Quando um usuário insere conteúdo através de um formulário da web, verifique se um usuário com esse e-mail já existe em seu banco de dados. Isso pode ser feito de duas maneiras:

- **Verifique o banco de dados interno (recomendado):** Se você tiver um registro externo ou banco de dados contendo as informações do usuário fornecidas que existem fora do Braze, consulte isso no momento da submissão do e-mail ou criação da conta para confirmar que as informações ainda não foram capturadas.
- **[`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/):** Use `email` como um identificador, e um novo perfil de usuário será criado se o endereço de e-mail ainda não existir.

### Passo 2: Registrar ou atualizar usuário

- **Se um usuário existir:**
  - Não crie um novo perfil.
  - Registre um atributo personalizado (por exemplo, `newsletter_subscribed: true`) no perfil do usuário para indicar que o usuário enviou seu e-mail através de uma assinatura de newsletter. Se vários perfis de usuário Braze existirem com o mesmo endereço de e-mail, todos os perfis serão exportados.<br><br>
- **Se um usuário não existir:**
  - Crie um perfil apenas de alias através do [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Este endpoint aceitará um [`user_alias` objeto]({{site.baseurl}}/api/objects_filters/user_alias_object/) e criará um perfil apenas de alias quando `update_existing_only` estiver definido como `false`. Defina o e-mail do usuário como o alias do usuário para referenciar esse usuário no futuro (já que o usuário não terá um `external_id`).

\![Diagrama mostrando o processo para atualizar um perfil de usuário apenas de alias. Um usuário envia seu endereço de e-mail e um atributo personalizado, seu código postal, em uma página de destino de marketing. Uma seta apontando da coleção da página de destino para um perfil de usuário apenas de alias mostra uma solicitação da API Braze para o endpoint de rastreamento de usuário, com o corpo da solicitação contendo o nome do alias do usuário, rótulo do alias, e-mail e código postal. O perfil tem o rótulo "Usuário apenas de alias criado no Braze" com os atributos do corpo da solicitação para mostrar os dados sendo refletidos no perfil recém-criado.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Capturando e-mails de usuários através de um formulário de captura de e-mail

Use um formulário de captura de e-mail para solicitar que os usuários enviem seu endereço de e-mail, que será adicionado ao perfil do usuário. Para mais informações sobre como configurar este formulário, confira [Formulário de captura de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/).
 
## Identificando usuários apenas de alias

Ao identificar usuários na criação da conta, usuários apenas de alias podem ser identificados e atribuídos um ID externo através do [`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) ao mesclar o usuário apenas de alias com o perfil conhecido. 

Para verificar se um usuário é apenas de alias, [verifique se o usuário existe](#step-1-check-if-user-exists) em seu banco de dados. 
- Se um registro externo existir, você pode chamar o `/users/identify/` endpoint. 
- Se o [`/users/export/id` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) retornar um `external_id`, você pode chamar o `/users/identify/` endpoint.
- Se o endpoint não retornar nada, uma chamada `/users/identify/` não deve ser feita.

## Capturando dados do usuário quando informações de usuário apenas por alias já estão presentes

Quando um usuário cria uma conta ou se identifica através do cadastro por e-mail, você pode mesclar os perfis. Para uma lista de campos que podem ser mesclados, consulte [Comportamento de atualizações de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).

### Mesclando perfis de usuário duplicados

À medida que seus dados de usuário crescem, você pode mesclar perfis de usuário duplicados no painel do Braze. Esses perfis duplicados devem ser encontrados usando a mesma consulta de pesquisa. Para mais informações sobre como duplicar perfis de usuário, confira [Mesclar perfis]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#merge-profiles).

Você também pode usar o [endpoint de mesclagem de usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) para mesclar um perfil de usuário em outro. 

{% alert note %}
Após os perfis de usuário serem mesclados, essa ação não pode ser desfeita.
{% endalert %}

## Recursos adicionais
- Confira nosso artigo sobre o [ciclo de vida do perfil do usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) do Braze para contexto adicional.<br>
- Veja nossa documentação sobre como definir IDs de usuário e chamar o método `changeUser()` para [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#suggested-user-id-naming-convention) e [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web).

