with open("topics.txt", 'r', encoding='utf-8') as file:
    tmp_num = 0
    tmp_first_topic = ''
    for item in file:
        text_line = item
        text_line = text_line.strip()
        # print(text_line)
        if '---------------------------------' in text_line:
            tmp_num = 0
            continue
        text_name = text_line.split(' => ')[0]
        text_url = text_line.split(' => ')[1]
        if tmp_num == 0:
            tmp_first_topic = text_name
            tmp_num = 1
        print(tmp_first_topic)

        text_line = tmp_first_topic + ' => ' + text_name + ' => ' + text_url + '\n'

        file = open('c_topics.txt', 'a')
        file.write(text_line)