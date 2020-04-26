import subprocess


def main():
    req = input("Enter commands= ")
    callCommand(req)


def callCommand(req):
    subprocess.run(req, shell=True)


if __name__ == '__main__':
    main()

