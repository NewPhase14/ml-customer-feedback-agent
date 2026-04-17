from autogen.code_utils import create_virtual_env
from autogen.coding import CodeBlock, LocalCommandLineCodeExecutor

venv_dir = ".venv"
venv_context = create_virtual_env(venv_dir)

executor = LocalCommandLineCodeExecutor(virtual_env_context=venv_context)
print(
    executor.execute_code_blocks(code_blocks=[CodeBlock(language="python", code="import sys; print(sys.executable)")])
)