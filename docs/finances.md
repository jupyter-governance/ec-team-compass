# Finances and grants

Project Jupyter's finances run through [The Linux Foundation](https://www.linuxfoundation.org/) (LF) and [LF Charities](https://lf-charities.org/).
This page explains how grants and other funds flow through the LF structures that hold Jupyter's money. It documents where the money can land, how much overhead is taken out, and who controls how it is spent.

## How money is held

Two LF entities can receive and hold Jupyter funds:

- **[The Jupyter Foundation](https://jupyterfoundation.org/)** is a directed fund of [The Linux Foundation 501(c)(6)](https://projects.propublica.org/nonprofits/organizations/460503801). This is the main pool of Jupyter money and is governed by the [Jupyter Foundation's governing board](xref:foundation).
- **[LF Charities Inc](https://lf-charities.org/)** hosts Project Jupyter as an open-source project and is a [501(c)(3) nonprofit](https://projects.propublica.org/nonprofits/organizations/841730246). Project Jupyter is governed by the Jupyter Executive Council, a community-elected group that also sits on the Jupyter Foundation governing board.[^509a3]

[^509a3]: LF Charities is a 509(a)(3) "supporting organization" for the LF 501(c)(6). That legal relationship is what lets Project Jupyter receive funds in LF Charities and later move them into the Jupyter Foundation to save on G&A overhead.

:::{warning} Open question: grants raised by someone other than the EC
The Executive Council controls the 501(c)(3), so it directs how those funds are spent.
We have not settled what happens when someone else, such as a subproject or individual leader, raises a grant and expects to direct those funds themselves.
We need a clear policy for who decides how that money is spent.
:::

## G&A fees (aka indirect fees)

The LF charges a general and administrative (G&A) fee on income to cover the administration cost. The rate is **9%** on the first 1 million USD of income in a year and **6%** on income over that. The fee is assessed when the income lands in its _final destination fund_, not when it first arrives. 

:::{note} Example
Money is received into LF Charities and then _transferred to the Jupyter Foundation_. It is charged the G&A fee when it lands in the Jupyter Foundation (its final destination). If the Jupyter Foundation has already received `$1 million USD` in income in the year, the funds moved in from LF Charities are charged the lower **6%** overhead rate.
:::

:::{note} High-cost grants may incur a higher G&A fee
Some grants require an exceptional amount of reporting or compliance work.
For example, grants or contracts from the US federal government.
For these, LF may charge an additional G&A fee to cover the extra administration costs.
:::

## Restricted funds and how transfers are tracked

There is a tradeoff between moving money into the Jupyter Foundation for the lower overhead and keeping it separately controlled in LF Charities.

When LF Charities transfers money into the Jupyter Foundation, it goes in without conditions.
This is deliberate: attaching conditions would make the money "restricted funding" under IRS rules and trigger extra reporting requirements. The cost of avoiding that is that the money becomes part of the Jupyter Foundation's single pot rather than a separately tracked bucket.

The Jupyter Foundation's governing board then [allocates that money](xref:foundation#budget-allocation). It can steer funds toward the priorities the Executive Council has laid out, so the EC's intent can still be honored in practice. What it cannot do is make an explicit written commitment tied to the transfer, since that would be the kind of condition that creates restricted funding.

If keeping funds under the Executive Council's governance matters more than the lower overhead, the money can instead stay in LF Charities. However, until the yearly income there for Jupyter passes 1 million USD (regardless of any funds that are in the 501(c)(6)), the overhead rate will be the higher 9% rate.

## Grants on behalf of a subproject

A grant "for Jupyter" can be received two ways:

- Into one of the LF entities above, so the money sits inside Jupyter's own structures.
- By an outside organization (for example, a university) that does the work and administers the grant directly.

:::{warning} Open question: approval for grant work on Jupyter technology
We need a process for approving grant work that involves Jupyter technology.
A grant commits people to a particular vision and execution plan, and we want to be sure the project is aligned with both before anyone signs on.
Otherwise others can get legally committed to work that Jupyter isn't ready to accept.
:::

