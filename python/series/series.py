def slices(series, length):
    if length > len(series):
        raise ValueError("Length is too large or the series is empty")
    if length <= 0:
        raise ValueError("The lenght should be a positive integer")
    return [series[i:i + length] for i in range(len(series) - length + 1)]
