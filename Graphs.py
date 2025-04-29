import Bipartite, MongolianTent, Circulant

if __name__ == "__main__":
    run = True
    while run == True:
        print('Please select which graph you would like to create')
        print('1: Complete Bipartite Graph')
        print('2: Mongolian Tent Graph')
        print('3: Circulant Graph')
        print('Q: Quit')
        type = input()

        if type == '1':
            m = int(input('Please enter the value of m: '))
            n = int(input('Please enter the value of n: '))
            graph = Bipartite.BipartiteGraph(m, n)
            print("\n")
        elif type == '2':
            n = int(input('Please enter the number of vertices in the paths: '))
            graph = MongolianTent.MongolianTentGraph(n)
            print('\n')
        elif type == '3':
            n = int(input('Please enter the number of vertices for set V: '))
            graph = Circulant.CirculantGraph(n)
            print('\n')
        elif type == ('q' or 'Q'):
            run = False
        else:
            print('Please enter one of the provided options')

