def format_output(result):
    if isinstance(result, list):
        return ", ".join(str(x) for x in result)
    return str(result)
