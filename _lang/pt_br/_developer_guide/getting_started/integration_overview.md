---
nav_title: Visão geral da integração
article_title: Visão geral da integração
page_order: 2
description: "Este artigo fornece uma visão geral básica do processo de integração."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %}](https://learning.braze.com/sdk-integration-basics) ){: style="float:right;width:120px;border:0;" class="noimgborder"}Primeiros passos: Visão geral da integração

> Este artigo fornece uma visão geral básica do processo de integração.

![Um diagrama de Venn de quatro círculos - descoberta, integração, garantia de qualidade e manutenção - centrado em torno de "tempo para valor."]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"} 

Como um recurso técnico, você capacitará sua equipe integrando à Braze ao seu stack de tecnologia. A integração é dividida, em linhas gerais, em quatro etapas:
* [Descoberta e planejamento](#discovery): Trabalhe com sua equipe para alinhar o escopo, planejar uma estrutura para dados e campanhas e criar uma estrutura de espaço de trabalho apropriada. 
* [Integração](#integration): Execute seu plano integrando o SDK e a API, ativando canais de envio de mensagens e configurando a importação e exportação de dados. 
* [Controle de qualidade](#qa): Confirme se o loop de dados e envio de mensagens entre a plataforma Braze e seu app ou site está funcionando conforme o esperado.
* [Manutenção](#maintenance): Depois de passar a Braze para a sua equipe de marketing, você continuará a garantir que tudo continue a funcionar sem problemas.

<br>
{% alert tip %}
Reconhecemos que cada organização tem suas necessidades distintas, e o Braze foi criado para atender a uma gama diversificada de opções de personalização que podem ser adaptadas às suas necessidades específicas. Os tempos de integração variam de acordo com seu caso de uso. 
{% endalert %}

## Descoberta e planejamento {#discovery}

Durante essa fase, você trabalhará com a sua equipe para definir o escopo das tarefas de integração e garantir que todas as partes interessadas estejam alinhadas a um objetivo comum. 

Sua equipe realizará o planejamento de ponta a ponta dos seus casos de uso para garantir que tudo possa ser criado conforme o esperado, com os dados corretos disponíveis para isso. Essa fase inclui o líder do projeto, o líder de CRM, a engenharia de front e back-end, os proprietários de produtos e os profissionais de marketing. 

A fase de descoberta e planejamento leva, em média, cerca de seis semanas. Os líderes de engenharia podem esperar passar de 2 a 4 horas por semana durante essa fase. Os desenvolvedores que trabalham com o produto podem esperar passar de 10 a 20 horas por semana no Braze durante a fase de descoberta e planejamento. 

{% alert tip %}
Durante o período de integração de sua empresa, a Braze realizará sessões de visão geral técnica. Recomendamos enfaticamente que os engenheiros participem dessas sessões. As sessões de visão geral técnica lhe dão a oportunidade de conversar sobre a escalabilidade da arquitetura da plataforma e ver exemplos práticos de como empresas do seu porte foram bem-sucedidas em casos de uso semelhantes.
{% endalert %}

![Ícones para diferentes canais, como e-mail, carrinho de compras, imagens, geolocalização, e assim por diante.]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"} 

### Planejamento de campanha

Sua equipe de CRM planejará os casos de uso de envio de mensagens que serão lançados em um futuro próximo. Isso inclui o:
* [Canal]({{site.baseurl}}/user_guide/message_building_by_channel) (por exemplo, notificações por push ou mensagens no app)
* [Método de entrega]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types) (por exemplo, entrega programada ou entrega baseada em ação)
* [Público alvo]({{site.baseurl}}/user_guide/engagement_tools/segments)
* [Métricas de sucesso]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)

Por exemplo, uma campanha para novos clientes pode ser: um e-mail enviado diariamente às 10 horas para um segmento de clientes que registraram sua primeira sessão ontem. O evento de conversão (a métrica de sucesso) é o registro de uma sessão.

<br>
{% alert important %}
A integração não pode começar até que a etapa de planejamento da campanha esteja concluída. Essa etapa determinará quais partes e peças do Braze precisam ser configuradas durante a fase de integração.
{% endalert %}

### Criação de requisitos de dados

Em seguida, sua equipe de CRM deve definir quais dados são necessários para lançar as campanhas planejadas, criando requisitos de dados. 

Muitos tipos comuns de atribuições do usuário, como nome, e-mail, data de nascimento, país e similares, são automaticamente rastreados após a integração do SDK da Braze. Outros tipos de dados precisarão ser definidos como dados personalizados.

Como desenvolvedor, você trabalhará com sua equipe para definir quais dados adicionais e personalizados fazem sentido rastrear. Seus dados personalizados afetarão a forma como sua base de usuários será classificada e segmentada. Você configurará uma taxonomia de eventos em todo o seu growth stack, estruturando seus dados para que sejam compatíveis com seus sistemas à medida que entram e saem do Braze.

{% alert tip %}
Mantenha a nomenclatura dos dados consistente em todas as ferramentas. Por exemplo, seu data warehouse pode registrar "comprar oferta por tempo limitado" de uma maneira específica. Você precisará decidir se é necessário um evento personalizado no Braze para corresponder a esse formato.
{% endalert %}

Saiba mais sobre [os dados coletados automaticamente e os dados personalizados]({{site.baseurl}}/developer_guide/analytics/).

### Planejamento de personalizações

Converse com seus profissionais de marketing sobre as personalizações desejadas. Por exemplo, você deseja implementar os cartões de conteúdo padrão da Braze? Deseja ajustar ligeiramente a aparência e o comportamento para que correspondam às diretrizes de sua marca? Deseja desenvolver uma interface de usuário totalmente nova para um componente e fazer com que o Braze rastreie sua análise de dados? Diferentes níveis de personalização exigem diferentes níveis de escopo.

### Como obter acesso ao dashboard

O dashboard do Braze é nossa interface de usuário na web. Os profissionais de marketing usarão o dashboard para fazer seu trabalho e criar conteúdo. Os desenvolvedores usam o dashboard para gerenciar as configurações de integração de apps, como chaves de API e credenciais de notificação por push.

O administrador da sua equipe deve adicionar você (e todos os outros membros da equipe que precisam de acesso ao Braze) como usuários no seu dashboard.

### Espaços de trabalho e chaves de API

O administrador da sua equipe também criará diferentes [espaços de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/). Os espaços de trabalho agrupam seus dados - usuários, segmentos, chaves de API - em um único local. Como prática recomendada, sugerimos colocar apenas versões diferentes do mesmo app ou de apps muito semelhantes em um único espaço de trabalho. 

É importante ressaltar que os espaços de trabalho fornecem chaves de API para várias plataformas (como iOS e Android). Você usará as chaves de API correlacionadas para associar os dados do SDK a um espaço de trabalho específico. Navegue até seus espaços de trabalho para acessar a chave de API de cada um de seus apps. Confira se cada chave de API tem as permissões corretas para executar o trabalho que você definiu como escopo. Consulte o [artigo sobre provisionamento da API]({{site.baseurl}}/api/basics/#rest-api-key) para saber mais.

{% alert important %}
É importante que você configure ambientes diferentes para desenvolvimento e produção. A configuração de um ambiente de teste evitará que você gaste dinheiro real durante a integração e o controle de qualidade. Para criar um ambiente de teste, configure um espaço de trabalho de teste e certifique-se de usar a respectiva chave de API para não preencher o espaço de trabalho de produção com dados de teste.
{% endalert %}  

## Integração {#integration}

![Gráfico de pirâmide abstrato representando o fluxo de informações de uma fonte de dados para um dispositivo do usuário.]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"} 

A Braze oferece suporte a aplicativos iOS, Android, aplicativos da Web e muito mais. Você também pode aceitar usar um wrapper SDK de plataforma cruzada, como o React Native ou o Unity. Normalmente, vemos os clientes se integrarem em um período de 1 a 6 semanas. Muitos clientes integraram a Braze com apenas um engenheiro, dependendo da amplitude de suas habilidades técnicas e da disponibilidade. Depende inteiramente do seu escopo específico de integração e de quanto tempo sua equipe dedica ao projeto Braze. 

Você precisará de desenvolvedores que estejam familiarizados com:
* Trabalhar na camada nativa de seu app ou site
* Criação de processos para acessar nossa API REST
* Teste de integração 
* Autenticação de token da Web JSON
* Habilidades gerais de gerenciamento de dados
* Configurações de registros DNS

### Integração com parceiros do CDP

Muitos clientes usam a integração da Braze como uma oportunidade de também se integrar a uma plataforma de dados do cliente (CDP) como um parceiro de integração. A Braze oferece rastreamento e análise de dados, enquanto uma CDP pode oferecer roteamento e orquestração de dados adicionais. A Braze oferece integração perfeita com muitas CDPs, como a [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle/) e [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/). 

Se estiver realizando a integração lado a lado com uma CDP, você mapeará as chamadas do SDK da sua CDP para o SDK da Braze. Essencialmente, você irá:
* Mapear chamadas de identificação para `changeUser` [(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)) e definir atribuições.
* Chamadas de fluxo de dados de mapas para `requestImmediateDataFlush` [(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush)).
* Registre eventos personalizados ou compras.

Exemplos de integrações entre o SDK da Braze e a CDP de sua escolha podem estar disponíveis, dependendo da plataforma que você escolheu. Para saber mais, consulte nossa [lista de parceiros de tecnologia CDP]({{site.baseurl}}/partners/data_and_analytics/). 

### Integração do SDK do Braze

O Braze SDK fornece duas funcionalidades essenciais: coleta e sincroniza os dados de usuários em um perfil de usuário consolidado e alimenta os canais de envio de mensagens, como notificações por push, mensagens no app e cartões de conteúdo. 

{% alert tip %}
Quando estiver totalmente integrado ao seu app ou site, o SDK da Braze oferece um nível de sofisticação de marketing totalmente realizado. Se você adiar a integração do SDK da Braze, algumas das funcionalidades descritas na documentação não estarão disponíveis.
{% endalert %}

Durante a implementação do SDK, você irá:

* Escrever o código de integração de SDK para cada plataforma à qual você deseja oferecer suporte.
* Ative os canais de envio de mensagens para cada plataforma, garantindo que o SDK do Braze rastreie os dados das interações com seus clientes por e-mail, SMS, notificações por push e outros canais.
* Crie quaisquer personalizações de componentes de UI planejadas (por exemplo, Cartões de Conteúdo personalizados). Para conteúdo totalmente personalizado, será necessário registrar a análise de dados, pois a coleta automática de dados do SDK não estará ciente dos seus novos componentes. Você pode padronizar essa implementação em nossos componentes padrão.

### Usando a API do Braze

Você usará nossa API REST para diferentes tarefas em diferentes momentos ao longo de seu tempo de uso do Braze. A API do Braze é útil para:

1. Importação de dados históricos; e
2. Atualizações contínuas que não são disparadas no Braze. Por exemplo, o perfil de um usuário faz upgrade para VIP sem que ele faça login em um app, portanto, a API precisa comunicar essas informações à Braze.

Comece com a [API da Braze]({{site.baseurl}}/api/basics).

{% alert important %}
Ao usar a API, não deixe de enviar suas solicitações em lote e envie apenas valores delta. O Braze reescreve todas as atribuições que são enviadas. Não atualize nenhum atributo personalizado se seu valor não tiver sido alterado.
{% endalert %}

### Configuração da análise de dados do produto

A Braze tem tudo a ver com dados. Os dados do Braze são armazenados no perfil do usuário. 

Os pontos de dados são uma estrutura por meio da qual você garante que está capturando os dados certos para seus profissionais de marketing, e não apenas "qualquer" dado que possa ser aspirado. Familiarize-se com os [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/).

### Migração de dados de usuários antigos

Você pode usar o [`/users/track endpoint`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da Braze para migrar dados históricos que foram registrados fora da Braze. Exemplos de dados comumente importados incluem tokens por push e compras anteriores. Esse endpoint pode ser usado para importações pontuais ou atualizações regulares em lote. 

Também é possível fazer a importação de usuários e atualizar os valores dos atributos personalizados por meio de um único [upload de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-a-csv) para o dashboard. Fazer upload de CSVs pode ser útil para profissionais de marketing, enquanto nossa API REST permite maior flexibilidade.

### Configuração do rastreamento de sessão

O SDK do Braze gera pontos de dados de "sessão aberta" e "sessão fechada". O SDK da Braze também libera os dados em intervalos regulares. Consulte esses links para obter os valores padrão de rastreamento de sessão, todos os quais podem ser personalizados ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)).

### Rastreamento de eventos personalizados, atributos e eventos de compra

Coordene-se com sua equipe para configurar o esquema de dados planejado, incluindo eventos personalizados, atributos de usuários e eventos de compra. Seu [esquema de dados personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) será inserido usando o dashboard e deve corresponder exatamente ao que foi implementado durante a integração de SDK.

{% alert tip %}
As IDs de usuário, chamadas `external_id`s na Braze, devem ser definidas para todos os usuários conhecidos. Eles devem ser imutáveis e acessíveis quando um usuário abre o app, permitindo o rastreamento de seus usuários entre dispositivos e plataformas. Consulte o artigo [Ciclo de vida do usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) para obter as práticas recomendadas.
{% endalert %}

### Outras ferramentas

Com base em seu caso de uso, pode haver outras ferramentas que você precise configurar. Por exemplo, talvez seja necessário configurar uma ferramenta como [geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/) para realizar suas histórias de usuários. Descobrimos que os clientes que têm a capacidade de configurar essas ferramentas adicionais depois de concluir as etapas essenciais de integração são mais bem-sucedidos.

## Controle de qualidade {#qa}
Ao executar a integração, você executará um controle de qualidade para assegurar que tudo o que está sendo configurado esteja funcionando conforme o esperado. Esse controle de qualidade se divide em duas categorias gerais: ingestão de dados e canais de envio de mensagens.

{% alert important %}
Confira se os seus ambientes de produção e teste estão configurados antes de iniciar o controle de qualidade.
{% endalert %}

| **Ingestão de dados de controle de qualidade**  | **Envio de mensagens de controle de qualidade**                                              |
|---------------------------|---------------------------------------------------------------|
| Você executará o controle de qualidade na forma como os dados são ingeridos, armazenados e exportados. | Você terá certeza de que as mensagens estão sendo enviadas corretamente aos usuários e que tudo está excelente. |
| Execute testes para confirmar que os dados estão armazenados corretamente. | Crie segmentos de usuários. |
| Confirme se os dados da sessão estão corretamente atribuídos ao espaço de trabalho pretendido no Braze. | Lançar campanhas e telas com sucesso. |
| Confirme se o início e o fim da sessão estão sendo registrados. | Confirme se as campanhas corretas estão sendo exibidas para os segmentos de usuários corretos. |
| Confirme se as informações de atribuição do usuário estão corretamente registradas nos perfis de usuário. | Confirme se os tokens por push estão sendo registrados corretamente. |
| Teste se os dados personalizados estão sendo registrados corretamente nos perfis de usuários. | Confirme se os tokens por push foram removidos corretamente. |
| Crie perfis de usuário anônimos. | Teste se as campanhas push estão sendo enviadas corretamente para os dispositivos e se o engajamento está registrado. |
| Confirme se os perfis de usuário anônimos se tornam perfis de usuário conhecidos quando o método `changeUser()` é chamado. | Teste se as mensagens no app são entregues e se as métricas são registradas. |
|                           | Teste se os cartões de conteúdo são entregues e se as métricas são registradas. |
|                           | Facilitar o conteúdo conectado (por exemplo, Accuweather). |
|                           | Confirme se todas as integrações de canais de envio de mensagens estão funcionando corretamente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Ao realizar QA na sua integração de SDK, use o [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sem ativar o registro detalhado para o seu app.
{% endalert %}

### Passando a Braze para os profissionais de marketing

Depois de integrar a plataforma ou o site, envolva a equipe de marketing para passar a propriedade da plataforma para eles. Esse processo é diferente em cada empresa, mas pode incluir o seguinte:

* Criação de uma [lógica Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid) complexa
* Ajuda para facilitar [o aquecimento de IP de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)
* Garantia de que outras partes interessadas entendam o tipo de dados que estão sendo rastreados

### Desenvolver para o futuro

Você já herdou uma base de código e não tinha a menor ideia do que o desenvolvedor inicial estava pensando? Pior ainda, você já escreveu um código, entendeu-o completamente e depois ficou completamente perplexo quando voltou a ele um ano depois? 

Durante a integração da Braze, as decisões coletivas tomadas em relação a dados, perfis de usuários, quais integrações estavam e não estavam no escopo, como as personalizações deveriam funcionar e muito mais, parecerão frescas em sua mente e, portanto, óbvias. Quando sua equipe quiser expandir a Braze ou quando outros recursos técnicos forem atribuídos ao seu projeto Braze, essas informações serão obscuras.

Crie um recurso para consolidar as informações que você aprendeu durante as sessões de visão geral técnica. Esse recurso ajudará a reduzir o tempo de integração de novos desenvolvedores que se juntam à sua equipe (ou servirá como um lembrete para você mesmo quando precisar expandir sua implementação atual do Braze). 

## Manutenção {#maintenance}

Após a transferência para seus profissionais de marketing, você continuará a servir como um recurso para manutenção. Você prestará atenção às atualizações do iOS e do Android que possam afetar o SDK da Braze e garantirá que seus fornecedores terceirizados estejam atualizados. 

Você fará o rastreamento das atualizações da plataforma Braze por meio do Braze [GitHub](https://github.com/braze-inc/). Ocasionalmente, seu administrador também receberá e-mails sobre atualizações urgentes e correções de bugs diretamente da Braze. 

## Limites de taxa do SDK 

### Usuários Ativos Mensais CY 24-25 

Para os clientes que adquiriram Usuários Ativos Mensais - CY 24-25, a Braze impõe limites de taxa do lado do servidor nas solicitações de API usadas por nossos SDKs para atualizar sessões, atributos de usuário, eventos e outros dados de perfil de usuário. Isso é para garantir a estabilidade da plataforma e manter um serviço rápido e confiável. 

* Os limites de taxa horária são definidos de acordo com o tráfego esperado do SDK em sua conta, que pode corresponder ao número de usuários ativos mensais (MAU) que você adquiriu, setor, sazonalidade ou outros fatores. Quando o limite de frequência horário é atingido, a Braze irá limitar as solicitações até a próxima hora.
* Todas as solicitações com limite de taxa são automaticamente reprocessadas pelo SDK.
* As solicitações do SDK estão correlacionadas com a quantidade de dados personalizados coletados em sua implementação. Se você está consistentemente perto ou no seu limite de frequência horário, considere:
    * Revisando sua integração de SDK para reduzir a coleta excessiva de dados.
    * Bloqueando dados personalizados que não são essenciais para seus casos de uso de marketing.
* Os limites de taxa de explosão são limites de taxa de curta duração que se aplicam quando um alto volume de solicitações chega em um período muito curto (ou seja, em segundos). Você não precisa tomar medidas quando os limites de estouro ocorrem, e o SDK tentará novamente em breve.

### Encontrando seus limites de taxa

Para encontrar os limites atuais com base na taxa de transferência esperada do SDK, acesse **Configurações** > **APIs e identificadores** > **Limites de API e SDK**.

Para uso histórico, acesse **Configurações** > **APIs e identificadores** > **Dashboard de API e SDK**.

### Mudanças e suporte

A brasagem pode modificar os limites de taxa para proteger a estabilidade do sistema ou permitir um aumento na taxa de transferência de dados na sua conta. Entre em contato com o suporte da Braze ou com seu gerente de sucesso do cliente para perguntas ou preocupações sobre limites de taxa e como eles impactam seu negócio.
