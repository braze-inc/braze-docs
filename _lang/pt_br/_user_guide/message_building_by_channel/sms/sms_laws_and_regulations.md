---
nav_title: "Leis e regulamentos de SMS"
article_title: Leis e regulamentos de SMS
page_order: 3
description: "Este artigo de referência aborda as leis e os regulamentos relacionados a SMS e MMS."
page_type: reference
channel:
  - SMS
  
---

# Leis, regulamentos e prevenção de abuso de SMS

> Como o envio de mensagens SMS é uma das formas mais diretas de alcançar clientes e usuários, acessando diretamente o telefone do usuário, devem existir regulamentações que impeçam as marcas de abusar ou usar excessivamente esse relacionamento, e as multas por violações podem custar milhares de dólares. 

{% alert warning %}
Este artigo não se destina a fornecer, nem pode ser considerado como aconselhamento jurídico. O uso de SMS está sujeito a requisitos legais específicos. Busque orientação jurídica para ter certeza de que você está utilizando serviços de SMS que cumprem todas as leis aplicáveis.
{% endalert %}

## As seis regras para obter a conformidade correta

Em geral, recomendamos que você use seu bom senso ao abordar o envio de SMS. A Braze, assim como nossos parceiros de envio, tem verificações em vigor que impedem a maioria dos abusos de SMS.

Há seis regras que você deve seguir:

1. **Obtenha o consentimento explícito dos usuários antes de enviar-lhes SMS.** Sempre que os usuários fornecem consentimento, é sua responsabilidade registrar, atualizar e manter essas informações em um banco de dados de usuários em conformidade. De acordo com as diretrizes legais básicas, as informações mais importantes que você precisa reter em relação ao consentimento são:
  - A hora e a data em que o usuário deu o consentimento
  - O tipo de envio de mensagens SMS com o qual eles consentiram
  - O número de telefone dos usuários
  - O idioma em que houve a aceitação<br><br>

2. **Comunique claramente os tipos de SMS que você enviará**. Os usuários devem entender quais mensagens devem esperar de sua marca nesse canal e os tipos de informações ou ofertas que receberão. Indique explicitamente o objetivo de suas futuras campanhas, a frequência das mensagens e lembre os usuários de que as taxas de mensagens/dados se aplicam.<br><br>

3. **Mantenha as informações essenciais atualizadas e visíveis**. Certifique-se de que a versão mais atualizada dos Termos e Condições de sua marca e a Política de Privacidade de Marketing por SMS estejam claramente visíveis e facilmente acessíveis em sua página de aceitação de SMS.<br><br>

4. **Envie SMS somente para números de telefone obtidos legalmente e com aceitação**. Como parte do planejamento da migração técnica, certifique-se de que sua equipe entenda o mecanismo para vincular os status de aceitação a cada perfil de usuário em sua plataforma de engajamento com clientes.<br><br>

5. **Garantir a conformidade com a SHAFT nos EUA e em outras regiões relevantes.** O envio de mensagens SMS que contenham linguagem relacionada a sexo, ódio, álcool, armas de fogo e tabaco (SHAFT) é geralmente considerado ilegal nos EUA e em algumas outras regiões.<br><br>

6. **Verifique tudo duas vezes**. Trabalhe com sua equipe jurídica para garantir que seu programa de SMS esteja em total conformidade com todas as regras e regulamentações aplicáveis nas regiões em que sua marca opera.<br><br>

## Recursos

Aqui estão alguns links que você pode precisar consultar ao criar sua campanha de SMS:

- [Princípios de envio de mensagens e práticas recomendadas da CTIA para 2023](https://api.ctia.org/wp-content/uploads/2023/05/230523-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)
- [Guia do Twilio para conformidade com SMS nos EUA](https://www.twilio.com/learn/call-and-text-marketing/guide-to-us-sms-compliance)
- [Conformidade e recursos de SMS da Acoustic nos Estados Unidos](https://help.goacoustic.com/hc/en-us/articles/360043717414-United-States-SMS-compliance-and-resources)

## Considerações sobre conformidade

### Dados e privacidade

A privacidade do cliente é fundamental para um relacionamento significativo e respeitoso. Respeitar a privacidade e as informações de um cliente é apenas mais uma oportunidade de criar um vínculo entre ele e sua marca. Às vezes, o uso de ferramentas de marketing pode colocar os dados e a privacidade em último lugar.

Felizmente para você, a Braze segue as diretrizes de muitos [regulamentos de]({{site.baseurl}}/developer_guide/disclosures/security_qualifications/#security-qualifications "segurança"), incluindo [o GDPR]({{site.baseurl}}/dp-technical-assistance/).

A [CTIA](https://www.ctia.org/) (uma associação comercial que representa o setor de comunicações sem fio nos Estados Unidos) recomenda que você mantenha e exiba de forma visível uma política de privacidade clara e fácil de entender.

### Consentimento

As opções de aceitação, ajuda e exclusão são absolutamente necessárias ao criar campanhas de SMS.

A Lei de Proteção ao Consumidor por Telefone[(TCPAWikipedia](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991 ":Telephone Consumer Protection Act of 1991")) determina que uma empresa deve receber "consentimento expresso por escrito" para o envio de mensagens aos clientes - isso pode ser feito de várias maneiras, inclusive pela internet ou por dispositivos móveis. Você deve ser claro com o cliente sobre como pretende usar o SMS para se comunicar com ele.

Lembre-se de obedecer ao [Registro Nacional de Não Ligar](https://www.donotcall.gov/).

O Braze usa [Grupos de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) para gerenciar grupos de usuários com base em seu nível de consentimento.

### Spam e cadência

Da mesma forma que acontece com o e-mail, seus usuários ou clientes podem sofrer de esgotamento da caixa de entrada. Mas esse é apenas um dos motivos para não enviar mensagens incansáveis a seus clientes. Consulte especificamente a [Seção 5 da Lei da FTC](https://www.federalreserve.gov/boarddocs/supmanual/cch/ftca.pdf "PDF: Lei da Federal Trade Commission Seção 5") para garantir a conformidade (nos U.S.).

Algumas considerações sobre spam estão incorporadas aos recursos de SMS em geral (limites de envio de códigos longos e curtos), bem como aos limites de frequência do Braze. No entanto, você ainda deve considerar as leis de conformidade ao planejar suas campanhas.

### Conteúdo

Essa pode ser uma questão complicada, mas, em caso de dúvida, evite tópicos que envolvam violência, sexo, drogas, tabaco ou outras parafernálias. Tenha cuidado ao enviar mensagens sobre esses tópicos - você ainda pode ser cobrado por mensagens bloqueadas por várias operadoras.

A [CTIA](https://www.ctia.org/) recomenda garantir a conformidade com a SHAFT, que define os seguintes tópicos como geralmente "ilegais" no envio de mensagens nos Estados Unidos:

- Sexo
- Ódio
- Álcool
- Armas de fogo
- Tabaco

Para saber mais sobre esse tópico, consulte os [Princípios e práticas recomendadas de envio de mensagens da CTIA para 2019](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf).

### Programação

Certifique-se de estar em conformidade com a [TCPA](https://en.wikipedia.org/wiki/telephone_consumer_protection_act_of_1991), que determina que você não deve enviar mensagens durante o horário comercial. Consulte o conteúdo do regulamento para saber os horários exatos. No entanto, de qualquer forma, você não deveria enviar mensagens tão tarde – você não quer um alto engajamento?

### Internacional

A maioria dessas práticas recomendadas se aplica às diretrizes estabelecidas nos Estados Unidos da América. Se você estiver alcançando clientes fora das regiões dos U.S., pesquise as práticas recomendadas e as leis dessas regiões. É sempre uma prática recomendada agir de forma a aderir às regulamentações mais rigorosas, que geralmente são aplicadas nos Estados Unidos, no Canadá e em países que fazem parte da União Europeia.
