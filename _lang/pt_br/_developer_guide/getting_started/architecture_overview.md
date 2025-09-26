---
nav_title: Visão geral da arquitetura
article_title: Visão geral da arquitetura
page_order: 3
description: "Este artigo discute as diferentes partes e peças do stack de tecnologia da Braze, com links para artigos relevantes."
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

# Como começar: Visão geral da arquitetura

> Este artigo discute as diferentes partes e peças do stack de tecnologia da Braze, com links para artigos relevantes. 

Em última análise, a Braze trata de dados. A plataforma da Braze, com o SDK, a API REST e as integrações com parceiros, permite que você agregue e atue em cima de seus dados. 

![O Braze tem diferentes camadas. No total, ela é formada pelo SDK, a API, o dashboard e as integrações com parceiros. Cada uma delas contribui com partes de uma camada de ingestão de dados, uma camada de classificação, uma camada de orquestração, uma camada de personalização e uma camada de ação. A camada de ação tem vários canais, incluindo push, mensagens no app, Connected Catalog, webhook, SMS e e-mail.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [Ingestão de dados](#ingestion): O Braze extrai dados de uma variedade de fontes.
* [Classificação](#classification): Sua equipe de marketing segmenta dinamicamente sua base de usuários usando essas métricas. 
* [Orquestração](#orchestration): O Braze coordena de forma inteligente as mensagens para diferentes segmentos de público no momento ideal.
* [Ação](#action): Sua equipe de marketing age com base nos dados, criando conteúdo por meio de uma variedade de canais de envio de mensagens, como SMS e e-mail.
* [Personalização](#personalization): Os dados são transformados em tempo real com informações personalizadas sobre seu público. 
* [Exportação](#exporting-data): Em seguida, o Braze rastreia o engajamento de seus usuários com essas mensagens e as alimenta novamente na plataforma, criando um loop. Você obtém insights sobre esses dados por meio de relatórios e análises em tempo real.

Tudo isso funciona em conjunto para criar interações bem-sucedidas entre sua base de usuários e sua marca, de modo que você possa atingir suas metas. A Braze faz tudo isso no contexto de algo que chamamos de nosso stack verticalmente integrado. Vamos nos aprofundar em cada camada, uma de cada vez.

## Ingestão de dados {#ingestion}

A Braze foi desenvolvida com base em uma arquitetura de fluxo de dados que utiliza Snowflake, Kafka, MongoDB e Redis. Os dados de muitas fontes podem ser carregados na Braze por meio do SDK e da API. A plataforma pode lidar com qualquer dado em tempo real, independentemente de como ela esteja aninhada ou estruturada. Os dados do Braze são armazenados no perfil do usuário. 

{% alert tip %}
O Braze pode rastrear os dados de um usuário durante toda a jornada dele com você, desde o momento em que ele é anônimo até o momento em que ele faz o registro no seu app e é conhecido. As IDs de usuário, chamadas `external_id`s no Braze, devem ser definidas para cada um de seus usuários. Eles devem ser imutáveis e acessíveis quando um usuário abre o app, permitindo o rastreamento de seus usuários entre dispositivos e plataformas. Consulte o artigo [Ciclo de vida do usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) para obter as práticas recomendadas.
{% endalert %}

![A Braze importa fontes de dados de backend da API, fontes de dados de frontend do SDK, dados de data warehouse da nuvem pela ingestão de dados para nuvem da Braze e de integrações com parceiros. Esses dados são exportados por meio da API do Braze ]({% image_buster /assets/img/getting-started/import-export.png %}){: style="display:block;margin:auto;" }

{% alert note %}
Esse banco de dados de perfil de usuário centrado na pessoa permite velocidade interativa e em tempo real. O Braze pré-computa os valores quando os dados chegam e armazena os resultados em nosso formato de documento leve para recuperação rápida. E como a plataforma foi projetada dessa forma desde o início, ela é ideal para a maioria dos casos de uso de envio de mensagens, especialmente quando combinada com outros conceitos de dados, como Connected Content, catálogos de produtos e atribuições aninhadas.
{% endalert %}

### Fontes de dados de backend por meio da API do Braze
O Braze pode extrair dados de bancos de dados de usuários, transações off-line e data warehouses por meio de nossa [API REST]({{site.baseurl}}/api/endpoints/user_data). 

### Fontes de dados de front-end via Braze SDK
O Braze captura automaticamente dados primários de fontes de dados de front-end, como dispositivos de usuários, por meio do [Braze SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/). O SDK lida com novos usuários (anônimos) e gerencia os dados de seu perfil de usuário durante todo o seu ciclo de vida. 

### Integrações com parceiros
A Braze tem mais de 150 parceiros tecnológicos, que chamamos de "Alloys". Você pode complementar seus Data Feeds por meio de uma rede significativamente robusta de [tecnologias interoperáveis e APIs de dados.]({{site.baseurl}}/partners/home) 

### Conexão direta com o data warehouse por meio da ingestão de dados da nuvem da Braze
É possível enviar dados de clientes de seu data warehouse para a plataforma por meio da [Ingestão de dados para nuvem da Braze]({{site.baseurl}}/user_guide/data/cloud_ingestion/) em apenas alguns minutos, permitindo a sincronização de atributos, eventos e compras relevantes do usuário. A integração da ingestão de dados para a nuvem oferece suporte a estruturas de dados complexas, incluindo JSON aninhado e vetores de objetos.

A ingestão de dados na nuvem pode sincronizar dados do Snowflake, Amazon Redshift, Databricks e Google BigQuery.

## Classificação {#classification}
A camada de classificação ativa a sua equipe para classificar e criar públicos dinamicamente, chamados [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments), com base nos dados que passam pelo Braze. 

{% alert note %}
As camadas de classificação, orquestração e personalização são onde sua equipe de marketing fará a maior parte do trabalho. Eles interagem com essas camadas com mais frequência por meio do dashboard da Braze, nossa interface da Web. Os desenvolvedores têm uma função na configuração e na personalização dessas camadas.
{% endalert %}

Muitos tipos comuns de atribuições do usuário, como nome, e-mail, data de nascimento, país e outros, são automaticamente rastreados pelo SDK por padrão. Como desenvolvedor, você trabalhará com a sua equipe para definir quais dados adicionais e personalizados fazem sentido rastrear para o seu caso de uso. Seus dados personalizados afetarão a forma como sua base de usuários será classificada e segmentada. Você definirá esse modelo de dados durante o processo de implementação. 

Saiba mais sobre [os dados coletados automaticamente e os dados personalizados]({{site.baseurl}}/developer_guide/analytics/).

## Orquestração {#orchestration}
A camada de orquestração permite que sua equipe de marketing projete jornadas de usuário com base nos dados de usuários e no engajamento anterior. Esse trabalho é feito principalmente por meio de nossa interface de dashboard, mas você também tem a opção de lançar [campanhas por meio da API]({{site.baseurl}}/api/api_campaigns#api-campaigns). Por exemplo, você pode fazer com que seu backend informe ao Braze quando enviar as mensagens e campanhas que seus profissionais de marketing projetaram no dashboard e dispará-las de acordo com sua lógica de backend. Um exemplo de mensagem disparada pela API pode ser a redefinição de senha ou a confirmação de envio. 

{% alert note %}
As campanhas disparadas por API são ideais para casos de uso transacionais mais avançados. Eles permitem que os profissionais de marketing gerenciem o texto da campanha, os testes multivariantes e as regras de reelegibilidade no dashboard do Braze, enquanto disparam a entrega desse conteúdo a partir de seus servidores e sistemas. A solicitação da API para disparar a mensagem também pode incluir dados adicionais a serem modelados na mensagem em tempo real.
{% endalert %}


### Feature Flag
O Braze permite ativar ou desativar remotamente a funcionalidade para uma seleção de usuários por meio de [sinalizadores de recursos]({{site.baseurl}}/developer_guide/feature_flags/). Isso permite que os profissionais de marketing direcionem o segmento correto da sua base de usuários com envios de mensagens para recursos que ainda não foram implementados para todo o público. Mas, mais do que isso, os sinalizadores de recursos podem ser usados para ativar e desativar um recurso na produção sem implementação de código adicional ou atualizações da loja de aplicativos. Isso permite que você implemente novos recursos com segurança e confiança.

## Personalização {#personalization}
A camada de personalização representa a capacidade de fornecer conteúdo dinâmico em suas mensagens. Ao usar o Liquid, uma linguagem de personalização amplamente utilizada, sua equipe pode extrair dinamicamente os dados existentes para exibir a mensagem personalizada para cada destinatário. Além disso, você pode inserir qualquer informação acessível em seu servidor da Web ou via API diretamente nas mensagens que está enviando, como notificações por push ou e-mails, usando o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). O conteúdo conectado se baseia no Liquid e usa uma sintaxe familiar.

E como esse conteúdo dinâmico é programável, os profissionais de marketing podem incluir valores computados, respostas de outras chamadas ou itens do catálogo de produtos. Depois de configurar esses sistemas durante a implementação, sua equipe de marketing pode fazer isso com pouco ou nenhum suporte das equipes técnicas. 

## Ação {#action}
A camada de ação ativa o envio real de mensagens aos usuários. O objetivo da camada de ação é enviar a mensagem certa para o usuário certo no momento certo, com base nos dados disponíveis em todas as camadas discutidas anteriormente. O envio de mensagens é feito dentro do seu aplicativo ou site (como o envio de mensagens no app ou por meio de elementos gráficos como carrosséis e banners do cartão de conteúdo) ou fora da experiência no app (como o envio de notificações por push ou e-mails).

### Canais de envio de mensagens
O Braze foi projetado para lidar com um cenário tecnológico em evolução com seu modelo de dados independente de canal e centrado no usuário. O dashboard gerencia a entrega de mensagens e os disparos transacionais. Por exemplo, seus profissionais de marketing podem disparar uma mensagem SMS oferecendo um cupom para uma de suas lojas recém-inauguradas quando um usuário entrar no geofence definido próximo a esse local, ou enviar um e-mail a um usuário para informá-lo de que seu programa favorito tem uma nova temporada.

O [SDK do Braze]({{site.baseurl}}/user_guide/getting_started/web_sdk/) possibilita canais adicionais de envio de mensagens: push, mensagens no app e cartões de conteúdo. Você integra o SDK ao seu app ou site para permitir que sua equipe de marketing use o dashboard do Braze para coordenar suas campanhas em todos os canais de envio de mensagens compatíveis.

![]({% image_buster /assets/img/getting_started/channels.png %})

## Exportação de dados
De maneira crítica, todas as interações do usuário final com o Braze são rastreadas para que você possa medir seu engajamento e alcance. E depois que a Braze tiver agregado seus dados de todas essas fontes, eles poderão ser exportados de volta para seu stack de tecnologia usando uma variedade de ferramentas, fechando o ciclo.

### Currents
O [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) é um complemento opcional do Braze que fornece uma exportação de streaming granular que alimenta continuamente outros destinos de sua pilha. O Currents é um feed de dados brutos por usuário e por evento que exporta dados a cada cinco minutos ou a cada 15.000 eventos, o que ocorrer primeiro. Exemplos de alguns destinos downstream do Currents seriam Segment, S3, Redshift e Mixpanel, entre outros. 

### Compartilhamento de dados Snowflake
A funcionalidade de [compartilhamento seguro de dados]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) do Snowflake permite que o Braze lhe dê acesso seguro aos dados em nosso portal Snowflake sem se preocupar com o atrito do fluxo de trabalho, os pontos de falha e os custos desnecessários que vêm com os relacionamentos típicos com os provedores de dados. Todo o compartilhamento é realizado por meio da camada de serviços e do armazenamento de metadados exclusivos da Snowflake: nenhum dado é realmente copiado ou transferido entre as contas. Esse é um conceito importante porque os dados compartilhados não ocupam nenhum espaço de armazenamento em uma conta de consumidor e, portanto, não contribuem para suas cobranças mensais de armazenamento de dados. Os únicos encargos para os consumidores são os recursos de computação (ou seja, data warehouses virtuais) usados para consultar os dados compartilhados.

### APIs de exportação do Braze
A API do Braze fornece [endpoints]({{site.baseurl}}/api/endpoints/export) que permitem exportar análises agregadas de forma programática, bem como exportar dados de usuários individuais. Esses dados podem ser exportados para públicos e segmentos de qualquer tamanho. 

### CSVs
Por fim, há uma opção para baixar seus dados em nível agregado diretamente do dashboard como um [CSV]({{site.baseurl}}/user_guide/data/export_braze_data/). A opção CSV permite que os membros da sua equipe exportem facilmente os dados do Braze.

{% alert tip %}
Embora a exportação CSV tenha um limite básico de 500.000 linhas, as APIs não têm um limite nesse sentido.
{% endalert %}

## Juntando tudo 
Um dos seus usuários, vamos chamá-lo de Mel, acabou de receber o anúncio do seu produto. Nos bastidores, todas as camadas da plataforma Braze trabalharam juntas para garantir que esse processo ocorresse sem problemas. 

As informações de Mel foram transferidas para o Braze de sua plataforma legada de engajamento com clientes por meio de uma importação de CSV. Toda vez que Mel interagia com seu app após a integração, mais dados eram adicionados ao perfil de cliente dela. 

Seu anúncio de produto foi enviado a todos os clientes que gostaram de um item semelhante em seu app. Você definiu esses dados como um evento personalizado. O SDK fez o rastreamento desse evento e segmentou sua base de usuários de acordo com isso. A Braze orquestrou a melhor hora do dia para enviar esse anúncio e personalizou o anúncio chamando Mel pelo seu nome preferido. 

Quando Mel abre o anúncio, ela adiciona seu novo produto à lista de desejos dela. A Braze rastreia o fato de ela ter clicado no e-mail automaticamente. O SDK rastreia o fato de ela ter colocado seu novo produto na lista de desejos. Cada vez que eles se engajam com a sua marca, você e seus usuários aprendem mais um sobre o outro.

![]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})



