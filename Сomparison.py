import timeit

from task_3 import knuth_morris_pratt
from task_3 import boyer_moore
from task_3 import rabin_karp

def time_comparison(algorithm, content, to_find):
    return timeit.timeit(lambda: algorithm(content, to_find), number=100)

def main():
    article_1 = './task_3/article_1.txt'
    article_2 = './task_3/article_2.txt'

    with open(article_1, "r", encoding="utf-8", errors="ignore") as file:
        content_1 = file.read()
    with open(article_2, 'r', encoding="utf-8", errors="ignore") as file:
        content_2 = file.read()

    substring_1 = content_1[200:215]
    substring_2 = content_2[300:330]
    fake_substring = "lorem ipsum dolor sit amet"

    print(f"knuth morris pratt, article 1: {time_comparison(knuth_morris_pratt.kmp_search, content_1, substring_1)}")
    print(f"knuth morris pratt, article 2: {time_comparison(knuth_morris_pratt.kmp_search, content_2, substring_2)}")
    print(f"knuth morris pratt, article 1 (fake) : {time_comparison(knuth_morris_pratt.kmp_search, content_1, fake_substring)}")
    print(f"knuth morris pratt, article 1 (fake) : {time_comparison(knuth_morris_pratt.kmp_search, content_2, fake_substring)}")

    print(f"boyer moore, article 1: {time_comparison(boyer_moore.boyer_moore_search, content_1, substring_1)}")
    print(f"boyer moore, article 2: {time_comparison(boyer_moore.boyer_moore_search, content_2, substring_2)}")
    print(f"boyer moore, article 1 (fake): {time_comparison(boyer_moore.boyer_moore_search, content_1, fake_substring)}")
    print(f"boyer moore, article 2 (fake): {time_comparison(boyer_moore.boyer_moore_search, content_2, fake_substring)}")

    print(f"rabin karp, article 1: {time_comparison(rabin_karp.rabin_karp_search, content_1, substring_1)}")
    print(f"rabin karp, article 2: {time_comparison(rabin_karp.rabin_karp_search, content_2, substring_2)}")
    print(f"rabin karp, article 1 (fake): {time_comparison(rabin_karp.rabin_karp_search, content_1, fake_substring)}")
    print(f"rabin karp, article 2 (fake): {time_comparison(rabin_karp.rabin_karp_search, content_2, fake_substring)}")

if __name__ == "__main__":
    main()