# Weekly Business Review SQLTool + A2UI Agent

A high-code Oracle AIDP example that turns governed sales and customer-success data into an interactive Weekly Business Review. The agent queries five uploaded tables through predefined, read-only SQLTools, reasons across the returned results, and renders an A2UI dashboard with filters, KPI cards, charts, tables, insights, recommendations, and follow-up actions.

The repository includes synthetic CSV data. It does not include a database, OCI credentials, tenancy identifiers, or a deployed Agent Hub configuration.

## Agent card description

> A SQLTool-backed Weekly Business Review agent for an enterprise SaaS product portfolio. It analyzes sales pipeline, subscription renewals, product adoption, and customer-support health, then produces interactive A2UI dashboards with filters, charts, account-level insights, risks, and recommended actions.

## How it works

```text
User request
    |
    v
OCI-hosted reasoning model
    |
    v
Six predefined AIDP SQLTools
    |
    v
Structured response plan
    |
    v
Python validation and A2UI rendering
```

The model decides which tools are needed and synthesizes the business narrative from their results. It does not generate or execute arbitrary SQL. Python validates the response plan, asks the model to repair an invalid plan, and only then converts the approved plan into A2UI operations.

When data is unavailable or no rows match the requested scope, the agent reports that state explicitly. It does not substitute fabricated fallback data.

## Capabilities

- Conversational questions and concise text responses
- Date, region, and segment filtering
- Executive KPI summaries
- Pipeline-by-stage analysis and charting
- Renewal-risk account prioritization
- Product-adoption and usage analysis
- Support-health and escalation analysis
- Cross-dataset insights and recommended actions
- Interactive A2UI follow-up buttons
- Diagnostic IDs for model, SQLTool, planning, and rendering failures

## Repository layout

```text
weekly-business-review-github/
|-- agent.py                     # Deployment entrypoint and complete agent
|-- oci_llm.py                   # OCI model configuration
|-- requirements.txt             # Additional Python dependency
|-- .env.example                 # Configuration names with placeholder values
|-- CONFIGURATION.md             # Step-by-step deployment configuration
|-- a2ui/                        # A2UI manager, parser, schemas, and catalogs
|-- sample_data/                 # Synthetic CSV tables for the example
|-- docs/
|   |-- aidp-setup.md            # AIDP table and deployment setup
|   `-- data-dictionary.md       # Table and column definitions
```

## Sample customers

The sample data uses fictional, anonymized organizations:

- ABC Manufacturing
- DEF Health
- GHI Financial
- JKL Energy
- MNO Media
- PQR Cloud
- STU Robotics
- VWX Dynamics

## Prerequisites

- An Oracle AIDP workspace with Agent Hub access
- A catalog and schema available to the AIDP SQLTool connection
- Compute and read permissions for the uploaded tables
- Access to an OCI Generative AI model
- An Agent Hub renderer that supports the included A2UI catalog components

The AIDP runtime is expected to provide `aidputils`, LangChain, and LangGraph. `requirements.txt` lists the extra package used directly by this example.

## Load the sample data

Upload each file in `sample_data/` as a table with the matching filename:

| File | Table |
|---|---|
| `weekly_business_metrics.csv` | `weekly_business_metrics` |
| `pipeline_by_stage.csv` | `pipeline_by_stage` |
| `renewal_risk_accounts.csv` | `renewal_risk_accounts` |
| `product_usage_by_account.csv` | `product_usage_by_account` |
| `support_health_by_account.csv` | `support_health_by_account` |

Preserve `week_start` and `week_end` as Oracle `DATE` or `TIMESTAMP` columns. See `docs/data-dictionary.md` for the full schema.

## Configure the agent

Set these values in the deployment environment or the approved Agent Hub configuration mechanism:

```text
WBR_CATALOG_KEY=<catalog containing the five tables>
WBR_SCHEMA_KEY=<schema containing the five tables>
OCI_TENANCY_OCID=<your OCI tenancy OCID>
OCI_INFERENCE_ENDPOINT=<insert your OCI inference endpoint>
OCI_MODEL_ID=<insert your deployed model ID>
```

Do not commit real OCIDs, API keys, tokens, passwords, or client secrets. Use the AIDP Credential Store for secrets when a connected service requires them.

## Deploy to Agent Hub

Upload the following while preserving the `a2ui/` directory:

```text
agent.py
oci_llm.py
requirements.txt
a2ui/
```

Use `agent.py` as the high-code entry file. It defines a single local agent class with `setup()` and `invoke()` methods.

Required values are documented step by step in `CONFIGURATION.md`. Additional deployment notes are in `docs/aidp-setup.md`.

## Example prompts

Start by verifying the SQLTool connection:

> What Weekly Business Review regions, segments, and date ranges are available?

Then test the complete experience:

> Show the complete weekly business review for North America Enterprise from 2026-07-27 to 2026-08-02. Highlight the top risks and recommend three actions.

Additional coverage:

- `Show pipeline by stage for North America Enterprise from 2026-07-27 to 2026-08-02.`
- `Which renewal-risk accounts need executive attention for North America Enterprise from 2026-07-27 to 2026-08-02?`
- `Compare product usage and support health for North America Enterprise from 2026-07-27 to 2026-08-02. Which accounts need intervention?`
- `Show the complete review for EMEA Enterprise from 2026-07-27 to 2026-08-02.`
- `Show the complete review for EMEA Commercial from 2025-01-01 to 2025-01-07.`

The last prompt demonstrates the no-results path.
