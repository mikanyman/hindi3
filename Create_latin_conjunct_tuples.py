import itertools

list = ['k', 'kh', 'g', 'gh', 'ṅ', 'c', 'ch', 'j', 'z', 'jh', \
        'ñ', 'ṭ', 'ṭh', 'ḍ', 'ṛ', 'ḍh', 'ṛh', 'ṇ', 't', 'th', \
        'd', 'dh', 'n', 'p', 'ph', 'f', 'b', 'bh', 'm', 'y', \
        'r', 'l', 'v', 'ś', 'ṣ', 's', 'h', 'ḷ', 'kṣ', 'jñ']

c = itertools.product(list, repeat=2)

for combi in c:
    print(combi)

# Remove tuples starting with kṣ and jñ
# Source: https://www.wikiwand.com/en/Devanagari

"""

('k', 'k')
('k', 'kh')
('k', 'g')
('k', 'gh')
('k', 'ṅ')
('k', 'c')
('k', 'ch')
('k', 'j')
('k', 'z')
('k', 'jh')
('k', 'ñ')
('k', 'ṭ')
('k', 'ṭh')
('k', 'ḍ')
('k', 'ṛ')
('k', 'ḍh')
('k', 'ṛh')
('k', 'ṇ')
('k', 't')
('k', 'th')
('k', 'd')
('k', 'dh')
('k', 'n')
('k', 'p')
('k', 'ph')
('k', 'f')
('k', 'b')
('k', 'bh')
('k', 'm')
('k', 'y')
('k', 'r')
('k', 'l')
('k', 'v')
('k', 'ś')
('k', 'ṣ')
('k', 's')
('k', 'h')
('k', 'ḷ')
('k', 'kṣ')
('k', 'jñ')
('kh', 'k')
('kh', 'kh')
('kh', 'g')
('kh', 'gh')
('kh', 'ṅ')
('kh', 'c')
('kh', 'ch')
('kh', 'j')
('kh', 'z')
('kh', 'jh')
('kh', 'ñ')
('kh', 'ṭ')
('kh', 'ṭh')
('kh', 'ḍ')
('kh', 'ṛ')
('kh', 'ḍh')
('kh', 'ṛh')
('kh', 'ṇ')
('kh', 't')
('kh', 'th')
('kh', 'd')
('kh', 'dh')
('kh', 'n')
('kh', 'p')
('kh', 'ph')
('kh', 'f')
('kh', 'b')
('kh', 'bh')
('kh', 'm')
('kh', 'y')
('kh', 'r')
('kh', 'l')
('kh', 'v')
('kh', 'ś')
('kh', 'ṣ')
('kh', 's')
('kh', 'h')
('kh', 'ḷ')
('kh', 'kṣ')
('kh', 'jñ')
('g', 'k')
('g', 'kh')
('g', 'g')
('g', 'gh')
('g', 'ṅ')
('g', 'c')
('g', 'ch')
('g', 'j')
('g', 'z')
('g', 'jh')
('g', 'ñ')
('g', 'ṭ')
('g', 'ṭh')
('g', 'ḍ')
('g', 'ṛ')
('g', 'ḍh')
('g', 'ṛh')
('g', 'ṇ')
('g', 't')
('g', 'th')
('g', 'd')
('g', 'dh')
('g', 'n')
('g', 'p')
('g', 'ph')
('g', 'f')
('g', 'b')
('g', 'bh')
('g', 'm')
('g', 'y')
('g', 'r')
('g', 'l')
('g', 'v')
('g', 'ś')
('g', 'ṣ')
('g', 's')
('g', 'h')
('g', 'ḷ')
('g', 'kṣ')
('g', 'jñ')
('gh', 'k')
('gh', 'kh')
('gh', 'g')
('gh', 'gh')
('gh', 'ṅ')
('gh', 'c')
('gh', 'ch')
('gh', 'j')
('gh', 'z')
('gh', 'jh')
('gh', 'ñ')
('gh', 'ṭ')
('gh', 'ṭh')
('gh', 'ḍ')
('gh', 'ṛ')
('gh', 'ḍh')
('gh', 'ṛh')
('gh', 'ṇ')
('gh', 't')
('gh', 'th')
('gh', 'd')
('gh', 'dh')
('gh', 'n')
('gh', 'p')
('gh', 'ph')
('gh', 'f')
('gh', 'b')
('gh', 'bh')
('gh', 'm')
('gh', 'y')
('gh', 'r')
('gh', 'l')
('gh', 'v')
('gh', 'ś')
('gh', 'ṣ')
('gh', 's')
('gh', 'h')
('gh', 'ḷ')
('gh', 'kṣ')
('gh', 'jñ')
('ṅ', 'k')
('ṅ', 'kh')
('ṅ', 'g')
('ṅ', 'gh')
('ṅ', 'ṅ')
('ṅ', 'c')
('ṅ', 'ch')
('ṅ', 'j')
('ṅ', 'z')
('ṅ', 'jh')
('ṅ', 'ñ')
('ṅ', 'ṭ')
('ṅ', 'ṭh')
('ṅ', 'ḍ')
('ṅ', 'ṛ')
('ṅ', 'ḍh')
('ṅ', 'ṛh')
('ṅ', 'ṇ')
('ṅ', 't')
('ṅ', 'th')
('ṅ', 'd')
('ṅ', 'dh')
('ṅ', 'n')
('ṅ', 'p')
('ṅ', 'ph')
('ṅ', 'f')
('ṅ', 'b')
('ṅ', 'bh')
('ṅ', 'm')
('ṅ', 'y')
('ṅ', 'r')
('ṅ', 'l')
('ṅ', 'v')
('ṅ', 'ś')
('ṅ', 'ṣ')
('ṅ', 's')
('ṅ', 'h')
('ṅ', 'ḷ')
('ṅ', 'kṣ')
('ṅ', 'jñ')
('c', 'k')
('c', 'kh')
('c', 'g')
('c', 'gh')
('c', 'ṅ')
('c', 'c')
('c', 'ch')
('c', 'j')
('c', 'z')
('c', 'jh')
('c', 'ñ')
('c', 'ṭ')
('c', 'ṭh')
('c', 'ḍ')
('c', 'ṛ')
('c', 'ḍh')
('c', 'ṛh')
('c', 'ṇ')
('c', 't')
('c', 'th')
('c', 'd')
('c', 'dh')
('c', 'n')
('c', 'p')
('c', 'ph')
('c', 'f')
('c', 'b')
('c', 'bh')
('c', 'm')
('c', 'y')
('c', 'r')
('c', 'l')
('c', 'v')
('c', 'ś')
('c', 'ṣ')
('c', 's')
('c', 'h')
('c', 'ḷ')
('c', 'kṣ')
('c', 'jñ')
('ch', 'k')
('ch', 'kh')
('ch', 'g')
('ch', 'gh')
('ch', 'ṅ')
('ch', 'c')
('ch', 'ch')
('ch', 'j')
('ch', 'z')
('ch', 'jh')
('ch', 'ñ')
('ch', 'ṭ')
('ch', 'ṭh')
('ch', 'ḍ')
('ch', 'ṛ')
('ch', 'ḍh')
('ch', 'ṛh')
('ch', 'ṇ')
('ch', 't')
('ch', 'th')
('ch', 'd')
('ch', 'dh')
('ch', 'n')
('ch', 'p')
('ch', 'ph')
('ch', 'f')
('ch', 'b')
('ch', 'bh')
('ch', 'm')
('ch', 'y')
('ch', 'r')
('ch', 'l')
('ch', 'v')
('ch', 'ś')
('ch', 'ṣ')
('ch', 's')
('ch', 'h')
('ch', 'ḷ')
('ch', 'kṣ')
('ch', 'jñ')
('j', 'k')
('j', 'kh')
('j', 'g')
('j', 'gh')
('j', 'ṅ')
('j', 'c')
('j', 'ch')
('j', 'j')
('j', 'z')
('j', 'jh')
('j', 'ñ')
('j', 'ṭ')
('j', 'ṭh')
('j', 'ḍ')
('j', 'ṛ')
('j', 'ḍh')
('j', 'ṛh')
('j', 'ṇ')
('j', 't')
('j', 'th')
('j', 'd')
('j', 'dh')
('j', 'n')
('j', 'p')
('j', 'ph')
('j', 'f')
('j', 'b')
('j', 'bh')
('j', 'm')
('j', 'y')
('j', 'r')
('j', 'l')
('j', 'v')
('j', 'ś')
('j', 'ṣ')
('j', 's')
('j', 'h')
('j', 'ḷ')
('j', 'kṣ')
('j', 'jñ')
('z', 'k')
('z', 'kh')
('z', 'g')
('z', 'gh')
('z', 'ṅ')
('z', 'c')
('z', 'ch')
('z', 'j')
('z', 'z')
('z', 'jh')
('z', 'ñ')
('z', 'ṭ')
('z', 'ṭh')
('z', 'ḍ')
('z', 'ṛ')
('z', 'ḍh')
('z', 'ṛh')
('z', 'ṇ')
('z', 't')
('z', 'th')
('z', 'd')
('z', 'dh')
('z', 'n')
('z', 'p')
('z', 'ph')
('z', 'f')
('z', 'b')
('z', 'bh')
('z', 'm')
('z', 'y')
('z', 'r')
('z', 'l')
('z', 'v')
('z', 'ś')
('z', 'ṣ')
('z', 's')
('z', 'h')
('z', 'ḷ')
('z', 'kṣ')
('z', 'jñ')
('jh', 'k')
('jh', 'kh')
('jh', 'g')
('jh', 'gh')
('jh', 'ṅ')
('jh', 'c')
('jh', 'ch')
('jh', 'j')
('jh', 'z')
('jh', 'jh')
('jh', 'ñ')
('jh', 'ṭ')
('jh', 'ṭh')
('jh', 'ḍ')
('jh', 'ṛ')
('jh', 'ḍh')
('jh', 'ṛh')
('jh', 'ṇ')
('jh', 't')
('jh', 'th')
('jh', 'd')
('jh', 'dh')
('jh', 'n')
('jh', 'p')
('jh', 'ph')
('jh', 'f')
('jh', 'b')
('jh', 'bh')
('jh', 'm')
('jh', 'y')
('jh', 'r')
('jh', 'l')
('jh', 'v')
('jh', 'ś')
('jh', 'ṣ')
('jh', 's')
('jh', 'h')
('jh', 'ḷ')
('jh', 'kṣ')
('jh', 'jñ')
('ñ', 'k')
('ñ', 'kh')
('ñ', 'g')
('ñ', 'gh')
('ñ', 'ṅ')
('ñ', 'c')
('ñ', 'ch')
('ñ', 'j')
('ñ', 'z')
('ñ', 'jh')
('ñ', 'ñ')
('ñ', 'ṭ')
('ñ', 'ṭh')
('ñ', 'ḍ')
('ñ', 'ṛ')
('ñ', 'ḍh')
('ñ', 'ṛh')
('ñ', 'ṇ')
('ñ', 't')
('ñ', 'th')
('ñ', 'd')
('ñ', 'dh')
('ñ', 'n')
('ñ', 'p')
('ñ', 'ph')
('ñ', 'f')
('ñ', 'b')
('ñ', 'bh')
('ñ', 'm')
('ñ', 'y')
('ñ', 'r')
('ñ', 'l')
('ñ', 'v')
('ñ', 'ś')
('ñ', 'ṣ')
('ñ', 's')
('ñ', 'h')
('ñ', 'ḷ')
('ñ', 'kṣ')
('ñ', 'jñ')
('ṭ', 'k')
('ṭ', 'kh')
('ṭ', 'g')
('ṭ', 'gh')
('ṭ', 'ṅ')
('ṭ', 'c')
('ṭ', 'ch')
('ṭ', 'j')
('ṭ', 'z')
('ṭ', 'jh')
('ṭ', 'ñ')
('ṭ', 'ṭ')
('ṭ', 'ṭh')
('ṭ', 'ḍ')
('ṭ', 'ṛ')
('ṭ', 'ḍh')
('ṭ', 'ṛh')
('ṭ', 'ṇ')
('ṭ', 't')
('ṭ', 'th')
('ṭ', 'd')
('ṭ', 'dh')
('ṭ', 'n')
('ṭ', 'p')
('ṭ', 'ph')
('ṭ', 'f')
('ṭ', 'b')
('ṭ', 'bh')
('ṭ', 'm')
('ṭ', 'y')
('ṭ', 'r')
('ṭ', 'l')
('ṭ', 'v')
('ṭ', 'ś')
('ṭ', 'ṣ')
('ṭ', 's')
('ṭ', 'h')
('ṭ', 'ḷ')
('ṭ', 'kṣ')
('ṭ', 'jñ')
('ṭh', 'k')
('ṭh', 'kh')
('ṭh', 'g')
('ṭh', 'gh')
('ṭh', 'ṅ')
('ṭh', 'c')
('ṭh', 'ch')
('ṭh', 'j')
('ṭh', 'z')
('ṭh', 'jh')
('ṭh', 'ñ')
('ṭh', 'ṭ')
('ṭh', 'ṭh')
('ṭh', 'ḍ')
('ṭh', 'ṛ')
('ṭh', 'ḍh')
('ṭh', 'ṛh')
('ṭh', 'ṇ')
('ṭh', 't')
('ṭh', 'th')
('ṭh', 'd')
('ṭh', 'dh')
('ṭh', 'n')
('ṭh', 'p')
('ṭh', 'ph')
('ṭh', 'f')
('ṭh', 'b')
('ṭh', 'bh')
('ṭh', 'm')
('ṭh', 'y')
('ṭh', 'r')
('ṭh', 'l')
('ṭh', 'v')
('ṭh', 'ś')
('ṭh', 'ṣ')
('ṭh', 's')
('ṭh', 'h')
('ṭh', 'ḷ')
('ṭh', 'kṣ')
('ṭh', 'jñ')
('ḍ', 'k')
('ḍ', 'kh')
('ḍ', 'g')
('ḍ', 'gh')
('ḍ', 'ṅ')
('ḍ', 'c')
('ḍ', 'ch')
('ḍ', 'j')
('ḍ', 'z')
('ḍ', 'jh')
('ḍ', 'ñ')
('ḍ', 'ṭ')
('ḍ', 'ṭh')
('ḍ', 'ḍ')
('ḍ', 'ṛ')
('ḍ', 'ḍh')
('ḍ', 'ṛh')
('ḍ', 'ṇ')
('ḍ', 't')
('ḍ', 'th')
('ḍ', 'd')
('ḍ', 'dh')
('ḍ', 'n')
('ḍ', 'p')
('ḍ', 'ph')
('ḍ', 'f')
('ḍ', 'b')
('ḍ', 'bh')
('ḍ', 'm')
('ḍ', 'y')
('ḍ', 'r')
('ḍ', 'l')
('ḍ', 'v')
('ḍ', 'ś')
('ḍ', 'ṣ')
('ḍ', 's')
('ḍ', 'h')
('ḍ', 'ḷ')
('ḍ', 'kṣ')
('ḍ', 'jñ')
('ṛ', 'k')
('ṛ', 'kh')
('ṛ', 'g')
('ṛ', 'gh')
('ṛ', 'ṅ')
('ṛ', 'c')
('ṛ', 'ch')
('ṛ', 'j')
('ṛ', 'z')
('ṛ', 'jh')
('ṛ', 'ñ')
('ṛ', 'ṭ')
('ṛ', 'ṭh')
('ṛ', 'ḍ')
('ṛ', 'ṛ')
('ṛ', 'ḍh')
('ṛ', 'ṛh')
('ṛ', 'ṇ')
('ṛ', 't')
('ṛ', 'th')
('ṛ', 'd')
('ṛ', 'dh')
('ṛ', 'n')
('ṛ', 'p')
('ṛ', 'ph')
('ṛ', 'f')
('ṛ', 'b')
('ṛ', 'bh')
('ṛ', 'm')
('ṛ', 'y')
('ṛ', 'r')
('ṛ', 'l')
('ṛ', 'v')
('ṛ', 'ś')
('ṛ', 'ṣ')
('ṛ', 's')
('ṛ', 'h')
('ṛ', 'ḷ')
('ṛ', 'kṣ')
('ṛ', 'jñ')
('ḍh', 'k')
('ḍh', 'kh')
('ḍh', 'g')
('ḍh', 'gh')
('ḍh', 'ṅ')
('ḍh', 'c')
('ḍh', 'ch')
('ḍh', 'j')
('ḍh', 'z')
('ḍh', 'jh')
('ḍh', 'ñ')
('ḍh', 'ṭ')
('ḍh', 'ṭh')
('ḍh', 'ḍ')
('ḍh', 'ṛ')
('ḍh', 'ḍh')
('ḍh', 'ṛh')
('ḍh', 'ṇ')
('ḍh', 't')
('ḍh', 'th')
('ḍh', 'd')
('ḍh', 'dh')
('ḍh', 'n')
('ḍh', 'p')
('ḍh', 'ph')
('ḍh', 'f')
('ḍh', 'b')
('ḍh', 'bh')
('ḍh', 'm')
('ḍh', 'y')
('ḍh', 'r')
('ḍh', 'l')
('ḍh', 'v')
('ḍh', 'ś')
('ḍh', 'ṣ')
('ḍh', 's')
('ḍh', 'h')
('ḍh', 'ḷ')
('ḍh', 'kṣ')
('ḍh', 'jñ')
('ṛh', 'k')
('ṛh', 'kh')
('ṛh', 'g')
('ṛh', 'gh')
('ṛh', 'ṅ')
('ṛh', 'c')
('ṛh', 'ch')
('ṛh', 'j')
('ṛh', 'z')
('ṛh', 'jh')
('ṛh', 'ñ')
('ṛh', 'ṭ')
('ṛh', 'ṭh')
('ṛh', 'ḍ')
('ṛh', 'ṛ')
('ṛh', 'ḍh')
('ṛh', 'ṛh')
('ṛh', 'ṇ')
('ṛh', 't')
('ṛh', 'th')
('ṛh', 'd')
('ṛh', 'dh')
('ṛh', 'n')
('ṛh', 'p')
('ṛh', 'ph')
('ṛh', 'f')
('ṛh', 'b')
('ṛh', 'bh')
('ṛh', 'm')
('ṛh', 'y')
('ṛh', 'r')
('ṛh', 'l')
('ṛh', 'v')
('ṛh', 'ś')
('ṛh', 'ṣ')
('ṛh', 's')
('ṛh', 'h')
('ṛh', 'ḷ')
('ṛh', 'kṣ')
('ṛh', 'jñ')
('ṇ', 'k')
('ṇ', 'kh')
('ṇ', 'g')
('ṇ', 'gh')
('ṇ', 'ṅ')
('ṇ', 'c')
('ṇ', 'ch')
('ṇ', 'j')
('ṇ', 'z')
('ṇ', 'jh')
('ṇ', 'ñ')
('ṇ', 'ṭ')
('ṇ', 'ṭh')
('ṇ', 'ḍ')
('ṇ', 'ṛ')
('ṇ', 'ḍh')
('ṇ', 'ṛh')
('ṇ', 'ṇ')
('ṇ', 't')
('ṇ', 'th')
('ṇ', 'd')
('ṇ', 'dh')
('ṇ', 'n')
('ṇ', 'p')
('ṇ', 'ph')
('ṇ', 'f')
('ṇ', 'b')
('ṇ', 'bh')
('ṇ', 'm')
('ṇ', 'y')
('ṇ', 'r')
('ṇ', 'l')
('ṇ', 'v')
('ṇ', 'ś')
('ṇ', 'ṣ')
('ṇ', 's')
('ṇ', 'h')
('ṇ', 'ḷ')
('ṇ', 'kṣ')
('ṇ', 'jñ')
('t', 'k')
('t', 'kh')
('t', 'g')
('t', 'gh')
('t', 'ṅ')
('t', 'c')
('t', 'ch')
('t', 'j')
('t', 'z')
('t', 'jh')
('t', 'ñ')
('t', 'ṭ')
('t', 'ṭh')
('t', 'ḍ')
('t', 'ṛ')
('t', 'ḍh')
('t', 'ṛh')
('t', 'ṇ')
('t', 't')
('t', 'th')
('t', 'd')
('t', 'dh')
('t', 'n')
('t', 'p')
('t', 'ph')
('t', 'f')
('t', 'b')
('t', 'bh')
('t', 'm')
('t', 'y')
('t', 'r')
('t', 'l')
('t', 'v')
('t', 'ś')
('t', 'ṣ')
('t', 's')
('t', 'h')
('t', 'ḷ')
('t', 'kṣ')
('t', 'jñ')
('th', 'k')
('th', 'kh')
('th', 'g')
('th', 'gh')
('th', 'ṅ')
('th', 'c')
('th', 'ch')
('th', 'j')
('th', 'z')
('th', 'jh')
('th', 'ñ')
('th', 'ṭ')
('th', 'ṭh')
('th', 'ḍ')
('th', 'ṛ')
('th', 'ḍh')
('th', 'ṛh')
('th', 'ṇ')
('th', 't')
('th', 'th')
('th', 'd')
('th', 'dh')
('th', 'n')
('th', 'p')
('th', 'ph')
('th', 'f')
('th', 'b')
('th', 'bh')
('th', 'm')
('th', 'y')
('th', 'r')
('th', 'l')
('th', 'v')
('th', 'ś')
('th', 'ṣ')
('th', 's')
('th', 'h')
('th', 'ḷ')
('th', 'kṣ')
('th', 'jñ')
('d', 'k')
('d', 'kh')
('d', 'g')
('d', 'gh')
('d', 'ṅ')
('d', 'c')
('d', 'ch')
('d', 'j')
('d', 'z')
('d', 'jh')
('d', 'ñ')
('d', 'ṭ')
('d', 'ṭh')
('d', 'ḍ')
('d', 'ṛ')
('d', 'ḍh')
('d', 'ṛh')
('d', 'ṇ')
('d', 't')
('d', 'th')
('d', 'd')
('d', 'dh')
('d', 'n')
('d', 'p')
('d', 'ph')
('d', 'f')
('d', 'b')
('d', 'bh')
('d', 'm')
('d', 'y')
('d', 'r')
('d', 'l')
('d', 'v')
('d', 'ś')
('d', 'ṣ')
('d', 's')
('d', 'h')
('d', 'ḷ')
('d', 'kṣ')
('d', 'jñ')
('dh', 'k')
('dh', 'kh')
('dh', 'g')
('dh', 'gh')
('dh', 'ṅ')
('dh', 'c')
('dh', 'ch')
('dh', 'j')
('dh', 'z')
('dh', 'jh')
('dh', 'ñ')
('dh', 'ṭ')
('dh', 'ṭh')
('dh', 'ḍ')
('dh', 'ṛ')
('dh', 'ḍh')
('dh', 'ṛh')
('dh', 'ṇ')
('dh', 't')
('dh', 'th')
('dh', 'd')
('dh', 'dh')
('dh', 'n')
('dh', 'p')
('dh', 'ph')
('dh', 'f')
('dh', 'b')
('dh', 'bh')
('dh', 'm')
('dh', 'y')
('dh', 'r')
('dh', 'l')
('dh', 'v')
('dh', 'ś')
('dh', 'ṣ')
('dh', 's')
('dh', 'h')
('dh', 'ḷ')
('dh', 'kṣ')
('dh', 'jñ')
('n', 'k')
('n', 'kh')
('n', 'g')
('n', 'gh')
('n', 'ṅ')
('n', 'c')
('n', 'ch')
('n', 'j')
('n', 'z')
('n', 'jh')
('n', 'ñ')
('n', 'ṭ')
('n', 'ṭh')
('n', 'ḍ')
('n', 'ṛ')
('n', 'ḍh')
('n', 'ṛh')
('n', 'ṇ')
('n', 't')
('n', 'th')
('n', 'd')
('n', 'dh')
('n', 'n')
('n', 'p')
('n', 'ph')
('n', 'f')
('n', 'b')
('n', 'bh')
('n', 'm')
('n', 'y')
('n', 'r')
('n', 'l')
('n', 'v')
('n', 'ś')
('n', 'ṣ')
('n', 's')
('n', 'h')
('n', 'ḷ')
('n', 'kṣ')
('n', 'jñ')
('p', 'k')
('p', 'kh')
('p', 'g')
('p', 'gh')
('p', 'ṅ')
('p', 'c')
('p', 'ch')
('p', 'j')
('p', 'z')
('p', 'jh')
('p', 'ñ')
('p', 'ṭ')
('p', 'ṭh')
('p', 'ḍ')
('p', 'ṛ')
('p', 'ḍh')
('p', 'ṛh')
('p', 'ṇ')
('p', 't')
('p', 'th')
('p', 'd')
('p', 'dh')
('p', 'n')
('p', 'p')
('p', 'ph')
('p', 'f')
('p', 'b')
('p', 'bh')
('p', 'm')
('p', 'y')
('p', 'r')
('p', 'l')
('p', 'v')
('p', 'ś')
('p', 'ṣ')
('p', 's')
('p', 'h')
('p', 'ḷ')
('p', 'kṣ')
('p', 'jñ')
('ph', 'k')
('ph', 'kh')
('ph', 'g')
('ph', 'gh')
('ph', 'ṅ')
('ph', 'c')
('ph', 'ch')
('ph', 'j')
('ph', 'z')
('ph', 'jh')
('ph', 'ñ')
('ph', 'ṭ')
('ph', 'ṭh')
('ph', 'ḍ')
('ph', 'ṛ')
('ph', 'ḍh')
('ph', 'ṛh')
('ph', 'ṇ')
('ph', 't')
('ph', 'th')
('ph', 'd')
('ph', 'dh')
('ph', 'n')
('ph', 'p')
('ph', 'ph')
('ph', 'f')
('ph', 'b')
('ph', 'bh')
('ph', 'm')
('ph', 'y')
('ph', 'r')
('ph', 'l')
('ph', 'v')
('ph', 'ś')
('ph', 'ṣ')
('ph', 's')
('ph', 'h')
('ph', 'ḷ')
('ph', 'kṣ')
('ph', 'jñ')
('f', 'k')
('f', 'kh')
('f', 'g')
('f', 'gh')
('f', 'ṅ')
('f', 'c')
('f', 'ch')
('f', 'j')
('f', 'z')
('f', 'jh')
('f', 'ñ')
('f', 'ṭ')
('f', 'ṭh')
('f', 'ḍ')
('f', 'ṛ')
('f', 'ḍh')
('f', 'ṛh')
('f', 'ṇ')
('f', 't')
('f', 'th')
('f', 'd')
('f', 'dh')
('f', 'n')
('f', 'p')
('f', 'ph')
('f', 'f')
('f', 'b')
('f', 'bh')
('f', 'm')
('f', 'y')
('f', 'r')
('f', 'l')
('f', 'v')
('f', 'ś')
('f', 'ṣ')
('f', 's')
('f', 'h')
('f', 'ḷ')
('f', 'kṣ')
('f', 'jñ')
('b', 'k')
('b', 'kh')
('b', 'g')
('b', 'gh')
('b', 'ṅ')
('b', 'c')
('b', 'ch')
('b', 'j')
('b', 'z')
('b', 'jh')
('b', 'ñ')
('b', 'ṭ')
('b', 'ṭh')
('b', 'ḍ')
('b', 'ṛ')
('b', 'ḍh')
('b', 'ṛh')
('b', 'ṇ')
('b', 't')
('b', 'th')
('b', 'd')
('b', 'dh')
('b', 'n')
('b', 'p')
('b', 'ph')
('b', 'f')
('b', 'b')
('b', 'bh')
('b', 'm')
('b', 'y')
('b', 'r')
('b', 'l')
('b', 'v')
('b', 'ś')
('b', 'ṣ')
('b', 's')
('b', 'h')
('b', 'ḷ')
('b', 'kṣ')
('b', 'jñ')
('bh', 'k')
('bh', 'kh')
('bh', 'g')
('bh', 'gh')
('bh', 'ṅ')
('bh', 'c')
('bh', 'ch')
('bh', 'j')
('bh', 'z')
('bh', 'jh')
('bh', 'ñ')
('bh', 'ṭ')
('bh', 'ṭh')
('bh', 'ḍ')
('bh', 'ṛ')
('bh', 'ḍh')
('bh', 'ṛh')
('bh', 'ṇ')
('bh', 't')
('bh', 'th')
('bh', 'd')
('bh', 'dh')
('bh', 'n')
('bh', 'p')
('bh', 'ph')
('bh', 'f')
('bh', 'b')
('bh', 'bh')
('bh', 'm')
('bh', 'y')
('bh', 'r')
('bh', 'l')
('bh', 'v')
('bh', 'ś')
('bh', 'ṣ')
('bh', 's')
('bh', 'h')
('bh', 'ḷ')
('bh', 'kṣ')
('bh', 'jñ')
('m', 'k')
('m', 'kh')
('m', 'g')
('m', 'gh')
('m', 'ṅ')
('m', 'c')
('m', 'ch')
('m', 'j')
('m', 'z')
('m', 'jh')
('m', 'ñ')
('m', 'ṭ')
('m', 'ṭh')
('m', 'ḍ')
('m', 'ṛ')
('m', 'ḍh')
('m', 'ṛh')
('m', 'ṇ')
('m', 't')
('m', 'th')
('m', 'd')
('m', 'dh')
('m', 'n')
('m', 'p')
('m', 'ph')
('m', 'f')
('m', 'b')
('m', 'bh')
('m', 'm')
('m', 'y')
('m', 'r')
('m', 'l')
('m', 'v')
('m', 'ś')
('m', 'ṣ')
('m', 's')
('m', 'h')
('m', 'ḷ')
('m', 'kṣ')
('m', 'jñ')
('y', 'k')
('y', 'kh')
('y', 'g')
('y', 'gh')
('y', 'ṅ')
('y', 'c')
('y', 'ch')
('y', 'j')
('y', 'z')
('y', 'jh')
('y', 'ñ')
('y', 'ṭ')
('y', 'ṭh')
('y', 'ḍ')
('y', 'ṛ')
('y', 'ḍh')
('y', 'ṛh')
('y', 'ṇ')
('y', 't')
('y', 'th')
('y', 'd')
('y', 'dh')
('y', 'n')
('y', 'p')
('y', 'ph')
('y', 'f')
('y', 'b')
('y', 'bh')
('y', 'm')
('y', 'y')
('y', 'r')
('y', 'l')
('y', 'v')
('y', 'ś')
('y', 'ṣ')
('y', 's')
('y', 'h')
('y', 'ḷ')
('y', 'kṣ')
('y', 'jñ')
('r', 'k')
('r', 'kh')
('r', 'g')
('r', 'gh')
('r', 'ṅ')
('r', 'c')
('r', 'ch')
('r', 'j')
('r', 'z')
('r', 'jh')
('r', 'ñ')
('r', 'ṭ')
('r', 'ṭh')
('r', 'ḍ')
('r', 'ṛ')
('r', 'ḍh')
('r', 'ṛh')
('r', 'ṇ')
('r', 't')
('r', 'th')
('r', 'd')
('r', 'dh')
('r', 'n')
('r', 'p')
('r', 'ph')
('r', 'f')
('r', 'b')
('r', 'bh')
('r', 'm')
('r', 'y')
('r', 'r')
('r', 'l')
('r', 'v')
('r', 'ś')
('r', 'ṣ')
('r', 's')
('r', 'h')
('r', 'ḷ')
('r', 'kṣ')
('r', 'jñ')
('l', 'k')
('l', 'kh')
('l', 'g')
('l', 'gh')
('l', 'ṅ')
('l', 'c')
('l', 'ch')
('l', 'j')
('l', 'z')
('l', 'jh')
('l', 'ñ')
('l', 'ṭ')
('l', 'ṭh')
('l', 'ḍ')
('l', 'ṛ')
('l', 'ḍh')
('l', 'ṛh')
('l', 'ṇ')
('l', 't')
('l', 'th')
('l', 'd')
('l', 'dh')
('l', 'n')
('l', 'p')
('l', 'ph')
('l', 'f')
('l', 'b')
('l', 'bh')
('l', 'm')
('l', 'y')
('l', 'r')
('l', 'l')
('l', 'v')
('l', 'ś')
('l', 'ṣ')
('l', 's')
('l', 'h')
('l', 'ḷ')
('l', 'kṣ')
('l', 'jñ')
('v', 'k')
('v', 'kh')
('v', 'g')
('v', 'gh')
('v', 'ṅ')
('v', 'c')
('v', 'ch')
('v', 'j')
('v', 'z')
('v', 'jh')
('v', 'ñ')
('v', 'ṭ')
('v', 'ṭh')
('v', 'ḍ')
('v', 'ṛ')
('v', 'ḍh')
('v', 'ṛh')
('v', 'ṇ')
('v', 't')
('v', 'th')
('v', 'd')
('v', 'dh')
('v', 'n')
('v', 'p')
('v', 'ph')
('v', 'f')
('v', 'b')
('v', 'bh')
('v', 'm')
('v', 'y')
('v', 'r')
('v', 'l')
('v', 'v')
('v', 'ś')
('v', 'ṣ')
('v', 's')
('v', 'h')
('v', 'ḷ')
('v', 'kṣ')
('v', 'jñ')
('ś', 'k')
('ś', 'kh')
('ś', 'g')
('ś', 'gh')
('ś', 'ṅ')
('ś', 'c')
('ś', 'ch')
('ś', 'j')
('ś', 'z')
('ś', 'jh')
('ś', 'ñ')
('ś', 'ṭ')
('ś', 'ṭh')
('ś', 'ḍ')
('ś', 'ṛ')
('ś', 'ḍh')
('ś', 'ṛh')
('ś', 'ṇ')
('ś', 't')
('ś', 'th')
('ś', 'd')
('ś', 'dh')
('ś', 'n')
('ś', 'p')
('ś', 'ph')
('ś', 'f')
('ś', 'b')
('ś', 'bh')
('ś', 'm')
('ś', 'y')
('ś', 'r')
('ś', 'l')
('ś', 'v')
('ś', 'ś')
('ś', 'ṣ')
('ś', 's')
('ś', 'h')
('ś', 'ḷ')
('ś', 'kṣ')
('ś', 'jñ')
('ṣ', 'k')
('ṣ', 'kh')
('ṣ', 'g')
('ṣ', 'gh')
('ṣ', 'ṅ')
('ṣ', 'c')
('ṣ', 'ch')
('ṣ', 'j')
('ṣ', 'z')
('ṣ', 'jh')
('ṣ', 'ñ')
('ṣ', 'ṭ')
('ṣ', 'ṭh')
('ṣ', 'ḍ')
('ṣ', 'ṛ')
('ṣ', 'ḍh')
('ṣ', 'ṛh')
('ṣ', 'ṇ')
('ṣ', 't')
('ṣ', 'th')
('ṣ', 'd')
('ṣ', 'dh')
('ṣ', 'n')
('ṣ', 'p')
('ṣ', 'ph')
('ṣ', 'f')
('ṣ', 'b')
('ṣ', 'bh')
('ṣ', 'm')
('ṣ', 'y')
('ṣ', 'r')
('ṣ', 'l')
('ṣ', 'v')
('ṣ', 'ś')
('ṣ', 'ṣ')
('ṣ', 's')
('ṣ', 'h')
('ṣ', 'ḷ')
('ṣ', 'kṣ')
('ṣ', 'jñ')
('s', 'k')
('s', 'kh')
('s', 'g')
('s', 'gh')
('s', 'ṅ')
('s', 'c')
('s', 'ch')
('s', 'j')
('s', 'z')
('s', 'jh')
('s', 'ñ')
('s', 'ṭ')
('s', 'ṭh')
('s', 'ḍ')
('s', 'ṛ')
('s', 'ḍh')
('s', 'ṛh')
('s', 'ṇ')
('s', 't')
('s', 'th')
('s', 'd')
('s', 'dh')
('s', 'n')
('s', 'p')
('s', 'ph')
('s', 'f')
('s', 'b')
('s', 'bh')
('s', 'm')
('s', 'y')
('s', 'r')
('s', 'l')
('s', 'v')
('s', 'ś')
('s', 'ṣ')
('s', 's')
('s', 'h')
('s', 'ḷ')
('s', 'kṣ')
('s', 'jñ')
('h', 'k')
('h', 'kh')
('h', 'g')
('h', 'gh')
('h', 'ṅ')
('h', 'c')
('h', 'ch')
('h', 'j')
('h', 'z')
('h', 'jh')
('h', 'ñ')
('h', 'ṭ')
('h', 'ṭh')
('h', 'ḍ')
('h', 'ṛ')
('h', 'ḍh')
('h', 'ṛh')
('h', 'ṇ')
('h', 't')
('h', 'th')
('h', 'd')
('h', 'dh')
('h', 'n')
('h', 'p')
('h', 'ph')
('h', 'f')
('h', 'b')
('h', 'bh')
('h', 'm')
('h', 'y')
('h', 'r')
('h', 'l')
('h', 'v')
('h', 'ś')
('h', 'ṣ')
('h', 's')
('h', 'h')
('h', 'ḷ')
('h', 'kṣ')
('h', 'jñ')
('ḷ', 'k')
('ḷ', 'kh')
('ḷ', 'g')
('ḷ', 'gh')
('ḷ', 'ṅ')
('ḷ', 'c')
('ḷ', 'ch')
('ḷ', 'j')
('ḷ', 'z')
('ḷ', 'jh')
('ḷ', 'ñ')
('ḷ', 'ṭ')
('ḷ', 'ṭh')
('ḷ', 'ḍ')
('ḷ', 'ṛ')
('ḷ', 'ḍh')
('ḷ', 'ṛh')
('ḷ', 'ṇ')
('ḷ', 't')
('ḷ', 'th')
('ḷ', 'd')
('ḷ', 'dh')
('ḷ', 'n')
('ḷ', 'p')
('ḷ', 'ph')
('ḷ', 'f')
('ḷ', 'b')
('ḷ', 'bh')
('ḷ', 'm')
('ḷ', 'y')
('ḷ', 'r')
('ḷ', 'l')
('ḷ', 'v')
('ḷ', 'ś')
('ḷ', 'ṣ')
('ḷ', 's')
('ḷ', 'h')
('ḷ', 'ḷ')
('ḷ', 'kṣ')
('ḷ', 'jñ')

"""