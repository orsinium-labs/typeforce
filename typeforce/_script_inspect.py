import sys
import MODULE_NAME as module  # type: ignore[import]

for name in dir(module):
    obj = getattr(module, name)
    ann = getattr(obj, '__annotations__', None)
    if ann:
        sys.exit(21)
sys.exit(22)
