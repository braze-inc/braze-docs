---
nav_title: Zeotap Symphony
description: "Este artigo de referência descreve a parceria entre a Braze e a Zeotap, uma plataforma de dados do cliente de última geração que fornece resolução, insights e enriquecimento de identidade."
page_type: partner
search_tag: Partner
page_order: 2 
---

# Zeotap Symphony

A integração Braze e Zeotap Symphony permite que você crie orquestrações em tempo real e execute campanhas de e-mail e notificações por push.

- Envie nomes e sobrenomes pelo Zeotap, com base nos quais os usuários podem enviar e-mails personalizados pelo Braze.
- Envie eventos personalizados ou um evento de compra em tempo real por meio do Zeotap, com base nos quais os usuários podem criar disparadores de campanha no Braze para direcionar seus clientes

{% alert note %}
Para criar campanhas de marketing por e-mail, integre os e-mails brutos à Zeotap mapeando-os para `Email Raw` no Zeotap Catalogue.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Nome do cliente | Esse é o nome do cliente de sua conta Braze. Você pode encontrá-lo navegando até o console da Braze. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instância | Sua instância do Braze pode ser obtida com seu gerente de integração do Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integração

Esta seção contém informações sobre os dois métodos que podem ser integrados à Braze:

### Método 1
Neste método, você deve executar as seguintes tarefas:
1. Integrar o SDK da Braze ao seu site ou app.
2. Integrar a Braze com a Zeotap pela Symphony.

- `User traits` devem ser mapeados para os respectivos campos do Braze na guia **Data To Send (Dados a serem enviados** ). Se você mapear as atribuições `Event` e `Purchase`, isso levará à duplicação de eventos na Braze.
- Mapeie `External ID` para `User ID` configurado durante a configuração do SDK do Braze.

Quando a integração for configurada com sucesso, você poderá criar campanhas de e-mail e notificações por push com base em atributos personalizados enviados ao Braze por meio do Symphony.

### Método 2
Neste método, você pode integrar a Braze à Zeotap pela Symphony.

- Este método não suporta os recursos da interface do usuário do Braze, como envio de mensagens no aplicativo, Cartões de Conteúdo ou notificações por push.
- A Zeotap recomenda mapear o site `hashed email` disponível no Zeotap Catalogue para o site `External ID`.

Quando a integração for definida com sucesso, você só poderá criar campanhas de e-mail com base em atributos personalizados enviados ao Braze por meio do Symphony.

## Fluxo de dados para o Braze e identificadores suportados

Os dados fluirão do Zeotap para o Braze usando o [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Os seguintes pontos resumem o fluxo de dados:

1. O Zeotap envia atributos de perfil de usuário, atributos personalizados, eventos personalizados e campos de compra.
2. Você mapeia todos os campos relevantes do Catálogo Zeotap para os campos do Braze na guia **Data To Send (Dados a serem enviados** ).
3. Em seguida, é feito o upload dos dados para a Braze.

É possível encontrar detalhes sobre as diferentes atribuições na seção [Dados a serem enviados](#data-to-send-tab).

## Configuração do destino

Após aplicar filtros ou adicionar uma condição para seus usuários no Symphony, é possível ativá-los no Braze em **Send to Destinations (Enviar para destinos**). Uma nova janela é aberta, onde você pode configurar seu destino. Você pode usar um destino existente na lista de **Destinos disponíveis** ou criar um novo.

#### Adicionar novo destino
Execute as etapas a seguir para adicionar um novo destino:
1. Selecione **Adicionar Novo Destino**.
2. Procure por **Braze**.
3. Adicione o **nome do cliente**, **a chave de API** e a **instância** e salve o destino.

O destino é criado e disponibilizado em **Available Destinations (Destinos disponíveis**).

#### Adicionar entradas em nível de fluxo de trabalho
Depois de criar um destino, você deve adicionar entradas no nível do fluxo de trabalho, conforme mencionado abaixo.
1. Escolha o destino na lista de destinos disponíveis usando o recurso de pesquisa.
2. Os campos **Client Name (Nome do cliente**), **API Key (Chave de API**) e **Instance (Instância)** são preenchidos automaticamente com base no valor que você inseriu ao criar o destino.
3. Digite o **nome do público** que você deseja criar para esse nó de fluxo de trabalho. Isso é enviado como um **atributo personalizado** para o Braze.
4. Complete o mapeamento de Catálogo para destinos na guia **Dados a serem enviados**. Você pode encontrar detalhes sobre como realizar o mapeamento abaixo.

#### Guia Dados a serem enviados
A guia **Data To Send (Dados a serem enviados** ) permite mapear os campos do catálogo Zeotap para os campos do Braze que podem ser enviados ao Braze. O mapeamento pode ser feito de uma das seguintes maneiras:
- **Mapeamento estático** \- Há determinados campos que o Zeotap mapeia automaticamente para os campos Braze relevantes, como e-mail, telefone, nome, sobrenome e assim por diante.<br>
- **Seleção suspensa** – mapeie os campos relevantes ingeridos na Zeotap para os campos da Braze fornecidos no menu suspenso.<br>![Várias características do usuário definidas no Zeotap, como idioma, cidade, aniversário e mais.]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **Entrada de dados personalizados** \- Adicione dados personalizados mapeados ao campo Zeotap relevante e envie para o Braze.<br>![Selecionando "loyalty_points" como a característica do usuário no Zeotap.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## Atribuições suportadas
Você pode encontrar detalhes de todos os campos da Braze nesta seção.

| Campo da Braze | Tipo de mapeamento | Descrição |
| --- | --- | --- |
| ID externo | Seleção suspensa | Este é o `User ID` persistente definido pela Braze para rastrear usuários em dispositivos e plataformas. Recomendamos que você mapeie `User ID` para `External ID`; caso contrário, o Zeotap poderá enviar e-mail como um alias de usuário.<br><br>A Zeotap recomenda mapear o `hashed email` disponível no Zeotap Catalogue para o `External ID`.|
| E-mail | Mapeamento estático | É mapeado para `Email Raw` no Zeotap Catalogue. |
| Telefone | Mapeamento estático | É mapeado para `Mobile Raw` no Zeotap Catalogue.<br><br>\- O Braze aceita números de telefone no formato `E.164`. O Zeotap não realiza nenhuma transformação. Portanto, é necessário que você fazer a ingestão dos números de telefone no formato prescrito. Para saber mais, consulte [Números de telefone do usuário]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| Nome | Mapeamento estático | É mapeado para `First Name` no Zeotap Catalogue. |
| Sobrenome | Mapeamento estático | É mapeado para `Last Name` no Zeotap Catalogue. |
| Gênero | Mapeamento estático | É mapeado para `Gender` no Zeotap Catalogue. |
| Nome do evento personalizado | Mapeamento estático | É mapeado para `Event Name` no Zeotap Catalogue.<br><br>Tanto o nome do evento personalizado quanto o registro de data e hora do evento personalizado devem ser mapeados para capturar eventos personalizados no Braze. O evento personalizado não poderá ser processado se nenhum deles estiver mapeado. Para saber mais, consulte o [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Registro de data e hora do evento personalizado | Mapeamento estático | Isso é mapeado para o `Event Timestamp` no Zeotap Catalogue.<br><br>Tanto o nome do evento personalizado quanto o registro de data e hora do evento personalizado devem ser mapeados para capturar eventos personalizados no Braze. O evento personalizado não poderá ser processado se nenhum deles estiver mapeado. Para saber mais, consulte o [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Inscrição de e-mail | Seleção suspensa | Faça a integração de um campo `Email Marketing Preference` e mapeie para ele.<br><br>Zeotap envia os três valores a seguir:<br>- `opted_in` - indica que o usuário se registrou explicitamente para a preferência de marketing por e-mail.<br>- `unsubscribed` - indica que o usuário aceitou explicitamente receber mensagens de e-mail.<br>- `subscribed` - indica que o usuário nem aceitou nem recusou. |
| Inscrição de push | Seleção suspensa | Faça a integração de um campo `Push Marketing Preference` e mapeie para ele.<br><br>Zeotap envia os três valores a seguir:<br>- `opted_in` - indica que o usuário se registrou explicitamente para a preferência de marketing por push.<br>- `unsubscribed` - indica que o usuário aceitou explicitamente receber mensagens de push.<br>- `subscribed` - indica que o usuário nem aceitou nem recusou. |
| Ativar o rastreamento de aberturas de e-mail | Seleção suspensa | Mapeie o campo relevante `Marketing Preference`.<br><br>Quando definido como true, ele ativa um pixel de rastreamento de abertura a ser adicionado a todos os futuros e-mails enviados a esse usuário. |
| Ativar o envio de e-mail para rastreamento de cliques | Seleção suspensa | Mapeie o campo relevante `Marketing Preference`.<br><br>Quando definido como true, ativa o rastreamento de cliques para todos os links em todos os futuros e-mails enviados a esse usuário. |
| ID do produto | Seleção suspensa | \- Identificador de uma ação de compra `(Product Name/Product Category)`. Para obter mais detalhes, consulte o [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/).<br>\- Faça integração do atributo relevante no Zeotap Catalogue e mapeie para ele.<br><br>`Product ID`, `Currency` e `Price` devem ser mapeados obrigatoriamente para capturar eventos de compra na Braze. O evento de compra não poderá ser realizado se algum dos três for esquecido. Para saber mais, consulte o [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-object). |
| Moeda | Seleção suspensa | \- Atributo de moeda para a ação de compra.<br>\- O formato suportado é `ISO 4217 Alphabetic Currency Code`.<br>\- Faça integração de dados de moeda corretamente formatados no Zeotap Catalogue e mapeie para ele.<br><br>`Product ID`, `Currency` e `Price` devem ser mapeados obrigatoriamente para capturar eventos de compra na Braze. O evento de compra não poderá ser realizado se algum dos três for esquecido. |
| Preço | Seleção suspensa | \- Atribuição de preço para a ação de compra.<br>\- Faça integração do atributo relevante no Zeotap Catalogue e mapeie para ele.<br><br>`Product ID`, `Currency` e `Price` devem ser mapeados obrigatoriamente para capturar eventos de compra na Braze. O evento de compra não poderá ser realizado se algum dos três for esquecido. |
| Quantidade | Seleção suspensa | \- Atribuição de quantidade para a ação de compra.<br>\- Faça integração do atributo relevante no Zeotap Catalogue e mapeie para ele. |
| País | Seleção suspensa | Mapeie para o campo `Country` do Catalogue que você está integrando. |
| Cidade | Seleção suspensa | Mapeie para o campo `City` do Catalogue que você está integrando. |
| Idioma | Seleção suspensa | \- O formato aceito é o padrão `ISO-639-1` (por exemplo, en).<br>\- Faça integração do idioma formatado corretamente e mapeie para ele. |
| Data de nascimento | Seleção suspensa | Mapeie para o campo `Date of Birth` que você está integrando. |
| Atributo personalizado | Entrada de dados personalizados | Mapeie qualquer atributo de usuários para uma entrada de dados personalizada, que é então enviada à Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Visualização de dados no console do Braze

Depois que você mapear as atribuições relevantes a serem enviadas e publicadas no fluxo de trabalho, os eventos começarão a fluir para o Braze com base nos critérios definidos. É possível pesquisar por ID de e-mail ou ID externa no console do Braze.

![]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Vários atributos estão em diferentes seções do dashboard de usuário na Braze.
- A guia **Profile (Perfil** ) contém as atribuições do usuário.
- A guia **Atributos personalizados** contém os atributos personalizados definidos pelo usuário.
- A guia **Custom Events (Eventos personalizados** ) contém o evento personalizado definido pelo usuário.
- A guia **Purchases (Compras** ) contém as compras feitas pelo usuário durante um período de tempo.

## Criação de campanhas

Os usuários podem criar campanhas no Braze e ativar usuários em tempo real ou com base no horário programado. As campanhas podem ser disparadas com base nas ações realizadas pelo usuário (evento personalizado, compra) ou nos atributos do usuário.

