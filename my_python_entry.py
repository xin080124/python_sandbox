
import argparse

def main():

    parser = argparse.ArgumentParser(description='Loading demo data')
    parser.add_argument('--argu_demo_1', help='Please provede argu_demo_1')
    parser.add_argument('--argu_demo_2', help='Please provede argu_demo_2')

    args = parser.parse_args()

    argu_demo_1 = args.argu_demo_1
    argu_demo_2 = args.argu_demo_2

    print("argu_demo", argu_demo_1, argu_demo_2)
    
if __name__ == '__main__':
    main()
