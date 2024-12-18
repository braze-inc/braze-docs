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
{% tab exemplo de conjuntos de permissões %}
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
{% tab exemplos de funções %}
| Nome do Papel | espaço de trabalho | Permissões  
----------- | ----------- | ---------
| profissional de marketing - Marcas de Moda | {::nomarkdown}[DEV] Marca de Moda, [QA] Marca de Moda, [PROD] Marca de Moda {:/} | “Acesse Campanhas, canvas, Cartões, Flags de Recursos, Segmentos, Biblioteca de Mídia e Central de Preferências"<br>“Gerenciar ativos da biblioteca de mídia” |
| profissional de marketing - Marcas de Cuidados com a Pele | {::nomarkdown}[DEV] Marca de Cuidados com a Pele, [QA] Marca de Cuidados com a Pele, [PROD] Marca de Cuidados com a Pele {:/} | “Acesse Campanhas, canvas, Cartões, Flags de Recursos, Segmentos, Biblioteca de Mídia e Centros de Preferências” <br>“Gerenciar ativos da biblioteca de mídia” |
| Gerenciamento de Usuários - Todas as Marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | “Gerenciar Usuários do Dashboard”<br>“Gerenciar equipes” |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

### Como os conjuntos de permissões e as funções diferem das equipes?

Consulte [Usuários da empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) para obter um detalhamento das diferenças entre equipes, conjuntos de permissões e funções.

## Editando as permissões de um usuário

Para editar as permissões atuais de [admin](#admin), [empresa](#company) ou [espaço de trabalho](#workspace) de um usuário, Acessar **Configurações** > **Usuários da Empresa**, depois selecione o nome deles.

![A página "Usuários da Empresa" no Braze com um usuário listado nos resultados.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

### Administrador

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Há também algumas coisas que apenas os administradores podem fazer no Braze. 

Apenas administradores podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Adicionar, editar, excluir, suspender ou reativar outros [Braze usuários]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Exportar usuários do Braze como um CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador**, depois selecione **Atualizar usuário**.

![Os detalhes do usuário selecionado com a caixa de seleção de administrador em foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar o Braze até que você atribua a ele pelo menos uma permissão [no nível da empresa](#company) ou [no nível do espaço de trabalho](#workspace).
{% endalert %}

### Empresa

Para gerenciar as seguintes permissões a nível de empresa para um usuário, marque ou desmarque a caixa ao lado dessa permissão. Quando terminar, selecione **Atualizar usuário**.

|Nome da permissão|Descrição|
|----------|-----------|
|Gerenciar configurações da empresa|Permite que os usuários modifiquem qualquer configuração da empresa.|
|Criar e excluir espaços de trabalho|Permite aos usuários criar e excluir espaços de trabalho.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaço de trabalho

Você pode dar a um usuário diferentes permissões para cada espaço de trabalho ao qual ele pertence no Braze. Para gerenciar suas permissões de nível de espaço de trabalho, selecione **Selecionar espaços de trabalho e permissões**, depois escolha suas permissões manualmente ou atribua um conjunto de permissões [que você criou anteriormente](#creating-a-permission-set).

Se você precisar dar a um usuário permissões diferentes para diferentes espaços de trabalho, repita este processo quantas vezes forem necessárias. Para uma descrição de cada permissão, consulte [Lista de permissões](#list-of-permissions).

{% tabs local %}
{% tab selecione manualmente %}
Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Permissões**, escolha uma ou mais permissões no menu suspenso. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Ativar Acesso de Administrador** se desejar conceder a eles permissões totais para este espaço de trabalho.

Quando terminar, selecione **Atualizar usuário**.

![Permissões de espaço de trabalho sendo selecionadas manualmente na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})
{% endtab %}

{% tab atribuir conjunto de permissões %}
Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Conjuntos de permissão**, escolha um conjunto de permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões de nível de espaço de trabalho sendo atribuídas por meio de um conjunto de permissões na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})
{% endtab %}
{% endtabs %}

## Exportando permissões de usuário

Para baixar a lista de seus usuários e suas permissões, acesse **Configurações** > **Usuários da Empresa**, depois selecione **Exportar Usuários**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

![A página "Usuários da Empresa" no Braze com a opção "Exportar Usuários" em foco.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permissões

{% alert important %}
A partir de abril de 2024, para criar ou atualizar listas de códigos promocionais, os usuários do Braze precisam da permissão “Acessar Campanhas, canvas, Cartões, Segmentos, Biblioteca de Mídia”.
{% endalert %}

|Nível|Nome|Definição|
|---|---|---|
|Administrador|Administrador|Permite aos usuários acessar todos os recursos disponíveis. Esta é a configuração padrão para todos os novos usuários. Pode atualizar as configurações da empresa (nome da empresa e fuso horário), o que os usuários limitados não podem fazer.|
|Empresa|Criar e excluir espaços de trabalho|Permite aos usuários criar e excluir espaços de trabalho.|
|Empresa|Gerenciar configurações da empresa|Permite que os usuários modifiquem qualquer configuração da empresa.|
|Espaço de trabalho|Acesse Campanhas, canvas, Cartões, Blocos de Conteúdo, Flags de Recursos, Segmentos, Biblioteca de Mídia, Localizações, Códigos de Promoção e Centros de Preferências|Permite que os usuários visualizem as métricas de performance de campanhas e Canvas, criem e dupliquem rascunhos de campanhas e Canvas, editem rascunhos e modelos de campanhas e Canvas, visualizem rascunhos de Feed de notícias, segmentos, modelos e mídias, criem modelos, façam upload de mídia, criem ou atualizem listas de códigos de promoção, visualizem relatórios de engajamento e visualizem configurações globais de mensagens no painel. No entanto, os usuários com essa permissão não podem pausar ou editar conteúdo ao vivo existente.|
|Espaço de trabalho|Acessar console de desenvolvedores|Permite acesso total às seguintes configurações e logs:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Chaves de API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Grupos internos</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Registro de atividades de envio de mensagem</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Registro de usuários de eventos</a></li><li><a href='/docs/user_guide/data_and_analytics/cloud_ingestion/'>Gerenciar Ingestão de Dados na Nuvem</a></li></ul>{:/}|
|Espaço de trabalho|Aprovar e rejeitar campanhas|Permite que os usuários aprovem ou rejeitem campanhas. O [fluxo de trabalho de aprovação para campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta se quiser participar do acesso antecipado.|
|Espaço de trabalho|Aprovar e rejeitar canvas|Permite que os usuários aprovem ou neguem canvas. O [fluxo de trabalho de aprovação para canvas]({{site.baseurl}}/canvas_approval) deve ser ativado para que essa permissão se aplique.|
|Espaço de trabalho|Editar integrações com o Currents|Permite que os usuários modifiquem uma conexão Currents, incluindo credenciais. Por padrão, os usuários atribuídos à permissão "Integrações Externas" também recebem essa permissão.|
|Espaço de trabalho|Editar segmentos|Permite aos usuários criar e editar segmentos. Você ainda pode criar campanhas com segmentos e filtros existentes sem essa permissão. Você precisa dessa permissão para gerar um segmento de usuários em um CSV ou redirecionar o grupo de usuários no CSV.|
|Espaço de trabalho|Exportar dados de usuários|Permite que os usuários exportem seus dados de usuários de segmentos, campanhas e canvas.|
|Espaço de trabalho|Importar e atualizar dados de usuários|Permite que os usuários importem arquivos CSV e atualizem arquivos de usuários do app, bem como visualizem a página de importação de usuário. Isso também permite que você edite o status de inscrição de um usuário e suas regras de aceitação/recusa de grupo de inscrições.|
|Espaço de trabalho|Lançar Blocos de Conteúdo|Permite que os usuários lancem [Blocos de Conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Espaço de trabalho|Abrir Centrais de Preferências|Permite que os usuários lancem [centros de preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Espaço de trabalho|Gerenciar apps|Permite que os usuários editem **Configurações do app**.|
|Espaço de trabalho|Permissão para gerenciar catálogos do dashboard|Permite aos usuários criar e gerenciar catálogos.|
|Espaço de trabalho|Gerenciar usuários do dashboard|Permite que os usuários visualizem, editem e gerenciem a página de **Usuários da Empresa**. Usuários com esta permissão podem modificar as permissões de qualquer usuário, incluindo eles próprios. Como tal, esta permissão deve ser vista como um nível de acesso administrativo. Esta permissão não permite que os usuários excluam usuários porque apenas os administradores podem excluir usuários.|
|Espaço de trabalho|Gerenciar configurações de e-mail|Permite que os usuários salvem as alterações de configuração de e-mail (**Configurações** > **Preferências de e-mail**).|
|Espaço de trabalho|Gerenciar eventos, atributos, compras|Permite que os usuários editem atributos personalizados (usuários sem essa capacidade ainda podem visualizar atributos personalizados), editem e visualizem propriedades de eventos personalizados e editem e visualizem propriedades de produtos em **Configurações de Dados**.|
|Espaço de trabalho|Gerenciar integrações externas|Permite acesso a todas as guias em **Tecnologia Parceiros** e a capacidade de sincronizar a Braze com outras plataformas.|
|Espaço de trabalho|Gerenciar Feature Flags|Permite que os usuários criem ou editem [flags de recursos]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/).|
|Espaço de trabalho|Gerenciar ativos da biblioteca de mídia|Permite que os usuários adicionem, editem e excluam ativos da biblioteca de mídia.|
|Espaço de trabalho|Gerenciar grupos de inscrição|Permite que os usuários criem e gerenciem grupos de inscrição.|
|Espaço de trabalho|Gerenciar tags|Permite que os usuários editem ou excluam tags (sob **Gerenciamento de Tag**). Você não precisa dessa permissão para adicionar {tags} a campanhas ou segmentos.|
|Espaço de trabalho|Gerenciar equipes|Permite que os usuários gerenciem **Equipes Internas**. A capacidade de selecionar esta permissão depende do seu contrato com a Braze.|
|Espaço de trabalho|Gerenciar transformações|Permite aos usuários criar e gerenciar Transformações de Dados.|
|Espaço de trabalho|Publicar cartões|Esta permissão só é visível se a sua conta estiver habilitada para o feed de notícias, que está sendo descontinuado. Isso não afeta os Cartões de Conteúdo. Permite que os usuários criem e editem cards de feed de notícias. Você ainda pode ver os cards do feed de notícias sem esta permissão. Se a sua conta estiver habilitada para o feed de notícias e um usuário puder lançar Blocos de Conteúdo existentes, ele precisará das permissões "Publicar Cartões" e "Lançar Blocos de Conteúdo".|
|Espaço de trabalho|Enviar campanhas, canvas|Permite que os usuários editem, arquivem e interrompam campanhas e canvas, criem campanhas e lancem canvas.|
|Espaço de trabalho|Ver informações de faturamento|Permite que os usuários visualizem assinaturas e faturamento.|
|Espaço de trabalho|Ver Integração do Currents|Permite que os usuários visualizem todas as informações sobre uma conexão Currents, excluindo credenciais. Por padrão, os usuários atribuídos à permissão "Acessar Campanhas, canvas, Cartões, Blocos de Conteúdo, Flags de Recursos, Segmentos, Biblioteca de Mídia, Localizações, Códigos de Promoção e Centros de Preferências" também recebem essa permissão.|
|Espaço de trabalho|Ver atributos personalizados marcados como IPI|Permite que este usuário visualize atributos personalizados que são marcados como IPI sem ser um administrador.|
|Espaço de trabalho|Ver IPI|Permite que os usuários visualizem os campos de informações pessoalmente identificáveis conforme definido pela sua empresa no dashboard.|
|Espaço de trabalho|Ver perfis de usuário em conformidade com IPI|Permite que os usuários vejam perfis de usuários, mas editem campos que a sua empresa definiu como informações pessoalmente identificáveis (IPI).|
|Espaço de trabalho|Ver transformações|Permite que os usuários visualizem [Transformações de Dados do Braze]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/).|
|Espaço de trabalho|Ver dados de uso|Permite que os usuários visualizem o uso do app, incluindo os painéis de desempenho do canal.|
|Espaço de trabalho|Mesclar usuários duplicados|Permite que os usuários mesclem perfis de usuário duplicados.|
|Espaço de trabalho|Prévia de usuários duplicados|Permite que os usuários vejam uma prévia de quais perfis de usuário estão duplicados.|
|Espaço de trabalho|Criar e editar modelos de canva|Permite que os usuários criem e editem modelos do Canva.|
|Espaço de trabalho|Ver modelos de canva|Permite que os usuários visualizem os modelos do Canva.|
|Espaço de trabalho|Arquivar modelos de canva|Permite que os usuários arquivem modelos do Canva.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
