# このコードは情報科学類22生の卒業に必要な単位を計算してくれるものです
# 他大学の単位認定など例外的なものには対応していません

import csv
import sys

#ファイルを開く
GradesFile = open(sys.argv[1], encoding="shift_jis")
GradesDictReader = csv.DictReader(GradesFile)

#変数の定義
kisoCommonMustCount = 0
kisoCommonSelectCountA = 0
kisoCommonSelectCountB = 0
kisoRelationCountA = 0
kisoRelationCountB = 0

senmonMustCount = 0
senmonSelectCountA = 0
senmonSelectCountB = 0

senmonkisoMustCount = 0
senmonkisoSelectCountA = 0
senmonkisoSelectCountB = 0
senmonkisoSelectCountC = 0
senmonkisoSelectCountD = 0

sotsugyouCount = 0

GradesList = ["A+", "A", "B", "C", "P"]
senmonkisoMustList = ["線形代数A", "線形代数B", "微分積分A", "微分積分B", "情報数学A", "専門基礎英語", 
                      "プログラミング入門A", "プログラミング入門B", "コンピュータとプログラミング",
                      "データ構造とアルゴリズム", "データ構造とアルゴリズム実験", "論理回路", "論理回路演習",
                      "線形代数1", "線形代数2", "微積分1", "微積分2"]
senmonkisoSelectListA = ["確率論", "統計学", "数値計算法", "論理と形式化", "論理システム", "論理システム演習"]
senmonkisoSelectListB = ["Computer Science in English A", "Computer Science in English B"]
kisoCommonList = ["ファーストイヤーセミナー", "学問への誘い", "情報リテラシー(講義)", "情報リテラシー(演習)", "データサイエンス",
                  "English Reading Skills I", "English Presentation Skills I",
                  "English Reading Skills II", "English Presentation Skills II"]
senmonMustList = ["ソフトウェアサイエンス実験A", "ソフトウェアサイエンス実験B", "情報システム実験A", "情報システム実験B",
                  "知能情報メディア実験A", "知能情報メディア実験B", "卒業研究A", "卒業研究B", "専門語学A", "専門語学B"]
senmonSelectList = ["情報科学特別演習", "情報特別演習I", "情報特別演習II"]

for dict in GradesDictReader:
  
  # 専門基礎科目(必修)の計算
  if dict["科目名 "] in senmonkisoMustList:
    if dict["総合評価"] in GradesList:
      senmonkisoMustCount += float(dict["単位数"])
  
  # 専門基礎科目(選択)の計算
  elif dict["科目名 "] in senmonkisoSelectListA:
    if dict["総合評価"] in GradesList:
      senmonkisoSelectCountA += float(dict["単位数"])

  elif dict["科目名 "] in senmonkisoSelectListB:
    if dict["総合評価"] in GradesList:
      senmonkisoSelectCountB += float(dict["単位数"])
  
  elif dict["科目番号"].startswith("GB1"):
    if dict["総合評価"] in GradesList:
      senmonkisoSelectCountC += float(dict["単位数"])

  elif dict["科目番号"].startswith("GA1") and dict["科目名 "] not in senmonSelectList:
    if dict["総合評価"] in GradesList:
      senmonkisoSelectCountD += float(dict["単位数"])
  
  # 専門科目(必修)の計算
  elif dict["科目名 "] in senmonMustList:
    if dict["総合評価"] in GradesList:
      senmonMustCount += float(dict["単位数"])

  # 専門科目(選択)の計算
  elif dict["科目番号"].startswith("GB20") or dict["科目番号"].startswith("GB30") or dict["科目番号"].startswith("GB40"):
    if dict["総合評価"] in GradesList:
      senmonSelectCountA += float(dict["単位数"])
  
  elif dict["科目番号"].startswith("GB2") or dict["科目番号"].startswith("GB3") or dict["科目番号"].startswith("GB4") or dict["科目番号"].startswith("GA4") or dict["科目名 "] in senmonSelectList:
    if dict["総合評価"] in GradesList:
      senmonSelectCountB += float(dict["単位数"])

  
  # 基礎科目(共通)の計算
  elif dict["科目名 "] in kisoCommonList or dict["科目名 "].startswith("基礎体育") or dict["科目名 "].startswith("応用体育"):
    if dict["総合評価"] in GradesList:
      kisoCommonMustCount += float(dict["単位数"])
  
  elif dict["科目番号"].startswith("12"):
    if dict["総合評価"] in GradesList:
      kisoCommonSelectCountA += float(dict["単位数"])
  
  elif dict["科目番号"].startswith("32") or dict["科目番号"].startswith("33") or dict["科目番号"].startswith("34") or dict["科目番号"].startswith("35") or dict["科目番号"].startswith("36") or dict["科目番号"].startswith("37") or dict["科目番号"].startswith("51") or dict["科目番号"].startswith("52") or dict["科目番号"].startswith("40"):
    if dict["総合評価"] in GradesList:
      kisoCommonSelectCountB += float(dict["単位数"])
  
  # 基礎科目(関連)の計算
  elif dict["科目番号"].startswith("A") or dict["科目番号"].startswith("B") or dict["科目番号"].startswith("C") or dict["科目番号"].startswith("D") or dict["科目番号"].startswith("W") or dict["科目番号"].startswith("Y"):
    if dict["総合評価"] in GradesList:
      kisoRelationCountA += float(dict["単位数"])

  elif dict["科目番号"].startswith("E") or dict["科目番号"].startswith("F") or dict["科目番号"].startswith("GC") or dict["科目番号"].startswith("GE") or dict["科目番号"].startswith("H"):
    if dict["総合評価"] in GradesList:
      kisoRelationCountB += float(dict["単位数"])

#ファイルを閉じる
GradesFile.close()
  
# 最大単位数があるものの調整
senmonSelectCountB = min(senmonSelectCountB, 18)
kisoCommonSelectCountB = min(kisoCommonSelectCountB, 4)
kisoRelationCountB = min(kisoRelationCountB, 4)

# 卒業要件の確認に必要な計算
MustCount = senmonMustCount + senmonkisoMustCount + kisoCommonMustCount
senmonSelectCount = min(senmonSelectCountA + senmonkisoSelectCountB, 34)
senmonkisoSelectCount = min(senmonkisoSelectCountA + senmonkisoSelectCountB + senmonkisoSelectCountC + senmonkisoSelectCountD, 26)
kisoCommonSelectCount = min(kisoCommonSelectCountA + kisoCommonSelectCountB, 5)
kisoRelationCount = min(kisoRelationCountA + kisoRelationCountB, 10)
SelectCount = senmonSelectCount + senmonkisoSelectCount + kisoCommonSelectCount + kisoRelationCount
sotsugyouCount = MustCount + SelectCount

MustCheck = MustCount == 54
senmonSelectACheck = senmonSelectCountA >= 16
senmonkisoSelectAcheck = senmonkisoSelectCountA >= 8
senmonkisoSelectBCheck = senmonkisoSelectCountB >= 2
senmonkisoSelectCCheck = senmonkisoSelectCountC >= 4
senmonkisoSelectDCheck = senmonkisoSelectCountD >= 8
kisoCommonSelectACheck = kisoCommonSelectCountA >= 1
kisoRelationACheck = kisoRelationCountA >= 6
sotsugyouCheck = MustCheck and senmonkisoSelectAcheck and senmonkisoSelectBCheck and senmonkisoSelectCCheck and senmonkisoSelectDCheck and kisoCommonSelectACheck and kisoRelationACheck



# 卒業要件の表示
print("(卒業要件確認項目：あなたの取得単位数 / 卒業に必要な単位数)")
print("【卒業要件】")
print(f'必修単位:{MustCount} / 54')
print(f'選択単位:{SelectCount} / 71')
print(f'合計    :{sotsugyouCount} / 125')
if sotsugyouCheck:
  print("あなたは卒業要件を満たしています")
else:
  print("あなたは卒業要件を満たしていません")

# 詳細の表示
print('【詳細】')

# 基礎科目の卒業要件確認
print(f'基礎共通科目(必修):{kisoCommonMustCount:5} / 12.0')
print(f'基礎共通科目(選択):{kisoCommonSelectCountA+kisoCommonSelectCountB:5} / 1.0~5.0')
print(f'学士基盤科目      :{kisoCommonSelectCountA:5} / 1.0~')
print(f'基礎関連科目      :{kisoRelationCountA+kisoRelationCountB:5} / 6.0~10.0')
print(f'文系科目          :{kisoRelationCountA:5} / 6.0~')

#　専門基礎科目の卒業要件確認
print(f'専門基礎科目(必修):{senmonkisoMustCount:5} / 26.0')
print(f'専門基礎科目(選択):{senmonkisoSelectCountA+senmonkisoSelectCountB+senmonkisoSelectCountC+senmonkisoSelectCountD:5} / 26.0')
print(f'専門基礎選択A     :{senmonkisoSelectCountA:5} / 8.0~')
print(f'専門基礎選択B     :{senmonkisoSelectCountB:5} / 2.0~')
print(f'専門基礎選択C     :{senmonkisoSelectCountC:5} / 4.0~')
print(f'専門基礎選択D     :{senmonkisoSelectCountD:5} / 8.0~')

# 専門科目の卒業要件確認
print(f'専門科目(必修)    :{senmonMustCount:5} / 16.0')
print(f'専門科目(選択)    :{senmonSelectCountA+senmonSelectCountB:5} / 34.0')
print(f'GB20,GB30,GB40から始まる科目:{senmonSelectCountA:5} / 16.0~')