# Pull Request/Issue Resolution

#### Description of Change:
> I'm changing..... (could be a link, a new image, a new section, etc.)... because...

Closes #**ISSUE_NUMBER_HERE**

#### Is this change associated with a Braze feature/product release?
- [ ] Yes (**Insert Feature Release Date Here**)
- [ ] No

---

<details>
<summary>✔️ Pull Request Checklist</summary>
<br>

- [ ] Check that you haven't removed any images (replacing an image with an updated one of the same name is fine), as this breaks the French site
- [ ] Check that all links work.
- [ ] Ensure you have completed [our Contributors License Agreement](https://www.braze.com/docs/cla/).
- [ ] Tag @josh-mccrowell-braze and @bre-fitzgerald as a reviewer when your work is **done and ready to be reviewed for merge**. Are you an internal product manager? Reference the internal reviewing chart to tag the appropriate reviewer.
- [ ] If the documentation involves a 1) paid SKU, 2) a third party, 3) SMS, 4) AI, or 5) privacy, ensure that Maria Maldonado on the Legal team has signed off.
- [ ] Tag others as reviewers as necessary.
- [ ] If you have modified any links, be sure to add redirects to `assets` > `js` > `broken_redirect_list.js`

</details>

<details>
<summary>⭐ Helpful Wiki Shortcuts</summary>
<br>

- [Writing Style Guide](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub)
- [Image Style Guide](https://docs.google.com/document/d/e/2PACX-1vRJSkwcjmjrTfLDagZccLpOMMyh5NN5SXRZSjz12cRAHbX4OrUmhvCmYpf_p5YB-9r4_jSOQLkicQIH/pub)
- [Styling Test Page](https://www.braze.com/docs/home/styling_test_page/)

</details>

<details>
<summary>❗ ATTN: For PR Reviewers</summary>
<br>

- [ ] Read our [Reviewing a PR page](https://github.com/Appboy/braze-docs/wiki/Reviewing-a-PR) for more on our reviewing suggestions.
- [ ] Read our [Previewing Documentation page](https://github.com/braze-inc/braze-docs/wiki/Previewing-and-Testing-Documentation) to see how to check the deployment.
  - [ ] Preview all changes in the linked Vercel environment by clicking the preview link in the vercel-bot comment in your PR.
</details>

<details>
<summary>❗ ATTN: Internal Reviewing Chart </summary>
<br>
<b>Work at Braze and not sure who to tag for review?</b> <br>Before tagging @josh-mccrowell-braze or @bre-fitzgerald for a general review, reference the following chart to see if a specific product vertical/reviewer applies to your pull request.
<br><br>
<table>
<tr>
    <td><b>Reviewer</b></td>
    <td><b>Product Vertical</b></td>
  </tr>
  <tr>
    <td>@josh-mccrowell-braze</td>
    <td>Monolith Deployments<br>Quality Infrastructure<br>Platform Infrastructure<br>Datalake<br>SDKs<br>Currents</td>
  </tr>
  <tr>
    <td>@bre-fitzgerald</td>
    <td>Intelligence<br>In-App Messages<br>Channels<br>FIX</td>
  </tr>
  <tr>
    <td>@lydia-xie</td>
    <td>Ingestion<br>Core Objects<br>Core Messaging<br>Messaging Experience<br>Message Components<br>Email (Composition and Infrastructure)</td>
  </tr>
  <tr>
    <td>@rachel-feinberg</td>
    <td>Customer Lifecycle, Identity and Permissions<br>SMS<br>User Targeting<br>Reporting</td>
  </tr>
</table>
</details>
