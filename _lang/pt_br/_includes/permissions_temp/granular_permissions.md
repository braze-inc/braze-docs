{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Criando um conjunto de permissões

Use conjuntos de permissões para agrupar permissões relacionadas a áreas ou ações específicas. Você pode aplicar conjuntos de permissões a usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acessar **Configurações** > **Configurações de Permissão**, depois selecione **Criar conjunto de permissões**. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nome|Permissões|
\|-----------|----------------|
|Desenvolvedores|"Ver Chaves da API", "Editar Chaves da API", "Ver Grupos Internos", "Editar Grupos Internos", "Ver Registro de Atividade de Mensagens", "Ver Registro de Usuários de Eventos", "Ver identificadores da API", "Ver Dashboard de Uso da API", "Ver Limites da API", "Ver Alertas de Uso da API", "Editar Alertas de Uso da API", "Ver Depurador SDK", "Editar Depurador SDK".|
|Profissionais de Marketing|"Ver Campanhas", "Editar Campanhas", "Arquivar Campanhas", "Ver Canvases", "Editar Canvases", "Arquivar Canvases", "Ver Regras de Limitação de Frequência", "Editar Regras de Limitação de Frequência", "Ver Priorização de Mensagens", "Editar Priorização de Mensagens", "Ver Blocos de Conteúdo", "Ver Flags de Funcionalidade", "Editar Flags de Funcionalidade", "Arquivar Flags de Funcionalidade", "Ver Segmentos", "Editar Segmentos", "Editar Grupo de Controle Global", "Ver Modelos IAM", "Editar Modelos IAM", "Arquivar Modelos IAM", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Arquivar Modelos de E-mail", "Ver Modelos de Webhook", "Editar Modelos de Webhook", "Arquivar Modelos de Webhook", "Ver Modelos de Link", "Editar Modelos de Link", "Ver Ativos da Biblioteca de Mídia", "Ver Localizações", "Editar Localizações", "Arquivar Localizações", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centros de Preferência", "Editar Centros de Preferência", "Editar Relatórios", "Ver Modelos de Banner", "Ver Configurações de Múltiplas Línguas", "Usar Operador", "Ver Agentes do Estúdio de Decisão", "Ver Evento de Conversão do Estúdio de Decisão".|
|Gerenciamento de Usuários|"Ver Usuários do Dashboard", "Editar Usuários do Dashboard", "Ver Equipes", "Editar Equipes", "Arquivar Equipes".|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Criando uma função

As funções permitem mais estrutura ao agrupar suas permissões personalizadas individuais com os controles de acesso do espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nome do Papel | espaço de trabalho | Permissões  
----------- | ----------- | ---------
| Profissional de Marketing - Marcas de Moda | {::nomarkdown}[DEV] Marca de Moda, [QA] Marca de Moda, [PROD] Marca de Moda {:/} | "Ver Campanhas", "Editar Campanhas", "Arquivar Campanhas", "Ver Canvases", "Editar Canvases", "Arquivar Canvases", "Ver Blocos de Conteúdo", "Editar Blocos de Conteúdo", "Arquivar Blocos de Conteúdo", "Lançar Blocos de Conteúdo", "Ver Flags de Funcionalidade", "Editar Flags de Funcionalidade", "Arquivar Flags de Funcionalidade", "Ver Segmentos", "Editar Segmentos", "Ver Modelos de Banner", "Editar Modelos de Banner", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Ver Ativos da Biblioteca de Mídia", "Editar Ativos da Biblioteca de Mídia", "Excluir Ativos da Biblioteca de Mídia", "Ver Localizações", "Editar Localizações", "Arquivar Localizações", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centros de Preferência", "Editar Centros de Preferência". |
| Profissional de Marketing - Marcas de Cuidados com a Pele | {::nomarkdown}[DEV] Marca de Cuidados com a Pele, [QA] Marca de Cuidados com a Pele, [PROD] Marca de Cuidados com a Pele {:/} |"Ver Campanhas", "Editar Campanhas", "Arquivar Campanhas", "Ver Canvases", "Editar Canvases", "Arquivar Canvases", "Ver Blocos de Conteúdo", "Editar Blocos de Conteúdo", "Arquivar Blocos de Conteúdo", "Lançar Blocos de Conteúdo", "Ver Flags de Funcionalidade", "Editar Flags de Funcionalidade", "Arquivar Flags de Funcionalidade", "Ver Segmentos", "Editar Segmentos", "Ver Modelos de Banner", "Editar Modelos de Banner", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Ver Ativos da Biblioteca de Mídia", "Editar Ativos da Biblioteca de Mídia", "Excluir Ativos da Biblioteca de Mídia", "Ver Localizações", "Editar Localizações", "Arquivar Localizações", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centros de Preferência", "Editar Centros de Preferência".|
| Gerenciamento de Usuários - Todas as Marcas | {::nomarkdown}[DEV] Marca de Moda, [QA] Marca de Moda, [PROD] Marca de Moda, [DEV] Marca de Cuidados com a Pele, [QA] Marca de Cuidados com a Pele, [PROD] Marca de Cuidados com a Pele {:/} | "Ver Usuários do Dashboard", "Editar Usuários do Dashboard", "Ver Equipes", "Editar Equipes", "Arquivar Equipes"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e funções diferem das Equipes?

{% multi_lang_include permissions.md content="Differences" %}

### Considerações para adicionar permissões de usuário às Equipes

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard do Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho, ou ao adicioná-los a uma Equipe. O botão **Salvar/Atualizar Usuários** pode ficar desativado se as permissões do usuário forem idênticas às que eles já possuem no nível do espaço de trabalho. Essa restrição existe porque não há benefício em ter uma Equipe se todos os usuários possuem as mesmas permissões que todo o espaço de trabalho.

Para adicionar um usuário a uma Equipe com sucesso, mantendo as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários Limitados

Usuários limitados têm permissões específicas que permitem gerenciar certos aspectos do dashboard do Braze, enquanto têm restrições em comparação com administradores da empresa e administradores de espaço de trabalho.

| Escopo | Descrição |
| --- | --- |
| Permissões | Usuários limitados podem editar as permissões de outros usuários limitados se tiverem as permissões "Ver Usuários do Dashboard" e "Editar Usuários do Dashboard". Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, eles não podem criar ou gerenciar contas de administrador da empresa. |
| Limitações de função | Se um usuário limitado tiver todas as permissões, exceto "Administrador do Espaço de Trabalho", ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador do espaço de trabalho. |
| Visibilidade das permissões | Se um usuário limitado tiver as permissões "Ver Usuários do Dashboard" e "Editar Usuários do Dashboard" para um espaço de trabalho (como Dev), mas não para outro (como Prod), ele não verá as permissões do espaço de trabalho Prod na página de detalhes dos usuários do dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparando usuários limitados

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do Espaço de Trabalho | Os Administradores do Espaço de Trabalho têm permissões específicas para gerenciar Espaços de Trabalho, mas não têm a mesma autoridade que os Administradores da Empresa. Usuários Limitados podem herdar permissões semelhantes às dos Administradores do Espaço de Trabalho se tiverem as permissões necessárias marcadas. |
| Administrador (Administrador da Empresa) | Os Administradores da Empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro Administrador da Empresa para essa ação. |
| Acesso somente para visualização | Para acessar partes do dashboard, como a página de Campanhas, os usuários devem ter permissões de visualização atribuídas a eles.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erro de acesso limitado

Os usuários podem encontrar mensagens como "Você precisa de permissões de 'Ver Páginas de Destino' para acessar esta página". Nesses casos, o usuário e o administrador da conta devem verificar se as permissões necessárias foram concedidas. Se sim, tente resolver o problema desativando e reativando as permissões do usuário. 

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Editando as permissões de um usuário

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Configurações** > **Usuários da Empresa**, em seguida, selecione o nome deles.

![A página "Usuários da Empresa" no Braze mostrando uma tabela de usuários do dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Administrador

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Adicionar, editar, excluir, suspender ou reativar outros [Braze usuários]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Exportar usuários do Braze como um CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador**, depois selecione **Atualizar usuário**.

![Os detalhes do usuário selecionado com a caixa de seleção de administrador em foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar o Braze até que você atribua a ele pelo menos uma [permissão em nível de empresa ou em nível de espaço de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gerenciar as seguintes permissões a nível de empresa para um usuário, marque ou desmarque a caixa ao lado dessa permissão. Quando terminar, selecione **Atualizar usuário**.

|Nome da permissão|Descrição|
|----------|-----------|
|Gerenciar configurações da empresa|Permite que os usuários modifiquem as configurações de permissão e verificação do remetente. .|
|Criar e excluir espaços de trabalho|Permite aos usuários criar e excluir espaços de trabalho.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espaço de trabalho

Você pode dar a um usuário diferentes permissões para cada espaço de trabalho ao qual ele pertence no Braze. Para gerenciar as permissões em nível de espaço de trabalho, selecione **Selecionar espaços de trabalho e permissões**, em seguida, escolha as permissões manualmente ou atribua um [conjunto de permissões ou função]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que você criou anteriormente. Se você precisar dar a um usuário permissões diferentes para diferentes espaços de trabalho, repita este processo quantas vezes forem necessárias. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, sob **Permissões**, selecione uma ou mais permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Atribuir acesso de administrador do espaço de trabalho** se desejar dar a eles permissões completas para este espaço de trabalho em vez disso.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo selecionadas manualmente no Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Conjuntos de permissão**, escolha um conjunto de permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo atribuídas através de um conjunto de permissões no Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, sob **Função**, escolha uma função. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo atribuídas através de uma função no Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportando permissões de usuário

Para baixar uma lista de seus usuários e suas permissões, acesse **Configurações** > **Usuários da Empresa**, em seguida, selecione **Exportar Usuários**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

![A página "Usuários da Empresa" no Braze com a opção "Exportar Usuários" em foco.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permissões

| Permissão | Definição |
|-------------------------------------------------|---------------------|
| Ver informações de faturamento                            | Ver detalhes de cobrança |
| Ver atributos personalizados marcados como IPI            | Ver atributos personalizados marcados como IPI |
| Ver IPI                                        | Ver IPI |
| Ver perfis de usuário em conformidade com IPI                | Acessar pesquisa de usuários e visualizar perfis de usuários com IPI redigido |
| Ver dados de uso                                 | Ver dados de uso |
| Mesclar usuários duplicados                           | Combinar usuários duplicados em um usuário. Duplicatas são removidas após a mesclagem. |
| Prévia de usuários duplicados                         | Prévia dos perfis de usuário que são duplicatas |
| Ver modelos de canva                           | Veja os modelos do Canvas |
| Arquivar modelos de canva                        | Mover modelos de canva para o arquivo |
| Lançar Blocos de Conteúdo                           | Lançar Blocos de Conteúdo |
| Abrir Centrais de Preferências                       | Lançar centros de preferência |
| Exportar dados de usuários                                | Baixar usuários do dashboard |
| Editar integrações com o Currents                      | Criar, atualizar e excluir integrações Currents |
| Ver Integração do Currents                       | Ver integrações Currents |
| Ver campanhas                                  | Ver campanhas |
| Editar campanhas                                  | Criar e atualizar campanhas |
| Arquivar campanha                               | Mover campanhas para o arquivo |
| Enviar campanhas                                  | Iniciar, parar, pausar ou retomar campanhas | 
| Enviar canvas                         		  | Iniciar, parar, pausar ou retomar canvas |
| Ver regras de limite de frequência                    | Ver regras de limite de frequência |
| Editar regras de limite de frequência                    | Criar e atualizar Regras de Limitação de Frequência |
| Ver canvas                                   | Ver canvas |
| Editar canvas                                   | Criar e atualizar canvas |
| Arquivar canvas                                | Mover canvas para o arquivo |
| Ver blocos de conteúdo                             | Ver blocos de conteúdo |
| Editar blocos de conteúdo                             | Criar e atualizar Blocos de Conteúdo |
| Arquivar blocos de conteúdo                          | Mover Blocos de Conteúdo para o arquivo |
| Visualizar Feature Flags                              | Ver bandeiras de recurso |
| Editar Feature Flag                              | Criar e atualizar bandeiras de recurso |
| Arquivar Feature Flags                           | Mover bandeiras de recurso para o arquivo |
|  Ver Modelos de Mensagens do WhatsApp                | Permite que os usuários vejam [modelos de mensagens do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message). |
| Editar Modelos de Mensagens do WhatsApp | Permite que os usuários criem modelos de mensagens do WhatsApp no construtor de modelos. Esse recurso está atualmente em acesso antecipado. |
| Exibir segmentos                                   | Ver segmentos. Os usuários devem ter a permissão "Ver Segmentos" para ter a permissão "Editar Segmentos" ou "Arquivar Segmentos". |
| Arquivar segmentos                                | Arquivar e desarquivar segmentos. Os usuários com a permissão "Arquivar Segmentos" também devem ter a permissão "Ver Segmentos". |
| Editar segmentos                                   | Criar e atualizar Segmentos. Os usuários com a permissão "Editar Segmentos" também devem ter a permissão "Ver Segmentos". |
| Exibir o grupo de controle global                       | Ver página de configuração do Grupo de Controle Global |
| Editar grupo de controle global                       | Criar e salvar alterações no Grupo de Controle Global. Os usuários com a permissão "Editar Grupo de Controle Global" também devem ter permissões para "Editar Campanhas" e "Editar Canvases". Os usuários com a permissão "Editar Grupo de Controle Global" também recebem a permissão "Ver Grupo de Controle Global". |
| Ver modelos de banner                           | Ver modelos de banner |
| Editar modelos de banner                           | Criar e atualizar modelos de banner |
| Arquivar modelos de banner                   	  | Mover modelos de banner para o arquivo |
| Exibir modelos de e-mail                            | Ver modelos de e-mail |
| Editar modelo de e-mail                            | Criar e atualizar modelos de e-mail |
| Arquivar modelos de e-mail                         | Mover modelos de e-mail para o arquivo |
| Exibir modelos de links   	                      | Ver modelos de link |
| Editar modelos de links	                          | Criar e atualizar modelos de link |
| Publicar landing page                           | Tornar uma página de destino rascunho ativa |
| Editar rascunhos de landing page                        | Criar e salvar rascunhos de página de destino |
| Ver landing pages			                  | Ver páginas de destino |
| Editar modelos de landing page	                  |  Criar e atualizar modelos de página de destino |
| Exibir modelos de landing page	                  | Ver modelos de página de destino |
| Arquivar Modelo de Página de Destino 	              | Mover modelos de página de destino para o arquivo |
| Exibir ativos da biblioteca de mídia                       | Ver ativos da biblioteca de mídia |
| Editar ativos da biblioteca de mídia                       | Criar e atualizar ativos da biblioteca de mídia |
| Excluir ativos da biblioteca de mídia                     | Excluir permanentemente ativos da biblioteca de mídia |
| Ver locais                                  | Ver locais |
| Editar locais                                  | Criar e editar locais |
| Arquivar locais                               | Mover locais para o arquivo |
| Ver Códigos de Promoção                            | Ver códigos promocionais |
| Editar Códigos de Promoção                            | Criar e atualizar códigos promocionais |
| Códigos de Promoção de Exportação                          | Baixe uma lista de códigos promocionais do dashboard |
| Ver Centrais de Preferências                         | Ver centros de preferências  |
| Editar Centrais de Preferências                         | Criar e atualizar centros de preferências |
| Abrir Centrais de Preferências	                      | Tornar um rascunho do Centro de Preferências ativo ou atualizar um existente |
| Exibir chaves de API                                   | Ver chaves de API |
| Editar chaves de API                                   | Criar e atualizar chaves de API |
| Ver Grupos Internos                            | Ver grupos internos |
| Editar Grupos Internos                            | Criar e atualizar grupos internos |
| Visualizar registro de atividades de envio de mensagem                       | Ver logs de atividade de mensagens |
| Exibir registro de usuários de eventos                             | Ver logs de usuários de eventos |
| Ver identificadores de API                            | Ver identificadores de API e outros identificadores |
| Exibir o dashboard de uso da API                        | Ver o dashboard de uso da API |
| Exibir limites da API                                 | Ver limites de taxa da API |
| Exibir alertas de uso da API                           | Ver alertas de uso da API |
| Editar alertas de uso da API                           | Criar e atualizar alertas de uso da API |
| Editar depurador do SDK                               | Criar e baixar sessões do SDK Debugger |
| Exibir depurador do SDK                               | Ver SDK Debugger ou sessões de depuração |
| Exibir configurações do app                               | Ver página de Configurações do App |
| Editar configurações do app                               | Criar, editar e atualizar apps nas configurações do app |
| Ver catálogos                                   | Ver catálogos e seleções |
| Editar catálogos                                   | Criar e atualizar catálogos e seleções |
| Exportar catálogo                                 | Baixar catálogos do dashboard |
| Excluir catálogos                                 | Excluir catálogos permanentemente |
| Ver Usuários do Dashboard                            | Ver Usuários da Empresa |
| Editar usuários do painel                            | Criar e atualizar usuários da empresa 
| Ver configurações de e-mail                             | Ver Preferências de E-mail |
| Editar configurações de e-mail                             | Ativar e atualizar Preferências de E-mail | 
| Criptografia em nível de campo do identificador de edição            | Ativar e atualizar configurações de Criptografia em Nível de Campo |
| Visualizar atributos personalizados                          | Ver atributos personalizados e relatório de uso |
| Editar atributos personalizados                          | Criar e atualizar atributos personalizados |
| Lista de bloqueio de atributos personalizados                     | Adicionar atributos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Excluir atributos personalizados                        | Excluir atributos personalizados permanentemente |
| Exportar atributos personalizados                        | Baixar atributos personalizados do dashboard |
| Visualizar eventos personalizados                              | Ver eventos personalizados e relatório de uso, e adicionar eventos personalizados ao e-mail do relatório diário de análise |
| Editar eventos personalizados                              | Criar e atualizar eventos personalizados |
| Lista de bloqueio de eventos personalizados                         | Adicione eventos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Excluir eventos personalizados                            | Exclua permanentemente eventos personalizados |
| Exportar eventos personalizados                            | Baixe eventos personalizados do dashboard |
| Editar segmentação de propriedades de eventos personalizados         | Ative e desative a segmentação para propriedades de eventos personalizados |
| Visualizar produtos                                   | Veja produtos |
| Editar produtos                                   | Crie e atualize produtos |
| Lista de bloqueio de produtos                              | Adicione produtos a uma lista de bloqueio que restringe o uso no dashboard |
| Editar segmentação de propriedades de compra             | Ative e desative a segmentação para propriedades de eventos de compra |
| Edite Parceiros de Tecnologia                        | Crie e atualize parceiros de tecnologia |
| Editar ingestão de dados na nuvem                       | Crie, atualize e exclua fontes e sincronizações |
| Veja Configurações de Múltiplas Línguas                    | Veja configurações multilíngues |
| Crie Configurações de Localidade de Múltiplas Línguas           | Crie e atualize configurações de localidade multilíngues |
| Exclua Configurações de Localidade de Múltiplas Línguas           | Exclua permanentemente configurações multilíngues |
| Editar inscrições                              | Crie e atualize grupos de assinatura |
| Exibir tags                                       | Veja tags |
| Editar tags                                       | Crie e atualize tags |
| Excluir tags                                     | Excluir tags permanentemente |
| Ver equipes                                      | Ver equipes |
| Editar equipe                                      | Criar e atualizar equipes |
| Arquivar equipes                                   | Mover equipes para o arquivo |
| Ver transformação de dados                        | Ver transformações de dados |
| Editar transformação de dados                        | Criar e atualizar transformações de dados |
| Lançar campanha                                | Iniciar, parar, pausar ou retomar campanhas existentes |
| Lançar canvas                                 | Iniciar, parar, pausar ou retomar Canvases existentes |
| Editar modelos de tela                           | Criar e atualizar modelos de Canvas |
| Aprovar campanha                               | Aprovar ou negar campanhas. O [fluxo de trabalho de aprovação para campanhas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar do acesso antecipado. |
| Aprovação de telas                                | Aprovar ou negar Canvases. O [fluxo de trabalho de aprovação para canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve ser ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar do acesso antecipado. |
| Ver colocações                                 | Ver colocação de Banner |
| Editar Colocações                                 | Ver colocações de Banner sem fazer alterações |
| Arquivar colocações?                              | Mover colocações de Banner para o arquivo |
| Exibir configurações push                              | Ver configurações de Push |
| Editar configurações de push                              | Criar e atualizar configurações de Push |
| Editar Relatórios                                    | Criar e atualizar relatórios |
| Exibir importação de usuários                               | Ver importações de usuários CSV |
| Importar usuários                                    | Fazer upload de usuários para o dashboard |
| Editar dados de usuários                                  | Criar e atualizar dados de usuários |
| Ver usuários mesclados                                | Ver uma lista de registros de mesclagem de usuários |
| Exibir registros de exclusão de usuários	            	  | Exibir registros de exclusão de usuários |
| Excluir usuários do dashboard	                  | Excluir permanentemente usuários do dashboard individualmente ou em massa. |      
| Exibir agentes de IA personalizados                           | Permite que os usuários vejam agentes de IA personalizados. |
| Editar agentes de IA personalizados                           | Permite que os usuários criem e atualizem agentes de IA personalizados. |
| Arquivar agentes de IA personalizados                        | Permite que os usuários arquivem agentes de IA personalizados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }