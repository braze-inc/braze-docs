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

O Braze tem três estados globais de inscrição para usuários de e-mail (listados na tabela a seguir), que são os guardiões finais entre suas mensagens e seus usuários. Por exemplo, os usuários considerados `unsubscribed` não receberão mensagens direcionadas ao estado de inscrição global de `subscribed` ou `opted-in`.

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

Se um usuário tiver marcado um ou mais de seus e-mails como spam, o Braze só enviará e-mails de transação para esse usuário. Neste caso, e-mails transacionais referem-se à opção selecionada **Enviar para todos os usuários, incluindo usuários cancelados** na etapa **Público-alvo**.

{% alert tip %}
Consulte nossas práticas recomendadas [de aquecimento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) para obter orientação sobre como reengajar seus usuários de forma eficaz.
{% endalert %}

### Bounces e e-mails inválidos

{% multi_lang_include metrics.md metric='Hard Bounce' %} {% multi_lang_include metrics.md metric='soft bounce' %} 

Quando um endereço de e-mail retorna como inválido, o estado de inscrição do usuário não é automaticamente definido como "cancelado". Se um endereço de e-mail retornar como inválido (como quando um e-mail é inválido ou não existe), marcaremos o endereço de e-mail do usuário como inválido e não tentaremos enviar mais e-mails para esse endereço de e-mail. Se esse usuário alterar seu endereço de e-mail, voltaremos a enviar e-mails para ele, pois o novo e-mail pode ser válido. Os soft bounces são automaticamente tentados novamente por 72 horas.

### Atualização dos estados de envio de e-mail

Há quatro maneiras de atualizar o estado da inscrição de e-mail de um usuário:

#### integração de SDK

Use o SDK da Braze para atualizar o estado da inscrição de um usuário.

#### API REST

Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar o [atributo `email_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) para um determinado usuário.

#### Perfil do usuário

1. Localize o usuário em **Pesquisar usuários**. 
2. Na guia **Engajamento**, selecione os botões **Cancelou inscrição**, **Inscrito** ou **Optado** para alterar o status de inscrição desse usuário. 

Se disponível, o perfil do usuário também exibe um carimbo de data/hora de quando a inscrição do usuário foi alterada pela última vez.

#### Central de Preferências

A [Central de Preferências](#email-preference-center) Liquid pode ser incluída na parte inferior de seus e-mails, permitindo que os usuários aceitem ou não receber e-mails. O Braze gerencia as atualizações do estado da inscrição a partir da central de preferências.

### Verificação do estado do envio de e-mail

![Perfil do usuário para John Doe com seu estado de inscrição de e-mail definido como Inscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Há duas maneiras de verificar o estado da inscrição de e-mail de um usuário no Braze:

1. **Exportação da API REST:** Use os endpoints [Exportar usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Exportar usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para exportar perfis de usuários individuais em formato JSON.
2. **Perfil do usuário:** Encontre o perfil do usuário na página [Pesquisar usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/), em seguida, selecione a guia **Engajamento** para visualizar e atualizar manualmente o estado de inscrição de um usuário. 

Quando um usuário atualizar seu endereço de e-mail, seu estado de inscrição será definido como inscrito, a menos que o endereço de e-mail atualizado já exista em outro lugar em um espaço de trabalho Braze.

## Grupos de inscrições

Os grupos de inscrições são filtros de segmento que podem restringir ainda mais seu público a partir dos [estados de inscrição globais](#subscription-states). Você pode adicionar até 350 grupos de inscrição por espaço de trabalho. Esses grupos permitem que você apresente opções de inscrição mais granulares aos usuários finais.

Por exemplo, suponha que você envie várias categorias de campanhas de e-mail (promocionais, boletins informativos ou atualizações de produtos). Nesse caso, é possível usar grupos de inscrições para permitir que seus clientes escolham as categorias de e-mail das quais desejam se inscrever ou cancelar a inscrição em massa a partir de uma única página, usando uma [central de preferências de e-mail](#email-preference-center). Como alternativa, você pode usar grupos de inscrições para permitir que seus clientes escolham a frequência com que desejam receber seus e-mails, criando grupos de inscrições para e-mails diários, semanais ou mensais.

Use os [endpoints de grupo de Inscrições]({{site.baseurl}}/api/endpoints/subscription_groups) para gerenciar programaticamente os grupos de inscrições que você armazenou no painel do Braze para a página do **Grupo de inscrições**.

### Criação de um grupo de inscrições

1. Acesse **Público** > **Inscrições**.
2. Selecione **Criar grupo de inscrições para e-mail**. 
3. Dê um nome e uma descrição ao seu grupo de inscrições.
4. Selecione **Salvar**. 

Todos os grupos de inscrições são adicionados automaticamente à sua Central de Preferências.

![Campos para criar um grupo de inscrições.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentação com um grupo de inscrições

Ao criar seus segmentos, defina o nome do grupo de inscrições como um filtro. Isso confirmará que os usuários que fizeram a aceitação do seu grupo receberão seus e-mails. Isso é ótimo para boletins informativos mensais, cupons, níveis de associação e muito mais.

![Exemplo de direcionamento de usuários no segmento "Usuários Inativos" com o filtro para usuários no grupo de inscrições "Alertas Estáveis".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Arquivamento de grupos de inscrições

Os grupos de inscrições arquivados não podem ser editados e não aparecerão mais nos filtros de segmentos ou em sua Central de Preferências. Se tentar arquivar um grupo que está sendo usado como filtro de segmento em qualquer e-mail, campanha ou Canva, você receberá uma mensagem de erro que o impedirá de arquivar o grupo até que remova todos os usos dele.

Para arquivar seu grupo na página **Grupos de inscrições**, faça o seguinte:

1. Encontre seu grupo na lista de grupos de inscrições. 
2. Selecione **Arquivar** no menu suspenso <i class="fa-solid fa-ellipsis-vertical"></i>.

O Braze não processará nenhuma alteração de estado para usuários em grupos arquivados. Por exemplo, se você arquivar "Grupo de Inscrições A" enquanto Susie estiver inscrita nele, ela permanecerá "inscrita" neste grupo, mesmo que clique em um link de cancelamento de inscrição (isso não deve importar para Susie porque "Grupo de Inscrições A" está arquivado e você não pode enviar mensagens usando-o).

#### Visualização dos tamanhos dos grupos de inscrições

Você pode consultar o gráfico de **Série temporal do grupo de inscrições** na página **Grupos de Inscrições** para visualizar o tamanho do grupo de inscrições com base no número de usuários ao longo de um período de tempo. Esses tamanhos de grupos de inscrições também são consistentes com outras áreas do Braze, como o cálculo do tamanho do segmento.

![Um exemplo de gráfico "grupo de inscrições Timeseries" datado de 2 a 11 de dezembro. O gráfico mostra um aumento de ~10 milhões no número de usuários da 6ª para a 7ª.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Visualização de grupos de inscrições na análise de dados da campanha

É possível ver o número de usuários que alteraram o estado da inscrição (inscritos ou cancelados) em uma campanha de e-mail específica na página de análise de dados dessa campanha.

1. Na página de **Análise de dados de campanha** para sua campanha, role para baixo até a seção **Performance de mensagens de e-mail**.
2. Selecione a seta abaixo de **Grupos de inscrições** para ver a contagem agregada de mudanças de estado, conforme enviado por seus clientes.

![A página "Desempenho da Mensagem de E-mail" exibindo a contagem agregada de mudanças de estado enviadas pelos clientes.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

## Central de Preferências de E-mail

A Central de Preferências de e-mail é uma maneira fácil de gerenciar quais usuários recebem determinados grupos de boletins informativos e pode ser encontrada no dashboard em **Grupos de inscrições**. Cada grupo de inscrições que você cria é adicionado à lista da Central de Preferências. 

Para saber mais sobre como adicionar ou personalizar uma Central de Preferências, consulte [Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Alteração de inscrições de e-mail {#changing-email-subscriptions}

Na maioria dos casos, seus usuários gerenciam a inscrição de e-mail por meio de links de inscrição incluídos nos e-mails que recebem. Você deve inserir um rodapé em conformidade com a lei com um link de cancelamento de inscrição na parte inferior de cada e-mail enviado. Quando os usuários selecionam a URL de cancelamento de inscrição em seu rodapé, eles devem ser cancelados e levados a uma página de destino que confirma a alteração em sua inscrição. Recomendamos incluir esta tag Liquid: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Observe que quando um usuário seleciona "Cancelar inscrição de todos os tipos de e-mail acima" na Central de Preferências de e-mail, isso atualiza seu status de assinatura global de e-mail para `unsubscribed` e cancela a inscrição em todos os grupos de inscrições.

### Criação de rodapés personalizados {#custom-footer}

Se não quiser usar o rodapé padrão do Braze em seus e-mails, você poderá criar um rodapé de e-mail personalizado em todo o espaço de trabalho, que poderá ser modelado em cada e-mail usando o atributo {% raw %}`{{${email_footer}}}`{% endraw %} Liquid.

Dessa forma, você não precisa criar um novo rodapé para cada modelo de e-mail ou campanha de e-mail que usar. Para obter as etapas, consulte [Rodapé de e-mail personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Gerenciamento de estados de inscrição para endereços IP chineses

Se você prevê que seus destinatários de e-mail terão um endereço IP chinês, não deve confiar apenas em um link de cancelamento de inscrição em seu e-mail para manter suas listas `unsubscribed`. Em vez disso, forneça maneiras alternativas para que os usuários cancelem a inscrição facilmente, como abrir um tíquete de suporte por meio do portal de suporte ou enviar um e-mail para um representante do cliente. 

### Criação de uma página de cancelamento de inscrição personalizada

Quando os usuários selecionam uma URL de cancelamento de inscrição em um e-mail, eles são levados a uma página de destino padrão que confirma a alteração em sua inscrição.

Para criar uma landing page personalizada para a qual os usuários serão direcionados (em vez da página padrão) ao se inscreverem:

1. Acesse **Preferências de e-mail** > **Páginas de inscrição e rodapés**.
2. Forneça o HTML para sua landing page personalizada. 

Recomendamos incluir um link de cancelamento de inscrição (como {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) na landing page para que os usuários tenham a opção de cancelar a inscrição caso tenham cancelado por acidente.

![E-mail de cancelamento de inscrição personalizado no painel da Página de Cancelamento de Inscrição Personalizada.]({% image_buster /assets/img/custom_unsubscribe.png %})

### Criação de uma página de aceitação personalizada

Em vez de inscrever imediatamente um usuário em suas campanhas de e-mail, a criação de uma página de aceitação personalizada pode dar aos usuários a oportunidade de reconhecer e controlar suas preferências de notificação. Essa comunicação adicional também pode ajudar suas campanhas de e-mail a ficarem fora da pasta de spam, pois seus usuários terão optado pela aceitação. 

1. Acesse **Configurações** > **Preferências de e-mail**.
2. Selecione **Páginas de inscrição e rodapés**.
3. Personalize o estilo na seção **Página de aceitação personalizada** para ver como isso indica aos seus usuários que eles foram inscritos.

{% alert tip %}
A Braze recomenda o uso de um processo de aceitação dupla para ajudar no envio de e-mail. Esse processo envia um e-mail de confirmação adicional em que o usuário confirma suas preferências de notificação novamente por meio de um link no e-mail. Nesse ponto, o usuário é considerado aceito.
{% endalert %}

## Inscrições e direcionamento de campanhas {#subscriptions-and-campaign-targeting}

Por padrão, campanhas com mensagens push ou de e-mail são direcionadas a usuários que estão inscritos ou que aceitaram por padrão. Você pode alterar essa preferência de direcionamento ao editar uma campanha, acessando a etapa **Público-alvo** e selecionando o menu suspenso ao lado de **Enviar para esses usuários:**.

A Braze oferece suporte a três estados de direcionamento:

- Usuários inscritos ou com aceitação (padrão).
- Somente usuários com aceitação.
- Todos os usuários, inclusive aqueles que cancelaram a inscrição.

{% alert important %}
É sua responsabilidade cumprir com quaisquer [leis de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) aplicáveis ao usar essas configurações de direcionamento.
{% endalert %}

## Segmentação por inscrições de usuários {#segmenting-by-user-subscriptions}

Os filtros "Status de Inscrição por E-mail" e "Status de Inscrição por Push" permitem segmentar seus usuários pelo status de inscrição.

Isso pode ser útil se você quiser direcionar usuários que não se inscreveram nem se descadastraram e incentivá-los a se inscrever explicitamente para e-mail ou push. Nesse caso, você criaria um segmento com um filtro para "Status de inscrição em e-mail/push" e as campanhas para esse segmento serão direcionadas aos usuários inscritos, mas sem aceitação.

![Status de Inscrição de E-mail usado como um filtro de segmento.]({% image_buster /assets/img_archive/not_optin.png %})

