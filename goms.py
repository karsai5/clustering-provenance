K = 0.2
P = 1.2
C = 0.2
H = 0.4
M = 1.35
R = 0

print("Goms example")
ctrlscore = H+K+M+P+C+R+M+P+C+R+M+P+C+R+M+P+C+R+R+M+K+P+C+R
print("Click Score: " + str(ctrlscore))
searchscore = H+M+C+R+M+P+C+H+M+K+K+K+K+K+K+K+K+K+K+K+K+K+K+K+R
print("Search Score:\t" + str(searchscore))

print("Select all child nodes in citizen science (40 nodes)")
ctrlscore = H+K+((M+P+C+R)*41)+R+M+K+P+C+R
print("Ctrl Score:\t" + str(ctrlscore))
searchscore = H+M+C+R+M+P+C+H+M+(K*22)+K+R
print("Search Score:\t" + str(searchscore))
