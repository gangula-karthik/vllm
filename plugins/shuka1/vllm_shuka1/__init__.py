# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

from transformers import AutoConfig

from vllm import ModelRegistry
from vllm_shuka1.config import ShukaConfig

_MODEL_TYPE = "shuka"
_ARCHITECTURE = "ShukaModel"
_MODEL_QUALNAME = "vllm_shuka1.model:ShukaModel"


def register() -> None:
    AutoConfig.register(_MODEL_TYPE, ShukaConfig, exist_ok=True)

    from vllm.transformers_utils import config as vllm_config

    vllm_config._CONFIG_REGISTRY[_MODEL_TYPE] = ShukaConfig

    if _ARCHITECTURE not in ModelRegistry.get_supported_archs():
        ModelRegistry.register_model(_ARCHITECTURE, _MODEL_QUALNAME)
