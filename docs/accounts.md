# Accounts and login information

(passwords)=
## 1Password

We share all Jupyter passwords in a 1Password account.
All JEC team members should have access to this account.
If you do not, ask another team member for access.

Avoid as much as possible to use this service when delegation is possible,
for many services you can login as _yourself_ and have access to the Jupyter
accounts. This is critical in case of a break to know _whose account_ was
breach, and which action from which member need to be reviewed.

## Google Workspace account

Each EC member has access to a Google Workspace account tied to the jupyter.org domain. This workspace account hosts shared drives, jupyter.org google groups, and other infrastructure. The account names are of the form first.last@jupyter.org.

## E-mail and Google account

We have a shared GMail account at `projectjupyter@gmail.com`. This is different from the Google Workspaces account defined above, and is from earlier phases of the project.
This is used as a common login for many services and tools that we use.

`projectjupyter@gmail.com` supports delegation; do not use the [](#passwords)
service. Ask to be added as a delegated user if you do not know how to do it.
Delegated accounts appear with a key symbol followed by `delegated` in the user
switcher.

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

**Do not** access Cloudflare using the shared Jupyter [the Jupyter passwords
service](#passwords); create a Cloudflare account using your own
username/password, and ask a Cloudflare admin to be added as a delegated user.
