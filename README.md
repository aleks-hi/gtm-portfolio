# GTM Engineering Portfolio

Claude skills, Clay workflows and outbound methods for B2B teams, built with **Claude**, **Clay**, **HubSpot**, **MailerLite**, **Lusha** and **Google Sheets**.

Client work is confidential, so all examples use fictional companies and people.

## Claude skills
| Skill | What it does |
|---|---|
| [trigger-research](skills/trigger-research/SKILL.md) | Researches a prospect, picks a sourced trigger with a scoring rule, drafts a 1st/2nd/3rd message, and QA-checks it before a human sends it. [Example output](skills/trigger-research/examples/example-output.md) |
| [lead-list-qa](skills/lead-list-qa/SKILL.md) | Checks a lead list before outreach or CRM import: duplicates, date typos, bad emails and phones, wrong websites, status gaps. Includes a [Python script](skills/lead-list-qa/scripts/qa_check.py) and a [sample run](skills/lead-list-qa/examples/sample_run.txt) |

## Claude integrations
| Workflow | What it shows |
|---|---|
| [CRM activity sync skill](claude-integrations/crm-activity-sync-skill.md) | A daily, unattended Claude skill that keeps the CRM current from email-tool and telephony activity |

## Clay workflows
| Workflow | What it shows |
|---|---|
| [Signal-based account qualification: a real run](clay-workflows/outbound-signal-qualification.md) | 15 Nordic SaaS companies → 10 real fits → 2 hiring outbound sales. AI columns, human review, and the errors it caught |

## Outbound
| Workflow | What it shows |
|---|---|
| [Trigger research and personalised messaging](outbound/trigger-research-and-messaging.md) | The full process around the trigger-research skill: research, drafting, human review, CRM logging |
| [Account-based list building](outbound/account-based-list-building.md) | Buying committees per account, batch rollout and a weekly update routine |
| [List operations and a pricing model template](ops/spreadsheet-list-ops-and-pricing-model.md) | Merging and matching lists safely, and comparing pricing models from tool costs |

## Other work
| Workflow | What it shows |
|---|---|
| [LinkedIn content system](content/linkedin-content-system.md) | Post formulas, launch messaging, localisation |
| [Invite-only event playbook](outbound/invite-only-event-playbook.md) | Segmented invitations, closed registration, RSVP matching |
| [Social media launch with Canva](content/social-launch-with-canva.md) | Brand kit, layout system, licence and compliance checks |

## Stack
Claude (skills, MCP connectors) · Clay · HubSpot · MailerLite · Lusha · Google Sheets · LinkedIn · Canva · Python
