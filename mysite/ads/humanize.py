def naturalsize(count):
    fcount = float(count)
    multipliers = [(1 << 30, 'GB'), (1 << 20, 'MB'), (1 << 10, 'KB')]
    for factor, suffix in multipliers:
        if fcount >= factor:
            break
    amount = int(fcount / factor)
    return f"{amount} {suffix}"
