---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "Este artigo de referência descreve a parceria entre a Braze e o Dynamics 365 Customer Insights, uma plataforma de dados do cliente líder no mercado, que permite exportar segmentos de clientes para a Braze para usar em campanhas ou canvas."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights
 
> O [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) é uma plataforma empresarial de dados de cliente líder que oferece experiências personalizadas aos clientes com uma visão de 360 graus.

_Esta integração é mantida pelo Dynamics 365 Customer Insights._

## Sobre a integração

A integração entre o Braze e o Dynamics 365 Customer Insights permite que você exporte segmentos de clientes para o Braze para usar em campanhas ou canvas.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Dynamics 365 Customer Insights | É necessário ter uma conta [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) para usar a parceria. Você precisará de acesso como administrador para visualizar e editar conexões dentro da sua conta do Dynamics 365 Customer Insights para acessar os plugins necessários. |
| Chave da API REST do Braze | Uma chave da API REST do Braze é necessária com `users.track` e `users.export.segment` permissões. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Identificadores de perfil correspondentes | Os perfis de clientes unificados nos segmentos exportados contêm um campo representando um endereço de e-mail e um Braze `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Configurar conexão Braze

No Customer Insights, navegue para **Admin > Connections** (Admin > Conexões). Em seguida, selecione **Adicionar conexões** e escolha **Braze** para configurar a conexão. 

1. Dê à sua conexão um nome reconhecível no campo **Nome de exibição**. 
2. Escolha quem pode usar esta conexão. Se você deixar este campo em branco, o padrão será Administradores. Para saber mais, consulte [Permitir que os colaboradores usem uma conexão para exportações](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Forneça sua chave de API do Braze e o endpoint REST no formato `rest.iad-03.braze.com`.
4. Selecione **Concordo** para confirmar a conformidade com os dados e a privacidade.
5. Selecione **Conectar** para iniciar a conexão com a Braze.
6. Selecione **Add yourself as export user** (Adicione-se como usuário de exportação) e forneça suas credenciais do Customer Insights.
7. Selecione **Salvar** para concluir a conexão.

### Etapa 2: Crie um Segmento Braze

1. No Braze, acesse **público** > **Segmentos**.
2. Crie um segmento dos usuários que você deseja que a Microsoft atualize através do Dynamics 365 Customer Insights.
3. Capture o **Identificador da API** do segmento

### Etapa 3: Configurar uma exportação

Você pode configurar esta exportação se tiver acesso a uma conexão deste tipo. Para saber mais, consulte [Visão geral das exportações](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. No Customer Insights, acesse **Data > Exports** (Dados > Exportações). Para criar uma nova exportação, selecione **Add destination** (Adicionar destino).
2. No campo **Conexão para exportação**, selecione uma conexão para a seção Braze. Se esse nome de seção não aparecer, isso significa que não há conexões desse tipo disponíveis para você.
3. Forneça o identificador da API do segmento no Braze.
4. Na seção **Data matching**, no campo **e-mail**, selecione o campo que representa o endereço de e-mail de um cliente. Em seguida, no campo **ID do Cliente Braze**, selecione o campo que representa o ID do cliente no Braze. Você também pode selecionar um campo adicional e opcional para correspondência de dados.
  a. Se você mapear o `external_id` no Braze para o campo de ID do cliente Braze no Customer Insights, os registros existentes serão atualizados no Braze ao exportar.
  b. Se você mapear um campo de ID diferente que não representa o `external_id` de um registro no Braze, ou um campo vazio, novos registros serão criados no Braze ao exportar.
5. Por fim, selecione os segmentos que deseja exportar e selecione **Salvar**. 

Observe que o salvamento da exportação não a executa imediatamente. Esta exportação será executada com cada [atualização programada](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). Você também pode [exportar dados sob demanda](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand). 


### Usando essa integração

Após seus segmentos serem exportados com sucesso para o Braze, você pode encontrá-los como atributos personalizados nos perfis de usuário. O atributo personalizado será nomeado com o identificador da API do segmento Braze que foi inserido ao configurar a conexão de exportação. Por exemplo, `"Segment_API_Identifier": "0000-0000-0000"`

Para criar um segmento desses usuários no Braze, navegue até **Segmentos**, crie um novo segmento e selecione **Atributos Personalizados** como seu filtro. A partir daqui, você pode escolher o atributo personalizado sincronizado do Dynamics 365. Depois que o segmento é criado, você pode selecioná-lo como um filtro de público ao criar uma campanha ou canva.

{% alert note %}
Para saber mais sobre a integração, visite o artigo de [integração](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) com a Braze criado pela Microsoft.
{% endalert %}


