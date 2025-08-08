---
nav_title: Solução de problemas
article_title: Solução de problemas de acesso ao Braze
page_order: 8
page_type: reference
description: "Este artigo o orienta na solução de problemas que você pode ter ao tentar acessar o Braze."

---

# Solução de problemas de acesso ao Braze

> Este artigo o ajuda a solucionar problemas que possam ocorrer ao tentar acessar o Braze.

## Bloqueio da conta

Você está bloqueado em sua conta Braze, mas não se preocupe! Podemos ajudar você a voltar a participar.	

É possível saber que tipo de bloqueio está ocorrendo pela mensagem de erro recebida:	

- [Vejo um erro sobre minha senha.](#password-error)	
- [Não vejo nenhum erro, mas a Braze ainda não está me deixando entrar.](#instance-error)	
- [Estou vendo um erro sobre a suspensão da conta.](#account-suspension)	

### Erro de senha

A segurança de sua conta é importante para nós, portanto, as senhas são necessárias para entrar na sua conta.	
- Confira se está entrando na [instância correta do dashboard da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Consulte o administrador de sua conta ou o gerente de conta do Braze para ter certeza.	
- Sua senha pode ter expirado, portanto, será necessário [redefini-la]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	
- Se você usa um serviço de [logon único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), verifique com o administrador da conta se a configuração foi concluída corretamente.	
- Se a sua empresa estiver em várias instâncias da Braze, é possível que esteja usando o e-mail incorreto para fazer o registro.  	

Em caso de dúvida, você sempre pode [redefinir sua senha]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	

### Erro de instância

Se estiver usando a mesma máquina que costuma usar para registrar, a Braze deverá detectar automaticamente a instância correta. No entanto, se isso não acontecer ou se você estiver registrando pela primeira vez, recomendamos que considere o seguinte:	

- Confira se está entrando na [instância correta do dashboard da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Consulte o administrador de sua conta ou o gerente de conta do Braze para ter certeza.
- Se a sua empresa estiver em várias instâncias da Braze, é possível que esteja usando o e-mail incorreto para fazer o registro.	

### Suspensão da conta	

Isso não acontece com muita frequência, mas levamos muito a sério a suspensão e a exclusão de contas. Se encontrar esse erro, recomendamos que entre em contato com o administrador da Braze de sua empresa, com o gerente de conta da Braze ou com o [Suporte][suporte].

## O dashboard do Braze não carrega ou não funciona como esperado

Primeiro, teste se o dashboard será carregado em um navegador diferente. Se o problema não persistir em um navegador diferente, tente o seguinte:

- **Reinicie o dashboard:** Faça logout, saia do navegador e tente registrar-se no dashboard.
- **Atualize seu navegador local:** [Limpe os cookies e o cache do navegador]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies) e tente registrar o dashboard novamente.
- **Use plug-ins compatíveis ou ferramentas de terceiros:** Bloqueadores de anúncios ou softwares de segurança podem impedir o carregamento do dashboard do Braze. Teste isso desativando um bloqueador de anúncios e, em seguida, registrando no dashboard do Braze.
        \- Também é possível verificar os registros do console do navegador. Erros relacionados a `ERR_BLOCKED_BY_CLIENT` podem indicar que o conteúdo está bloqueado por um bloqueador de anúncios.
- **Verifique a qualidade de sua conexão:** A qualidade de sua conexão pode ser ruim. Tente fazer o registro no dashboard do Braze em um dispositivo diferente.
- **Confirme que está acessando o cluster correto:** Certifique-se de que esteja registrando no cluster atribuído à sua empresa. Por exemplo, você pode ser atribuído à US-03, mas está registrando na US-01.
- **Atualize seu navegador:** Atualize seu navegador para o [navegador compatível]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers) mais recente e tente registrar-se no dashboard.

Se o problema ocorrer em todos os navegadores, tente o seguinte:

- **Verifique sua conexão de rede:** Tente desativar sua VPN, se possível, ou desative e reative sua conexão de rede.
- **Reinicie seu dispositivo:** Tente fazer o registro no dashboard do Braze depois de reiniciar o dispositivo.

Se tiver resolvido os problemas anteriores e o dashboard ainda não carregar ou não funcionar como esperado, entre em contato com [o Suporte]({{site.baseurl}}/braze_support/).


