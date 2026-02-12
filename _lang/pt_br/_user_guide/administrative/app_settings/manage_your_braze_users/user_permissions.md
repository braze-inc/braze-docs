---
nav_title: Permissões
article_title: Permissões do Braze
page_order: 2
page_type: reference
description: "Este artigo de referência cobre como as permissões de usuário funcionam na Braze. Aqui, você pode aprender como editar e definir permissões de usuário, escolhendo quem pode acessar seus aplicativos no dashboard."
tool: Dashboard

---

# Permissões do Braze

> Aprenda a criar conjuntos de permissões, criar funções, editar permissões de usuário e exportar permissões de usuário, para que você possa garantir que seus usuários acessem apenas os espaços de trabalho e recursos que mais precisam.

## Criando um conjunto de permissões

Use conjuntos de permissões para agrupar permissões relacionadas a áreas ou ações específicas. Eles podem ser aplicados aos usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acessar **Configurações** > **Configurações de Permissão**, depois selecione **Criar conjunto de permissões**. Para uma descrição de cada permissão, consulte [Lista de permissões](#list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nome|Permissões|
\|-----------|----------------|
|Desenvolvedores|“Acessar Console de Desenvolvimento”|
|Marketers|“Acesse Campanhas, canvas, Cartões, Feature Flags, Segmentos, Biblioteca de Mídia e Centrais de Preferências” <br> “Gerenciar ativos da biblioteca de mídia”|
|Gerenciamento de Usuários|“Gerenciar Usuários do Dashboard” <br> “Gerenciar equipes”|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Criando uma função

As funções permitem mais estrutura ao agrupar suas permissões personalizadas individuais com os controles de acesso do espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. Para uma descrição de cada permissão, consulte [Lista de permissões](#list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nome do Papel | espaço de trabalho | Permissões  
----------- | ----------- | ---------
| Profissional de marketing - Marcas de moda | {::nomarkdown}[DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda {:/} | "Acesse campanhas, telas, cartões, Feature Flags, segmentos, biblioteca de mídia e Central de Preferências"<br>“Gerenciar ativos da biblioteca de mídia” |
| Profissional de marketing - Marcas de produtos para a pele | {::nomarkdown}[DEV] Marca de produtos para a pele, [QA] Marca de produtos para a pele, [PROD] Marca de produtos para a pele {:/} | "Acessar campanhas, canvas, cartões, Feature Flags, segmentos, biblioteca de mídia e centrais de preferências" <br>“Gerenciar ativos da biblioteca de mídia” |
| Gerenciamento de usuários - Todas as marcas | {::nomarkdown}[DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda, [DEV] Marca de cuidados com a pele, [QA] Marca de cuidados com a pele, [PROD] Marca de cuidados com a pele {:/} | "Manage Dashboard Users" (Gerenciar usuários do dashboard)<br>“Gerenciar equipes” |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e as funções diferem do Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Considerações sobre a adição de permissões de usuário ao Teams

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard do Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho ou adicioná-los a uma equipe. O botão **Save/Update Users (Salvar/Atualizar usuários** ) poderá ficar acinzentado se as permissões do usuário forem idênticas às que ele já tem no nível do espaço de trabalho. Essa restrição existe porque não há vantagem em ter uma equipe se todos os usuários tiverem as mesmas permissões que todo o espaço de trabalho.

Para adicionar com êxito um usuário a uma equipe e manter as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados

Os usuários limitados têm permissões específicas que lhes permitem gerenciar determinados aspectos do dashboard do Braze, embora tenham restrições em comparação com os administradores da empresa e do espaço de trabalho.

| Permissões | Os usuários limitados podem editar as permissões de outros usuários limitados se tiverem a permissão "Manage Dashboard Users" (Gerenciar usuários do dashboard) marcada. Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, eles não podem criar ou gerenciar contas de administrador da empresa. |
| Limitações de função: Se um usuário limitado tiver todas as permissões, exceto "Administrador do grupo de app", ele ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador de espaço de trabalho. |
| Visibilidade das permissões: se um usuário limitado tiver a opção "Gerenciar usuários do dashboard" marcada para um grupo de app (como Dev), mas não para outro (como Prod), ele não verá as permissões do grupo de app Prod em seu perfil "Gerenciar usuários". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparação de usuários limitados

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do grupo de app | Os administradores de grupos de aplicativos têm permissões específicas para gerenciar grupos de aplicativos, mas não têm a mesma autoridade que os administradores da empresa. Os usuários limitados podem herdar permissões semelhantes às dos administradores do grupo de app se tiverem as permissões necessárias verificadas. |
| Administrador da empresa | Os administradores da empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro administrador da empresa para realizar essa ação. |
| Permissão básica de somente leitura | Para acessar certas partes do dashboard, como a página Technology Partners, os usuários devem ter uma permissão básica de somente leitura. Isso inclui ter a opção "Manage External Integrations" (Gerenciar integrações externas) ativada, juntamente com permissões para Access Campaigns (Acessar campanhas), Canvas, Cards (Cartões), Segments (Segmentos) e Media Library (Biblioteca de mídia). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erro de acesso limitado

Os usuários podem encontrar mensagens como "Acesso limitado". Você não tem permissão para acessar esta página." Nesses casos, o administrador da conta deve verificar se é possível resolver o problema desativando e reativando as permissões do usuário.

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Editando as permissões de um usuário

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Settings** > **Company Users** e selecione o nome dele.

![A página "Company Users" (Usuários da empresa) no Braze com um usuário listado nos resultados.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### Administrador

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Adicionar, editar, excluir, suspender ou reativar outros [Braze usuários]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- Exportar usuários do Braze como um CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador**, depois selecione **Atualizar usuário**.

![Os detalhes do usuário selecionado com a caixa de seleção do administrador em foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar o Braze até que você atribua a ele pelo menos uma permissão [no nível da empresa](#company) ou [no nível do espaço de trabalho](#workspace).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gerenciar as seguintes permissões a nível de empresa para um usuário, marque ou desmarque a caixa ao lado dessa permissão. Quando terminar, selecione **Atualizar usuário**.

|Nome da permissão|Descrição|
|----------|-----------|
|Gerenciar configurações da empresa|Permite que os usuários modifiquem qualquer configuração da empresa.|
|Criar e excluir espaços de trabalho|Permite aos usuários criar e excluir espaços de trabalho.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espaço de trabalho

Você pode dar a um usuário diferentes permissões para cada espaço de trabalho ao qual ele pertence no Braze. Para gerenciar as permissões no nível do espaço de trabalho, selecione **Select workspaces and permissions (Selecionar espaços de trabalho e permissões**) e, em seguida, escolha as permissões manualmente para selecionar ou atribuir um conjunto de permissões [criado anteriormente](#creating-a-permission-set).

Se você precisar dar a um usuário permissões diferentes para diferentes espaços de trabalho, repita este processo quantas vezes forem necessárias. Para uma descrição de cada permissão, consulte [Lista de permissões](#list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Permissões**, escolha uma ou mais permissões no menu suspenso. O Braze atribui essas permissões somente para os espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Ativar Acesso de Administrador** se desejar conceder a eles permissões totais para este espaço de trabalho.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo selecionadas manualmente no Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Conjuntos de permissão**, escolha um conjunto de permissões. O Braze atribui essas permissões somente para os espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo atribuídas por meio de um conjunto de permissões no Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportando permissões de usuário

Para baixar uma lista de seus usuários e suas permissões, acesse **Configurações** > **Usuários da empresa** e selecione **Exportar usuários**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

![A página "Company Users" (Usuários da empresa) no Braze com a opção "Export Users" (Exportar usuários) em destaque.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permissões

{% alert important %}
A partir de abril de 2024, para criar ou atualizar listas de códigos promocionais, os usuários do Braze precisam da permissão “Acessar Campanhas, canvas, Cartões, Segmentos, Biblioteca de Mídia”.
{% endalert %}

|Nível|Nome|Definição|
|---|---|---|
|Administrador|Administrador|Permite aos usuários acessar todos os recursos disponíveis. Esta é a configuração padrão para todos os novos usuários. Pode atualizar as configurações da empresa (nome da empresa e fuso horário), o que os usuários limitados não podem fazer.|
|Empresa|Criar e excluir espaços de trabalho|Permite aos usuários criar e excluir espaços de trabalho.|
|Empresa|Gerenciar configurações da empresa|Permite que os usuários modifiquem qualquer configuração da empresa.|
|Espaço de trabalho|Acesse Campanhas, canvas, Cartões, Blocos de Conteúdo, Flags de Recursos, Segmentos, Biblioteca de Mídia, Localizações, Códigos de Promoção e Centros de Preferências|Permite que os usuários visualizem as métricas de performance de campanhas e Canvas, criem e dupliquem rascunhos de campanhas e Canvas, editem rascunhos e modelos de campanhas e Canvas, visualizem rascunhos de segmentos, modelos e mídias, criem modelos, façam upload de mídias, criem ou atualizem listas de códigos de promoção, visualizem relatórios de engajamento e visualizem configurações globais de mensagens no dashboard. No entanto, os usuários com essa permissão não podem pausar ou editar conteúdo ao vivo existente.|
|Espaço de trabalho|Acessar console de desenvolvedores|Permite acesso total às seguintes configurações e logs:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Chaves de API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Grupos internos</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Registro de atividades de envio de mensagem</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Registro de usuários de eventos</a></li></ul>{:/}|
|Espaço de trabalho|Aprovar e rejeitar campanhas|Permite que os usuários aprovem ou rejeitem campanhas. O [fluxo de trabalho de aprovação para campanhas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta se quiser participar do acesso antecipado.|
|Espaço de trabalho|Aprovar e rejeitar canvas|Permite que os usuários aprovem ou neguem canvas. O [fluxo de trabalho de aprovação para canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve ser ativado para que essa permissão se aplique.|
|Espaço de trabalho|Editar integrações com o Currents|Permite que os usuários modifiquem uma conexão Currents, incluindo credenciais. Por padrão, os usuários atribuídos à permissão "Integrações Externas" também recebem essa permissão.|
|Espaço de trabalho|Editar segmentos|Permite aos usuários criar e editar segmentos. Você ainda pode criar campanhas com segmentos e filtros existentes sem essa permissão. Você precisa dessa permissão para gerar um segmento de usuários em um CSV ou redirecionar o grupo de usuários no CSV.|
|Espaço de trabalho|Exportar dados de usuários|Permite que os usuários exportem seus dados de usuários de segmentos, campanhas e canvas. Essa permissão inclui informações confidenciais do usuário, como nomes, envios de e-mail e outras informações de identificação pessoal (IPI) coletadas. Para exportar CSVs do dashboard, você deve ter essa permissão e a permissão "View IPI".|
|Espaço de trabalho|Importar e atualizar dados de usuários|Permite que os usuários importem arquivos CSV e atualizem arquivos de usuários do app, bem como visualizem a página de importação de usuário. Isso também permite que você edite o status de inscrição de um usuário e suas regras de aceitação/recusa de grupo de inscrições.|
|Espaço de trabalho|Lançar e gerenciar blocos de conteúdos|Permite que os usuários iniciem e gerenciem [blocos de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Espaço de trabalho|Abrir Centrais de Preferências|Permite que os usuários lancem [centros de preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Espaço de trabalho|Gerenciar apps|Permite que os usuários editem **Configurações do app**.|
|Espaço de trabalho|Permissão para gerenciar catálogos do dashboard|Permite aos usuários criar e gerenciar catálogos.|
|Espaço de trabalho|Gerenciar usuários do dashboard| Permite que os não administradores visualizem, editem e gerenciem a página **Usuários da empresa** e gerenciem os usuários do dashboard em seu espaço de trabalho, modificando as permissões de qualquer usuário, inclusive eles próprios. Os usuários com essa permissão não podem excluir usuários (somente os administradores podem excluir usuários).<br><br>Isso corresponde à permissão herdada `MANAGE_DEVELOPERS_AND_PERMISSIONS`.|
|Espaço de trabalho|Gerenciar configurações de e-mail|Permite que os usuários salvem as alterações de configuração de e-mail (**Configurações** > **Preferências de e-mail**).|
|Espaço de trabalho|Gerenciar eventos, atributos, compras|Permite que os usuários editem atributos personalizados (usuários sem essa capacidade ainda podem visualizar atributos personalizados), editem e visualizem propriedades de eventos personalizados e editem e visualizem propriedades de produtos em **Configurações de Dados**.|
|Espaço de trabalho|Gerenciar integrações externas|Permite o acesso a todas as guias em **Parceiros de tecnologia**, a capacidade de sincronizar o Braze com outras plataformas e o acesso para gerenciar [a ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Espaço de trabalho|Gerenciar Feature Flags|Permite que os usuários criem ou editem [flags de recursos]({{site.baseurl}}/developer_guide/feature_flags/).|
|Espaço de trabalho|Gerenciar ativos da biblioteca de mídia|Permite que os usuários adicionem, editem e excluam ativos da biblioteca de mídia.|
|Espaço de trabalho|Gerenciar grupos de inscrição|Permite que os usuários criem e gerenciem grupos de inscrição.|
|Espaço de trabalho|Gerenciar tags|Permite que os usuários editem ou excluam tags (sob **Gerenciamento de Tag**). Você não precisa dessa permissão para adicionar {tags} a campanhas ou segmentos.|
|Espaço de trabalho|Gerenciar equipes|Permite que os usuários gerenciem **Equipes Internas**. A capacidade de selecionar esta permissão depende do seu contrato com a Braze.<br><br>Isso corresponde à permissão herdada `MANAGE_TERRITORIES`.|
|Espaço de trabalho|Gerenciar transformações|Permite aos usuários criar e gerenciar Transformações de Dados.|
|Espaço de trabalho|Enviar campanhas, canvas|Permite que os usuários editem, arquivem e interrompam campanhas e canvas, criem campanhas e lancem canvas. |
|Espaço de trabalho|Ver informações de faturamento|Permite que os usuários visualizem assinaturas e faturamento.|
|Espaço de trabalho|Ver Integração do Currents|Permite que os usuários visualizem todas as informações sobre uma conexão Currents, excluindo credenciais. Por padrão, os usuários atribuídos à permissão "Acessar Campanhas, canvas, Cartões, Blocos de Conteúdo, Flags de Recursos, Segmentos, Biblioteca de Mídia, Localizações, Códigos de Promoção e Centros de Preferências" também recebem essa permissão.|
|Espaço de trabalho|Ver atributos personalizados marcados como IPI|Permite que usuários não administradores visualizem atributos personalizados que contenham informações confidenciais e estejam marcados como informações de identificação pessoal (IPI).|
|Espaço de trabalho|Ver IPI|Permite que os usuários visualizem os campos de informações de identificação pessoal (IPI) conforme definido pela sua empresa no dashboard. Os usuários também podem visualizar os campos de IPI na guia **Preview as a User** das prévias de mensagens.<br><br>Você precisa dessa permissão para usar o [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), pois ele permite o acesso direto a alguns dados de clientes. Para exportar CSVs do dashboard, os usuários precisam dessa permissão e da permissão "Exportar dados de usuários".|
|Espaço de trabalho|Ver perfis de usuário em conformidade com IPI|Permite que os usuários visualizem perfis de usuários que contenham campos que sua empresa definiu como informações de identificação pessoal (IPI), mas os campos de IPI são redigidos.<br><br>Você precisa dessa permissão para usar a ferramenta de pesquisa de usuários. |
|Espaço de trabalho|Ver transformações|Permite que os usuários visualizem [Transformações de Dados do Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|Espaço de trabalho|Ver dados de uso|Permite que os usuários visualizem o uso do app, incluindo os painéis de desempenho do canal.|
|Espaço de trabalho|Mesclar usuários duplicados|Permite que os usuários mesclem perfis de usuário duplicados.|
|Espaço de trabalho|Prévia de usuários duplicados|Permite que os usuários vejam uma prévia de quais perfis de usuário estão duplicados.|
|Espaço de trabalho|Criar e editar modelos de canva|Permite que os usuários criem e editem modelos do Canva.|
|Espaço de trabalho|Ver modelos de canva|Permite que os usuários visualizem os modelos do Canva.|
|Espaço de trabalho|Arquivar modelos de canva|Permite que os usuários arquivem modelos do Canva.|
|Espaço de trabalho|Gerenciar segmentação de propriedades personalizadas de eventos|Permite que os usuários criem segmentos com base na recência e na frequência da propriedade do evento.|
|Espaço de trabalho|Publicar landing page|Permite que os usuários publiquem [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|Espaço de trabalho|Criar rascunhos de landing page|Permite que os usuários criem e salvem rascunhos de landing page.|
|Espaço de trabalho|Acessar landing page|Permite que os usuários acessem a página **Landing Pages**.|
|Espaço de trabalho|Criar e editar modelos de landing page|Permite que os usuários criem e editem modelos de landing page.|
|Espaço de trabalho|Exibir modelos de landing page|Permite que os usuários visualizem modelos de landing page.|
|Espaço de trabalho|Arquivar modelos de landing page|Permite que os usuários arquivem modelos de landing page.|
|Espaço de trabalho|Exibir agentes de IA personalizados|Permite que os usuários visualizem [agentes de IA personalizados]({{site.baseurl}}/user_guide/brazeai/agents/). Esse recurso está em beta.|
|Espaço de trabalho|Criar agentes de IA personalizados|Permite que os usuários criem agentes de IA personalizados. Esse recurso está em beta.|
|Espaço de trabalho|Editar agentes de IA personalizados|Permite que os usuários editem agentes de IA personalizados. Esse recurso está em beta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
