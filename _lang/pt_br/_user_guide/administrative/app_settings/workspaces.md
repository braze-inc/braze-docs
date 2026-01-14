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

Tudo o que você faz no Braze acontece em um espaço de trabalho. Os espaços de trabalho são um ambiente compartilhado para que você acompanhe e gerencie o envolvimento de aplicativos móveis ou sites relacionados. Os espaços de trabalho agrupam os mesmos aplicativos ou aplicativos muito semelhantes: por exemplo, as versões para Android e iOS do seu aplicativo móvel. 

## Criação de um espaço de trabalho

### Etapa 1: Tenha um plano

Antes de começar, certifique-se de ter trabalhado com sua equipe e com o gerente de integração do Braze para determinar a melhor configuração de espaço de trabalho para o seu caso de uso. Para saber mais sobre como planejar seus espaços de trabalho no Braze, consulte o site [Getting Started: Espaços de trabalho]({{site.baseurl}}/user_guide/getting_started/workspaces/) guide.

### Etapa 2: Adicione seu espaço de trabalho

Você pode criar novos espaços de trabalho ou alternar entre espaços de trabalho existentes no menu suspenso do espaço de trabalho no cabeçalho global.

1. Selecione o menu suspenso do espaço de trabalho e, em seguida, <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Create workspace**.

\![O menu suspenso do espaço de trabalho com o botão "Criar espaço de trabalho".]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Dê um nome ao seu espaço de trabalho.

{% alert tip %}
Talvez você queira adotar uma convenção de nomes para que outras pessoas da empresa possam encontrar facilmente seu espaço de trabalho. Por exemplo: "Upon Voyage US - Produção" e "Upon Voyage US - Encenação".
{% endalert %}

{:start="3"}
3\. Selecione **Criar**. Pode levar alguns segundos para que o Braze crie seu espaço de trabalho.

\!["Criar espaço de trabalho" modal com o nome "Upon Voyage US - Staging".]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

Você será levado à página **Configurações do aplicativo** para começar a adicionar suas instâncias de aplicativo. Você pode acessar essa página a qualquer momento em **Configurações** > **Configurações do aplicativo**.

Página "Configurações do aplicativo" para o espaço de trabalho do Upon Voyage US - Staging com um botão para adicionar um aplicativo.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### Etapa 3: Adicione suas instâncias de aplicativo

Nós nos referimos aos diferentes sites e aplicativos que são coletados em um espaço de trabalho como "instâncias de aplicativos".

1. Na página **Configurações do aplicativo**, selecione **\+ Adicionar aplicativo**.
2. Dê um nome à sua instância de aplicativo e selecione em qual plataforma ou plataformas essa instância de aplicativo está. Se você selecionar várias plataformas, o Braze criará uma instância do aplicativo para cada plataforma.

\!["Add New App to Upon Voyage US - Staging" modal com opções para selecionar detalhes do aplicativo.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3\. Selecione **Adicionar aplicativo** para confirmar.

#### Chaves da API do aplicativo

Depois de adicionar a instância do seu aplicativo, você terá acesso à chave de API dele. A chave de API é usada ao fazer solicitações entre a instância do seu aplicativo e a API do Braze. A chave de API também é importante para integrar o Braze SDK ao seu aplicativo ou site.

Página de configurações do aplicativo Upon Voyage para iOS com campos para a chave de API e o ponto de extremidade do SDK.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
Você deve criar instâncias de aplicativo separadas para cada versão do seu aplicativo em cada plataforma. Por exemplo, se você tiver versões Free e Pro do seu aplicativo no iOS e no Android, crie quatro instâncias de aplicativo em seu espaço de trabalho (aplicativo gratuito para iOS, aplicativo gratuito para Android, aplicativo pro para iOS e aplicativo pro para Android). Isso lhe dará quatro chaves de API para usar, uma para cada instância de aplicativo.
{% endalert %}

#### Versão do Live SDK

A versão do SDK ativo exibida na página Configurações do aplicativo para um aplicativo específico é a versão mais alta do aplicativo com pelo menos 5% do total de sessões diárias e com pelo menos 500 sessões no último dia.

Esse campo é exibido depois que você tiver integrado o Braze SDK ao seu aplicativo ou site. Se uma versão mais recente do SDK do Braze estiver disponível para sua plataforma, ela será registrada aqui com a tag "Newer Version Available".

Seção "["Live SDK Version"] com um valor de campo "5.4.0" e um ícone que informa que uma nova versão está disponível.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### Etapa 4: Repetir conforme necessário

Repita as etapas 2 e 3 para configurar quantos espaços de trabalho seu plano exigir. Como prática recomendada, recomendamos que você crie um espaço de trabalho de teste para integração e teste de campanha.

{% alert tip %}
**Adicionar um espaço de trabalho de teste**<br>Você pode realizar testes de aplicativos colocando determinados usuários completamente em sandbox na sua instância de produção. Crie um novo espaço de trabalho e, ao publicar seu aplicativo, certifique-se de alterar a chave de API que o Braze está usando para corresponder à do seu espaço de trabalho de produção em vez do espaço de trabalho de teste.
{% endalert %}

## Gerenciamento de espaços de trabalho

### Adicionar favoritos

Você pode adicionar espaços de trabalho favoritos para acessar ainda mais rapidamente os espaços de trabalho que mais usa.

\![Menu suspenso Espaço de trabalho com a guia "Espaços de trabalho favoritos".]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

Para adicionar espaços de trabalho favoritos:

1. Selecione o menu suspenso do seu perfil e, em seguida, selecione **Gerenciar sua conta**.
2. Na seção **Account Profile (Perfil da conta** ), localize o campo **Favorite workspaces (Espaços de trabalho favoritos** ).
3. Selecione seus espaços de trabalho na lista.
4. Selecione **Salvar alterações**.

Não há limite para o número de espaços de trabalho que você pode adicionar como favorito, mas recomendamos manter essa lista curta por conveniência.

### Renomear espaços de trabalho

Para renomear seu espaço de trabalho:

1. Vá para **Configurações** > **Configurações do aplicativo**.
2. Passe o mouse sobre o nome do seu espaço de trabalho e selecione <i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i>.
3. Dê um novo nome ao seu espaço de trabalho e selecione <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Save**.

O ícone de lápis que aparece ao lado do nome do espaço de trabalho.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Exclusão de workspaces e instâncias de aplicativos

Para excluir seu espaço de trabalho ou instância de aplicativo:

1. Vá para **Configurações** > **Configurações do aplicativo**.
2. Selecione **Excluir espaço de** trabalho para excluir o respectivo espaço de trabalho ou selecione o ícone da lixeira ao lado da respectiva instância do aplicativo.

Não é possível excluir instâncias de aplicativos ou espaços de trabalho que estejam sendo usados atualmente para direcionar usuários ou que tenham mais de 1.000 usuários. Se você tentar fazer isso, receberá uma mensagem de erro. Para prosseguir e excluí-los, [crie um caso de suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/) que inclua um link do painel e o nome da instância do aplicativo ou do espaço de trabalho a ser excluído.

{% alert warning %}
Tenha cuidado ao excluir espaços de trabalho! Depois que um espaço de trabalho é excluído, ele não pode ser restaurado.
{% endalert %}

A página de configurações do aplicativo com um botão para excluir um espaço de trabalho e um ícone de lixeira para excluir um aplicativo.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Perguntas frequentes

### Devo criar um novo espaço de trabalho quando estiver lançando um aplicativo atualizado?

Isso depende do fato de você estar atualizando seu aplicativo ou criando um aplicativo totalmente novo.

#### Atualizando seu aplicativo

Se você estiver atualizando o aplicativo, deverá separar as versões antiga e nova criando uma nova instância do aplicativo no mesmo espaço de trabalho. Dessa forma, você pode segmentar efetivamente os usuários da nova versão ao selecionar esse aplicativo durante a segmentação. Se você quiser enviar mensagens aos usuários que estão na versão antiga, poderá usar filtros para [direcionar a versão anterior do aplicativo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

Se você criar um novo espaço de trabalho, seus usuários existirão em dois lugares: o espaço de trabalho antigo e o novo. Eles também poderiam ter o mesmo token de envio. Isso pode fazer com que os usuários recebam uma mensagem de marketing destinada apenas aos usuários antigos do espaço de trabalho, mesmo que já tenham feito o upgrade.

#### Lançamento de um novo aplicativo

Se você estiver lançando um aplicativo totalmente novo na loja de aplicativos, deverá criar um novo espaço de trabalho. Ao criar um novo espaço de trabalho, todos os dados históricos e perfis de usuário da versão anterior do aplicativo não existirão nesse novo espaço de trabalho. Portanto, depois que os usuários existentes atualizarem para a nova versão do aplicativo, eles terão um novo perfil criado sem nenhum dos dados comportamentais do aplicativo antigo.

### Tenho várias instâncias de aplicativos em um espaço de trabalho - como posso me certificar de que minha mensagem seja direcionada apenas para um único aplicativo? {#singular-app}

Para garantir que sua mensagem seja direcionada somente a um aplicativo específico, adicione um segmento que seja direcionado somente aos usuários das instâncias de aplicativo escolhidas. Isso é especialmente importante se um usuário tiver dois tokens de envio para instâncias de aplicativos diferentes no mesmo espaço de trabalho. Nesse cenário, os usuários poderiam receber uma notificação de um aplicativo diferente daquele em que estão. Não é uma experiência ideal!

Por padrão, um segmento tem como alvo todos os aplicativos e sites no espaço de trabalho. Para configurar um segmento que tenha como alvo apenas um aplicativo ou site:

1. Crie um segmento com um nome significativo. Na Braze, usamos o formato "Todos os usuários ({Nome} {Plataforma})". Por exemplo, "All Users (Upon Voyage iOS)".
2. Para **Aplicativos e sites direcionados**, selecione **Usuários de aplicativos específicos**.
3. No menu suspenso **Aplicativos específicos**, selecione seu aplicativo ou site.

\![Segmento que tem como alvo usuários de aplicativos específicos.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

Em seguida, você pode adicionar esse segmento à sua mensagem e começar a refinar ainda mais seu público-alvo com segmentos e filtros adicionais, se necessário.

#### Campanhas

Para campanhas, adicione seu segmento à etapa **Target Audiences (Públicos-alvo** ) do compositor.

#### Tela

No Canvas, adicione seu segmento às etapas da mensagem, na seção **Validações de entrega**. As validações de entrega verificam novamente se o público-alvo atende aos critérios de entrega no envio da mensagem. Lembre-se de especificar validações de entrega para cada etapa da mensagem para garantir que ela seja entregue ao aplicativo correto. Não há necessidade de segmentar no nível de entrada.

{% details Expand for steps in the original Canvas workflow %}

No fluxo de trabalho original do Canvas, adicione seu segmento ao nível do componente do Canvas na seção **Audience (Público)**. Não há necessidade de segmentar no nível de entrada.

{% enddetails %}


