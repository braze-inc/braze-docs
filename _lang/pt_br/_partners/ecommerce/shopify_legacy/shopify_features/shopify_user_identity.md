---
nav_title: Gestão de Identidade do Usuário do Shopify
article_title: "Gestão de Identidade do Usuário do Shopify"
description: "Este artigo de referência descreve o recurso de gerenciamento de identidade do usuário da Shopify."
page_type: partner
search_tag: Partner
alias: "/shopify_user_identity/"
page_order: 3
---

# Gerenciamento de identidade do usuário do Shopify

> Braze receberá sinais de seus clientes do Shopify por meio de seus comportamentos no site e ouvindo os webhooks do Shopify que você configurou como parte de sua integração. Para sites não headless da Shopify, a Braze ajudará a reconciliar os usuários da página de checkout. Para sites headless da Shopify, consulte nosso guia de integração sobre como [reconciliar usuários do checkout]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#headless-checkout).

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Capturando informações para perfis de usuários 

### rastreamento de usuário do Shopify

Se os visitantes da sua loja forem convidados (ou seja, anônimos), a Braze capturará o `device_id` para as sessões desses clientes específicos. Depois de configurar a reconciliação de usuários para formulários do Shopify durante sua [implementação do Web SDK]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk), os e-mails dos clientes serão adicionados aos perfis de usuários anônimos sempre que os clientes inserirem suas informações em um formulário. 

Quando os visitantes da loja inserem seu e-mail em um formulário de captura de newsletter ou e-mail do Shopify, o Braze receberá um evento de webhook do Shopify para criar o perfil do usuário. Braze então mescla este perfil de usuário com o perfil de usuário anônimo rastreado pelo Web SDK e atribui o ID de cliente do Shopify como o alias do usuário no perfil de usuário. 

À medida que os clientes avançam para o checkout e fornecem outras informações identificáveis, como números de telefone, a Braze deve capturar os dados de usuários relevantes dos webhooks do Shopify e mesclá-los com o usuário anônimo com o `device_id`.
- Se você implementou o SDK para Web via Shopify ScriptTag, em um site não headless da Shopify ou via Google Tag Manager, a Braze garantirá automaticamente que os dados de usuários da página de checkout e os dados da sessão do perfil de usuário anônimo sejam mesclados ao perfil de alias de usuário com o ID de cliente da Shopify atribuído.
- Se você implementou o SDK para Web em um site headless da Shopify, confirme se os dados de usuários enviados na página de checkout estão devidamente atribuídos ao perfil de usuário correto pelo SDK para Web ou pela API. Para saber mais, confira [Como implementar o SDK para Web diretamente no seu site headless da Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#headless-site).

À medida que os clientes continuam o processo de finalização da compra, a Braze verifica se o endereço de e-mail, número de telefone ou ID de cliente do Shopify inserido corresponde a um perfil de usuário existente. Se houver uma correspondência, a Braze sincroniza os dados de usuários do Shopify com esse perfil.

Se o endereço de e-mail ou número de telefone estiver associado a vários perfis de usuário identificados, a Braze sincroniza os dados do Shopify com o perfil com a atividade mais recente.

Se a Braze não encontrar uma correspondência para o endereço de e-mail ou número de telefone, a Braze criará um novo perfil de usuário com os dados suportados do Shopify.

### Quando os clientes da Shopify sincronizam com a Braze

Braze atualiza perfis de usuário existentes ou cria novos para leads, inscrições e registros de contas capturados em sua loja Shopify. Você pode coletar dados de perfil de usuário com os seguintes métodos na Shopify e mais:
- Cliente cria uma conta
- O endereço de e-mail ou número de telefone do cliente é coletado em um formulário de captura do Shopify
- O endereço de e-mail do cliente é coletado de um formulário de newsletter
- O endereço de e-mail ou número de telefone do cliente é coletado por meio de uma ferramenta de terceiros que está conectada ao Shopify, como o EcomSend

A Braze tentará primeiro mapear os dados suportados do Shopify para quaisquer perfis de usuário existentes usando o endereço de e-mail ou número de telefone do cliente. 

Para evitar perfis de usuário duplicados, é fundamental que você revise as instruções de reconciliação de usuários para o Shopify Forms para o método que você usou para [implementar o Web SDK no seu site Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk).

## Mesclagem de perfis de usuário 

{% alert note %}
A integração padrão da Shopify fornece ferramentas para ajudar a mesclar seu perfil de usuário anônimo e o perfil de alias da Shopify. Se você estiver implementando a integração em um site headless da Shopify, consulte [Como implementar o SDK para Web diretamente no seu site headless da Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features) para confirmar se está reconciliando seus usuários corretamente. <br><br> Se você encontrar perfis de usuário duplicados, pode usar nossa [ferramenta de mesclagem em massa]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging/) para ajudar a simplificar seus dados.
{% endalert %}

Braze mescla os campos do perfil de usuário anônimo com o perfil de usuário identificado quando encontramos uma correspondência com um dos seguintes:
- ID do cliente do Shopify
- E-mail
- Número de telefone

Braze mescla os seguintes campos do perfil de usuário anônimo para o perfil de usuário identificado:
- Nome
- Sobrenome
- E-mail
- Gênero
- Data de nascimento
- Número de telefone
- Fuso horário
- Cidade natal
- País
- Idioma
- Atributos personalizados
    - Dados de evento personalizado e evento de compra (excluindo propriedades de evento, contagem e carimbos de data e hora da primeira e última data)
    - Propriedades de evento personalizado e evento de compra para segmentação “X vezes em Y dias” (onde X<=50 e Y<=30)
- push tokens
- Histórico de mensagens
- Qualquer um dos seguintes campos encontrados no perfil do usuário anônimo ou no perfil do usuário identificado, como evento personalizado, contagem de eventos de compra e carimbos de data e hora da primeira e última data
    - Esses campos mesclados atualizarão os filtros “para X eventos em Y dias”. Para eventos de compra, esses filtros incluem "número de compras em Y dias" e "dinheiro gasto nos últimos Y dias".

{% alert important %}
Os dados da sessão ainda não são suportados como parte do processo de mesclagem.
{% endalert %}

## Sincronizando assinantes do Shopify

Durante o processo de configuração do Shopify, a Braze fornece controles flexíveis para sincronizar os endereços de e-mail dos seus clientes e os estados de aceitação de SMS com os grupos de inscrição e os estados de inscrição nos perfis de usuário da Braze. 

### Coletar inscritos de e-mail ou SMS

Durante a configuração da loja Shopify no Braze, você terá a opção de sincronizar seus assinantes de e-mail e SMS do Shopify no Braze. 

#### Coletar inscritos de e-mails

Para ativar a coleta de inscritos de e-mail, ative o recurso na sua configuração da Shopify. Recomendamos que você atribua pelo menos um [grupo de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups), da Braze como inscritos de e-mail da Shopify. Braze adicionará seus assinantes de e-mail aos grupos de inscrição especificados para que eles sejam incluídos no seu direcionamento de público quando você enviar uma mensagem. 

![]({% image_buster /assets/img/Shopify/collect_email.png %})

Quando ativado, a Braze sincronizará atualizações para seus assinantes de e-mail do Shopify e atualizações para seus estados de inscrição de e-mail em tempo real. Se você não ativar a opção de substituição, seus clientes da Shopify serão inscritos ou desinscritos do grupo de inscrições associado à sua loja da Shopify.

Se você ativar a opção de substituição, a Braze atualizará o estado global de inscrição no perfil do usuário. Isso significa que, se seus clientes estiverem marcados como cancelaram inscrição no Shopify, o Braze marcará o estado de inscrição global como cancelaram inscrição no perfil do usuário e cancelar a inscrição do cliente de todos os grupos de inscrição de e-mail disponíveis. Como resultado, nenhuma mensagem será enviada aos usuários que cancelaram a inscrição globalmente do e-mail.

#### Coletar inscritos de SMS

Para coletar assinantes de SMS do Shopify, você deve criar [grupos de inscrição de SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) como parte da sua [configuração de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/). 

Quando você estiver com tudo pronto para coletar seus inscritos de SMS da Shopify, ative a coleta de inscritos de SMS na página de configuração da Shopify. Você deve selecionar pelo menos um grupo de inscrições de SMS para que possa direcionar e enviar mensagens de SMS adequadamente. 

![]({% image_buster /assets/img/Shopify/collect_sms.png %})

Quando ativado, a Braze sincronizará atualizações para seus assinantes de SMS do Shopify e seus estados de inscrição de SMS em tempo real. Se você não ativar a opção de substituição, seus clientes da Shopify serão inscritos ou desinscritos do grupo de inscrições associado à sua loja da Shopify.

Os inscritos de SMS não têm estados de inscrição globais, então você não precisa considerá-los ao usar uma opção de substituição. Um usuário só pode ser desinscrito ou inscrito em um grupo de inscrições de SMS.

#### Atributos personalizados legados

Clientes antigos do Shopify podem ter o método antigo de coletar assinantes de e-mail e SMS através dos atributos personalizados `shopify_accepts_marketing` e `shopify_sms_consent`. Se você salvar as configurações acima com a substituição ativada, a Braze removerá os atributos personalizados nos perfis de usuário e sincronizará esses valores com seu respectivo grupo de inscrições para e-mail e grupo de inscrições para SMS.

Se você tiver campanhas ou canvas existentes usando esses atributos personalizados legados, remova esses atributos e confirme se as campanhas ou canvas estão usando o estado de inscrição apropriado, grupo ou ambos.
