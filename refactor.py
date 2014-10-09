small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')

def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    #put it in a list
    lst_of_words = title.lower().split()

    #take length of list
    num_of_words = len(lst_of_words)
    if num_of_words < 1:
        return ''
    #new_title = lst_of_words.pop(0)
    #new_title = new_title[0].upper() + new_title[1:]
    
    list_of_words = lst_of_words[1:]
    lst_of_words = lst_of_words[0].capitalize()
    for i in range (len(list_of_words)):
        if small_words in list_of_words:
            list_of_words[i]=list_of_words[i].lower()
        else: 
            list_of_words[i]=list_of_words[i].capitalize()
    new_title = lst_of_words + list_of_words
    return str(new_title)
    

book_title('the WORKS OF AleXANDer dumas')


def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()