import csv

print('ご指定された郵便番号を調べます')
ken = input('都道府県名を入れてください:')
city = input('市区町村名を入れてください:')
street = input('町城の指定があれば（わからない場合はインターキー）を入れてください:')

#データベースファイルを読み込む

kenall = open('KEN_ALL.CSV','r',encoding='shift-jis')
kenall_reader = csv.reader(kenall)

#データ抽出処理
zip_code = []   #検索した郵便番号のリスト

#一件ずつ読み込んで検索します。
for row in kenall_reader:
    if ken in row[6]:
        if city in row[7]:
            if street != '' and street in row[8]:
                zip_code.append(row[2])
            elif street == '':
                zip_code.append(row[2])
            else:
                continue
        else:
            continue
    else:
        continue
kenall.close()

if zip_code == []:
    zip_code = '見つかりませんでした。'

print('お探しの郵便番号の候補一覧です。：', zip_code)
