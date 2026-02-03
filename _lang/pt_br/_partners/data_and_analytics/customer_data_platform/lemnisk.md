---
nav_title: Lemnisk
article_title: Integre Lemnisk com Braze
description: "Este artigo de referência detalha a parceria entre Braze e Lemnisk, uma plataforma de automação de marketing liderada por uma plataforma de dados do cliente habilitada por IA, permitindo que você transmita dados de usuários coletados na Lemnisk de várias fontes para o Braze, para ativá-los em vários canais e destinos usando as ferramentas do Braze."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/) é uma Plataforma de Dados do Cliente (CDP) alimentada por IA e uma solução de automação de marketing que permite a captura, unificação e ativação em tempo real de dados de clientes de fontes diversas e isoladas. Ela entrega perfeitamente esses dados unificados em várias plataformas de MarTech e negócios, enquanto oferece análises robustas em tempo real para rastrear cada estágio do ciclo de vida dos dados do cliente. 

_Esta integração é mantida pela Lemnisk._

## Sobre a integração

A integração entre Lemnisk e Braze permite que marcas e empresas desbloqueiem todo o potencial do Braze, atuando como uma camada de inteligência liderada por CDP que unifica dados de usuários em tempo real entre plataformas, enviando as informações e comportamentos dos usuários coletados para o Braze em tempo real. A Lemnisk entrega perfis de clientes enriquecidos diretamente no Braze, misturando sinais comportamentais e atributos pessoais que permitem personalizar suas mensagens com um contexto mais profundo.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Contas Lemnisk | Uma conta [Lemnisk](https://www.lemnisk.co/) é necessária para aproveitar esta parceria. |
| API Externa na Lemnisk | Entre em contato com seu CSM da Lemnisk para habilitar **API Externa** para sua conta. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com permissão `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua conta]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints#api-and-sdk-endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integrando Lemnisk

### Etapa 1: Crie uma API Externa do Braze {#create-a-braze-external-api}

Na Lemnisk, acesse o canal de API Externa. Selecione **Adicionar Nova API Externa**. Agora vamos configurar o endpoint [Rastrear Usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track) como uma API Externa.

![Iniciando o processo de criação da API Externa na Lemnisk]({% image_buster /assets/img/lemnisk/open_external_api.png %})

Sob **Detalhes Básicos**, insira um nome, descrição, canal e identificador do canal.

![Inserindo detalhes básicos de configuração para uma nova API Externa no Lemnisk]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

Sob **Detalhes da API Externa**, insira os detalhes relevantes para seu `users.track` endpoint. Você pode definir múltiplos campos de nível de engajamento usando {% raw %}`{{}}`{% endraw %}, o que permite definir valores diferentes para diferentes campanhas.

![Preenchendo os detalhes do endpoint e carga útil da API Externa]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Para finalizar a configuração do seu rastreamento de usuários, selecione **Salvar**. Você será redirecionado automaticamente para a página **Testar API**.

### Etapa 2: Teste a configuração

Na página **Testar API**, insira alguns valores de teste para os parâmetros da API na sua visualização de árvore JSON, e então selecione **Testar Configuração**.

Se suas credenciais e definições de API estiverem corretas, a Braze retornará uma resposta de sucesso.

![Testando uma configuração de API Externa com uma carga útil de exemplo e resposta de sucesso]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

Em seguida, você verificará se seus eventos estão sendo enviados para a Braze com sucesso. No painel da Braze, acesse **público** > **Buscar Usuários**, e então insira um dos identificadores da sua configuração de API Externa (como um endereço de e-mail de usuário). Se tudo estiver funcionando corretamente, o perfil que recebeu seu disparo de API de teste será listado.

![Visualizando o perfil de um usuário e a visão geral da atividade na Braze]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### Etapa 3: Disparar eventos de usuário na Braze

1. No Lemnisk, crie um novo segmento. Por exemplo, você poderia criar um segmento que envia informações para a Braze assim que os usuários enviarem um formulário de lead.
2. No seu novo segmento, acesse **API Externa** > **Adicionar Engajamento**.
3. Sob **Criação de Engajamento**, insira os detalhes básicos e selecione a configuração [que você criou anteriormente](#create-a-braze-external-api).
4. Sob **Configurar Parâmetros**, você encontrará as entradas para os parâmetros da Braze que você escolheu expor no nível de engajamento. No exemplo a seguir, mostra _Name of the User_, _Product ID_ e _Event Time_.
    ![Criando um engajamento para enviar dados de usuários para Braze]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. Insira as variáveis de personalização relevantes para nossos parâmetros escolhidos, e então selecione **Salvar**.
6. Quando terminar, ative o Engajamento.
