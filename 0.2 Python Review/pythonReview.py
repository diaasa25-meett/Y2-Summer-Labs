def create_youtube_video(title,description):
	vid={"title":title,'description':description,'likes':0,'dislikes':0,"comments":{}}
	return vid 
def likes(vid):
	if "likes" in vid: 
		vid["likes"]+=1
		return vid 
def dislikes(vid):
	if 'dislikes' in vid:
		vid["dislikes"]+=1
		return vid
def add_a_comment(Y_vid,username,comment_t):
	Y_vid["comments"][username]= comment_t
	return Y_vid
x= create_youtube_video("TRIPLET BLINDFOLDED COOKING CHALLENGE","*gone wrong*")	
print(495)
y= add_a_comment(x,"Lala","I wish I was in a TRIPLET </3")
print(y)
for i in range(495):
	y=likes(y)
print(y)	