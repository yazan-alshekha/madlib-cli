def welcome_message():
    print("Welcome to our game ")




input_words=["Adjective","Adjective","A First Name","Past Tense Verb","A First Name","Adjective","Adjective","Plural Noun","Large Animal","Small Animal","A Girl's Name","Adjective","Plural Noun","Adjective","Plural Noun","Number 1-50","First Name's","Number","Plural Noun","Number","Plural Noun"]

output_words=[]

def input_function():
    for i in input_words:
        msg=input("please enter a :"+i)
        output_words.append(msg)


def read_file():
    file=open('assets/text_game.txt')
    content=file.read()
    # print(content)
    file.close()
    insert_content(content)
    # print(content)



def insert_content(content):
    content=content.format(output_words[0],output_words[1],output_words[2],output_words[3],output_words[4],output_words[5],output_words[6],output_words[7],output_words[8],output_words[9],output_words[10],output_words[11],output_words[12],output_words[13],output_words[14],output_words[15],output_words[16],output_words[17],output_words[18],output_words[19],output_words[20])
    print(content)
    create_txt(content)

def create_txt(content):
    with open('assets/text_game_copy.txt','w') as f:
        f.write(content)

if __name__ == "__main__":
    input_function()
    read_file()




