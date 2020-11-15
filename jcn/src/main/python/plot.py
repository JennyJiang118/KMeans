import matplotlib.pyplot as plt


def read_data():
    data = []
    with open("/Users/osx/Desktop/2-4", "r") as f:
        for line in f:
            line = line.strip('\n')
            line = line.split("\t")
            #print(line[0])
            line = list(line[0].split(","))+list(line[1])
            line = list(map(int, line))

            data.append(line)
    return data

def plot(data):
    plt.figure(figsize=(12, 12))
    plt.xlabel('X')
    plt.ylabel('Y')

    x1=[]
    x2=[]
    y1=[]
    y2=[]

    for i in range(len(data)):
        if(data[i][2]==1):
            x1.append(data[i][0])
            y1.append(data[i][1])
        else:
            x2.append(data[i][0])
            y2.append(data[i][1])





    plt.scatter(x1, y1, c ="red", alpha=0.6, label = "category 1")
    plt.scatter(x2, y2, c ="blue", alpha=0.6, label = "category 2")

    plt.legend()
    plt.title("cluster num = 2, iteration = 4")
    plt.savefig(r'/Users/osx/Desktop/2-4')
    plt.show()







def main():
    data = read_data()
    plot(data)



if __name__ == '__main__':
    main()


#['86,43', '3']


