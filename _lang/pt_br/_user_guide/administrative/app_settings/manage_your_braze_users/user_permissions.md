---
nav_title: Permissões
article_title: Permissões de brasagem
page_order: 2
page_type: reference
description: "Este artigo de referência aborda como as permissões de usuário funcionam no Braze. Aqui, você pode aprender a editar e definir permissões de usuário, escolhendo quem pode acessar seus aplicativos no painel."
tool: Dashboard

---

# Permissões de brasagem

> Saiba como criar conjuntos de permissões, criar funções, editar permissões de usuários e exportar permissões de usuários, para garantir que os usuários acessem apenas os espaços de trabalho e os recursos de que mais precisam.

## Criação de um conjunto de permissões

Use conjuntos de permissões para agrupar permissões relacionadas a áreas temáticas ou ações específicas. Eles podem ser aplicados aos usuários do painel que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, vá para **Configurações** > **Configurações de permissão** e selecione **Criar conjunto de permissões**. Para obter uma descrição de cada permissão, consulte [Lista de permissões](#list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nome|Permissões|
\|-----------|----------------|
|Desenvolvedores|"Acessar o console de desenvolvimento"|.
|Marketers|"Campanhas de acesso, telas, cartões, sinalizadores de recursos, segmentos, biblioteca de mídia e centros de preferência" <br> "Gerenciar ativos da biblioteca de mídia"
|User Management|"Gerenciar usuários do painel" <br> "Gerenciar equipes"|.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Criação de uma função

As funções permitem maior estruturação ao agrupar suas permissões personalizadas individuais com controles de acesso ao espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um único painel. Com as funções, você pode adicionar usuários do painel aos espaços de trabalho corretos e conceder-lhes diretamente as permissões associadas. Para obter uma descrição de cada permissão, consulte [Lista de permissões](#list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nome da função | Espaço de trabalho | Permissões  
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Center"<br>"Gerenciar ativos da biblioteca de mídia"
| Marketer - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers" <br>"Gerenciar ativos da biblioteca de mídia"
| Gerenciamento de usuários - Todas as marcas | {::nomarkdown}[DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda, [DEV] Marca de cuidados com a pele, [QA] Marca de cuidados com a pele, [PROD] Marca de cuidados com a pele {:/} | "Manage Dashboard Users" (Gerenciar usuários do painel)<br>"Gerenciar equipes"
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e as funções diferem do Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Considerações sobre a adição de permissões de usuário ao Teams

Você pode encontrar dificuldades ao tentar salvar permissões no painel do Braze, principalmente ao adicionar ou remover usuários de um espaço de trabalho ou adicioná-los a uma equipe. O botão **Save/Update Users (Salvar/Atualizar usuários** ) poderá ficar acinzentado se as permissões do usuário forem idênticas às que ele já tem no nível do espaço de trabalho. Essa restrição existe porque não há vantagem em ter uma equipe se todos os usuários tiverem as mesmas permissões que o espaço de trabalho inteiro.

Para adicionar com êxito um usuário a uma equipe e manter as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados

Os usuários limitados têm permissões específicas que lhes permitem gerenciar determinados aspectos do painel do Braze, embora tenham restrições em comparação com os administradores da empresa e os administradores do espaço de trabalho.

| Permissões | Os usuários limitados podem editar as permissões de outros usuários limitados se tiverem a permissão "Manage Dashboard Users" (Gerenciar usuários do painel) marcada. Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, eles não podem criar ou gerenciar contas de administrador da empresa. |
| Limitações de função: Se um usuário limitado tiver todas as permissões, exceto "Administrador do grupo de aplicativos", ele ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador de espaço de trabalho. |
| Visibilidade das permissões: se um usuário limitado tiver a opção "Gerenciar usuários do painel" marcada para um grupo de aplicativos (como Dev), mas não para outro (como Prod), ele não verá as permissões do grupo de aplicativos Prod em seu perfil "Gerenciar usuários". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparação de usuários limitados

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do grupo de aplicativos | Os administradores de grupos de aplicativos têm permissões específicas para gerenciar grupos de aplicativos, mas não têm a mesma autoridade que os administradores da empresa. Os usuários limitados podem herdar permissões semelhantes às dos administradores do grupo de aplicativos se tiverem as permissões necessárias verificadas. |
| Administrador da empresa | Os administradores da empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do painel. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro administrador da empresa para realizar essa ação. |
| Permissão básica de somente leitura | Para acessar determinadas partes do painel, como a página Technology Partners, os usuários devem ter uma permissão básica de somente leitura. Isso inclui ter a opção "Manage External Integrations" (Gerenciar integrações externas) ativada, juntamente com as permissões para Access Campaigns (Acessar campanhas), Canvases (Telas), Cards (Cartões), Segments (Segmentos) e Media Library (Biblioteca de mídia). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erro de acesso limitado

Os usuários podem encontrar mensagens como "Acesso limitado". Você não tem permissão para acessar esta página." Nesses casos, o administrador da conta deve verificar se é possível resolver o problema desativando e reativando as permissões do usuário.

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do painel para outro.
{% endalert %}

## Edição das permissões de um usuário

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, vá para **Settings** > **Company Users (** **Configurações** > **Usuários da empresa**) e selecione o nome dele.

A página "Company Users" (Usuários da empresa) no Braze com um usuário listado nos resultados.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### Administrador

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [as configurações de aprovação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Adicionar, editar, excluir, suspender ou cancelar a suspensão de outros [usuários do Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Exportar usuários do Braze como um CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador** e, em seguida, selecione **Atualizar usuário**.

\![Os detalhes do usuário selecionado com a caixa de seleção do administrador em foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar o Braze até que você atribua a ele pelo menos uma permissão [no nível da empresa](#company) ou [do espaço de trabalho](#workspace).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gerenciar as seguintes permissões no nível da empresa para um usuário, marque ou desmarque a caixa ao lado dessa permissão. Quando terminar, selecione **Update user (Atualizar usuário**).

|Nome da permissão|Descrição|
|----------|-----------|
|Gerenciar as configurações da empresa|Permite que os usuários modifiquem qualquer configuração da empresa.|
|Criar e excluir espaços de trabalho|Permite que os usuários criem e excluam espaços de trabalho.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espaço de trabalho

Você pode conceder a um usuário permissões diferentes para cada espaço de trabalho ao qual ele pertence no Braze. Para gerenciar as permissões no nível do espaço de trabalho, selecione **Select workspaces and permissions (Selecionar espaços de trabalho e permissões**) e, em seguida, escolha as permissões manualmente para selecionar ou atribuir um conjunto de permissões [criado anteriormente](#creating-a-permission-set).

Se for necessário conceder a um usuário permissões diferentes para espaços de trabalho diferentes, repita esse processo quantas vezes forem necessárias. Para obter uma descrição de cada permissão, consulte [Lista de permissões](#list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Em **Workspaces**, escolha um ou mais workspaces no menu suspenso. Em seguida, em **Permissões**, escolha uma ou mais permissões no menu suspenso. Essas permissões serão atribuídas somente aos espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Enable Admin Access (Ativar acesso de administrador** ) se, em vez disso, quiser conceder a eles permissões completas para esse espaço de trabalho.

Quando terminar, selecione **Update user (Atualizar usuário**).

Permissões em nível de espaço de trabalho sendo selecionadas manualmente no Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Em **Workspaces**, escolha um ou mais workspaces no menu suspenso. Em seguida, em **Permission Sets (Conjuntos de permissões**), escolha um conjunto de permissões. Essas permissões serão atribuídas somente aos espaços de trabalho que você selecionou.

Quando terminar, selecione **Update user (Atualizar usuário**).

Permissões em nível de espaço de trabalho sendo atribuídas por meio de um conjunto de permissões no Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportação de permissões de usuário

Para fazer o download de uma lista de seus usuários e suas permissões, vá para **Settings** > **Company Users** e selecione **Export Users**. Um arquivo CSV será enviado para seu endereço de e-mail em breve.

A página "Usuários da empresa" no Braze com a opção "Exportar usuários" em destaque.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permissões

{% alert important %}
A partir de abril de 2024, para criar ou atualizar listas de códigos promocionais, os usuários do Braze precisam da permissão "Access Campaigns, Canvases, Cards, Segments, Media Library".
{% endalert %}

|Nível|Nome|Definição|
|---|---|---|
|Administrador|Administrador|Permite que os usuários acessem todos os recursos disponíveis. Essa é a configuração padrão para todos os novos usuários. Pode atualizar as configurações da empresa (nome da empresa e fuso horário), o que os usuários limitados não podem fazer.|
|Empresa|Criar e excluir espaços de trabalho|Permite que os usuários criem e excluam espaços de trabalho.|
|Empresa|Gerenciar as configurações da empresa|Permite que os usuários modifiquem qualquer configuração da empresa.|
|Espaço de trabalho|Acesse campanhas, telas, cartões, blocos de conteúdo, sinalizadores de recursos, segmentos, biblioteca de mídia, locais, códigos de promoção e centros de preferência|Permite que os usuários visualizem as métricas de desempenho da campanha e do Canvas, criem e dupliquem rascunhos de campanhas e Canvases, editem rascunhos e modelos de campanhas e Canvas, visualizem rascunhos de segmentos, modelos e mídia, criem modelos, carreguem mídia, criem ou atualizem listas de códigos de promoção, visualizem relatórios de envolvimento e visualizem configurações globais de mensagens no painel. No entanto, os usuários com essa permissão não podem pausar ou editar o conteúdo ao vivo existente.|
|Espaço de trabalho|Acessar o console de desenvolvimento|Permite acesso total às seguintes configurações e registros:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Chaves de API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Grupos internos</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Registro de atividades de mensagens</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Registro de usuário de eventos</a></li></ul>{:/}|
|Espaço de trabalho|Campanhas de aprovação e negação|Permite que os usuários aprovem ou recusem campanhas. O [fluxo de trabalho de aprovação de campanhas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão seja aplicada. Essa configuração está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta se estiver interessado em participar do acesso antecipado.|
|Espaço de trabalho|Aprovar e recusar telas|Permite que os usuários aprovem ou recusem Canvases. O [fluxo de trabalho de aprovação para Canvases]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão seja aplicada.|
|Espaço de trabalho|Editar integrações de correntes|Permite que os usuários modifiquem uma conexão do Currents, incluindo as credenciais. Por padrão, os usuários aos quais foi atribuída a permissão "External Integrations" também recebem essa permissão.|
|Espaço de trabalho|Editar segmentos|Permite que os usuários criem e editem segmentos. Você ainda pode criar campanhas com segmentos e filtros existentes sem essa permissão. Você precisa dessa permissão para gerar um segmento a partir de usuários em um CSV ou redirecionar o grupo de usuários no CSV.|
|Espaço de trabalho|Exportar dados do usuário|Permite que os usuários exportem seus dados de usuários de segmentos, campanhas e Canvases. Essa permissão inclui informações confidenciais do usuário, como nomes, endereços de e-mail e outras informações de identificação pessoal (PII) coletadas. |
|Espaço de trabalho|Importar e atualizar dados do usuário|Permite que os usuários importem arquivos CSV e de atualização de usuários de aplicativos, bem como visualizem a página User Import (Importação de usuários). Isso também permite que você edite o status da assinatura de um usuário e as regras de ativação/desativação do grupo de assinatura.|
|Espaço de trabalho|Iniciar e gerenciar blocos de conteúdo|Permite que os usuários iniciem e gerenciem [blocos de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Espaço de trabalho|Lançamento de centros de preferência|Permite que os usuários iniciem [centros de preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Espaço de trabalho|Gerenciar aplicativos|Permite que os usuários editem **as configurações do aplicativo**.|
|Espaço de trabalho|Permissão do painel Manage Catalogs (Gerenciar catálogos)|Permite que os usuários criem e gerenciem catálogos.|
|Espaço de trabalho|Gerenciar usuários do painel| Permite que os não administradores visualizem, editem e gerenciem a página **Company Users (Usuários da empresa** ) e gerenciem os usuários do painel em seu espaço de trabalho, modificando as permissões de qualquer usuário, inclusive eles próprios. Os usuários com essa permissão não podem excluir usuários (somente os administradores podem excluir usuários).|
|Espaço de trabalho|Gerenciar configurações de e-mail|Permite que os usuários salvem as alterações de configuração de e-mail**(Configurações** > **Preferências de e-mail**).|
|Espaço de trabalho|Gerenciar eventos, atributos e compras|Permite que os usuários editem atributos personalizados (usuários sem esse recurso ainda podem visualizar atributos personalizados), editem e visualizem propriedades de eventos personalizados e editem e visualizem propriedades de produtos em **Configurações de dados**.|
|Espaço de trabalho|Gerenciar integrações externas|Permite o acesso a todas as guias em **Parceiros de tecnologia**, a capacidade de sincronizar o Braze com outras plataformas e o acesso para gerenciar [a ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Espaço de trabalho|Gerenciar sinalizadores de recursos|Permite que os usuários criem ou editem [sinalizadores de recursos]({{site.baseurl}}/developer_guide/feature_flags/).|
|Espaço de trabalho|Gerenciar ativos da biblioteca de mídia|Permite que os usuários adicionem, editem e excluam ativos da biblioteca de mídia.|
|Espaço de trabalho|Gerenciar grupos de assinatura|Permite que os usuários criem e gerenciem grupos de assinatura.|
|Espaço de trabalho|Gerenciar tags|Permite que os usuários editem ou excluam tags (em **Gerenciamento de tags**). Você não precisa dessa permissão para adicionar tags a campanhas ou segmentos.|
|Espaço de trabalho|Gerenciar equipes|Permite que os usuários gerenciem **equipes internas**. A capacidade de selecionar essa permissão depende de seu contrato com a Braze.|
|Espaço de trabalho|Gerenciar transformações|Permite que os usuários criem e gerenciem transformações de dados.|
|Espaço de trabalho|Enviar campanhas, telas|Permite aos usuários editar, arquivar e interromper campanhas e Canvases, criar campanhas e lançar Canvases. |
|Espaço de trabalho|Exibir detalhes de faturamento|Permite que os usuários visualizem as assinaturas e o faturamento.|
|Espaço de trabalho|Exibir integração de correntes|Permite que os usuários visualizem todas as informações sobre uma conexão do Currents, excluindo as credenciais. Por padrão, os usuários aos quais foi atribuída a permissão "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers" também recebem essa permissão.|
|Espaço de trabalho|Exibir atributos personalizados marcados como PII|Permite que usuários não administradores visualizem atributos personalizados que contenham informações confidenciais e estejam marcados como informações de identificação pessoal (PII).|
|Espaço de trabalho|Exibir PII|Permite que os usuários visualizem os campos de informações de identificação pessoal (PII) conforme definido pela sua empresa no painel. Os usuários também podem visualizar os campos de PII na guia **Visualizar como usuário** das visualizações de mensagens.<br><br>Você precisa dessa permissão para usar o [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), pois ele permite o acesso direto a alguns dados do cliente.|
|Espaço de trabalho|Exibir perfis de usuário em conformidade com PII|Permite que os usuários visualizem perfis de usuários que contenham campos que sua empresa definiu como informações de identificação pessoal (PII), mas os campos de PII são redigidos.<br><br>Você precisa dessa permissão para usar a ferramenta de pesquisa de usuários. |
|Espaço de trabalho|Exibir Transformações|Permite que os usuários visualizem [as transformações de dados do Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|Espaço de trabalho|Exibir dados de uso|Permite que os usuários visualizem o uso do aplicativo, incluindo os painéis de desempenho do canal.|
|Espaço de trabalho|Mesclar usuários duplicados|Permite que os usuários mesclem perfis de usuário duplicados.|
|Espaço de trabalho|Visualizar usuários duplicados|Permite que os usuários visualizem quais perfis de usuário estão duplicados.|
|Espaço de trabalho|Criar e editar modelos de tela|Permite que os usuários criem e editem modelos do Canvas.|
|Espaço de trabalho|Exibir modelos de tela|Permite que os usuários visualizem os modelos do Canvas.|
|Espaço de trabalho|Modelos do Archive Canvas|Permite que os usuários arquivem modelos do Canvas.|
|Espaço de trabalho|Gerenciar a segmentação de propriedades de eventos personalizados|Permite que os usuários criem segmentos com base na recência e na frequência da propriedade do evento.|
|Espaço de trabalho|Publicar páginas de destino|Permite que os usuários publiquem [páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|Espaço de trabalho|Criar rascunhos de páginas de destino|Permite que os usuários criem e salvem rascunhos de páginas de destino.|
|Espaço de trabalho|Acessar páginas de destino|Permite que os usuários acessem a página **Landing Pages**.|
|Espaço de trabalho|Criar e editar modelos de páginas de destino|Permite que os usuários criem e editem modelos de páginas de destino.|
|Espaço de trabalho|Exibir modelos de página de destino|Permite que os usuários visualizem modelos de páginas de destino.|
|Espaço de trabalho|Modelos de página de destino de arquivo|Permite que os usuários arquivem modelos de páginas de destino.|
|Espaço de trabalho|Exibir agentes de IA personalizados|Permite que os usuários visualizem [agentes de IA personalizados]({{site.baseurl}}/user_guide/brazeai/agents/). Esse recurso está atualmente na versão beta.|
|Espaço de trabalho|Criar agentes de IA personalizados|Permite que os usuários criem agentes de IA personalizados. Esse recurso está atualmente na versão beta.|
|Espaço de trabalho|Editar agentes de IA personalizados|Permite que os usuários editem agentes de IA personalizados. Esse recurso está atualmente na versão beta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
