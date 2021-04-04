import secrets
import subprocess
import platform

def copy2clip(txt):
    if platform.system() == 'Darwin':
        cmd= f'echo "{txt.strip()}"|pbcopy'
    else:
        cmd= f'echo "{txt.strip()}"|clip'
    return subprocess.check_call(cmd, shell=True)

def main():
    pass_len = input('password len: ')
    p = secrets.token_urlsafe(int(pass_len))
    copy2clip(p)

    print(p)

if __name__ == '__main__':
    main()