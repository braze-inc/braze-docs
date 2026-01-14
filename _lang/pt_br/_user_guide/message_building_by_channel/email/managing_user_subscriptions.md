---
nav_title: Assinaturas de e-mail
article_title: Assinaturas de e-mail
page_order: 6
description: "Este artigo de referência aborda os diferentes estados de assinatura do usuário, como criar e gerenciar grupos de assinatura e como segmentar usuários com base em suas assinaturas."
channel:
  - email

---

# Assinaturas de e-mail

> Saiba mais sobre os diferentes estados de assinatura do usuário, como criar e gerenciar grupos de assinatura e como segmentar usuários com base em suas assinaturas.

Este documento é apenas para fins informativos. Ele não tem a intenção de fornecer, nem pode ser considerado como aconselhamento jurídico em qualquer capacidade. O envio de e-mails de marketing e transacionais pode estar sujeito a requisitos legais específicos. Para garantir que esteja fazendo isso em conformidade com todas as leis, regras e regulamentos aplicáveis específicos da sua empresa, procure a orientação do seu consultor jurídico e/ou da equipe de conformidade regulamentar.

## Estados de assinatura {#subscription-states}

O Braze tem três estados de assinatura global para usuários de e-mail (listados na tabela a seguir), que são os guardiões finais entre suas mensagens e seus usuários. Por exemplo, os usuários que são considerados `unsubscribed` não receberão mensagens direcionadas ao estado de assinatura global de `subscribed` ou `opted-in`.

| Estado | Definição |
| ----- | ---------- |
| Aceitação | Um usuário confirmou explicitamente que deseja receber e-mails. Recomendamos um processo de opt-in explícito para obter o consentimento dos usuários para o envio de e-mails. |
| Assinatura | Um usuário não cancelou a assinatura nem optou explicitamente por receber e-mails. Esse é o estado padrão da assinatura quando um perfil de usuário é criado. |
| Cancelamento da inscrição | Um usuário cancelou explicitamente a assinatura de seus e-mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
O Braze não conta as alterações de estado da assinatura em relação aos seus pontos de dados, globalmente, e em torno dos grupos de assinatura.
{% endalert %}

### Endereços de e-mail não assinados

O Braze cancelará automaticamente a assinatura de qualquer usuário que cancelar manualmente a assinatura do seu e-mail por meio de um [rodapé personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Se o usuário atualizar o endereço de e-mail e a opção **Resubscribe users when they update their email** estiver ativada nas definições **de configuração de envio**, o envio normal de e-mails será retomado.

Se um usuário tiver marcado um ou mais de seus e-mails como spam, o Braze só enviará e-mails transacionais a esse usuário. Nesse caso, os e-mails transacionais se referem à opção **Send to all users including unsubscribed users (Enviar para todos os usuários, inclusive usuários não inscritos** ) selecionada na etapa **Target Audience (Público-alvo** ).

{% alert tip %}
Consulte nossas práticas recomendadas [de aquecimento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) para obter orientação sobre como reengajar seus usuários de forma eficaz.
{% endalert %}

### Bounces e e-mails inválidos

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Quando um endereço de e-mail sofre hard bounce, o estado da assinatura do usuário não é automaticamente definido como "cancelado". Se um endereço de e-mail sofrer hard bounces (como quando um e-mail é inválido ou não existe), marcaremos o endereço de e-mail do usuário como inválido e não tentaremos enviar mais e-mails para esse endereço de e-mail. Se esse usuário alterar seu endereço de e-mail, voltaremos a enviar e-mails para ele, pois o novo e-mail pode ser válido. Os soft bounces são automaticamente tentados novamente por 72 horas.

### Atualização dos estados de assinatura de e-mail

Há quatro maneiras de atualizar o estado da assinatura de e-mail de um usuário:

#### Integração de SDK

Use o SDK do Braze para atualizar o estado da assinatura de um usuário.

#### API REST

Use o [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar o [atributo`email_subscribe` ]({{site.baseurl}}/api/objects_filters/user_attributes_object) de um determinado usuário.

#### Perfil do usuário

1. Localize o usuário por meio de **Search Users**. 
2. Na guia **Envolvimento**, selecione os botões **Não inscrito**, **Inscrito** ou Optou **por participar** para alterar o status de inscrição do usuário. 

Se disponível, o perfil do usuário também exibe um registro de data e hora de quando a assinatura do usuário foi alterada pela última vez.

#### Centro de preferências

O [centro de preferências](#email-preference-center) Liquid pode ser incluído na parte inferior dos seus e-mails, permitindo que os usuários optem por receber ou não os e-mails. O Braze gerencia as atualizações do estado da assinatura a partir do centro de preferências.

### Verificação do estado da assinatura de e-mail

Perfil de usuário para John Doe com o estado de assinatura de e-mail definido como Subscribed (Inscrito).]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Há duas maneiras de verificar o estado da assinatura de e-mail de um usuário com o Braze:

1. **Exportação da API REST:** Use os pontos de extremidade [Exportar usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Exportar usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para exportar perfis de usuários individuais no formato JSON.
2. **Perfil do usuário:** Localize o perfil do usuário na página [Pesquisar usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) e, em seguida, selecione a guia **Envolvimento** para visualizar e atualizar manualmente o estado da assinatura de um usuário.

Quando um usuário atualizar seu endereço de e-mail, seu estado de assinatura será definido como inscrito, a menos que o endereço de e-mail atualizado já exista em outro lugar em um espaço de trabalho do Braze.

## Grupos de assinatura

Os grupos de assinatura são filtros de segmento que podem restringir ainda mais seu público-alvo a partir dos [estados de assinatura global](#subscription-states). Você pode adicionar até 350 grupos de assinatura por espaço de trabalho. Esses grupos permitem que você apresente opções de assinatura mais granulares para os usuários finais.

Por exemplo, suponha que você envie várias categorias de campanhas de e-mail (promocionais, boletins informativos ou atualizações de produtos). Nesse caso, você pode usar grupos de assinatura para permitir que seus clientes escolham quais categorias de e-mail desejam assinar ou cancelar a assinatura em massa a partir de uma única página, usando um [centro de preferências de e-mail](#email-preference-center). Como alternativa, você pode usar grupos de assinatura para permitir que seus clientes escolham a frequência com que desejam receber seus e-mails, criando grupos de assinatura para e-mails diários, semanais ou mensais.

Use os [pontos de extremidade do Grupo de Assinatura]({{site.baseurl}}/api/endpoints/subscription_groups) para gerenciar programaticamente os grupos de assinatura que você armazenou no painel do Braze na página **Grupo de Assinatura**.

### Criação de um grupo de assinaturas

1. Vá para **Audience** > **Gerenciamento de grupos de assinatura**.
2. Selecione **Criar grupo de assinatura de e-mail**. 
3. Dê um nome e uma descrição ao seu grupo de assinaturas.
4. Selecione **Salvar**. 

Todos os grupos de assinatura são adicionados automaticamente à sua central de preferências.

\![Campos para criar um grupo de assinaturas.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentação com um grupo de assinaturas

Ao criar seus segmentos, defina o nome do grupo de assinatura como um filtro. Isso confirmará que os usuários que optaram por participar do seu grupo receberão seus e-mails. Isso é ótimo para boletins informativos mensais, cupons, níveis de associação e muito mais.

Exemplo de segmentação de usuários no segmento "Lapsed Users" com o filtro para usuários no grupo de assinatura "Weekly Emails".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Arquivamento de grupos de assinaturas

Os grupos de assinatura arquivados não podem ser editados e não aparecerão mais nos filtros de segmento ou em seu centro de preferências. Se você tentar arquivar um grupo que esteja sendo usado como filtro de segmento em qualquer e-mail, campanha ou Canvas, receberá uma mensagem de erro que o impedirá de arquivar o grupo até que você remova todos os usos dele.

Para arquivar seu grupo na página **Grupos de assinatura**, faça o seguinte:

1. Localize seu grupo na lista de grupos de assinatura. 
2. Selecione **Archive (Arquivo** ) no menu suspenso <i class="fa-solid fa-ellipsis-vertical"></i>.

O Braze não processará nenhuma alteração de estado para usuários em grupos arquivados. Por exemplo, se você arquivar o Grupo de Assinatura 1 enquanto Susie estiver inscrita nele, ela permanecerá "inscrita" nesse grupo, mesmo que clique em um link de cancelamento de assinatura (isso não deve importar para Susie porque o Grupo de Assinatura 1 está arquivado e você não pode enviar nenhuma mensagem usando-o).

#### Visualização do tamanho dos grupos de assinaturas

Você pode fazer referência ao gráfico **Série temporal do grupo de** assinatura na página **Grupos de assinatura** para visualizar o tamanho do grupo de assinatura com base no número de usuários em um período de tempo. Esses tamanhos de grupos de assinatura também são consistentes com outras áreas do Braze, como o cálculo do tamanho do segmento.

Um exemplo de gráfico "Subscription Group Timeseries" datado de 2 a 11 de dezembro. O gráfico mostra um aumento de aproximadamente 10 milhões no número de usuários do 6º para o 7º dia.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Exibição de grupos de assinatura na análise de campanhas

Você pode ver o número de usuários que alteraram o estado da assinatura (assinaram ou cancelaram a assinatura) de uma campanha de e-mail específica na página de análise dessa campanha.

1. Na página **Campaign Analytics** da sua campanha, role para baixo até a seção **Email Message Performance (Desempenho da mensagem de e-mail** ).
2. Selecione a seta em **Subscription Groups** para ver a contagem agregada de alterações de estado, conforme enviadas por seus clientes.

A página "Desempenho de mensagens de e-mail" exibe a contagem agregada de alterações de estado enviadas pelos clientes.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Verificação do grupo de assinatura de e-mail de um usuário

- **Perfil do usuário:** Os perfis de usuários individuais podem ser acessados por meio do painel de controle do Braze na página [Pesquisar usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Aqui, você pode procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Você também pode visualizar os grupos de assinatura de e-mail de um usuário na guia **Envolvimento**.
- **API REST do Braze:** Use o [ponto de extremidade Listar grupos de assinatura do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou o [ponto de extremidade Listar status do grupo de assinatura do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para visualizar os grupos de assinatura de perfis de usuários individuais. 

## Centro de preferências de e-mail

O centro de preferências de e-mail é uma maneira fácil de gerenciar quais usuários recebem determinados grupos de boletins informativos e pode ser encontrado no painel em **Subscription Groups (Grupos de assinaturas**). Cada grupo de assinatura que você cria é adicionado à lista do centro de preferências. 

Para saber mais sobre como adicionar ou personalizar um centro de preferências, consulte [Centro de preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Alteração de assinaturas de e-mail {#changing-email-subscriptions}

Na maioria dos casos, seus usuários gerenciarão a assinatura de e-mail por meio de links de assinatura incluídos nos e-mails que recebem. Você deve inserir um rodapé em conformidade com a lei com um link de cancelamento de assinatura na parte inferior de cada e-mail que enviar. Quando os usuários selecionam o URL de cancelamento de assinatura no rodapé, eles devem ser cancelados e levados a uma página de destino que confirma a alteração da assinatura. Recomendamos incluir esta tag Liquid: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Observe que, quando um usuário seleciona "Unsubscribe from all of the above types of emails" (Cancelar assinatura de todos os tipos de e-mails acima) no centro de preferências de e-mail, isso atualiza o status global da assinatura de e-mail para `unsubscribed` e cancela a assinatura de todos os grupos de assinatura.

### Criação de rodapés personalizados {#custom-footer}

Se não quiser usar o rodapé padrão do Braze em seus e-mails, você poderá criar um rodapé de e-mail personalizado em todo o espaço de trabalho, que poderá ser modelado em cada e-mail usando o atributo {% raw %}`{{${email_footer}}}`{% endraw %} Liquid.

Dessa forma, você não precisa criar um novo rodapé para cada modelo de e-mail ou campanha de e-mail que usar. Para ver as etapas, consulte [Personalizar o rodapé do e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Gerenciamento de estados de assinatura para endereços IP chineses

Se você prevê que seus destinatários de e-mail terão um endereço IP chinês, não deve confiar apenas em um link de cancelamento de assinatura em seu e-mail para manter suas listas `unsubscribed`. Em vez disso, forneça maneiras alternativas para os usuários cancelarem facilmente a assinatura, como abrir um tíquete de suporte por meio do portal de suporte ou enviar um e-mail para um representante do cliente. 

### Criação de uma página de cancelamento de assinatura personalizada

Quando os usuários selecionam um URL de cancelamento de assinatura em um e-mail, eles são levados a uma página de destino padrão que confirma a alteração da assinatura.

Para criar uma página de destino personalizada para a qual os usuários serão direcionados (em vez da página padrão) ao se inscreverem:

1. Vá para **Preferências de e-mail** > **Páginas e rodapés de assinatura**.
2. Forneça o HTML para sua página de destino personalizada. 

Recomendamos incluir um link de reinscrição (como {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) na página de destino para que os usuários tenham a opção de reinscrever-se caso tenham cancelado a assinatura por acidente.

\![Página personalizada de cancelamento de assinatura com uma visualização "Sorry to see you go!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Criação de uma página de opt-in personalizada

Em vez de inscrever imediatamente um usuário em suas campanhas de e-mail, a criação de uma página de opt-in personalizada pode dar aos usuários a oportunidade de reconhecer e controlar suas preferências de notificação. Essa comunicação adicional também pode ajudar suas campanhas de e-mail a ficarem fora da pasta de spam, já que seus usuários terão optado pelo opt-in. 

1. Vá para **Configurações** > **Preferências de e-mail**.
2. Selecione **Subscription Pages and Footers (Páginas de assinatura e rodapés**).
3. Personalize o estilo na seção **Página de opt-in personalizada** para ver como isso indica aos seus usuários que eles foram inscritos.

Os usuários serão direcionados a essa página por meio da tag {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}.

{% alert tip %}
Braze recomenda o uso de um processo de opt-in duplo para ajudar no alcance de seus e-mails. Esse processo envia um e-mail de confirmação adicional em que o usuário confirma suas preferências de notificação novamente por meio de um link no e-mail. Nesse momento, o usuário é considerado opt-in.
{% endalert %}

\![E-mail personalizado de opt-in com a mensagem "Fico feliz em ver que você ainda quer receber notícias nossas".]({% image_buster /assets/img/custom_optin.png %})

## Assinaturas e direcionamento de campanhas {#subscriptions-and-campaign-targeting}

Por padrão, as campanhas com mensagens push ou de e-mail são direcionadas aos usuários que estão inscritos ou optaram por participar por padrão. Você pode alterar essa preferência de segmentação ao editar uma campanha, indo para a etapa **Público-alvo** e selecionando o menu suspenso ao lado de **Enviar para estes usuários:**.

O Braze suporta três estados de direcionamento:

- Usuários que estão inscritos ou optaram por participar (padrão).
- Somente usuários que optaram por participar.
- Todos os usuários, inclusive aqueles que cancelaram a assinatura.

{% alert important %}
É sua responsabilidade cumprir todas as [leis de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) aplicáveis ao usar essas configurações de direcionamento.
{% endalert %}

## Segmentação por assinaturas de usuários {#segmenting-by-user-subscriptions}

Os filtros "Email Subscription Status" (Status da assinatura por e-mail) e "Push Subscription Status" (Status da assinatura por push) permitem segmentar os usuários pelo status da assinatura.

Isso pode ser útil se você quiser segmentar usuários que não optaram nem por receber nem por não receber e incentivá-los a optar explicitamente por receber e-mail ou push. Nesse caso, você criaria um segmento com um filtro para "Email/Push Subscription Status is Subscribed" e as campanhas para esse segmento seriam direcionadas aos usuários que estão inscritos, mas não optaram por participar.

Status de assinatura de e-mail usado como um filtro de segmento.]({% image_buster /assets/img_archive/not_optin.png %})

