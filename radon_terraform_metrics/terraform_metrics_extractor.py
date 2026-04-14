from import_metrics import general_metrics, configuration_metrics,complex_metrics


def extract_all(script: str):

    if script is None:
        raise TypeError('Expected a string')

    metrics = {}
    metrics.update(general_metrics)
    metrics.update(configuration_metrics)
    metrics.update(complex_metrics)
    results = dict()

    for name in metrics:
        results[name] = metrics[name](script).count()

    return results