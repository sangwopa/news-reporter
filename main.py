import os
import logging
import argparse

def arg_parser():
    # 파서 설정
    parser = argparse.ArgumentParser(description="Argument Setting")
    parser.add_argument("--debug", action="store_true", help="activate debugging mode")
    args = parser.parse_args()
    
    return args
    



def main():
    print(1)
    




if __name__ == "__main__":
    main()