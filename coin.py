x = int(input("商品の金額を入力してください"))
n = int(input("入金する金額を入力をしてください"))
#お釣りを計算
change = n - x

#500円玉の数を計算
coin_500 = change // 500
change = change - 500 * coin_500

#100円玉の数を計算
coin_100 = change // 100
change = change - 100 * coin_100

#50円玉の数を計算
coin_50 = change // 50
change = change - 50 * coin_50

#10円玉の数を計算
coin_10 = change // 10
change = change - 10 * coin_10

#それぞれの小銭の数を表示
print(f"500円玉{coin_500}枚")
print(f"100円玉{coin_100}枚")
print(f"50円玉{coin_50}枚")
print(f"10円玉{coin_10}枚")