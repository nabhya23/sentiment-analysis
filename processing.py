from collections import Counter


def process_emotions(word_file, emotion_file):
    # Read words from final_words.txt
    with open(word_file, 'r') as f:
        word_list = [line.strip() for line in f.readlines()]

    emotion_list = []

    # Open and read the emotion file
    with open(emotion_file, 'r') as file:
        for line in file:
            # Clean and split the line
            clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

           
            if word in word_list:
                emotion_list.append(emotion)

    # Count each emotion
    emotion_count = Counter(emotion_list)


    with open('emotion_count.txt', 'w') as f:
        for emotion, count in emotion_count.items():
            f.write(f"{emotion}:{count}\n")


# Run processing when this file is executed
process_emotions('final_words.txt', 'emotions.txt')
