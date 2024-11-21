---
nav_title: "Migração de dados de usuários"
article_title: Migração de dados de usuários
page_order: 4
description: "Este artigo de referência aborda todas as considerações que você precisará ter em mente ao migrar seus dados de usuários para o Braze."
page_type: reference
channel:
  - SMS
noindex: true

---

# Migração de dados de usuários

> Este artigo abordará todas as considerações que você precisará ter em mente ao migrar seus dados de usuários para o Braze.

## Formatar os números de telefone do usuário de acordo com os padrões da operadora

As operadoras de telefonia têm um tipo específico de formato que esperam, chamado E.164, que é o plano de numeração telefônica internacional que garante que cada dispositivo tenha um número globalmente exclusivo. É isso que permite que as chamadas telefônicas e as mensagens de texto sejam corretamente roteadas para telefones individuais em diferentes países. E.164 números são formatados conforme mostrado na imagem a seguir e podem ter no máximo 15 dígitos.

![E.164 O formato consiste em um sinal de mais, código do país, código de área e número de telefone][imagem]{: style="max-width:50%;border: 0;"}

Para saber mais, consulte [Números de telefone do usuário][userphone].

## Atualizar informações históricas sobre os estados de inscrição dos usuários

Se tiver alguma informação histórica sobre os [estados de inscrição][subscriptionstate] ] do seu usuário para seus vários canais de envio de mensagens, atualize essas informações na Braze.

## Exemplo de etapas de migração

Antes de começar a criar campanhas de SMS por meio do Braze, será necessário atualizar os dados de usuários para garantir que tudo isso funcione.

**Aqui está um resumo rápido dos dados de usuários que você precisará atualizar no Braze:**

1. **Importar os números de telefone dos usuários no formato correto** ([E.164][0]), a formatação requer um sinal de mais (+) e um código de país. Um exemplo é +12408884782. Para saber mais sobre como fazer a importação de números de telefone de usuários, consulte [Números de telefone de usuários][userphone].
    * Use o [endpoint`/users/track` ][1] para atribuir o valor `phone`.<br><br>

2. **Atribua o SMS do seu usuário [status de inscrição][subscriptionstate]** (como inscrito ou cancelado) se tiver essa informação.
    * Use o [ponto de extremidade`/subscription/status/set` ][6] para definir os usuários como inscritos ou cancelados em seus grupos de inscrições de SMS.

{% alert note %}
Depois de configurar os grupos de inscrições de SMS em seu dashboard, você poderá obter o `subscription_group_id` associado, que será necessário para sua solicitação de API.
{% endalert %}

[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[picture]: {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#sms-subscription-states
