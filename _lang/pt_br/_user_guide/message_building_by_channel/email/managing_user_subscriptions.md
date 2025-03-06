---
nav_title: Inscrições em e-mail
article_title: Inscrições em e-mail
page_order: 6
description: "Este artigo de referência aborda os diferentes estados de inscrição do usuário, como criar e gerenciar grupos de inscrições e como segmentar usuários com base em suas inscrições."
channel:
  - email

---

# Inscrições em e-mail

> Saiba mais sobre os diferentes estados de inscrição do usuário, como criar e gerenciar grupos de inscrições e como segmentar usuários com base em suas inscrições.

Este documento é apenas para fins informativos. Ele não se destina a fornecer, nem pode ser considerado como aconselhamento jurídico de qualquer tipo. O envio de e-mails de marketing e transação pode estar sujeito a requisitos legais específicos. Para garantir que esteja fazendo isso em conformidade com todas as leis, regras e regulamentos aplicáveis específicos da sua empresa, procure a orientação do seu consultor jurídico e/ou da equipe de conformidade regulamentar.

## Estados de inscrição {#subscription-states}

A Braze tem três estados de inscrição global para usuários de e-mail (listados na tabela a seguir), que são o guardião final entre suas mensagens e seus usuários. Por exemplo, os usuários considerados `unsubscribed` não receberão mensagens direcionadas ao estado de inscrição global de `subscribed` ou `opted-in`.

| Status | Definição |
| ----- | ---------- |
| Aceitação | Um usuário confirmou explicitamente que deseja receber e-mails. Recomendamos um processo de aceitação explícita para obter o consentimento dos usuários para o envio de e-mails. |
| Inscreveu-se | Um usuário não cancelou a inscrição nem fez a aceitação explícita para receber e-mails. Esse é o estado padrão da inscrição quando um perfil de usuário é criado. |
| Cancelou inscrição | Um usuário cancelou explicitamente a inscrição em seus e-mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
A Braze não conta as alterações de estado da inscrição em relação aos seus pontos de dados, globalmente, e em torno dos grupos de inscrições.
{% endalert %}

### Endereços de e-mail cancelados

O Braze cancelará automaticamente a inscrição de qualquer usuário que tenha cancelado manualmente o envio de seu e-mail por meio de um [rodapé personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Se o usuário atualizar seu endereço de e-mail e a opção **Resubscribe users when they update their email** estiver ativada nas definições **de Sending Configuration**, o envio normal de e-mail será retomado.

Se um usuário tiver marcado um ou mais de seus e-mails como spam, o Braze só enviará e-mails de transação para esse usuário. Nesse caso, os e-mails de transação referem-se à opção **Send to all users including unsubscribed users (Enviar para todos os usuários, inclusive usuários com inscrição cancelada** ) selecionada na etapa **Target Audience (Público-alvo** ).

{% alert tip %}
Consulte nossas práticas recomendadas [de aquecimento de IP]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) para obter orientação sobre como reengajar seus usuários de forma eficaz.
{% endalert %}

### Bounces e e-mails inválidos

{% multi_lang_include metrics.md metric='Hard Bounce' %} {% multi_lang_include metrics.md metric='soft bounce' %} 

Se esse usuário alterar seu endereço de e-mail, voltaremos a enviar e-mails para ele, pois o novo e-mail pode ser válido. Os soft bounces são automaticamente tentados novamente por 72 horas.

### Atualização dos estados de envio de e-mail

Há quatro maneiras de atualizar o estado da inscrição de e-mail de um usuário:

#### integração de SDK

Use o SDK da Braze para atualizar o estado da inscrição de um usuário.

#### API REST

Use o endpoint [`/users/track`] [users-track] para atualizar o atributo [`email_subscribe`][user_attributes_object] de um determinado usuário.

#### Perfil do usuário

1. Localize o usuário em **Pesquisar usuários**. 
2. Na guia **Engajamento**, clique nos botões **Cancelamento da inscrição**, **Inscrição** ou **Aceitação** para alterar o status da inscrição do usuário. 

Se disponível, o perfil do usuário também exibe um carimbo de data/hora de quando a inscrição do usuário foi alterada pela última vez.

#### Central de Preferências

A [Central de Preferências](#email-preference-center) Liquid pode ser incluída na parte inferior de seus e-mails, permitindo que os usuários aceitem ou não receber e-mails. O Braze gerencia as atualizações do estado da inscrição a partir da central de preferências.

### Verificação do estado do envio de e-mail

![Perfil de usuário para John Doe com o estado de inscrição de e-mail definido como Subscribed (Inscrito).][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Há duas maneiras de verificar o estado da inscrição de e-mail de um usuário no Braze:

1. **Exportação da API REST:** Use os pontos de extremidade [Export users by segment][segment] ou [Export users by identifier][identifier] para exportar perfis de usuários individuais no formato JSON.
2. **Perfil do usuário:** Localize o perfil do usuário na página [Search Users][5] ] e, em seguida, selecione a guia **Engajamento** para visualizar e atualizar manualmente o estado da inscrição de um usuário.

Quando um usuário atualizar seu endereço de e-mail, seu estado de inscrição será definido como inscrito, a menos que o endereço de e-mail atualizado já exista em outro lugar em um espaço de trabalho Braze. É possível exportar perfis de usuários individuais no formato JSON usando os pontos de extremidade [Export users by segment][segment] ou [Export users by identifier][identifier].

## Grupos de inscrições

Os grupos de inscrições são filtros de segmento que podem restringir ainda mais seu público a partir dos [estados de inscrição globais](#subscription-states). Você pode adicionar até 350 grupos de inscrição por espaço de trabalho. Esses grupos permitem que você apresente opções de inscrição mais granulares aos usuários finais.

Por exemplo, suponha que você envie várias categorias de campanhas de e-mail (promocionais, boletins informativos ou atualizações de produtos). Nesse caso, é possível usar grupos de inscrições para permitir que seus clientes escolham as categorias de e-mail das quais desejam se inscrever ou cancelar a inscrição em massa a partir de uma única página, usando uma [central de preferências de e-mail](#email-preference-center). Como alternativa, você pode usar grupos de inscrições para permitir que seus clientes escolham a frequência com que desejam receber seus e-mails, criando grupos de inscrições para e-mails diários, semanais ou mensais.

Use os [Endpoints do grupo de inscrições][25] para gerenciar programaticamente os grupos de inscrições que você armazenou no dashboard do Braze na página **Grupo de inscrições**.

### Criação de um grupo de inscrições

1. Acesse **Público** > **Inscrições**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), essa página está localizada em **Usuários** > **Grupos de inscrições**.
{% endalert %}

{: start="2"}
2\. Selecione **\+ Criar grupo de inscrições para e-mail**.
3\. Dê um nome e uma descrição ao seu grupo de inscrições e clique em **Salvar**. 

Todos os grupos de inscrições são adicionados automaticamente à sua Central de Preferências.

![Campos para criar um grupo de inscrições.][26]{: height="50%" width="50%"}

### Segmentação com um grupo de inscrições

Ao criar seus segmentos, defina o nome do grupo de inscrições como um filtro. Isso confirmará que os usuários que fizeram a aceitação do seu grupo receberão seus e-mails. Isso é ótimo para boletins informativos mensais, cupons, níveis de associação e muito mais.

![GIF de um usuário definindo o nome de um grupo de inscrições como um filtro.][27]{: style="max-width:80%"}

### Arquivamento de grupos de inscrições

Os grupos de inscrições arquivados não podem ser editados e não aparecerão mais nos filtros de segmentos ou em sua Central de Preferências. Se tentar arquivar um grupo que está sendo usado como filtro de segmento em qualquer e-mail, campanha ou Canva, você receberá uma mensagem de erro que o impedirá de arquivar o grupo até que remova todos os usos dele.

Você pode arquivar seu grupo na página **Grupos de inscrições**. Localize seu grupo na lista, clique na engrenagem e selecione **Arquivo** no menu suspenso.

O Braze não processará nenhuma alteração de estado para usuários em grupos arquivados. Por exemplo, se você arquivar o "Grupo de inscrições A" enquanto a Susie estiver `subscribed` nele, ela permanecerá "`subscribed`" nesse grupo, mesmo que clique em um link de cancelamento de inscrição (isso não deve importar para a Susie porque o "Grupo de inscrições A" está arquivado e você não pode enviar nenhuma mensagem para ele).

#### Visualização dos tamanhos dos grupos de inscrições

É possível fazer referência ao gráfico **Série temporal do grupo de** inscrições na página **Grupos de inscrições** para ver o tamanho do grupo de inscrições com base no número de usuários em um período de tempo. Esses tamanhos de grupos de inscrições também são consistentes com outras áreas do Braze, como o cálculo do tamanho do segmento.

![Um exemplo de gráfico "grupo de inscrições Timeseries" datado de 2 a 11 de dezembro. O gráfico mostra um aumento de ~10 milhões no número de usuários da 6ª para a 7ª.][10]

#### Visualização de grupos de inscrições na análise de dados da campanha

É possível ver o número de usuários que alteraram o estado da inscrição (inscritos ou cancelados) em uma campanha de e-mail específica na página de análise de dados dessa campanha.

Na página **Análise de dados** da campanha de sua campanha, role para baixo até a seção **Desempenho de mensagens de e-mail** e clique na seta abaixo de **Grupos de inscrições** para ver a contagem agregada de alterações de estado, conforme enviadas por seus clientes.

![A página "Desempenho da Mensagem de E-mail" exibindo a contagem agregada de mudanças de estado enviadas pelos clientes.][30]

## Central de Preferências de E-mail

A Central de Preferências de e-mail é uma maneira fácil de gerenciar quais usuários recebem determinados grupos de boletins informativos e pode ser encontrada no dashboard em **Grupos de inscrições**. Cada grupo de inscrições que você cria é adicionado à lista da Central de Preferências. Para saber mais sobre como adicionar ou personalizar uma Central de Preferências, consulte [Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/).

## Alteração de inscrições de e-mail {#changing-email-subscriptions}

Na maioria dos casos, seus usuários gerenciam a inscrição de e-mail por meio de links de inscrição incluídos nos e-mails que recebem. Você deve inserir um rodapé em conformidade com a lei com um link de cancelamento de inscrição na parte inferior de cada e-mail enviado. Quando os usuários clicam no URL de cancelamento da inscrição no rodapé, eles devem cancelar a inscrição e ser levados a uma landing page que confirma a alteração da inscrição. Recomendamos incluir esta tag Liquid: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Observe que quando um usuário seleciona "Cancelar inscrição de todos os tipos de e-mail acima" na Central de Preferências de e-mail, isso atualiza seu status de assinatura global de e-mail para `unsubscribed` e cancela a inscrição em todos os grupos de inscrições.

### Criação de rodapés personalizados {#custom-footer}

Se não quiser usar o rodapé padrão do Braze em seus e-mails, você poderá criar um rodapé de e-mail personalizado em todo o espaço de trabalho, que poderá ser modelado em cada e-mail usando o atributo {% raw %}`{{${email_footer}}}`{% endraw %} Liquid.

Dessa forma, você não precisa criar um novo rodapé para cada modelo de e-mail ou campanha de e-mail que usar. Para obter as etapas, consulte [Rodapé de e-mail personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Gerenciamento de estados de inscrição para endereços IP chineses

Se você prevê que seus destinatários de e-mail terão um endereço IP chinês, não deve confiar apenas em um link de cancelamento de inscrição em seu e-mail para manter suas listas `unsubscribed`. Em vez disso, forneça maneiras alternativas para que os usuários cancelem a inscrição facilmente, como abrir um tíquete de suporte por meio do portal de suporte ou enviar um e-mail para um representante do cliente. 

### Criação de uma página de cancelamento de inscrição personalizada

Quando os usuários clicam em um URL de cancelamento de inscrição em um e-mail, eles são levados a uma landing page padrão que confirma a alteração da inscrição.

Para criar uma landing page personalizada para a qual os usuários serão direcionados (em vez da página padrão) após a inscrição, acesse **Preferências de e-mail** > **Páginas de inscrição e rodapés** e forneça o HTML para a sua landing page personalizada. Recomendamos incluir um link de cancelamento de inscrição (como {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) na landing page para que os usuários tenham a opção de cancelar a inscrição caso tenham cancelado por acidente.

![Envio de e-mail de cancelamento de inscrição personalizado no painel Página de cancelamento de inscrição personalizado.][11]

### Criação de uma página de aceitação personalizada

Em vez de inscrever imediatamente um usuário em suas campanhas de e-mail, a criação de uma página de aceitação personalizada pode dar aos usuários a oportunidade de reconhecer e controlar suas preferências de notificação. Essa comunicação adicional também pode ajudar suas campanhas de e-mail a ficarem fora da pasta de spam, pois seus usuários terão optado pela aceitação. 

Acesse **Preferências de e-mail** > **Páginas de inscrição e rodapés** e personalize o estilo na seção **Página de aceitação personalizada** para ver como isso indica aos seus usuários que eles foram inscritos.

{% alert tip %}
A Braze recomenda o uso de um processo de aceitação dupla para ajudar no envio de e-mail. Esse processo envia um e-mail de confirmação adicional em que o usuário confirma suas preferências de notificação novamente por meio de um link no e-mail. Nesse ponto, o usuário é considerado aceito.
{% endalert %}

## Inscrições e direcionamento de campanhas {#subscriptions-and-campaign-targeting}

As campanhas com envio de mensagens push ou de e-mail são direcionadas aos usuários que estão inscritos ou com aceitação por padrão. É possível alterar essa preferência de direcionamento ao editar uma campanha, acessando a etapa **Público-alvo** e clicando no menu suspenso ao lado de **Enviar para estes usuários:**.

A Braze oferece suporte a três estados de direcionamento:

- Usuários inscritos ou com aceitação (padrão).
- Somente usuários com aceitação.
- Todos os usuários, inclusive aqueles que cancelaram a inscrição.

{% alert important %}
É sua responsabilidade cumprir todas as [leis de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) aplicáveis ao usar essas configurações de direcionamento.
{% endalert %}

![Exemplo de direcionamento de público para usuários inscritos ou com aceitação na seção Opções de direcionamento da etapa Público-alvo.][17]

## Segmentação por inscrições de usuários {#segmenting-by-user-subscriptions}

Os filtros `Email Subscription Status` e `Push Subscription Status` permitem segmentar os usuários pelo status da inscrição.

Por exemplo, isso pode ser útil se você quiser direcionar os usuários que não aceitaram nem recusaram e incentivá-los a aceitar explicitamente o envio de e-mail ou push. Nesse caso, você criaria um segmento com um filtro para "Status de inscrição em e-mail/push" e as campanhas para esse segmento serão direcionadas aos usuários inscritos, mas sem aceitação.

![Status da inscrição de e-mail usado como um filtro de segmento.][18]

[10]: {% image_buster /assets/img_archive/subscription_group_graph.png %}
[11]: {% image_buster /assets/img/custom_unsubscribe.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[16]: {% image_buster /assets/img_archive/user-profile-subscription-ui.png %}
[17]: {% image_buster /assets/img_archive/campaign-targeting-subscription-ui.png %}
[18]: {% image_buster /assets/img_archive/not_optin.png %}
[19]: {% image_buster /assets/img_archive/email_settings.png %}
[25]: {{site.baseurl}}/api/endpoints/subscription_groups
[26]: {% image_buster /assets/img/sub_group_create.png %}
[27]: {% image_buster /assets/img/sub_group_use.gif %}
[28]: {{site.baseurl}}/api/endpoints/preference_center/
[29]: {% image_buster /assets/img/user-sub-state-export.png %}
[30]: {% image_buster /assets/img/campaign_analytics_sub_groups.png %}
[users-track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[3]: {% image_buster /assets/img/push_example.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segmento]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
