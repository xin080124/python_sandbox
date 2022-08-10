
import argparse

def main():

    parser = argparse.ArgumentParser(description='Loading demo data')
    parser.add_argument('--argu_demo', help='Please provede argu_demo')
    args = parser.parse_args()

    argu_demo = args.argu_demo

    print("argu_demo", argu_demo)
    
if __name__ == '__main__':
    main()
