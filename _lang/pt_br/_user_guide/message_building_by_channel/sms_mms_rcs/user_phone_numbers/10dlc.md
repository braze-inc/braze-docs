---
nav_title: "A2P 10DLC"
article_title: A2P 10DLC
page_order: 2.9
description: "Este artigo aborda o A2P 10DLC, por que o registro 10DLC é necessário para os clientes de código longo dos EUA, informações úteis sobre custos e rendimento e como começar a fazer o registro."
page_type: reference
channel:
  - SMS
  
---

# Códigos longos de 10 dígitos de aplicativo para pessoa

> A2P 10DLC refere-se a um sistema nos Estados Unidos que permite que as empresas enviem mensagens do tipo aplicativo para pessoa (A2P) por meio de um número de telefone padrão de código longo de 10 dígitos (10DLC). Esses códigos longos registrados têm maior taxa de transferência, melhor entregabilidade e melhor conformidade do que o código longo padrão.

{% alert important %}
Todos os clientes que atualmente têm e/ou usam códigos longos dos EUA para enviar a clientes dos EUA devem registrar seus códigos longos para o 10DLC; aqueles que não o fizerem sofrerão filtragem pesada de todas as mensagens. Esse processo de inscrição leva de 4 a 6 semanas.
{% endalert %}

## Por que é necessário

O serviço 10DLC foi criado para facilitar especificamente o envio de mensagens A2P usando códigos longos. Historicamente, os códigos longos eram destinados ao envio de mensagens pessoa a pessoa (P2P), mas, quando usados por motivos de marketing, causavam restrições às empresas devido à taxa de transferência limitada e ao aumento da filtragem. 

O 10DLC ajuda a aliviar esses problemas, oferecendo: 
- **Maior rendimento**: Os números 10DLC suportam um volume maior de mensagens do que os códigos longos regulares.
- **Melhor entregabilidade**: Os números 10DLC são designados para o tráfego A2P, portanto, as mensagens enviadas com esses números têm maior probabilidade de chegar ao destinatário e são menos propensas a serem filtradas ou rejeitadas pela operadora do que as mensagens enviadas por meio de códigos longos locais regulares. 
- **Conformidade aprimorada**: O uso de um código longo local para envio de mensagens de texto comerciais é contra as diretrizes [da CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Os números 10DLC foram designados para envio de mensagens em massa e permitem que as marcas cumpram as regulamentações do setor sem depender de códigos curtos.
- **Econômico**: O 10DLC é uma ótima opção para empresas que desejam começar a enviar SMS ou enviar SMS em pequenos volumes. Para marcas que enviam grandes volumes de mensagens, acima de 100.000 mensagens por dia, recomendamos o uso de um código curto. 

Desde 2019, as operadoras começaram a adotar o 10DLC para envio de mensagens comerciais, com a Verizon e a AT&T atualmente oferecendo suporte ao 10DLC, e esperamos que todas as principais operadoras o sigam em breve. Embora isso possa causar inconvenientes a curto prazo, a longo prazo, os clientes desfrutarão de melhores taxas de entregabilidade e, ao mesmo tempo, protegerão seus consumidores de mensagens indesejadas. 

## O que você precisa saber

### Acesso

O registro de códigos longos com o A2P 10DLC levará de 4 a 6 semanas.

### Custos 

O registro no A2P 10DLC pode incluir vários tipos de taxas:

| Tipo de taxa | Descrição |
| -------- | ---------- |
| Taxas de registro | Taxas nominais aplicadas ao registrar sua marca e caso de uso em todas as principais redes dos EUA. |
| Taxas de verificação secundária | As marcas podem recorrer de seu [Brand Trust Score](#trust-score) e solicitar um processo de verificação secundário para melhorar seu rendimento geral; há uma taxa associada a esse processo. |
| Taxas da operadora | Taxas cobradas pelas operadoras por mensagens SMS e MMS de saída enviadas aos usuários após o registro do 10DLC. A partir de 1º de outubro de 2021, as taxas da operadora serão mais altas para o tráfego não registrado (códigos longos padrão) do que para o tráfego registrado (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Acesse o artigo do Twilio 10DLC para conferir as [estimativas de taxas](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) atualizadas.

### Taxa de transferência

A taxa de transferência de mensagens para seu 10DLC depende de vários fatores, incluindo a pontuação de confiança da marca, os limites diários de mensagens e seus casos de uso de envio de mensagens.

#### Índice de confiança na marca {#trust-score}

O The Campaign Registry (TCR) é uma agência terceirizada que usa um algoritmo de reputação para analisar critérios específicos relacionados à sua empresa e atribuir uma pontuação de confiança que determina o envio de mensagens para cada marca. Essa pontuação de confiança será atribuída quando um cliente se registrar para o envio de mensagens do US 10DLC. Quanto maior for a pontuação de confiança, melhor será a experiência de mensagens por segundo (MPS). 

|     | Índice de confiança | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Alta | 75-100 | 75 MPS | 75 MPS | 75 MPS |
| Média | 50-74 | 40 MPS | 40 MPS | 40 MPS |
| Baixa | 1-49 | 4 MPS | 4 MPS | 4 MPS | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
As empresas listadas no Índice Russel 3000 receberão um alto rendimento e uma pontuação de confiança na marca após o registro e a análise do 10DLC.
{% endalert %} 

#### Limites diários de mensagens

Os limites diários variam de 2.000 a 200.000 mensagens, dependendo da pontuação de confiança de sua marca, e se aplicam a todos os códigos longos. Embora as altas pontuações de confiança da marca sejam acompanhadas de uma taxa de transferência de 60 mensagens por segundo, quaisquer limites diários de mensagens definidos pela operadora ainda serão aplicados. Isso significa que os códigos curtos seriam uma opção melhor se o pico diário de mensagens de uma marca for maior do que o limite diário imposto. 

#### Casos de uso de envio de mensagens

A taxa de transferência também é afetada pelo tipo de caso de uso de envio de mensagens que você escolher. A maioria dos clientes se enquadrará no caso de uso de marketing padrão ou de marketing misto. Outros casos de uso menos comuns serão suscetíveis a valores de taxa de transferência diferentes.

Dependendo do seu caso de uso, a pontuação de confiança necessária para atingir a taxa de transferência máxima varia. As tabelas a seguir listam casos de uso padrão e intervalos de pontuação de confiança de casos de uso comuns. Para casos de uso especiais, como serviços de emergência ou caridade, consulte os [documentos do Twilio](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Casos de uso padrão | Descrição |
| ------------------ | ----------- |
| Marketing | Conteúdo promocional, como vendas e ofertas por tempo limitado. |
| Misturado | Campanha que abrange vários casos de uso, como o Atendimento ao Cliente. | 
| Ensino superior | Campanhas para instituições de ensino superior. |
| Pesquisa de opinião e votação | Pesquisas e votações não políticas, como pesquisas com clientes. |
| PSA | PSAs para aumentar a conscientização sobre um determinado tópico. |
| Atendimento ao cliente | Suporte, gerenciamento de contas e outras interações com o cliente. |
| Notificações de entrega | Status das mensagens de entrega. |
| Notificações de conta | Notificações sobre o status de uma conta. |
| 2FA | Qualquer autenticação de verificação de conta, como OTP. | 
| Alertas de segurança | Notificação de um sistema comprometido. |
| Alertas de fraude | Envio de mensagens sobre atividades potencialmente fraudulentas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Caso de uso declarado %}
Um caso de uso declarado significa que você escolheu um caso de uso específico não relacionado a marketing (por exemplo, 2FA ou Notificações de conta).

| Índice de confiança | Taxa de transferência total para as principais redes dos EUA | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Caso de Uso de Marketing Misturado %}

Casos de uso de marketing misto podem ser registrados para clientes que desejam enviar mensagens para múltiplos casos de uso a partir do mesmo conjunto de números ou para marketing.

| Índice de confiança | Taxa de transferência total para as principais redes dos EUA | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

Acesse o artigo do Twilio 10DLC para conferir as [estimativas de rendimento](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) atualizadas.

## Próximas etapas

Os clientes que ainda não se registraram no 10DLC devem trabalhar com seu gerente de sucesso do cliente para registrar seus códigos longos. **Se os clientes não registrarem seus códigos longos, a partir de 1º de outubro de 2021, qualquer remetente A2P que use códigos longos sofrerá uma filtragem pesada de todas as mensagens.** Entre em contato com o gerente de sucesso do cliente para iniciar o registro no 10DLC. 
