---
nav_title: SmarterSends
article_title: SmarterSends
description: "Este artigo de referência descreve a parceria entre a Braze e a SmarterSends, uma interface fácil de usar projetada para que até profissionais que não sejam da área de marketing possam programar e implementar campanhas de e-mails alinhadas com a marca."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [O SmarterSends](https://smartersends.com) impulsiona a personalização com campanhas de marketing que as empresas podem criar, programar e implementar para reforçar a conformidade legal e da marca com controle sobre o conteúdo e os dados usados. 

Esta integração é mantida pela SmarterSends.

## Sobre a integração

A parceria entre a Braze e a SmarterSends permite combinar o poder da Braze com o conteúdo hiperlocalizado de propriedade de seus usuários distribuídos para elevar suas campanhas de marketing.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta SmarterSends | É necessário ter uma [conta SmarterSends](https://smartersends.com) para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com essas permissões: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. Para aumentar a segurança, coloque na lista de permissões o endereço IP da SmarterSends (disponível em sua instância). |
| Ponto de extremidade REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
| ID da campanha da API do Braze | O [ID da campanha da API do Braze]({{site.baseurl}}/api/api_campaigns/) é o identificador exclusivo de todas as campanhas enviadas por meio do SmarterSends. Isso pode ser criado no dashboard da Braze em **Envio de mensagens** > **Campanhas**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Com a integração do Braze e do SmarterSends, você pode tirar proveito do marketing distribuído criando e executando campanhas de marketing em vários canais e locais. Essas vantagens incluem:

1. **Maior alcance:** usar vários canais e locais para atingir um público mais amplo e direcionar clientes em diferentes locais, resultando em maior exposição da marca.
2. **Envio de mensagens direcionadas:** Adaptar o envio de mensagens em todos os canais e locais para que repercutam no público local, a fim de obter uma comunicação e um engajamento mais eficazes com os clientes. 
3. **Melhoria da consistência da marca:** Alinhamento do envio de mensagens e da imagem de sua marca em todos os canais e locais, o que é importante para a criação de uma marca forte e reconhecível.
4. **Melhores insights:** Coleta de dados de vários canais e locais, fornecendo insights valiosos sobre o comportamento e as preferências dos clientes, que podem ser usados para refinar as estratégias e táticas de marketing, tanto em nível local quanto global.
5. **Aumento da eficiência:** Aproveitar os pontos fortes de diferentes canais e locais, o que pode resultar em um uso mais eficiente dos recursos e, ao mesmo tempo, atingir as metas de marketing desejadas. 

## Integração

### Etapa 1: Criar uma chave de API REST

1. No Braze, acesse **Settings** > **API Keys** (Configurações > Chaves de API) e clique em **Create New API Key** (Criar nova chave de API).
2. Digite um nome para a chave de API.
3. Selecione as seguintes permissões para essa chave para permitir que o SmarterSends interaja com seu espaço de trabalho no Braze.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. Adicione o endereço IP do SmarterSends à seção **Whislist IPs**.
5. Clique em **Save API Key (Salvar chave de API**).
6. Copie e cole a chave de API com as permissões apropriadas nas configurações do **Braze Email Service Provider** no SmarterSends.

### Etapa 2: Criar ou copiar um ID de aplicativo

1. Em seu espaço de trabalho do Braze, acesse **Configurações** > **Configurações do app**. 
2. Configure um novo app ou use o ID do aplicativo de um aplicativo existente em seu espaço de trabalho. Note que o ID do aplicativo é rotulado como a **chave de API**. 
3. Copie e cole esse ID no campo **ID do app** no SmarterSends.

### Etapa 3: Criar uma campanha de API

Uma campanha API permite o rastreamento de métricas para todos os e-mails do SmarterSends no Braze e capacita o SmarterSends a disparar essas campanhas baseadas em API.

1. No Braze, [crie uma campanha de API]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Clique em **E-mail** em **Selecionar canal de mensagens** para adicionar um canal de envio de mensagens e começar a rastrear as métricas.
3. Em seguida, copie e cole o ID da campanha do Braze no campo **Campaign ID** do SmarterSends. 
4. Copie e cole o ID da variação da mensagem do Braze no campo **Message Variant ID** do SmarterSends. Esse será o ID de mensagem padrão usado se você decidir não criar um ID de mensagem para cada grupo no SmarterSends.
5. Para cada grupo que você criar no SmarterSends, adicione uma variante de mensagens à sua campanha de API no Braze. Em seguida, copie o ID da variante da mensagem para o ID da variante da mensagem do grupo no SmarterSends.

{% alert tip %}
Crie um ID de variante de mensagem para cada grupo que você criar no SmarterSends para visualizar as métricas dos envios de cada grupo separadamente em seu espaço de trabalho do Braze. Isso pode ser útil para identificar tendências entre grupos ao criar relatórios no Braze.
{% endalert %}

## Personalização

Cada instância do SmarterSends é totalmente personalizável com as cores do logotipo de sua marca e o nome de domínio personalizado, criando um ambiente familiar. Além disso, para maior personalização, é possível definir os atributos e os atributos personalizados para direcionamento de usuários em campanhas com base nos segmentos dentro do seu espaço de trabalho Braze.


