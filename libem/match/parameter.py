import libem.parameter as libem
from libem.core.struct import Parameter

model = libem.model
temperature = libem.temperature

tools = Parameter(
    default=[],
    options=[],
)

# chain-of-thought, confidence score, and clarity score
cot = Parameter(
    default=False
)
confidence = Parameter(
    default=False
)
clarity = Parameter(
    default=False
)
