def transform(legacy_data):
    return {data.lower(): key for key, dataset in legacy_data.items() for data in dataset}
