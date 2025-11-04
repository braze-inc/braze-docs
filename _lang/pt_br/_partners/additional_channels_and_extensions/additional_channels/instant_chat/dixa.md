---
nav_title: Dixa
article_title: Dixa
description: "Este artigo descreve a parceria entre a Braze e a Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> A [Dixa](https://www.dixa.com/) é uma plataforma de atendimento ao cliente projetada para aprimorar as experiências de suporte unificando canais de comunicação como chat, e-mail, telefone e redes sociais em uma única interface. Ele ajuda as empresas a melhorar a satisfação e a eficiência do cliente por meio de roteamento inteligente, automação e insights de performance em tempo real.

A integração Braze e Dixa oferece uma visão melhor de todos os seus usuários, fornecendo aos agentes de atendimento ao cliente dados do Braze em tempo real.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Um relato da Dixa        | É necessário ter uma conta de administrador da Dixa para aproveitar essa parceria.                                                                                           |
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com as permissões `users.export.ids` e `email.status`.<br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Um endpoint Braze REST | [Seu URL do ponto de extremidade REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá do URL do Braze para sua instância.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Coloque os dados do Braze na visualização do agente de atendimento ao cliente enquanto se comunica com seus usuários em diferentes canais de comunicação, como e-mail, Messenger ou chat.

## Integração

Você deve ser um administrador da Dixa para configurar as integrações dentro da Dixa. Para a integração com o Braze, no Dixa, acesse **Configurações** > **Integrações** > **Braze**.

![]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### Etapa 1: Criar a integração na Dixa

Na página **Criar widget do Braze**, preencha os seguintes campos obrigatórios para criar a integração:

- **Nome do widget:** Esse é o nome da integração que será usado posteriormente na barra lateral da conversa como o título.
- **URL de API:** Esse é o URL do endpoint da API do Braze REST para sua instância.
- **chave de API:** Essa é a chave de API do Braze que você criou nos pré-requisitos.

### Etapa 2: Configurar a integração

Em seguida, configure a integração do Braze e do Dixa. Escolha uma das seguintes opções para ajustar a visualização do widget do Braze na barra lateral da conversa.

#### Mostrar o widget na barra lateral da conversa

Essa configuração mostra ou oculta toda a integração na barra lateral da conversa no Dixa. 

Se estiver configurando ativamente a integração, recomendamos desativar essa opção enquanto preenche os campos obrigatórios. Quando terminar a configuração, você poderá ativá-la novamente e os agentes da Dixa poderão usar a integração.

#### Exibir detalhes do cliente

Escolha mostrar ou ocultar os detalhes do usuário. Os detalhes contêm dados sobre local, e-mail, número de telefone, estado da inscrição de e-mail, estado da inscrição de notificação por push e a duração da associação no Braze. 

#### Exibir o botão para alterar o estado da inscrição de e-mail

Os botões são baseados em um dos três estados de inscrição do Braze: `subscribed`, `opted-in` e `unsubscribed`. Se um usuário for `subscribed`, o agente poderá optar por `opt-in` ou `unsubscribe`. Quando um usuário é `opted-in` ou `unsubscribed`, só é possível alternar entre os dois.

#### Exibir uma lista de atributos personalizados

Escolha mostrar ou ocultar os atributos personalizados do usuário no Braze.

#### Exibir uma lista de eventos personalizados

Escolha mostrar ou ocultar os eventos personalizados do usuário no Braze.

#### Exibir uma lista de compras

Escolha mostrar ou ocultar uma lista de produtos comprados pelo usuário. Aqui, você pode ver quantas vezes ele foi comprado. Para visualizar a primeira e a última data de compra, passe o mouse sobre o item. 

### Exemplo de integração

O exemplo a seguir mostra um exemplo de integração:

![A integração do Braze e do Dixa no Dixa que exibe o estado de envio de e-mail de um usuário, atributos personalizados, eventos personalizados e compras.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

