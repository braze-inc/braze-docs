---
nav_title: Acessar o Decisioning Studio
article_title: Acessar o BrazeAI Decisioning Studio
page_order: 0
description: "Saiba como configurar e integrar o BrazeAI Decisioning <sup>StudioTM</sup> Acessar o Braze."
---

# BrazeAI Decisioning Studio™ Acessar

> Localize as principais informações no Braze para iniciar a integração com o BrazeAI Decisioning Studio™ Acessar.

## Essenciais

### Criação de uma chave da API REST no Braze

Para criar uma nova chave da API REST:

1. No dashboard do Braze, vá para **Configurações** > **APIs e identificadores** > **Chaves de API**.
2. Selecione **Create API Key (Criar chave de API**).
3. Digite um nome para sua chave de API. Um exemplo é "DecisioningStudioGoEmail".
4. Selecione as permissões com base nas seguintes categorias:
    - **Dados de usuários:** selecione `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Envio de mensagens:** selecione `messages.send`
    - **Campanhas:** selecione todas as permissões listadas
    - **Canva:** selecione todas as permissões listadas
    - **Segmentos:** selecione todas as permissões listadas
    - **Modelos:** selecione todas as permissões listadas

{: start="5"}
5\. Selecione **Create API key (Criar chave de API**).
6\. Em seguida, copie a chave de API e cole-a em seu portal BrazeAI Decisioning Studio™ Acessar.

### Localizando o nome de exibição de seu e-mail Braze

Para encontrar o nome de exibição de seu e-mail Braze:

1. No painel do Braze, acesse **Settings** > **Email Preferences**( **Configurações** > **Preferências de e-mail**).
2. Localize o nome de exibição a ser usado com o BrazeAI Decisioning Studio™ Acessar.
3. Copie e cole o **nome de exibição De** no portal do BrazeAI Decisioning Studio™ Acessar como o **nome de exibição do e-mail**.
4. Copie e cole o endereço de e-mail associado em seu portal BrazeAI Decisioning Studio™ Acessar como o **endereço de e-mail De**, que combina a parte de localização e o domínio.

### Localizando sua ID de usuário

Para encontrar sua ID de usuário:

1. No dashboard do Braze, acesse **Público** > **Pesquisar usuários**.
2. Procure o usuário por sua ID de usuário externo, alias de usuário, e-mail, número de telefone ou token por push.
3. Copie o ID do usuário para fazer referência em sua configuração.

![Exemplo de perfil de usuário a partir da localização de um usuário com seu ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

### Como encontrar seu URL do Braze

Para identificar seu URL do Braze:

1. Acesse o dashboard do Braze.
2. Na janela de seu navegador, o URL do Braze começa com `https://` e termina com `braze.com`. Um exemplo de URL do Braze é `https://dashboard-01.braze.com`.

### Como encontrar sua chave de API do Braze

{% alert note %}
O Braze oferece IDs de aplicativos (chamados de chaves de API no dashboard do Braze) que você pode usar para fins de rastreamento, como para associar a atividade a um aplicativo específico em seu espaço de trabalho. Se você usar IDs de aplicativos, o BrazeAI Decisioning Studio™ Acessa a associação de uma ID de aplicativo a cada experimentador.<br><br>Se você não usar IDs de app, poderá inserir qualquer string de caracteres como espaço reservado.
{% endalert %}

1. No dashboard do Braze, acesse **Settings** > **App Settings (** **Configurações** > **Configurações do app**).
2. Acesse o app que deseja rastrear.
3. Copie e cole a **chave de API** em seu portal BrazeAI Decisioning Studio™ Acessar.

### Configuração das chaves de API do Klaviyo

Você deve configurar uma chave de API para usar o Klaviyo para o BrazeAI Decisioning Studio™ Acessar.

1. No Klaviyo, acesse **Configurações** > **Chaves de API**.
2. Selecione **Create Private API Key (Criar chave de API privada**). 
3. Digite um nome para a chave de API. Um exemplo é o "Decisioning Studio Experimenters".
4. Selecione as seguintes permissões para a chave de API:
    - Campanhas: Ler Acesso
    - Privacidade de dados: Acesso completo
    - Eventos: Acesso completo
    - Fluxos: Acesso completo
    - Imagens: Ler Acesso
    - Lista: Acesso completo
    - Métricas: Acesso completo
    - Perfis: Acesso completo
    - Segmentos: Ler Acesso
    - Modelos: Acesso completo
    - Webhooks: Ler Acesso

![Uma chave de API da Klaviyo com as permissões selecionadas.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Selecione **Criar**.
6\. Copie essa chave de API e cole-a no portal do BrazeAI Decisioning Studio™ Acessar onde for solicitado.

### Configuração de um pacote de aplicativos SFMC

Para usar o Salesforce Marketing Cloud para o BrazeAI Decisioning Studio™ Acessar, você deve configurar um pacote de app no Salesforce Marketing Cloud. 

1. Acesse a página inicial do Marketing Cloud. 
2. Abra o menu no cabeçalho global e selecione **Setup (Configuração**).
3. Acesse **Apps** em **Platform Tools** na navegação do painel lateral e selecione **Installed Packages (Pacotes instalados**).
4. Selecione **Novo** para criar um pacote de aplicativos.
5. Dê um nome e uma descrição ao pacote do app.

![Um pacote de app com o nome "Experimenter 1 - Test 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Selecione **Add Component (Adicionar componente**).
7\. Para o **tipo de componente**, selecione **Integração de API**. Em seguida, selecione **Next**.
8\. Para o **Tipo de integração**, selecione **Servidor para servidor**. Em seguida, selecione **Next**.
9\. Em seguida, selecione os seguintes escopos recomendados apenas para o pacote do seu app:
    \- Canais > E-mail > Ler, escrever, enviar
    \- Canais > OTT > Ler
    \- Canais > Push > Ler
    \- Canais > SMS > Ler
    \- Canais > Social > Ler
    \- Canais > Web > Ler
    \- Ativos > Documentos e imagens > Ler, escrever
    \- Ativos > Conteúdo salvo > Ler, escrever
    \- Automation > Automations > Read, Write, Execute
    \- Automation > Journeys > Ler, escrever, executar, ativar/interromper/pausar/enviar/agendar
    \- Contatos > Públicos > Ler
    \- Contatos > Lista e assinantes > Ler, escrever
    \- Plataforma Cross Cloud > Público do mercado > Visualizar
    \- Cross Cloud Platform > Membro do público do mercado > Visualizar
    \- Cross Cloud Platform > Marketing Cloud Connect > Ler
    \- Dados > Extensões de dados > Leitura, gravação
    \- Dados > Locais de arquivos > Ler
    \- Dados > Eventos de rastreamento > Leitura, gravação
    \- Notificações de eventos > Retornos de chamada > Ler
    \- Notificações de eventos > Inscrições > Ler

{% details Show image of recommended scopes %}

![Os escopos recomendados para o pacote do app Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Selecione **Salvar**.
11\. Copie e cole os seguintes campos no portal do BrazeAI Decisioning Studio™ Acessar: **ID do cliente**, **segredo do cliente**, **URI da base de autenticação**, **URI da base REST**, **URI da base SOAP**.