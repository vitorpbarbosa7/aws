from kedro.pipeline import Pipeline, node

from .nodes import toy_print


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=toy_print,
                inputs='params:toy_input', 
                outputs=None,
                name='toy_print'                
            )
        ]
    )