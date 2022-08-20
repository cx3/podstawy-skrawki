import json
import requests


def main():
    i = 37
    while 1:
        # https://kodpocztowy.intami.pl/api/57-360
        # postal: str = input('Write postal code:')
        i += 1
        s = str(i)
        postal = '0' * (5 - len(s)) + s
        print(postal)
        if i > 100:
            break

        while ' ' in postal:
            postal = postal.replace(' ', '')

        ok = True
        for ch in postal:
            if not ch.isdigit():
                if not ch == '-':
                    ok = False
        if not ok:
            print('# Error: signs must be digits or dash (-)')

        if postal.count('-') > 1:
            print('Incorrect postal')
            continue

        ok = False
        if 5 <= len(postal) < 7:
            if len(postal) == 6 and postal.count('-') == 1 and postal[2] == '-':
                ok = True
            else:
                ok = False
            if len(postal) == 5:
                postal = postal[:2] + '-' + postal[2:]
                ok = True


        if not ok:
            print('# Error: write postal code XX-XXX or XXXXX...')
            continue

        response = requests.get('https://kodpocztowy.intami.pl/api/' + postal).json()
        print(type(response))
        print(response)

        print(json.dumps(response, sort_keys=True, indent=2))

        data = json.dumps(response)

        open(postal + '.json', 'w').write(data)
        # break


if __name__ == '__main__':
    main()
