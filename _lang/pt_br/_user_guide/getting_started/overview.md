---
nav_title: Visão geral do Braze
article_title: "Primeiros passos: Visão geral do Braze"
page_order: 1
page_type: reference
description: "Familiarize-se com os principais conceitos que você precisará conhecer ao trabalhar no Braze."

---

# Primeiros passos: Visão geral do Braze

Bem-vindo ao Braze! Esta coleção de artigos o ajudará a começar a usar nossa plataforma e o apresentará aos principais termos, recursos e funcionalidades do Braze. Esta página apresenta os principais conceitos que você precisará conhecer ao trabalhar no Braze.

{% alert tip %}
É altamente recomendável conferir nosso curso gratuito [Braze Foundations for Everyone](https://learning.braze.com/page/braze-foundations-for-everyone) juntamente com esses artigos. Não é necessário nenhum login ou conta especial para este curso. Se você for um desenvolvedor e estiver procurando um resumo técnico do Braze, confira também o [Getting Started for Developers]({{site.baseurl}}/developer_guide/getting_started/platform_overview/).
{% endalert %}

Nas seções de Introdução, vamos nos concentrar nas implementações comuns do Braze. No entanto, o Braze é incrivelmente flexível e pode ser personalizado para agregar valor à sua organização de várias maneiras. Para garantir a clareza e a brevidade, fornecemos uma visão geral descritiva da configuração padrão em vez de oferecer instruções rígidas. Reconhecemos que cada organização tem suas necessidades distintas, e o Braze foi criado para atender a uma ampla gama de opções de personalização que podem ser adaptadas às suas necessidades específicas.

Vamos explorar juntos o poder do Braze.

## Como funciona o Braze

A Braze é uma plataforma de envolvimento do cliente que ajuda marcas de todos os tamanhos a criar campanhas personalizadas e direcionadas em vários canais. O Braze lhe dá a capacidade de ouvir seus clientes, entender o que o comportamento deles está sinalizando e, em seguida, agir enviando aos clientes a mensagem certa, por meio do canal certo, no momento certo.

{% alert tip %}
Certifique-se de [adicionar seus colegas ao Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users) para que eles possam explorar a plataforma com você.
{% endalert %}

## Usuários e segmentos

Os usuários são seus clientes - as pessoas que recebem as mensagens que você envia usando o Braze. Todos os dados que você coleta sobre um usuário e ingere no Braze são armazenados no perfil do usuário, como dados demográficos, informações pessoais, preferências e comportamentos. Essas informações alimentam suas mensagens e é assim que você pode personalizá-las para o usuário certo.

\![]({% image_buster /assets/img/getting_started/user_profile.png %})

Os segmentos dividem sua base de clientes em grupos menores, que podem ser direcionados com mensagens específicas. Você pode usar diferentes variáveis para criar segmentos, desde características como gênero, local e idade até comportamentos como padrões de interação com campanhas anteriores ou em que ponto da jornada do cliente eles se encontram.

Os segmentos são dinâmicos - os usuários podem entrar e sair dos segmentos em tempo real com base no comportamento e na posição em que se encontram em relação à sua marca. Isso garante que seus clientes recebam as mensagens mais relevantes para eles em um determinado momento. Você pode criar quantos segmentos forem necessários para fins de segmentação e envio de mensagens.

\![]({% image_buster /assets/img/getting_started/segment.png %})

Para saber mais, confira: [Primeiros passos: Usuários e segmentos]({{site.baseurl}}/user_guide/getting_started/users_segments/).

## Campanhas e telas

Campanhas e Canvases são a forma de enviar mensagens aos seus usuários.

As campanhas são melhores para mensagens únicas enviadas a um segmento de público específico em vários canais. Você pode aproveitar qualquer um dos nossos canais de mensagens compatíveis em sua campanha (e-mail, push, mensagens no aplicativo, SMS e muito mais).

Canvases são fluxos de trabalho de campanha avançados que permitem automatizar e orquestrar jornadas personalizadas de clientes em vários canais. Em um Canvas, você pode configurar a lógica de ramificação, atrasos, pontos de decisão e eventos de conversão para orientar os clientes por meio de uma série de interações. As telas ajudam a garantir uma comunicação consistente e contínua em diferentes pontos de contato, aumentando as chances de envolvimento e conversão do cliente. 

Para saber mais, confira: [Primeiros passos: Campaigns and Canvases]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

## Espaços de trabalho

Os espaços de trabalho agrupam seus dados - usuários, segmentos, campanhas e Canvases - em um único local. As informações não são compartilhadas entre os espaços de trabalho, portanto, tenha isso em mente ao adicionar sites e aplicativos aos seus espaços de trabalho. Como prática recomendada, sugerimos colocar apenas versões diferentes do mesmo aplicativo ou de aplicativos muito semelhantes em um único espaço de trabalho.

Exemplos de usos para espaços de trabalho incluem:

- Diferentes linhas de produtos ou aplicativos
- Públicos diferentes (como motoristas de entrega e clientes)
- Negócios separados
- Ambiente de teste

Para saber mais, confira: [Primeiros passos: Espaços de trabalho]({{site.baseurl}}/user_guide/getting_started/workspaces/).

## Integração do Braze

O Braze foi projetado para entrar em operação de forma rápida e fácil. Nosso tempo médio de obtenção de valor é de seis semanas em nossa base de clientes de centenas de marcas.

\![]({% image_buster /assets/img/getting_started/timetovalue.png %})

Esta é a estrutura do Braze para estimar a duração de sua integração com base em quatro componentes nos quais você pode trabalhar em paralelo. O intervalo típico é de 30 a 180 dias, com a maioria das contas concluindo sua integração em 45 a 60 dias.

- **Nível de complexidade da migração da campanha:** O tempo necessário para migrar as campanhas depende de quantas você tem, de quão personalizadas elas são e de seus recursos. Se você tiver menos de dez campanhas para migrar, isso levará menos de 60 dias. Mas se você tiver mais de 100 campanhas, isso será mais complicado. Se apenas uma pessoa estiver migrando 100 campanhas, isso é diferente de 10 pessoas migrando 100.

{% alert tip %}
Precisa de ajuda com sua migração? Nossos [parceiros certificados Braze](https://www.braze.com/partners/solutions-partners) podem ajudar!
{% endalert %}

- **Volume de e-mail:** Para enviar e-mails, você precisará aquecer seus IPs. [O aquecimento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) é o processo de criar reputação de remetente com seus endereços IP recém-atribuídos. Se você enviar menos de 2 a 3 milhões de e-mails por dia, o aquecimento do seu IP deverá levar 30 dias ou menos. Tenha em mente seu pico de envio. Se você normalmente envia 2 milhões de e-mails por dia, mas planeja enviar 7 milhões em um período sazonal, esse "pico" de envio é o que você deve esperar. Os remetentes de grande volume podem usar vários IPs para acelerar o processo de aquecimento.
- **Complexidade organizacional:** Nosso processo de integração pode se adaptar às necessidades de sua empresa. Quer você seja uma única unidade de negócios, tenha um Centro de Excelência, várias unidades independentes ou use agências para aumentar suas equipes, a Braze tem experiência em trabalhar em todos os cenários.
- **Sofisticação da infraestrutura de dados:** Se você estiver implementando apenas o Braze SDK ou já tiver uma plataforma de dados do cliente (CDP), é possível ter tudo configurado em apenas 30 dias. O uso de uma CDP moderna pode acelerar o processo. No entanto, se você tiver muitos sistemas, ferramentas ou bancos de dados de back-end para conectar ao Braze, poderá levar mais tempo e precisar de mais recursos dedicados para concluir a configuração.

Para saber mais, confira: [Primeiros passos: Visão geral da integração]({{site.baseurl}}/user_guide/getting_started/integration/).

