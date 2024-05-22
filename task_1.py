import os
import shutil
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Рекурсивно копіює файли з вихідної директорії до нової директорії, сортує за розширенням файлів.')
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dst_dir', type=str, nargs='?', default='dist',
                        help='Шлях до директорії призначення (за замовчуванням: dist)')
    return parser.parse_args()


def copy_files_recursively(src_dir, dst_dir):
    try:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[1][1:] or 'no_extension'
                new_dir = os.path.join(dst_dir, file_ext)
                os.makedirs(new_dir, exist_ok=True)
                shutil.copy2(file_path, os.path.join(new_dir, file))
    except Exception as e:
        print(f'Помилка при копіюванні файлів: {e}')


def main():
    args = parse_arguments()
    src_dir = os.path.abspath(args.src_dir)
    dst_dir = os.path.abspath(args.dst_dir)

    if not os.path.exists(src_dir):
        print(f'Вихідна директорія не існує: {src_dir}')
        return

    try:
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        copy_files_recursively(src_dir, dst_dir)
        print(f'Файли успішно скопійовані та відсортовані у директорії: {dst_dir}')
    except Exception as e:
        print(f'Помилка при створенні директорії призначення: {e}')


if __name__ == '__main__':
    main()
