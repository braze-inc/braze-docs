---
nav_title: API Network Connectivity Issues
article_title: API Network Connectivity Issues
page_order: 4
description: "This reference article touches on API connectivity issues and how to troubleshoot them."
page_type: reference
---

# API connectivity issues

> This reference article touches on API connectivity issues and how to troubleshoot them.

Braze's API endpoints use a CDN that routes traffic to the closest POP based on DNS information.  If you are having issues connecting or notice that you are connecting to a POP that is not efficient, please make sure to use your provider's DNS servers or DNS servers that are set up in the same data center as your server and have proper IP location meta-information associated with them.

We have noticed that a handful of firewalls attempt to modify or secure HTTPS/TLS traffic which interferes with connections to Braze's API endpoints. If your servers are behind any sort of physical firewall, please disable any HTTPS/TLS acceleration or modifications that the firewall(s) and/or router(s) are performing.  Additionally, you can whitelist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

Occasionally, iptables setups that filter on SYN/ACK/RST packets can also cause issues, so if you are using iptables on your host you could also whitelist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

If you are still having network issues with connecting to Braze's API Endpoint, please provide an [MTR Test][1] and the results from [Fastly Debug][2] while experiencing an issue and submit that with your support request. Note that the test results must be obtained from a server that is having issues connecting to Braze's API endpoint, not from a development machine.  A network capture (tcpdump or .pcap file) will also be helpful if it can be obtained.

For more information about MTR, check out these resources based on your operating system:

- [GNU/Linux][4]
- [macOS][5]

## Whitelisting Braze's API endpoint IP ranges

To whitelist Braze's API endpoint through your firewall, our CDN provides access to the list of assigned IP ranges via a JSON dump. You can access the public list of Fastly IP ranges [here][3].


[1]: https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2
[2]: http://www.fastly-debug.com/
[3]: https://api.fastly.com/public-ip-list
[4]: https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues
[5]: https://formulae.brew.sh/formula/mtr
