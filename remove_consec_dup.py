import re
#
# patt = r'([A-Za-z0-9]+) \1'
# sentence = '''
# double double toil and trouble
# fire burn and cauldron bubble bubble
# tomorrow and tomorrow and tomorrow
# creeps in this this petty pace from day toto day
# to the last syllable of recorded time time
# '''
#
# f = re.findall(patt, ss)
# print(f)
# for w in f:
#     to_replace = w + " " + w
#     print(w)
#     ss = ss.replace(w, to_replace)
# print(ss)

# d = re.sub(patt, '', ss)
# print(d)

# sentence = 'I need need to learn regex... regex from scratch!'

# remove punctuation
# the unicode flag makes it work for more letter types (non-ascii)
# no_punc = re.sub(r'[^\w\s]', '', sentence, re.UNICODE)
# print('No punctuation:', no_punc)

# remove duplicates
# re_output = re.sub(r'\b(\w+)( \1\b)+', r'\1', no_punc)
# print('No duplicates:', re_output)


