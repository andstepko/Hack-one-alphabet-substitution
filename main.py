import operator

ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.-?!:;"
SPACE = ' '
LEN = len(ALPHABET)

CRYPTED_TEXT = "пкцхкдогта,-тгфоь-л,!вктоы-шкяо-шз-ы,ёш:о-шоё пштк,,-доцаб-ш!огщот кпш-ош-х-офш-бо-шсцатгш:пнщос-о-б!ь,-тк,гещолаохца,гуёщосцгкыаяотоь-,уко анотозкцкт,еоьобцашёъос-окх-оёбкюзк,гн щопа анояёфваноюгл,:об!яаозкцктк,пьанъо-,осцгкыаяошкскц:о,апяаюзаш:пно;ш-еоюгл,геоьобцашёъоь-,пша,шг,ояктг,об!яо-фк,:оцазщошк об-яккофш-о-,о,коюзаяоёюкото;ш-оякш-обцашао,гь-яанъо,-що,кп -шцно,аопт-еояеб-т:огоётаюк,гкоьопкцхкеогта,-тгфёщоь-,пша,шг,ёояктг,ёоб!я-отозкцкт,ко,кя-ть-опобцаш- ъок ёо,кя-ть-щозаюко,ксцгнш,-об!я-отгзкш:о-ш,-вк,гкобцашаоьозкцкт,къозяноь-,пша,шг,аояктг,аозкцкт,ноб!яао кпш-оюгл,гщош-окпш:оцаз-пшкдщопшцаза,гдщошцёзаиозянопкцхкногта,-тгфаозкцкт,ноб!яащопо-з,-допш-ц-,!що-шз!ыо-шошцёзащопозцёх-до–ос-якл,-косц-шгт-нзгкогпс-цфк,,-пшгщоь-ш-ц-ко-,осцг,г аяопоёз-т-я:пштгк огоп-л,а,гк окх-ос-я:л!ъозяноь-,пша,шг,аояктг,аозкцкт,ноб!яаошк оы-ц-ващофш-о-,аосцкзпшатяняаос-сцг.козяношцёзао,кп- ,к,,-ос-якл,-х-иозянопкцхкногта,-тгфаозкцкт,ноб!яао-п-бк,,-оы-ц-ваошк щофш-оша о -ю,-огоз-яю,-о,гфкх-о,козкяаш:ъоьц- кош-х-щого-ш,-вк,гкопкцхкногта,-тгфаоьо,ац-зёо,кпь-я:ь-оь-ц-бгя-оь-,пша,шг,аъопкцхкдогта,-тгфох-т-цгящофш-о-,ояебгшогол,акшо,ац-зщогофапш-обкпкз-таяопо ёюгьа гщофш-о-,оё кяозкяаш:оы-ц-в-що,косцгшт-цннп:ого,коя- анп:щогоглоьаюз-дошаь-добкпкз!от!т-згяо-б.гкоза,,!котос-я:лёо,ац-заоготоз-ьалашкя:пшт-щофш-ол,аяо;ш-шо,ац-зъошаь-ко-ш,-вк,гкоьо,ац-зёо,ко,цатгя-п:оь-,пша,шг,ёояктг,ёъозяноь-,пша,шг,ао,ац-зоб!яош-я:ь-охяат,!доёфапш,гьото-б.к ошцёзкщогщо,кп -шцно,аотпкоётаюк,гкогоьаьёерш-оьц-т,ёеояеб-т:оьо ёюгьёщотп-па,,ёеог щоьаьо-,опа ох-т-цгящоткц-нш,-щопо -я-ь- обаб!рь-ц гягу!що-,щоьаьоёфапш,гьопо,г ото-б.к озкякщог,-хзаосцгы-згтвгдотот-пыг.к,:ко-шопгя!щоьц-ш-пшгщопсцаткзягт-пшго;шгыояезкдщо-фк,:офапш-щоь-хзаото-б.к озкякошцкб-таягп:озцёхгкоьафкпштащосцгы-згяото-ля-бяк,гко,ао,ац-золаокх-обкпскф,-пш:що,кцнвягт-пш:щос:н,пшт-щоя-ю:ъоь-,пша,шг,ояктг,щокпягобоёо,кх-опсц-пгягщояебгшояго-,о,ац-зщоцквгшкя:,-о,кол,аяоб!щоьаьо,ао;ш-о-шткшгш:ъо-,ояебгяого,кояебгяо,ац-зошаьоюкщоьаьогот--б.кояезкдъоцалё ккшпнщоьаьоз-бц!дофкя-ткьщо-,об-я:вкояебгящофк о,кояебгяояезкдщоаос-ш- ёого,ац-зъо,-ояебгш:огяго,кояебгш:о,ац-зщоьаьофш-рш-о-п-бк,,-кщо-,о,ко -хщос-ш- ёофш-о,кош-я:ь-оюгяопо,ац-з- що,кош-я:ь-отпкокх-ог,шкцкп!об!ягоптнла,!опо,ац-з- що,-о-,опфгшаяогопа -х-опкбнофапш:ео,ац-защо,котгзкяотопкбкого,ац-зко,гьаьгыо"

CRYPTOGRAM = "ощлж9шсркс7ркгмь7п- 79килцё-79ш78ц-ё-5эь79шплч лж9л7пч15эь7к95шмшо9зс7г-и57л7йшч-мш77йшч-мэ79-3-щ7л3ш9э7азо5мл7щзош5эь79л7к95шмшо9зс7г-и57ч-ищ.3-ш5о17п75л ь735л7г- кщк17йшч-мэ7бшмшплёк5о17и-и7плщло-5зсь7к7я5л79ш78ёкпк5шщэ9ль75-и7и-и7шцл7бмшёикь7п7л5щк3кш7л57о- лцл7к бшм-5лм-ь7ощ-пкщкоэ7л5щк39лс7плщло-5ло5э.х"
MY_CRYPTOGRAM = ".!?йэчщфчэ!?чщ?вщйв-вё!?чэ?гы?ч-йэиа?чщ?павх-спмщёщ? ёэё?фъпёэг?ёщйвё!?в-ъ?вээбцщч-щ?;?.?мгщпщч?;?ч-йэина?чщ?бмнщё?павх-спэгачэе"
REAL_PROBABILITIES = {'о': 0.10983, 'е': 0.08483, 'а': 0.07998, 'и': 0.07367, 'н': 0.06700,
                      'т': 0.06318, 'с': 0.05473, 'р': 0.04746, 'в': 0.04533, 'л': 0.04343,
                      'к': 0.03486, 'м': 0.03203, 'д': 0.02977, 'п': 0.02804, 'у': 0.02615,
                      'я': 0.02001, 'ы': 0.01898, 'ь': 0.01735, 'г': 0.01687, 'з': 0.01641,
                      'б': 0.01592, 'ч': 0.01450, 'й': 0.01208, 'х': 0.00966, 'ж': 0.00940,
                      'ш': 0.00718, 'ю': 0.00639, 'ц': 0.00486, 'щ': 0.00361, 'э': 0.00331,
                      'ф': 0.00267, 'ъ': 0.00037, 'ё': 0.00013}
# ',': , '.': , '-': , '?': , '!': , ':': , ';': }

MAX_REAL_PROBABILITY = max(REAL_PROBABILITIES.values())

DICTIONARY_FILE_NAME = "litw-win_utf.txt"


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
    new_alphabet = [None] * LEN
    for letter in ALPHABET:
        letter_index = ALPHABET.index(letter)
        new_index = letter_index ** key % LEN
        while not new_alphabet[new_index] is None:
            new_index = (new_index + 1) % LEN
        new_alphabet[new_index] = letter
    return new_alphabet


# region HACK
def hack(cryptogram):
    cryptogram = cryptogram.lower()

    cryptogram_letter_probabilities = build_probabilities_list(cryptogram)

    cryptogram = exchange_with_spaces(cryptogram,
                                      cryptogram_letter_probabilities[len(cryptogram_letter_probabilities) - 1][0])
    cryptogram_letter_probabilities = build_probabilities_list(cryptogram)

    letter_variants_dict = build_letter_variants(cryptogram_letter_probabilities)
    # for cur_letter in letter_variants_dict:
    #     print(cur_letter + " ==>" + str(letter_variants_dict[cur_letter]))

    dict_words_len_4 = 4
    all_unreal_words_4 = find_all_unreal_words(cryptogram, dict_words_len_4)
    # too many
    all_unreal_words_4 = all_unreal_words_4[:10]
    dictionary_words_4 = load_words_particular_length_from_file(dict_words_len_4)

    dict_words_len_5 = 5
    all_unreal_words_5 = find_all_unreal_words(cryptogram, dict_words_len_5)
    # # too many
    all_unreal_words_5 = all_unreal_words_5[:10]
    dictionary_words_5 = load_words_particular_length_from_file(dict_words_len_5)

    words_variants_4 = build_words_variants(all_unreal_words_4, dictionary_words_4, letter_variants_dict)
    words_variants_5 = build_words_variants(all_unreal_words_5, dictionary_words_5, letter_variants_dict)

    alphabet_variants = build_alphabet_variants(words_variants_4 + words_variants_5)

    print_hacked_alternatives(cryptogram, alphabet_variants)
    print("\n\nFINISH")


def build_probabilities_list(cryptogram):
    cryptogram_len = len(cryptogram)
    letters_count = {}
    for letter in cryptogram:
        cur_counter = letters_count.get(letter, 0)
        letters_count[letter] = cur_counter + 1

    letter_probabilities = {}
    for cur_letter in letters_count:
        cur_letter_count = letters_count.get(cur_letter, 0)
        cur_letter_probability = cur_letter_count / cryptogram_len
        letter_probabilities[cur_letter] = cur_letter_probability

    letter_probabilities = sort_by_values(letter_probabilities)
    return letter_probabilities


def exchange_with_spaces(cryptogram, letter_to_exchange):
    space = SPACE
    result_text = ""

    for letter in cryptogram:
        if letter == letter_to_exchange:
            result_text += space
        elif letter == space:
            result_text += letter_to_exchange
        else:
            result_text += letter

    return result_text


def build_letter_variants(probability_list):
    real_probabilities = REAL_PROBABILITIES

    letter_variants_list = []
    for cur_tuple in probability_list:
        cur_letter = cur_tuple[0]
        cur_probability = cur_tuple[1]
        percentage_window = ((cur_probability * 100) ** (1/2)) / 100
        cur_min_probability = max(0, cur_probability - percentage_window)
        cur_max_probability = min(cur_probability + percentage_window, MAX_REAL_PROBABILITY)
        available_letters = [letter for letter in real_probabilities
                             if cur_min_probability <= real_probabilities[letter] <= cur_max_probability]
        letter_variants_list.append((cur_letter, available_letters))
    return dict(letter_variants_list)


def sort_by_values(dictionary):
    return sorted(dictionary.items(), key=operator.itemgetter(1))


def find_all_unreal_words(cryptogram, dict_words_len):
    all_words = cryptogram.split(SPACE)
    result_words = []

    for cur_word in all_words:
        cur_word_len = len(cur_word)
        if cur_word_len == dict_words_len: # or cur_word_len == dict_words_len + 1:
            result_words.append(cur_word)

    return list(set(result_words))


def generate_all_letter_conversion_dictionaries(unreal_word, letter_variants):
    unique_letters = list(set(unreal_word))
    unique_letters_number = len(unique_letters)

    variants_number = []
    for i in range(0, unique_letters_number):
        cur_letter = unique_letters[i]
        cur_letter_variants = letter_variants[cur_letter]
        variants_number.append(len(cur_letter_variants))

    # generate all indexes combinations
    cur_digit_combinations = []
    cur_digit_combinations.append([])
    for i in range(0, unique_letters_number):
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
        for i in range(0, unique_letters_number):
            cur_letter_cur_index = cur_indexes_combination[i]
            cur_unique_letter = unique_letters[i]
            unreal_letter_variants = letter_variants[cur_unique_letter]
            cur_conversion_dict[cur_unique_letter] = unreal_letter_variants[cur_letter_cur_index]
        # validate and append generated dictionary
        dict_values = list(cur_conversion_dict.values())
        unique_dict_values = set(cur_conversion_dict.values())
        if len(dict_values) == len(unique_dict_values):
            letter_conversion_dictionaries.append(cur_conversion_dict)

    return letter_conversion_dictionaries


def generate_all_possible_words(unreal_word, all_letter_conversion_dictionaries):
    all_possible_words = []
    for conversion_dict in all_letter_conversion_dictionaries:
        possible_word = ''
        for unreal_letter in unreal_word:
            possible_word += conversion_dict[unreal_letter]
        all_possible_words.append(possible_word)

    return all_possible_words


def which_real_word_matches(unreal_words, real_words):
    real_words_matching = []

    for real_word in real_words:
        for unreal_word in unreal_words:
            if unreal_word == real_word:
                real_words_matching.append(real_word)
                # print(real_word)

    return real_words_matching


# region files
def load_words_particular_length_from_file(words_len):
    file_name = str(words_len) + '.txt'
    return load_words_from_file(file_name)


def load_words_from_file(file_name):
    file = open(file_name, 'r')

    read_data = file.read()
    read_words = read_data.split('\n')

    file.close()
    return read_words


def print_text_to_file(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()
# endregion files


def build_words_variants(all_unreal_words, dictionary_words, letter_variants_dict):
    print("build_words_variants().unreal_words len==>" + str(len(all_unreal_words)))
    words_variants = []
    counter = 0
    for unreal_word in all_unreal_words:
        all_letter_conversion_dictionaries \
            = generate_all_letter_conversion_dictionaries(unreal_word, letter_variants_dict)
        all_possible_words = generate_all_possible_words(unreal_word, all_letter_conversion_dictionaries)

        real_word_matching = which_real_word_matches(all_possible_words, dictionary_words)

        adding_tuple = (unreal_word, real_word_matching)
        words_variants.append(adding_tuple)
        print(str(counter) + ')')
        counter += 1
        print(adding_tuple)
        print(len(adding_tuple[1]))

    return words_variants

    # words_variants = []
    # words_variants.append(('ш-х-', ['того', 'тебе', 'себе', 'кого', 'раза', 'ваша', 'наша', 'небе', 'саша', 'реже', 'нача', 'даша', 'раба', 'дача', 'маша', 'риги', 'собо', 'вече', 'тиши', 'каша', 'неге', 'таща', 'каза', 'ребе', 'нече', 'сажа', 'маха', 'наза', 'ного', 'рого', 'дичи', 'дохо', 'тихи', 'визи', 'каба', 'лебе', 'мага', 'миши', 'рече', 'тобо', 'ваза', 'кача', 'нищи', 'реше', 'теще', 'виши', 'возо', 'деше', 'лаза', 'лиши', 'мехе', 'мого', 'рафа', 'рихи', 'розо', 'саха', 'таба', 'тече', 'веге', 'каца', 'лиги', 'лизи', 'лобо', 'мебе', 'меге', 'мифи', 'ниги', 'ничи', 'ниши', 'ножо', 'резе', 'робо', 'сече', 'таза']))
    # words_variants.append(('фш-б', ['чтоб', 'этом', 'этой', 'этих', 'этим', 'глаз', 'чрез', 'зная', 'этак', 'грех', 'юлия', 'хлеб', 'знак', 'гроб', 'близ', 'бред', 'злой', 'знай', 'брак', 'фрак', 'гром', 'злая', 'этаж', 'экой', 'благ', 'экая', 'штаб', 'эдак', 'храм', 'змея', 'этог', 'юрий', 'змей', 'фраз', 'хлоп', 'град', 'грек', 'злом', 'знач', 'зноя', 'юной', 'чтой', 'брем', 'грез', 'зной', 'швам', 'блед', 'ждем', 'храп', 'ядом', 'гроз', 'злоб', 'змий', 'блик', 'звой', 'хром', 'шкап', 'эдип', 'грач', 'греб', 'хлам', 'хрип', 'швей', 'шлем', 'шрам', 'эдем', 'юная', 'ямой', 'гриб', 'фрау', 'фрид', 'хлиб', 'ямах', 'блаж', 'ближ', 'блох', 'гной', 'греч', 'грея', 'злоп', 'зрим', 'флаг', 'флам', 'швах', 'швед', 'швея', 'этап', 'юлий', 'юрой', 'яком', 'блаз', 'блок', 'браг', 'брам', 'брач', 'брех', 'бром', 'гвоз', 'глох', 'гном', 'граб', 'граж', 'грам', 'грем', 'грим', 'злак', 'злей', 'злод', 'хлад', 'хлой', 'храб', 'хрия', 'цвей', 'чмок', 'чтим', 'шмак', 'экип', 'юрия', 'явим', 'явок', 'ядим', 'який', 'якоб', 'якой', 'ялик', 'ярем', 'ярок', 'яток']))
    # words_variants.append(('б!яа', ['была', 'были', 'пяти', 'ушла', 'уйти', 'угла', 'пыли', 'ушли', 'дыма', 'мысл', 'мыла', 'быва', 'быка', 'бэла', 'бюст', 'быта', 'уйди', 'мяса', 'ушки', 'пятн', 'быки', 'угли', 'язва', 'жгут', 'мэра', 'быст', 'быти', 'дыра', 'мыли', 'мыса', 'пята', 'узла', 'жгла', 'жгли', 'мгла', 'бяда', 'ужли', 'узки', 'учка', 'жгун', 'мяла', 'мяли', 'мясн', 'пшла', 'пырс', 'пяди', 'убла', 'убра', 'узда', 'учла', 'ушми', 'уюта']))
    # words_variants.append((';ш-е', ['этой', 'этих', 'этою', 'этаж', 'экой', 'этог', 'юрий', 'фраз', 'юной', 'флаг', 'юлий', 'юрой', 'цвей', 'юнош']))
    # words_variants.append(('цазщ', ['друг', 'двух', 'силы', 'виду', 'дамы', 'видя', 'саду', 'разу', 'сидя', 'силу', 'стыд', 'стук', 'слух', 'днях', 'круг', 'вряд', 'миру', 'рады', 'всяк', 'лизу', 'дачу', 'кабы', 'дабы', 'дням', 'двум', 'даму', 'даль', 'пруд', 'лизы', 'княз', 'пару', 'варя', 'парк', 'случ', 'малу', 'слуг', 'лапы', 'самы', 'марк', 'вазы', 'дичь', 'крым', 'разд', 'сады', 'пары', 'разг', 'прям', 'виды', 'визг', 'милы', 'клуб', 'пику', 'рамы', 'служ', 'разб', 'улыб', 'паук', 'раму', 'услы', 'дары', 'валу', 'маль', 'паду', 'скуп', 'даву', 'друж', 'кары', 'паль', 'разы', 'силь', 'скуч', 'вазу', 'круп', 'ладу', 'рабы', 'малы', 'палк', 'рагу', 'давя', 'карм', 'лапу', 'липы', 'миль', 'плуг', 'прыг', 'скры', 'сруб', 'друз', 'кипя', 'лады', 'ламп', 'липу', 'пиру', 'разм', 'ригу', 'связ', 'сичь', 'слых', 'ярый', 'вспы', 'карп', 'карь', 'круж', 'лиду', 'раду', 'ризу', 'ризы', 'саму', 'валы', 'внук', 'киль', 'кляч', 'маку', 'памя', 'пиль', 'стру', 'явку', 'вапы', 'вслу', 'диву', 'капу', 'кипу', 'лары', 'ларь', 'лиды', 'лиры', 'маяк', 'милу', 'миры', 'пауз', 'пилу', 'пиры', 'рабу', 'ступ', 'стуч', 'увяз', 'вакх', 'валь', 'валя', 'вару', 'варь', 'визу', 'вилы', 'виль', 'виля', 'вспя', 'даля', 'дару', 'дарь', 'друк', 'дрых', 'каву', 'кадь', 'кард', 'кару', 'кипы', 'кляу', 'княж', 'кряж', 'лавк', 'лавы', 'ламы', 'лапк', 'ларя', 'ливм', 'лику', 'лиму', 'лимы', 'лиру', 'лруг', 'мазь', 'марь', 'паву', 'павы', 'падь', 'пазы', 'паля', 'пачк', 'паях', 'пидж', 'пряч', 'разя', 'риму', 'свык', 'сизы', 'сияй', 'скря', 'скуд', 'сряд', 'ству', 'стры', 'стря', 'стуж', 'уряд', 'ятку']))
    # return words_variants


# region build_alphabet_variants
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
    branches = build_choices_for_merging(first_word, first_word_variants)

    for i in range(1, len(sorted_words_variants)):
        cur_tuple = sorted_words_variants[i]
        cur_word = cur_tuple[0]
        cur_word_variants = cur_tuple[1]

        new_choices = build_choices_for_merging(cur_word, cur_word_variants)
        branches = merge_branches_with_new_choices(branches, new_choices)

    # each branch is a key-alphabet candidate!
    return branches


def my_compare_func(a):
    return len(a[1])


def build_choices_for_merging(word, word_variants):
    choices = []
    for variant_word in word_variants:
        branch = {}
        for i in range(0, len(word)):
            key = word[i]
            value = variant_word[i]
            branch[key] = value
        choices.append(branch)
    return choices


def merge_branches_with_new_choices(branches, new_choices):
    # each branch and each choice is a letter-to-letter dictionary
    result_branches = []
    print('merge_branches_with_new_choices().branches==>' + str(len(branches)) +
          ' new_choices==>' + str(len(new_choices)))

    for cur_branch in branches:
        for cur_choice in new_choices:
            merged_branch = merge_branches(cur_branch, cur_choice)
            if merged_branch is not None:
                result_branches.append(merged_branch)

    if len(result_branches) == 0:
        result_branches = branches
    print('merge_branches_with_new_choices().result_branches==>' + str(len(result_branches)))
    return result_branches


def merge_branches(branch_1, branch_2):
    for entrance in branch_1:
        value_1 = branch_1[entrance]
        try:
            value_2 = branch_2[entrance]
            if value_1 != value_2:
                return None
        except KeyError:
            continue

    result_branch = branch_1.copy()
    result_branch.update(branch_2)
    return result_branch
# endregion build_alphabet_variants


def print_hacked_alternatives(cryptogram, alphabet_variants):
    alphabet_variants_len = len(alphabet_variants)
    print("hack().alphabet_variants len==>" + str(alphabet_variants_len) + "\n")
    print_text_to_file('alphabet_variants.log', str(alphabet_variants))
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


# region interactive
def run_interactive_improvement(cryptogram):
    cryptogram = cryptogram.lower()
    cryptogram_letter_probabilities = build_probabilities_list(cryptogram)
    cryptogram = exchange_with_spaces(cryptogram,
                                      cryptogram_letter_probabilities[len(cryptogram_letter_probabilities) - 1][0])
    print("cryptogram==>" + str(len(cryptogram)))

    f = open('file', 'r')
    file_text = f.read()
    f.close()
    alternatives_strings = file_text.split('\n')
    alternatives_strings = alternatives_strings[:len(alternatives_strings) - 1]
    print("read lines==>" + str(len(alternatives_strings)))

    alt_dictionaries = []
    for i in range(len(alternatives_strings)):
        alternative = alternatives_strings[i]
        alternative = alternative[alternative.index(')') + 1: len(alternative) - 1]
        alt_dict = {}
        for j in range(len(alternative)):
            initial_letter = cryptogram[j]
            alt_letter = alternative[j]
            alt_dict[initial_letter] = alt_letter
        alt_dictionaries.append(alt_dict)

    print_hacked_alternatives(cryptogram, alt_dictionaries)
    while 1:
        limit = input()
        parameters = limit.split(' ')
        position = int(parameters[0])
        letter = parameters[1]

        new_alt_dictionaries = []
        for alt_dict in alt_dictionaries:
            try:
                if alt_dict[cryptogram[position]] == letter:
                    new_alt_dictionaries.append(alt_dict)
            except KeyError:
                pass

        if len(new_alt_dictionaries) == 0:
            for alt_dict in alt_dictionaries:
                alt_dict[cryptogram[position]] = letter
        else:
            alt_dictionaries = new_alt_dictionaries

        print_hacked_alternatives(cryptogram, alt_dictionaries)
# endregion interactive
# endregion HACK

# hack(CRYPTED_TEXT)
run_interactive_improvement(CRYPTED_TEXT)
