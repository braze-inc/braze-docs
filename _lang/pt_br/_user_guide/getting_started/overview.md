---
nav_title: Visão geral do Braze
article_title: "Primeiros passos: Visão geral do Braze"
page_order: 1
page_type: reference
description: "Familiarize-se com os principais conceitos que você precisará conhecer ao trabalhar no Braze."

---

# Primeiros passos: Visão geral do Braze

Que bom ter você na Braze! Esta coleção de artigos o ajudará a começar a usar nossa plataforma e lhe apresentará os principais termos, recursos e funcionalidades do Braze. Esta página apresenta os principais conceitos que você precisará conhecer ao trabalhar no Braze.

{% alert tip %}
É altamente recomendável conferir nosso curso gratuito [Braze Foundations for Everyone](https://learning.braze.com/page/braze-foundations-for-everyone) juntamente com esses artigos. Não é necessário nenhum login ou conta especial para este curso. Se você é um desenvolvedor e está procurando um resumo técnico do Braze, dê uma olhada também em [Getting Started for Developers]({{site.baseurl}}/developer_guide/platform_wide/getting_started/platform_overview).
{% endalert %}

Nas seções de Introdução, nos concentramos nas implementações comuns da Braze. No entanto, a Braze é incrivelmente flexível e pode ser personalizada para agregar valor à sua organização de várias maneiras. Para garantir a clareza e a brevidade, fornecemos uma visão geral descritiva da configuração padrão em vez de oferecer instruções rígidas. Reconhecemos que cada organização tem suas necessidades distintas, e o Braze foi criado para atender a uma gama diversificada de opções de personalização que podem ser adaptadas às suas necessidades específicas.

Vamos explorar juntos o poder da Braze.

## Como o Braze funciona

A Braze é uma plataforma de engajamento com clientes que ajuda marcas de todos os tamanhos a criar campanhas personalizadas e direcionadas em vários canais. O Braze lhe dá a capacidade de ouvir seus clientes, entender o que o comportamento deles está sinalizando e, em seguida, agir enviando aos clientes a mensagem certa, por meio do canal certo, no momento certo.

{% alert tip %}
Certifique-se de [adicionar seus colegas ao Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users) para que eles possam explorar a plataforma com você.
{% endalert %}

## Usuários e segmentos

Os usuários são seus clientes - as pessoas que recebem as mensagens que você envia usando o Braze. Todos os dados que você coleta sobre um usuário e ingere no Braze são armazenados no perfil do usuário, como dados demográficos, informações pessoais, preferências e comportamentos. Essas informações alimentam o envio de mensagens e é assim que você pode personalizar suas mensagens para o usuário certo.

![][1]

Os segmentos dividem sua base de clientes em grupos menores que podem ser direcionados com envios de mensagens específicos. É possível usar diferentes variáveis para criar segmentos, desde características como gênero, local e idade até comportamentos como padrões de interação com campanhas anteriores ou em que ponto da jornada do cliente eles se encontram.

Os segmentos são dinâmicos - os usuários podem entrar e sair dos segmentos em tempo real com base em seu comportamento e em sua posição em relação à sua marca. Isso garante que seus clientes recebam o envio de mensagens mais relevante para eles em um determinado momento. Você pode criar quantos segmentos forem necessários para fins de direcionamento e envio de mensagens.

![][2]

Para saber mais, confira: [Primeiros passos: Usuários e segmentos]({{site.baseurl}}/user_guide/getting_started/users_segments/).

## Campanhas e canvas

Campanhas e Canvas são a forma de envio de mensagens aos seus usuários.

As campanhas são melhores para mensagens únicas enviadas a um segmento específico de mensagens em vários canais. Você pode aproveitar qualquer um dos nossos canais de envio de mensagens compatíveis em sua campanha (e-mail, push, mensagens no app, SMS e muito mais).

As telas são fluxos de trabalho de campanha avançados que permitem automatizar e orquestrar jornadas personalizadas de clientes em vários canais. Em um Canva, você pode configurar lógica de ramificação, postergações, pontos de decisão e eventos de conversão para orientar os clientes em uma série de interações. As telas ajudam a garantir uma comunicação consistente e contínua em diferentes pontos de contato, aumentando as chances de engajamento e conversão do cliente. 

Para saber mais, confira: [Primeiros passos: Campanhas e telas]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

## Espaços de trabalho

Os espaços de trabalho agrupam seus dados de usuários, segmentos, campanhas e Canvas em um único local. As informações não são compartilhadas entre espaços de trabalho, portanto, tenha isso em mente ao adicionar sites e apps aos seus espaços de trabalho. Como prática recomendada, sugerimos colocar apenas versões diferentes do mesmo app ou de apps muito semelhantes em um único espaço de trabalho.

Exemplos de usos para espaços de trabalho incluem:

- Diferentes linhas de produtos ou apps
- Diferentes públicos (como motoristas de entrega e clientes)
- Negócios separados
- Ambiente de teste

Para saber mais, confira: [Primeiros passos: Espaços de trabalho]({{site.baseurl}}/user_guide/getting_started/workspaces/).

## Integração do Braze

O Braze foi projetado para entrar em operação de forma rápida e fácil. Nosso tempo médio de obtenção de valor é de seis semanas em nossa base de clientes de centenas de marcas.

![][3]

Aqui está a estrutura do Braze para estimar a duração de sua integração com base em quatro componentes nos quais você pode trabalhar em paralelo. O intervalo típico é de 30 a 180 dias, com a maioria das contas concluindo sua integração em 45 a 60 dias.

- **Nível de complexidade da migração da campanha:** O tempo necessário para migrar as campanhas depende de quantas você tem, de quão personalizadas elas são e de seus recursos. Se você tiver menos de dez campanhas para migrar, isso levará menos de 60 dias. Mas se você tiver mais de 100 campanhas, isso será mais complicado. Se apenas uma pessoa estiver migrando 100 campanhas, isso é diferente de 10 pessoas migrando 100.

{% alert tip %}
Precisa de ajuda com sua migração? Nossos [parceiros certificados Braze](https://www.braze.com/partners/solutions-partners) podem ajudar!
{% endalert %}

- **Volume de e-mail:** Para enviar e-mails, você precisará fazer o aquecimento de seus IPs. [O aquecimento de IP]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) é o processo de construção da reputação do remetente com seus endereços IP recém-atribuídos. Se você enviar menos de 2 a 3 milhões de e-mails por dia, o aquecimento de seu IP deverá levar 30 dias ou menos. Tenha em mente seu pico de envio. Se você normalmente envia 2 milhões de e-mails por dia, mas planeja enviar 7 milhões em um período sazonal, esse "pico" de envio é o que deve ser considerado. Os remetentes de alto volume podem usar vários IPs para acelerar o processo de aquecimento.
- **Complexidade organizacional:** Nosso processo de integração pode se adaptar às necessidades de sua empresa. Quer você seja uma única unidade de negócios, tenha um Centro de Excelência, várias unidades independentes ou use agências para aumentar suas equipes, a Braze tem experiência em trabalhar em todos os cenários.
- **Sofisticação da infraestrutura de dados:** Se estiver implementando apenas o SDK da Braze ou já tiver uma plataforma de dados do cliente (CDP), é possível ter tudo configurado em apenas 30 dias. O uso de uma CDP moderna pode acelerar o processo. No entanto, se você tiver muitos sistemas, ferramentas ou bancos de dados de back-end para conectar ao Braze, poderá levar mais tempo e precisar de mais recursos dedicados para concluir a configuração.

Para saber mais, confira: [Primeiros passos: Visão geral da integração]({{site.baseurl}}/user_guide/getting_started/integration/).

[1]: {% image_buster /assets/img/getting_started/user_profile.png %}
[2]: {% image_buster /assets/img/getting_started/segment.png %}
[3]: {% image_buster /assets/img/getting_started/timetovalue.png %}