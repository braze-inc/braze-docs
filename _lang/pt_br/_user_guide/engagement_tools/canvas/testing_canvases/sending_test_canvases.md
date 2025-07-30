---
nav_title: Enviar canvas de teste
article_title: Enviar canvas de teste
page_order: 1
description: "Este artigo de referência aborda como testar um Canva antes do lançamento e as práticas recomendadas."
page_type: reference
tool: Canvas
---

# Envio de telas de teste

> Depois de [criar seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), há várias verificações que podem ser realizadas antes do lançamento, dependendo de detalhes como o tamanho do público ou o número de filtros de segmentação.

Quando possível, a Braze recomenda testar um canva antes de lançá-lo. Normalmente, esse teste será realizado em seu ambiente Braze. Testar o Canvas pode envolver duplicá-lo, levar os usuários teste ao longo da jornada do usuário e verificar se o comportamento do usuário está alinhado com o que foi delineado no Canvas.

## Etapa 1: Crie seu plano de teste

Criar um plano de teste é essencial antes de começar a testar seu Canva. Um plano de teste pode ajudar a identificar e rastrear áreas específicas de sua jornada do Canva.

Ao criar seu plano de testes, considere as seguintes questões:
- Foi criado pelo menos um usuário para cada ramo e jornada do Canva?
- Algum segmento está sendo usado em seu Canva? 
	- Se forem usados segmentos, pode haver pré-requisitos para que um usuário se enquadre no Canva antes de ser elegível para uma jornada do usuário.
- As mensagens no Canvas de teste têm algum Liquid nos títulos das mensagens que levam à ID do usuário ou ao endereço de e-mail para garantir que sejam fáceis de identificar a mensagem e o usuário para fins de teste?

## Etapa 2: Identifique os usuários de teste

Em seguida, identifique um conjunto de usuários teste que passarão pelas etapas do Canva sem realmente enviar mensagens aos usuários pretendidos. Os usuários de teste podem ser endereços de e-mail existentes que não são usados para serviços reais em seu dashboard do Braze ou novos endereços de e-mail que são usados exclusivamente para fins de teste. 

## Etapa 3: Configure seu Canvas

Em seguida, é hora de testar seu canva! Para manter as informações do Canvas original e do Canvas de teste organizadas, crie uma duplicata do seu Canvas para fins de teste.

Há duas maneiras de testar seu Canva. 

- **Método 1:** No Canvas duplicado, edite a parte **Entry Audience (Público de entrada)** do construtor do Canvas para que apenas os usuários de teste sejam elegíveis para o Canvas. Também é possível inserir seu próprio endereço de e-mail como usuário teste, adicionando o filtro de teste **Endereço de e-mail**. No exemplo abaixo, limitamos o Canva a dois usuários teste que usaram o app pela primeira vez há menos de três dias.

![Um canva com um público de "Usou esses aplicativos pela primeira vez há menos de 3 dias" e os endereços de e-mail de dois usuários de teste.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Método 2:** [Faça uma prévia das jornadas do usuário]({{site.baseurl}}/preview_user_paths/) selecionando o botão **Test Canvas** no rodapé do construtor do Canvas.

## Etapa 4: Inicie seu teste

Inicie o Canva de teste para permitir que os usuários comecem a entrar. Conclua os comportamentos do usuário em seu aplicativo que enviariam os usuários pela respectiva jornada do Canva.

Verifique se os usuários teste estão recebendo as mensagens pretendidas nas etapas do Canva. Note que os usuários de teste podem não receber uma mensagem por motivos que não se limitam a

- Não elegível para o Grupo de Controle Global
- Limitações do limite de frequência
- Associação de segmento incompatível
- Envio de mensagens abortadas
- Tokens por push associados a diferentes usuários

Continue a iterar os testes do Canvas para garantir que seu Canvas tenha a performance desejada.

## Dicas gerais

### Identifique suas etapas do Canva

Em alguns casos, um usuário pode potencialmente receber várias mensagens ao passar por um Canva. Se a postergação entre as etapas tiver sido reduzida significativamente para testes, talvez nem sempre fique claro qual mensagem está sendo disparada durante o teste. Garantir que as mensagens de teste incluam o nome da etapa ou o ID do usuário (usando Liquid) facilitará a identificação e a confirmação de que a mensagem correta foi enviada aos usuários corretos.

### Criar um grupo interno

Em vez de criar usuários de teste individuais, é possível criar um [Grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que é um grupo interno cuja finalidade é revisar o conteúdo da sua mensagem. Isso inclui um grupo de usuários que receberão mensagens de teste de campanhas e Canvas. Em seguida, você pode adicionar esse grupo de teste no campo **Add Content Test Groups (Adicionar grupos de teste de conteúdo** ) em **Test Recipients (Destinatários de teste**).

### Reduzir as postergações

Para ajudar a executar testes com mais eficiência, sugerimos reduzir os envios de mensagens para minutos ou segundos para fins de teste, para que você possa visualizá-las em tempo hábil. Por exemplo, aguarde pelo menos 2 a 3 minutos entre os testes para poder isolar ações específicas para jornadas específicas do canva.

### Aproveite os blocos de conteúdo

Se algum conteúdo for repetido em sua estrutura de teste (por exemplo, um Liquid complexo para filtrar usuários em diferentes etapas do Canva), tente salvar esse conteúdo repetido como um [bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks). Agora, você poderá incluir o bloco de conteúdo em todas as etapas individuais do Canva.

### Use o Postman e o endoint Rastrear usuário

Você pode executar testes com o Postman e a [Braze Postman Collection]({{site.baseurl}}/api/postman_collection/). Use o [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar e rastrear eventos personalizados e compras para seus vários usuários teste.

Note que o envio de dados para a API de rastreamento de usuários só pode ser feito com uma ID externa. Portanto, os usuários de teste podem precisar ser adicionados como usuários de teste em um grupo interno no dashboard do Braze para que erros específicos possam ser investigados com mais detalhes. 

#### Teste de várias ramificações

Quando estiver testando um Canva com várias ramificações que direcionam os usuários com base em diferentes atribuições e eventos, siga este plano de teste:

1. Para cada ramo, identifique as atribuições e os eventos que o usuário deve ter para ser incluído na jornada do Canva.
2. Crie-os em uma carga útil JSON a ser postada usando o endpoint `/users/track`.

