---
nav_title: Sendbird
article_title: Sendbird
description: "Este artigo de referência descreve a parceria entre o Braze e o Sendbird, uma solução líder de envio de mensagens no app que permite que os usuários recebam notificações no app na plataforma Sendbird."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> O [Sendbird](https://sendbird.com/) Notifications oferece aos profissionais de marketing e gerentes de produtos um novo e poderoso canal de envio de mensagens persistentes e interativas no app para se comunicar com seus clientes. Essas mensagens podem ser usadas para qualquer comunicação e são mais comumente usadas para fins promocionais e transacionais.

_Esta integração é mantida pela Sendbird._

## Sobre a integração

A integração do Braze e do Sendbird permite que os usuários do Braze:
* Utilize as capacidades de segmentação e disparo do Braze para iniciar notificações personalizadas dentro do app.
* Crie notificações personalizadas no aplicativo na plataforma Sendbird Notifications, que são então entregues no ambiente do app, aumentando o engajamento do usuário.

Ao aproveitar os recursos conjuntos da Braze e do Sendbird Notifications, as empresas podem elevar o engajamento do cliente e aumentar as taxas de conversão por meio de estratégias eficazes de notificação no aplicativo.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Sendbird | É necessário ter uma conta Sendbird para aproveitar essa parceria. |
| Sendbird UIKit | Você deve ter o Sendbird UIKit instalado em seu app para [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) ou [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit). |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

![]({% image_buster /assets/img/sendbird/use-cases.png %})

A integração das Notificações Braze e Sendbird oferece uma variedade de casos de uso para aumentar o engajamento do cliente e proporcionar uma experiência excepcional ao usuário:

- **Marketing**: Aprimore campanhas direcionadas com promoções personalizadas e recomendações adaptadas às preferências dos usuários, como descontos exclusivos baseados no histórico de navegação ou em compras anteriores.
- **Transacional**: Eleve a comunicação com o cliente por meio de atualizações em tempo real sobre pedidos, entregas, faturamento e pagamentos, incluindo notificações sobre o status do pedido, detalhes de remessa e prazos de entrega estimados.

## Integração

### Etapa 1: Criar um modelo de notificação

[Os modelos do Sendbird](https://sendbird.com/docs/notifications/v1/templates) permitem que você envie notificações personalizadas no app, criando e usando vários modelos para cada canal. Os modelos podem ser criados e personalizados no Sendbird Dashboard sem a necessidade de escrever código.

![]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Etapa 2: Configure a integração do Braze no dashboard do Sendbird

No **Sendbird Dashboard**, selecione seu aplicativo, navegue até **Notifications > Integrations (Notificações > Integrações**) e clique em **Add (Adicionar** ) na seção **Braze**. Aqui você precisará da sua chave da API REST da Braze e do endpoint REST da Braze.

Depois de fornecer todos os campos, clique em **Save (Salvar)** para concluir a integração e acessar os endpoints de integração e o token da API.

### Etapa 3: instale o Sendbird Notification Builder

Em seguida, você deve instalar o [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji). Essa extensão do Google Chrome permite enviar notificações personalizadas pelo Sendbird no dashboard da Braze.

![]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Adicione as credenciais do Sendbird à extensão

Depois que a extensão for instalada, clique no ícone do Sendbird na barra de ferramentas do navegador e selecione **Configurações**. Agora forneça o ID do app e o token da API encontrados no **Sendbird Notification Builder**.

### Etapa 4: Mapear o ID de usuário do Sendbird para o ID de usuário do Braze

Um ID de usuário Sendbird deve ser adicionado a um perfil de usuário Braze como um [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) para que a integração seja usada. É possível fazer upload e atualizar perfis de usuários por meio de arquivos CSV na página [Importação de usuários]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv). Como alternativa, você pode usar o ID de usuário da Braze como o ID de usuário do Sendbird.

### Etapa 5: Configure seu modelo de webhook

Na Braze, em **Modelos e mídia**, acesse **Modelos de webhook** e escolha **Modelo de webhook do Sendbird**. Observe que esse modelo só ficará disponível se você tiver instalado a extensão Sendbird Notification Builder.

{% raw %}
1. Forneça um nome de modelo e adicione equipes e tags conforme necessário.
2. Copie um endpoint em tempo real ou em lote do dashboard do Sendbird para a **URL do Webhook**.
3. No campo **Receiver** (Receptor), clique no ícone <i class="fas fa-plus"></i> e insira o atributo de usuário mapeado para o ID de usuário do Sendbird.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` se estiver usando um atributo personalizado `sendbird_id` como o ID de usuário do Sendbird.
    - `{{ '{{' }}${user_id}}}` se estiver usando o ID de usuário da Braze como ID de usuário do Sendbird.
4. Na guia **Settings (Configurações** ), substitua `SENDBIRD_API_TOKEN` pelo token da API de notificações do dashboard do Sendbird.
5. Salvar o modelo.
{% endraw %}

## Usando essa integração

### Campanhas

1. No dashboard do Braze, na página **Campanhas**, clique em **Criar campanha** > **Webhook**.
2. Selecione o modelo de webhook que você criou acima. É altamente recomendável que você use o endpoint Batch para campanhas.
3. Personalize o modelo editando suas variáveis na guia **Compose (Criar** ).

### Canva

1. Em um Canva novo ou existente, adicione um componente **Message**. 
2. Abra o componente e selecione **Webhook** nos **canais de envio de mensagens**.
3. Selecione o modelo de webhook que você criou acima. É altamente recomendável que você use o ponto de extremidade em tempo real para Canvas.
4. Personalize o modelo editando suas variáveis na guia **Compose (Criar** ).

## Personalização

### Rastreamento do status de entrega e de abertura

Para integrar a entrega das notificações e o evento de status de abertura com a métrica de conversão de uma campanha, adicione um evento personalizado no dashboard do Braze.

1. No dashboard do Braze, acesse **Configurações > Gerenciar configurações > Eventos personalizados** e clique em **\+ Adicionar evento personalizado**.
2. Depois de criar um evento personalizado, clique em **Manage Properties (Gerenciar propriedades**), adicione uma propriedade chamada "status" e escolha "String" como o tipo de propriedade.
3. Ao criar uma notificação em campanhas ou canvas, insira o nome do evento personalizado no campo **Nome do evento**.

Esse evento personalizado será disparado duas vezes para cada notificação, quando uma mensagem for enviada e quando um usuário abrir a mensagem.
- Quando uma mensagem é enviada, um evento personalizado é disparado com o status `SENT`.
- Quando uma mensagem é lida, um evento personalizado é disparado com o status `READ`.


