"""Model-specific default parameter sources."""

from pathlib import Path
from typing import List, Tuple, Union

__all__ = ("get_default_params_for_model",)

# Mapping from model name patterns to embedded param file names.
# Keys are tuples of model name substrings; if any substring matches, those
# param files will be loaded.
_MODEL_PARAM_MAP: dict[tuple[str, ...], list[str]] = {
    ("plane",): [
        "embedded://plane-default.parm",
    ],
    ("quad", "copter", "heli", "hexa", "octa", "tri", "y6"): [
        # "embedded://copter-default.parm",
        # "embedded://copter-skybrush.parm",
        "embedded://copter.parm",
    ],
}

_DEFAULT_COPTER_PARAMS: list[str] = [
    "embedded://copter-default.parm",
    "embedded://copter-skybrush.parm",
]


def get_default_params_for_model(
    model: str | None,
) -> List[Union[Path, str, Tuple[str, float]]]:
    """Return a list of default embedded param file paths for the given model.

    Parameters:
        model: The SITL model name (e.g., 'quad', 'plane', 'heli'). If None or
            unrecognised, defaults to copter parameters.

    Returns:
        A list of ``embedded://...`` strings suitable for passing to
        SimulatedDroneSwarm.
    """
    if model is None:
        return list(_DEFAULT_COPTER_PARAMS)

    model_lower = model.lower()
    for patterns, param_files in _MODEL_PARAM_MAP.items():
        for pattern in patterns:
            if pattern in model_lower:
                return list(param_files)

    # Fallback to copter defaults
    return list(_DEFAULT_COPTER_PARAMS)
