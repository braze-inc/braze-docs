At Braze, we __strongly suggest__ naming User IDs also known as `external_user_ids`, in a [UUIDs/GUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. UUIDs/GUIDs are Universally Unique Identifiers that consist of a 128-bit number used to identify information in computer systems. This means that these UUIDs are long, random and well distributed. If you choose a different method in which to name your User IDs, they must also be long, random and well distributed. It is also important to note, that User IDs are __case sensitive__. For example, "Abcdef" is a different user from "abcdef".

If you find your `external_user_ids` include names, email addresses, timestamps, or incrementors we __strongly suggest__ picking up a new naming method that is more secure. We do not want names, email address, timestamps or incrementors included in your User IDs, because while it might be easy for people within your organization to quickly identify others, __it is not a secure method__.

Providing this information to others may allow people outside your organization to glean information on how your User IDs are structured, opening up your organization to potentially malicious updates or removal of information. Choosing the correct naming convention from the start is one of the most important steps in setting up User IDs, however a migration is possible using our [External ID Migration API Endpoint]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| User ID Naming |
| Good Example | Bad Example |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 83nmas45-eks1-083m-mk36-426655440000 | Anna@email.com |
| Mbfjla32-937z-09es-sbv6-064026245228 | CompanyName-1-2-19 |
| k6twn923-8234-7354-lzpd-139317000652 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}