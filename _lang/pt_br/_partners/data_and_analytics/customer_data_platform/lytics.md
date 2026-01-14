---
nav_title: Lítica
article_title: Lítica
description: "Este artigo de referência aborda a integração entre a Braze e a Lytics. A Lytics é uma plataforma empresarial de dados do cliente para profissionais de marketing, analistas e tecnólogos. Essa integração permite que as marcas sincronizem e mapeiem seus dados do Lytics diretamente no Braze."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lítica

> A [Lytics](https://www.lytics.com/) é a plataforma de dados do cliente (CDP) preferida para a próxima geração de empresas centradas no cliente. As soluções Lytics Decision Engine, Conductor e Cloud Connect oferecem aos profissionais de marketing e às equipes de dados oportunidades de realizar resolução de identidade, orquestração e otimização de campanhas em tempo real e em conformidade com a privacidade.

_Essa integração é mantida pela Lytics._

## Sobre a integração

A integração entre o Braze e o Lytics fornece uma visão unificada de seus clientes para ativar uma personalização poderosa e conduzir campanhas otimizadas usando a próxima melhor orquestração de ações e decisões.

A integração permite que as marcas:

- Exportem públicos para a Braze diretamente da Lytics
- Envie eventos de campanhas do Braze ou canvas para o Lytics em tempo real para campanhas personalizadas e para criar perfis de usuários avançados

## Casos de uso

Conecte o Braze ao Lytics para [importar](#importing-data-from-braze-to-lytics) atividades de e-mail, SMS e push para enriquecer os perfis de usuário do Lytics. Usando a Braze e a Lytics em conjunto, você também pode [exportar](#integration) os públicos orientados por comportamento e entre canais da Lytics para criar jornadas de clientes altamente personalizadas na Braze usando dados primários.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Lytics | É necessário ter uma conta do Lytics para aproveitar essa integração. |
| Número da conta da Lytics | É necessário um número de conta do Lytics para configurar o URL do endpoint do webhook. |
| Token da API da Lytics | Um token da API REST da Lytics com permissões de gerenciamento de dados. <br><br> Isso pode ser criado no dashboard da Lytics, em **Account Settings Console** > **Access Tokens** > **Create New Token** (Console de configurações da conta > Tokens de acesso > Criar novo token). |
| Chave da API REST do Braze | Uma chave da API REST do Braze com permissão `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instâncias da Braze | Sua [instância do Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Entre em contato com o gerente de integração da Braze para obter essas informações se não tiver certeza. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Esta seção descreve como exportar dados do Lytics para o Braze.

### Etapa 1: Criar uma autorização

No Lytics, navegue até o dashboard **Authorization (Autorização** ) no console **Data (Dados)** na barra de navegação. Selecione **Create New Authorization (Criar nova autorização** ), procure e selecione **Braze**.

No prompt **Configure Authorization** (Configurar autorização) exibido, forneça um rótulo e uma descrição e insira sua chave da API REST e a instância da Braze. Selecione **Complete** quando terminar.

![]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### Etapa 2: Criar um novo trabalho

Na Lytics, navegue até o dashboard **Jobs** (Trabalhos) dentro do console **Dados** (Data) na barra de navegação. Selecione **Create New Job (Criar novo trabalho** ), procure e selecione **Braze**.  No prompt **Select Job Type**(Selecionar tipo de trabalho) exibido, selecione **Export Audience** (Exportar público).

![]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

Em seguida, escolha uma autorização nas opções **Select Authorization** (Selecionar autorização).

![]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### Etapa 3: Configurar o trabalho

No prompt **Configure Job** (Configurar trabalho), forneça um rótulo e uma descrição opcional. Em seguida, na entrada **Braze External User ID Field (Campo de ID de usuário externo do Braze** ), selecione o campo no Lytics que contém o ID de usuário externo do Braze (`braze_id`). A próxima etapa é a mais importante - selecione os públicos a serem exportados para o Braze.

![]({% image_buster /assets/img/lytics/braze_job.png %}){: style="max-width:80%;"}

Por fim, escolha a opção preferível para a caixa de seleção **Existing Users (Usuários existentes** ). Deixar essa caixa marcada adicionará usuários que já existem no público selecionado do Lytics. Se desmarcada, os usuários só serão exportados para o Braze quando entrarem ou saírem do público após o início do fluxo de trabalho.

{% alert note %}
Ao marcar essa caixa, todos os usuários existentes no público selecionado serão empurrados para o Braze. Isso resultará na ocorrência de um ponto de dados por usuário e por público para a sincronização inicial.
{% endalert %}

Clique em **Complete (Concluir** ) quando terminar para iniciar a exportação e salvar.

![]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

Depois que o trabalho de exportação for configurado, o Lytics enviará os públicos selecionados para o Braze por meio da integração nativa. A seguir, mostramos um exemplo de público com a estrutura JSON do público enviado à Braze.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Um novo usuário será criado no Braze para qualquer `external_id` incluído na exportação do público que ainda não exista no Braze. 

## Importação de dados do Braze para o Lytics

Você pode importar dados de público da Braze para a Lytics usando os seguintes métodos:

- [Usando webhooks](#using-webhooks)
- [De um arquivo CSV](#from-a-csv-file)

### Usando webhooks

#### Etapa 1: Criar um token da API do Lytics

Navegue até o Lytics Account Menu (Menu da conta do Lytics) no canto inferior esquerdo selecionando o nome da sua conta e selecione **Access Tokens (Tokens de acesso** ) no menu suspenso. Em seguida, selecione **Create API Token (Criar token de API)**

![]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

Insira um nome, uma descrição opcional e um período de expiração do token. Em seguida, alterne o escopo do **Data Manager** (Gerenciador de dados) para permissões de API e clique em **Generate Token** (Gerar token). Copie o token e armazene-o em um local seguro.

![]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### Etapa 2: Configurar o URL do webhook do Lytics

O URL do webhook da Lytics é usado pela Braze para enviar uma mensagem para a API da Lytics a partir da Braze. Essa mensagem pode ser usada para personalizar suas campanhas de mensagens no Lytics ou pode ser usada para enriquecer seu perfil de cliente do Lytics. Os dois parâmetros a seguir devem ser adicionados ao URL do webhook da Lytics:

- Número da conta do Lytics
- Token da API da Lytics

Configure o URL do webhook da seguinte forma:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Substitua `<ACCOUNT-NUMBER>` pelo número de sua conta e `<LYTICS-API-TOKEN>` pelo token da API do Lytics.

#### Etapa 3: Criar um Webhook no Braze 

No Braze, crie uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). Adicione o URL do webhook do Lytics no campo **URL do webhook**.

Após definir o tipo de solicitação (método HTTP `POST`) e configurar o restante dos detalhes do webhook, o webhook estará pronto para testes e implantação. Aqui está um exemplo de corpo da solicitação POST após a configuração do webhook na Braze:

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "John",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@email.com",
  "braze_id": "xxxxxx" 
}
```

### De um arquivo CSV

Esta seção descreve como fazer a importação de dados de usuários do Braze de um segmento para o Lytics.

#### Etapa 1: Criar uma autorização

No Lytics, navegue até o dashboard **Authorization (Autorização** ) no console **Data (Dados)** na barra de navegação. Selecione **Create New Authorization (Criar nova autorização** ), procure e selecione **Custom Integrations (Integrações personalizadas**).

Selecione o tipo preferido de autorização SFTP com base nos seus requisitos comerciais e de segurança. Os seguintes tipos de autorização são compatíveis com a importação de arquivos para o Lytics via SFTP:

- Autorização do servidor SFTP do cliente
- Autorização do servidor SFTP do cliente com chave privada PGP
- Autorização do servidor SFTP gerenciado do Lytics

As autorizações SFTP de chave pública são apenas para exportação SFTP.

![]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

No prompt **Configure Authorization (Configurar autorização)** exibido, forneça um rótulo e uma descrição e preencha o restante dos requisitos de configuração. Clique em **Complete** quando terminar.

#### Etapa 2: Exportar seus dados de segmento para CSV

Na Braze, navegue até **Público** > **Segmentos**. Localize o segmento que deseja exportar e selecione <i class="fas fa-gear" aria-label="Configurações"></i> e, em seguida, **Exportar dados de usuários em CSV**. É possível exportar até 500.000 usuários em um segmento. Para obter detalhes, consulte [Exportação de dados de segmento para CSV]({{site.baseurl}}/user_guide/data/export_braze_data/segment_data_to_csv/).

#### Etapa 3: Configurar um trabalho de importação de CSV

Na Lytics, navegue até o dashboard **Jobs** (Trabalhos) dentro do console **Dados** (Data) na barra de navegação. Selecione **Create New Job (Criar novo trabalho** ), procure e selecione **Custom Integrations (Integrações personalizadas**).

Depois selecione o tipo de trabalho. Para importar arquivos CSV da Braze para a Lytics, selecione **Import CSV** (Import CSV) como o tipo de trabalho.

![]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

Por fim, insira um rótulo e uma descrição opcional para o trabalho e configure outros detalhes necessários. Clique em **Complete** para iniciar e salvar o trabalho.







