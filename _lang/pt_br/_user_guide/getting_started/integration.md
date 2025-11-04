---
nav_title: Integração
article_title: Visão geral da integração de onboarding
page_order: 8
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."

---

# Integração

> A integração com o Braze é um processo que vale a pena. Mas você é inteligente. Você está **aqui**. É claro que você já sabe disso. Mas o que você provavelmente não sabe é que você e seus desenvolvedores estão prestes a embarcar em uma jornada conjunta que requer conhecimento técnico, planejamento estratégico e comunicação consistente que ajudará na coordenação entre os dois.

{% alert note %}
Observe que o conteúdo deste artigo não se aplica a e-mails. Verifique isso na seção [Configuração de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/).
{% endalert %}

## O lado técnico do processo de integração

Você pode se pegar pensando: "Meus desenvolvedores são mágicos! Eles podem fazer qualquer coisa, então eu geralmente os deixo à vontade!" E eles provavelmente estão e provavelmente podem! Mas não há razão para que você não saiba o que eles estão fazendo nos bastidores. Na verdade, isso ajudaria todo o processo se você soubesse quando entrar com informações e o que procurar quando eles disserem: "Você pode me enviar a chave da API e o endpoint da API?"

Então, o que eles estão fazendo quando integram o Braze ao seu aplicativo ou site? Que bom que você perguntou!

### Etapa 1: Eles implementam o SDK do Braze

O Braze SDK (Software Development Kit) é a forma como enviamos e obtemos informações de e para seu aplicativo ou site. Seus engenheiros estão, essencialmente, unindo nossos aplicativos. Para isso, eles precisam de algumas informações importantes:

* Suas [chaves de API]({{site.baseurl}}/api/api_key/)
* Seu [ponto de extremidade do SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * O Braze não fornece mais endpoints personalizados, portanto, use os endpoints predefinidos do SDK. Se você recebeu um endpoint personalizado pré-existente, aqui você pode encontrar as etapas de configuração envolvidas na integração [com Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) e [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk).

Você pode fornecer essas informações diretamente a eles ou dar-lhes acesso ao Braze criando uma conta para eles. 

{% alert warning %}
Certifique-se de que você e seus desenvolvedores não alterem as credenciais da empresa no Braze de forma inadvertida ou não intencional, pois isso pode causar problemas durante o processo de implementação ou bloquear uma ou mais contas.
{% endalert %}

### Etapa 2: Eles implementam seus canais de mensagens desejados

O Braze tem muitas opções para entrar em contato com seus usuários, e cada uma delas requer sua própria configuração ou ajuste para funcionar da maneira que você deseja. É nesse ponto que a comunicação com seus engenheiros se torna fundamental.

Não deixe de informar aos desenvolvedores quais canais você deseja usar para garantir que a implementação seja feita de forma eficiente e na ordem correta.

| Canal | Detalhes |
|---|---|
| Mensagens no aplicativo | Requer a implementação do SDK, bem como essas etapas específicas do canal. |
| Empurrar | Requer a implementação do SDK para fornecer o tratamento adequado das credenciais de mensagens e dos tokens de envio. |
| E-mail | Esse é um processo totalmente diferente. Consulte a seção [Configuração de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/) para obter mais detalhes sobre a integração. |
| Cartões de conteúdo | Para começar a usar [os cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), entre em contato com seu gerente de sucesso do cliente Braze. |
| SMS & MMS | Consulte a seção [Configuração de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/) para obter mais detalhes sobre a integração. |
| Webhooks | Requer a implementação do SDK, bem como etapas específicas do canal. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Você pode usar o Braze para criar campanhas de mensagens acessíveis em cada canal. Trabalhe com seus desenvolvedores para garantir que você atenda aos padrões de acessibilidade em sua implementação.
{% endalert %}

### Etapa 3: Eles configuram seus dados

O Braze não é um pônei de um truque só. Não se trata apenas de enviar e-mails ou enviar push. Trata-se de criar jornadas de clientes personalizadas e exclusivas para cada usuário e cliente. As jornadas do cliente se baseiam nas ações dele dentro do seu aplicativo ou site, e você pode definir quais são elas! A próxima tarefa de seus desenvolvedores é garantir que as ações realizadas em seu aplicativo ou site sejam captadas pelo Braze.

Então, o que você precisa fazer para obter essas informações?

1. Trabalhe com sua equipe de marketing para definir campanhas, metas, atributos e eventos que você precisa monitorar. Defina esses casos de uso e compartilhe-os com suas equipes.
2. Defina seus requisitos de dados personalizados[(atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/), etc.).
3. A partir daí, discuta como esses dados devem ser rastreados (acionados por meio do SDK, etc.).
4. Defina quantos [espaços de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/) você precisa. Seus engenheiros precisarão saber como [testar e configurar]({{site.baseurl}}/user_guide/getting_started/workspaces/) esses espaços de trabalho.

Depois de descobrir todas essas informações, compartilhe-as com seu engenheiro. Eles pegarão essas informações e implementarão seus [dados personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/). Talvez seja necessário [importar alguns usuários]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/). Você também deve estar ciente das [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

### Etapa 4: Eles personalizam com base no que você deseja

Se quiser coisas como lançamento acionado por API e Connected Content, discuta isso com o seu contato no Braze e com os desenvolvedores para garantir que você conseguirá obter dados que estão fora do seu aplicativo e do Braze em suas mensagens.

### Etapa 5: Vocês dois realizam o controle de qualidade em sua implementação

Trabalhe em conjunto com seu engenheiro para garantir que tudo esteja funcionando. Envie [mensagens de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/), use nossos [aplicativos de teste para Android]({{site.baseurl}}/developer_guide/references/?tab=android) e [aplicativos de teste para iOS]({{site.baseurl}}/developer_guide/references/?tab=swift), verifique todas as caixas antes de começar a enviar!

Temos até instruções específicas para [testar sua integração com Android ou FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) e testar o [push para iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing/).

## Após a implementação

Lembre-se de que a linha de chegada da implementação não é também o sinal verde para enviar um milhão de mensagens ao mesmo tempo. O envio de um milhão de push pode prejudicar seu aplicativo se todos os clientes clicarem no mesmo link simultaneamente. Recomendamos que você discuta qual é a capacidade de sua configuração interna para lidar com solicitações do Braze antes de clicar no botão **Enviar**. Em seguida, você pode definir a [limitação de]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) sua [taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) com base nisso.

\![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Depois que você se sentir confortável usando o Braze, considere a possibilidade de se tornar um Braze Firebrand! Com o Braze Firebrands, nossa comunidade de engajamento do cliente, estamos criando uma comunidade de pessoas que se movimentam e agitam usando o Braze para modernizar a experiência do cliente e o marketing. Interessado em saber mais? [Registre-se agora](https://brazefirebrands.splashthat.com/).
