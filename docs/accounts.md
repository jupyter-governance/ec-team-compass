# Accounts and login information

(passwords)=
## 1Password

We share all Jupyter passwords in a 1Password account.
All JEC team members should have access to this account.
If you do not, ask another team member for access.

**Prefer delegating to user accounts over using the shared account**. 1Password lets you [delegate access and authority to user accounts](https://1password.com/features/user-management/) which is preferred over using the shared account.

## Google Workspace account

Each EC member has access to a Google Workspace account tied to the jupyter.org domain. This workspace account hosts shared drives, jupyter.org google groups, and other infrastructure. The account names are of the form first.last@jupyter.org.

## E-mail and Google account

We have a shared GMail account at `projectjupyter@gmail.com`. This is different from the Google Workspaces account defined above, and is from earlier phases of the project.
This is used as a common login for many services and tools that we use.

**To access the Jupyter gmail account** ask a team member to add you as a "delegated user" if you do not know how to do it.
Delegated accounts appear with a key symbol followed by `delegated` in the user switcher.

## Google Calendar

The [Jupyter-wide Google Calendar](https://calendar.google.com/calendar/u/1?cid=bTNoZWs2OWRhZzczODF1bXQ4a2NqZDc1dTRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) is a shared calendar for all of Jupyter's events.
Editing rights to this calendar is given out on a person-by-person basis.
All JEC members should have the ability to edit this calendar.
If you want edit access, ask another member of the JEC to add you to this calendar.

**To add events**, from your personal Google account, open the calendar app, create an event, and select the **Project Jupyter** calendar.

(cloudflare)=
## CloudFlare for URLs and DNS

Jupyter has a CloudFlare account that controls the DNS for all of the Jupyter domains.

All **Executive Council** members have access to this account.

**Delegate to user accounts rather than using the shared account**. As with the [1Password service](#passwords), CloudFlare lets you [delegate access to user accounts](https://developers.cloudflare.com/fundamentals/manage-members/manage/): create a CloudFlare account with your own username and password, and ask a CloudFlare admin to add you as a delegated user.

### Proxy status and HTTPS for hosted sites (GitHub Pages, Netlify, Read the Docs)

CloudFlare's proxy (the orange cloud icon) is on by default for new DNS records. If a domain points to a hosting provider that issues its own HTTPS certificate, a proxied record can break the SSL certificate process, because the provider can no longer see the real DNS target to validate the domain.

**To fix this**: set the record in CloudFlare to "DNS only" (grey cloud) so the host handles HTTPS directly. Here are a few static hosts this might apply to:

- **GitHub Pages**: [community discussion](https://github.com/orgs/community/discussions/23632)
- **Netlify**: [DNS & HTTPS troubleshooting](https://docs.netlify.com/manage/domains/troubleshooting-tips/)
- **Read the Docs**: their docs tell you to disable the proxy on the CNAME record, since Cloudflare won't proxy a domain that's already proxied on Read the Docs' own Cloudflare account. See their [custom domains guide](https://github.com/readthedocs/readthedocs.org/blob/main/docs/user/guides/custom-domains.rst).

If a site needs CloudFlare-specific features like caching or a WAF, keep the proxy on and use a CloudFlare Certificate instead, but this might not work for things like double-level subdomains (e.g. `foo.bar.jupyter.org`).

## Zoom

We use the Linux Foundation meeting system for scheduling virtual meetings using
Zoom. To schedule a virtual meeting for Jupyter, please contact a member of the
Executive Council.

To lower the friction of collaborating, we have one Zoom meeting open every day
from noon-10pm UTC. Many subprojects use this shared project Zoom meeting for
their meetings.

In order to administer a Zoom meeting, including recording a meeting, you need
the Host Key for the meeting. If you have permission to see the Host Key for a
meeting, you can access it by doing the following:

1. Log into https://lfx.linuxfoundation.org/
2. Under the Action Center block, click the meeting name (don't click "join")
3. In the popup with meeting info, you will be able to see the Host Key as one of fields
4. In Zoom, open the participant view, click "Claim Host", and enter the host key
