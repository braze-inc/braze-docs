---
nav_title: Inscrições em e-mail
article_title: Inscrições em e-mail
page_order: 6
description: "Este artigo de referência aborda os diferentes estados de inscrição do usuário, como criar e gerenciar grupos de inscrições e como segmentar usuários com base em suas inscrições."
channel:
  - email

---

# Inscrições em e-mail

> Saiba sobre os estados de inscrição do usuário, como criar e gerenciar grupos de inscrições e como segmentar usuários com base em suas inscrições.

Este documento é apenas para fins informativos. Ele não se destina a fornecer, nem pode ser considerado como aconselhamento jurídico de qualquer tipo. O envio de e-mails de marketing e de transação pode estar sujeito a requisitos legais específicos. Para garantir que esteja fazendo isso em conformidade com todas as leis, regras e regulamentos aplicáveis específicos da sua empresa, procure a orientação do seu consultor jurídico e/ou da equipe de conformidade regulamentar.

## Estados de inscrição {#subscription-states}

A Braze tem três estados globais de inscrição para usuários de e-mail. Esses estados bloqueiam suas mensagens para os usuários. Por exemplo, usuários no estado `unsubscribed` não recebem mensagens direcionadas a `subscribed` ou `opted-in`.

| Status | Definição |
| ----- | ---------- |
| Aceitação | Um usuário confirmou explicitamente que deseja receber e-mails. Recomendamos um processo de aceitação explícita para obter o consentimento dos usuários para o envio de e-mails. |
| Inscreveu-se | Um usuário não cancelou a inscrição nem fez a aceitação explícita para receber e-mails. Esse é o estado padrão da inscrição quando um perfil de usuário é criado. |
| Cancelou inscrição | Um usuário cancelou explicitamente a inscrição em seus e-mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
A Braze não conta as alterações de estado da inscrição em relação aos seus pontos de dados, globalmente e em torno dos grupos de inscrições.
{% endalert %}

### Endereços de e-mail cancelados

A Braze cancela automaticamente a inscrição de qualquer usuário que se descadastre manualmente através de um [rodapé personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Se o usuário atualizar seu endereço de e-mail e **Reinscrever usuários quando atualizarem seu e-mail** estiver ativado em **Configuração de Envio**, o envio normal será retomado.

Se um usuário marcar um ou mais de seus e-mails como spam, a Braze enviará apenas e-mails de transação para esse usuário. E-mails de transação referem-se à opção **Enviar para todos os usuários, incluindo usuários descadastrados** em **Público-Alvo**.

{% alert tip %}
Consulte nossas práticas recomendadas de [aquecimento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) para obter orientação sobre como reengajar seus usuários de forma eficaz.
{% endalert %}

### Bounces e e-mails inválidos

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Quando um endereço de e-mail retorna com hard bounce, a Braze não define automaticamente o estado de inscrição do usuário como "cancelado". Se um endereço retornar com hard bounce (inválido ou inexistente), a Braze o marca como inválido e não tenta novos envios. Se o usuário mudar seu endereço de e-mail, a Braze retoma o envio. A Braze tenta novamente soft bounces por 72 horas.

### Atualização dos estados de inscrição de e-mail

Há quatro maneiras de atualizar o estado da inscrição de e-mail de um usuário:

#### Integração de SDK

Use o SDK da Braze para atualizar o estado da inscrição de um usuário.

#### API REST

Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar o [atributo `email_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) de um usuário. Por exemplo, para definir o estado de inscrição de e-mail de um usuário como cancelado quando ele usa um link de cancelamento de inscrição personalizado, inclua `email_subscribe: "unsubscribed"` nos atributos do usuário na sua solicitação.

#### Perfil de usuário

1. Localize o usuário em **Pesquisar Usuários**. 
2. Em **Engajamento**, selecione **Descadastrado**, **Inscrito** ou **Optou por Receber** para alterar o status de inscrição do usuário. 

Se disponível, o perfil de usuário também exibe um carimbo de data/hora de quando a inscrição do usuário foi alterada pela última vez.

#### Central de Preferências

Inclua [Central de Preferências](#email-preference-center) Liquid no final de seus e-mails para permitir que os usuários optem por entrar ou sair. A Braze gerencia atualizações de estado de inscrição a partir da Central de Preferências.

### Verificação do estado de inscrição de e-mail

![Perfil de usuário para John Doe com o estado de inscrição de e-mail definido como Inscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Você pode verificar o estado de inscrição de e-mail de um usuário das seguintes maneiras:

1. **Exportação da API REST:** Use os endpoints [Exportar usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Exportar usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para exportar perfis de usuários individuais em formato JSON.
2. **Perfil de usuário:** Encontre o perfil do usuário na página [Pesquisar Usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/), em seguida, selecione a guia **Engajamento** para visualizar e atualizar manualmente o estado de inscrição de um usuário.

Quando um usuário atualizar seu endereço de e-mail, seu estado de inscrição será definido como inscrito, a menos que o endereço de e-mail atualizado já exista em outro lugar em um espaço de trabalho da Braze.

## Grupos de inscrições

Os grupos de inscrições são filtros de segmento que podem restringir ainda mais seu público a partir dos [estados de inscrição globais](#subscription-states). Você pode adicionar até 350 grupos de inscrições por espaço de trabalho. Esses grupos permitem que você apresente opções de inscrição mais granulares aos usuários finais.

Por exemplo, suponha que você envie várias categorias de campanhas de e-mail (promocionais, newsletters ou atualizações de produtos). Nesse caso, é possível usar grupos de inscrições para permitir que seus clientes escolham as categorias de e-mail das quais desejam se inscrever ou cancelar a inscrição em massa a partir de uma única página, usando uma [Central de Preferências de e-mail](#email-preference-center). Como alternativa, você pode usar grupos de inscrições para permitir que seus clientes escolham a frequência com que desejam receber seus e-mails, criando grupos de inscrições para e-mails diários, semanais ou mensais.

Use os [endpoints de grupo de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups) para gerenciar programaticamente os grupos de inscrições que você armazenou no dashboard da Braze na página **Grupo de Inscrições**.

### Criação de um grupo de inscrições

1. Acesse **Público** > **Gerenciamento de Grupos de Inscrição**.
2. Selecione **Criar grupo de inscrições para e-mail**. 
3. Dê um nome e uma descrição ao seu grupo de inscrições.
4. Selecione **Salvar**. 

Todos os grupos de inscrições são adicionados automaticamente à sua Central de Preferências.

![Campos para criar um grupo de inscrições.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentação com um grupo de inscrições

Ao criar seus segmentos, defina o nome do grupo de inscrições como um filtro. Isso confirmará que os usuários que fizeram a aceitação do seu grupo receberão seus e-mails. Isso é ótimo para newsletters mensais, cupons, níveis de associação e muito mais.

![Exemplo de direcionamento de usuários no segmento "Usuários Inativos" com o filtro para usuários no grupo de inscrições "E-mails Semanais".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Arquivamento de grupos de inscrições

Os grupos de inscrições arquivados não podem ser editados e não aparecerão mais nos filtros de segmentos ou na sua Central de Preferências. Se tentar arquivar um grupo que está sendo usado como filtro de segmento em qualquer e-mail, campanha ou Canvas, você receberá uma mensagem de erro que o impedirá de arquivar o grupo até que remova todos os usos dele.

Para arquivar seu grupo na página **Grupos de Inscrições**, faça o seguinte:

1. Encontre seu grupo na lista de grupos de inscrições. 
2. Selecione **Arquivar** no menu suspenso <i class="fa-solid fa-ellipsis-vertical"></i>.

A Braze não processa mudanças de estado para usuários em grupos arquivados. Por exemplo, se você arquivar o Grupo de Inscrições 1 enquanto Alex está inscrito nele, Alex permanece "inscrito" mesmo que clique em um link de cancelamento de inscrição. Isso não importa porque o Grupo de Inscrições 1 está arquivado e você não pode enviar mensagens usando-o.

#### Visualização dos tamanhos dos grupos de inscrições

Você pode consultar o gráfico de **Série Temporal do Grupo de Inscrições** na página **Grupos de Inscrições** para visualizar o tamanho do grupo de inscrições com base no número de usuários ao longo de um período de tempo. Esses tamanhos de grupos de inscrições também são consistentes com outras áreas da Braze, como o cálculo do tamanho do segmento.

![Um exemplo de gráfico "Série Temporal do Grupo de Inscrições" datado de 2 a 11 de dezembro. O gráfico mostra um aumento de ~10 milhões no número de usuários do dia 6 para o dia 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Visualização de grupos de inscrições na análise de dados da campanha

Você pode ver a contagem de usuários que mudaram seu estado de inscrição (inscrito ou cancelado) de uma campanha de e-mail específica na página de análise de dados dessa campanha.

1. Na página de **Análise de Dados da Campanha** para sua campanha, role para baixo até a seção **Performance de Mensagens de E-mail**.
2. Selecione a seta abaixo de **Grupos de Inscrições** para ver a contagem agregada de mudanças de estado, conforme enviado por seus clientes.

![A página "Performance de Mensagens de E-mail" exibindo a contagem agregada de mudanças de estado enviadas pelos clientes.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Verificando o grupo de inscrições de e-mail de um usuário

- **Perfil de usuário:** Os perfis de usuários individuais podem ser acessados por meio do dashboard da Braze na página [Pesquisar Usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Aqui, é possível procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Você também pode visualizar os grupos de inscrições de e-mail de um usuário na guia **Engajamento**.
- **API REST da Braze:** Use o [endpoint Listar grupos de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou o [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para visualizar os grupos de inscrições do perfil de um usuário individual. 

## Central de Preferências de e-mail

A Central de Preferências de e-mail permite que você gerencie quais usuários recebem newsletters dos grupos de inscrições. Encontre-a no dashboard em **Grupos de Inscrições**. Cada grupo de inscrições que você cria é adicionado à lista da Central de Preferências. 

Para saber mais sobre como adicionar ou personalizar uma Central de Preferências, consulte [Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Alteração de inscrições de e-mail {#changing-email-subscriptions}

Na maioria dos casos, os usuários gerenciam sua inscrição de e-mail através de links incluídos nos e-mails que recebem. Insira um rodapé legalmente compatível com um link de cancelamento de inscrição na parte inferior de cada e-mail. Quando os usuários selecionam a URL de cancelamento de inscrição, a Braze cancela a inscrição deles e mostra uma landing page confirmando a mudança. Inclua esta Liquid tag: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Quando um usuário seleciona "Cancelar inscrição de todos os tipos de e-mails acima" na Central de Preferências, a Braze define seu status global de inscrição de e-mail como `unsubscribed` e o cancela de todos os grupos.

### Criação de rodapés personalizados {#custom-footer}

Se você não quiser usar o rodapé padrão, crie um rodapé de e-mail personalizado para todo o espaço de trabalho e use-o como modelo em cada e-mail com {% raw %}`{{${email_footer}}}`{% endraw %}.

Isso permite que você evite criar um novo rodapé para cada modelo de e-mail ou campanha de e-mail. Para ver as etapas, consulte [Rodapé de e-mail personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Gerenciamento de estados de inscrição para endereços IP chineses

Se você antecipar endereços IP chineses, não confie apenas em um link de cancelamento de inscrição para manter listas de `unsubscribed`. Forneça caminhos alternativos de cancelamento de inscrição, como um ticket de suporte ou e-mail de representante do cliente. 

### Criação de uma página de cancelamento de inscrição personalizada

Quando os usuários selecionam uma URL de cancelamento de inscrição, a Braze mostra uma landing page padrão confirmando a mudança.

Para criar uma landing page personalizada (em vez da padrão) exibida após a inscrição:

1. Acesse **Preferências de E-mail** > **Páginas de Inscrição e Rodapés**.
2. Forneça o HTML para sua landing page personalizada. 

Inclua um link de reinscrição (como {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) para que os usuários possam se reinscrever caso tenham cancelado a inscrição por acidente.

![Página de cancelamento de inscrição personalizada com uma prévia "Lamentamos vê-lo partir!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Criação de uma página de aceitação personalizada

Use uma página de aceitação personalizada para permitir que os usuários reconheçam e controlem as preferências de notificação antes da inscrição. Essa comunicação adicional pode ajudar as campanhas de e-mail a não irem para pastas de spam.

1. Acesse **Configurações** > **Preferências de E-mail**.
2. Selecione **Páginas de Inscrição e Rodapés**.
3. Personalize o estilo na seção **Página de aceitação personalizada** para ver como isso indica aos seus usuários que eles foram inscritos.

Os usuários acessam esta página através da tag {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}.

{% alert tip %}
Use um processo de dupla aceitação para melhorar o alcance. A Braze envia um e-mail de confirmação adicional onde o usuário confirma as preferências de notificação através de um link. Após a confirmação, a aceitação do usuário é registrada.
{% endalert %}

![E-mail de aceitação personalizado com a mensagem "Ficamos felizes em ver que você ainda quer ouvir de nós".]({% image_buster /assets/img/custom_optin.png %})

## Inscrições e direcionamento de campanhas {#subscriptions-and-campaign-targeting}

Por padrão, a Braze direciona campanhas com mensagens push ou e-mail para usuários que estão inscritos ou com aceitação. Altere isso em **Público-Alvo** selecionando o dropdown ao lado de **Enviar para esses usuários:**.

A Braze oferece suporte a três estados de direcionamento:

- Usuários inscritos ou com aceitação (padrão).
- Somente usuários com aceitação.
- Todos os usuários, inclusive aqueles que cancelaram a inscrição.

{% alert important %}
É sua responsabilidade cumprir quaisquer [leis de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) aplicáveis ao usar essas configurações de direcionamento.
{% endalert %}

## Segmentação por inscrições de usuários {#segmenting-by-user-subscriptions}

Use os filtros "Status de Inscrição por E-mail" e "Status de Inscrição por Push" para segmentar usuários por status de inscrição.

Use isso para direcionar usuários que não fizeram aceitação nem cancelaram e incentivar uma aceitação explícita. Crie um segmento com o filtro "Status de Inscrição por E-mail/Push é Inscrito" e envie campanhas para usuários que estão inscritos, mas não com aceitação.

![Status de inscrição de e-mail usado como um filtro de segmento.]({% image_buster /assets/img_archive/not_optin.png %})