---
nav_title: Recursos Meta
article_title: Recursos Meta
page_order: 12
description: "Este artigo apresenta documentação, informações e recursos úteis da Meta para melhorar sua compreensão da integração com o WhatsApp."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Recursos Meta

## Documentação da Meta

Consulte a seguinte documentação da Meta para saber mais sobre nomes de exibição, números de telefone e muito mais.

- [Orientação do nome de exibição](https://www.facebook.com/business/help/757569725593362)
- [Ativação do Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Requisitos de números de telefone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Limites de envio de mensagens](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Classificação de qualidade](https://www.facebook.com/business/help/896873687365001)

## Atualizações de produtos do WhatsApp

### Junho de 2026: IDs de usuário com escopo de negócio
*Última atualização em março de 2026*

- A Meta está introduzindo IDs de usuário para substituir o compartilhamento de números de telefone por questões de privacidade
- A Braze está trabalhando em uma solução antes da implementação
- Implementação esperada pela Meta em junho de 2026

### Novembro de 2025: [API de mensagens de marketing para WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (anteriormente Marketing Messages Lite API)
*Última atualização em março de 2026*

- Substitui os limites estáticos da Cloud API por limites dinâmicos baseados em engajamento
- Não disponível na EMEA, Japão ou Coreia do Sul para entrega otimizada
- Mensagens de utilidade/autenticação continuam pela Cloud API automaticamente

### Outubro de 2025: Mudança no processo de aprovação de Conta Comercial Oficial (OBA)
*Última atualização em março de 2026*

- Anteriormente aberto a todos os clientes pelo WhatsApp Manager
- Agora restrito a: governo/grandes anunciantes da Meta, anunciantes diretos ou via um BSP como a Braze (até 5 por semana)
- Novos pré-requisitos: verificação de negócio, verificação em duas etapas, nome de exibição aprovado, notabilidade
- Entre em contato com seu gerente de sucesso do cliente para obter assistência

### Outubro de 2025: Reduções de preços regionais
*Última atualização em março de 2026*

- Tarifas mais baixas de utilidade/autenticação na Argentina, Egito, México, América do Norte
- Tarifas de marketing mais baixas no México (a partir de 1º de outubro de 2025)

### Outubro de 2025: Limites de envio de mensagens mudam de por telefone para por portfólio de negócios
*Última atualização em março de 2026*

- Os limites agora são compartilhados entre todos os números de telefone em um portfólio
- Os portfólios herdam o limite mais alto existente
- Acesso mais rápido a limites mais altos (em até 6 horas)
- Risco: empresas sem um número "ilimitado" podem ver os limites agregados diminuírem

### 1º de julho de 2025: Reformulação de preços
*Última atualização em março de 2026*

- A cobrança por mensagem substituiu a cobrança por conversa
- Mensagens de utilidade enviadas em uma janela de serviço de 24 horas passaram a ser gratuitas
- Tarifas atualizadas de utilidade/autenticação em vários mercados, com novas faixas de volume
- Novas regras sobre categorização incorreta de modelos de utilidade — empresas podem enfrentar rejeição de modelos e restrições de envio

### Abril de 2025: Pausa no envio de mensagens de marketing para números de telefone dos EUA
*Última atualização em agosto de 2025*

A Meta pausará o envio de todas as mensagens de modelo de marketing para usuários do WhatsApp que tenham um número de telefone dos Estados Unidos (um número composto por um código de discagem `+1` e um código de área dos EUA). Não há data programada para o término dessa pausa.

Qualquer tentativa de enviar um modelo para um usuário do WhatsApp com um número de telefone dos EUA resultará no erro `131049`.

### Março de 2025: Restrições por uso indevido de categorias de modelos
*Última atualização em março de 2026*

- A Meta introduziu medidas de fiscalização para empresas que fazem uso indevido da categorização de utilidade/marketing
- Pode resultar em restrições de 7 a 30 dias na criação de modelos e revisões de categorias

### Março de 2025: Limites de mensagens de modelo de marketing por usuário
*Última atualização em agosto de 2025*

A Meta limitará o número de mensagens de modelo de marketing que um usuário pode receber de todas as empresas em um determinado período de tempo, começando com mensagens que têm menos probabilidade de serem lidas.

Uma exceção é que, se uma pessoa responder a uma mensagem de marketing, isso iniciará uma janela de atendimento ao cliente de 24 horas. As mensagens de marketing enviadas dentro dessa janela não contarão para o limite da pessoa.

O limite específico varia de acordo com o usuário, dependendo do seu nível de engajamento. Saiba mais sobre os limites por usuário para mensagens de modelo de marketing no WhatsApp [aqui](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Janeiro de 2025: WhatsApp pausando o envio de mensagens de marketing para usuários dos EUA a partir de 1º de abril
*Última atualização em janeiro de 2025*

O WhatsApp pausará o envio de mensagens de marketing para usuários dos EUA (pessoas com números de telefone dos EUA) a partir de 1º de abril de 2025. [Utilidade, serviço, autenticação](https://developers.facebook.com/docs/whatsapp/pricing/) e [mensagens de resposta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) ainda serão permitidas nos EUA.

O envio de mensagens de marketing (além de todos os outros tipos de mensagens) para todos os outros países ou regiões ainda é permitido e não será afetado.

A Meta nos informou que está fazendo essa atualização para manter a integridade do ecossistema do WhatsApp nos EUA, onde o WhatsApp está crescendo rapidamente, mas ainda em um estágio inicial (por exemplo, mensagens de marketing têm um engajamento menor do que em outras regiões). Eles continuarão a avaliar quando o mercado dos EUA estiver pronto para retomar as mensagens de marketing.

A entrega de mensagens de marketing para números de telefone com códigos de área dos EUA será rejeitada pelo WhatsApp e retornará um código de erro 131049.

### Novembro de 2024: Mudanças na política de aceitação do WhatsApp
*Última atualização em janeiro de 2025*

A Meta recentemente atualizou sua [política de aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Em vez de exigir consentimento específico do canal, as empresas agora podem enviar mensagens aos usuários na plataforma se:

1. A pessoa forneceu seu número de telefone.
2. A pessoa deu aceitação para envio de mensagens gerais, não apenas WhatsApp.

As empresas ainda precisam cumprir todas as leis locais e seguir os requisitos abaixo ao obter a aceitação:

- As empresas devem deixar claro que a pessoa está optando por receber comunicação da empresa
- As empresas devem declarar claramente o nome da empresa da qual a pessoa está optando por receber mensagens
- As empresas devem cumprir a legislação aplicável

Embora o WhatsApp tenha afrouxado sua política, a Braze ainda recomenda coletar a aceitação específica para o canal do WhatsApp a fim de promover a melhor experiência do cliente e taxas de engajamento. Como sempre, consulte sua equipe jurídica para ver o que faz sentido para sua marca.

### Novembro de 2024: Atualizações no limite de modelo de marketing por usuário para pessoas nos EUA, antes da temporada de festas
*Última atualização em dezembro de 2024*

Desde que a Meta implementou o limite de modelo de marketing por usuário, houve melhorias significativas nas taxas de leitura e no sentimento dos usuários.
 
A partir de agora, antes da temporada de festas, as pessoas nos EUA receberão menos novas conversas de marketing. A Meta espera que essa mudança crie públicos mais engajados, o que, em última análise, leva a melhores resultados para os negócios. Isso pode resultar em taxas de entrega mais baixas para o seu negócio se você enviar mensagens de marketing para números de telefone dos EUA, que podem ser monitoradas com o código de erro `131049` por meio do Braze Currents e do registro de atividade de mensagens.

As empresas nos EUA ainda podem enviar mensagens de marketing em outras regiões, e não há impacto nas mensagens de utilidade, autenticação ou serviço, nem nas mensagens de modelo de marketing enviadas dentro de uma janela de conversa iniciada pelo usuário (por exemplo, um anúncio de clique para o WhatsApp, carrossel de produtos ou modelo de cupom enviado como parte de uma conversa).

### Novembro de 2024: WhatsApp expandindo as imposições de qualidade em nível de conta para incluir taxas de leitura
*Última atualização em dezembro de 2024*

O WhatsApp está continuamente investindo em novas maneiras de ajudar as empresas a criar experiências de qualidade para seus clientes, como reduzir comportamentos semelhantes a spam em sua plataforma.

No dia 22 de novembro, o WhatsApp começou a expandir suas medidas de qualidade em nível de conta existentes nas contas comerciais do WhatsApp (WABAs) com taxas de leitura extremamente baixas. Essa mudança será implementada globalmente.

Quando a taxa de leitura de uma conta cai significativamente (por exemplo, a maioria das mensagens enviadas pela conta não são lidas), bloqueios de envio de mensagens serão aplicados à conta. A gravidade do bloqueio aumentará se houver taxas de leitura consistentemente baixas em escala.

Se a taxa de leitura da conta for extremamente baixa, as seguintes ações serão tomadas:

- A conta será bloqueada para o envio de mensagens iniciadas pela empresa. Ela ainda poderá responder a mensagens iniciadas pelos clientes. Este bloqueio inicial é um "bloqueio suave" e pode ser reconhecido selecionando o botão de reconhecimento na Qualidade da Conta para voltar a enviar mensagens.
- Se a taxa de leitura continuar a cair ou permanecer baixa após o bloqueio suave, as empresas podem enfrentar um aumento gradual nas ações de fiscalização (por exemplo, alguns dias de restrições no envio de mensagens).
- As empresas terão que esperar o limite imposto para voltar a enviar mensagens. Se a taxa de leitura continuar baixa após bloqueios suaves repetidos, a conta será eventualmente desativada.

#### Como se manter atualizado sobre esses avisos e imposições

Semelhante à aplicação existente da plataforma, as empresas serão notificadas sobre essas ações e poderão reconhecê-las usando a página de Qualidade da Conta no WhatsApp Business Manager. Confirme se você tem os dados de contato corretos listados no WhatsApp Business Manager para todos os administradores necessários, pois os e-mails de notificação de fiscalização serão enviados com base nessas informações.

Notificações sobre graves violações de spam serão:

- Exibidas no Centro de Notificações do WhatsApp Business Manager
- Exibidas em um banner no WhatsApp Manager
- Enviadas como e-mail para todos os administradores definidos no WhatsApp Business Manager

### Maio de 2024: Lançamento da Cloud API na Turquia
*Última atualização em maio de 2024*

A Meta agora fornece às empresas com Cloud API acesso à Turquia para envio de mensagens comerciais. Anteriormente, o WhatsApp Cloud API estava disponível para uso das empresas na Turquia, mas os usuários do WhatsApp com números turcos não podiam enviar ou receber mensagens enviadas via Cloud API.

A Meta sempre deixa claro para os usuários quando eles estão conversando com uma empresa hospedada pela Meta, e todos os usuários são obrigados a aceitar os Termos de Serviço do WhatsApp e a Política de Privacidade relevantes para prosseguir com o envio de mensagens comerciais. A atualização dos Termos de Serviço e da Política de Privacidade de 2021 na Turquia foi pausada, mas agora está sendo implementada. Isso não altera o compromisso da Meta com a privacidade — as conversas pessoais continuam protegidas por criptografia de ponta a ponta, o que significa que somente você e o destinatário pretendido poderão vê-las. A atualização permite que os usuários turcos acessem recursos opcionais do WhatsApp Business, se assim desejarem, e oferece mais transparência sobre o funcionamento do WhatsApp.  
 
As empresas da Cloud API agora podem iniciar conversas com usuários do WhatsApp com números turcos, que agora retornarão um webhook como uma conversa "enviada", em vez do código de erro 131026 atual.

Para que uma mensagem comercial seja "entregue" ou "lida", é necessário que o usuário aceite os termos do WhatsApp. Uma empresa não será cobrada a menos que a mensagem seja entregue.

Os usuários que receberem ou tentarem enviar uma mensagem para uma empresa da Cloud API receberão uma notificação no app sobre a atualização dos termos, que esclarece que eles não podem enviar mensagens para uma empresa da Cloud API até que tenham aceitado a atualização do WhatsApp. Além disso, os usuários que registrarem ou registrarem novamente o app em seus telefones serão solicitados a aceitar a atualização do WhatsApp.

Ao aceitar a atualização, o usuário verá o aviso de mensagem do sistema da Cloud API ao conversar com uma empresa da Cloud API.

### Maio de 2024: Limites de mensagens de modelo de marketing por usuário
*Última atualização em maio de 2024*

A Meta está implementando novas abordagens para manter experiências de usuário de alta qualidade e maximizar o engajamento com mensagens de modelos de marketing na plataforma WhatsApp. A partir de 23 de maio de 2024, eles limitarão o número de mensagens de modelo de marketing que cada usuário individual pode receber de todas as empresas com as quais interage durante um determinado período de tempo, começando com um pequeno número de conversas que têm menos probabilidade de serem lidas. Note que o limite é determinado com base no número de mensagens de modelo de marketing que a pessoa já recebeu de qualquer empresa, e não está relacionado especificamente à sua marca. No entanto, isso pode afetar a entregabilidade das suas mensagens de modelo de marketing.

O limite se aplica apenas a mensagens de modelo de marketing que normalmente abririam uma nova conversa de marketing. Se uma conversa de marketing já estiver aberta entre sua marca e um usuário do WhatsApp, as mensagens de modelo de marketing enviadas para o usuário não serão afetadas.

Se uma mensagem de modelo de marketing não for entregue a um determinado usuário devido ao limite, a Cloud API retornará o código de erro 131026. Observe, no entanto, que esses códigos de erro abrangem uma ampla gama de problemas que podem resultar na não entrega de uma mensagem e, por motivos de privacidade, a Meta não divulgará se, de fato, a mensagem não foi entregue devido ao limite. Consulte o [documento de solução de problemas](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) da Cloud API para obter descrições dos motivos de não entrega e o que você pode fazer para determinar a causa subjacente.

Se você receber um desses códigos de erro e suspeitar que ele se deve ao limite, evite reenviar imediatamente a mensagem do modelo, pois isso só resultará em outra resposta de erro.

Para saber mais sobre essa atualização de entregabilidade, incluindo detalhes sobre o monitoramento da sua entregabilidade e outras práticas recomendadas para o envio de mensagens de marketing no WhatsApp, consulte nossa recente [publicação no blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Abril de 2024: Ritmo de modelo para modelos de utilidade
*Última atualização em abril de 2024*

No ano passado, o WhatsApp introduziu o ritmo de modelos para mensagens de marketing como uma nova maneira de ajudar as empresas a melhorar o engajamento com seus modelos e criar experiências valiosas para os usuários. A partir de 30 de abril, eles estão expandindo o ritmo de modelo para mensagens de utilidade. Se um modelo de utilidade de uma conta for pausado devido ao feedback do usuário, eles aplicarão o ritmo aos novos modelos de utilidade criados nos próximos sete dias.

### Abril de 2024: As taxas de leitura afetarão a classificação de qualidade dos modelos de marketing
*Última atualização em março de 2024*

O WhatsApp está testando novas abordagens, começando com os consumidores na Índia, para criar experiências mais valiosas e maximizar o engajamento com as conversas de marketing das empresas. Isso pode incluir a limitação do número de conversas de marketing que uma pessoa recebe de qualquer empresa em um determinado período, começando com um pequeno número de conversas que têm menos probabilidade de serem lidas. A Braze receberá um código de erro se uma mensagem não for entregue.

O WhatsApp começará a considerar as taxas de leitura como parte da classificação de qualidade para modelos de marketing, juntamente com as métricas tradicionais, como bloqueios e denúncias. O WhatsApp pode pausar temporariamente as campanhas de mensagens de marketing com baixas taxas de leitura, dando às empresas tempo para iterar nos modelos com o menor engajamento antes de aumentar o volume a partir de 1º de abril de 2024.

### Fevereiro de 2024: Experimentação de conversas de marketing
*Última atualização em fevereiro de 2024*

A partir de 6 de fevereiro de 2024, o WhatsApp está testando novas abordagens, começando com os consumidores na Índia, para criar experiências mais valiosas e maximizar o engajamento dos clientes com as conversas de marketing da sua marca. Isso pode incluir a limitação do número de conversas de marketing que um usuário recebe da sua marca em um determinado período, começando com um pequeno número de conversas que têm menos probabilidade de serem lidas.

### Outubro de 2023: Ritmo de modelos
*Última atualização em outubro de 2023*

A partir de 12 de outubro de 2023, o WhatsApp está introduzindo um conceito chamado "ritmo de modelo" para mensagens de marketing. Em vez de enviar a mensagem para todo o público da campanha simultaneamente, o "ritmo de modelo" inicialmente envia a mensagem para um subconjunto menor de usuários para obter feedback em tempo real dos destinatários da campanha antes de enviar as mensagens restantes.

O "limite de ritmo" (o subconjunto inicial de mensagens enviadas) é variável, dependendo do modelo. Após o envio inicial, o WhatsApp manterá as mensagens restantes por um período máximo de 30 minutos. Durante esse período de espera, eles avaliam a qualidade do modelo com base no feedback dos clientes. Se o feedback for positivo, indicativo de um modelo de alta qualidade, eles enviam as mensagens restantes. Se o feedback for negativo, eles descartam as mensagens restantes não entregues, evitando mais feedbacks negativos de uma parcela maior dos seus clientes e ajudando a evitar possíveis problemas de fiscalização de qualidade (como impactos na classificação da qualidade do número de telefone).

Observe que o WhatsApp usa o mesmo sistema para avaliar a qualidade do modelo no ritmo de modelo e na pausa de modelo. Portanto, as mensagens não entregues durante o ritmo de modelo (devido a modelos de baixa qualidade) são as mesmas que teriam sido pausadas em uma escala maior.

Em última análise, essa atualização oferece um ciclo de feedback mais rápido (30 minutos em vez de horas ou dias com a pausa de modelo), para que você possa ajustar seus modelos e proporcionar uma melhor experiência ao cliente.

**Se tiver mais dúvidas sobre essa atualização, entre em contato com o representante do parceiro Meta.**

### Junho de 2023: Experimentação de envio de mensagens
*Última atualização em junho de 2023*

A partir de 14 de junho de 2023, a Meta está introduzindo novas práticas de experimentação na plataforma WhatsApp para avaliar como as mensagens de marketing afetam a experiência e o engajamento do consumidor. Esse experimento pode afetar suas mensagens de marketing enviadas na API do WhatsApp Business com a Braze.

A Meta pretende continuar esse tipo de experimentação na plataforma WhatsApp. Para saber mais, consulte a [documentação da Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**A experimentação do WhatsApp afeta apenas as mensagens de marketing.** Esse experimento tem o potencial de impactar a entrega de mensagens de modelos de marketing. Os modelos de utilidade e autenticação continuarão a ser entregues sem nenhum impacto da experimentação.

No experimento, a Meta escolhe aleatoriamente cerca de 1% dos consumidores do WhatsApp como participantes. Se for escolhido, a Meta não enviará modelos de mensagens de marketing a esses consumidores, a menos que uma das opções a seguir seja verdadeira:

- Se um consumidor tiver respondido a você nas últimas 24 horas;
- Se uma conversa de marketing existente estiver aberta; ou
- Se um anúncio do WhatsApp foi clicado pelo consumidor nas últimas 72 horas.

## Perguntas frequentes {#faq}

### Como saberei se minha mensagem de marketing foi afetada pelo experimento da Meta?

Se uma mensagem não for entregue devido ao experimento, um código de erro específico será exibido no registro de atividade e no Currents. A mensagem também será contada como uma falha e incorporada às suas métricas de falhas do WhatsApp em todos os relatórios do dashboard da Braze. Você não será cobrado por essas mensagens.

Esse código de erro 130472 indicará "O número do usuário faz parte de um experimento". Consulte a [documentação da Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) para saber mais sobre os códigos de erro da API do WhatsApp Cloud.

### Posso recusar a participação no experimento da Meta?

Não, a Meta não permite recusas no experimento. Todos os usuários e provedores de API do WhatsApp Business estão sujeitos a este experimento da Meta.

### Posso tentar reenviar um modelo mais tarde?

Não há um tempo fixo para esse experimento. Portanto, um consumidor pode continuar sujeito ao experimento.

### O que posso fazer se minhas mensagens de marketing não forem entregues devido ao experimento da Meta?

Recomendamos o uso de outros canais da Braze, como e-mail, SMS, notificações por push ou mensagens no app, para enviar uma mensagem com conteúdo semelhante aos usuários pretendidos.