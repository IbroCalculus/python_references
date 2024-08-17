from typing import List


def get_full_name(*, names: List[str]) -> str:
    return ' '.join(names)


print(get_full_name(names=['Ibrahim', 'Musa', 'Suleiman', 'Aboy']))