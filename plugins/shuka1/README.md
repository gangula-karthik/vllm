# vLLM Shuka-1 Plugin

Out-of-tree vLLM model plugin for `sarvamai/shuka-1`.

## Install

From this checkout:

```bash
uv pip install -e plugins/shuka1
```

For local vLLM development, install vLLM first as usual:

```bash
VLLM_USE_PRECOMPILED=1 uv pip install -e . --torch-backend=auto
uv pip install -e plugins/shuka1
```

## Use

```bash
vllm serve sarvamai/shuka-1 --trust-remote-code --max-model-len 4096
```

To load only this plugin when multiple vLLM plugins are installed:

```bash
VLLM_PLUGINS=register_shuka1 vllm serve sarvamai/shuka-1 --trust-remote-code --max-model-len 4096
```

This plugin intentionally keeps Shuka-1 support outside the vLLM core tree.
