---
nav_title: Campanhas de usuários ativos
article_title: Campanhas de usuários ativos
page_order: 0.5
page_type: tutorial
description: "Este artigo de instruções descreve os benefícios das campanhas de usuários ativos no dashboard do Braze e as etapas para criar e configurar uma."
tool: 
  - Campaigns

---

# Campanhas de usuários ativos

> Identifique seus usuários ativos para ajudá-lo a fazer campanhas personalizadas e recompensar aqueles que frequentam sua plataforma. 

Entrar em contato com usuários já ativos do seu app pode ser uma ferramenta poderosa para ajudar a criar um grupo dedicado de usuários consistentes do app. Um pouco de reconhecimento personalizado dos seus usuários avançados pode transformá-los em evangelistas do seu app.

Você também pode conferir nosso [curso do Braze Learning](https://learning.braze.com/quick-overview-segment-and-campaign-setup) sobre estratégia de marketing para e-mail e as campanhas de ciclo de vida recomendadas!

## Compreensão dos usuários ativos

O Braze define um "usuário ativo" para um determinado período de tempo como qualquer usuário que tenha uma sessão nesse período.

Se um usuário perder a conectividade, armazenaremos em cache os dados da sessão localmente e faremos upload deles quando o usuário recuperar a conexão de rede. Essas sessões também serão aplicadas à contagem de usuários ativos. Além disso, se o seu app tiver um processo de registro, o Braze contará todos os usuários como ativos - registrados ou não registrados.

Se você definir IDs de usuário para identificar usuários, quando um novo usuário se registrar, ele será contado como um usuário ativo separado. Os usuários que forem atualizados por meio da API também serão contados como usuários ativos no período em que forem atualizados.

## Etapa 1: Identificação de seus principais usuários

Usando a nossa seleção de filtros, crie um segmento de usuários que, na sua opinião, engloba a sua base de usuários mais fiel e consistente. O segmento de amostra a seguir define os principais usuários.

![]({% image_buster /assets/img_archive/define_top_users.png %} "Defina seus principais usuários")

Além disso, não será necessário continuar atualizando esse segmento, pois os usuários que entrarem ou saírem das restrições da campanha serão direcionados ou descartados de forma correspondente.

{% alert note %}
O exemplo anterior segmenta os usuários por uso geral do app. Na maioria dos casos, o conjunto total de filtros necessários para definir seu principal segmento de usuários será amplamente definido pelas especificidades do seu app.
{% endalert %}

## Etapa 2: Entre em contato com seus principais usuários

### Faça com que seus usuários se sintam valorizados

Faça com que seus usuários se sintam apreciados, agradecendo-lhes pela fidelidade e dedicação ao seu app. Dê aos seus usuários mais motivos para continuar voltando ao seu app para incentivar mais atividades. Isso pode assumir a forma de ofertas especiais ou bônus exclusivos para seus principais usuários. 

Recompensas inesperadas podem ser mais eficazes para incentivar ações contínuas dos usuários do que se você as tivesse prometido desde o início!

![Uma campanha na etapa Criação com uma notificação Rich do iOS que diz "Mais uma vez, obrigado por comprar conosco! Para demonstrar nossa gratidão, estamos oferecendo frete grátis em sua próxima compra".]({% image_buster /assets/img/congratulations_push.jpg %})

### Mantenha o controle de seus resultados

Acompanhe as aberturas para garantir que esteja direcionando a coleção adequada de usuários com o tipo de mensagem ideal. Além disso, acompanhe todas as aceitações de push e tenha cuidado para não perder esses usuários cruciais.

