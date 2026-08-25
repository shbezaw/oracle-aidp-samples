from __future__ import annotations

import os
from typing import Any


TENANCY_OCID = os.getenv(
    "OCI_TENANCY_OCID",
    "",
).strip()
OCI_ENDPOINT = os.getenv(
    "OCI_INFERENCE_ENDPOINT",
    "",
).strip()
MODEL_ID = os.getenv("OCI_MODEL_ID", "").strip()


def pre_invoke_setup(**kwargs: Any) -> Any:
    """Forward Agent Hub session setup when the AIDP helper package is present."""

    try:
        from aidputils.agents.toolkit.agent_helper import pre_invoke_setup as aidp_pre_invoke_setup
    except ModuleNotFoundError:
        return None
    return aidp_pre_invoke_setup(**kwargs)


def build_llm() -> Any:
    """Build the OCI-backed planner used by the deployed WBR agent."""

    required_configuration = {
        "OCI_TENANCY_OCID": TENANCY_OCID,
        "OCI_INFERENCE_ENDPOINT": OCI_ENDPOINT,
        "OCI_MODEL_ID": MODEL_ID,
    }
    missing = [name for name, value in required_configuration.items() if not value]
    if missing:
        raise RuntimeError(
            "Missing required OCI model configuration: " + ", ".join(missing)
        )

    from aidputils.agents.toolkit.agent_helper import init_oci_llm
    from aidputils.agents.toolkit.configs import OCIAIConf

    llm_conf = OCIAIConf(
        model_provider="generic",
        compartment_id=TENANCY_OCID,
        model_args={},
        endpoint=OCI_ENDPOINT,
        model_id=MODEL_ID,
        guardrails_config={
            "name": "Default Guardrails",
            "description": "Default empty guardrails configuration",
            "policies": [],
        },
    )
    llm = init_oci_llm(llm_conf)
    if llm is None:
        raise RuntimeError("init_oci_llm returned None.")
    return llm
