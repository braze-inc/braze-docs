---
nav_title: Integração
article_title: Visão geral da integração
page_order: 8
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."

---

# Integração

> A integração com a Braze é um processo que vale a pena. Mas você é inteligente. Você está **aqui**. É claro que você já sabe disso. Mas o que você provavelmente não sabe é que você e seus desenvolvedores estão prestes a acessar uma jornada juntos que requer conhecimento técnico, planejamento estratégico e comunicação consistente que ajudará na coordenação entre os dois.

{% alert note %}
Note que o conteúdo deste artigo não se aplica a e-mails. Verifique isso na seção de [configuração de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/).
{% endalert %}

## O lado técnico do processo de integração

Você pode se pegar pensando: "Meus desenvolvedores são mágicos! Eles podem fazer qualquer coisa, então, geralmente, eu os deixo à vontade!" E eles provavelmente estão e provavelmente podem! Mas não há razão para que você não saiba o que eles estão fazendo nos bastidores. Na verdade, isso ajudaria todo o processo se você soubesse quando entrar com informações e o que procurar quando eles disserem: "Você pode me enviar a chave de API e o endpoint da API?".

Então, o que eles estão fazendo quando integram o Braze ao seu app ou site? Que bom que você perguntou!

### Etapa 1: Eles implementam o SDK do Braze

É por meio do SDK (kit de desenvolvimento de software) da Braze que trocamos informações com seu app ou site. Seus engenheiros estão, essencialmente, unindo nossos apps. Para isso, eles precisam de algumas informações importantes:

* Suas [chaves de API]({{site.baseurl}}/api/api_key/)
* Seu [endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * A Braze não fornece mais endpoints personalizados, portanto, use os endpoints predefinidos do SDK. Se você tiver recebido um endpoint personalizado pré-existente, Aqui, você pode encontrar as etapas de configuração envolvidas para integração [com Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) e [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk).

Você pode fornecer essas informações diretamente a eles ou dar-lhes acesso à Braze criando uma conta para eles. 

{% alert warning %}
Certifique-se de que você e seus desenvolvedores não alterem as credenciais da empresa no Braze sem saber ou sem querer, pois isso pode causar problemas durante o processo de implementação ou bloquear uma ou mais contas.
{% endalert %}

### Etapa 2: Eles implementam seus canais de envio de mensagens desejados

O Braze tem muitas opções para entrar em contato com seus usuários, e cada uma delas requer sua própria configuração ou ajuste para funcionar da maneira que você deseja. É nesse ponto que a comunicação com seus engenheiros se torna fundamental.

Não se esqueça de informar aos desenvolvedores quais canais você quer usar para garantir que a implementação seja feita de forma eficiente e na ordem correta.

| Canal | Informações |
|---|---|
| Mensagem no app | Requer a implementação do SDK, bem como essas etapas específicas do canal. |
| Push | Requer a implementação do SDK para fornecer o tratamento adequado das credenciais de envio de mensagens e tokens por push. |
| E-mail | Esse é um processo totalmente diferente. Consulte a seção [Configuração de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/) para obter mais detalhes sobre a integração. |
| Cartões de conteúdo | Para começar a usar [os cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), entre em contato com o gerente de sucesso do cliente da Braze. |
| SMS E MMS | Consulte a seção [Configuração de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/) para obter mais detalhes sobre a integração. |
| Webhooks | Requer a implementação do SDK, bem como etapas específicas do canal. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Você pode usar o Braze para criar campanhas de envio de mensagens acessíveis em cada canal. Trabalhe com seus desenvolvedores para garantir que você atenda aos padrões de acessibilidade em sua implementação.
{% endalert %}

### Etapa 3: Eles configuram seus dados

A Braze é versátil. Não se trata apenas de enviar e-mails ou push. Trata-se de criar jornadas de clientes personalizadas e exclusivas para cada usuário e cliente. As jornadas do cliente são baseadas em suas ações dentro de seu app ou site, e você pode definir quais são elas! A próxima tarefa de seus desenvolvedores é garantir que as ações realizadas em seu app ou site sejam captadas pelo Braze.

Então, o que você precisa fazer para obter essas informações?

1. Trabalhe com sua equipe de marketing para definir campanhas, metas, atribuições e eventos que precisam ser rastreados. Defina esses casos de uso e compartilhe-os com suas equipes.
2. Defina seus requisitos de dados personalizados[(atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/), etc.).
3. A partir daí, discuta como esses dados devem ser rastreados (disparados por meio do SDK, etc.).
4. Defina quantos [espaços de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/) você precisa. Seus engenheiros precisarão saber como [testar e configurar]({{site.baseurl}}/user_guide/getting_started/workspaces/) esses espaços de trabalho.

Depois de descobrir todas essas informações, compartilhe-as com seu engenheiro. Eles pegarão essas informações e implementarão seus [dados personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/). Talvez seja necessário [importar alguns usuários]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/). Você também deve estar ciente das [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

### Etapa 4: Eles personalizam com base no que você deseja

Se quiser coisas como lançamentos disparados por API e Connected Content, discuta isso com seu contato no Braze e com seus desenvolvedores para garantir que será possível obter dados que estão fora do seu app e do Braze em suas mensagens.

### Etapa 5: Ambos realizam o controle de qualidade em sua implementação

Trabalhe em conjunto com seu engenheiro para garantir que tudo esteja funcionando. Envie [mensagens de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/), use nossos [aplicativos de teste para Android]({{site.baseurl}}/developer_guide/references/?tab=android) e [aplicativos de teste para iOS]({{site.baseurl}}/developer_guide/references/?tab=swift), verifique todas as caixas antes de começar a enviar!

Temos até instruções específicas para [testar sua integração com o Android ou FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) e testar o [push para iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing/).

## Após a implementação

Tenha em mente que a linha de chegada da implementação não é também o sinal verde para o envio de um milhão de mensagens de uma só vez. O envio de um milhão de push pode quebrar seu app se todos os clientes clicarem no mesmo link simultaneamente. Recomendamos que você discuta qual é a capacidade de sua configuração interna para lidar com solicitações do Braze antes de clicar no botão **Enviar**. Em seguida, você pode definir seu [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) com base nisso.

![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Depois de se sentir confortável usando a Braze, considere a possibilidade de se tornar um Braze Firebrand! Com o Braze Firebrands, nossa comunidade de engajamento de clientes, estamos construindo uma comunidade de pessoas que se movimentam e agitam usando o Braze para modernizar a experiência e o marketing de seus clientes. Quer saber mais? [Registre-se agora](https://brazefirebrands.splashthat.com/).
