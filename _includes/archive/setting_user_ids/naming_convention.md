At Braze, we **strongly recommend** naming user IDs, also referred to as external IDs, in a [UUIDs and GUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. UUIDs and GUIDs are universally unique identifiers that consist of a 128-bit number used to identify information in computer systems. This means that these UUIDs are long, random and well distributed. If you choose a different method in which to name your user IDs, they must also be long, random and well distributed. It is also important to note, that user IDs are **case sensitive**. For example, "Abcdef" is a different user from "abcdef".

If you find your user IDs include names, email addresses, timestamps, or incrementors, we suggest using a new naming method that is more secure so that your user IDs are not as easy to guess or impersonate. If you choose to include this in your user IDs, we **strongly recommend** adding our [SDK authentication]({{site.baseurl}}/developer_guide/authentication/) feature to prevent user impersonation.

Providing this information to others may allow people outside your organization to glean information on how your user IDs are structured, opening up your organization to potentially malicious updates or removal of information. Choosing the correct naming convention from the start is one of the most important steps in setting up user IDs. However, a migration is possible using our [external ID migration endpoint]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| User ID Naming |
| Recommended | Not Recommended |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | CompanyName-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}