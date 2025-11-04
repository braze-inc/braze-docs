---
nav_title: BlueConic
article_title: BlueConic
description: "Este artigo de referência descreve a parceria entre o Braze e a BlueConic, uma plataforma líder de dados do cliente, permitindo que você unifique os dados em perfis individuais persistentes e, em seguida, sincronize-os entre os dois sistemas para metas de importação por meio de um servidor Amazon S3 do Amazon Web Services."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [A BlueConic](https://www.blueconic.com/), a principal plataforma de dados do cliente, libera os dados primários das empresas de sistemas díspares e os torna acessíveis onde e quando forem necessários para transformar os relacionamentos com os clientes e impulsionar o crescimento dos negócios. 

_Essa integração é mantida pela Blueconic._

## Sobre a integração

A integração entre Braze e BlueConic permite que os usuários unifiquem os dados em perfis individuais persistentes e, em seguida, sincronizem-nos entre os dois sistemas para metas de importação por meio de um servidor Amazon Web Services S3. As possíveis metas incluem iniciativas voltadas para o crescimento, orquestração do ciclo de vida do cliente, modelagem e análise de dados, produtos e experiências digitais, monetização baseada no público e muito mais. Essa integração oferece suporte à importação e exportação em lote programadas. 

{% alert important %}
Ao usar a integração, a BlueConic enviará deltas (dados alterados) em cada sincronização. Isso inclui todos os perfis que foram alterados desde o último envio e todas as atribuições desse perfil. Monitore o uso de pontos de dados adequadamente.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta BlueConic | É necessário ter uma [conta BlueConic](https://www.blueconic.com/) para usar a parceria. Você precisará de acesso para [visualizar e editar conexões](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles) na sua conta BlueConic para acessar os plug-ins. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com as permissões `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists` e `segments.details`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze | Sua URL de endpoint REST. Seu endpoint dependerá do [URL do Braze para sua instância](https://portal.aws.amazon.com/billing/signup#/start). |
| Autenticação S3 | Você precisará de acesso a um servidor Amazon Web Services (S3) para exportar e importar os dados. |
| Acessar ID da chave<br>Chave de acesso de segredo | O ID da chave de acesso e a chave de acesso secreta permitirão que você autentique seu servidor S3 para importação e exportação. |
| Bucket AWS | Você precisará se conectar ao S3 dentro do plug-in. Após a autenticação, os buckets disponíveis serão exibidos em um menu suspenso. É onde os arquivos a serem importados ou exportados são armazenados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integração

### Etapa 1: Criando uma conexão Braze

Na BlueConic, selecione **Connections** (Conexões) na barra de navegação e depois **Add Connection** (Adicionar conexão). No prompt que aparece, pesquise **Braze** e selecione **Braze connection** (Conexão com a Braze). 

Expanda ou recolha os campos de metadados disponíveis na conexão clicando no ícone de chevron cinza. Nesses campos, você pode favoritar essa conexão, nomear sua conexão, adicionar rótulos, incluir uma descrição e optar por receber notificações por e-mail se a conexão [for executada ou não for executada](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ). 

Salve as configurações.

### Etapa 2: Configuração de uma conexão Braze

Para configurar a conexão entre a BlueConic e o Braze, você deve adicionar as credenciais da sua conta do Braze e as informações da conta do Amazon Web Services (S3) para autenticar a conexão. 

1. Na BlueConic, selecione **Set up and run (Configurar e executar** ) na seção **Setup (Configuração)** no painel esquerdo.<br><br>
2. Na página de autenticação da Braze que se abre, insira seu endpoint da API REST da Braze e a chave da API da Braze.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. Na seção de configuração e autenticação do S3, insira estas credenciais: ID da chave de acesso do Amazon Web Services (S3), chave de acesso secreta e bucket S3. Elas precisam ser as [mesmas credenciais]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) que você configurou ao definir a integração entre o Braze e o Amazon S3. Salve as configurações. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### Etapa 3: Criação de metas de importação ou exportação (mapeamento de importação)

Depois que a autenticação for concluída, você deverá criar pelo menos uma meta de importação ou exportação, ativar a conexão e agendar ou executar a conexão.

{% tabs %}
{% tab Importação %}

1. Selecione **Importar dados para a BlueConic** no painel esquerdo para abrir a página de configuração de dados do Braze.<br><br>
2. Selecione o local dos dados no Braze. Aqui, você pode dizer à BlueConic onde encontrar os dados a serem importados, selecionando seu público Braze.<br>![O público da BlueConic Braze foi definido como "Usuários de teste da BlueConic".]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Em seguida, mapeie os identificadores entre a Braze e a BlueConic. <br>![O campo "External ID" da Braze foi definido para mapear o campo "Braze external ID" (ID externo da Braze) da BlueConic.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Para vincular os dados de clientes entre os dois sistemas, insira um ou mais identificadores de clientes.<br>Use a caixa de seleção **Allow creation... (Permitir criação...)** para permitir que a BlueConic crie novos perfis para dados que não correspondam a um perfil BlueConic existente.<br><br>
4. Em seguida, corresponda os campos de dados da BlueConic da exportação aos campos da Braze. Use os campos suspensos para selecionar o identificador de perfil BlueConic ou uma propriedade de perfil à esquerda e selecione o identificador de perfil Braze correspondente. Em seguida, use o menu suspenso para especificar como o conteúdo importado deve ser adicionado aos valores existentes: adicionado, somado, definido somente se a propriedade de perfil estiver vazia ou definido como limpo (se o campo Braze estiver vazio).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Use o botão **Add Mapping** para criar linhas de mapeamento adicionais, conforme necessário. Você pode adicionar várias linhas de mapeamento com a opção **Adicionar campos restantes**. A BlueConic detecta os campos Braze restantes e os combina com as propriedades do perfil BlueConic. Você pode definir a estratégia de mesclagem para importações (definir, adicionar, somar, definir se vazio ou limpar) e fornecer um prefixo personalizado para os nomes das propriedades do perfil BlueConic.<br><br>
5. Por fim, selecione **Run the connection** (Executar a conexão) para iniciar a conexão. Visite a [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) para saber mais sobre agendamento e execução de conexões.
{% endtab %}
{% tab Exportação %}

1. Selecione **Exportar dados para o Braze** no painel esquerdo para configurar sua exportação de dados da BlueConic para o Braze.<br><br>
2. Escolha um segmento BlueConic para a exportação. Somente os perfis desse segmento com identificadores correspondentes no Braze serão exportados.<br>![Um segmento BlueConic de 20 mil perfis.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. Em seguida, vincule os identificadores entre os perfis BlueConic e os campos Braze. Opcionalmente, você pode optar por permitir que a BlueConic crie novos registros se nenhuma correspondência existente for encontrada.<br>![O campo "External ID" da Braze foi definido para mapear o campo "Braze external ID" (ID externo da Braze) da BlueConic.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. Em seguida, corresponda os campos de dados da BlueConic da exportação aos campos da Braze. Use o menu suspenso do ícone da BlueConic para escolher o tipo de [informação](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) que deseja exportar. As informações disponíveis incluem propriedades de perfil, identificadores de perfil BlueConic, segmentos associados, todas as interações visualizadas, níveis de permissão e um valor de texto estático.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Por fim, clique em **Run the connection** (Executar a conexão) para iniciar a conexão. Visite a [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) para saber mais sobre agendamento e execução de conexões.
{% endtab %}
{% endtabs %}

## Etapa 4: Ativar a conexão

Use o botão de alternância ao lado do título da conexão da Braze para ativar e desativar a conexão. Uma conexão deve estar ativada para ser executada durante os horários programados. 


