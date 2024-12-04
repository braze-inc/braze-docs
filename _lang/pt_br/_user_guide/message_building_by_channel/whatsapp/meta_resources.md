---
nav_title: Recursos Meta
article_title: Recursos Meta
page_order: 81
description: "Este artigo apresenta documentação, informações e recursos úteis da Meta para melhorar sua compreensão da integração com o WhatsApp."
page_type: reference
channel:
  - WhatsApp

---

# Recursos meta

## Meta documentação

Consulte a seguinte documentação da Meta para saber mais sobre nomes de exibição, números de telefone e muito mais.

- [Orientação do nome de exibição](https://www.facebook.com/business/help/757569725593362) 
- [Ativação do Meta Insight](https://www.facebook.com/business/help/218116047387456)
- [Requisitos de números de telefones](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Limites de envio de mensagens](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Classificação de qualidade](https://www.facebook.com/business/help/896873687365001)

## Atualizações de produtos do WhatsApp

### Maio de 2024: Lançamento da API de Nuvem na Turquia
*Última atualização em maio de 2024*

A Meta agora fornece às empresas com API de Nuvem acesso à Turquia para envio de mensagens comerciais. Anteriormente, o WhatsApp Cloud API estava disponível para uso das empresas na Turquia, mas os usuários do WhatsApp com números turcos não podiam enviar ou receber mensagens enviadas via Cloud API. 

A Meta sempre deixa claro para os usuários quando eles estão conversando com uma empresa hospedada pela Meta, e todos os usuários são obrigados a aceitar os Termos de Serviço do WhatsApp e a Política de Privacidade relevantes para prosseguir com o envio de mensagens comerciais. A atualização dos Termos de Serviço e da Política de Privacidade de 2021 na Turquia foi pausada, mas agora está sendo implementada. Isso não altera o compromisso da Meta com a privacidade - as conversas pessoais continuam protegidas por criptografia de ponta a ponta, o que significa que somente você e o destinatário pretendido poderão vê-las. A atualização ativa os usuários turcos para acessar recursos opcionais do WhatsApp Business, se assim desejarem, e oferece mais transparência sobre o funcionamento do WhatsApp.  
 
Os negócios da API na nuvem agora podem iniciar conversas com usuários do WhatsApp com números turcos, que agora retornarão um webhook como uma conversa "enviada", em vez do código de erro 131026 de hoje.

Para que uma mensagem comercial seja "entregue" ou "lida", é necessário que o usuário aceite os termos do WhatsApp. Uma empresa não será cobrada a menos que a mensagem seja entregue.

Os usuários que receberem ou tentarem enviar uma mensagem para uma empresa da Cloud API receberão uma notificação no app sobre a atualização dos termos, que esclarece que eles não podem enviar mensagens para uma empresa da Cloud API até que tenham aceitado a atualização do WhatsApp. Além disso, os usuários que registrarem ou registrarem novamente o app em seus telefones serão solicitados a aceitar a atualização do WhatsApp.

Ao aceitar a atualização, o usuário verá o aviso de mensagem do sistema da API de Nuvem ao conversar com uma empresa da API de Nuvem.

### Maio de 2024: Limites de mensagens de modelo de marketing por usuário
*Última atualização em maio de 2024*

A Meta está implementando novas abordagens para manter experiências de usuário de alta qualidade e maximizar o engajamento com mensagens de modelos de marketing na plataforma WhatsApp. A partir de 23 de maio de 2024, eles limitarão o número de mensagens de modelo de marketing que cada usuário individual pode receber de todas as empresas com as quais interage durante um determinado período de tempo, começando com um pequeno número de conversas que têm menos probabilidade de serem lidas. Note que o limite é determinado com base no número de mensagens de modelo de marketing que a pessoa já recebeu de qualquer empresa, e não está relacionado especificamente à sua marca. No entanto, isso pode afetar a entregabilidade de suas mensagens de modelo de marketing.

O limite se aplica apenas a mensagens de modelo de marketing que normalmente abririam uma nova conversa de marketing. Se uma conversa de marketing já estiver aberta entre sua marca e um usuário do WhatsApp, as mensagens de modelo de marketing enviadas para o usuário não serão afetadas.

Se uma mensagem de modelo de marketing não for entregue a um determinado usuário devido ao limite, a API de Nuvem retornará o código de erro 131026. Observe, no entanto, que esses códigos de erro abrangem uma ampla gama de problemas que podem resultar na não entrega de uma mensagem e, por motivos de privacidade, a Meta não divulgará se, de fato, a mensagem não foi entregue devido ao limite. Consulte o [documento de solução de problemas](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) da API de Nuvem para obter descrições dos motivos de não entrega e o que você pode fazer para determinar a causa subjacente.

Se você receber um desses códigos de erro e suspeitar que ele se deve ao limite, evite reenviar imediatamente a mensagem do modelo, pois isso só resultará em outra resposta de erro. 

Para saber mais sobre essa atualização de entregabilidade, incluindo detalhes sobre o monitoramento de sua entregabilidade e outras práticas recomendadas para o envio de mensagens de marketing no WhatsApp, consulte nossa [publicação](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog) recente [no blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Abril de 2024: Ritmo de modelo para modelos de utilitários
*Última atualização em abril de 2024*

No ano passado, o WhatsApp introduziu o ritmo de modelos para mensagens de marketing como uma nova maneira de ajudar as empresas a melhorar o engajamento com seus modelos e criar experiências valiosas para os usuários. A partir de 30 de abril, eles estão expandindo o ritmo do modelo para mensagens de utilidade pública. Se um modelo de utilitário para uma conta for pausado devido ao feedback do usuário, ele acompanhará os novos modelos de utilitário que forem criados nos próximos sete dias.

### Abril de 2024: As taxas de leitura afetarão o índice de qualidade dos modelos de marketing 
*Última atualização em março de 2024*

O WhatsApp está testando novas abordagens, começando com os consumidores na Índia, para criar experiências mais valiosas e maximizar o engajamento com as conversas de marketing dos profissionais de marketing. Isso pode incluir a limitação do número de conversas de marketing que uma pessoa recebe de qualquer empresa em um determinado período, começando com um pequeno número de conversas que têm menos probabilidade de serem lidas. O Braze receberá um código de erro se uma mensagem não for entregue.

O WhatsApp começará a considerar as taxas de leitura como parte de nossa classificação de qualidade para modelos de marketing, juntamente com as métricas tradicionais, como bloqueios e relatórios. O WhatsApp pode pausar temporariamente as campanhas de mensagens de marketing com baixas taxas de leitura, dando às empresas tempo para iterar nos modelos com o menor engajamento antes de aumentar o volume a partir de 1º de abril de 2024. 

### Fevereiro de 2024: Experimentação de conversas de marketing
*Última atualização em fevereiro de 2024*

A partir de 6 de fevereiro de 2024, o WhatsApp está testando novas abordagens, começando com os consumidores na Índia, para criar experiências mais valiosas e maximizar o engajamento dos clientes com as conversas de marketing da sua marca. Isso pode incluir a limitação do número de conversas de marketing que um usuário recebe da sua marca em um determinado período, começando com um pequeno número de conversas que têm menos probabilidade de serem lidas.

### Outubro de 2023: Pacote de modelos 
*Última atualização em outubro de 2023*

A partir de 12 de outubro de 2023, o WhatsApp está introduzindo um conceito chamado "ritmo do modelo" para mensagens de marketing. Em vez de enviar a mensagem para todo o público da campanha simultaneamente, o "template pacing" inicialmente envia a mensagem para um subconjunto menor de usuários para obter feedback em tempo real dos destinatários da campanha antes de enviar as mensagens restantes. 

O "limite de ritmo" (o subconjunto inicial de mensagens enviadas) é variável, dependendo do modelo. Após o envio inicial, o WhatsApp manterá as mensagens restantes por um período máximo de 30 minutos. Durante esse período de espera, eles avaliam a qualidade do modelo com base no feedback dos clientes. Se o feedback for positivo, indicativo de um modelo de alta qualidade, eles enviam as mensagens restantes. Se o feedback for negativo, eles descartam as mensagens restantes não entregues, evitando mais feedbacks negativos de uma parcela maior de seus clientes e ajudando a evitar possíveis problemas de aplicação da qualidade (como impactos na classificação da qualidade do número de telefone). 

Observe que o WhatsApp usa o mesmo sistema para avaliar a qualidade do modelo no ritmo do modelo e na pausa do modelo. Portanto, as mensagens não entregues durante o ritmo do modelo (devido a modelos de baixa qualidade) são as mesmas que teriam sido pausadas em uma escala maior. 

Em última análise, essa atualização oferece um ciclo de feedback mais rápido (30 minutos em vez de horas ou dias com a pausa do modelo), para que você possa ajustar seus modelos e proporcionar uma melhor experiência ao cliente.

**Se tiver outras dúvidas sobre essa atualização, entre em contato com o representante de parceiros da Meta.**

### Junho de 2023: Experimentação de envio de mensagens 
*Última atualização em junho de 2023*

A partir de 14 de junho de 2023, a Meta está introduzindo novas práticas de experimentação na plataforma WhatsApp para avaliar como as mensagens de marketing afetam a experiência e o engajamento do consumidor. Essa experiência pode afetar suas mensagens de marketing enviadas na API do WhatsApp Business com o Braze.

A Meta pretende continuar esse experimento na plataforma WhatsApp. Para saber mais, consulte a [a documentação da Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**A experimentação do WhatsApp afeta apenas as mensagens de marketing.** Esse experimento tem o potencial de impactar a entrega de mensagens de modelos de marketing. Os modelos de utilidade e autenticação continuarão a ser fornecidos sem nenhum impacto na experimentação.

No experimento, a Meta escolhe aleatoriamente cerca de 1% dos consumidores do WhatsApp como participantes. Se for escolhido, a Meta não enviará modelos de mensagens de marketing a esses consumidores, a menos que uma das opções a seguir seja verdadeira:

- Se um consumidor tiver respondido a você nas últimas 24 horas;
- Se uma conversa de marketing existente estiver aberta; ou
- Se um anúncio do WhatsApp foi clicado pelo consumidor nas últimas 72 horas.

## Perguntas frequentes {#faq}

### Como saberei se minha mensagem de marketing foi afetada pelo experimento do Meta?

Se uma mensagem não for entregue devido ao experimento, um código de erro específico será exibido no Log de atividade e no Currents. A mensagem também será contada como uma falha e incorporada às suas métricas de falhas do WhatsApp em todos os relatórios do dashboard do Braze. Você não será cobrado por essas mensagens.

Esse código de erro 130472 indicará "O número do usuário faz parte de um experimento". Consulte [a documentação da Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) para saber mais sobre os códigos de erro da API do WhatsApp Cloud.

### Posso recusar a participação no experimento da Meta?

Não, a Meta não permite recusas no experimento. Todos os usuários e provedores de API do WhatsApp Business estão sujeitos a este experimento da Meta.

### Posso tentar reenviar um modelo mais tarde?

Não há um tempo fixo para esse experimento. Portanto, um consumidor pode continuar sujeito ao experimento.

### O que posso fazer se minhas mensagens de marketing não forem entregues devido à experiência da Meta?

Recomendamos o uso de outros canais do Braze, como e-mail, SMS, notificações por push ou mensagens no app, para enviar uma mensagem com conteúdo semelhante aos usuários pretendidos.
