SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
}

def approximate_size(size, a_kilobye_is_1024_bytes=True):
    """
    Convert a file size to human-readable form.

    Keyword arguments:
        size -- file size in bytes
        a_kilobye_is_1024_bytes -- use 1024 if True, 1000 if False

    Returns: string

    """

    if size < 0:
        raise ValueError("Number must be non-negative")

    multiple = 1024 if a_kilobye_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('Number too large!')


if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
    print(approximate_size(4000, False))