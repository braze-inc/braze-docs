{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Criando um conjunto de permissões

Use conjuntos de permissões para agrupar permissões relacionadas a áreas ou ações específicas. Você pode aplicar conjuntos de permissões a usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acesse **Configurações** > **Configurações de Permissão**, depois selecione **Criar conjunto de permissões**. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nome|Permissões|
|-----------|----------------|
|Desenvolvedores|"Ver Chaves de API", "Editar Chaves de API", "Ver Grupos Internos", "Editar Grupos Internos", "Ver Registro de Atividade de Mensagens", "Ver Registro de Usuários de Eventos", "Ver identificadores de API", "Ver Dashboard de Uso da API", "Ver Limites da API", "Ver Alertas de Uso da API", "Editar Alertas de Uso da API", "Ver Depurador SDK", "Editar Depurador SDK".|
|Profissionais de Marketing|"Ver Campanhas", "Editar Campanhas", "Arquivar Campanhas", "Ver Canvas", "Editar Canvas", "Arquivar Canvas", "Ver Regras de Limitação de Frequência", "Editar Regras de Limitação de Frequência", "Ver Priorização de Mensagens", "Editar Priorização de Mensagens", "Ver Blocos de Conteúdo", "Ver Feature Flags", "Editar Feature Flags", "Arquivar Feature Flags", "Ver Segmentos", "Editar Segmentos", "Editar Grupo de Controle Global", "Ver Modelos IAM", "Editar Modelos IAM", "Arquivar Modelos IAM", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Arquivar Modelos de E-mail", "Ver Modelos de Webhook", "Editar Modelos de Webhook", "Arquivar Modelos de Webhook", "Ver Modelos de Link de E-mail", "Editar Modelos de Link de E-mail", "Ver Ativos da Biblioteca de Mídia", "Ver Locais", "Editar Locais", "Arquivar Locais", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centrais de Preferências", "Editar Centrais de Preferências", "Editar Relatórios do Dashboard", "Ver Modelos de Banner", "Ver Configurações de Localização", "Usar Operator", "Ver Agentes do Decisioning Studio", "Ver Evento de Conversão do Decisioning Studio".|
|Gerenciamento de Usuários|"Editar Usuários do Dashboard", "Ver Equipes", "Editar Equipes", "Arquivar Equipes".|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Criando uma função

As funções permitem mais estrutura ao agrupar suas permissões personalizadas individuais com os controles de acesso do espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nome da Função | Espaço de trabalho | Permissões  
----------- | ----------- | ---------
| Profissional de Marketing - Marcas de Moda | {::nomarkdown}[DEV] Marca de Moda, [QA] Marca de Moda, [PROD] Marca de Moda {:/} | "Ver Campanhas", "Editar Campanhas", "Arquivar Campanhas", "Ver Canvas", "Editar Canvas", "Arquivar Canvas", "Ver Blocos de Conteúdo", "Editar Blocos de Conteúdo", "Arquivar Blocos de Conteúdo", "Lançar Blocos de Conteúdo", "Ver Feature Flags", "Editar Feature Flags", "Arquivar Feature Flags", "Ver Segmentos", "Editar Segmentos", "Ver Modelos de Banner", "Editar Modelos de Banner", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Ver Ativos da Biblioteca de Mídia", "Editar Ativos da Biblioteca de Mídia", "Excluir Ativos da Biblioteca de Mídia", "Ver Locais", "Editar Locais", "Arquivar Locais", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centrais de Preferências", "Editar Centrais de Preferências". |
| Profissional de Marketing - Marcas de Cuidados com a Pele | {::nomarkdown}[DEV] Marca de Cuidados com a Pele, [QA] Marca de Cuidados com a Pele, [PROD] Marca de Cuidados com a Pele {:/} |"Ver Campanhas", "Editar Campanhas", "Arquivar Campanhas", "Ver Canvas", "Editar Canvas", "Arquivar Canvas", "Ver Blocos de Conteúdo", "Editar Blocos de Conteúdo", "Arquivar Blocos de Conteúdo", "Lançar Blocos de Conteúdo", "Ver Feature Flags", "Editar Feature Flags", "Arquivar Feature Flags", "Ver Segmentos", "Editar Segmentos", "Ver Modelos de Banner", "Editar Modelos de Banner", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Ver Ativos da Biblioteca de Mídia", "Editar Ativos da Biblioteca de Mídia", "Excluir Ativos da Biblioteca de Mídia", "Ver Locais", "Editar Locais", "Arquivar Locais", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centrais de Preferências", "Editar Centrais de Preferências".|
| Gerenciamento de Usuários - Todas as Marcas | {::nomarkdown}[DEV] Marca de Moda, [QA] Marca de Moda, [PROD] Marca de Moda, [DEV] Marca de Cuidados com a Pele, [QA] Marca de Cuidados com a Pele, [PROD] Marca de Cuidados com a Pele {:/} | "Editar Usuários do Dashboard", "Ver Equipes", "Editar Equipes", "Arquivar Equipes"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e funções diferem das Equipes?

{% multi_lang_include permissions.md content="Differences" %}

### Considerações para adicionar permissões de usuário às Equipes

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard da Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho, ou ao adicioná-los a uma Equipe. O botão **Salvar/Atualizar Usuários** pode ficar desativado se as permissões do usuário forem idênticas às que ele já possui no nível do espaço de trabalho. Essa restrição existe porque não há benefício em ter uma Equipe se todos os usuários possuem as mesmas permissões que todo o espaço de trabalho.

Para adicionar um usuário a uma Equipe com sucesso, mantendo as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados

Usuários limitados têm permissões específicas que permitem gerenciar certos aspectos do dashboard da Braze, mas com restrições em comparação com administradores da empresa e administradores de espaço de trabalho.

| Escopo | Descrição |
| --- | --- |
| Permissões | Usuários limitados podem editar as permissões de outros usuários limitados se tiverem a permissão "Editar Usuários do Dashboard". Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, não podem criar ou gerenciar contas de administrador da empresa. |
| Limitações de função | Se um usuário limitado tiver todas as permissões, exceto "Administrador do Espaço de Trabalho", ele ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador do espaço de trabalho. |
| Visibilidade das permissões | Se um usuário limitado tiver a permissão "Editar Usuários do Dashboard" para um espaço de trabalho (como Dev), mas não para outro (como Prod), ele não verá as permissões do espaço de trabalho Prod na página de detalhes dos usuários do dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparando usuários limitados

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do Espaço de Trabalho | Os Administradores do Espaço de Trabalho têm permissões específicas para gerenciar Espaços de Trabalho, mas não têm a mesma autoridade que os Administradores da Empresa. Usuários Limitados podem herdar permissões semelhantes às dos Administradores do Espaço de Trabalho se tiverem as permissões necessárias marcadas. |
| Administrador (Administrador da Empresa) | Os Administradores da Empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro Administrador da Empresa para essa ação. |
| Acesso somente para visualização | Para acessar partes do dashboard, como a página de Campanhas, os usuários devem ter permissões de visualização atribuídas a eles.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erro de acesso limitado

Os usuários podem encontrar mensagens como "Você precisa de permissões de 'Ver Landing Pages' para acessar esta página". Nesses casos, o usuário e o administrador da conta devem verificar se as permissões necessárias foram concedidas. Se sim, tente resolver o problema desativando e reativando as permissões do usuário. 

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Editando as permissões de um usuário

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Configurações** > **Usuários da Empresa** e selecione o nome dele.

![A página "Usuários da Empresa" na Braze mostrando uma tabela de usuários do dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Administrador

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Adicionar, editar, excluir, suspender ou reativar outros [usuários da Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Exportar usuários da Braze como um arquivo CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador** e depois selecione **Atualizar usuário**.

![Os detalhes do usuário selecionado com a caixa de seleção de administrador em foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar a Braze até que você atribua a ele pelo menos uma [permissão em nível de empresa ou em nível de espaço de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gerenciar as seguintes permissões em nível de empresa para um usuário, marque ou desmarque a caixa ao lado da permissão. Quando terminar, selecione **Atualizar usuário**.

|Nome da permissão|Descrição|
|----------|-----------|
|Gerenciar configurações da empresa|Permite que os usuários modifiquem as configurações de permissão e verificação do remetente.|
|Criar e excluir espaços de trabalho|Permite que os usuários criem e excluam espaços de trabalho.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espaço de trabalho

Você pode dar a um usuário diferentes permissões para cada espaço de trabalho ao qual ele pertence na Braze. Para gerenciar as permissões em nível de espaço de trabalho, selecione **Selecionar espaços de trabalho e permissões** e escolha as permissões manualmente ou atribua um [conjunto de permissões ou função]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que você criou anteriormente. Se você precisar dar a um usuário permissões diferentes para diferentes espaços de trabalho, repita este processo quantas vezes forem necessárias. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Permissões**, selecione uma ou mais permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Atribuir acesso de administrador do espaço de trabalho** se desejar dar a eles permissões completas para este espaço de trabalho.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo selecionadas manualmente na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Conjuntos de permissão**, escolha um conjunto de permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo atribuídas por meio de um conjunto de permissões na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Função**, escolha uma função. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo atribuídas por meio de uma função na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportando permissões de usuário

Para baixar uma lista dos seus usuários e suas permissões, acesse **Configurações** > **Usuários da Empresa** e selecione **Exportar Usuários**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

![A página "Usuários da Empresa" na Braze com a opção "Exportar Usuários" em foco.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permissões

| Permissão | Definição |
|-------------------------------------------------|---------------------|
| Ver informações de faturamento                            | Ver detalhes de cobrança |
| Ver atributos personalizados marcados como IPI            | Ver atributos personalizados marcados como IPI |
| Ver IPI                                        | Ver IPI |
| Ver perfis de usuário em conformidade com IPI                | Acessar pesquisa de usuários e visualizar perfis de usuários com IPI ocultada |
| Ver dados de uso                                 | Ver dados de uso |
| Mesclar usuários duplicados                           | Combinar usuários duplicados em um único usuário. As duplicatas são removidas após a mesclagem. |
| Prévia de usuários duplicados                         | Prévia dos perfis de usuário que são duplicatas |
| Ver modelos de Canvas                           | Ver modelos de Canvas |
| Arquivar modelos de Canvas                        | Mover modelos de Canvas para o arquivo |
| Lançar blocos de conteúdo                           | Lançar blocos de conteúdo |
| Lançar Centrais de Preferências                       | Lançar Centrais de Preferências |
| Editar integrações do Currents                      | Criar, atualizar e excluir integrações do Currents |
| Ver integrações do Currents                       | Ver integrações do Currents |
| Ver campanhas                                  | Ver campanhas |
| Editar campanhas                                  | Criar e atualizar campanhas |
| Arquivar campanhas                               | Mover campanhas para o arquivo |
| Lançar campanhas                                | Iniciar, parar, pausar ou retomar campanhas existentes |
| Ver regras de limitação de frequência                    | Ver regras de limitação de frequência |
| Editar regras de limitação de frequência                    | Criar e atualizar regras de limitação de frequência |
| Ver canvas                                   | Ver canvas |
| Editar canvas                                   | Criar e atualizar canvas |
| Arquivar canvas                                | Mover canvas para o arquivo |
| Lançar canvas                                 | Iniciar, parar, pausar ou retomar canvas existentes |
| Ver blocos de conteúdo                             | Ver blocos de conteúdo |
| Editar blocos de conteúdo                             | Criar e atualizar blocos de conteúdo |
| Arquivar blocos de conteúdo                          | Mover blocos de conteúdo para o arquivo |
| Ver Feature Flags                              | Ver Feature Flags |
| Editar Feature Flags                              | Criar e atualizar Feature Flags |
| Arquivar Feature Flags                           | Mover Feature Flags para o arquivo |
| Ver modelos de mensagens do WhatsApp                 | Permite que os usuários vejam [modelos de mensagens do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message). |
| Editar modelos de mensagens do WhatsApp | Permite que os usuários criem modelos de mensagens do WhatsApp no construtor de modelos. Esse recurso está atualmente em acesso antecipado. |
| Ver segmentos                                   | Ver segmentos. Os usuários devem ter a permissão "Ver Segmentos" para ter a permissão "Editar Segmentos" ou "Arquivar Segmentos". |
| Arquivar segmentos                                | Arquivar e desarquivar segmentos. Os usuários com a permissão "Arquivar Segmentos" também devem ter a permissão "Ver Segmentos". |
| Editar segmentos                                   | Criar e atualizar segmentos. Os usuários com a permissão "Editar Segmentos" também devem ter a permissão "Ver Segmentos". |
| Ver grupo de controle global                       | Ver página de configuração do grupo de controle global |
| Editar grupo de controle global                       | Criar e salvar alterações no grupo de controle global. Os usuários com a permissão "Editar Grupo de Controle Global" também devem ter permissões para "Editar Campanhas" e "Editar Canvas". Os usuários com a permissão "Editar Grupo de Controle Global" também recebem a permissão "Ver Grupo de Controle Global". |
| Ver modelos de banner                           | Ver modelos de banner |
| Editar modelos de banner                           | Criar e atualizar modelos de banner |
| Arquivar modelos de banner                   	  | Mover modelos de banner para o arquivo |
| Ver modelos de e-mail                            | Ver modelos de e-mail |
| Editar modelos de e-mail                            | Criar e atualizar modelos de e-mail |
| Arquivar modelos de e-mail                         | Mover modelos de e-mail para o arquivo |
| Ver modelos de link de e-mail   	                  | Ver modelos de link sem fazer alterações |
| Editar modelos de link de e-mail	                      | Criar e atualizar modelos de link |
| Publicar landing pages                           | Tornar uma landing page em rascunho ativa |
| Editar rascunhos de landing page                        | Criar e salvar rascunhos de landing page |
| Ver landing pages			                  | Ver landing pages |
| Editar modelos de landing page	                  | Criar e atualizar modelos de landing page |
| Ver modelos de landing page	                  | Ver modelos de landing page |
| Arquivar modelos de landing page 	              | Mover modelos de landing page para o arquivo |
| Ver ativos da biblioteca de mídia                       | Ver ativos da biblioteca de mídia |
| Editar ativos da biblioteca de mídia                       | Criar e atualizar ativos da biblioteca de mídia |
| Excluir ativos da biblioteca de mídia                     | Excluir permanentemente ativos da biblioteca de mídia |
| Ver locais                                  | Ver locais |
| Editar locais                                  | Criar e editar locais |
| Arquivar locais                               | Mover locais para o arquivo |
| Ver códigos de promoção                            | Ver códigos promocionais |
| Editar códigos de promoção                            | Criar e atualizar códigos promocionais |
| Exportar códigos de promoção                          | Baixar uma lista de códigos promocionais do dashboard |
| Ver Centrais de Preferências                         | Ver Centrais de Preferências |
| Editar Centrais de Preferências                         | Criar e atualizar Centrais de Preferências |
| Lançar Centrais de Preferências	                      | Tornar um rascunho da Central de Preferências ativo ou atualizar uma existente |
| Ver chaves de API                                   | Ver chaves de API |
| Editar chaves de API                                   | Criar e atualizar chaves de API |
| Ver grupos internos                            | Ver grupos internos |
| Editar grupos internos                            | Criar e atualizar grupos internos |
| Excluir grupos internos                          | Excluir grupos internos |
| Ver registro de atividade de mensagens                       | Ver registros de atividade de mensagens |
| Ver registro de usuários de eventos                             | Ver registros de usuários de eventos |
| Ver identificadores de API                            | Ver identificadores de API e outros identificadores |
| Ver dashboard de uso da API                        | Ver o dashboard de uso da API |
| Ver limites da API                                 | Ver limites de taxa da API |
| Ver alertas de uso da API                           | Ver alertas de uso da API |
| Editar alertas de uso da API                           | Criar e atualizar alertas de uso da API |
| Editar depurador do SDK                               | Criar e baixar sessões do depurador do SDK |
| Ver depurador do SDK                               | Ver depurador do SDK ou sessões de depuração |
| Ver configurações do app                               | Ver página de configurações do app |
| Editar configurações do app                               | Criar, editar e atualizar apps nas configurações do app |
| Ver catálogos                                   | Ver catálogos e seleções |
| Editar catálogos                                   | Criar e atualizar catálogos e seleções |
| Exportar catálogos                                 | Baixar catálogos do dashboard |
| Excluir catálogos                                 | Excluir catálogos permanentemente |
| Editar usuários do dashboard                            | Ver, criar e editar usuários da empresa |
| Ver configurações de e-mail                             | Ver preferências de e-mail |
| Editar configurações de e-mail                             | Ativar e atualizar preferências de e-mail | 
| Editar criptografia em nível de campo do identificador            | Ativar e atualizar configurações de criptografia em nível de campo |
| Ver atributos personalizados                          | Ver atributos personalizados e relatório de uso |
| Editar atributos personalizados                          | Criar e atualizar atributos personalizados |
| Bloquear atributos personalizados                     | Adicionar atributos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Excluir atributos personalizados                        | Excluir atributos personalizados permanentemente |
| Exportar atributos personalizados                        | Baixar atributos personalizados do dashboard |
| Ver eventos personalizados                              | Ver eventos personalizados e relatório de uso, e adicionar eventos personalizados ao e-mail do relatório diário de análise de dados |
| Editar eventos personalizados                              | Criar e atualizar eventos personalizados |
| Bloquear eventos personalizados                         | Adicionar eventos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Excluir eventos personalizados                            | Excluir permanentemente eventos personalizados |
| Exportar eventos personalizados                            | Baixar eventos personalizados do dashboard |
| Editar segmentação de propriedades de eventos personalizados         | Ativar e desativar a segmentação para propriedades de eventos personalizados |
| Ver produtos                                   | Ver produtos |
| Editar produtos                                   | Criar e atualizar produtos |
| Bloquear produtos                              | Adicionar produtos a uma lista de bloqueio que restringe o uso no dashboard |
| Editar segmentação de propriedades de compra             | Ativar e desativar a segmentação para propriedades de eventos de compra |
| Editar parceiros de tecnologia                        | Criar e atualizar parceiros de tecnologia |
| Editar ingestão de dados na nuvem                       | Criar, atualizar e excluir fontes e sincronizações |
| Ver configurações de localização                      | Ver página de configurações de localização multilíngue |
| Editar configurações de localização                      | Criar localizações multilíngues |
| Excluir configurações de localização                    | Excluir localizações multilíngues |
| Editar inscrições                              | Criar e atualizar grupos de inscrições |
| Ver tags                                       | Ver tags |
| Editar tags                                       | Criar e atualizar tags |
| Excluir tags                                     | Excluir tags permanentemente |
| Ver equipes                                      | Ver equipes |
| Editar equipes                                      | Criar e atualizar equipes |
| Arquivar equipes                                   | Mover equipes para o arquivo |
| Ver transformação de dados                        | Ver transformações de dados |
| Editar transformação de dados                        | Criar e atualizar transformações de dados |
| Editar modelos de Canvas                           | Criar e atualizar modelos de Canvas |
| Aprovar campanhas                               | Aprovar ou negar campanhas. O [fluxo de trabalho de aprovação para campanhas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar do acesso antecipado. |
| Aprovar canvas                                | Aprovar ou negar canvas. O [fluxo de trabalho de aprovação para canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar do acesso antecipado. |
| Ver posicionamentos                                 | Ver posicionamento de banner |
| Editar posicionamentos                                 | Ver posicionamentos de banner sem fazer alterações |
| Arquivar posicionamentos                              | Mover posicionamentos de banner para o arquivo |
| Ver configurações de push                              | Ver configurações de push |
| Editar configurações de push                              | Criar e atualizar configurações de push |
| Editar relatórios do dashboard                          | Criar e atualizar relatórios |
| Ver importação de usuários                               | Ver importações de usuários CSV sem fazer alterações |
| Importar usuários                                    | Fazer upload de usuários para o dashboard |
| Exportar dados de usuários                                | Baixar usuários do dashboard |
| Editar dados de usuários                                  | Criar e atualizar dados de usuários |
| Ver mesclagem de usuários                                | Ver uma lista de registros de mesclagem de usuários |
| Ver registros de exclusão de usuários	            	  | Ver registros de exclusão de usuários |
| Excluir usuários do dashboard	                  | Excluir permanentemente usuários do dashboard individualmente ou em massa. |      
| Ver agentes de IA personalizados                           | Permite que os usuários vejam agentes de IA personalizados. |
| Editar agentes de IA personalizados                           | Permite que os usuários criem e atualizem agentes de IA personalizados. |
| Arquivar agentes de IA personalizados                        | Permite que os usuários arquivem agentes de IA personalizados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }