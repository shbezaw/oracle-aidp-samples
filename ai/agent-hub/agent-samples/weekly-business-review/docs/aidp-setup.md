# Oracle AIDP Setup

## 1. Create the tables

Upload each CSV in `sample_data/` to an AIDP-accessible catalog and schema. Preserve these table names:

- `weekly_business_metrics`
- `pipeline_by_stage`
- `renewal_risk_accounts`
- `product_usage_by_account`
- `support_health_by_account`

Confirm that `week_start` and `week_end` are exposed as Oracle `DATE` or `TIMESTAMP` values. The included SQLTools convert incoming `YYYY-MM-DD` parameters with `TO_DATE`.

## 2. Configure deployment values

Set the following deployment environment values:

```text
WBR_CATALOG_KEY=<catalog containing the tables>
WBR_SCHEMA_KEY=<schema containing the tables>
OCI_TENANCY_OCID=<OCI tenancy OCID>
OCI_INFERENCE_ENDPOINT=<insert your OCI inference endpoint>
OCI_MODEL_ID=<insert your deployed model ID>
```

Use Agent Hub Credential Store or deployment configuration for secrets. This example does not require or accept a database password in source code.

## 3. Upload the agent

Upload these files while preserving the `a2ui/` directory:

```text
agent.py
oci_llm.py
requirements.txt
a2ui/
```

Use `agent.py` as the high-code entrypoint. It exposes one local class with `setup()` and `invoke()`.

## 4. Verify SQLTool access

Start with the unparameterized connectivity request:

```text
What Weekly Business Review regions, segments, and date ranges are available?
```

Then run a populated review:

```text
Show the complete weekly business review for North America Enterprise from 2026-07-27 to 2026-08-02. Highlight the top risks and recommend three actions.
```

## Troubleshooting

- `AgentSetupFailed`: confirm that only `agent.py`, `oci_llm.py`, `requirements.txt`, and `a2ui/` were uploaded.
- `AIDP_SQL_TOOL_CONNECTION_DATA_FETCH_ERROR`: verify catalog connection, schema access, compute, and permissions.
- `AIDP_SQL_TOOL_QUERY_EXECUTION_ERROR`: verify table and column names plus the `DATE` or `TIMESTAMP` types for `week_start` and `week_end`.
