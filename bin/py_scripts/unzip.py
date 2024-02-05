import zipfile
import argparse


def main(args_):
    if args_.zipfile:
        with zipfile.ZipFile(args_.zipfile, mode='r') as z_file:
            if args_.files:
                for i in z_file.namelist():
                    if args_.files.endswith('*'):
                        if i.startswith(args_.files[:-1]):
                            z_file.extract(i, args_.out)
                    else:
                        z_file.extract(i, args_.out)
            else:
                z_file.extractall(args.out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("zipfile", help="file to unpack",
                        type=str)
    parser.add_argument("--files", help="files of zip file to unpack",
                        type=str, default=None)
    parser.add_argument("--out", help="output of zip file to unpack",
                        type=str, default='.')
    args = parser.parse_args()
    main(args)
