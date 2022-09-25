"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from .pipelines import toy_pipe as tp

toy_pipe = tp.create_pipeline()


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {"__default__": toy_pipe}
