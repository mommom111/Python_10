scores = {
  '国語': 87, '数学': 86, '英語': 70, '理科': 73, '社会': 80
}

def scoreAvg(japanese, math, english):
  return (japanese + math + english) / 3

print(scoreAvg(87, 86, 70))

# def three_subject_avg(scores):
#   total_score = 0
#   for sbj, score in scores.items():
#     if sbj in ['国語', '数学', '英語']:
#       total_score += score
#   return total_score / 3

# result = three_subject_avg(scores)
# print(result)