# Data Dictionary

All records in `sample_data/` are synthetic and intended only for demonstration.

## `weekly_business_metrics`

One row per week, region, and customer segment.

| Column | Meaning |
| --- | --- |
| `week_start`, `week_end` | Inclusive reporting period in `YYYY-MM-DD` format |
| `region`, `segment` | Review scope |
| `active_accounts` | Active customer accounts in scope |
| `pipeline_usd` | Open pipeline value in USD |
| `renewal_risk_usd` | Subscription ARR exposed to renewal risk |
| `product_active_users` | Active product users |
| `support_sla_pct` | Support SLA attainment percentage |
| `open_escalations` | Open support escalations |
| `nps` | Net Promoter Score |

## `pipeline_by_stage`

Pipeline value and opportunity count by sales stage for each review scope.

## `renewal_risk_accounts`

Synthetic account-level renewal exposure, risk reason, days to renewal, and accountable role.

## `product_usage_by_account`

Synthetic account-level active users, workflow volume, feature adoption, and usage change.

## `support_health_by_account`

Synthetic account-level ticket volume, priority cases, SLA breaches, response time, and escalations.

## Relationships

`account_id` is stable across the renewal, usage, and support tables. This allows the agent to reason across customer risk signals without embedding joins or arbitrary generated SQL.
