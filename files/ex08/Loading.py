import os


def ft_tqdm(lst: range) -> None:
    """
    Mimics the tqdm progress bar using the yield operator.
    Displays a progress bar adapted to the terminal width.
    """
    total = len(lst)
    term_width = os.get_terminal_size().columns

    # tqdm format: "100%|================| N/N [time<time, it/s]"
    # We approximate the available bar width
    prefix_len = 5   # "100% "
    suffix_len = len(f"| {total}/{total}")
    bar_width = term_width - prefix_len - suffix_len - 2

    for i, item in enumerate(lst, 1):
        yield item
        percent = i / total
        filled = int(bar_width * percent)
        bar = "=" * filled + ">" if filled < bar_width else "=" * bar_width
        bar = bar.ljust(bar_width)
        line = f"{int(percent * 100):3d}%|{bar}| {i}/{total}"
        print(f"\r{line}", end="", flush=True)
