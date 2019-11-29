from timeit import timeit


def ordinal(n, suffix='.'):
    return "{}{}{}".format(
        n,
        "tsnrhtdd"[
           (n/10 % 10 != 1) *
           (n % 10 < 4)*n % 10
           ::4
        ],
        suffix
    )


def run_tests(
        test=timeit,
        ranked=True,
        **tests
):
    results = dict()
    for name, func in tests.items():
        results[name] = test(func)

    if ranked:
        ranked_keys = sorted(
            results.keys(),
            # key=results.__getitem__
            key=lambda k: results[k]
        )

        for rank, key in enumerate(ranked_keys, start=1):
            result = results[key]
            print(ordinal(rank), key, '=', result)

    else:
        for name, result in results.items():
            print(name, '=', result)
