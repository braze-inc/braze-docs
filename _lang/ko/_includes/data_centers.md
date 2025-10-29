{% if include.datacenters == "AU" %}
| 대시보드 URL > REST 엔드포인트 > SDK 엔드포인트 >
| --- | --- | --- |
| `https://dashboard.au-01.braze.com` | `https://rest.au-01.braze.com` | `sdk.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endif %}

{% if include.datacenters == "EU" %}
| 대시보드 URL > REST 엔드포인트 > SDK 엔드포인트 >
| --- | --- | --- |
| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endif %}

{% if include.datacenters == "ID" %}
| 대시보드 URL > REST 엔드포인트 > SDK 엔드포인트 >
| --- | --- | --- |
| `https://dashboard.id-01.braze.com` | `https://rest.id-01.braze.com` | `sdk.id-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endif %}

{% if include.datacenters == "US" %}
| 대시보드 URL > REST 엔드포인트 > SDK 엔드포인트 >
| --- | --- | --- |
| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
| `https://dashboard.us-10.braze.com` | `https://rest.us-10.braze.com` | `sdk.us-10.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endif %}

{% if include.datacenters == "instances" %}
|인스턴스|URL|REST 엔드포인트|SDK 엔드포인트|
\|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|US-10| `https://dashboard.us-10.braze.com` | `https://rest.us-10.braze.com` | `sdk.us-10.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
|AU-01| `https://dashboard.au-01.braze.com`| `https://rest.au-01.braze.com` | `sdk.au-01.braze.com` |
|ID-01| `https://dashboard.id-01.braze.com`| `https://rest.id-01.braze.com` | `sdk.id-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }
{% endif %}

<!--The following section is the list of IPs for IP allowlisting-->

{% if include.datacenters == "ips" %}
{% subtabs %}
{% subtab United States (US) %}
예를 들어 `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, 다음은 관련 IP 주소입니다.
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`

예를 들어 `US-08` 이 관련 IP 주소입니다:
- `52.151.246.51`
- `52.170.163.182`
- `40.76.166.157`
- `40.76.166.170`
- `40.76.166.167`
- `40.76.166.161`
- `40.76.166.156`
- `40.76.166.166`
- `40.76.166.160`
- `40.88.51.74`
- `52.154.67.17`
- `40.76.166.80`
- `40.76.166.84`
- `40.76.166.85`
- `40.76.166.81`
- `40.76.166.71`
- `40.76.166.144`
- `40.76.166.145`

예를 들어 `US-10` 이 관련 IP 주소입니다:
- `100.25.232.164`
- `35.168.86.179`
- `52.7.44.117`
- `3.92.153.18`
- `35.172.3.129`
- `50.19.162.19`
{% endsubtab %}
{% subtab European Union (EU) %}
인스턴스 `EU-01` 및 `EU-02`의 경우, 관련 IP 주소는 다음과 같습니다.
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% subtab Australia (AU) %}
예를 들어 `AU-01` 이 관련 IP 주소입니다:
- `13.210.1.145`
- `13.211.70.159`
- `13.238.45.54`
- `52.65.73.167`
- `54.153.242.239`
- `54.206.45.213`
{% endsubtab %}
{% subtab Indonesia (ID) %}
예를 들어 `ID-01` 이 관련 IP 주소입니다:
- `108.136.157.246`
- `108.137.30.207`
- `16.78.128.71`
- `16.78.14.134`
- `16.78.162.208`
- `43.218.73.35`
{% endsubtab %}
{% endsubtabs %}
{% endif %}
