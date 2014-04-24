import codecs

def build_word_map(fname):

    # open = codecs.open
    # fp = open(fname, 'r', 'ascii')

    fp = open(fname, 'r')

    word_mp = {}
    word_info = ''
    last_word = ''
    count = 0
    while True:
        line = fp.readline()

        print(line)
        
        count += 1
        
        if len(line) == 0:
            break
        
        if len(line) < 2:
            continue

        if line[0].isdigit() == False:
            if len(word_info) > 0:
                 word_info += "。"
            word_info += line.split('\n')[0]
            
            continue

        # print(line)
        res = line.split(' ', 4)
        word = res[1]
        # print(res[1])
        if len(word_info) > 0:
            word_mp[last_word] = word_info
            # print("%s => %s" % (last_word, word_info))            
            word_info = ''
            
        last_word = word
        
    # print(word_mp)
    fp.close()

    if len(word_info) > 0:
        word_mp[last_word] = word_info
        # print("%s => %s" % (last_word, word_info))
            
    return word_mp
    
# build_word_map('新东方六级词汇单词__乱序版.txt')
mp = build_word_map('bad_map.txt')
# print( len(mp) )


