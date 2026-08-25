# Configuration Guide - Weekly Business Review Agent

## Required configuration values

The agent requires five deployment values:

1. `OCI_TENANCY_OCID` - OCI tenancy or compartment identifier accepted by your AIDP model runtime
2. `OCI_INFERENCE_ENDPOINT` - Endpoint for your OCI Generative AI deployment
3. `OCI_MODEL_ID` - Model identifier available in that deployment and region
4. `WBR_CATALOG_KEY` - AIDP catalog containing the Weekly Business Review tables
5. `WBR_SCHEMA_KEY` - Schema containing the Weekly Business Review tables

No concrete OCI identifier, endpoint, model, catalog, or schema is included in this repository.

---

## Step 1: Find the OCI identifier

1. Sign in to the OCI Console.
2. Open **Identity & Security** and select **Compartments**.
3. Select the compartment used by the AIDP deployment.
4. Copy the identifier required by your model runtime.

Set it as:

```text
OCI_TENANCY_OCID=insert_your_tenancy_or_compartment_id
```

The environment-variable name follows this example's existing runtime contract. Confirm whether your environment expects a tenancy or compartment OCID.

---

## Step 2: Find the inference endpoint

1. Open the OCI Generative AI service in the OCI Console.
2. Select the region and model deployment used by the agent.
3. Copy its inference endpoint.
4. Confirm that the endpoint region matches the deployed model.

Set it as:

```text
OCI_INFERENCE_ENDPOINT=insert_your_inference_endpoint
```

---

## Step 3: Choose the model

1. In OCI Generative AI, review models available in the selected region.
2. Choose a model supported by your AIDP runtime.
3. Copy the exact model identifier.

Set it as:

```text
OCI_MODEL_ID=insert_your_model_id
```

Model availability can differ by region and tenancy.

---

## Step 4: Find the AIDP catalog and schema

1. Open **Master catalog** in AIDP Workbench.
2. Select the catalog containing the uploaded CSV tables.
3. Expand the catalog and select the schema.
4. Confirm that these tables are visible:
   - `weekly_business_metrics`
   - `pipeline_by_stage`
   - `renewal_risk_accounts`
   - `product_usage_by_account`
   - `support_health_by_account`

Set the values as:

```text
WBR_CATALOG_KEY=insert_your_catalog_key
WBR_SCHEMA_KEY=insert_your_schema_key
```

The catalog and schema must be accessible to the deployed agent principal and compute.

---

## Step 5: Configure the deployment

Add all values to the Agent Hub deployment environment:

```text
WBR_CATALOG_KEY=insert_your_catalog_key
WBR_SCHEMA_KEY=insert_your_schema_key
OCI_TENANCY_OCID=insert_your_tenancy_or_compartment_id
OCI_INFERENCE_ENDPOINT=insert_your_inference_endpoint
OCI_MODEL_ID=insert_your_model_id
```

The `.env.example` file contains the same placeholders for reference. The agent reads environment variables directly; it does not load `.env` automatically.

---

## Step 6: Upload the agent

Upload these files while preserving the `a2ui/` directory:

```text
agent.py
oci_llm.py
requirements.txt
a2ui/
```

Use `agent.py` as the high-code entry file.

---

## Validate the configuration

After deployment, ask:

```text
What Weekly Business Review regions, segments, and date ranges are available?
```

A successful response confirms that the agent initialized and the unparameterized SQLTool reached the configured catalog. Then ask:

```text
Show the complete weekly business review for North America Enterprise from 2026-07-27 to 2026-08-02.
```

This validates parameter binding, model synthesis, and A2UI rendering.

---

## Troubleshooting

### Missing configuration

The agent reports every missing SQL or model environment variable during initialization. Add the listed values and redeploy.

### `AgentSetupFailed`

Confirm the entry file, upload structure, required environment variables, and availability of the selected model.

### SQL connection failure

For `AIDP_SQL_TOOL_CONNECTION_DATA_FETCH_ERROR`, verify the catalog connection, compute, permissions, and deployment-principal access.

### SQL execution failure

For `AIDP_SQL_TOOL_QUERY_EXECUTION_ERROR`, confirm the table and column names and verify that date columns are available as `DATE` or `TIMESTAMP` values.

### Model failure

Confirm that the endpoint is valid for the selected region and that the model identifier is available to the deployment.

---

## Configuration checklist

- [ ] OCI tenancy or compartment identifier added
- [ ] OCI inference endpoint added
- [ ] OCI model identifier added
- [ ] AIDP catalog key added
- [ ] AIDP schema key added
- [ ] Five required tables are visible
- [ ] Agent files uploaded with the `a2ui/` directory preserved
- [ ] Catalog discovery prompt succeeds
- [ ] Complete A2UI review prompt succeeds
