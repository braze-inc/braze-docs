---
nav_title: Automatizar o registro do Zoom
article_title: Automatizar o registro do Zoom
page_order: 1
page_type: tutorial
description: "Este artigo descreve como automatizar o registro de participantes do Zoom em suas campanhas de mensagens por e-mail, push e no app."
channel: 
  - email
  - push
  - in-app messages

---

# Automatize o registro no Zoom

> Os webinars se tornaram comuns para os clientes da Braze nos últimos anos. Ao hospedar um webinar do Zoom, os usuários devem inserir suas informações em uma landing page do Zoom para inscrever-se. 

Um fluxo de usuário recomendado é descrito abaixo:
1. Agende um webinar no Zoom e gere um `webinarId`.
2. Use a Braze para promover os webinars do Zoom por e-mail, push e canais de envio de mensagens no app. 
3. Inclua um botão de chamada para ação nessas comunicações que adicione automaticamente os usuários ao webinar.

Isso pode ser feito usando as [APIs do Zoom](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) para adicionar automaticamente um usuário a um webinar por meio de um clique em um botão em um e-mail, push ou mensagem no app. Use o seguinte endpoint, substituindo o ID do webinar na solicitação da API. 

POST: `/meetings/{webinarId}/registrants`

Para saber mais, consulte o [Adicionar endpoint registrante de webinar do Zoom](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate).<br><br>

{% tabs %}
{% tab E-mail %}

Crie uma campanha de e-mail com um botão de chamada para ação no corpo da mensagem. Quando um usuário clicar no botão, redirecione-o para a landing page do webinar (com os parâmetros apropriados incluídos no link de redirecionamento). 

Usando os parâmetros no URL para passar dados de usuários, crie uma chamada de API para disparar quando a página for carregada para adicionar o usuário ao webinar.

![Mensagem de e-mail com modelo Liquid usado para incluir nome, sobrenome, endereço de e-mail e cidade.]({% image_buster /assets/img/zoom/zoom1.png %})

Os usuários agora estão registrados para o webinar com os detalhes que já existem em seu perfil da Braze.

{% endtab %}
{% tab Push %}

1. Criar uma campanha push<br><br>

	Defina o comportamento ao clicar no botão para criar um link para a landing page do webinar.<br>

	![Link para o webinar quando um botão é clicado.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Um exemplo simples de landing page para usuários que se inscrevem por meio de um clique no botão de um push. Informe ao usuário para o que ele se inscreveu e confirme seu registro:<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Crie uma campanha de webhook disparada pela mensagem no app ou pelo clique no botão.<br><br>
 	Usando os dados de usuários existentes em seus perfis na Braze, inscreva-se no webinar.<br>

	![Uma campanha baseada em ações que será enviada aos usuários que clicaram em um botão para uma campanha específica.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Exemplo de chamada de webhook para o ponto de extremidade do Zoom.<br>
	{% raw %}
	```json
	POST https://api.zoom.com//meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. Os usuários agora estão registrados para o webinar com os detalhes que já existem em seu perfil da Braze.

{% endtab %}
{% tab Mensagem no app %}

1. Crie uma campanha de mensagens no app<br><br>

	Defina o comportamento ao clicar no botão para criar um link para a landing page do webinar<br>

	![Link para o webinar quando um botão é clicado.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Um exemplo simples de landing page para usuários que se inscrevem por meio de um clique no botão de uma mensagem no app. Informe ao usuário para o que ele se inscreveu e confirme seu registro:<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Crie uma campanha de webhook disparada pela mensagem no app ou pelo clique no botão.<br><br>
	Usando os dados de usuários existentes em seus perfis na Braze, inscreva-se no webinar.<br>

	![Uma campanha baseada em ação que será enviada aos usuários que clicaram em um botão para uma campanha específica.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Exemplo de chamada de webhook para o ponto de extremidade do Zoom.<br>
	{% raw %}
	```json
	POST https://api.zoom.com//meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. Os usuários agora estão registrados para o webinar com os detalhes que já existem em seu perfil da Braze.

{% endtab %}
{% endtabs %}
