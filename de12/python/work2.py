name="aaa"
waist=30
age=44

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=55:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")

# nameという変数にtanakaを代入
name="tanaka"
# waistという変数に55を代入
waist=55
# ageという変数に28を代入
age=28

print(name,"さんは腹囲",waist,"cmで年齢は",age,"才ですよー！")

if age>=40 and waist>=85:
    print(name,"さん、あなたはおじさんです")
else:
    print(name,"さん、あなたは若い")