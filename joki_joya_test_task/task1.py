def first_non_repeating_letter(s: str) -> str:
    letter_count: dict = {}
    for letter in s:
        lower_letter: str = letter.lower()
        if lower_letter in letter_count:
            letter_count[lower_letter]['qty'] += 1
        else:
            letter_count[lower_letter] = {}
            letter_count[lower_letter]['qty'] = 1
            letter_count[lower_letter]['original'] = letter

    for letter in letter_count.items():
        if letter[1]['qty'] == 1:
            return letter[1]['original']
    return ''


if __name__ == '__main__':
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'
    assert first_non_repeating_letter('') == ''
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('hello world, eh?') == 'w'
    assert first_non_repeating_letter('sTreSS') == 'T'
    assert first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') == ','
