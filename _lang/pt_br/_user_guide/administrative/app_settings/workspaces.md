---
nav_title: Criação e gerenciamento de espaços de trabalho
article_title: Criação e gerenciamento de espaços de trabalho
page_order: 0
page_type: reference
description: "Este artigo aborda como criar, configurar e gerenciar seus espaços de trabalho."

---

# Criação e gerenciamento de espaços de trabalho

> Este artigo aborda como criar, configurar e gerenciar seus espaços de trabalho. 

## O que é um espaço de trabalho?

Tudo o que você faz no Braze acontece em um espaço de trabalho. Os espaços de trabalho são um ambiente compartilhado para você rastrear e gerenciar engajamento para apps e sites relacionados. Os espaços de trabalho agrupam os mesmos aplicativos ou aplicativos muito semelhantes: por exemplo, as versões para Android e iOS do seu aplicativo móvel. 

## Criação de um espaço de trabalho

### Etapa 1: Tenha um plano

Antes de começar, certifique-se de ter trabalhado com sua equipe e com o gerente de integração do Braze para determinar a melhor configuração de espaço de trabalho para o seu caso de uso. Para saber mais sobre o planejamento de seus espaços de trabalho na Braze, confira o artigo [Como começar: espaços de trabalho][link].

### Etapa 2: Adicione seu espaço de trabalho

Você pode criar novos espaços de trabalho ou alternar entre espaços de trabalho existentes no menu suspenso de espaços de trabalho no cabeçalho global.

1. Selecione o menu suspenso do espaço de trabalho e clique em <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Criar espaço de trabalho**.

![][1]

{:start="2"}
2\. Dê um nome ao seu espaço de trabalho.

{% alert tip %}
Talvez você queira adotar uma convenção de nomes para que outras pessoas da empresa possam encontrar facilmente seu espaço de trabalho. Por exemplo: "Upon Voyage US - Produção" e "Upon Voyage US - Encenação".
{% endalert %}

{:start="3"}
3\. Selecione **Criar**. Pode levar alguns segundos para que a Braze crie seu espaço de trabalho.

![][2]

Você será levado à página **Configurações do aplicativo** para começar a adicionar suas instâncias do app. Você pode acessar essa página a qualquer momento em **Configurações** > **Configurações do app**.

![][3]

### Etapa 3: Adicione suas instâncias do app

Referimo-nos aos diferentes sites e aplicativos que são coletados em um espaço de trabalho como "instâncias do app".

1. Na página **Configurações do aplicativo**, clique em **\+ Adicionar aplicativo**.
2. Dê um nome à instância do app e selecione em qual plataforma ou plataformas essa instância do app está. Se você selecionar várias plataformas, a Braze criará uma instância do app para cada plataforma.

![][4]{: style="max-width:60%" }

{:start="3"}
3\. Clique em **Add app (Adicionar aplicativo** ) para confirmar.

#### Chaves de API do app

Depois de adicionar a instância do app, você terá acesso à chave de API dele. A chave de API é usada ao fazer solicitações entre a instância do app e a API do Braze. A chave de API também é importante para a integração do SDK da Braze com seu app ou site.

![][5]

{% alert note %}
Você deve criar instâncias do app separadas para cada versão do seu aplicativo em cada plataforma. Por exemplo, se você tiver versões Free e Pro do seu aplicativo no iOS e no Android, crie quatro instâncias do app em seu espaço de trabalho (aplicativo gratuito para iOS, aplicativo gratuito para Android, aplicativo pro para iOS e aplicativo pro para Android). Isso dará quatro chaves de API para usar, uma para cada instância do app.
{% endalert %}

#### Versão do Live SDK

A versão do SDK ativo exibida na página Configurações do aplicativo para um aplicativo específico é a versão mais alta do aplicativo com pelo menos 5% do total de sessões diárias e com pelo menos 500 sessões no último dia.

Esse campo aparece após a integração do SDK da Braze com seu app ou site. Se uma versão mais recente do SDK da Braze estiver disponível para sua plataforma, ela será notada aqui com a tag "Versão mais nova disponível".

![][6]

### Etapa 4: Repetir conforme necessário

Repita as etapas 2 e 3 para configurar quantos espaços de trabalho seu plano exigir. Recomendamos que você crie um espaço de trabalho de teste para integração e teste de campanha.

{% alert tip %}
**Adicionar um espaço de trabalho de teste**<br>É possível realizar testes de app colocando determinados usuários completamente em sandbox na sua instância de produção. Crie um novo espaço de trabalho e, ao publicar seu aplicativo, certifique-se de alterar a chave de API que o Braze está usando para corresponder à do seu espaço de trabalho de produção em vez do espaço de trabalho de teste.
{% endalert %}

## Gerenciamento de espaços de trabalho

### Adicionar favoritos

Você pode adicionar espaços de trabalho favoritos para acessar ainda mais rapidamente os espaços de trabalho que mais usa.

![][7]

Para adicionar espaços de trabalho favoritos:

1. Selecione o menu suspenso do seu perfil e, em seguida, selecione **Gerenciar sua conta**.
2. Na seção **Account Profile (Perfil da conta** ), localize o campo **Favorite workspaces (Espaços de trabalho favoritos** ).
3. Selecione seus espaços de trabalho na lista.
4. Selecione **Salvar alterações**.

Não há limite para o número de espaços de trabalho que você pode adicionar como favorito, mas recomendamos manter essa lista curta por conveniência.

### Renomear espaços de trabalho

Para renomear seu espaço de trabalho:

1. Acesse **Configurações** > **Configurações do app**.
2. Passe o mouse sobre o nome de seu espaço de trabalho e selecione <i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i>.
3. Dê um novo nome ao seu espaço de trabalho e selecione <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Save**.

![][8]

### Exclusão de espaços de trabalho


Para excluir seu espaço de trabalho:

1. Acesse **Configurações** > **Configurações do app**.
2. Selecione **Excluir espaço de trabalho**.

{% alert warning %}
Tenha cuidado ao excluir espaços de trabalho! Depois que um espaço de trabalho é excluído, ele não pode ser restaurado.
{% endalert %}

![][9]

## Perguntas frequentes

### Devo criar um novo espaço de trabalho quando estiver lançando um aplicativo atualizado?

Se os usuários só precisarem atualizar o aplicativo e você não estiver lançando um aplicativo totalmente novo na loja de aplicativos, não deverá criar um novo espaço de trabalho, a menos que não planeje mais enviar mensagens aos usuários na versão mais antiga.

Ao criar um novo espaço de trabalho, todos os dados históricos e perfis de usuários da versão anterior do app não existirão nesse novo espaço de trabalho. Portanto, depois que os usuários existentes fizerem upgrade para a nova versão do aplicativo, eles terão um novo perfil criado sem nenhum dos dados de comportamento do aplicativo antigo.

Além disso, seus usuários existiriam em dois lugares: o espaço de trabalho antigo e o novo espaço de trabalho. Eles também podem ter o mesmo token por push. Isso pode fazer com que os usuários recebam uma mensagem de marketing destinada apenas aos usuários do espaço de trabalho antigo, mesmo que já tenham feito upgrade.

#### O que devo fazer em vez disso?

Para separar os aplicativos antigos dos novos, crie uma nova instância do app no mesmo espaço de trabalho. Dessa forma, é possível direcionar efetivamente os usuários para a nova versão ao selecionar esse app durante a segmentação. Se quiser enviar mensagens aos usuários que estão na versão antiga, poderá usar filtros para [direcionar a versão anterior do app]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

### Tenho várias instâncias do app em um espaço de trabalho. Como posso me certificar de direcionar minha mensagem apenas para um único app? {#singular-app}

Para garantir que sua mensagem seja direcionada apenas a um aplicativo específico, adicione um segmento que direcione apenas os usuários das instâncias do app escolhido. Isso é especialmente importante se um usuário tiver dois tokens por push para diferentes instâncias do app no mesmo espaço de trabalho. Nesse cenário, os usuários poderiam receber uma notificação de um app diferente daquele em que estão. Não é uma experiência ideal!

Por padrão, um segmento direciona todos os apps e sites no espaço de trabalho. Para configurar um segmento que direciona apenas um app ou site:

1. Crie um segmento com um nome significativo. No Braze, usamos o formato "Todos os usuários ({Nome} {Plataforma})". Por exemplo, "All Users (Upon Voyage iOS)".
2. Para **aplicativos e sites direcionados**, selecione **Usuários de aplicativos específicos**.
3. No menu suspenso **Aplicativos específicos**, selecione seu aplicativo ou site.

![][10]{: style="max-width:75%" }

Em seguida, você pode adicionar esse segmento à sua mensagem e começar a refinar ainda mais seu público com segmentos e filtros adicionais, se necessário.

#### Campanhas

Para campanhas, adicione seu segmento à etapa **Usuários-alvo** do criador.

#### Canvas Flow

No Canvas Flow, adicione seu segmento às etapas de Mensagem, na seção **Validações de entrega**. As validações de entrega conferem se o seu público atende aos critérios de entrega no envio da mensagem. Lembre-se de especificar validações de entrega para cada etapa da mensagem para garantir que ela seja entregue ao aplicativo correto. Não há necessidade de segmentar no nível de entrada.

{% details Expandir as etapas do fluxo de trabalho original do Canva %}

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar canvas usando o editor original. Esse conteúdo está disponível como referência para entender os segmentos e o direcionamento no editor original.<br><br>A Braze recomenda que os clientes que usam a experiência original do Canvas migrem para o Canvas Flow. É uma experiência de edição aprimorada para melhor construir e gerenciar canvas. Saiba mais sobre a [clonagem de canvas no Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

No fluxo de trabalho original do Canvas, adicione seu segmento ao nível do componente do Canvas na seção **Público**. Não há necessidade de segmentar no nível de entrada.
{% enddetails %}


[1]: {% image_buster /assets/img/workspaces/workspace_create.png %}
[2]: {% image_buster /assets/img/workspaces/workspace_name.png %}
[3]: {% image_buster /assets/img/workspaces/workspace_empty_state.png %}
[4]: {% image_buster /assets/img/workspaces/workspace_add_app.png %}
[5]: {% image_buster /assets/img/workspaces/app_api_key.png %}
[6]: {% image_buster /assets/img/workspaces/app_live_sdk_version.png %}
[7]: {% image_buster /assets/img/workspaces/workspace_favorites.png %}
[8]: {% image_buster /assets/img/workspaces/workspace_rename.gif %}
[9]: {% image_buster /assets/img/workspaces/workspace_delete.png %}
[10]: {% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %}
[link]: {{site.baseurl}}/user_guide/getting_started/workspaces/
