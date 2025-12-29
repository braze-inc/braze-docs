---
nav_title: Ciclo de vida do perfil do usuário
article_title: Ciclo de vida do perfil do usuário
page_order: 2
page_type: reference
description: "Este artigo de referência descreve o ciclo de vida do perfil de usuário do Braze e as várias maneiras pelas quais um perfil de usuário pode ser identificado e referenciado."

---

# Ciclo de vida do perfil do usuário

> Este artigo descreve o ciclo de vida do perfil de usuário do Braze e as várias maneiras de identificar e fazer referência a um perfil de usuário. Se quiser entender melhor o ciclo de vida do cliente, confira nosso curso do Braze Learning sobre [Mapeamento do ciclo de vida do usuário](https://learning.braze.com/mapping-customer-lifecycles).

Todos os dados persistentes associados a um usuário são armazenados em seu perfil de usuário. Depois que um perfil de usuário é criado, seja por meio da API ou depois que um usuário é reconhecido pelo SDK, é possível atribuir vários parâmetros a esse perfil para identificar e fazer referência a esse usuário. 

Esses parâmetros incluem:

* `braze_id` (atribuído por Braze)
* `external_id`
* `email`
* `phone`
* Qualquer número de aliases de usuário personalizados que você definir

## Perfis de usuários anônimos

Qualquer usuário sem um `external_id` designado é chamado de [usuário anônimo]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/). Por exemplo, esses podem ser usuários que visitaram seu site, mas não se inscreveram, ou usuários que baixaram seu aplicativo móvel, mas não criaram um perfil.

Inicialmente, quando um usuário é reconhecido pelo SDK, um perfil de usuário anônimo é criado com um `braze_id` associado: um identificador exclusivo que é atribuído automaticamente pelo Braze, não pode ser editado e é específico do dispositivo. Esse identificador pode ser usado para atualizar o perfil do usuário por meio da [API]({{site.baseurl}}/api/endpoints/user_data/).

## Perfis de usuários identificados

Depois que um usuário for reconhecido em seu aplicativo (fornecendo uma forma de ID de usuário ou endereço de e-mail), sugerimos atribuir um `external_id` ao perfil desse usuário usando o método `changeUser` [(Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). O site `external_id` permite identificar o mesmo perfil de usuário em vários dispositivos.

Os benefícios adicionais de usar um `external_id` incluem o seguinte: 

- Fornecer uma experiência de usuário consistente em vários dispositivos e plataformas (por exemplo, não enviar notificações de usuário caducas para o tablet Android de um usuário quando ele é um usuário fiel do aplicativo para iPhone).
- Aumente a precisão de suas análises confirmando que os usuários não estão criando um novo perfil de usuário sempre que desinstalam e reinstalam ou instalam o aplicativo em um dispositivo diferente.
- Habilite a importação de dados do usuário de fontes externas ao aplicativo usando os [pontos de extremidade de dados do usuário]({{site.baseurl}}/api/endpoints/user_data/) e direcione os usuários com mensagens transacionais usando nossos [pontos de extremidade de mensagens]({{site.baseurl}}/api/endpoints/messaging/).
- Pesquise usuários individuais usando nossos [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) "Testing" no segmentador e na seção [**Pesquisar usuários**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) página.

### Considerações sobre IDs externas

{% alert warning %}
Não atribua um `external_id` a um perfil de usuário antes de poder identificá-lo de forma exclusiva. Depois de identificar um usuário, não é possível revertê-lo para anônimo.
<br><br>
Um `external_id` pode ser atualizado usando o [ponto de extremidade`/users/external_ids/rename` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/). No entanto, qualquer tentativa de definir um `external_id` diferente durante a sessão de um usuário criará um novo perfil de usuário com o novo `external_id` associado a ele. Nenhum dado será transmitido entre os dois perfis.
{% endalert %} 

#### Risco de usar um e-mail ou um e-mail com hash como uma ID externa

O uso de um endereço de e-mail ou de um endereço de e-mail com hash como sua ID externa Braze pode simplificar o gerenciamento de identidade em todas as suas fontes de dados; no entanto, é importante considerar os possíveis riscos à privacidade do usuário e à segurança dos dados.

- **Informações que podem ser adivinhadas:** Os endereços de e-mail são facilmente adivinháveis, o que os torna vulneráveis a ataques.
- **Risco de exploração:** Se um usuário mal-intencionado alterar seu navegador da Web para enviar o endereço de e-mail de outra pessoa como sua ID externa, ele poderá acessar mensagens confidenciais ou informações da conta.

### O que acontece quando você identifica usuários anônimos

Um dos dois cenários pode ocorrer quando você identifica usuários anônimos:

1) **Um usuário anônimo se torna um novo usuário identificado:** <br>Se o `external_id` ainda não existir no Braze, o usuário anônimo se tornará um novo usuário identificado e manterá todos os mesmos atributos e histórico do usuário anônimo. 

2) **Um usuário anônimo é identificado como um usuário já existente:** <br>Se o `external_id` já existir no Braze, então esse usuário foi previamente identificado como um usuário no sistema de alguma outra forma, como por meio de outro dispositivo (como um tablet) ou dados de usuário importados. 

Em outras palavras, você já tem um perfil de usuário para esse usuário. Nesse caso, o Braze fará o seguinte:
1. Tornar órfão o usuário anônimo
2. Mesclar [campos de perfil de usuário específicos]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) que ainda não existem no perfil de usuário identificado do perfil anônimo
3. Remova o perfil anônimo da sua base de usuários para que a contagem de usuários não seja inflada

Se tanto o usuário anônimo quanto o usuário conhecido tiverem um primeiro nome, o primeiro nome do usuário conhecido será mantido. Se o usuário conhecido tiver um valor nulo e o usuário anônimo tiver um valor, o valor do usuário anônimo será mesclado no perfil do usuário conhecido se o valor se enquadrar nesses [campos específicos do perfil do usuário]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

Para obter informações sobre como definir um `external_id` em relação a um perfil de usuário, consulte nossa documentação[(iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)).

## Aliases de usuário

Para se referir aos usuários por outros identificadores que não o Braze `external_id`, defina aliases de usuário em um perfil de usuário. Qualquer alias definido em um perfil de usuário atuará além do `braze_id` ou `external_id` do usuário, em vez de substituí-lo. Não há limite para o número de aliases que podem ser definidos em um perfil de usuário.

Cada alias funciona como um par chave-valor que consiste em duas partes: um `alias_label`, que define a chave do alias, e um `alias_name`, que define o valor. Um `alias_name` para qualquer rótulo único deve ser exclusivo em toda a sua base de usuários (assim como em `external_id`). Se você tentar atualizar um segundo perfil de usuário com uma combinação de rótulo e nome pré-existente, o perfil de usuário não será atualizado.

### Atualização de aliases de usuário

Um alias pode ser atualizado com um novo nome para um determinado rótulo depois de definido, usando nossos [pontos de extremidade de dados do usuário]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) ou passando um novo nome pelo SDK. O alias do usuário ficará visível ao exportar os dados desse usuário.

\![Dois perfis de usuário diferentes para usuários separados com o mesmo rótulo de alias de usuário, mas com nomes de alias diferentes]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Marcação de usuários anônimos

Os aliases de usuário também permitem que você marque usuários anônimos com um identificador. Por exemplo, se um usuário fornecer ao seu site de comércio eletrônico o endereço de e-mail, mas ainda não tiver se inscrito, o endereço de e-mail poderá ser usado como um alias para esse usuário anônimo. Esses usuários podem então ser exportados usando seus aliases ou referenciados pela API.

### Comportamento de aliases em perfis de usuários anônimos

Se um perfil de usuário anônimo com um alias for reconhecido posteriormente com um `external_id`, ele será tratado como um perfil de usuário identificado normal, mas manterá o alias existente e ainda poderá ser referenciado por esse alias.

### Definição de aliases em perfis de usuários conhecidos

Um alias de usuário também pode ser definido em um perfil de usuário conhecido para fazer referência a um usuário conhecido por outro ID conhecido externamente. Por exemplo, um usuário pode ter um ID de ferramenta de business intelligence (como um Amplitude ID) que você deseja referenciar no Braze.

Para obter informações sobre como definir um alias de usuário, consulte nossa documentação para cada plataforma[(iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users)).

Um fluxograma do ciclo de vida de um perfil de usuário no Braze. Quando changeUser() é chamado para um usuário anônimo, esse usuário se torna um usuário identificado e os dados são migrados para seu perfil de usuário identificado. O usuário identificado tem uma ID Braze e uma ID externa. Nesse ponto, se um segundo usuário anônimo tiver changeUser() chamado, os campos de dados do usuário que ainda não existirem no Identified User serão mesclados. Se o usuário identificado tiver um alias adicionado ao seu perfil de usuário existente, nenhum dado será afetado, mas ele se tornará um usuário identificado com alias. Se um terceiro usuário anônimo com o mesmo rótulo de alias que o usuário identificado, mas com um nome de alias diferente, tiver a função changeUser() chamada, todos os campos que não existirem no usuário identificado serão mesclados e o rótulo de alias no perfil do usuário identificado será mantido.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Está com dificuldades para imaginar como isso pode ser visto no ciclo de vida do perfil do usuário de seus clientes? Visite [Práticas recomendadas]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/) para ver as práticas recomendadas de coleta de dados do usuário.
{% endalert %}

## Caso de uso avançado

Você pode definir um novo alias de usuário para perfis de usuário identificados existentes por meio do nosso SDK e da nossa API usando os [pontos de extremidade de dados do usuário]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint). No entanto, os aliases de usuário não podem ser definidos por meio da API para um perfil de usuário desconhecido existente.

Os aliases de usuário também são mesclados no processo. No entanto, se tanto o usuário a ser tornado órfão quanto o usuário de destino tiverem um alias com o mesmo rótulo, somente o alias do usuário de destino será mantido.

Desinstalar e reinstalar um aplicativo gerará um novo `braze_id` anônimo para esse usuário.

### Solução de problemas com IDs de usuário

Todos os IDs de usuário podem ser usados para localizar e identificar usuários em seu painel para testes. Para localizar seu usuário no painel do Braze, consulte [Adicionar usuários de teste]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

{% alert important %}
O Braze banirá ou bloqueará os usuários com mais de 5.000.000 de sessões ("usuários fictícios") e não ingerirá mais seus eventos de SDK, pois esses usuários geralmente são o resultado de uma integração incorreta. Se você descobrir que isso aconteceu com um usuário legítimo, entre em contato com o gerente da sua conta Braze.
{% endalert %}