import operator

# region unchanged data
RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.-?!:;"
# ENDGLISH_ALPHABET = "abcdefghijklmnopqrstuvwxyz ,.-?!:;\"/"

RUSSIAN_REAL_PROBABILITIES = {'о': 0.10983, 'е': 0.08483, 'а': 0.07998, 'и': 0.07367, 'н': 0.06700,
                              'т': 0.06318, 'с': 0.05473, 'р': 0.04746, 'в': 0.04533, 'л': 0.04343,
                              'к': 0.03486, 'м': 0.03203, 'д': 0.02977, 'п': 0.02804, 'у': 0.02615,
                              'я': 0.02001, 'ы': 0.01898, 'ь': 0.01735, 'г': 0.01687, 'з': 0.01641,
                              'б': 0.01592, 'ч': 0.01450, 'й': 0.01208, 'х': 0.00966, 'ж': 0.00940,
                              'ш': 0.00718, 'ю': 0.00639, 'ц': 0.00486, 'щ': 0.00361, 'э': 0.00331,
                              'ф': 0.00267, 'ъ': 0.00037, 'ё': 0.00013}
# ',': , '.': , '-': , '?': , '!': , ':': , ';': }

ENDGLISH_REAL_PROBABILITIES = {'a': 0.0796, 'b': 0.0160, 'c': 0.0284, 'd': 0.0401, 'e': 0.1286,
                               'f': 0.0262, 'g': 0.0199, 'h': 0.0539, 'i': 0.0777, 'j': 0.0016,
                               'k': 0.0041, 'l': 0.0351, 'm': 0.0243, 'n': 0.0751, 'o': 0.0662,
                               'p': 0.0181, 'q': 0.0017, 'r': 0.0683, 's': 0.0662, 't': 0.0972,
                               'u': 0.0248, 'v': 0.0115, 'w': 0.0180, 'x': 0.0017, 'y': 0.0152,
                               'z': 0.0005}
# endregion unchanged data

# Config
ALPHABET_VARIANTS_LOG_FILE_NAME = 'alphabet_variants.log'
MESSAGE_VARIANTS_LOG = 'message_variants.log'

SPACE = ' '
PUNCTUATION_MARKS = [',', '.', '-', '?', '!', ':', ';']
ALPHABET = RUSSIAN_ALPHABET
ALPHABET_LEN = len(ALPHABET)
MAX_REAL_PROBABILITY = max(RUSSIAN_REAL_PROBABILITIES.values())
LENGTH_WORDS_NUMBER_TUPLES = [(4, 15), (5, 20), (6, 5)]

# ENCRYPTED_TEXT = "пкцхкдогта,-тгфоь-л,!вктоы-шкяо-шз-ы,ёш:о-шоё пштк,,-доцаб-ш!огщот кпш-ош-х-офш-бо-шсцатгш:пнщос-о-б!ь,-тк,гещолаохца,гуёщосцгкыаяотоь-,уко анотозкцкт,еоьобцашёъос-окх-оёбкюзк,гн щопа анояёфваноюгл,:об!яаозкцктк,пьанъо-,осцгкыаяошкскц:о,апяаюзаш:пно;ш-еоюгл,геоьобцашёъоь-,пша,шг,ояктг,об!яо-фк,:оцазщошк об-яккофш-о-,о,коюзаяоёюкото;ш-оякш-обцашао,гь-яанъо,-що,кп -шцно,аопт-еояеб-т:огоётаюк,гкоьопкцхкеогта,-тгфёщоь-,пша,шг,ёояктг,ёоб!я-отозкцкт,ко,кя-ть-опобцаш- ъок ёо,кя-ть-щозаюко,ксцгнш,-об!я-отгзкш:о-ш,-вк,гкобцашаоьозкцкт,къозяноь-,пша,шг,аояктг,аозкцкт,ноб!яао кпш-оюгл,гщош-окпш:оцаз-пшкдщопшцаза,гдщошцёзаиозянопкцхкногта,-тгфаозкцкт,ноб!яащопо-з,-допш-ц-,!що-шз!ыо-шошцёзащопозцёх-до–ос-якл,-косц-шгт-нзгкогпс-цфк,,-пшгщоь-ш-ц-ко-,осцг,г аяопоёз-т-я:пштгк огоп-л,а,гк окх-ос-я:л!ъозяноь-,пша,шг,аояктг,аозкцкт,ноб!яаошк оы-ц-ващофш-о-,аосцкзпшатяняаос-сцг.козяношцёзао,кп- ,к,,-ос-якл,-х-иозянопкцхкногта,-тгфаозкцкт,ноб!яао-п-бк,,-оы-ц-ваошк щофш-оша о -ю,-огоз-яю,-о,гфкх-о,козкяаш:ъоьц- кош-х-щого-ш,-вк,гкопкцхкногта,-тгфаоьо,ац-зёо,кпь-я:ь-оь-ц-бгя-оь-,пша,шг,аъопкцхкдогта,-тгфох-т-цгящофш-о-,ояебгшогол,акшо,ац-зщогофапш-обкпкз-таяопо ёюгьа гщофш-о-,оё кяозкяаш:оы-ц-в-що,косцгшт-цннп:ого,коя- анп:щогоглоьаюз-дошаь-добкпкз!от!т-згяо-б.гкоза,,!котос-я:лёо,ац-заоготоз-ьалашкя:пшт-щофш-ол,аяо;ш-шо,ац-зъошаь-ко-ш,-вк,гкоьо,ац-зёо,ко,цатгя-п:оь-,пша,шг,ёояктг,ёъозяноь-,пша,шг,ао,ац-зоб!яош-я:ь-охяат,!доёфапш,гьото-б.к ошцёзкщогщо,кп -шцно,аотпкоётаюк,гкогоьаьёерш-оьц-т,ёеояеб-т:оьо ёюгьёщотп-па,,ёеог щоьаьо-,опа ох-т-цгящоткц-нш,-щопо -я-ь- обаб!рь-ц гягу!що-,щоьаьоёфапш,гьопо,г ото-б.к озкякщог,-хзаосцгы-згтвгдотот-пыг.к,:ко-шопгя!щоьц-ш-пшгщопсцаткзягт-пшго;шгыояезкдщо-фк,:офапш-щоь-хзаото-б.к озкякошцкб-таягп:озцёхгкоьафкпштащосцгы-згяото-ля-бяк,гко,ао,ац-золаокх-обкпскф,-пш:що,кцнвягт-пш:щос:н,пшт-щоя-ю:ъоь-,пша,шг,ояктг,щокпягобоёо,кх-опсц-пгягщояебгшояго-,о,ац-зщоцквгшкя:,-о,кол,аяоб!щоьаьо,ао;ш-о-шткшгш:ъо-,ояебгяого,кояебгяо,ац-зошаьоюкщоьаьогот--б.кояезкдъоцалё ккшпнщоьаьоз-бц!дофкя-ткьщо-,об-я:вкояебгящофк о,кояебгяояезкдщоаос-ш- ёого,ац-зъо,-ояебгш:огяго,кояебгш:о,ац-зщоьаьофш-рш-о-п-бк,,-кщо-,о,ко -хщос-ш- ёофш-о,кош-я:ь-оюгяопо,ац-з- що,кош-я:ь-отпкокх-ог,шкцкп!об!ягоптнла,!опо,ац-з- що,-о-,опфгшаяогопа -х-опкбнофапш:ео,ац-защо,котгзкяотопкбкого,ац-зко,гьаьгыо"
# ENCRYPTED_TEXT = "ощлж9шсркс7ркгмь7п- 79килцё-79ш78ц-ё-5эь79шплч лж9л7пч15эь7к95шмшо9зс7г-и57л7йшч-мш77йшч-мэ79-3-щ7л3ш9э7азо5мл7щзош5эь79л7к95шмшо9зс7г-и57ч-ищ.3-ш5о17п75л ь735л7г- кщк17йшч-мэ7бшмшплёк5о17и-и7плщло-5зсь7к7я5л79ш78ёкпк5шщэ9ль75-и7и-и7шцл7бмшёикь7п7л5щк3кш7л57о- лцл7к бшм-5лм-ь7ощ-пкщкоэ7л5щк39лс7плщло-5ло5э.х"
# ENCRYPTED_TEXT = ".!?йэчщфчэ!?чщ?вщйв-вё!?чэ?гы?ч-йэиа?чщ?павх-спмщёщ? ёэё?фъпёэг?ёщйвё!?в-ъ?вээбцщч-щ?;?.?мгщпщч?;?ч-йэина?чщ?бмнщё?павх-спэгачэе"
ENCRYPTED_TEXT = "Бтсвбр ел ибвн анжмс, Гвлъ ел бтсвбрн тсбмс Т залсбгалрыим цнвкрлим, Т снвнилим ъл тлълим; Наь влтснс пнвнъ ърбвцби, Л пбъ енй хвутслаьеый ъби; Онакл сли жмрнс вучелд, Ъл злснйемцл клклд! Онакл пнтнекм пбнс Ъл бвншкм ртн гвызнс, Л бвншкм ен пвбтсын, Ртн ткбваупкм збабсын"


def encrypt(message, new_alphabet):
    message = message.lower()
    encrypted_message = ""

    for letter in message:
        letter_index = ALPHABET.find(letter)
        if letter_index == -1:
            encrypted_message += letter
        else:
            encrypted_letter = new_alphabet[letter_index]
            encrypted_message += encrypted_letter

    return encrypted_message


def decrypt(message, new_alphabet):
    decrypted_message = ""

    for encrypted_letter in message:
        decrypted_letter = ALPHABET[new_alphabet.index(encrypted_letter)]
        decrypted_message += decrypted_letter

    return decrypted_message


def build_new_alphabet(key):
    new_alphabet = [None] * ALPHABET_LEN
    for letter in ALPHABET:
        letter_index = ALPHABET.index(letter)
        new_index = letter_index ** key % ALPHABET_LEN
        while not new_alphabet[new_index] is None:
            new_index = (new_index + 1) % ALPHABET_LEN
        new_alphabet[new_index] = letter
    return new_alphabet


# region BUILD AND SAVE VARIANTS
def build_and_save_variants(cryptogram):
    cryptogram = cryptogram.lower()
    statistical_letter_occurrences = build_letter_occurrence_statistics(cryptogram)
    cryptogram = fix_cryptogram_spaces_and_punctuation(cryptogram, statistical_letter_occurrences)
    statistical_letter_occurrences = build_letter_occurrence_statistics(cryptogram)
    letter_substitution_variants =\
        build_letters_substitution_variants(statistical_letter_occurrences)

    words_variants = build_words_variants(cryptogram, letter_substitution_variants,
                                          LENGTH_WORDS_NUMBER_TUPLES)

    alphabet_variants = build_alphabet_variants(words_variants)
    print_hacked_alternatives(cryptogram, alphabet_variants)
    print("\n\nFINISH")


def fix_cryptogram_spaces_and_punctuation(cryptogram, statistical_letter_occurrences):
    letters_in_statistics = len(statistical_letter_occurrences)
    most_common_letter = statistical_letter_occurrences[letters_in_statistics - 1][0]
    cryptogram = substitute_with_spaces(cryptogram, most_common_letter)
    for punctuation_mark in PUNCTUATION_MARKS:
        cryptogram = cryptogram.replace(punctuation_mark, '')
    return cryptogram


def build_words_variants(cryptogram, letter_substitution_variants, length_words_number_tuples):
    result_words_variants = []
    for length_words_number_tuple in length_words_number_tuples:
        cur_words_variants = build_words_variants_particular_length(cryptogram,
                                                                    letter_substitution_variants,
                                                                    length_words_number_tuple[0],
                                                                    length_words_number_tuple[1])
        result_words_variants += cur_words_variants
    return result_words_variants


def build_words_variants_particular_length(cryptogram, letter_substitution_variants,
                                           letters_in_word, words_to_return):
    print("build_words_variants_particular_length().letters_in_word==>" + str(letters_in_word) +
          " words_to_return==>" + str(words_to_return))
    all_unreal_words = obtain_words_by_length(cryptogram, letters_in_word)
    print("build_words_variants_particular_length().all_unreal_words==>" + str(len(all_unreal_words)))
    # too many
    unreal_words = all_unreal_words[:words_to_return]
    real_words = load_real_words_by_length(letters_in_word)
    return build_words_substitution_variants(unreal_words, real_words, letter_substitution_variants)


def build_letter_occurrence_statistics(cryptogram):
    cryptogram_len = len(cryptogram)
    met_letters_counters = count_letters_occurrences(cryptogram)

    letter_occurrence_statistics = {}
    for cur_letter in met_letters_counters:
        cur_letter_counter = met_letters_counters.get(cur_letter, 0)
        cur_letter_occurrence = cur_letter_counter / cryptogram_len
        letter_occurrence_statistics[cur_letter] = cur_letter_occurrence

    letter_occurrence_statistics = sort_occurrence_statistics_by_values(letter_occurrence_statistics)
    return letter_occurrence_statistics


def count_letters_occurrences(text):
    met_letters_counter = {}
    for letter in text:
        cur_letter_counter = met_letters_counter.get(letter, 0)
        met_letters_counter[letter] = cur_letter_counter + 1
    return met_letters_counter


def substitute_with_spaces(message, letter_to_substitute):
    space = SPACE
    result_text = ""

    for letter in message:
        if letter == letter_to_substitute:
            result_text += space
        elif letter == space:
            result_text += letter_to_substitute
        else:
            result_text += letter

    return result_text


def build_letters_substitution_variants(letters_probabilities):
    real_probabilities = RUSSIAN_REAL_PROBABILITIES

    letter_variants_list = []
    for cur_tuple in letters_probabilities:
        cur_letter = cur_tuple[0]
        cur_probability = cur_tuple[1]

        percentage_window = ((cur_probability * 100) ** (1/2)) / 100
        min_probability = max(0, cur_probability - percentage_window)
        max_probability = min(cur_probability + percentage_window, MAX_REAL_PROBABILITY)
        available_letters = [letter for letter in real_probabilities
                             if min_probability <= real_probabilities[letter] <= max_probability]
        letter_variants_list.append((cur_letter, available_letters))
    return dict(letter_variants_list)


def sort_occurrence_statistics_by_values(dictionary):
    return sorted(dictionary.items(), key=operator.itemgetter(1))


def obtain_words_by_length(cryptogram, words_len):
    all_words = cryptogram.split(SPACE)
    result_words = []

    for cur_word in all_words:
        cur_word_len = len(cur_word)
        if cur_word_len == words_len:
            result_words.append(cur_word)

    return list(set(result_words))


# TODO Refactor me.
def generate_all_letter_conversion_dictionaries(unreal_word, letter_variants):
    unique_word_letters = list(set(unreal_word))
    unique_word_letters_number = len(unique_word_letters)

    variants_number = []
    for i in range(0, unique_word_letters_number):
        cur_letter = unique_word_letters[i]
        cur_letter_variants = letter_variants[cur_letter]
        variants_number.append(len(cur_letter_variants))

    # generate all indexes combinations
    cur_digit_combinations = []
    cur_digit_combinations.append([])
    for i in range(0, unique_word_letters_number):
        new_cur_digit_combinations = []
        for j in range(0, variants_number[i]):
            for cur_digit_combination in cur_digit_combinations:
                temp = cur_digit_combination[:]
                temp.append(j)
                new_cur_digit_combinations.append(temp)
        cur_digit_combinations = new_cur_digit_combinations
    all_indexes_combinations = cur_digit_combinations

    letter_conversion_dictionaries = []
    for cur_indexes_combination in all_indexes_combinations:
        # generate one conversion dictionary
        cur_conversion_dict = {}
        for i in range(0, unique_word_letters_number):
            cur_letter_cur_index = cur_indexes_combination[i]
            cur_unique_letter = unique_word_letters[i]
            unreal_letter_variants = letter_variants[cur_unique_letter]
            cur_conversion_dict[cur_unique_letter] = unreal_letter_variants[cur_letter_cur_index]
        # validate and append generated dictionary
        dict_values = list(cur_conversion_dict.values())
        unique_dict_values = set(cur_conversion_dict.values())
        if len(dict_values) == len(unique_dict_values):
            letter_conversion_dictionaries.append(cur_conversion_dict)

    return letter_conversion_dictionaries


# region files
def load_real_words_by_length(words_len):
    file_name = str(words_len) + '.txt'
    return load_words_from_file(file_name)


def load_words_from_file(file_name):
    file = open(file_name, 'r')

    read_data = file.read()
    read_words = read_data.split('\n')

    file.close()
    return read_words


def overwrite_file(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()


def read_entire_file(file_name):
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()
    return file_content
# endregion files


# region Build words substitution variants
def build_words_substitution_variants(all_unreal_words, dictionary_words, letter_variants_dict):
    print("build_words_substitution_variants().unreal_words len==>" + str(len(all_unreal_words)))
    words_variants = []
    words_variants_counter = 0
    for unreal_word in all_unreal_words:
        all_letter_conversion_dictionaries \
            = generate_all_letter_conversion_dictionaries(unreal_word, letter_variants_dict)

        all_possible_words = generate_all_possible_words(unreal_word, all_letter_conversion_dictionaries)
        all_possible_matching_real_words = filter_real_words(all_possible_words, dictionary_words)

        word_variants = (unreal_word, all_possible_matching_real_words)
        words_variants.append(word_variants)
        # log
        print('unreal word #' + str(words_variants_counter) + '/' + str(len(all_unreal_words)) + ':')
        print(word_variants)
        print('real variants==>' + str(len(word_variants[1])))
        words_variants_counter += 1

    return words_variants


def generate_all_possible_words(unreal_word, all_letter_conversion_dictionaries):
    all_possible_words = []
    for conversion_dict in all_letter_conversion_dictionaries:
        possible_word = ''
        for unreal_letter in unreal_word:
            possible_word += conversion_dict[unreal_letter]
        all_possible_words.append(possible_word)

    return all_possible_words


def filter_real_words(unreal_words, real_words):
    result_words = []

    for unreal_word in unreal_words:
        for real_word in real_words:
            if unreal_word == real_word:
                result_words.append(unreal_word)
                break

    return result_words
# endregion Build words substitution variants


# region build_alphabet_variants
# TODO Refactor me.
def build_alphabet_variants(words_variants):
    sorted_words_variants = []
    print('\nsorted_words_variants==>')
    for key, value in sorted(words_variants, key=my_compare_func):
        sorted_words_variants.append((key, value))
        print(key + " " + str(len(value)))
    print('\n')

    first_tuple = sorted_words_variants[0]
    first_word = first_tuple[0]
    first_word_variants = first_tuple[1]
    branches = build_one_word_branches(first_word, first_word_variants)

    for i in range(1, len(sorted_words_variants)):
        cur_tuple = sorted_words_variants[i]
        cur_word = cur_tuple[0]
        cur_word_variants = cur_tuple[1]

        new_word_branches = build_one_word_branches(cur_word, cur_word_variants)
        if len(new_word_branches) == 0:
            continue
        result_branches = update_branches_lists(branches, new_word_branches)
        if len(result_branches) > 0:
            branches = result_branches

    # each branch is a key-alphabet candidate!
    return branches


def my_compare_func(a):
    return len(a[1])


def build_one_word_branches(word, word_variants):
    branches = []
    for word_variant in word_variants:
        branch = {}
        for i in range(0, len(word)):
            key = word[i]
            value = word_variant[i]
            branch[key] = value
        branches.append(branch)
    return branches


def update_branches_lists(branches, new_branches):
    # each branch and each choice is a letter-to-letter dictionary
    print('merge_branches_with_new_choices().branches==>' + str(len(branches)) +
          ' new_choices==>' + str(len(new_branches)))

    if len(branches) == 0:
        return new_branches
    elif len(new_branches) == 0:
        return branches
    else:
        return merge_branches_lists(branches, new_branches)


def merge_branches_lists(branches, new_branches):
    result_branches = []
    for cur_branch in branches:
        for cur_new_branch in new_branches:
            merged_branch = merge_two_branches(cur_branch, cur_new_branch)
            if merged_branch is not None:
                result_branches.append(merged_branch)

    print('intersect_branches().result_branches==>' + str(len(result_branches)))
    return result_branches


def merge_two_branches(branch_1, branch_2):
    for entrance in branch_1:
        value_1 = branch_1[entrance]
        try:
            value_2 = branch_2[entrance]
            if value_1 != value_2:
                # Branches conflict with each other.
                return None
        except KeyError:
            continue

    # Branches are not contrary to one another.
    result_branch = branch_1.copy()
    result_branch.update(branch_2)
    return result_branch
# endregion build_alphabet_variants


def print_hacked_alternatives(cryptogram, alphabet_variants):
    alphabet_variants_len = len(alphabet_variants)
    print("print_hacked_alternatives().alphabet_variants len==>" + str(alphabet_variants_len) + "\n")
    overwrite_file(ALPHABET_VARIANTS_LOG_FILE_NAME, str(alphabet_variants))
    counter = 0
    for alphabet_variant in alphabet_variants:
        # print(alphabet_variant)
        hacked_text = ""
        for unreal_letter in cryptogram:
            if unreal_letter != SPACE:
                try:
                    real_letter = alphabet_variant[unreal_letter]
                    hacked_text += real_letter
                except KeyError:
                    hacked_text += "_"
            else:
                hacked_text += SPACE
        print('(' + str(counter) + '/' + str(alphabet_variants_len) + ')' + hacked_text)
        counter += 1
# endregion BUILD AND SAVE VARIANTS


# region interactive improvement
def run_interactive_improvement(cryptogram):
    cryptogram = cryptogram.lower()
    statistical_letter_occurrences = build_letter_occurrence_statistics(cryptogram)
    cryptogram = fix_cryptogram_spaces_and_punctuation(cryptogram, statistical_letter_occurrences)
    print("cryptogram length==>" + str(len(cryptogram)))

    message_variants = read_message_variants_from_log_file()
    letters_substitution_variants = build_possible_letters_substitution_dictionaries(
        cryptogram, message_variants)
    print_hacked_alternatives(cryptogram, letters_substitution_variants)

    while 1:
        do_interactive_improvement_iteration(cryptogram, letters_substitution_variants)


def do_interactive_improvement_iteration(cryptogram, letters_substitution_variants):
    position, user_letter = read_user_position_and_letter()
    cryptogram_letter = cryptogram[position]

    new_letters_substitution_variants = substitute_initial_letter_with_user_letter(
        letters_substitution_variants, cryptogram_letter, user_letter)

    if len(new_letters_substitution_variants) == 0:
        for letters_substitution_variant in letters_substitution_variants:
            letters_substitution_variant[cryptogram_letter] = user_letter
    else:
        letters_substitution_variants = new_letters_substitution_variants

    print_hacked_alternatives(cryptogram, letters_substitution_variants)


def substitute_initial_letter_with_user_letter(letters_substitution_variants,
                                               cryptogram_letter,
                                               user_letter):
    new_letters_substitution_variants = []
    for letters_substitution_variant in letters_substitution_variants:
        try:
            if letters_substitution_variant[cryptogram_letter] == user_letter:
                new_letters_substitution_variants.append(letters_substitution_variant)
        except KeyError:
            pass
    return new_letters_substitution_variants


def read_user_position_and_letter():
    user_input = input()
    parameters = user_input.split(' ')
    position = int(parameters[0])
    letter = parameters[1]
    return position, letter


def read_message_variants_from_log_file():
    message_variants_log = read_entire_file(MESSAGE_VARIANTS_LOG)
    message_variants = message_variants_log.split('\n')
    # Last string in log is empty.
    message_variants = message_variants[:len(message_variants) - 1]
    print("read message variants==>" + str(len(message_variants)))
    return message_variants


def build_possible_letters_substitution_dictionaries(cryptogram, message_variants):
    possible_letters_substitutions = []
    for message_variant in message_variants:
        message_variant = message_variant[
                          message_variant.index(')') + 1: len(message_variant) - 1]
        letters_substitution_dict = {}
        for i in range(len(message_variant)):
            initial_letter = cryptogram[i]
            alternative_letter = message_variant[i]

            letters_substitution_dict[initial_letter] = alternative_letter
        possible_letters_substitutions.append(letters_substitution_dict)
    return possible_letters_substitutions
# endregion interactive improvement


def main(cryptogram):
    build_and_save_variants(cryptogram)
    run_interactive_improvement(cryptogram)


# main(ENCRYPTED_TEXT)

build_and_save_variants(ENCRYPTED_TEXT)
# run_interactive_improvement(ENCRYPTED_TEXT)
