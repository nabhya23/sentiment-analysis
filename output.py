import matplotlib.pyplot as plt


def plot_emotions(emotion_count_file):
    emotion_count = {}

    # Read emotion counts from emotion_count.txt
    with open(emotion_count_file, 'r') as f:
        for line in f.readlines():
            emotion, count = line.strip().split(':')
            emotion_count[emotion] = int(count)

    # Plot emotions
    fig, ax = plt.subplots()
    ax.bar(emotion_count.keys(), emotion_count.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()


# Run output generation when this file is executed
plot_emotions('emotion_count.txt')
