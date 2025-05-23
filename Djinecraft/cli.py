import argparse
from Djinecraft.core.start_project import start_project
from Djinecraft.core.start_app import start_app

def main():
    parser = argparse.ArgumentParser(prog='djinecraft', description='Minecraft datapack preprocessor')

    subparsers = parser.add_subparsers(dest='command', required=True)

    # startproject command
    project_parser = subparsers.add_parser('startproject', help='Create a new Djinecraft project')
    project_parser.add_argument('name', help='Name of the project')

    # startapp command
    app_parser = subparsers.add_parser('startapp', help='Create a new Djinecraft app')
    app_parser.add_argument('name', help='Name of the app')

    args = parser.parse_args()

    if args.command == 'startproject':
        start_project(args.name)
    elif args.command == 'startapp':
        start_app(args.name)

if __name__ == "__main__":
    main()
