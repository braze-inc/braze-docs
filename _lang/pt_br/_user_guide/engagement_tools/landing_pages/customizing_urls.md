---
nav_title: Personalizar o URL
article_title: Personalize os URLs da landing page
description: "Saiba como personalizar os URLs de suas landing pages com a marca de sua empresa, conectando seu domínio ao espaço de trabalho do Braze."
page_order: 1
---

# Personalize os URLs da landing page

> Saiba como personalizar os URLs de suas landing pages com a marca de sua empresa, conectando seu domínio ao espaço de trabalho do Braze.

## Como funciona?

Quando você [conectar seu domínio ao Braze](#connecting-your-domain-to-braze), ele será usado como o domínio padrão para todas as landing pages. Por exemplo, se você conectar o subdomínio `forms.example.com`, os URLs da landing page agora serão `forms.example.com/holiday-sale`.

O número de domínios personalizados que você pode conectar à sua conta Braze depende do seu [nível de plano]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers). Para aumentar seu limite, entre em contato com o gerente de sua conta Braze.

## Conectando seu domínio ao Braze

Para conectar um domínio à sua conta Braze, peça a um administrador que siga as etapas abaixo.

1. Acesse **Configurações** > **Configurações da landing page**.
2. Digite o domínio ao qual deseja se conectar e selecione **Enviar**. Por exemplo, `forms.example.com`.
3. Copie e cole os registros **TXT** e **CNAME** nas configurações de DNS do seu provedor de domínio.
4. Retorne ao dashboard do Braze para verificar a conexão.

![Página Landing Page Settings com um registro TXT e dois registros CNAME listados com seus respectivos nomes e valores.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Dependendo do seu provedor de domínio, a conexão pode levar até 48 horas. Quando o processo for concluído, começaremos a usar seu domínio personalizado para suas landing pages no dashboard do Braze.
{% endalert %}

## Remoção de seu domínio

Se você for um administrador do Braze, poderá remover um domínio configurado anteriormente, concluindo as etapas a seguir:

1. Acesse **Configurações** > **Configurações da landing page**.
2. Selecione **Remover domínio personalizado**
3. Confirmar a remoção do domínio.
4. Remova os registros DNS listados das configurações do seu domínio.

{% alert important %}
Quando você remover um domínio personalizado, esse URL não será mais válido. Todas as landing pages que estavam usando esse domínio serão automaticamente revertidas para o domínio padrão definido pelo Braze.
{% endalert %}


## Recursos do DNS

{% multi_lang_include dns_records.md %}

## Solução de problemas 

### Falha na conexão com meu domínio

Verifique se o domínio foi inserido corretamente e se corresponde ao que foi enviado ao Braze a partir de sua conta de provedor de domínio. Se estiver correto e corresponder, verifique os registros TXT e CNAME fornecidos pelo Braze. Eles devem corresponder aos registros inseridos na conta do provedor de domínio.

## Perguntas frequentes

### Posso conectar vários subdomínios ao meu espaço de trabalho ou conectar um subdomínio a vários espaços de trabalho?

Não, atualmente só é possível conectar um subdomínio a um espaço de trabalho.

### Posso usar o mesmo subdomínio que uso atualmente para meu site principal ou meu domínio de envio?

Não, você não pode usar subdomínios que já estejam em uso. Embora esses subdomínios sejam válidos, eles não podem ser usados para landing pages se já estiverem atribuídos a outros fins ou tiverem registros DNS que entrem em conflito com os registros CNAME necessários.

### Por que meu domínio personalizado está preso em "Conectando" apesar dos registros DNS válidos?

Se o seu domínio personalizado mostrar todos os registros DNS como "Conectado", mas o status do domínio permanecer em "Conectando" por mais de quatro horas, sua organização poderá estar usando registros CAA (Autorização de Autoridade de Certificação) ou retenções de zona do Cloudflare que impedem o Braze de proteger sua página.

#### Registros da CAA

Os registros CAA restringem quais autoridades de certificação podem emitir certificados SSL para o seu domínio. Se os seus registros CAA não incluírem a LetsEncrypt, o Braze (por meio da Cloudflare) não poderá emitir o certificado SSL necessário.

Para resolver isso, peça à sua equipe de TI para adicionar um registro CAA ao seu subdomínio com os seguintes valores:
- **Tipo de registro:** CAA
- **Valor:** `0 issue "letsencrypt.org"`

Para saber mais, consulte a [documentação do CAA da LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### A zona do Cloudflare é mantida

Se sua organização usa o Cloudflare, um recurso de segurança de retenção de zona pode estar impedindo o Braze de criar seu domínio personalizado.

Para resolver isso, peça à equipe de TI para liberar temporariamente a retenção de zona. Para saber mais, consulte a [documentação de retenção de zona da Cloudflare](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Reiniciar o processo de validação

Depois de resolver qualquer um dos problemas, exclua e recrie seu domínio personalizado no dashboard do Braze para reiniciar o processo de validação.

