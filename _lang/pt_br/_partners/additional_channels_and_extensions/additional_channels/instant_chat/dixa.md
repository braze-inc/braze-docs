---
nav_title: Dixa
article_title: Dixa
description: "Este artigo descreve a parceria entre a Braze e a Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> A [Dixa](https://www.dixa.com/) é uma plataforma de atendimento ao cliente projetada para aprimorar as experiências de suporte unificando canais de comunicação como chat, e-mail, telefone e redes sociais em uma única interface. Ela ajuda as empresas a melhorar a satisfação e a eficiência do cliente por meio de roteamento inteligente, automação e insights de performance em tempo real.

A integração da Braze com a Dixa oferece uma visão melhor de todos os seus usuários, fornecendo aos agentes de atendimento ao cliente dados da Braze em tempo real.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta da Dixa        | É necessário ter uma conta de administrador da Dixa para aproveitar essa parceria.                                                                                           |
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com as permissões `users.export.ids` e `email.status`.<br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Um endpoint REST da Braze | [URL do seu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Exiba os dados da Braze na visualização do agente de atendimento ao cliente enquanto se comunica com seus usuários em diferentes canais de comunicação, como e-mail, Messenger ou chat. Além disso, use a Transformação de Dados da Braze para enviar dados da Dixa para a Braze e pausar o marketing enquanto resolve o problema de um usuário.

## Integração

Você deve ser um administrador da Dixa para configurar as integrações dentro da Dixa. Para a integração com a Braze, na Dixa, acesse **Configurações** > **Integrações** > **Braze**.

![A página Criar widget da Braze na Dixa, onde você insere o nome do widget, a URL da API e a chave de API.]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### Etapa 1: Criar a integração na Dixa

Na página **Criar widget da Braze**, preencha os seguintes campos obrigatórios para criar a integração:

- **Nome do widget:** Esse é o nome da integração que será usado posteriormente na barra lateral da conversa como título.
- **URL da API:** Essa é a URL do endpoint da API REST da Braze para sua instância.
- **Chave de API:** Essa é a chave de API da Braze que você criou nos pré-requisitos.

### Etapa 2: Configurar a integração

Em seguida, configure a integração da Braze com a Dixa. Escolha uma das seguintes opções para ajustar a visualização do widget da Braze na barra lateral da conversa.

#### Mostrar o widget na barra lateral da conversa

Essa configuração mostra ou oculta toda a integração na barra lateral da conversa na Dixa. 

Se estiver configurando ativamente a integração, recomendamos desativar essa opção enquanto preenche os campos obrigatórios. Quando terminar a configuração, você poderá ativá-la novamente e os agentes da Dixa poderão usar a integração.

#### Exibir detalhes do cliente

Escolha mostrar ou ocultar os detalhes do usuário. Os detalhes contêm dados sobre local, e-mail, número de telefone, estado da inscrição de e-mail, estado da inscrição de notificação por push e a duração da associação na Braze. 

#### Exibir o botão para alterar o estado da inscrição de e-mail

Os botões são baseados em um dos três estados de inscrição da Braze: `subscribed`, `opted-in` e `unsubscribed`. Se um usuário for `subscribed`, o agente poderá optar por `opt-in` ou `unsubscribe`. Quando um usuário é `opted-in` ou `unsubscribed`, só é possível alternar entre os dois.

#### Exibir uma lista de atributos personalizados

Escolha mostrar ou ocultar os atributos personalizados do usuário na Braze.

#### Exibir uma lista de eventos personalizados

Escolha mostrar ou ocultar os eventos personalizados do usuário na Braze.

#### Exibir uma lista de compras

Escolha mostrar ou ocultar uma lista de produtos que o usuário comprou. Aqui, você pode ver quantas vezes o usuário comprou o produto. Para ver a data da primeira e da última compra, passe o mouse sobre o item. 

### Exemplo de integração

Veja a seguir um exemplo da integração:

![A integração da Braze com a Dixa na Dixa que exibe o estado de inscrição de e-mail do usuário, atributos personalizados, eventos personalizados e compras.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

## Ferramenta de transformação de dados

A Dixa usa webhooks para enviar dados para a Braze. Você deve ser um administrador da Dixa para configurar webhooks.

O primeiro passo é criar uma transformação de dados na Braze. 

1. Acesse **Configurações de dados** > **Transformações de dados** > **Criar transformação**.
2. Selecione **Começar do zero**, selecione o destino **POST: Track Users** e selecione **Criar transformação**.
3. No editor de transformação, copie o código de exemplo de **Exemplo de ferramenta de transformação** abaixo e insira-o no campo **Código de transformação**. Selecione **Salvar**, copie a **URL do webhook** e abra a Dixa.
4. Na Dixa, acesse **Configurações** > **Integrações** > **Webhooks** > **+ Webhook de saída**.
5. Na página de configurações do webhook, cole a URL da Braze e ative os eventos que deseja rastrear. **Conversa criada** é um bom ponto de partida para rastrear as conversas dos clientes. 
6. Selecione **Salvar** para concluir a configuração da Dixa.

### Exemplo de ferramenta de transformação

```js
// Transforming the provided payload to match Braze /users/track endpoint specifications.

// Extracting necessary details from the payload
const requester = payload.data.conversation.requester;
const event = payload.data.conversation;

// Defining user attributes based on the provided payload, prioritizing email if available.
const userAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  _update_existing_only: false, // Set to false to create or update user profiles when identified by email
  organization: payload.organization.name, // Including an additional attribute for demonstration
};

// Defining event attributes based on the provided payload.
const eventAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  name: payload.event_fqn, // The name of the event
  time: event.created_at, // ISO 8601 datetime format
  properties: { // Including additional event properties
    event_version: payload.event_version,
    conversation_status: event.status,
    conversation_channel: event.channel
  },
  _update_existing_only: false // Set to false to create or update user profiles when identified by email
};

// Constructing the final object to match Braze /users/track endpoint schema
const brazecall = {
  attributes: [userAttributes], // Wrapping userAttributes in an array as per specifications
  events: [eventAttributes] // Wrapping eventAttributes in an array as per specifications
};

// Returning the transformed data
return brazecall;
```
